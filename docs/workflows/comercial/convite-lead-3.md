# ✅ 001.007 [3/3] — Envio de Convite: Resposta

!!! info "Visão Geral"
    Último estágio que processa respostas dos leads ao convite. Recebe webhook "Quero Saber Mais", valida, envia vídeo de apresentação + link do grupo WhatsApp, e registra conversão no banco.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `Q8fXdJi9qhdmrs3l` |
| **Status** | 🟢 Ativo |
| **Nós** | 20 |
| **Trigger** | Webhook POST `/quero_saber_mais` |
| **Tags** | `OK`, `Cadastrado`, `Documentado` |

---

## Fluxo

```mermaid
flowchart TD
    A["🔗 Webhook\n/quero_saber_mais"] --> B{"❓ If\nVálido?"}
    B -->|Sim| C{"🔀 Switch\nTipo ação?"}
    C -->|"Enviar conteúdo"| D["✏️ Edit Fields"]
    D --> E["📹 Enviar Video\nWhatsApp"]
    E --> F["⏳ Wait"]
    F --> G["🔗 Enviar Link Grupo\nWhatsApp"]
    C -->|"Registrar"| H["📊 Execution Data"]
    H --> I["🐘 SQL\nUpdate status"]
    I --> J["🐘 SQL\nLog"]
    
    style A fill:#1a1a2e,stroke:#C8A24E,color:#fff
    style E fill:#1a1a2e,stroke:#25d366,color:#fff
```

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| PostgreSQL | `Evento Vendas` |