# 📊 001.011 — Pipedrive: Update Deal (Dispatcher)

!!! info "Visão Geral"
    Dispatcher que recebe webhooks de atualização de deals do Pipedrive, converte campos customizados e roteia para filas específicas: Lead Score Pixel (tracking) ou Mudança de Responsável.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `xawOX8VHRfM8AbwM` |
| **Status** | 🟢 Ativo |
| **Nós** | 10 |
| **Trigger** | Webhook POST `/pipedrive_update_deal` |
| **Tags** | `OK`, `Cadastrado`, `Documentado` |

---

## Fluxo

```mermaid
flowchart LR
    A["🔗 Webhook\n/pipedrive_update_deal"] --> B["✏️ Edit Fields1"]
    B --> C["▶️ 001.006\nConverter Campos"]
    C --> D{"🔀 Switch"}
    D -->|"Lead Score"| E["🐇 pipedrive_leadscore_pixel"]
    D -->|"Mudança user"| F["🐇 pipedrive_mudanca_user"]
    
    style A fill:#1a1a2e,stroke:#C8A24E,color:#fff
```

## Filas

| Fila | Consumer |
|:-----|:---------|
| `pipedrive_leadscore_pixel` | 001.010 |
| `pipedrive_mudanca_user` | (worker separado) |

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| RabbitMQ | `RabbitMQ` |