# 📱 001.004 — Typeform: Envio de Mensagem Parcial

!!! info "Visão Geral"
    Sub-workflow que envia mensagens WhatsApp para leads que preencheram parcialmente o formulário Typeform. Busca dados do deal no Pipedrive, filtra leads elegíveis e dispara sequência de mensagens para o SDR e para o lead.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `iW5VeKzMhlHTiLTF` |
| **Status** | 🔴 Inativo (sub-workflow) |
| **Nós** | 23 |
| **Trigger** | Execute Workflow Trigger (passthrough) |
| **Tags** | `Cadastrado`, `Documentado` |

---

## Fluxo

```mermaid
flowchart TD
    A["▶️ Trigger"] --> B["🐘 leads_colaboradores"]
    B --> C["📱 SDR 1\nDados WhatsApp"]
    C --> D["📨 Mensagem SDR"]
    D --> E["⏳ Wait7"] --> F["📨 Mensagem1"]
    F --> G["⏳ Wait8"] --> H["📨 Mensagem2"]
    
    A --> I["⏳ Wait"] --> J["📊 Get deal\nPipedrive"]
    J --> K["⚙️ filtro2\nElegibilidade"]
    K --> L{"❓ If"}
    L -->|"Elegível"| M["📨 Sequência de 4 msgs\npara o lead"]
    
    style D fill:#1a1a2e,stroke:#25d366,color:#fff
```

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| Pipedrive | `Pipedrive - evoluamidia@gmail.com` |
| WhatsApp | `Z Api` |
| PostgreSQL | `Postgres - Metricas` |