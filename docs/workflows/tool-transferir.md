# Tool Transferir (Handoff IA → Hunter)

> **Arquivo n8n (export):** `workflows/exports/tool-transferir.json`  
> **Status:** 🟢 Ativo  
> **Owner:** <preencher>  
> **Última revisão:** <YYYY-MM-DD>

## Objetivo

- Executar handoff invisível do agente IA para a Hunter
- Notificar a Hunter com resumo da conversa
- Garantir que o lead não perceba a troca

## Quando roda (Trigger)

- Tipo: Chamado como sub-workflow / tool pelo Agente de IA
- Eventos de entrada: Critério de handoff atingido (3+ msgs engajamento, interesse em agendar, pergunta sem resposta, pedido de humano)

## Entradas esperadas

```json
{
  "lead_id": "...",
  "chat_id": "5511999999999@s.whatsapp.net",
  "motivo_handoff": "engajamento_3_msgs",
  "resumo_conversa": "Lead Maria, 45 anos, queixa de bigode chinês...",
  "hunter_telefone": "5511888888888"
}
```

## Saídas

- Notificação enviada para Hunter no WhatsApp
- Status do lead atualizado no Supabase (handoff = true)
- Agente para de responder mensagens desse lead

## Regras de negócio

- Lead NÃO pode perceber que houve troca
- Hunter recebe resumo completo da conversa
- Hunter assume no MESMO número de WhatsApp
- Antes do handoff, agente envia frase neutra ("um instante" ou similar)
- ⚠️ Problema atual: telefone da Hunter hardcoded — precisa ser dinâmico

## Integrações e dependências

**Supabase:**

- Update status do lead (handoff = true, hunter atribuída)

**UaZapi:**

- `POST /send/text` — notificação para Hunter

## Fluxo em alto nível

1. Recebe trigger de handoff do Agente de IA
2. Gera resumo da conversa
3. Atualiza status do lead no Supabase
4. Envia notificação para Hunter via WhatsApp
5. Marca conversa como "handoff realizado"

## Nós críticos

| Nó | Motivo | Como detectar | Como corrigir |
|----|--------|--------------|---------------|
| Dados do contato | Info incompleta causa falha | Notificação não chega | Validar campos antes do handoff |
| Telefone Hunter | Hardcoded no workflow | Só funciona pra 1 Hunter | Tornar dinâmico via Supabase |

## Testes

**Caso 1 — Handoff por engajamento**

- Input: Lead com 3+ mensagens engajadas
- Resultado esperado: Hunter notificada com resumo, lead não percebe

**Caso 2 — Handoff por pergunta sem resposta**

- Input: Lead faz pergunta que agente não sabe
- Resultado esperado: Handoff imediato, Hunter recebe contexto

## Changelog

| Data | Mudança | Por quem |
|------|---------|----------|
| | | |
