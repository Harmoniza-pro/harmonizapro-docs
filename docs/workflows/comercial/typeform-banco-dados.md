# 🗄️ 001.012 — Typeform: Banco de Dados

!!! info "Visão Geral"
    Worker que consome dados de formulários Typeform da fila e persiste no PostgreSQL. Verifica se o lead já existe no banco (INSERT ou UPDATE) e executa queries de tracking.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `nZU47kosH8E2FkJ5` |
| **Status** | 🟢 Ativo |
| **Nós** | 13 |
| **Trigger** | RabbitMQ — fila `typeform_banco_de_dados` |
| **Tags** | `OK`, `Cadastrado`, `Documentado` |

---

## Fluxo

```mermaid
flowchart TD
    A["🐇 Trigger\ntypeform_banco_de_dados"] --> B{"❓ checkQueue"}
    B -->|OK| C["🐘 SQL\nBuscar lead existente"]
    C --> D{"❓ If\nExiste?"}
    D -->|Sim| E["🐘 SQL\nUPDATE lead_tracking"]
    D -->|Não| F["🐘 SQL\nINSERT lead_tracking"]
    E --> G["🐘 SQL\nDados complementares"]
    F --> H["🐘 SQL\nDados complementares"]
    
    style A fill:#1a1a2e,stroke:#ff6600,color:#fff
```

## Fila

| Fila | Publisher |
|:-----|:---------|
| `typeform_banco_de_dados` | 001.001 [1/2] e [2/2] |

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| RabbitMQ | `RabbitMQ` |
| PostgreSQL | `Postgres - Metricas` |