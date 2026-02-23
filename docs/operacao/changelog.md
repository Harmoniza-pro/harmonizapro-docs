# Changelog

> Registro de todas as alterações nos workflows, integrações e regras de negócio do sistema. Mantenha este log atualizado a cada mudança significativa.

---

## Como usar este changelog

Toda alteração no sistema deve ser registrada aqui seguindo o formato:

```markdown
### [DATA] — Título da mudança

**Autor:** Nome
**Workflow(s):** Nome do workflow afetado
**Tipo:** ✨ Feature | 🐛 Fix | ⚡ Melhoria | 🔧 Refactor | 📝 Docs | 🚨 Hotfix

Descrição do que mudou e por quê.
```

---

## 2026

### [2026-02-23] — Documentação técnica completa do sistema

**Autor:** Pedro Vinicius
**Workflow(s):** Todos
**Tipo:** 📝 Docs

Criação da documentação técnica completa do sistema de qualificação via IA, incluindo:

- PRD 001 do Agente de Qualificação
- Documentação detalhada dos 4 workflows (Agente de IA, Chamada Typeform, Tool Transferir, Fluxo Follow Ups)
- Playbooks de abordagem por perfil e respostas para objeções
- Runbooks de troubleshooting (webhook fora, handoff falhando)
- Base de conhecimento de 5 clínicas
- Dashboard de métricas e KPIs
- Mapa de dependências completo
- Análise de custos por workflow

---

### [2026-02-20] — Agente de IA v3: Multi-modelo com contingência

**Autor:** Pedro Vinicius
**Workflow(s):** Agente de IA
**Tipo:** ✨ Feature

Implementação do sistema de contingência multi-modelo:

- Modelo principal: Claude Sonnet 4 + GPT-5
- Contingência em rate limit: Claude Sonnet 4.5
- Retry automático após 15 segundos
- Fallback transparente (lead não percebe a troca)

---

### [2026-02-19] — Processamento de mídia (áudio, imagem, vídeo, docs)

**Autor:** Pedro Vinicius
**Workflow(s):** Agente de IA
**Tipo:** ✨ Feature

Agente agora processa 4 tipos de mídia além de texto:

- Áudio → OpenAI Whisper (transcrição)
- Imagem → GPT-4o (análise visual)
- Vídeo → Google Gemini (análise de conteúdo)
- Documento → Google Gemini (extração de texto)

Mídia convertida é injetada como texto no contexto do agente.

---

### [2026-02-18] — Sistema de fila Redis

**Autor:** Pedro Vinicius
**Workflow(s):** Agente de IA
**Tipo:** ⚡ Melhoria

Implementação de fila com Redis para agrupar mensagens consecutivas de um mesmo lead. Antes, o agente respondia cada mensagem individualmente (causando respostas fragmentadas). Agora, aguarda um buffer de tempo, agrupa tudo e responde de uma vez.

---

### [2026-02-16] — Tool Transferir com resumo inteligente

**Autor:** Pedro Vinicius
**Workflow(s):** Tool Transferir
**Tipo:** ✨ Feature

Handoff agora inclui resumo automático da conversa gerado por GPT-4o Mini (máx 50 palavras). Hunter recebe contexto completo do lead sem precisar ler toda a conversa.

Dois caminhos: com resumo (quando há histórico) e sem resumo (fallback).

---

### [2026-02-14] — Fluxo de Follow Ups (4 rodadas)

**Autor:** Pedro Vinicius
**Workflow(s):** Fluxo Follow Ups
**Tipo:** ✨ Feature

Criação do sistema de reengajamento automático com 4 rodadas progressivas:

- Scheduler a cada 11 minutos
- Verificação de horário comercial + tratamento de sábado
- Anti-duplicidade por rodada
- Mensagens salvas na memória do agente
- Status: em desenvolvimento (workflow inativo)

---

### [2026-02-12] — Chamada Typeform com split de budget

**Autor:** Pedro Vinicius
**Workflow(s):** Chamada Typeform
**Tipo:** ⚡ Melhoria

Lead com budget alto agora é encaminhado diretamente para a Hunter (pula qualificação por IA). Anti-duplicidade implementada para evitar reprocessamento de formulários.

---

## Template para novas entradas

```markdown
### [AAAA-MM-DD] — Título da mudança

**Autor:** Nome
**Workflow(s):** Nome do workflow
**Tipo:** ✨ Feature | 🐛 Fix | ⚡ Melhoria | 🔧 Refactor | 📝 Docs | 🚨 Hotfix

Descrição do que mudou.

- Detalhe 1
- Detalhe 2
- Impacto: [descrever impacto em métricas ou operação]
```

!!! tip "Boas práticas"
    - Registre **antes** de mergear na main
    - Inclua o **motivo** da mudança, não só o que mudou
    - Se afeta métricas, descreva o **impacto esperado**
    - Se é hotfix, descreva o **incidente** que causou
    - Use as datas reais — o XX acima é placeholder para datas que precisam ser preenchidas
