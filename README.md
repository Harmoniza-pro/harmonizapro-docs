<p align="center">
  <img src="https://img.shields.io/badge/HarmonizaPRO-Docs-blueviolet?style=for-the-badge&logo=bookstack&logoColor=white" alt="HarmonizaPRO Docs"/>
</p>

<h1 align="center">📋 HarmonizaPRO — Documentação</h1>

<p align="center">
  <strong>Central de documentação do sistema de qualificação de leads via WhatsApp com IA para clínicas de harmonização facial.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/n8n-Automação-orange?style=flat-square&logo=n8n&logoColor=white" alt="n8n"/>
  <img src="https://img.shields.io/badge/Claude-IA-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude AI"/>
  <img src="https://img.shields.io/badge/WhatsApp-UaZapi-25D366?style=flat-square&logo=whatsapp&logoColor=white" alt="WhatsApp"/>
  <img src="https://img.shields.io/badge/Supabase-Database-3ECF8E?style=flat-square&logo=supabase&logoColor=white" alt="Supabase"/>
  <img src="https://img.shields.io/badge/MkDocs-Material-526CFE?style=flat-square&logo=materialformkdocs&logoColor=white" alt="MkDocs Material"/>
  <img src="https://img.shields.io/badge/Idioma-Português%20BR-009739?style=flat-square" alt="Português BR"/>
</p>

<p align="center">
  <a href="#-sobre-o-projeto">Sobre</a> •
  <a href="#-arquitetura">Arquitetura</a> •
  <a href="#-início-rápido">Início Rápido</a> •
  <a href="#-estrutura-do-repositório">Estrutura</a> •
  <a href="#-o-que-está-documentado">Conteúdo</a> •
  <a href="#-gerador-automático">Gerador</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## 🧠 Sobre o Projeto

O **HarmonizaPRO** é um sistema de **agente de IA** que automatiza a qualificação de leads para clínicas de harmonização facial. O agente conversa com leads via WhatsApp, qualifica, aquece e entrega para a Hunter (vendedora) **apenas os leads prontos para agendar consulta**.

Este repositório contém **toda a documentação** do sistema:

| 📄 Documento | 🎯 Para quem |
|:---|:---|
| PRD (Requisitos) | Product Manager, Stakeholders |
| Docs de Workflows | Desenvolvedores, DevOps |
| Playbooks | Equipe de vendas (Hunters), Treinamento |
| Runbooks | Operações, Suporte técnico |
| Base de Conhecimento | Agente de IA, Onboarding de clínicas |

> 💡 **Por que documentar?** Um agente mal configurado **queima leads**. Documentação clara = menos erros, onboarding rápido, e escala com qualidade.

---

## 🏗️ Arquitetura

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Typeform   │────▶│     n8n      │────▶│   WhatsApp   │
│  (Formulário)│     │ (Orquestração│     │   (UaZapi)   │
└──────────────┘     │  de Fluxos)  │     └──────┬───────┘
                     └──────┬───────┘            │
                            │                    │
                     ┌──────▼───────┐            │
                     │   Claude AI  │            │
                     │  (Cérebro do │     ┌──────▼───────┐
                     │    Agente)   │     │    Lead      │
                     └──────┬───────┘     │  (WhatsApp)  │
                            │             └──────────────┘
                     ┌──────▼───────┐
                     │   Supabase   │
                     │  (Database)  │
                     └──────────────┘
```

### 🔄 Fluxo Principal

```
📝 Lead preenche formulário
        │
        ▼
   Budget ALTO? ──SIM──▶ 🏃 Hunter entra direto
        │
       NÃO
        │
        ▼
   🤖 Agente IA inicia conversa (< 2 min)
        │
        ▼
   Lead respondeu? ──NÃO──▶ 📩 Follow-up (5 msgs / 7 dias)
        │                              │
       SIM                        Respondeu? ──NÃO──▶ 🌱 Nutrição
        │                              │
        ▼                             SIM
   🔍 Qualificação                     │
   • Descobre dores                    │
   • Apresenta protocolo               │
   • Confirma fit                      │
        │                              │
        ▼                              │
   Qualificado? ◀──────────────────────┘
        │
   ┌────┴────┐
  SIM       NÃO
   │         │
   ▼         ▼
🤝 HANDOFF   🔄 Continua
  → Hunter    com agente
```

---

## ⚡ Início Rápido

### 📋 Pré-requisitos

- 🐍 Python 3.8+
- 📦 pip
- 🔧 Git

### 🚀 Instalação

```bash
# 1️⃣  Clone o repositório
git clone https://github.com/SEU-USUARIO/harmonizapro-docs.git
cd harmonizapro-docs

# 2️⃣  Execute o setup automático
chmod +x setup.sh
./setup.sh

# 3️⃣  Ative o ambiente virtual
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 4️⃣  Rode o site de documentação
mkdocs serve
```

> 🌐 Acesse `http://127.0.0.1:8000` no navegador para ver a documentação.

### 📥 Gerando docs a partir do n8n

```bash
# 1️⃣  Exporte o workflow do n8n (JSON)
# 2️⃣  Coloque em workflows/exports/
cp ~/Downloads/meu-workflow.json workflows/exports/

# 3️⃣  Rode o gerador
python tools/generate_docs.py

# ✅  O esqueleto do doc será criado em docs/workflows/
# 📝  Preencha as partes humanas (objetivo, regras, testes)
```

---

## 📁 Estrutura do Repositório

```
harmonizapro-docs/
│
├── 📄 README.md                         ← Você está aqui!
├── 📄 mkdocs.yml                        ← Config do site (navegação, tema, plugins)
├── 🔧 setup.sh                          ← Script de setup automático
├── 📄 .gitignore
│
├── 🔧 tools/
│   └── generate_docs.py                 ← 🤖 Gerador automático de docs do n8n JSON
│
├── 📦 workflows/
│   └── exports/                         ← 📥 Coloque aqui os JSON exportados do n8n
│
└── 📚 docs/
    │
    ├── 🏠 index.md                      ← Página inicial com visão geral e status
    │
    ├── 📋 prd-001-agente-qualificacao.md ← PRD completo (13 seções + fluxo visual)
    │   • Problema / Dor
    │   • Objetivo & Métricas
    │   • Escopo (Must Have / Nice to Have)
    │   • Usuários & Personas
    │   • Integrações & Dependências
    │   • Regras de Negócio
    │   • Interface & Experiência
    │   • Requisitos Técnicos
    │   • Cronograma & Entregas
    │   • Riscos & Considerações
    │   • Materiais de Apoio
    │   • Exemplo de Conversa Ideal
    │   • Aprovação
    │
    ├── 🏥 base-conhecimento-clinicas.md  ← Dados de 5 clínicas + template
    │   • Dra. Renata Rezende (Protocolo RR)
    │   • Dra. Gabriela Veloso (Protocolo GV)
    │   • Dra. Aline di Toro (Protocolo Lumine FACE)
    │   • Dra. Raquel (Protocolo New Naturee)
    │   • Dra. Karise (Protocolo Lumi Lift)
    │
    ├── ⚙️ workflows/                    ← Documentação técnica dos workflows n8n
    │   ├── index.md                      ← Índice com status de cada workflow
    │   ├── _template.md                  ← Template para novos workflows
    │   ├── agente-de-ia.md               ← Workflow principal (webhook + Claude + UaZapi)
    │   ├── chamada-typeform.md           ← Trigger do formulário + 1ª mensagem
    │   └── tool-transferir.md            ← Handoff invisível IA → Hunter
    │
    ├── 📖 playbooks/                     ← Procedimentos operacionais
    │   ├── index.md
    │   ├── abordagem-por-perfil.md       ← 10 casos de leads com scripts completos
    │   └── respostas-objecoes.md         ← Respostas para preço, desconto, etc.
    │
    └── 🚨 runbooks/                      ← Troubleshooting / incidentes
        ├── index.md
        ├── webhook-fora.md               ← Webhook não recebe mensagens
        └── handoff-falhando.md           ← Hunter não é notificada
```

---

## 📚 O que está documentado

### 📋 PRD 001 — Agente de Qualificação IA

O documento de requisitos completo, com 13 seções:

| Seção | Conteúdo |
|:------|:---------|
| 🎯 **Problema** | Por que estamos construindo isso |
| 🏆 **Objetivo** | Métricas de sucesso (>70% conversão, <2min resposta) |
| 📦 **Escopo** | Must Have vs Nice to Have vs Fora do escopo |
| 👥 **Personas** | Lead, Hunter, Gestão — jornadas completas |
| 🔌 **Integrações** | Typeform, n8n, Claude, UaZapi, Supabase, ClickUp |
| ⚖️ **Regras de Negócio** | Qualificação, engajamento, follow-up, handoff, objeções |
| 🖥️ **Interface** | Experiência para Lead, Hunter e Gestão |
| 🔧 **Requisitos Técnicos** | Performance, segurança, monitoramento |
| 📅 **Cronograma** | 5 fases (Fase 0 → MVP → V2 → V3 → V4) |
| ⚠️ **Riscos** | 5 riscos mapeados com mitigação |
| 📎 **Materiais** | Template de clínica, checklist para dev |
| 💬 **Conversa Ideal** | Seção para exemplo de referência |
| ✅ **Aprovação** | Tabela de sign-off |

### ⚙️ Workflows n8n

Cada workflow é documentado com:

- 🎯 Objetivo claro
- 🔗 Trigger (webhook, cron, manual)
- 📥 Payload de entrada esperado
- 📤 Saídas geradas
- ⚖️ Regras de negócio aplicáveis
- 🔌 Integrações (Supabase, UaZapi, Claude)
- 🗺️ Fluxo em alto nível
- ⚠️ Nós críticos (onde costuma quebrar)
- 🧪 Casos de teste
- 📝 Changelog

### 📖 Playbooks

| Playbook | Conteúdo |
|:---------|:---------|
| **Abordagem por Perfil** | 10 exemplos reais de leads com scripts completos de conversa (primeira mensagem + 3 perguntas de qualificação) |
| **Respostas para Objeções** | Templates para: preço, desconto, outro procedimento, pergunta desconhecida, pedido de humano, irritação |

### 🚨 Runbooks

| Runbook | Quando usar |
|:--------|:-----------|
| **Webhook Fora do Ar** | Diagnóstico completo: n8n → UaZapi → conectividade |
| **Handoff Falhando** | Dados incompletos, telefone hardcoded, workaround manual |

### 🏥 Base de Conhecimento

Dados estruturados de **5 clínicas**:

| Clínica | Protocolo | Status |
|:--------|:----------|:-------|
| Dra. Renata Rezende | Protocolo RR | ✅ Completo |
| Dra. Gabriela Veloso | Protocolo GV | ✅ Completo |
| Dra. Aline di Toro | Protocolo Lumine FACE | ⚠️ Incompleto |
| Dra. Raquel | Protocolo New Naturee | ✅ Completo |
| Dra. Karise | Protocolo Lumi Lift | ✅ Completo |

---

## 🤖 Gerador Automático

O script `tools/generate_docs.py` analisa o JSON exportado do n8n e gera automaticamente:

| Detectado | Exemplo |
|:----------|:--------|
| 🔗 Webhook trigger | `POST /harmonizapro` |
| 🗄️ Tabelas Supabase | `leads` (insert, update, select) |
| 🌐 HTTP endpoints | `POST /send/text` (UaZapi) |
| 🧠 Nós de IA | AI Agent (Claude) |
| 📊 Tipos de nós | Top 10 mais usados |
| 📈 Contagem total | Número de nós no workflow |

### Como usar

```bash
# Exportar workflow do n8n como JSON
# Salvar em workflows/exports/

python tools/generate_docs.py

# ✅ Gerado: docs/workflows/agente-de-ia.md
# 📋 Total: 1 workflow(s) processado(s)
#    Agora preencha as partes humanas nos arquivos gerados
```

> 💡 O gerador cria o **esqueleto** com tudo que pode ser extraído automaticamente. Você só precisa preencher as **partes humanas**: objetivo, regras de negócio, casos de teste.

---

## 🗺️ Roadmap

### Projeto HarmonizaPRO

| Fase | Entrega | Descrição | Status |
|:-----|:--------|:----------|:-------|
| **Fase 0** | 📚 Base de conhecimento | Documento estruturado de cada clínica | 🟡 Em progresso |
| **MVP** | 🤖 Agente básico | Conversa + qualificação + handoff manual | 🟡 Em progresso |
| **V2** | 📩 Follow-ups | Cadência automática de 5 msgs em 7 dias | ⚪ Pendente |
| **V3** | 🤝 Handoff inteligente | Critérios automáticos de qualificação | ⚪ Pendente |
| **V4** | 📊 Integração ClickUp | Atualiza CRM automaticamente (PRD 3) | ⚪ Pendente |

### Documentação

- [x] 📋 PRD 001 completo com 13 seções
- [x] ⚙️ Docs dos 3 workflows principais
- [x] 📖 Playbook de abordagem por perfil (10 casos)
- [x] 📖 Playbook de respostas para objeções
- [x] 🚨 Runbooks de troubleshooting
- [x] 🏥 Base de conhecimento de 5 clínicas
- [x] 🤖 Gerador automático de docs
- [ ] 🔄 GitHub Action para validar docs vs JSON
- [ ] 📊 Dashboard de cobertura da documentação
- [ ] 📖 Playbook de follow-up (quando V2 pronto)

---

## 🛠️ Tecnologias

| Tecnologia | Uso no Projeto |
|:-----------|:---------------|
| <img src="https://img.shields.io/badge/MkDocs-526CFE?style=flat-square&logo=materialformkdocs&logoColor=white" alt="MkDocs"/> | Site de documentação estático |
| <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/> | Gerador automático de docs |
| <img src="https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white" alt="Markdown"/> | Formato dos documentos |
| <img src="https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white" alt="n8n"/> | Orquestração dos workflows |
| <img src="https://img.shields.io/badge/Claude-191919?style=flat-square&logo=anthropic&logoColor=white" alt="Claude"/> | IA / cérebro do agente |
| <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white" alt="Supabase"/> | Banco de dados |
| <img src="https://img.shields.io/badge/WhatsApp-25D366?style=flat-square&logo=whatsapp&logoColor=white" alt="WhatsApp"/> | Canal de comunicação (via UaZapi) |

---

## 📌 Problemas Conhecidos

> Documentados em detalhe nos [Runbooks](docs/runbooks/).

| Problema | Impacto | Workaround |
|:---------|:--------|:-----------|
| 📞 Telefone da Hunter hardcoded | Só funciona para 1 Hunter | Tornar dinâmico via Supabase |
| 📝 Dados incompletos do contato | Handoff falha | Validar antes do handoff |
| ⏳ Typing indicators não funcionam | Bot detectável | Investigar UaZapi endpoints |
| ✂️ Quebra de mensagem no meio de frase | Parece robótico | Usar quebra por fronteira de frase |
| 🏥 Dados da Dra. Aline di Toro | Protocolo incompleto | Coletar informações |

---

## 🤝 Como Contribuir

1. **Atualizou um workflow?** → Exporte o JSON, rode o gerador, preencha as mudanças
2. **Encontrou um bug?** → Documente no runbook correspondente
3. **Nova clínica?** → Use o template em `base-conhecimento-clinicas.md`
4. **Novo playbook?** → Crie em `docs/playbooks/` e adicione ao `mkdocs.yml`

### Convenções

- 📝 Documentos em **Português BR**
- 📅 Datas no formato **YYYY-MM-DD**
- 🏷️ Status: 🟢 Ativo | 🟡 Em progresso | ⚪ Pendente | 🔴 Desativado
- 📁 Nomes de arquivo em **kebab-case** (ex: `agente-de-ia.md`)

---

## 📊 Métricas do Projeto

```
📄 Total de documentos:  17 arquivos
📋 PRD:                   1 documento (13 seções)
⚙️ Workflows:             3 documentados + 1 template
📖 Playbooks:             2 (10 casos de leads + objeções)
🚨 Runbooks:              2 (webhook + handoff)
🏥 Clínicas:              5 documentadas
🤖 Gerador automático:    1 script Python
```

---

## 📜 Licença

Projeto interno — **HarmonizaPRO** © 2026

---

<p align="center">
  <strong>Feito com 💜 para escalar clínicas de harmonização facial</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PRD-001-blueviolet?style=flat-square" alt="PRD 001"/>
  <img src="https://img.shields.io/badge/Workflows-3-orange?style=flat-square" alt="3 Workflows"/>
  <img src="https://img.shields.io/badge/Clínicas-5-green?style=flat-square" alt="5 Clínicas"/>
  <img src="https://img.shields.io/badge/Playbooks-2-blue?style=flat-square" alt="2 Playbooks"/>
  <img src="https://img.shields.io/badge/Runbooks-2-red?style=flat-square" alt="2 Runbooks"/>
</p>
