# 🔄 001.006 — Pipedrive: Conversão de Campos

!!! info "Visão Geral"
    Sub-workflow utilitário que converte IDs de campos customizados do Pipedrive para seus nomes legíveis. Busca a definição dos deal fields via API e mapeia valores. Usado pelo 001.010 e 001.011.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **ID** | `1ZOJnFDLY7e8hV8j` |
| **Status** | 🔴 Inativo (sub-workflow) |
| **Nós** | 10 |
| **Trigger** | Execute Workflow Trigger (passthrough) |
| **Tags** | `OK`, `Cadastrado`, `Documentado` |

---

## Fluxo

```mermaid
flowchart LR
    A["▶️ Trigger"] --> B["✏️ Edit Fields"]
    B --> C{"🔀 Switch\nTipo conversão?"}
    C -->|"Rota 1"| D["⚙️ Code\nConverter campos"]
    C -->|"Rota 2"| E["⚙️ Code3\nOutra conversão"]
    
    style A fill:#1a1a2e,stroke:#C8A24E,color:#fff
```

Busca definição via `GET /api/v1/dealFields` e converte IDs numéricos para nomes.

## Chamado por

| Workflow | Contexto |
|:---------|:---------|
| 001.010 — Lead Score Pixel | Converter campos antes do pixel |
| 001.011 — Update Deal | Converter campos do webhook |

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| Pipedrive | `Pipedrive - evoluamidia@gmail.com` |