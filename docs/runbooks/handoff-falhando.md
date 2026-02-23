# Runbook: Handoff Falhando

## Sintoma

O agente qualifica o lead, mas a Hunter não recebe notificação e/ou o lead não é transferido corretamente.

## Diagnóstico

1. **Verificar execução do workflow Tool Transferir:**
   - Acessar n8n → Executions
   - Filtrar por workflow "Tool Transferir"
   - Verificar se há erros na execução

2. **Verificar dados do contato:**
   - No Supabase, buscar o lead
   - Verificar se os campos obrigatórios estão preenchidos (telefone, nome, chat_id)
   - ⚠️ **Problema conhecido:** Dados incompletos do contato causam falha no handoff

3. **Verificar telefone da Hunter:**
   - ⚠️ **Problema conhecido:** Telefone da Hunter está HARDCODED no workflow
   - Verificar se o número está correto

4. **Verificar envio da notificação:**
   - No n8n, verificar a execução do nó HTTP Request que envia para UaZapi
   - Verificar se o status foi 200

## Resolução

| Causa | Solução |
|-------|---------|
| Dados do contato incompletos | Preencher dados faltantes no Supabase |
| Telefone da Hunter hardcoded errado | Corrigir no workflow (temporário) / tornar dinâmico (permanente) |
| UaZapi falhou no envio | Verificar logs do UaZapi, reenviar manualmente |
| Workflow Tool Transferir desativado | Ativar o workflow |

## Workaround manual

Se o handoff falhar, a Hunter pode ser notificada manualmente:

1. Acessar Supabase → tabela de leads
2. Buscar o lead
3. Copiar resumo da conversa
4. Enviar manualmente para a Hunter

## Prevenção

- Tornar telefone da Hunter dinâmico (buscar do Supabase por clínica)
- Validar dados do contato ANTES de tentar handoff
- Adicionar retry automático em caso de falha no envio
