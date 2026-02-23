# HarmonizaPRO — Documentação Técnica

Central de documentação dos workflows n8n, integrações e automações que sustentam a operação comercial da HarmonizaPRO — consultoria de marketing especializada em clínicas de harmonização facial.

---

## O Que É Este Sistema

A HarmonizaPRO opera **41+ workflows n8n** organizados em 7 departamentos. Juntos, eles formam um pipeline completo que vai da captação do lead no Typeform até o fechamento no CRM do Hunter, passando por qualificação com IA, distribuição entre SDRs, tracking de conversões e sincronização de dados em tempo real.

```
                          ┌─────────────────────────────┐
                          │      CAPTAÇÃO DE LEADS       │
                          │  Typeform · Calendly · Meta  │
                          └──────────────┬──────────────┘
                                         │
              ┌──────────────────────────┼──────────────────────────┐
              ▼                          ▼                          ▼
   ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
   │  🤖 IA Harmoniza │       │  💼 Comercial    │       │  📍 Tracking     │
   │  Agente WhatsApp │       │  Pipedrive CRM   │       │  Facebook CAPI   │
   │  Claude + GPT    │       │  Distribuição     │       │  Pixel Events    │
   └────────┬────────┘       └────────┬────────┘       └─────────────────┘
            │                         │
            ▼                         ▼
   ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
   │  🎯 Hunters      │       │  ⚙️ Operação     │       │  📝 Formulários  │
   │  CRM ClickUp     │       │  Meta Ads         │       │  Sync ClickUp    │
   │  Ganho / Perda    │       │  Dados Clientes   │       │  → PostgreSQL    │
   └─────────────────┘       └─────────────────┘       └─────────────────┘
```

---

## Números do Ecossistema

| Métrica | Valor |
|:--------|:------|
| Workflows documentados | **41+** |
| Departamentos | **7** |
| Filas RabbitMQ | **12** |
| Webhooks ativos | **8+** |
| Integrações externas | **12** (Pipedrive, ClickUp, Meta, Typeform, Calendly, WhatsApp…) |
| Bancos PostgreSQL | **3** (Supabase, Métricas, Clientes) |

---

## Stack Tecnológica

| Camada | Tecnologia | Uso |
|:-------|:-----------|:----|
| **Orquestração** | n8n (self-hosted) | Motor de todos os workflows |
| **Mensageria** | RabbitMQ (quorum queues) | Filas assíncronas entre workflows |
| **IA Conversacional** | Claude Sonnet 4 + GPT-5 | Agente de qualificação via WhatsApp |
| **IA Contingência** | Claude Sonnet 4.5 | Fallback para rate limit |
| **IA Resumo** | GPT-4o Mini | Resumo de conversas no handoff |
| **Transcrição** | OpenAI Whisper | Áudio → texto |
| **Visão** | OpenAI GPT-4o / Google Gemini | Imagens, vídeos e documentos |
| **CRM** | Pipedrive | Pipeline de deals e tracking de leads |
| **Gestão** | ClickUp | CRM Hunters + operação de clientes |
| **WhatsApp** | UaZapi / Z-API / MegaAPI | Envio e recebimento de mensagens |
| **Tracking** | Facebook Conversions API | Eventos server-side (bypass ad blockers) |
| **Bancos** | PostgreSQL × 3 | Leads, métricas, clientes |
| **Planilhas** | Google Sheets | Central de Contas, relatórios |
| **Formulários** | Typeform / Calendly | Captação e agendamentos |
| **Monitoramento** | TrackAble | Auto-registro e captura de erros |

---

## Navegação por Departamento

| Departamento | Qtd | O que faz |
|:-------------|:---:|:----------|
| [🤖 IA Harmoniza](workflows/ia-harmoniza/agente-de-ia.md) | 4 | Agente de IA que qualifica leads via WhatsApp com Claude + GPT |
| [💼 Comercial](workflows/comercial/atualizar-dados-cliente.md) | 20 | Pipeline completo: Typeform → Pipedrive → distribuição → WhatsApp → pixel |
| [🎯 Hunters](workflows/hunters/central-automacao.md) | 5 | CRM dos SDRs no ClickUp com automação de ganho, perda e WhatsApp |
| [⚙️ Operação](workflows/operacao/central-automacao.md) | 7 | Gestão de clientes, monitoramento Meta Ads, retroativos |
| [📍 Tracking](workflows/tracking/gtm-typeform-1-receptor.md) | 3 | Pipeline server-side: Typeform → enriquecimento → Facebook CAPI |
| [📋 Templates](workflows/templates/organizar-clickup.md) | 2 | Blocos reutilizáveis: parser ClickUp e padrão RabbitMQ |
| [📝 Formulários](workflows/clickup/formularios-1-central.md) | 4 | Sync CRUD de formulários ClickUp ↔ PostgreSQL |

---

## Atalhos por Perfil

!!! tip "Desenvolvedor novo?"
    Comece pelo [Índice de Workflows](workflows/index.md) — tem o inventário completo, mapa de filas e diagrama de arquitetura.

!!! tip "Debugando um problema?"
    Use a busca (🔍) pelo **ID do workflow** ou vá direto ao departamento. Cada doc lista credenciais, filas e troubleshooting.

!!! tip "Criando um workflow novo?"
    Leia os [Templates](workflows/templates/organizar-clickup.md) primeiro — definem os padrões de RabbitMQ e parser ClickUp usados em todo o sistema.

---

## Padrões Arquiteturais

O sistema segue 4 padrões recorrentes:

**Dispatcher → Worker (RabbitMQ)** — Um workflow recebe o evento (webhook/schedule), publica na fila, outro consome e processa. Se o worker falha, a mensagem volta para a fila.

**Sub-workflows (Execute Workflow)** — Lógica reutilizável chamada por vários workflows. Ex: Distribuição de Leads é chamada pelo Calendly, Transferência e Leads Parados.

**Dedup por Redelivered** — Todo consumer RabbitMQ verifica `fields.redelivered` antes de processar. Se verdadeiro, deleta a mensagem sem reprocessar.

**OrganizarClickUp** — Template que transforma custom fields do ClickUp em JSON estruturado. Presente em 8+ workflows via sub-workflow 005.001.

---

## Credenciais Globais

| Credencial | Serviço | Presente em |
|:-----------|:--------|:------------|
| `RabbitMQ` | Filas de mensagens | 15+ workflows |
| `Pipedrive - evoluamidia@gmail.com` | CRM | 10+ workflows |
| `ClickUp - Ferramentas` | Gestão de tarefas | 8+ workflows |
| `Postgres - Metricas` | Banco principal de leads | 10+ workflows |
| `Metricas - Clientes` | Banco de dados de clientes | 5+ workflows |
| `Evento Vendas` | Banco de eventos de vendas | 3 workflows |
| `ferramentas@harmoniza.pro` | Google Sheets OAuth | 3 workflows |
| `Z Api` / MegaAPI | WhatsApp API | 5+ workflows |
| `Calendly account` | Agendamentos | 1 workflow |