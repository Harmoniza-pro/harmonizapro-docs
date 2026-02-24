# Fluxo Follow Ups

> Workflow de reengajamento automático. Roda a cada 11 minutos, busca leads que não responderam e envia mensagens de follow-up progressivas, respeitando horário comercial.

| Campo | Valor |
|:------|:------|
| **ID** | `W1msnd1vZWkpFSDM` |
| **Status** | ✅ Ativo |
| **Trigger** | Schedule — a cada 11 minutos |
| **Nós** | 65 |
| **Trigger alternativo** | Manual (botão "Execute workflow") |

---

## Objetivo

Reengajar leads que pararam de responder. O workflow roda automaticamente a cada 11 minutos, identifica leads elegíveis para follow-up e envia mensagens progressivas. Cada follow-up é uma "rodada" com critérios diferentes de tempo e conteúdo.

---

## Arquitetura Geral

O workflow tem **4 rodadas de follow-up paralelas**, cada uma com seus próprios critérios de elegibilidade. Todas rodam simultaneamente a cada execução.

```
Schedule (a cada 11 min)
    │
    ▼
Verificar Horário Comercial
    │
    ├── Fora do horário → Para
    │
    └── Dentro do horário → Buscar dados UaZapi
                             │
                             ▼
                    ┌────────┼────────┬────────┐
                    ▼        ▼        ▼        ▼
                 FUP 1    FUP 2    FUP 3    FUP 4
                (rodada) (rodada) (rodada) (rodada)
                    │        │        │        │
                    └────────┼────────┴────────┘
                             ▼
                    Juntar todos que receberam
                             │
                             ▼
                    Salvar lista de telefones
```

---

## Horário Comercial

Antes de executar qualquer follow-up, o sistema verifica:

### Verificação em 3 etapas:

1. **Horário Comercial?** (Switch) — Verifica se estamos dentro do horário de operação
2. **Hoje é sábado?** (Filter) — Tratamento especial para sábados (horário reduzido ou sem follow-up)
3. **Verificar horário comercial** (Filter) — Validação final

Se **fora do horário** → a execução é ignorada silenciosamente. O scheduler roda de novo em 11 minutos.

---

## Estrutura de Cada Rodada (FUP)

Cada rodada segue o mesmo padrão com 8 nós:

```
Controle - fup{N}           → Define critérios (qual follow-up, tempo mínimo)
    │
    ▼
Buscar - fup{N}             → Consulta leads elegíveis (Supabase: leads, getAll)
    │
    ▼
Filtro{N}                   → Filtra por critérios específicos da rodada
    │
    ▼
Remover duplicados{N}       → Evita enviar para o mesmo lead duas vezes
    │
    ▼
Enviar mensagem{N}          → POST via UaZapi (/send/text)
    │
    ├── Marcar fup - true{N} → Atualiza flag no Supabase (leads, update)
    │
    └── Preparar p/ salvar{N} → Formata mensagem
            │
            ▼
        Inserir msg na memória{N} → Salva na n8n_chat_histories
```

### Envio da Mensagem

```
POST {URL Base}/send/text
Headers:
  token: {token}
Body:
  number: {telefone_do_lead}
  text: {mensagem_de_follow_up}
```

### Pós-envio (dupla ação)

Após enviar cada follow-up, duas coisas acontecem em paralelo:

1. **Marca follow-up** — Atualiza a tabela `leads` para registrar que o lead recebeu aquela rodada
2. **Salva na memória** — Insere a mensagem na `n8n_chat_histories` para que o Agente de IA tenha contexto se o lead responder depois

---

## Rodadas de Follow-Up

| Rodada | Nó de controle | Critério de elegibilidade | Tipo de mensagem |
|:-------|:---------------|:--------------------------|:-----------------|
| **FUP 1** | `Controle - fup` | Lead não respondeu após 1ª abordagem | Lembrete gentil |
| **FUP 2** | `Controle - fup1` | Lead não respondeu após FUP 1 | Reforço de valor |
| **FUP 3** | `Controle - fup2` | Lead não respondeu após FUP 2 | Urgência/escassez |
| **FUP 4** | `Controle - fup3` | Lead não respondeu após FUP 3 | Última tentativa |

!!! info "Nota"
    Os critérios exatos de tempo entre cada rodada (ex: 24h, 48h, 72h) são definidos nos nós de `Controle` e `Filtro` de cada rodada. Consulte os parâmetros no n8n para os valores atuais.

---

## Consolidação Final

Depois que todas as 4 rodadas terminam, o sistema:

1. **Juntar todos que receberam** — Merge das 4 saídas
2. **Concatenar** — Junta todos os telefones que receberam follow-up nesta execução
3. **Salvar lista** — Registra no `executionData` para auditoria

---

## Dados UaZapi

O nó **Dados Uazapi** fornece os dados da instância WhatsApp para todas as 4 rodadas:

- `URL Base` — URL do servidor UaZapi
- `Token` — Token de autenticação

---

## Tabelas Supabase

| Tabela | Operação | Finalidade |
|:-------|:---------|:-----------|
| `leads` | getAll, update | Buscar leads elegíveis + marcar follow-up enviado |
| `n8n_chat_histories` | create | Salvar mensagem de follow-up na memória do agente |

---

## Credenciais

| Serviço | Credential |
|:--------|:-----------|
| Supabase | `ferramentas@harmoniza.pro` |

---

## Regras de Negócio

1. **Horário comercial obrigatório** — Follow-ups nunca são enviados fora do horário
2. **Sábados** — Tratamento especial (pode ter horário reduzido ou nenhum envio)
3. **Anti-duplicidade** — Cada rodada remove duplicados antes de enviar
4. **Memória** — Toda mensagem de follow-up é salva no histórico para dar contexto ao Agente de IA
5. **Progressão** — As 4 rodadas são sequenciais por lead (FUP 1 → 2 → 3 → 4), mas executadas em paralelo para diferentes leads
6. **Frequência** — O scheduler roda a cada 11 minutos, mas cada lead só recebe 1 follow-up por rodada

---

## Status Atual

!!! warning "Workflow inativo"
    Este workflow está **desativado** no n8n (`active: true`). Precisa ser ativado manualmente quando estiver pronto para produção. Pode ser testado usando o trigger manual "When clicking 'Execute workflow'".

---

## Troubleshooting

| Problema | Causa provável | Solução |
|:---------|:---------------|:--------|
| Follow-ups não estão sendo enviados | Workflow inativo | Ativar no n8n |
| Lead recebeu follow-up fora do horário | Lógica de horário comercial falhou | Checar nós "Horário Comercial?" e filtros |
| Lead recebeu o mesmo follow-up 2x | Remoção de duplicados falhou | Verificar nó "Remover duplicados" |
| Agente não tem contexto do follow-up | Inserção na memória falhou | Checar nós "Preparar p/ salvar" e "Inserir msg na memória" |
| Follow-up enviado para lead transferido | Filtro não exclui transferidos | Adicionar condição `transferido != true` nos filtros |