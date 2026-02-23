# ✅ 002.003 — Hunters: Ganho

!!! info "Visão Geral"
    Worker que consome a fila `clickup_hunter_ganho`, valida se todos os campos obrigatórios estão preenchidos e aprova ou rejeita o ganho. Se aprovado, atualiza o status da task para "ganho" e vincula com a task do cliente. Se reprovado, marca como recusado e adiciona um comentário indicando os campos faltantes.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **Nome** | 002.003 - Hunters - Ganho |
| **ID** | `9LCzkcuPhBYaK1MO` |
| **Instância** | `workflows.goldeletra.pro` |
| **Status** | 🟢 Ativo |
| **Nós** | 15 |
| **Trigger** | RabbitMQ — fila `clickup_hunter_ganho` |
| **Dependências** | RabbitMQ, ClickUp |

---

## Arquitetura

```mermaid
flowchart TD
    A["🐇 RabbitMQ Trigger\nclickup_hunter_ganho"] --> B{"❓ If\nRedelivered?"}
    B -->|Sim| C["🗑️ Delete message\nDescartar duplicata"]
    B -->|Não| D["📋 Get a task\nBuscar dados"]
    D --> E["⚙️ OrganizarClickUp\nParsear custom fields"]
    E --> F["⚙️ Code4\nValidar campos obrigatórios"]
    F --> G{"❓ If4\nAprovado?"}
    
    G -->|"✅ Aprovado"| H["🏷️ Alterar Tag - Aprovado\nCampo Automações"]
    G -->|"❌ Reprovado"| I["🏷️ Alterar Tag - Reprovado\nCampo Automações"]
    
    H --> J["✏️ Update a task\nStatus → 'ganho'"]
    J --> K["📋 Get a task1\nBuscar task cliente"]
    K --> L["⚙️ OrganizarClickUp1\nParsear cliente"]
    L --> M{"❓ If1\nTem task vinculada?"}
    M -->|Sim| N["✏️ Set custom field\nVincular tasks"]
    
    I --> O["💬 Create a comment\n'❌ Campos faltantes: ...'"]
    
    style A fill:#1a1a2e,stroke:#ff6600,color:#fff
    style G fill:#1a1a2e,stroke:#f97316,color:#fff
    style H fill:#1a1a2e,stroke:#22c55e,color:#fff
    style I fill:#1a1a2e,stroke:#ff5555,color:#fff
    style J fill:#1a1a2e,stroke:#22c55e,color:#fff
    style N fill:#1a1a2e,stroke:#7B68EE,color:#fff
    style O fill:#1a1a2e,stroke:#ff5555,color:#fff
```

---

## Fluxo Detalhado

### 1. Consumo e dedup
- **RabbitMQ Trigger** consome da fila `clickup_hunter_ganho` (quorum, acknowledge on success)
- **If** verifica `redelivered` — se a mensagem já foi entregue antes, descarta para evitar reprocessamento

### 2. Busca e organização
- **Get a task** busca dados completos da task pelo `task_id` recebido
- **OrganizarClickUp** parseia todos os custom fields em JSON estruturado (code JavaScript padrão)

### 3. Validação de campos obrigatórios
**Code4** verifica se todos os campos obrigatórios para um ganho estão preenchidos. Campos validados incluem informações do cliente, valor do contrato, etc.

Se algum campo obrigatório estiver vazio:

```
❌ Reprovado!

📋 Necessário preencher os seguintes campos:

🔸 Campo X
🔸 Campo Y
```

### 4. Aprovação

| Resultado | Ações |
|:----------|:------|
| **Aprovado** | Tag → `Campo Ganho Aprovado` → Status → `ganho` → Busca task cliente → Vincula |
| **Reprovado** | Tag → `Campo Ganho Recusado` → Comentário com campos faltantes |

### 5. Vinculação (apenas aprovado)
Após marcar como ganho, busca a task do cliente na Gestão de Clientes e vincula via custom field de relação — garantindo rastreabilidade bidirecional.

---

## Diferença do 002.004 (Perda)

| Aspecto | 002.003 (Ganho) | 002.004 (Perda) |
|:--------|:----------------|:-----------------|
| **Fila** | `clickup_hunter_ganho` | `clickup_hunter_perda` |
| **Status final** | `ganho` | `perdido` |
| **Campo validado** | Campos de contrato | `Motivo da Perda` |
| **Pós-aprovação** | Vincula com task cliente | Apenas atualiza status |
| **Nós** | 15 | 11 |

---

## Credenciais

| Serviço | Credencial |
|:--------|:-----------|
| RabbitMQ | `RabbitMQ` |
| ClickUp | `ClickUp - Ferramentas` |

---

## Troubleshooting

| Problema | Causa | Solução |
|:---------|:------|:--------|
| Mensagem reprocessada | RabbitMQ reentregou | Normal — nó If descarta redelivered |
| Sempre reprovado | Campo obrigatório vazio no ClickUp | Hunter deve preencher antes de mover |
| Vinculação falha | Task cliente não encontrada | Verificar se 002.001 criou a task |
| Tag não atualiza | ID do campo mudou | Verificar IDs no payload da 002.000 |