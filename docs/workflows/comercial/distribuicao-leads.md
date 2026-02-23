# 🎯 001.003 — Distribuição de Leads (Pipedrive)

!!! info "Visão Geral"
    Sub-workflow de distribuição round-robin de leads entre SDRs. Consulta o banco para identificar o próximo responsável disponível, atualiza contadores e retorna o email do SDR designado. Chamado por vários workflows (Calendly, Transferência, Leads Parados).

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `gTkwd0N0FUTUzo9q` |
| **Status** | 🔴 Inativo (sub-workflow) |
| **Nós** | 18 |
| **Trigger** | Execute Workflow Trigger (passthrough) |
| **Tags** | `Cadastrado`, `Documentado` |

---

## Arquitetura

```mermaid
flowchart TD
    A["▶️ Trigger"] --> B["📊 Execution Data"]
    B --> C{"🔀 Switch\nOrigem do lead?"}
    C -->|"Rota 1"| D{"❓ If\nTem responsável?"}
    C -->|"Rota 2"| E["🐘 SQL\nBuscar config"]
    D -->|Não| F["🐘 SQL\nBuscar disponíveis"]
    D -->|Sim| G["🐘 SQL\nBuscar específico"]
    F --> H["🐘 SQL\nAtualizar contador"]
    H --> I["✏️ Edit Fields\nRetorna responsável"]
    
    style A fill:#1a1a2e,stroke:#C8A24E,color:#fff
```

## Chamado por

| Workflow | Contexto |
|:---------|:---------|
| 001.002 — Calendly | Novo agendamento |
| 001.005 — Transferência | Lead transferido |
| 001.017 — Leads Parados | Redistribuição diária |

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| PostgreSQL | `Postgres - Metricas` |