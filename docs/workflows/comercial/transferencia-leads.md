# 🔄 001.005 — Pipedrive: Transferência de Leads

!!! info "Visão Geral"
    Workflow agendado que busca deals em estágio específico do Pipedrive, redistribui entre SDRs via sub-workflow de distribuição, atualiza o responsável e dispara envio de mensagem parcial.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `KTWEvow3Z8rGab9H` |
| **Status** | 🟢 Ativo |
| **Nós** | 17 |
| **Trigger** | Schedule Trigger |
| **Tags** | `Cadastrado`, `Documentado` |

---

## Fluxo

```mermaid
flowchart TD
    A["⏰ Schedule"] --> B["📊 Pipedrive API\nBuscar deals"]
    B --> C["⚙️ Code1\nExtrair dados"]
    C --> D["🔄 Loop"]
    D --> E{"❓ If\nElegível?"}
    E -->|Sim| F["✏️ Edit Fields"]
    F --> G["▶️ 001.003\nDistribuição"]
    G --> H["🔍 Find user"]
    H --> I["📊 Update deal\nNovo responsável"]
    I --> J["✏️ Edit Fields1"]
    J --> K["▶️ 001.004\nMensagem Parcial"]
    K --> D
    E -->|Não| D
    
    style A fill:#1a1a2e,stroke:#C8A24E,color:#fff
```

## Sub-workflows chamados

| Sub-workflow | Função |
|:-------------|:-------|
| 001.003 — Distribuição | Round-robin de SDRs |
| 001.004 — Mensagem Parcial | Envio WhatsApp |

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| Pipedrive | `Pipedrive - evoluamidia@gmail.com` |