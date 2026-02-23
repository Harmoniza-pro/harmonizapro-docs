# HarmonizaPRO — Documentação

Central de documentação dos workflows n8n, integrações (Supabase, UaZapi, Claude), regras de handoff e base de conhecimento das clínicas.

---

## Visão Geral

O **HarmonizaPRO** é um sistema de agente de IA para qualificação de leads via WhatsApp, voltado para clínicas de harmonização facial. O agente conversa com leads, qualifica, aquece e entrega para a Hunter apenas leads prontos para agendar.

| Número | Item |
|:------:|:-----|
| **3** | Workflows documentados |
| **5** | Clínicas cadastradas |
| **2** | Playbooks operacionais |
| **2** | Runbooks de troubleshooting |

---

## Arquitetura

```
Typeform (formulário Anti-Curioso)
    → n8n (orquestração)
        → Claude AI (cérebro do agente)
        → UaZapi (WhatsApp API)
        → Supabase (banco de dados)
```

---

## Navegação Rápida

| Seção | O que encontrar |
|:------|:----------------|
| [PRD 001](prd-001-agente-qualificacao.md) | Documento de requisitos completo do agente |
| [Workflows](workflows/index.md) | Documentação técnica de cada workflow n8n |
| [Playbooks](playbooks/index.md) | Procedimentos operacionais (como abordar, como responder) |
| [Runbooks](runbooks/index.md) | Troubleshooting e incidentes |
| [Base de Conhecimento](base-conhecimento-clinicas.md) | Dados das clínicas e protocolos |

---

## Status do Projeto

| Fase | Entrega | Status |
|:-----|:--------|:-------|
| **Fase 0** | Base de conhecimento | 🟢 Entregue |
| **MVP** | Agente básico (conversa + qualificação + handoff) | 🟢 Entregue |
| **V2** | Follow-ups automáticos (5 msgs / 7 dias) | 🟢 Entregue |
| **V3** | Handoff inteligente (critérios automáticos) | 🟢 Entregue |
| **V4** | Integração ClickUp (PRD 3) | ⚪ Pendente |

---

!!! tip "Como usar esta documentação"
    **Desenvolvedor?** Comece pelos [Workflows](workflows/index.md).  
    **Hunter/Vendas?** Vá direto pros [Playbooks](playbooks/index.md).  
    **Novo no projeto?** Leia o [PRD 001](prd-001-agente-qualificacao.md) primeiro.
