# 💬 001.008 — Envio de Mensagem: Clientes

!!! info "Visão Geral"
    Sub-workflow de envio de mensagens em massa para clientes via WhatsApp. Lê lista de destinatários do Google Sheets, verifica status de conexão do WhatsApp, e envia mensagens em lote com controle de rate limiting.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `VjXrQZZPivqrbNZM` |
| **Status** | 🔴 Inativo (sub-workflow) |
| **Nós** | 21 |
| **Trigger** | Execute Workflow Trigger (passthrough) |

---

## Fluxo

```mermaid
flowchart TD
    A["▶️ Trigger"] --> B["📊 Google Sheets\nLista de clientes"]
    B --> C["⚙️ Code\nSepara mensagens"]
    C --> D["🔄 Loop"]
    D --> E["📨 Mensagem WhatsApp"]
    E --> F["⏳ Wait"]
    F --> G["📊 Limit"]
    G --> H["📨 Msg Não Lida\nVerificar status"]
    H --> I{"❓ If\nConectado?"}
    I -->|Sim| J["📊 Sheets\nMarcar conectado"]
    I -->|Não| K["📊 Sheets\nMarcar desconectado"]
    
    style A fill:#1a1a2e,stroke:#C8A24E,color:#fff
    style E fill:#1a1a2e,stroke:#25d366,color:#fff
```

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| Google Sheets | `ferramentas@harmoniza.pro` |