# 🎯 001.010 — Pipedrive: Evento Pixel Lead Score

!!! info "Visão Geral"
    Worker que consome eventos de lead scoring do Pipedrive e dispara conversões para o Facebook Pixel (CAPI). Busca dados do deal, converte campos customizados, consulta tracking no banco, e envia evento com dados hasheados.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `QEPP7Y3zLwbeOxta` |
| **Status** | 🟢 Ativo |
| **Nós** | 21 |
| **Trigger** | RabbitMQ — fila `pipedrive_leadscore_pixel` |
| **Tags** | `Cadastrado`, `Documentado` |

---

## Fluxo

```mermaid
flowchart TD
    A["🐇 Trigger\npipedrive_leadscore_pixel"] --> B{"❓ checkQueue"}
    B -->|OK| C["📊 Get deal\nPipedrive"]
    C --> D["✏️ Edit Fields"]
    D --> E["▶️ 001.006\nConverter Campos"]
    E --> F["🐘 SQL\nBuscar tracking"]
    F --> G{"❓ If\nTem pixel?"}
    G --> H["✏️ Set\nConfig pixel"]
    H --> I["🔐 Hash: nome → sobrenome → email → telefone"]
    I --> J{"❓ checkFbc"}
    J -->|Com fbc| K["📡 CAPI site"]
    J -->|Sem fbc| L["📡 CAPI site1"]
    K --> M["🐘 SQL\nLog"]
    L --> M
    
    style A fill:#1a1a2e,stroke:#ff6600,color:#fff
    style K fill:#1a1a2e,stroke:#1877f2,color:#fff
```

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| RabbitMQ | `RabbitMQ` |
| Pipedrive | `Pipedrive - evoluamidia@gmail.com` |
| PostgreSQL | `Postgres - Metricas` |