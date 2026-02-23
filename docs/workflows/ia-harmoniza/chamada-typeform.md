# Chamada Typeform

> Workflow de entrada de leads. Recebe submissões do Typeform (Funil Anti-Curioso), registra o lead no Supabase e envia a primeira mensagem via WhatsApp.

| Campo | Valor |
|:------|:------|
| **ID** | `VPVYN9AzG8IGnKiR` |
| **Status** | ✅ Ativo |
| **Trigger** | Webhook POST `/typeform/hamoniza.pro` |
| **Nós** | 29 |

---

## Objetivo

Capturar leads que preencheram o formulário Typeform (Funil Anti-Curioso), registrar no banco de dados, e enviar a primeira abordagem no WhatsApp em menos de 2 minutos. Leads com budget alto são encaminhados diretamente para a Hunter.

---

## Fluxo Completo

```
Typeform (submissão do formulário)
    │
    ▼
Webhook POST /typeform/hamoniza.pro
    │
    ▼
Wait (pequeno delay)
    │
    ▼
Organizar informações (nome, telefone, budget, clínica)
    │
    ▼
Puxar dados UaZapi (instância WhatsApp)
    │
    ▼
Buscar Usuário (já existe na base?)
    │
    ▼
Anti-duplicidade (evitar reprocessamento)
    │
    ▼
Novo usuário?
    ├── SIM → Criar lead no Supabase
    │         │
    │         ▼
    │    Budget alto?
    │    ├── SIM → Atualizar lead + Buscar clínica/protocolo
    │    │         │
    │    │         ▼
    │    │    IA gera msg de handoff direto
    │    │         │
    │    │         ▼
    │    │    Enviar alerta para Hunter
    │    │
    │    └── NÃO → Buscar clínica/protocolo
    │              │
    │              ▼
    │         IA gera primeira mensagem personalizada
    │              │
    │              ▼
    │         Dividir mensagem + Enviar via WhatsApp
    │              │
    │              ▼
    │         Enviar alerta para Hunter
    │
    └── NÃO (lead já existe) → Buscar clínica/protocolo
                                │
                                ▼
                           IA gera msg considerando histórico
                                │
                                ▼
                           Enviar alerta para Hunter
```

---

## Entrada (Webhook)

**Endpoint:** `POST /typeform/hamoniza.pro`

Recebe o payload do Typeform contendo as respostas do formulário Anti-Curioso.

---

## Fase 1 — Organização dos Dados

### Wait

Pequeno delay após receber o webhook para garantir que os dados estejam completos.

### Info Organizadas

Extrai e padroniza os campos do Typeform: nome, telefone, faixa de budget, clínica de origem, respostas relevantes.

### Puxar Background

Busca na tabela `instancias_whatsapp` os dados da instância UaZapi da clínica (URL do servidor, token). Necessário para enviar mensagens via WhatsApp.

---

## Fase 2 — Verificação de Duplicidade

### Buscar Usuário

Consulta a tabela `leads` pelo telefone do lead. Verifica se já existe cadastro.

### Anti-duplicidade

Nó `code` que previne reprocessamento — se o mesmo formulário for enviado duas vezes, não cria lead duplicado.

### Novo Usuário?

| Resultado | Caminho |
|:----------|:--------|
| Lead novo | Cria registro → Avalia budget → Envia msg |
| Lead existente | Busca dados atuais → Gera msg com contexto → Alerta Hunter |

---

## Fase 3 — Avaliação de Budget

### Budget Alto?

Se o lead informou budget alto no Typeform, ele é considerado **prioridade** e vai direto para a Hunter.

| Budget | Ação |
|:-------|:-----|
| **Alto** | Atualiza lead no Supabase + IA gera mensagem de encaminhamento + Alerta direto para Hunter |
| **Normal/Baixo** | IA gera primeira abordagem personalizada + Lead entra no fluxo normal do Agente |

---

## Fase 4 — Geração da Primeira Mensagem com IA

### Para budget normal (Agente principal)

O nó **AI Agent** usa **OpenAI** para gerar a primeira mensagem de abordagem.

Antes de gerar, busca:

- **Clínica** (`clinicas_com_atendentes`) — nome, posicionamento
- **Protocolo** (`protocolos`) — nome do protocolo, descrição

Isso permite que a mensagem seja **personalizada** por clínica.

### Para budget alto (Handoff direto)

O nó **AI Agent1** usa **Anthropic (Claude)** para gerar uma mensagem de handoff que a Hunter recebe junto com os dados do lead.

### Para lead existente

Quando o lead já existe, o sistema busca a clínica e protocolo e gera uma mensagem considerando que é um retorno.

---

## Fase 5 — Envio da Mensagem

### Dividir Mensagem

O nó `code` **Dividir Mensagem** quebra a resposta da IA em múltiplas mensagens se necessário, para parecer mais natural no WhatsApp.

### Envio em Loop

O `splitInBatches` (Loop Over Items) envia cada mensagem individualmente via UaZapi:

```
POST {server_url}/send/text
Headers:
  token: {token}
Body:
  number: {telefone_do_lead}
  text: {mensagem}
```

### Alerta para Hunter

Independente do budget, a Hunter sempre recebe um alerta via WhatsApp com os dados do novo lead:

```
POST {server_url}/send/text
Body:
  number: {telefone_hunter}
  text: "🚨 Novo lead: {nome} - {telefone} - Budget: {budget}"
```

---

## Tabelas Supabase

| Tabela | Operação | Finalidade |
|:-------|:---------|:-----------|
| `leads` | create, get, update | Cadastro e consulta de leads |
| `instancias_whatsapp` | get | Dados do servidor UaZapi |
| `clinicas_com_atendentes` | get | Dados da clínica e Hunter |
| `protocolos` | get | Protocolo da clínica |

---

## Credenciais

| Serviço | Credential |
|:--------|:-----------|
| Supabase | `ferramentas@harmoniza.pro` |
| OpenAI | `ferramentas@harmoniza.pro` |
| Anthropic | `ferramentas@harmoniza.pro` |

---

## Regras de Negócio

1. **Tempo de resposta** — A primeira mensagem deve chegar em menos de 2 minutos após o formulário ser preenchido
2. **Anti-duplicidade** — Um lead que preencher o formulário duas vezes não é recadastrado
3. **Budget alto** — Lead com budget alto pula a qualificação e vai direto para Hunter
4. **Personalização** — Toda mensagem é gerada com contexto da clínica e protocolo específicos
5. **Alerta obrigatório** — Hunter sempre recebe notificação de novo lead, independente do budget

---

## Troubleshooting

| Problema | Causa provável | Solução |
|:---------|:---------------|:--------|
| Lead não recebe mensagem | Webhook do Typeform não está apontando | Verificar URL no Typeform: `.../webhook/typeform/hamoniza.pro` |
| Lead duplicado | Anti-duplicidade falhou | Checar nó "Anti-duplicidade" e lógica de verificação |
| Mensagem genérica | Clínica/protocolo não encontrados | Verificar se `clinica_id` está correto no lead |
| Hunter não recebe alerta | Telefone da Hunter errado | Checar tabela `clinicas_com_atendentes` |
| Demora > 2min | Wait muito longo ou fila no n8n | Verificar execuções pendentes no n8n |