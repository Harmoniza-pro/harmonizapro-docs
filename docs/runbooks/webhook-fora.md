# Runbook: Webhook Fora do Ar

## Sintoma

Mensagens do WhatsApp não estão chegando no n8n. Leads mandam mensagem e o agente não responde.

## Diagnóstico

1. **Verificar n8n:**
   - Acessar o painel do n8n
   - Ir em Executions → verificar se há execuções recentes
   - Se não há execuções → webhook não está recebendo

2. **Verificar UaZapi:**
   - Acessar painel do UaZapi
   - Verificar se o webhook está apontando para a URL correta do n8n
   - Verificar se a instância do WhatsApp está conectada (QR code)

3. **Verificar conectividade:**
   - Testar o endpoint com `curl`:
     ```bash
     curl -X POST https://SEU-N8N/webhook/harmonizapro \
       -H "Content-Type: application/json" \
       -d '{"test": true}'
     ```
   - Se retornar 404 → workflow não está ativo
   - Se retornar 500 → erro interno no workflow

## Resolução

| Causa | Solução |
|-------|---------|
| Workflow desativado | Ativar o workflow no n8n |
| URL do webhook mudou | Atualizar URL no UaZapi |
| WhatsApp desconectado | Reconectar escaneando QR code |
| n8n caiu/reiniciou | Verificar se o serviço está rodando |
| Rate limit UaZapi | Aguardar e verificar logs |

## Prevenção

- Configurar alerta se agente parar de funcionar (monitoramento)
- Verificar diariamente se há execuções recentes
