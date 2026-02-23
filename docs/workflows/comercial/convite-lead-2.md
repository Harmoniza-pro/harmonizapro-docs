# 📨 001.007 [2/3] — Envio de Convite: Mensagem

!!! info "Visão Geral"
    Worker que consome da fila de convites, aplica delay conforme timing calculado pelo scheduler, e envia mensagem de convite via WhatsApp (MegaAPI). Após envio, atualiza status no banco.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `Av4GRQZkp71h41VX` |
| **Status** | 🟢 Ativo |
| **Nós** | 13 |
| **Trigger** | RabbitMQ — fila `acao_vendas_grupo_whatsapp` |
| **Tags** | `Cadastrado`, `OK` |

---

## Fluxo

```mermaid
flowchart TD
    A["🐇 Trigger\nacao_vendas_grupo_whatsapp"] --> B{"❓ checkQueue"}
    B -->|Redelivered| C["🗑️ Delete"]
    B -->|OK| D["⏳ Wait\nTiming calculado"]
    D --> E["✏️ Edit Fields"]
    E --> F["⚙️ Code\nMontar mensagem"]
    F --> G["📨 Quero Saber Mais\nMegaAPI WhatsApp"]
    G --> H["🐘 SQL\nAtualizar status"]
    H --> I["⏳ Wait1"]
    
    style A fill:#1a1a2e,stroke:#ff6600,color:#fff
    style G fill:#1a1a2e,stroke:#25d366,color:#fff
```

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| RabbitMQ | `RabbitMQ` |
| PostgreSQL | `Evento Vendas` |