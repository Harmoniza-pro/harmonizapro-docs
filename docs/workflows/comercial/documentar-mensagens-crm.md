# 📝 001.009 — Pipedrive: Documentar Mensagens no CRM

!!! info "Visão Geral"
    Webhook que recebe mensagens do WhatsApp e as documenta como atividades no Pipedrive. Diferencia mensagens do lead e do atendente, processa texto, áudio, imagem, vídeo e documentos. Busca o deal correspondente por telefone.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `CJfeejjEkXAZwNeB` |
| **Status** | 🟢 Ativo |
| **Nós** | 34 (vários de mídia desabilitados) |
| **Trigger** | Webhook POST `/documentar_msgs` |

---

## Arquitetura

```mermaid
flowchart TD
    A["🔗 Webhook\n/documentar_msgs"] --> B{"❓ isGroup?"}
    B -->|Individual| C{"🔀 Switch\nTipo mídia?"}
    C -->|Texto| D["✏️ Set Text"]
    C -->|Áudio| E["🔐 Base64 → Transcrição"]
    C -->|Imagem| F["🖼️ Base64 → Análise IA"]
    D --> G["🔀 Merge"]
    G --> H["✏️ Set Input"]
    H --> I["⏳ Wait1"]
    I --> J["🔍 Encontra Negocio\nPipedrive"]
    J --> K{"❓ If\nEncontrou?"}
    K --> L["📊 Execution Data"]
    L --> M{"❓ fromMe?"}
    M -->|Sim| N["📝 Atividade: Msg Atendente"]
    M -->|Não| O["📝 Atividade: Msg Lead"]
    
    style A fill:#1a1a2e,stroke:#C8A24E,color:#fff
    style N fill:#1a1a2e,stroke:#22c55e,color:#fff
    style O fill:#1a1a2e,stroke:#3b82f6,color:#fff
```

## Tipos de mídia (maioria desabilitada, apenas texto ativo)

| Tipo | Status | Processamento |
|:-----|:-------|:-------------|
| Texto | ✅ Ativo | Direto |
| Áudio | ❌ Desabilitado | Base64 → OpenAI Whisper |
| Imagem | ❌ Desabilitado | Base64 → OpenAI Vision |
| Vídeo | ❌ Desabilitado | Base64 → Google Gemini |
| Documento | ❌ Desabilitado | Base64 → Google Gemini |

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| Pipedrive | `Pipedrive - evoluamidia@gmail.com` |