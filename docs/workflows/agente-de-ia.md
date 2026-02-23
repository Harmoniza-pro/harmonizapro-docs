# Agente de IA (Entrada Principal)

> **Arquivo n8n (export):** `workflows/exports/agente-de-ia.json`  
> **Status:** 🟢 Ativo  
> **Owner:** <preencher>  
> **Última revisão:** <YYYY-MM-DD>

## Objetivo

- Receber mensagens de leads via WhatsApp (UaZapi webhook)
- Processar com Claude para gerar resposta natural de qualificação
- Enviar resposta via WhatsApp e registrar no Supabase

## Quando roda (Trigger)

- Tipo: Webhook
- Endpoint: `POST /harmonizapro`
- Eventos de entrada: Mensagem recebida no WhatsApp via UaZapi

## Entradas esperadas (Payload)

```json
{
  "chat_id": "5511999999999@s.whatsapp.net",
  "sender": "5511999999999",
  "message": "Oi, preenchi o formulário...",
  "media": null
}
```

## Saídas

- Mensagem de resposta enviada via WhatsApp (UaZapi `/send/text`)
- Registro da conversa no Supabase
- Trigger de handoff quando lead qualificado

## Regras de negócio

**Critérios de handoff:**

- Lead respondeu 3+ mensagens COM engajamento → handoff
- Lead demonstrou interesse em agendar → handoff
- Lead fez pergunta que agente não sabe → handoff imediato
- Lead pediu pra falar com humano → handoff imediato

**Limitações do agente:**

- NÃO prometer desconto
- NÃO agendar consulta
- NÃO passar preço
- NÃO falar de procedimentos fora do protocolo

**Humanização da resposta:**

- Máximo 2-3 frases por mensagem
- Emoji ocasional (máximo 1 por mensagem)
- Sem padrões robóticos (repetição, caps excessivo)
- Quebra de mensagem em fronteiras naturais de frase

## Integrações e dependências

**Supabase:**

- <preencher tabelas após rodar generate_docs.py>

**UaZapi:**

- `POST /send/text` — envio de mensagens
- <preencher demais rotas>

**LLM (Claude):**

- Modelo: Claude (via n8n AI Agent node)
- Prompt otimizado: ~1.070 palavras (reduzido de 4.500)
- Proteção contra split de abreviações PT-BR (Dra., Dr., Sr., Sra.)

## Fluxo em alto nível

1. Webhook recebe mensagem do UaZapi
2. Busca dados do lead no Supabase
3. Monta contexto (histórico + dados do formulário + dados da clínica)
4. Envia para Claude processar
5. Quebra resposta em mensagens naturais
6. Envia via UaZapi com typing indicators
7. Salva conversa no Supabase
8. Verifica critérios de handoff

## Nós críticos

| Nó | Motivo | Como detectar | Como corrigir |
|----|--------|--------------|---------------|
| Webhook | Se UaZapi mudar payload | Erro 400 no n8n | Verificar formato do payload |
| Supabase (busca lead) | Dados incompletos do contato | Handoff falha | Garantir campos obrigatórios preenchidos |
| HTTP Request (UaZapi) | Rate limit ou server down | Timeout / 429 | Retry com backoff |
| AI Agent (Claude) | Token limit / resposta longa | Mensagem cortada | Ajustar max_tokens |

## Testes

**Caso 1 — Lead novo com mensagem simples**

- Input: "Oi, preenchi o formulário"
- Resultado esperado: Agente cumprimenta pelo nome, menciona dados do form, faz primeira pergunta

**Caso 2 — Lead pergunta preço**

- Input: "Quanto custa?"
- Resultado esperado: Resposta padrão de redirecionamento (investimento varia, consulta avalia)

**Caso 3 — Lead pede desconto**

- Input: "Tem desconto?"
- Resultado esperado: Resposta padrão de valor do protocolo

**Caso 4 — Lead com budget alto no form**

- Input: Qualquer mensagem, budget = alto
- Resultado esperado: Handoff direto para Hunter

## Changelog

| Data | Mudança | Por quem |
|------|---------|----------|
| | Criação do workflow | |
