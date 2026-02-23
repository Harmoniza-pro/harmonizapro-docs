# Workflows

Inventário completo dos 41+ workflows n8n da HarmonizaPRO, organizados por departamento conforme a instância de produção (`workflows.goldeletra.pro`).

---

## Arquitetura Geral

```mermaid
flowchart TB
    subgraph CAPTAÇÃO ["📥 Captação de Leads"]
        TF["Typeform"]
        CAL["Calendly"]
        META["Meta Ads"]
    end

    subgraph COMERCIAL ["💼 Comercial · 20 workflows"]
        direction TB
        F1["001.001\nFormulários\n(webhook + worker)"]
        C1["001.002\nCalendly"]
        DIST["001.003\nDistribuição\nround-robin"]
        UPD["001.011\nUpdate Deal\ndispatcher"]
        BD["001.012\nBanco de Dados"]
        MSG["001.004–008\nMensagens\nWhatsApp"]
        PARADO["001.017\nLeads Parados\ndiário 6h"]
    end

    subgraph IA ["🤖 IA Harmoniza · 4 workflows"]
        AG["Agente de IA\nClaude + GPT"]
        CT["Chamada\nTypeform"]
        TOOL["Tool\nTransferir"]
        FU["Follow\nUps"]
    end

    subgraph TRACKING ["📍 Tracking · 3 workflows"]
        GTM1["[1/3] Receptor"]
        GTM2["[2/3] Enriquecimento"]
        GTM3["[3/3] Pixel CAPI"]
    end

    subgraph HUNTERS ["🎯 Hunters · 5 workflows"]
        H0["Central\nAutomação"]
        HT["Typeform\nClientes"]
        HC["CRM\nHunter"]
        HG["Ganho"]
        HP["Perda"]
    end

    subgraph OPERAÇÃO ["⚙️ Operação · 7 workflows"]
        O0["Central\nAutomação"]
        OA["Meta Ads\nMonitor"]
        OL["Alterar Link\nFormulário"]
    end

    subgraph FORMULÁRIOS ["📝 Formulários · 4 workflows"]
        FC["Central"]
        F2["Created"]
        F3["Updated"]
        F4["Deleted"]
    end

    TF --> F1
    TF --> GTM1
    CAL --> C1
    F1 --> DIST
    C1 --> DIST
    F1 --> BD
    UPD --> |"RabbitMQ"| TRACKING
    PARADO --> DIST
    DIST --> MSG

    CT --> AG
    AG --> TOOL
    AG --> FU

    GTM1 --> GTM2 --> GTM3

    H0 --> HG
    H0 --> HP

    O0 --> OL
    META --> OA

    FC --> F2
    FC --> F3
    FC --> F4

    style COMERCIAL fill:#0d1117,stroke:#C8A24E,color:#fff
    style IA fill:#0d1117,stroke:#8b5cf6,color:#fff
    style TRACKING fill:#0d1117,stroke:#1877f2,color:#fff
    style HUNTERS fill:#0d1117,stroke:#22c55e,color:#fff
    style OPERAÇÃO fill:#0d1117,stroke:#3b82f6,color:#fff
    style FORMULÁRIOS fill:#0d1117,stroke:#f97316,color:#fff
    style CAPTAÇÃO fill:#0d1117,stroke:#ef4444,color:#fff
```

---

## Inventário por Departamento

### 🤖 IA Harmoniza

| Workflow | ID | Status | Trigger | Nós |
|:---------|:---|:------:|:--------|----:|
| [Agente de IA](ia-harmoniza/agente-de-ia.md) | `8hdajgWAADbHorQF` | 🟢 | Webhook POST | 92 |
| [Chamada Typeform](ia-harmoniza/chamada-typeform.md) | `VPVYN9AzG8IGnKiR` | 🟢 | Webhook POST | 29 |
| [Tool Transferir](ia-harmoniza/tool-transferir.md) | `Gt60I1KPG4ReJSIe` | 🟢 | Webhook POST | 12 |
| [Fluxo Follow Ups](ia-harmoniza/fluxo-follow-ups.md) | `W1msnd1vZWkpFSDM` | 🔴 | Schedule 11min | 65 |


### 💼 Comercial

| # | Workflow | ID | Status | Trigger | Nós |
|--:|:---------|:---|:------:|:--------|----:|
| 001 | [Typeform Formulários [1/2]](comercial/typeform-formularios-1.md) | `0hGkd1W7Aqg8qUUH` | 🟢 | Webhook POST | 30 |
| 001 | [Typeform Formulários [2/2]](comercial/typeform-formularios-2.md) | `ut7SuyAS0AQ3bywe` | 🟢 | 🐇 `typeform_pipedrive` | 30 |
| 002 | [Calendly Event Create](comercial/calendly-event-create.md) | `EOeEGroKenTL6tm8` | 🟢 | Calendly Trigger | 48 |
| 003 | [Distribuição de Leads](comercial/distribuicao-leads.md) | `gTkwd0N0FUTUzo9q` | ⚙️ | Sub-workflow | 18 |
| 004 | [Envio Mensagem Parcial](comercial/envio-mensagem-parcial.md) | `iW5VeKzMhlHTiLTF` | ⚙️ | Sub-workflow | 23 |
| 005 | [Transferência de Leads](comercial/transferencia-leads.md) | `KTWEvow3Z8rGab9H` | 🟢 | Schedule | 17 |
| 006 | [Conversão de Campos](comercial/conversao-campos.md) | `1ZOJnFDLY7e8hV8j` | ⚙️ | Sub-workflow | 10 |
| 007 | [Convite Lead [1/3] Scheduler](comercial/convite-lead-1.md) | `EPj4uqLra763cKjD` | 🔴 | Schedule 30min | 11 |
| 007 | [Convite Lead [2/3] Mensagem](comercial/convite-lead-2.md) | `Av4GRQZkp71h41VX` | 🟢 | 🐇 `acao_vendas_grupo_whatsapp` | 13 |
| 007 | [Convite Lead [3/3] Resposta](comercial/convite-lead-3.md) | `Q8fXdJi9qhdmrs3l` | 🟢 | Webhook POST | 20 |
| 008 | [Envio Mensagem Clientes](comercial/envio-mensagem-clientes.md) | `VjXrQZZPivqrbNZM` | ⚙️ | Sub-workflow | 21 |
| 009 | [Documentar Msgs CRM](comercial/documentar-mensagens-crm.md) | `CJfeejjEkXAZwNeB` | 🟢 | Webhook POST | 34 |
| 010 | [Evento Pixel Lead Score](comercial/evento-pixel-lead-score.md) | `QEPP7Y3zLwbeOxta` | 🟢 | 🐇 `pipedrive_leadscore_pixel` | 21 |
| 011 | [Update Deal Dispatcher](comercial/pipedrive-update-deal.md) | `xawOX8VHRfM8AbwM` | 🟢 | Webhook POST | 10 |
| 012 | [Typeform Banco de Dados](comercial/typeform-banco-dados.md) | `nZU47kosH8E2FkJ5` | 🟢 | 🐇 `typeform_banco_de_dados` | 13 |
| 013 | [Evento Lead Clientes](comercial/evento-lead-clientes.md) | `SiBXX9WD2onuqIAR` | 🟢 | Webhook | 4 |
| 014 | [Atualizar Dados Cliente](comercial/atualizar-dados-cliente.md) | `4L3UoZGFAsWofZYx` | 🟢 | 🐇 `dados_sdr` | 9 |
| 015 | [Dashboard Planilha](comercial/dashboard-planilha-atualizada.md) | `cQ49sJd4FLFY5Jfz` | 🟢 | Schedule 23h45 | 6 |
| 016 | [Retroativo UTM](comercial/retroativo-utm.md) | `a5zLplTyFmXN5lgP` | 🔴 | Manual | 5 |
| 017 | [Leads Parados](comercial/leads-parados.md) | `hUgd3JCAuUFUh5e4` | 🟢 | Cron `0 6 * * *` | 10 |

### 🎯 Hunters

| # | Workflow | Status | Trigger | Nós |
|--:|:---------|:------:|:--------|----:|
| 000 | [Central de Automação](hunters/central-automacao.md) | 🟢 | ClickUp Trigger | 7 |
| 001 | [Typeform Clientes](hunters/typeform-clientes.md) | 🟢 | Webhook POST | 14 |
| 002 | [CRM Hunter](hunters/crm-hunter.md) | 🟢 | Webhook POST | 19 |
| 003 | [Ganho](hunters/ganho.md) | 🟢 | 🐇 `clickup_hunter_ganho` | 15 |
| 004 | [Perda](hunters/perda.md) | 🟢 | 🐇 `clickup_hunter_perda` | 11 |

### ⚙️ Operação

| # | Workflow | Status | Trigger | Nós |
|--:|:---------|:------:|:--------|----:|
| 000 | [Central de Automação](operacao/central-automacao.md) | 🟢 | ClickUp Trigger | 4 |
| 001 | [Alterar Link Formulário](operacao/alterar-link-formulario.md) | 🟢 | 🐇 `clientes_alterar_link_form` | 11 |
| 002 | [Desempenho Meta Ads](operacao/desempenho-meta-ads.md) | 🟢 | Schedule + RabbitMQ | 30 |
| 003 | [Retroativo Respostas](operacao/retroativo-respostas-banco.md) | 🔴 | Manual | 21 |
| — | [Retroativo Tarefas CRM](operacao/retroativo-tarefas-crm.md) | 🔴 | Manual | 10 |

### 📍 Tracking

| Parte | Workflow | ID | Status | Trigger | Nós |
|:-----:|:---------|:---|:------:|:--------|----:|
| 1/3 | [Receptor](tracking/gtm-typeform-1-receptor.md) | `AiL4nHZJqhVO1vR1` | 🟢 | Webhook POST | 6 |
| 2/3 | [Enriquecimento](tracking/gtm-typeform-2-enriquecimento.md) | `0E0NW4uGtYBeRwHF` | 🟢 | 🐇 `gtm_banco_de_dados_1_2` | 14 |
| 3/3 | [Pixel CAPI](tracking/gtm-typeform-3-pixel.md) | `cq6W0FsGX4IMNdtl` | 🟢 | 🐇 `gtm_banco_de_dados_2_2` | 19 |

### 📋 Templates

| # | Workflow | Descrição |
|--:|:---------|:----------|
| 001 | [Organizar ClickUp](templates/organizar-clickup.md) | Parser universal de custom fields — usado em 8+ workflows |
| 002 | [RabbitMQ](templates/rabbitmq.md) | Padrão consumer (dedup) + publisher (quorum) |

### 📝 Formulários ClickUp

| Parte | Workflow | Status | Trigger | Nós |
|:-----:|:---------|:------:|:--------|----:|
| 1/4 | [Central](clickup/formularios-1-central.md) | 🟢 | Webhook POST | 7 |
| 2/4 | [TaskCreated](clickup/formularios-2-created.md) | ⚙️ | Sub-workflow | 8 |
| 3/4 | [TaskDeleted](clickup/formularios-3-deleted.md) | ⚙️ | Sub-workflow | 10 |
| 4/4 | [TaskUpdated](clickup/formularios-4-updated.md) | ⚙️ | Sub-workflow | 9 |

!!! note "Legenda de Status"
    🟢 Ativo em produção · 🔴 Inativo / Manual · ⚙️ Sub-workflow (chamado por outros)

---

## Mapa de Filas RabbitMQ

Todas usam **quorum queues** (`durable: true`, `acknowledge: executionFinishesSuccessfully`, `parallelMessages: 1`).

```mermaid
flowchart LR
    subgraph PUB ["Publishers"]
        P1["001.001 [1/2]\nFormulários"]
        P2["001.001 [1/2]+[2/2]"]
        P3["001.011\nUpdate Deal"]
        P4["001.015\nDashboard"]
        P5["001.007 [1/3]\nConvite Scheduler"]
        P6["002.000\nHunters Central"]
        P7["003.000\nOp Central"]
        P8["003.002\nMeta Ads"]
        P9["004.001 [1/3]\nTracking Receptor"]
        P10["004.001 [2/3]\nEnriquecimento"]
    end

    subgraph FILAS ["Filas"]
        Q1(["typeform_pipedrive"])
        Q2(["typeform_banco_de_dados"])
        Q3(["pipedrive_leadscore_pixel"])
        Q4(["pipedrive_mudanca_user"])
        Q5(["dados_sdr"])
        Q6(["acao_vendas_grupo_whatsapp"])
        Q7(["clickup_hunter_ganho"])
        Q8(["clickup_hunter_perda"])
        Q9(["clientes_alterar_link_form"])
        Q10(["trafego_desempenho"])
        Q11(["gtm_banco_de_dados_1_2"])
        Q12(["gtm_banco_de_dados_2_2"])
    end

    subgraph CON ["Consumers"]
        C1["001.001 [2/2]\nFormulários Worker"]
        C2["001.012\nBanco de Dados"]
        C3["001.010\nPixel Lead Score"]
        C5["001.014\nAtualizar Cliente"]
        C6["001.007 [2/3]\nConvite Msg"]
        C7["002.003\nGanho"]
        C8["002.004\nPerda"]
        C9["003.001\nAlterar Link"]
        C10["003.002 [2/2]\nMeta Ads Worker"]
        C11["004.001 [2/3]\nEnriquecimento"]
        C12["004.001 [3/3]\nPixel CAPI"]
    end

    P1 --> Q1 --> C1
    P2 --> Q2 --> C2
    P3 --> Q3 --> C3
    P3 --> Q4
    P4 --> Q5 --> C5
    P5 --> Q6 --> C6
    P6 --> Q7 --> C7
    P6 --> Q8 --> C8
    P7 --> Q9 --> C9
    P8 --> Q10 --> C10
    P9 --> Q11 --> C11
    P10 --> Q12 --> C12

    style FILAS fill:#1a1a2e,stroke:#ff6600,color:#fff
```

---

## Mapa de Sub-workflows

| Sub-workflow | ID | Chamado por |
|:-------------|:---|:------------|
| 001.003 — Distribuição de Leads | `gTkwd0N0FUTUzo9q` | 001.002 (Calendly), 001.005 (Transferência), 001.017 (Parados) |
| 001.004 — Mensagem Parcial | `iW5VeKzMhlHTiLTF` | 001.005 (Transferência) |
| 001.006 — Conversão de Campos | `1ZOJnFDLY7e8hV8j` | 001.010 (Lead Score), 001.011 (Update Deal) |
| 001.008 — Envio Mensagem Clientes | `VjXrQZZPivqrbNZM` | Disponível para chamada |
| 005.001 — Organizar ClickUp | `YQiSPhl44vt3lYWl` | 8+ workflows (Hunters, Operação, Formulários) |
| 006.000 [2/4] — TaskCreated | `kastfiC5DE6IdNUd` | 006.000 [1/4] Central |
| 006.000 [3/4] — TaskDeleted | `jGfoGDdLSD7uJlww` | 006.000 [1/4] Central |
| 006.000 [4/4] — TaskUpdated | `HVMQTCfVDbSFnQJt` | 006.000 [1/4] Central |

---

## Webhooks Ativos

| Path | Workflow | Fonte |
|:-----|:---------|:------|
| `/typeform_pipedrive` | 001.001 [1/2] | Typeform |
| `/typeform_gtm` | 004.001 [1/3] | GTM / Typeform |
| `/pipedrive_update_deal` | 001.011 | Pipedrive Webhooks |
| `/documentar_msgs` | 001.009 | WhatsApp |
| `/quero_saber_mais` | 001.007 [3/3] | WhatsApp (botão) |
| `/response_clickup` | 006.000 [1/4] | ClickUp Webhooks |
| `/mensagem_dras` | 002.001 | Typeform Clientes |
| `/mensagens_hunter` | 002.002 | WhatsApp (Hunter) |
| UUID paths | 001.013, IA workflows | Diversos |

---

## Schedules Ativos

| Workflow | Frequência | Horário |
|:---------|:-----------|:--------|
| 001.005 — Transferência | Periódico | — |
| 001.007 [1/3] — Convite | A cada 30 min | 7h–21h BRT |
| 001.015 — Dashboard | Diário | 23h45 |
| 001.017 — Leads Parados | Diário | 06h00 |
| 003.002 — Meta Ads | Diário | — |
| Métricas Diárias | Diário | — |
| Monitoramento Custos | Semanal | — |
| Fluxo Follow Ups | A cada 11 min | (inativo) |

---

## Error Workflow Global

A maioria dos workflows usa o error workflow **`ByxX1TqYfyvlgp2T`** para captura centralizada de falhas. Nós de auto-registro TrackAble (`webhooks.autotrackable.com.br`) estão presentes mas desabilitados na maioria dos workflows.