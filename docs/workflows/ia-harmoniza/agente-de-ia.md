# Agente de IA

> Workflow principal do sistema. Recebe mensagens do WhatsApp, processa com IA e responde ao lead de forma natural e humanizada.

| Campo | Valor |
|:------|:------|
| **ID** | `8hdajgWAADbHorQF` |
| **Status** | ✅ Ativo |
| **Trigger** | Webhook POST `/harmonizapro` |
| **Nós** | 92 |
| **IA Principal** | Claude Sonnet 4 (fallback: GPT-5) |
| **IA Contingência** | Claude Sonnet 4.5 |

---

## Objetivo

Receber toda mensagem enviada por um lead no WhatsApp, processar com inteligência artificial (incluindo texto, áudio, imagem, vídeo e documentos) e responder de forma natural, humanizada e estratégica — qualificando o lead e conduzindo-o ao agendamento.

---

## Fluxo Completo

```
Webhook POST /harmonizapro
    │
    ▼
Organizar dados (instância, sender, servidor UaZapi)
    │
    ▼
Buscar Usuário (Supabase: leads)
    │
    ▼
Buscar Clínica + Protocolo (Supabase)
    │
    ▼
Cadastrado no Typeform?
    ├── NÃO → Ignorar (lead não veio do funil)
    │
    └── SIM → Avaliar Mensagem
                ├── "reset"    → Deletar Memória + Resetar conversa
                ├── "excluir"  → Apagar contato + Memória
                ├── "destrans" → Destransferir lead
                │
                └── Mensagem normal → Verificar se está transferido
                                       ├── SIM → Não responder (Hunter cuida)
                                       │
                                       └── NÃO → Enviado pelo usuário?
                                                  ├── NÃO → Ignorar (msg do bot)
                                                  │
                                                  └── SIM → Registrar última msg
                                                             │
                                                             ▼
                                                    SISTEMA DE FILA (Redis)
                                                             │
                                                             ▼
                                                    Processar com IA
                                                             │
                                                             ▼
                                                    Formatar + Enviar resposta
```

---

## Entrada (Webhook)

O webhook recebe um POST da UaZapi sempre que chega uma mensagem no WhatsApp da clínica.

**Endpoint:** `POST /harmonizapro`

**Payload esperado:** Objeto com dados da mensagem (remetente, conteúdo, tipo de mídia, instância).

---

## Fase 1 — Organização e Validação

### Organizar

Extrai do payload: `server_url` (UaZapi), `sender` (telefone do lead), dados da instância.

### Buscar Usuário

Consulta a tabela `leads` no Supabase pelo `remotejid` (telefone). Retorna dados do lead incluindo `clinica_id`, `instancia_id`, status de transferência e dados do Typeform.

### Buscar Clínica + Protocolo

Com o `clinica_id`, busca na tabela `clinicas_com_atendentes` e depois em `protocolos`. Esses dados alimentam o prompt do agente para personalizar a conversa conforme a clínica.

### Cadastrado?

Verifica se o lead veio do Typeform (Funil Anti-Curioso). Se não veio, o agente **não responde** — evita interagir com mensagens aleatórias.

---

## Fase 2 — Avaliação da Mensagem

O nó **Avaliar Mensagem** é um `switch` que avalia o conteúdo:

| Comando | Ação | Resposta ao lead |
|:--------|:-----|:-----------------|
| `reset` | Deleta memória da conversa (`n8n_chat_histories`) | "Conversa redefinida ✅" |
| `excluir` | Apaga lead + memória completamente | "Contato excluído ✅" |
| `destrans` | Remove flag de transferência | "Lead destransferido ✅" |
| Mensagem normal | Segue para verificação de transferência | — |

### Verificação de Transferência

Se o lead já foi transferido para a Hunter (`transferido = true`), o agente **para de responder**. A Hunter assume o controle da conversa.

### Enviado pelo Usuário?

Filtra mensagens enviadas pelo próprio bot (evita loop). Só processa mensagens reais do lead.

---

## Fase 3 — Sistema de Fila (Redis)

O workflow implementa uma fila inteligente com Redis para lidar com leads que enviam múltiplas mensagens seguidas (ex: "oi" + "tudo bem?" + áudio). Em vez de responder cada uma individualmente, o sistema agrupa tudo e responde de uma vez.

### Como funciona:

1. **Adicionar na fila** — A mensagem é salva no Redis com chave única por lead
2. **Espera inicial** — Aguarda alguns segundos para capturar mensagens subsequentes
3. **Puxar fila** — Busca todas as mensagens acumuladas
4. **Verifica fila:**
    - Se vazia → Ignora (já foi processada)
    - Se tem mensagens → Limpa fila e processa tudo junto
    - Se ainda está recebendo → Espera adicional e tenta de novo

---

## Fase 4 — Processamento de Mídia

O agente aceita 4 tipos de mídia além de texto:

| Tipo | Processamento | Tecnologia |
|:-----|:-------------|:-----------|
| **Texto** | Direto para o agente | — |
| **Áudio** | Download → Transcrição | OpenAI Whisper |
| **Imagem** | Download → Análise visual | OpenAI GPT-4o |
| **Vídeo** | Download → Análise de conteúdo | Google Gemini |
| **Documento** | Download → Extração de texto | Google Gemini |

### Fluxo de mídia:

```
Mensagem com mídia
    │
    ▼
Download via UaZapi (/message/download)
    │
    ▼
Converter em binário
    │
    ▼
Tipo de Mídia? (switch)
    ├── audio → Whisper (transcrição)
    ├── image → GPT-4o ("descreva a imagem")
    ├── video → Gemini ("analise o vídeo")
    └── document → Gemini ("analise o documento")
    │
    ▼
Setar resultado como texto
    │
    ▼
Unir com mensagens de texto (Merge)
    │
    ▼
Concatenar tudo → Enviar ao Agente
```

---

## Fase 5 — Agente de IA (Cérebro)

### Modelo Principal

**Claude Sonnet 4** (`claude-sonnet-4-20250514`) com fallback para **GPT-5** (`gpt-5`).

### Prompt

O prompt é montado dinamicamente com dados da clínica e protocolo, injetados pelo nó **Prompt** antes de chegar ao agente.

### Tools (Ferramentas do Agente)

O agente tem acesso a 4 ferramentas que pode chamar durante a conversa:

| Tool | Tipo | Descrição |
|:-----|:-----|:----------|
| `buscar_lead` | Supabase (`leads`) | Consulta dados do lead (nome, telefone, budget, etc.) |
| `buscar_clinica` | Supabase (`clinicas_com_atendentes`) | Busca dados da clínica (nome, endereço, Hunter) |
| `buscar_protocolo` | Supabase (`protocolos`) | Busca protocolo da clínica (nome, descrição, preço) |
| `transferir` | HTTP Request | Aciona o workflow **Tool Transferir** para handoff |

### Memória

Usa **Supabase (PostgreSQL)** como memória persistente via `memoryPostgresChat`. A conversa inteira fica salva na tabela `n8n_chat_histories` indexada por `session_id` (telefone do lead).

### Agente de Contingência

Se o agente principal retorna rate limit (HTTP 429), o sistema:

1. Detecta o erro no nó **Rate limit**
2. Espera 15 segundos
3. Tenta novamente com o **Agente Contingência** (Claude Sonnet 4.5 `claude-sonnet-4-5-20250929`)

Se o agente de contingência também falhar, repete o ciclo.

### Agente de Teste

Existe um caminho alternativo ativado pelo **Chat Trigger** interno do n8n para testes manuais. Usa **Claude Sonnet 4.5** com **memória em buffer** (não persiste).

---

## Fase 6 — Formatação e Envio

Depois que o agente gera a resposta, o texto passa por uma pipeline de formatação:

1. **Normaliza `\n`** — Corrige quebras de linha escapadas
2. **Remove `\` isoladas** — Limpa caracteres de escape soltos
3. **Quebra em mensagens** — Se a resposta tem 2+ parágrafos, divide em mensagens separadas para parecer mais natural
4. **Gerar itens** — Cada parágrafo vira um item individual
5. **Salvar resposta** — Registra no execution data

### Envio via UaZapi

```
POST {server_url}/send/text
Headers:
  token: {token_da_instancia}
Body:
  number: {telefone_do_lead}
  text: {mensagem}
```

O envio é feito em **batch** com `splitInBatches` — cada mensagem é enviada separadamente com um delay simulando digitação (`tempo random` + `espera`), para parecer mais humano.

### Pós-envio: Salvar na Memória

Após enviar a resposta, o sistema busca o registro na tabela `n8n_chat_histories` e injeta o `content` real da mensagem (que pode ter chegado como áudio/imagem convertido). Isso garante que a memória reflita o que realmente foi dito.

---

## Tabelas Supabase Utilizadas

| Tabela | Operações | Finalidade |
|:-------|:----------|:-----------|
| `leads` | get, update, delete | Dados do lead, status de transferência, última mensagem |
| `clinicas_com_atendentes` | get | Dados da clínica, Hunter responsável |
| `protocolos` | get | Protocolo da clínica (nome, descrição, valor) |
| `n8n_chat_histories` | getAll, update, delete | Memória da conversa com o lead |
| `instancias_whatsapp` | get | URL do servidor UaZapi, token |

---

## Credenciais

| Serviço | Credential | Uso |
|:--------|:-----------|:----|
| Supabase | `ferramentas@harmoniza.pro` | Banco de dados |
| Anthropic | `ferramentas@harmoniza.pro` | Claude Sonnet 4 + 4.5 |
| OpenAI | `ferramentas@harmoniza.pro` | GPT-5, Whisper, GPT-4o |
| Google | `ferramentas@harmoniza.pro` | Gemini (vídeo/docs) |
| Redis | `ferramentas@harmoniza.pro` | Fila de mensagens |
| PostgreSQL | `ferramentas@harmoniza.pro (Agente IA)` | Memória do agente |

---

## Comandos Administrativos

Enviados diretamente no WhatsApp para a instância:

| Comando | Efeito |
|:--------|:-------|
| `reset` | Limpa memória da conversa e recomeça do zero |
| `excluir` | Remove o lead e toda sua memória |
| `destrans` | Remove flag de transferência (agente volta a responder) |

---

## Troubleshooting

| Problema | Causa provável | Solução |
|:---------|:---------------|:--------|
| Agente não responde | Lead não veio do Typeform | Verificar se existe na tabela `leads` |
| Agente não responde | Lead está transferido | Enviar `destrans` para destravar |
| Resposta cortada | Output vazio do agente | Verificar nó "Tem output?" — pode ser rate limit |
| Rate limit constante | Muitas requisições ao Claude | Verificar se Agente Contingência está funcionando |
| Áudio não processado | Falha no download UaZapi | Checar URL do servidor e token |
| Memória inconsistente | Mensagens de mídia sem content | Verificar pipeline de "Inserir conteúdo" |