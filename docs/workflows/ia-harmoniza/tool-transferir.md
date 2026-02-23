# Tool Transferir (Handoff IA → Hunter)

> Workflow acionado pelo Agente de IA quando o lead está pronto para ser atendido por um humano. Realiza o handoff invisível, gera um resumo da conversa e notifica a Hunter.

| Campo | Valor |
|:------|:------|
| **ID** | `Gt60I1KPG4ReJSIe` |
| **Status** | ✅ Ativo |
| **Trigger** | Webhook POST `/handoff-agenteia` |
| **Nós** | 12 |
| **IA** | GPT-4o Mini (resumo da conversa) |

---

## Objetivo

Transferir o atendimento do Agente de IA para a Hunter de forma invisível para o lead. A Hunter recebe uma notificação no WhatsApp com o telefone do lead, o motivo da transferência e (quando disponível) um resumo da conversa.

---

## Como é Acionado

Este workflow **não é chamado diretamente por um usuário**. Ele é uma **tool do Agente de IA**.

Quando o Agente decide que o lead precisa de um humano (ex: quer agendar, fez pergunta que o agente não sabe responder, pediu para falar com alguém), ele chama a tool `transferir` que faz um POST para este webhook:

```
POST https://webhooks.goldeletra.pro/webhook/handoff-agenteia
Body:
  telefone: "558399XXXXXXX"
  motivo: "Lead insistiu em agendar agora"
```

---

## Fluxo Completo

```
Webhook POST /handoff-agenteia
    │
    ├──────────────────────────────────────┐
    │                                      ▼
    ▼                            Transferido = true
Buscar ID da Clínica             (atualiza flag no Supabase)
(Supabase: leads)
    │
    ▼
Buscar Hunter
(Supabase: clinicas_com_atendentes)
    │
    ▼
Buscar dados da instância
(Supabase: instancias_whatsapp)
    │
    ▼
Buscar histórico da conversa
(Supabase: n8n_chat_histories)
    │
    ▼
Encontrou histórico?
    │
    ├── NÃO → Handoff SEM resumo
    │         (envia telefone + motivo para Hunter)
    │
    └── SIM → Organizar mensagens
              │
              ▼
         Concatenar todas as msgs
              │
              ▼
         GPT-4o Mini gera resumo (máx 50 palavras)
              │
              ▼
         Handoff COM resumo
         (envia telefone + motivo + resumo para Hunter)
```

---

## Fase 1 — Busca de Dados

### Buscar ID da Clínica

Consulta a tabela `leads` pelo `remotejid` (telefone) para descobrir o `clinica_id` e `instancia_id`.

### Buscar Hunter

Com o `clinica_id`, consulta `clinicas_com_atendentes` para encontrar o telefone da Hunter responsável.

### Buscar Dados da Instância

Com o `instancia_id`, consulta `instancias_whatsapp` para obter a URL do servidor UaZapi e o token de autenticação.

---

## Fase 2 — Flag de Transferência

**Em paralelo** com a busca de dados, o webhook já atualiza a tabela `leads`:

```sql
UPDATE leads
SET transferido = true,
    handoff_enviado = true,
    handoff_at = NOW()
WHERE remotejid = '{telefone}'
```

Isso garante que o **Agente de IA para de responder imediatamente** — antes mesmo do handoff ser enviado para a Hunter.

---

## Fase 3 — Resumo da Conversa

### Buscar Histórico

Consulta a tabela `n8n_chat_histories` pelo `session_id` (telefone). Retorna todas as mensagens trocadas entre o agente e o lead.

### Encontrou Histórico?

| Resultado | Caminho |
|:----------|:--------|
| Sem histórico | Handoff simples (só telefone + motivo) |
| Com histórico | Gera resumo com IA antes do handoff |

### Geração do Resumo

Se há histórico, o fluxo:

1. **Organizar mensagens** — Formata cada mensagem como `{tipo}: {conteúdo}`
2. **Concatenar** — Junta todas as mensagens em um único texto
3. **GPT-4o Mini** — Gera um resumo objetivo de no máximo 50 palavras

**System prompt do resumo:**

> "Você é um especialista em resumir conversas. Crie um resumo da transcrição de conversa de WhatsApp acima. Seu resumo deve ter no máximo 50 palavras. Seja objetivo."

---

## Fase 4 — Notificação da Hunter

### Handoff COM resumo

```
POST {server_url}/send/text
Body:
  number: "+5583996618397"
  text: |
    *LEAD TRANSFERIDO 🚨*
    -------------------------
    *Telefone:* wa.me/{telefone}
    *Motivo:* {motivo}
    *Resumo:* {resumo_da_conversa}
```

### Handoff SEM resumo

```
POST {server_url}/send/text
Body:
  number: "+55839794857"
  text: |
    *LEAD TRANSFERIDO 🚨*
    -------------------------
    *Telefone:* wa.me/{telefone}
    *Motivo:* {motivo}
```

!!! warning "Atenção: Telefones Hardcoded"
    Os telefones das Hunters estão **hardcoded** nos nós HTTP Request. Isso é um problema conhecido — no futuro, o telefone deve vir dinamicamente da tabela `clinicas_com_atendentes`.

---

## Tabelas Supabase

| Tabela | Operação | Finalidade |
|:-------|:---------|:-----------|
| `leads` | get, update | Buscar clínica + marcar como transferido |
| `clinicas_com_atendentes` | get | Encontrar a Hunter da clínica |
| `instancias_whatsapp` | get | URL e token do servidor UaZapi |
| `n8n_chat_histories` | get | Histórico da conversa para resumo |

---

## Credenciais

| Serviço | Credential |
|:--------|:-----------|
| Supabase | `ferramentas@harmoniza.pro` |
| OpenAI | `ferramentas@harmoniza.pro` |

---

## Critérios de Handoff

O Agente de IA decide transferir quando:

1. **Lead quer agendar** — Demonstrou interesse claro em marcar consulta
2. **Pergunta desconhecida** — Agente não tem informação para responder
3. **Pediu humano** — Lead explicitamente pediu para falar com alguém
4. **3+ mensagens engajadas** — Lead está aquecido e engajado na conversa

---

## Troubleshooting

| Problema | Causa provável | Solução |
|:---------|:---------------|:--------|
| Hunter não recebe notificação | Telefone hardcoded incorreto | Verificar nós "Handoff com/sem resumo" |
| Lead continua recebendo msgs do agente | Flag `transferido` não setou | Verificar nó "Transferido = true" e execução |
| Resumo vazio | Sem histórico na `n8n_chat_histories` | Verificar se a memória está sendo salva no Agente de IA |
| Handoff sem motivo | Tool `transferir` chamada sem motivo | Verificar prompt do Agente — deve exigir motivo |
| Erro no webhook | URL do webhook mudou | Checar se o Agente aponta para `/webhook/handoff-agenteia` |