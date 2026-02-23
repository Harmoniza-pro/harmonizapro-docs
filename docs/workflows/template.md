# <NOME DO WORKFLOW>

> **Arquivo n8n (export):** `workflows/exports/<arquivo>.json`  
> **Status:** Ativo/Inativo  
> **Owner:** <nome>  
> **Última revisão:** <YYYY-MM-DD>

## Objetivo

- O que esse workflow resolve, em 1–3 bullets.

## Quando roda (Trigger)

- Tipo: Webhook / Cron / Manual
- Endpoint (se webhook): `POST /<path>`
- Eventos de entrada: (ex.: mensagem recebida, lead novo, etc.)

## Entradas esperadas (Payload)

Exemplo mínimo:

```json
{
  "chat_id": "...",
  "sender": "...",
  "message": "...",
  "media": { "type": "...", "url": "..." }
}
```

## Saídas

O que ele gera/atualiza/envia (ex.: mensagem WhatsApp, gravação no Supabase, handoff, etc.)

## Regras de negócio

**Critérios de handoff:**

- <regra 1>
- <regra 2>

**Critérios de follow-up:**

- <regra 1>

**Tratamento de mídia (PDF/Vídeo/Áudio):**

- <regra 1>

## Integrações e dependências

**Supabase:**

- Tabelas tocadas: `<tabela>` (operação: insert/update/select)

**UaZapi:**

- Rotas usadas: `/send/text`, `/message/download` etc.

**Redis (se houver):**

- Chaves/padrões usados

**LLM (se houver):**

- Modelo, temperatura, limites, handoff/token checks

## Fluxo em alto nível (resumo)

1. Passo 1…
2. Passo 2…
3. Passo 3…

## Nós críticos (onde costuma quebrar)

| Nó | Motivo | Como detectar | Como corrigir |
|----|--------|--------------|---------------|
| <nome> | | | |

## Observabilidade (logs/monitoramento)

- O que logar
- Onde olhar erros (n8n executions, supabase logs, uazapi logs)

## Testes (casos)

**Caso 1 — Lead novo com mensagem simples**

- Input:
- Resultado esperado:

**Caso 2 — Mídia PDF**

- Input:
- Resultado esperado:

## Changelog

| Data | Mudança | Por quem |
|------|---------|----------|
| YYYY-MM-DD | | |
