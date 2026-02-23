# Chamada Typeform

> **Arquivo n8n (export):** `workflows/exports/chamada-typeform.json`  
> **Status:** 🟢 Ativo  
> **Owner:** <preencher>  
> **Última revisão:** <YYYY-MM-DD>

## Objetivo

- Receber submissões do formulário Anti-Curioso (Typeform)
- Criar/atualizar registro do lead no Supabase
- Disparar primeira mensagem personalizada via WhatsApp em < 2 min

## Quando roda (Trigger)

- Tipo: Webhook (Typeform)
- Endpoint: <preencher>
- Eventos de entrada: Formulário preenchido pelo lead

## Entradas esperadas (Payload)

Dados do Typeform:

```json
{
  "nome": "Maria Silva",
  "telefone": "5511999999999",
  "protocolo": "Protocolo RR",
  "procedimento_anterior": "Botox",
  "budget": "alto",
  "incomodo_rosto": "Bigode chinês e flacidez"
}
```

## Saídas

- Registro do lead criado no Supabase
- Primeira mensagem personalizada enviada via WhatsApp
- Se budget = ALTO → handoff direto para Hunter (sem agente)

## Regras de negócio

- Se budget = ALTO no formulário → Hunter entra direto (bypass do agente)
- Se budget ≠ ALTO → Agente IA inicia conversa
- Mensagem inicial deve usar dados do formulário (nome, incômodo, procedimento anterior)
- Tempo máximo entre form preenchido e primeira mensagem: < 2 minutos

## Integrações e dependências

**Typeform:**

- Webhook de submissão

**Supabase:**

- Insert em tabela de leads
- <preencher tabelas>

**UaZapi:**

- `POST /send/text` — primeira mensagem

## Fluxo em alto nível

1. Typeform envia webhook com dados do formulário
2. n8n extrai e formata dados
3. Verifica se lead já existe no Supabase
4. Cria/atualiza registro do lead
5. Verifica budget (ALTO = Hunter direto)
6. Monta mensagem inicial personalizada
7. Envia via UaZapi

## Nós críticos

| Nó | Motivo | Como detectar | Como corrigir |
|----|--------|--------------|---------------|
| Webhook Typeform | Formato do payload pode mudar | Campos faltando | Verificar mapeamento |
| Supabase insert | Telefone duplicado | Erro de constraint | Usar upsert |

## Testes

**Caso 1 — Lead novo com budget normal**

- Input: Form completo, budget = normal
- Resultado esperado: Lead criado no Supabase + msg personalizada enviada

**Caso 2 — Lead com budget ALTO**

- Input: Form completo, budget = alto
- Resultado esperado: Lead criado no Supabase + handoff direto para Hunter

## Changelog

| Data | Mudança | Por quem |
|------|---------|----------|
| | | |
