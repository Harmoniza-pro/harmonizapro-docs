# ⏸️ 001.017 — Pipedrive: Leads Parados

!!! info "Visão Geral"
    Workflow diário (6h) que identifica leads parados no estágio 128 (pipeline 21) do Pipedrive, redistribui entre SDRs via sub-workflow de distribuição e move para o estágio 81 com novo responsável.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `hUgd3JCAuUFUh5e4` |
| **Status** | 🟢 Ativo |
| **Nós** | 10 |
| **Trigger** | Schedule (cron `0 6 * * *`) |

---

## Fluxo

```mermaid
flowchart TD
    A["⏰ Schedule\n6h diário"] --> B["📊 Pipedrive API v2\nDeals stage 128"]
    B --> C["⚙️ Code1\nExtrair data"]
    C --> D["🔄 Loop"]
    D --> E["✏️ Edit Fields\norigem: parcial"]
    E --> F["▶️ 001.003\nDistribuição"]
    F --> G["🔍 Find user\nPipedrive"]
    G --> H{"❓ If\nLabel 109?"}
    H -->|Sim| I["📊 Update deal\n(Rota A)"]
    H -->|Não| J["📊 Update deal1\n(Rota B)"]
    I --> D
    J --> D
    
    style A fill:#1a1a2e,stroke:#C8A24E,color:#fff
```

### Regra de negócio
- Busca deals **abertos** no **stage 128** (pipeline 21) ordenados desc
- Redistribui via round-robin (001.003)
- Move todos para **stage 81** com novo responsável
- Label 109 diferencia rota de update

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| Pipedrive | `Pipedrive - evoluamidia@gmail.com` |