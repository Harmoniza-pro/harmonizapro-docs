# Workflows

Documentação técnica dos workflows n8n que compõem o sistema de qualificação de leads via WhatsApp da HarmonizaPRO.

---

## Visão Geral da Arquitetura

```
┌──────────────┐     ┌────────────────────┐     ┌──────────────────────┐
│  Typeform    │────▸│  Chamada Typeform  │────▸│    Agente de IA      │
│ (Formulário) │     │ (Registro + 1ª msg)│     │  (Conversa contínua) │
└──────────────┘     └────────────────────┘     └──────────┬───────────┘
                                                           │
                                              ┌────────────┼────────────┐
                                              ▼            ▼            ▼
                                        ┌──────────┐ ┌──────────┐ ┌──────────┐
                                        │  Tool    │ │  Follow  │ │ WhatsApp │
                                        │Transferir│ │   Ups    │ │ (UaZapi) │
                                        │ (Handoff)│ │(Reengaja)│ │          │
                                        └──────────┘ └──────────┘ └──────────┘
```

## Inventário

| Workflow | ID | Status | Trigger | Nós |
|:---------|:---|:-------|:--------|:----|
| [Agente de IA](agente-de-ia.md) | `8hdajgWAADbHorQF` | ✅ Ativo | Webhook POST | 92 |
| [Chamada Typeform](chamada-typeform.md) | `VPVYN9AzG8IGnKiR` | ✅ Ativo | Webhook POST | 29 |
| [Tool Transferir](tool-transferir.md) | `Gt60I1KPG4ReJSIe` | ✅ Ativo | Webhook POST | 12 |
| [Fluxo Follow Ups](fluxo-follow-ups.md) | `W1msnd1vZWkpFSDM` | ⚠️ Inativo | Schedule (11min) | 65 |

## Stack Tecnológica

| Camada | Tecnologia | Uso |
|:-------|:-----------|:----|
| Orquestração | n8n | Automação de workflows |
| IA Principal | Claude Sonnet 4 + GPT-5 | Agente conversacional + fallback |
| IA Contingência | Claude Sonnet 4.5 | Retry em caso de rate limit |
| IA Resumo | GPT-4o Mini | Resumo de conversas no handoff |
| Transcrição | OpenAI Whisper | Áudio → texto |
| Visão | OpenAI GPT-4o | Análise de imagens |
| Vídeo/Docs | Google Gemini | Análise de vídeo e documentos |
| WhatsApp | UaZapi | Envio e recebimento de mensagens |
| Banco de Dados | Supabase (PostgreSQL) | Leads, clínicas, memória, protocolos |
| Cache/Fila | Redis | Sistema de fila de mensagens |
| Formulário | Typeform | Captação de leads (Funil Anti-Curioso) |