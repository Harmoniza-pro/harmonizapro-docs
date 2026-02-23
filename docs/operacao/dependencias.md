# Mapa de Dependências

> Visão completa de como cada componente do sistema se conecta. Use estes diagramas para entender o impacto de qualquer mudança.

---

## Visão Geral do Sistema

```mermaid
graph TB
    subgraph ENTRADA["🟢 Entrada de Leads"]
        TF[Typeform<br>Funil Anti-Curioso]
        WH[WhatsApp<br>Mensagem do lead]
    end

    subgraph N8N["⚙️ n8n — Orquestração"]
        CT[Chamada Typeform<br><i>VPVYN9AzG8IGnKiR</i>]
        AG[Agente de IA<br><i>8hdajgWAADbHorQF</i>]
        TT[Tool Transferir<br><i>Gt60I1KPG4ReJSIe</i>]
        FU[Fluxo Follow Ups<br><i>W1msnd1vZWkpFSDM</i>]
    end

    subgraph IA["🧠 Inteligência Artificial"]
        CS4[Claude Sonnet 4<br><i>Principal</i>]
        GPT5[GPT-5<br><i>Fallback</i>]
        CS45[Claude Sonnet 4.5<br><i>Contingência</i>]
        MINI[GPT-4o Mini<br><i>Resumos</i>]
        WHISP[Whisper<br><i>Áudio</i>]
        GPT4O[GPT-4o<br><i>Imagens</i>]
        GEM[Gemini<br><i>Vídeo/Docs</i>]
    end

    subgraph DADOS["💾 Dados"]
        SB[(Supabase<br>PostgreSQL)]
        RD[(Redis<br>Fila)]
    end

    subgraph API["📡 APIs Externas"]
        UA[UaZapi<br>WhatsApp API]
    end

    TF -->|webhook POST| CT
    WH -->|via UaZapi| AG
    CT -->|cria lead + 1ª msg| SB
    CT -->|envia msg| UA
    AG -->|lê/escreve| SB
    AG -->|fila de msgs| RD
    AG -->|gera resposta| CS4
    AG -->|fallback| GPT5
    AG -->|rate limit| CS45
    AG -->|transcreve| WHISP
    AG -->|analisa img| GPT4O
    AG -->|analisa vid/doc| GEM
    AG -->|envia resposta| UA
    AG -->|tool transferir| TT
    TT -->|resume conversa| MINI
    TT -->|alerta Hunter| UA
    TT -->|marca transferido| SB
    FU -->|busca leads| SB
    FU -->|envia follow-up| UA
    FU -->|salva na memória| SB

    style ENTRADA fill:#2E7D32,color:#fff
    style N8N fill:#1565C0,color:#fff
    style IA fill:#6A1B9A,color:#fff
    style DADOS fill:#E65100,color:#fff
    style API fill:#C8A24E,color:#1A1A1A
```

---

## Dependências por Workflow

### Agente de IA — o mais complexo

```mermaid
graph LR
    subgraph TRIGGER["Trigger"]
        W[Webhook POST<br>/harmonizapro]
    end

    subgraph SUPABASE["Supabase (5 tabelas)"]
        T1[leads]
        T2[clinicas_com_atendentes]
        T3[protocolos]
        T4[n8n_chat_histories]
        T5[instancias_whatsapp]
    end

    subgraph REDIS["Redis"]
        R1[Fila de mensagens]
    end

    subgraph MODELOS["Modelos IA"]
        M1[Claude Sonnet 4]
        M2[GPT-5]
        M3[Claude Sonnet 4.5]
        M4[Whisper]
        M5[GPT-4o]
        M6[Gemini]
    end

    subgraph TOOLS["Tools do Agente"]
        TL1[buscar_lead]
        TL2[buscar_clinica]
        TL3[buscar_protocolo]
        TL4[transferir]
    end

    subgraph SAIDA["Saída"]
        UA[UaZapi /send/text]
        HO[Tool Transferir<br>webhook]
    end

    W --> T1
    W --> T2
    W --> T3
    W --> T5
    W --> R1
    T1 --> M1
    M1 --> UA
    M2 --> UA
    M3 --> UA
    M4 --> M1
    M5 --> M1
    M6 --> M1
    TL1 --> T1
    TL2 --> T2
    TL3 --> T3
    TL4 --> HO
    M1 --> T4

    style TRIGGER fill:#2E7D32,color:#fff
    style SUPABASE fill:#E65100,color:#fff
    style REDIS fill:#B71C1C,color:#fff
    style MODELOS fill:#6A1B9A,color:#fff
    style TOOLS fill:#1565C0,color:#fff
    style SAIDA fill:#C8A24E,color:#1A1A1A
```

---

### Chamada Typeform

```mermaid
graph LR
    TF[Typeform] -->|POST| WH[Webhook<br>/typeform/hamoniza.pro]
    WH --> ORG[Organizar dados]
    ORG --> SB1[(instancias_whatsapp)]
    ORG --> SB2[(leads)]
    SB2 -->|novo?| CREATE[Criar lead]
    SB2 -->|existe| EXIST[Lead existente]
    CREATE --> BUDGET{Budget alto?}
    BUDGET -->|sim| HAND[Handoff direto]
    BUDGET -->|não| IA[IA gera 1ª msg]
    EXIST --> IA2[IA com contexto]
    IA --> UA[UaZapi /send/text]
    IA2 --> UA
    HAND --> UA
    IA -->|salva| SB3[(leads)]
    
    style TF fill:#2E7D32,color:#fff
    style BUDGET fill:#C8A24E,color:#1A1A1A
```

---

### Tool Transferir

```mermaid
graph LR
    AG[Agente de IA<br>tool: transferir] -->|POST| WH[Webhook<br>/handoff-agenteia]
    WH --> SB1[(leads<br>remotejid → clinica_id)]
    WH --> FLAG[leads.transferido = true]
    SB1 --> SB2[(clinicas_com_atendentes<br>→ hunter)]
    SB2 --> SB3[(instancias_whatsapp<br>→ server_url)]
    SB3 --> SB4[(n8n_chat_histories<br>→ histórico)]
    SB4 -->|tem histórico| RESUMO[GPT-4o Mini<br>resumo 50 palavras]
    SB4 -->|sem histórico| SIMPLES[Handoff simples]
    RESUMO --> UA[UaZapi /send/text<br>→ Hunter]
    SIMPLES --> UA

    style AG fill:#1565C0,color:#fff
    style RESUMO fill:#6A1B9A,color:#fff
    style UA fill:#C8A24E,color:#1A1A1A
```

---

### Fluxo Follow Ups

```mermaid
graph TB
    CRON[Schedule<br>a cada 11 min] --> HC{Horário<br>comercial?}
    HC -->|não| STOP[Para]
    HC -->|sim| DADOS[Dados UaZapi]
    DADOS --> FUP1[Rodada 1]
    DADOS --> FUP2[Rodada 2]
    DADOS --> FUP3[Rodada 3]
    DADOS --> FUP4[Rodada 4]
    
    FUP1 --> BUSCA1[Buscar leads<br>elegíveis]
    BUSCA1 --> FILTRO1[Filtrar +<br>dedup]
    FILTRO1 --> ENVIO1[Enviar msg]
    ENVIO1 --> MARCA1[Marcar +<br>salvar memória]

    FUP1 --> MERGE[Juntar todos]
    FUP2 --> MERGE
    FUP3 --> MERGE
    FUP4 --> MERGE
    MERGE --> SAVE[Salvar lista<br>de enviados]

    style CRON fill:#2E7D32,color:#fff
    style HC fill:#C8A24E,color:#1A1A1A
    style STOP fill:#B71C1C,color:#fff
```

---

## Matriz de Dependências

Referência rápida: se algo quebrar, saiba o que é afetado.

### Se uma API cair...

| API fora do ar | Workflows afetados | Impacto | Severidade |
|:---------------|:-------------------|:--------|:-----------|
| **UaZapi** | Todos | Nenhuma mensagem é enviada/recebida | 🔴 Crítico |
| **Supabase** | Todos | Sem dados de leads, clínicas, memória | 🔴 Crítico |
| **Redis** | Agente de IA | Fila de mensagens para de funcionar, respostas duplicadas | 🟡 Alto |
| **Anthropic (Claude)** | Agente de IA | IA principal cai, fallback para GPT-5 | 🟡 Alto |
| **OpenAI** | Agente de IA, Chamada Typeform, Tool Transferir | GPT-5 fallback cai, Whisper para, resumos param | 🟡 Alto |
| **Google (Gemini)** | Agente de IA | Análise de vídeo e documentos para | 🟢 Médio |
| **Typeform** | Chamada Typeform | Novos leads não entram (mas existentes continuam) | 🟢 Médio |

### Se uma tabela Supabase for comprometida...

| Tabela | Leitura por | Escrita por | Se cair |
|:-------|:-----------|:-----------|:--------|
| `leads` | Agente, Typeform, Transferir, Follow Ups | Typeform, Agente, Transferir | Nenhum workflow funciona |
| `clinicas_com_atendentes` | Agente, Typeform, Transferir | — (manual) | Agente não sabe de qual clínica é o lead |
| `protocolos` | Agente, Typeform | — (manual) | Agente perde personalização por clínica |
| `n8n_chat_histories` | Agente, Transferir | Agente, Follow Ups | IA perde memória, handoff sem resumo |
| `instancias_whatsapp` | Agente, Typeform, Transferir | — (manual) | Sem URL/token do WhatsApp |

### Comunicação entre workflows

| De | Para | Método | Dado trafegado |
|:---|:-----|:-------|:---------------|
| Chamada Typeform | Agente de IA | Indireto (lead criado no Supabase) | `clinica_id`, `instancia_id`, dados do Typeform |
| Agente de IA | Tool Transferir | HTTP POST webhook | `telefone`, `motivo` |
| Tool Transferir | Agente de IA | Indireto (`leads.transferido = true`) | Flag que para o agente |
| Fluxo Follow Ups | Agente de IA | Indireto (msg salva em `n8n_chat_histories`) | Contexto de follow-up na memória |

---

## Credenciais Compartilhadas

| Credential | Serviço | Usada em |
|:-----------|:--------|:---------|
| `ferramentas@harmoniza.pro` (Supabase) | Supabase | Todos os 4 workflows |
| `ferramentas@harmoniza.pro` (Anthropic) | Claude API | Agente de IA, Chamada Typeform |
| `ferramentas@harmoniza.pro` (OpenAI) | OpenAI API | Agente de IA, Chamada Typeform, Tool Transferir |
| `ferramentas@harmoniza.pro` (Google) | Gemini API | Agente de IA |
| `ferramentas@harmoniza.pro` (Redis) | Redis | Agente de IA |
| `ferramentas@harmoniza.pro (Agente IA)` (Postgres) | PostgreSQL direto | Agente de IA (memória) |

!!! warning "Ponto único de falha"
    Todas as credenciais estão sob `ferramentas@harmoniza.pro`. Se essa conta for comprometida ou expirar, **todos os workflows param**. Considere separar credenciais por serviço ou ter backup.
