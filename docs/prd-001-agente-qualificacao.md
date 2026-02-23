# PRD 001 — Agente de Qualificação IA

> **Data de solicitação:** 2 de fevereiro de 2026  
> **Departamento beneficiado:** Hunters  
> **Prioridade:** 🟠 Alta  
> **Solicitado por:** Luciano Alberti  
> **Versão:** 1.0

---

## Checklist Inicial

- [ ] Levantar históricos de abordagens que tiveram sucesso (exemplos ligando resposta do formulário e abordagem inicial)
- [ ] Deixar base de dados/cliente protocolo 100% redonda
- [ ] Playbook SDRs

---

## 1. Problema / Dor

**Qual problema estamos resolvendo?**

Hunters perdem tempo iniciando conversa com leads que não são oportunidades reais. Muitos leads preenchem formulário mas não respondem, não têm budget, ou são apenas curiosos. A Hunter deveria entrar só quando o lead já está aquecido e qualificado.

**Contexto atual:**

- Lead preenche formulário
- Hunter entra em contato manualmente
- Hunter gasta tempo com leads frios/curiosos
- Leads quentes às vezes demoram pra receber atenção porque Hunter está ocupada com leads ruins
- Não há filtro automático entre "curioso" e "oportunidade"

**Impacto:**

- Hunters sobrecarregadas com volume de leads não qualificados
- Leads quentes podem esfriar esperando
- Tempo de venda desperdiçado em qualificação básica
- Escala limitada pelo número de Hunters

---

## 2. Objetivo & Resultado Esperado

**Objetivo principal:**

Criar um agente de IA que inicia a conversa com cada lead, qualifica, aquece, e entrega para a Hunter apenas os leads que são de fato uma oportunidade — prontos para agendar.

**O agente deve:**

1. Iniciar relacionamento de forma acolhedora
2. Descobrir contexto e dores do lead
3. Apresentar o protocolo (elevar nível de consciência)
4. Confirmar se faz sentido para o lead
5. Passar para Hunter quando lead estiver qualificado

**Métricas de sucesso:**

| Métrica | Antes | Meta Depois |
|---------|-------|-------------|
| % de leads que Hunter atende que viram oportunidade | X% | > 70% |
| Tempo da Hunter por lead qualificado | X min | Reduzir 50% |
| Tempo entre form preenchido e primeiro contato | X min | < 2 min |
| Leads que não respondem filtrados automaticamente | 0% | 100% |

**Valor estimado:**

- Hunter foca só em leads quentes → mais agendamentos
- Resposta instantânea 24/7 → menos leads esfriando
- Escala sem contratar mais Hunters

---

## 3. Escopo da Solução

### O que DEVE fazer (Must Have)

#### Iniciar conversa

- [ ] Lead preenche typeform → Agente inicia conversa no WhatsApp em < 2 min
- [ ] Mensagem inicial personalizada com dados do formulário
- [ ] Tom acolhedor, se passa por humano

#### Qualificar

- [ ] Fazer perguntas para descobrir contexto e dores
- [ ] Entender se lead já se frustrou com outros procedimentos
- [ ] Coletar insumos para apresentar o protocolo
- [ ] Apresentar o protocolo (elevar nível de consciência)
- [ ] Confirmar se faz sentido para o lead

#### Handoff para Hunter

- [ ] Lead respondeu 3+ mensagens com engajamento → passa pra Hunter
- [ ] Lead demonstrou interesse em agendar → passa pra Hunter
- [ ] Lead marcou budget alto no form → Hunter entra direto
- [ ] Lead fez pergunta que agente não sabe → passa pra Hunter
- [ ] Handoff invisível (lead não percebe troca)

#### Follow-up automático

- [ ] Lead não respondeu → 5 follow-ups cadenciados ao longo de 7 dias
- [ ] Lead respondeu em qualquer momento → cadência para e agente retoma conversa
- [ ] Após 7 dias sem resposta → move para nutrição (integra com PRD 3)

#### Limitações do agente (regras rígidas)

- [ ] NÃO pode prometer desconto ou condição especial
- [ ] NÃO pode agendar consulta (só Hunter agenda)
- [ ] NÃO pode passar preço
- [ ] NÃO pode falar de procedimentos fora do protocolo
- [ ] Se lead perguntar de outro procedimento → direciona para o protocolo

### O que SERIA BOM fazer (Nice to Have)

- [ ] Dashboard de performance do agente (% qualificação, tempo médio, etc)
- [ ] A/B test de diferentes abordagens de mensagem inicial
- [ ] Análise de sentimento para detectar lead irritado → passa pra Hunter
- [ ] Resumo automático da conversa para Hunter quando faz handoff

### O que NÃO está no escopo

- Agendar consulta (entra no PRD 2)
- Atualizar ClickUp (entra no PRD 3)
- Enviar áudio (apenas texto)
- Atender leads de canais diferentes do formulário Anti-Curioso

---

## 4. Usuários & Personas

**Quem interage com o sistema:**

| Usuário | Função | Interação |
|---------|--------|-----------|
| Lead | Potencial cliente | Conversa com agente no WhatsApp |
| Hunter | Vendas | Recebe lead qualificado, assume conversa |
| Gestão | Acompanhamento | Monitora performance do agente |

### Jornada do Lead (responde)

```
1. Preenche formulário (Anti-Curioso)
   ↓
2. Recebe msg do agente em < 2 min (WhatsApp)
   ↓
3. Agente faz perguntas, descobre dores
   ↓
4. Agente apresenta protocolo
   ↓
5. Lead engaja / demonstra interesse
   ↓
6. Hunter assume (lead não percebe)
   ↓
7. Hunter agenda consulta
```

### Jornada do Lead (não responde)

```
1. Preenche formulário
   ↓
2. Recebe msg do agente
   ↓
3. Não responde
   ↓
4. Follow-up 1 (após X horas)
   ↓
5. Follow-up 2, 3, 4, 5 (ao longo de 7 dias)
   ↓
6. Ainda não respondeu → Nutrição (PRD 3)
```

---

## 5. Integrações & Dependências

**Sistemas que precisam conversar:**

| Sistema | Função | Tipo | Acesso |
|---------|--------|------|--------|
| Typeform | Trigger de entrada | Webhook | [ ] Verificar |
| n8n | Orquestração do agente | Workflow | [ ] Configurar |
| LLM (Claude) | Cérebro do agente | API | [ ] Definir |
| WhatsApp (UaZapi) | Canal de conversa | API | [ ] Verificar |
| ClickUp | Atualizar status (via PRD 3) | API | [ ] Integrar |

### Dados de entrada (do formulário)

| Campo | Uso pelo agente |
|-------|-----------------|
| Nome | Personalizar conversa |
| Protocolo | Saber sobre o que falar |
| Procedimento que já fez | Contexto para conversa |
| Quanto está disposto a investir | Critério de qualificação (budget alto = Hunter direto) |
| O que mais incomoda no rosto | Dor principal para explorar |

### Dados da clínica (base de conhecimento)

| Informação | Necessário para |
|------------|-----------------|
| Nome do(a) Dr(a) | Personalizar, gerar confiança |
| Nome do protocolo | Apresentar corretamente |
| Informações do protocolo | Responder perguntas, elevar consciência |
| Público-alvo do protocolo | Qualificar se lead é fit |
| Dores que resolve | Conectar com dores do lead |
| Casos de sucesso | Gerar prova social |
| Localização | Informar se perguntarem |
| Formação do Dr(a) | Gerar autoridade |

!!! warning "AÇÃO NECESSÁRIA"
    Criar documento estruturado com essas informações para cada clínica.

---

## 6. Regras de Negócio

### Critérios de qualificação (quando passa pra Hunter)

**PASSA PRA HUNTER SE:**

- Lead marcou budget ALTO no formulário (entra direto, sem agente)
- Lead respondeu 3+ mensagens COM engajamento
- Lead demonstrou interesse explícito em agendar
- Lead fez pergunta que agente não sabe responder
- Lead pediu pra falar com humano

**NÃO PASSA (continua com agente ou vai pra nutrição):**

- Lead não responde
- Lead responde mas sem engajamento (respostas monossilábicas)
- Lead diz que não tem interesse agora

### Definição de "engajamento"

- Resposta com mais de 5 palavras
- Fez pergunta de volta
- Demonstrou curiosidade sobre o protocolo
- Compartilhou informação pessoal (dor, desejo, frustração)

### Regras de follow-up

| Follow-up | Quando | Tom |
|-----------|--------|-----|
| #1 | X horas após msg inicial | Lembrete leve |
| #2 | X horas após #1 | Reforço de valor |
| #3 | X horas após #2 | Urgência suave |
| #4 | X horas após #3 | Última tentativa |
| #5 | X horas após #4 | Despedida aberta |

!!! info "A definir"
    Definir intervalos exatos de cada follow-up.

### Regras de resposta do agente

**SE lead pergunta preço:**

> "O investimento varia de acordo com o seu caso específico. Na consulta, o Dr(a) [nome] vai avaliar e passar todos os detalhes. Posso te ajudar a entender melhor como funciona o protocolo?"

**SE lead pergunta de outro procedimento:**

> "Aqui na clínica o foco é o [nome do protocolo], que é um tratamento completo que [benefício principal]. Muitas pessoas que procuravam [procedimento que lead perguntou] acabaram tendo resultados ainda melhores com o protocolo. Quer que eu te explique como funciona?"

**SE lead pede desconto:**

> "Entendo! O valor do protocolo reflete toda a experiência e resultado que você vai ter. Na consulta, você vai entender exatamente o que está incluso. Posso te contar mais sobre o que faz o protocolo ser tão especial?"

**SE lead pergunta algo que agente não sabe:**

> → HANDOFF IMEDIATO PARA HUNTER

### Regras de handoff

- Hunter recebe notificação no WhatsApp (futuramente terá um front end)
- Hunter recebe resumo da conversa até o momento
- Hunter assume no mesmo número de WhatsApp
- Lead NÃO pode perceber que houve troca
- Transição deve ser seamless

---

## 7. Interface & Experiência

**Para o Lead:**

- Conversa normal no WhatsApp
- Não sabe que está falando com IA
- Tom acolhedor e humano
- Apenas texto (sem áudio)

**Para a Hunter:**

- Recebe notificação de lead qualificado
- Vê resumo da conversa (CRM ClickUp PRD 003)
- Assume conversa no mesmo número
- Continua de onde agente parou

**Para Gestão:**

- Dashboard de performance (nice to have)
- Logs de conversas para auditoria
- Métricas de qualificação

---

## 8. Requisitos Técnicos

**Plataforma:**

- n8n para orquestração
- LLM para geração de respostas (Claude)

**Performance:**

- Tempo de resposta do agente: < 90 segundos (mais humano; se lead responde na hora, agente responde na hora também para manter fluxo natural de conversa)
- Disponibilidade: 24/7
- Capacidade: múltiplas conversas simultâneas

**Segurança:**

- Dados de leads armazenados de forma segura
- Logs de conversa para auditoria
- Controle de acesso às configurações do agente

**Monitoramento:**

- Alertas se agente parar de funcionar
- Alertas se tempo de resposta aumentar
- Log de erros e exceções

---

## 9. Cronograma & Entregas

**Fases sugeridas:**

| Fase | Entrega | Descrição |
|------|---------|-----------|
| Fase 0 | Base de conhecimento | Documento estruturado de cada clínica |
| MVP | Agente básico | Inicia conversa + faz perguntas + handoff manual |
| V2 | Follow-ups | Cadência automática de 5 msgs em 7 dias |
| V3 | Handoff inteligente | Critérios automáticos de qualificação |
| V4 | Integração PRD 3 | Atualiza ClickUp automaticamente |

**Dependências:**

- [ ] Documento de cada clínica preenchido (Fase 0)
- [ ] Acesso à API do WhatsApp
- [ ] n8n configurado
- [ ] LLM escolhido e com acesso
- [ ] Exemplo de conversa ideal (para treinar tom do agente)
- [ ] Definição dos intervalos de follow-up

---

## 10. Riscos & Considerações

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Agente responde algo errado | Média | Alto | Regras rígidas + fallback pra Hunter |
| Lead percebe que é IA | Média | Médio | Tom humano, respostas naturais, não responder instantaneamente |
| Agente trava/para de funcionar | Baixa | Alto | Monitoramento + alertas + fallback manual |
| Lead reclama de demora | Baixa | Médio | Tempo de resposta < 30s |
| Handoff não funciona | Média | Alto | Testar exaustivamente antes de lançar |

**Pontos de atenção:**

- Agente mal configurado pode queimar lead — testar muito antes de ir pro ar
- Primeira versão deve ser conservadora (passa pra Hunter na dúvida)
- Monitorar primeiras conversas manualmente para ajustar

---

## 11. Materiais de Apoio

**Para o dev começar, preciso que você forneça:**

- [ ] Acesso ao n8n (ou onde vai rodar)
- [ ] Definição de qual LLM usar (GPT-4, Claude, etc)
- [ ] Acesso à API do WhatsApp
- [ ] Documento estruturado de cada clínica (criar antes de começar)
- [ ] Intervalos exatos dos 5 follow-ups
- [ ] Definição de onde Hunter recebe notificação de handoff

### Template — Documento da Clínica

```
CLÍNICA: [Nome]
DR(A): [Nome completo]
FORMAÇÃO: [Formação e credenciais]
LOCALIZAÇÃO: [Endereço]

PROTOCOLO: [Nome do protocolo]
O QUE É: [Descrição em 2-3 frases]
PÚBLICO-ALVO: [Quem é o cliente ideal]
DORES QUE RESOLVE: [Lista de dores]
DIFERENCIAIS: [O que torna único]
CASOS DE SUCESSO: [Exemplos/resultados]

PALAVRAS-CHAVE PARA USAR: [Tom de voz, termos específicos]
O QUE NÃO FALAR: [Termos proibidos, promessas que não pode fazer]
```

---

## 12. Exemplo de Conversa Ideal

!!! warning "A PREENCHER"
    Inserir aqui um exemplo de conversa ideal do agente com um lead, do início até o handoff para Hunter. Isso vai servir como referência de tom, ritmo e abordagem.

```
[AGENTE]:
[LEAD]:
[AGENTE]:
[LEAD]:
[AGENTE]:
[LEAD]:
[AGENTE]:
→ [HANDOFF PARA HUNTER]
[HUNTER]:
[LEAD]:
```

---

## 13. Aprovação

| Papel | Nome | Status | Data |
|-------|------|--------|------|
| Solicitante | | [ ] Aprovado | |
| Gestor | | [ ] Aprovado | |
| Dev | | [ ] Viável [ ] Dúvidas | |

---

## Anexo: Fluxo Visual

```
┌─────────────────────────────────────────────────────────────────┐
│                    FORMULÁRIO PREENCHIDO                         │
│  (Nome, Protocolo, Budget, Dores, Procedimentos anteriores)     │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  Budget = ALTO?   │
                    └─────────┬─────────┘
                              │
                  ┌───────────┴───────────┐
                  │                       │
                 SIM                     NÃO
                  │                       │
                  ▼                       ▼
    ┌───────────────────┐   ┌───────────────────┐
    │   HUNTER DIRETO   │   │  AGENTE IA INICIA │
    │   (sem agente)    │   │     (< 2 min)     │
    └───────────────────┘   └─────────┬─────────┘
                                      │
                                      ▼
                            ┌───────────────────┐
                            │  Lead respondeu?  │
                            └─────────┬─────────┘
                                      │
                          ┌───────────┴───────────┐
                          │                       │
                         SIM                     NÃO
                          │                       │
                          ▼                       ▼
            ┌───────────────────┐   ┌───────────────────┐
            │   QUALIFICAÇÃO    │   │    FOLLOW-UP      │
            │ • Descobre dores  │   │ • 5 msgs em 7 dias│
            │ • Apresenta proto │   │ • Cadenciado      │
            │ • Confirma fit    │   └─────────┬─────────┘
            └─────────┬─────────┘             │
                      │                       ▼
                      ▼               ┌───────────────────┐
            ┌───────────────────┐     │ Respondeu após    │
            │   QUALIFICADO?   │     │   follow-up?      │
            │ • 3+ msgs engaj. │     └─────────┬─────────┘
            │ • Interesse agend│               │
            │ • Pergunta s/resp│       ┌───────┴───────┐
            └─────────┬─────────┘      │               │
                      │               SIM             NÃO
              ┌───────┴───────┐        │               │
              │               │        │               ▼
             SIM             NÃO       │     ┌───────────────────┐
              │               │        │     │   → NUTRIÇÃO      │
              ▼               ▼        │     │     (PRD 3)       │
┌───────────────────┐ ┌──────────────┐│     └───────────────────┘
│ HANDOFF → HUNTER  │ │ Continua com ││
│ • Notificação     │ │   agente     │◄┘
│ • Resumo conversa │ └──────────────┘
│ • Lead não percebe│
└───────────────────┘
```
