# HarmonizaPRO — Documentação

Repositório central de documentação dos workflows n8n, integrações (Supabase, UaZapi, Claude), regras de handoff e base de conhecimento das clínicas.

## Visão Geral do Sistema

O HarmonizaPRO é um sistema de agente de IA para qualificação de leads via WhatsApp, voltado para clínicas de harmonização facial. O agente conversa com leads, qualifica, aquece e entrega para a Hunter apenas leads prontos para agendar.

## Arquitetura

```
Typeform (formulário) 
    → n8n (orquestração) 
        → Claude (IA / cérebro do agente)
        → UaZapi (WhatsApp API)
        → Supabase (banco de dados)
```

## Navegação Rápida

| Seção | O que encontrar |
|-------|----------------|
| [PRD 001](prd-001-agente-qualificacao.md) | Documento de requisitos completo do agente |
| [Workflows](workflows/index.md) | Documentação técnica de cada workflow n8n |
| [Playbooks](playbooks/index.md) | Procedimentos operacionais (como abordar, como responder) |
| [Runbooks](runbooks/index.md) | Troubleshooting e incidentes |
| [Base de Conhecimento](base-conhecimento-clinicas.md) | Dados das clínicas e protocolos |

## Status do Projeto

| Fase | Entrega | Status |
|------|---------|--------|
| Fase 0 | Base de conhecimento | 🟡 Em progresso |
| MVP | Agente básico (conversa + qualificação + handoff) | 🟡 Em progresso |
| V2 | Follow-ups automáticos (5 msgs / 7 dias) | ⚪ Pendente |
| V3 | Handoff inteligente (critérios automáticos) | ⚪ Pendente |
| V4 | Integração ClickUp (PRD 3) | ⚪ Pendente |
