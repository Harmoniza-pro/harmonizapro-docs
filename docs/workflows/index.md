# Índice de Workflows

Documentação técnica de cada workflow n8n do sistema HarmonizaPRO.

| Workflow | Função | Status |
|----------|--------|--------|
| [Agente de IA](agente-de-ia.md) | Workflow principal — recebe mensagens, processa com Claude, responde via WhatsApp | 🟢 Ativo |
| [Chamada Typeform](chamada-typeform.md) | Recebe submissão do formulário e inicia outreach | 🟢 Ativo |
| [Tool Transferir](tool-transferir.md) | Gerencia handoff de IA para Hunter | 🟢 Ativo |

## Como gerar docs automaticamente

Se você exportou um workflow novo do n8n:

1. Salve o JSON em `workflows/exports/`
2. Rode `python tools/generate_docs.py`
3. O esqueleto do doc será gerado em `docs/workflows/`
4. Preencha as partes humanas (objetivo, regras, testes)
