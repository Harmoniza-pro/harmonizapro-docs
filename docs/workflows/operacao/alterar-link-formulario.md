# 🔗 003.001 — Alterar Link do Formulário

!!! info "Visão Geral"
    Workerflow que consome a fila RabbitMQ `clientes_alterar_link_form`, busca os dados do cliente no ClickUp e atualiza o campo customizado de link do formulário nas tarefas relacionadas. Trabalha em par com o workflow `003.000 - Central de Automação`.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **Nome** | 003.001 - Gestão de Clientes - Alterar Link do Formulário |
| **ID** | `NzmHd3edF1NQW1Re` |
| **Instância** | `workflows.goldeletra.pro` |
| **Status** | 🟢 Ativo |
| **Nós** | 11 |
| **Trigger** | RabbitMQ — fila `clientes_alterar_link_form` |
| **Dependências** | RabbitMQ, ClickUp |

---

## Arquitetura

```mermaid
flowchart TD
    A["🐇 RabbitMQ Trigger\nclientes_alterar_link_form"] --> B{"❓ If\nMensagem válida?"}
    B -->|Não| C["🐇 Requeue\nDevolver à fila"]
    B -->|Sim| D["📋 Get a task\nBuscar dados do cliente"]
    D --> E["⚙️ Organizar campos\ncustom fields → JSON"]
    E --> F["✏️ Set custom field\nAtualizar link"]
    
    G["🖱️ Execução manual"] --> H["📋 Get many tasks\nBuscar todas as tasks"]
    H --> I["🔄 Loop\nProcessar em lote"]
    I --> J["⚙️ Organizar campos"]
    J --> K["✏️ Set custom field"]
    K --> I
    
    style A fill:#1a1a2e,stroke:#ff6600,color:#fff
    style B fill:#1a1a2e,stroke:#f97316,color:#fff
    style D fill:#1a1a2e,stroke:#7B68EE,color:#fff
    style F fill:#1a1a2e,stroke:#7B68EE,color:#fff
    style G fill:#333,stroke:#666,color:#999
```

---

## Nós em Detalhe

### 1. RabbitMQ Trigger
**Tipo:** `rabbitmqTrigger`

Consome mensagens da fila `clientes_alterar_link_form` publicadas pelo workflow 003.000.

| Parâmetro | Valor |
|:----------|:------|
| **Fila** | `clientes_alterar_link_form` |
| **Credencial** | `RabbitMQ` |

---

### 2. If — Validação
**Tipo:** `if` v2.2

Verifica se a mensagem contém dados válidos antes de prosseguir. Se inválida, devolve à fila (requeue).

---

### 3. Get a task
**Tipo:** `clickUp` v1

Busca os dados completos da task do cliente usando o `task_id` recebido na mensagem.

---

### 4. OrganizarClickUp
**Tipo:** `code` v2 (JavaScript)

Transforma os custom fields do ClickUp em um JSON estruturado, tratando diferentes tipos de campo (users, dropdown, labels, tasks, emoji).

---

### 5. Set a custom Field on a task
**Tipo:** `clickUp` v1

Atualiza o campo customizado de link do formulário na task do cliente.

---

### Fluxo alternativo: Execução em lote

O workflow também possui um fluxo de execução manual para processar todas as tasks em lote:

1. **Get many tasks** → busca todas as tasks da lista
2. **Loop Over Items** → processa uma por uma
3. **OrganizarClickUp1** → normaliza campos
4. **Set custom field** → atualiza cada task

---

## Integração com 003.000

```mermaid
sequenceDiagram
    participant CU as ClickUp
    participant C0 as 003.000 Central
    participant MQ as RabbitMQ
    participant C1 as 003.001 Alterar Link
    
    CU->>C0: taskUpdated (campo Hunter)
    C0->>MQ: Publish → clientes_alterar_link_form
    MQ->>C1: Consume message
    C1->>CU: Get task details
    CU-->>C1: Task data + custom fields
    C1->>CU: Set custom field (link)
```

---

## Credenciais

| Serviço | Credencial | Uso |
|:--------|:-----------|:----|
| RabbitMQ | `RabbitMQ` | Consumo de fila |
| ClickUp | `ClickUp - Ferramentas` | Leitura e escrita de tasks |

---

## Troubleshooting

| Problema | Causa | Solução |
|:---------|:------|:--------|
| Mensagens acumulando na fila | Worker parado | Verificar se workflow está ativo |
| Task não encontrada | `task_id` inválido | Verificar payload do 003.000 |
| Custom field não atualiza | ID do campo desatualizado | Comparar IDs no ClickUp |
| Requeue infinito | Mensagem corrompida | Verificar dead letter queue no RabbitMQ |