# ⏱️ Métricas Diárias

!!! info "Visão Geral"
    Workflow automático que roda todo dia às 7h, calcula os KPIs operacionais do dia anterior e envia um relatório formatado via WhatsApp para o time.

## Ficha Técnica

| Campo | Valor |
|:------|:------|
| **Nome** | Métricas Diárias |
| **Instância** | `workflows.goldeletra.pro` |
| **Status** | 🟢 Ativo |
| **Nós** | 5 |
| **Trigger** | Schedule — `0 7 * * *` (todo dia às 7h) |
| **Execução média** | ~3 segundos |
| **Dependências** | Supabase, UaZapi |

---

## Arquitetura

```mermaid
flowchart LR
    A["⏰ Todo dia às 7h"] --> B["📊 Calcular métricas\nde ontem"]
    B --> C["🔍 Buscar resultado\ncalculado"]
    C --> D["📝 Formatar\nmensagem"]
    D --> E["📱 Enviar relatório\nWhatsApp"]
    
    F["🖱️ Teste manual"] --> B
    
    style A fill:#1a1a2e,stroke:#C8A24E,color:#fff
    style B fill:#1a1a2e,stroke:#C8A24E,color:#fff
    style C fill:#1a1a2e,stroke:#C8A24E,color:#fff
    style D fill:#1a1a2e,stroke:#C8A24E,color:#fff
    style E fill:#1a1a2e,stroke:#C8A24E,color:#fff
    style F fill:#333,stroke:#666,color:#999
```

---

## Nós em Detalhe

### 1. Todo dia às 7h
**Tipo:** `scheduleTrigger` v1.2

Cron expression: `0 7 * * *` — dispara todos os dias às 07:00 (horário do servidor).

Executa antes do início do expediente para que o time já tenha os números do dia anterior ao abrir o celular.

---

### 2. Calcular métricas de ontem
**Tipo:** `httpRequest` v4.2

Chama a função RPC `calcular_metricas_dia` no Supabase via REST API.

| Parâmetro | Valor |
|:----------|:------|
| **Method** | `POST` |
| **URL** | `https://jauunacntwpztmzgpeft.supabase.co/rest/v1/rpc/calcular_metricas_dia` |
| **Body** | `{ "p_data": "YYYY-MM-DD" }` (data de ontem, calculada dinamicamente) |

**Headers:**

| Header | Valor |
|:-------|:------|
| `apikey` | Service role key do Supabase |
| `Authorization` | `Bearer {service_role_key}` |
| `Content-Type` | `application/json` |

**O que a função faz no banco:**

1. Conta leads novos criados no dia (`leads.created_at`)
2. Conta total de leads na base
3. Conta handoffs realizados no dia (`leads.handoff_at`)
4. Calcula taxa de qualificação: `handoffs / leads_novos × 100`
5. Faz `UPSERT` na tabela `metricas_diarias` (atualiza se já existir)

---

### 3. Buscar resultado calculado
**Tipo:** `supabase` v1

Busca o registro recém-inserido na tabela `metricas_diarias` filtrando pela data de ontem.

| Parâmetro | Valor |
|:----------|:------|
| **Tabela** | `metricas_diarias` |
| **Operação** | `get` |
| **Filtro** | `data = YYYY-MM-DD` (ontem) |
| **Credencial** | `ferramentas@harmoniza.pro` |

**Campos retornados:**

| Campo | Tipo | Descrição |
|:------|:-----|:----------|
| `leads_novos` | integer | Leads que entraram no dia |
| `leads_total` | integer | Base acumulada total |
| `handoffs_realizados` | integer | Transferidos para Hunter |
| `taxa_qualificacao` | numeric | % de conversão lead → handoff |
| `followups_enviados` | integer | Follow-ups automáticos disparados |
| `taxa_reengajamento` | numeric | % que responderam após follow-up |
| `rate_limits` | integer | Vezes que a IA atingiu limite |
| `erros_execucao` | integer | Erros de execução no dia |
| `custo_total_ia` | numeric | Custo estimado em USD |

---

### 4. Formatar mensagem
**Tipo:** `set` v3.4

Monta a mensagem formatada para WhatsApp com os dados do dia:

```
📊 *MÉTRICAS DE ONTEM* (22/02)
━━━━━━━━━━━━━━━━━

📥 *Leads novos:* 12
📋 *Leads total:* 847
🤝 *Handoffs:* 5
🎯 *Taxa qualificação:* 41.7%

📤 *Follow-ups enviados:* 23
🔄 *Reengajamento:* 26.1%

⚠️ *Rate limits:* 3
❌ *Erros:* 0

💰 *Custo IA (USD):* $1.87
```

Usa bold do WhatsApp (`*texto*`) e emojis para facilitar leitura rápida.

---

### 5. Enviar relatório WhatsApp
**Tipo:** `httpRequest` v4.2

Envia a mensagem via API do UaZapi.

| Parâmetro | Valor |
|:----------|:------|
| **Method** | `POST` |
| **URL** | `{UAZAPI_URL}/send/text` |
| **Body** | `{ "number": "{NUMERO_RELATORIO}", "text": "{mensagem}" }` |

**Headers:**

| Header | Valor |
|:-------|:------|
| `token` | Token da instância UaZapi |

O número pode ser um telefone individual ou um grupo do WhatsApp.

---

## Tabela: metricas_diarias

```sql
CREATE TABLE metricas_diarias (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  data                  DATE NOT NULL UNIQUE,
  leads_novos           INTEGER DEFAULT 0,
  leads_total           INTEGER DEFAULT 0,
  mensagens_processadas INTEGER DEFAULT 0,
  handoffs_realizados   INTEGER DEFAULT 0,
  taxa_qualificacao     NUMERIC(5,2) DEFAULT 0,
  followups_enviados    INTEGER DEFAULT 0,
  followups_respondidos INTEGER DEFAULT 0,
  taxa_reengajamento    NUMERIC(5,2) DEFAULT 0,
  rate_limits           INTEGER DEFAULT 0,
  erros_execucao        INTEGER DEFAULT 0,
  contingencias_usadas  INTEGER DEFAULT 0,
  custo_anthropic       NUMERIC(10,4) DEFAULT 0,
  custo_openai          NUMERIC(10,4) DEFAULT 0,
  custo_total_ia        NUMERIC(10,4) DEFAULT 0,
  calculado_em          TIMESTAMPTZ DEFAULT NOW()
);
```

**RLS:** Leitura pública habilitada (dados não-sensíveis, usados pelo dashboard da documentação).

---

## Views Disponíveis

| View | Descrição |
|:-----|:----------|
| `ultimas_metricas` | Últimos 30 dias de métricas |
| `metricas_semana` | Resumo agregado da última semana |

---

## Variáveis de Ambiente

| Variável | Descrição | Onde configurar |
|:---------|:----------|:----------------|
| `SUPABASE_URL` | URL do projeto Supabase | n8n → Settings → Variables |
| `SUPABASE_KEY` | Service role key (escrita) | n8n → Settings → Variables |
| `UAZAPI_URL` | URL do servidor UaZapi | n8n → Settings → Variables |
| `UAZAPI_TOKEN` | Token da instância | n8n → Settings → Variables |
| `NUMERO_RELATORIO` | Telefone/grupo que recebe | n8n → Settings → Variables |

!!! warning "Atenção"
    As URLs do Supabase estão hardcoded nos nós HTTP Request para evitar problemas de `https://` duplicado. Se o projeto Supabase mudar, atualize diretamente nos nós.

---

## Troubleshooting

| Problema | Causa | Solução |
|:---------|:------|:--------|
| Erro `ENOTFOUND` | URL com `https://` duplicado | Verificar se a URL no nó está sem expressão `{{ }}` |
| Erro `42883 function not found` | Função não existe no Supabase | Executar o SQL de criação da função `calcular_metricas_dia` |
| Métricas zeradas | Tabela `leads` sem dados no dia | Normal se não houve leads; verificar se `created_at` está populado |
| WhatsApp não recebe | Token ou número errado | Verificar variáveis `UAZAPI_TOKEN` e `NUMERO_RELATORIO` |
| Dados duplicados | — | Impossível: tabela tem `UNIQUE(data)` e função usa `ON CONFLICT` |

---

## Consumo na Documentação

A página **Dashboard de Métricas** (`docs/dashboard.md`) consome os dados desta tabela em tempo real via JavaScript + Supabase REST API, usando a **anon key** (read-only).

O dashboard atualiza automaticamente ao abrir a página — não precisa de refresh manual.