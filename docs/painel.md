# Painel Interativo

<p style="color:#888;font-size:.95em;border-left:3px solid #C8A24E;padding-left:14px;margin:16px 0 24px">
Visão consolidada do ecossistema HarmonizaPRO — navegue pelas abas para explorar cada área do sistema.
</p>

<style>
.hp-panel-tabs{display:flex;gap:4px;background:rgba(200,162,78,0.06);border-radius:12px;padding:4px;margin:24px 0 28px;flex-wrap:wrap;border:1px solid rgba(200,162,78,0.15)}
.hp-panel-tab{padding:10px 18px;border-radius:8px;border:none;cursor:pointer;background:transparent;color:#888;font-weight:500;font-size:.85em;transition:all .25s;font-family:inherit}
.hp-panel-tab:hover{color:var(--hp-gold,#C8A24E);background:rgba(200,162,78,0.06)}
.hp-panel-tab.active{background:rgba(200,162,78,0.15);color:var(--hp-gold,#C8A24E);font-weight:600}
.hp-panel-section{display:none;animation:hpFadeIn .4s ease}
.hp-panel-section.active{display:block}
@keyframes hpFadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.hp-section-title{font-size:1.3em;font-weight:700;color:var(--hp-gold,#C8A24E);margin:32px 0 6px;padding-bottom:8px;border-bottom:1px solid rgba(200,162,78,0.2)}
.hp-section-title:first-child{margin-top:0}
.hp-section-desc{color:#888;font-size:.88em;border-left:3px solid rgba(200,162,78,0.3);padding-left:12px;margin:8px 0 18px;line-height:1.5}
.hp-cards{display:grid;gap:16px;margin:20px 0}
.hp-cards-3{grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}
.hp-cards-6{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}
.hp-card{background:rgba(200,162,78,0.03);border:1px solid rgba(200,162,78,0.15);border-radius:14px;padding:22px 18px;transition:all .3s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.hp-card:hover{border-color:rgba(200,162,78,0.45);transform:translateY(-3px);box-shadow:0 12px 30px rgba(0,0,0,0.15)}
.hp-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--hp-gold,#C8A24E),transparent);opacity:0;transition:opacity .3s}
.hp-card:hover::before{opacity:1}
.hp-card-icon{font-size:1.8em;margin-bottom:8px;display:block}
.hp-card-title{font-size:1.05em;font-weight:700;margin-bottom:4px}
.hp-card-sub{font-size:.8em;color:#888;line-height:1.4}
.hp-card-badge{position:absolute;top:14px;right:14px;background:rgba(200,162,78,0.15);color:var(--hp-gold,#C8A24E);padding:4px 12px;border-radius:20px;font-size:.82em;font-weight:700}
.hp-card-tags{display:flex;gap:5px;flex-wrap:wrap;margin-top:10px}
.hp-card-tag{padding:2px 8px;border-radius:4px;font-size:.7em;background:rgba(255,255,255,0.06);color:#999;border:1px solid rgba(255,255,255,0.08)}
.hp-status{padding:3px 10px;border-radius:16px;font-size:.72em;font-weight:600;display:inline-block}
.hp-status-ok{background:rgba(34,197,94,0.12);color:#22c55e}
.hp-status-warn{background:rgba(249,115,22,0.12);color:#f97316}
.hp-journey{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:20px 0}
.hp-journey-step{text-align:center;padding:18px 12px;border-radius:14px;border:1px solid rgba(200,162,78,0.12);background:rgba(200,162,78,0.02);cursor:pointer;transition:all .3s;position:relative}
.hp-journey-step:hover,.hp-journey-step.active{border-color:rgba(200,162,78,0.45);background:rgba(200,162,78,0.06);transform:scale(1.04)}
.hp-journey-num{position:absolute;top:-8px;left:50%;transform:translateX(-50%);background:var(--hp-gold,#C8A24E);color:#111;font-size:.68em;font-weight:700;padding:2px 10px;border-radius:12px}
.hp-journey-icon{font-size:2em;margin:10px 0 6px;display:block}
.hp-journey-label{font-weight:600;font-size:.85em;margin-bottom:4px}
.hp-journey-desc{font-size:.72em;color:#888;line-height:1.3;max-height:0;overflow:hidden;transition:max-height .4s,opacity .3s;opacity:0}
.hp-journey-step.active .hp-journey-desc{max-height:60px;opacity:1}
.hp-chat{border-radius:16px;overflow:hidden;border:1px solid rgba(200,162,78,0.2);max-width:600px;margin:0 auto}
.hp-chat-header{background:#075e54;padding:14px 18px;display:flex;align-items:center;gap:12px}
.hp-chat-avatar{width:40px;height:40px;border-radius:50%;background:#128C7E;display:flex;align-items:center;justify-content:center;font-size:1.2em}
.hp-chat-name{color:#fff;font-weight:600;font-size:.95em}
.hp-chat-status{color:rgba(255,255,255,0.5);font-size:.72em}
.hp-chat-body{min-height:320px;max-height:400px;overflow-y:auto;padding:16px 18px;background:rgba(10,15,14,0.6);display:flex;flex-direction:column;gap:8px}
.hp-chat-empty{text-align:center;color:#555;font-size:.85em;margin-top:120px}
.hp-chat-msg{max-width:80%;padding:10px 14px;border-radius:10px;font-size:.88em;line-height:1.5;animation:hpFadeIn .3s ease;word-wrap:break-word}
.hp-chat-msg.agent{align-self:flex-start;background:#1f2937;border-top-left-radius:3px}
.hp-chat-msg.lead{align-self:flex-end;background:#005c4b;border-top-right-radius:3px}
.hp-chat-msg.system{align-self:center;background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.25);color:#22c55e;font-size:.78em;padding:8px 16px;border-radius:8px;text-align:center;max-width:90%}
.hp-chat-msg.hunter{align-self:flex-start;background:#4a1942;border-top-left-radius:3px}
.hp-chat-label{display:block;font-size:.68em;font-weight:700;margin-bottom:4px}
.hp-chat-label-hunter{color:#ec4899}
.hp-chat-controls{padding:12px;display:flex;gap:8px;border-top:1px solid rgba(200,162,78,0.1);background:rgba(200,162,78,0.02)}
.hp-chat-btn{flex:1;padding:11px;border-radius:8px;border:none;font-weight:600;font-size:.85em;cursor:pointer;transition:all .2s;font-family:inherit}
.hp-chat-btn-primary{background:var(--hp-gold,#C8A24E);color:#111}
.hp-chat-btn-primary:hover{opacity:.9}
.hp-chat-btn-primary:disabled{background:#555;color:#888;cursor:default}
.hp-chat-btn-reset{background:transparent;border:1px solid rgba(200,162,78,0.2);color:#888;flex:0 0 auto;padding:11px 16px}
.hp-chat-btn-reset:hover{border-color:rgba(200,162,78,0.4)}
.hp-followups{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px;margin:20px 0}
.hp-followup{text-align:center;padding:20px 14px;border-radius:14px;border:1px solid rgba(200,162,78,0.12);background:rgba(200,162,78,0.02);transition:all .3s}
.hp-followup:hover{border-color:rgba(200,162,78,0.35);transform:translateY(-2px)}
.hp-followup-icon{font-size:1.6em;margin-bottom:6px}
.hp-followup-num{font-weight:700;font-size:1em;margin-bottom:4px}
.hp-followup-time{font-size:.75em;color:var(--hp-gold,#C8A24E);margin-bottom:2px}
.hp-followup-tom{font-size:.72em;color:#888}
.hp-flow-container{background:rgba(200,162,78,0.03);border-radius:14px;padding:24px;border:1px solid rgba(200,162,78,0.12);overflow-x:auto}
.hp-flow-title{font-size:.82em;color:#888;margin-bottom:14px;text-align:center}
.hp-rules{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px;margin:20px 0}
.hp-rule{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:10px;border:1px solid rgba(200,162,78,0.1);transition:all .2s}
.hp-rule:hover{border-color:rgba(200,162,78,0.3)}
.hp-rule-icon{font-size:1.3em;flex-shrink:0}
.hp-rule-text{font-size:.85em}
.hp-rule.danger{border-color:rgba(239,68,68,0.2);background:rgba(239,68,68,0.03)}
.hp-rule.success{border-color:rgba(34,197,94,0.2);background:rgba(34,197,94,0.03)}
.hp-rule.critical{border-color:rgba(168,85,247,0.2);background:rgba(168,85,247,0.03)}
.hp-checklist{display:flex;flex-direction:column;gap:5px;max-width:560px;margin:20px 0}
.hp-check-item{display:flex;align-items:center;gap:10px;padding:7px 12px;border-radius:8px;cursor:pointer;border:1px solid rgba(200,162,78,0.08);transition:all .2s;user-select:none}
.hp-check-item:hover{border-color:rgba(200,162,78,0.25)}
.hp-check-item.checked{background:rgba(34,197,94,0.04);border-color:rgba(34,197,94,0.15)}
.hp-check-box{width:18px;height:18px;border-radius:5px;border:2px solid #555;display:flex;align-items:center;justify-content:center;font-size:.7em;transition:all .2s;flex-shrink:0}
.hp-check-item.checked .hp-check-box{background:#22c55e;border-color:#22c55e;color:#fff}
.hp-check-label{font-size:.82em}
.hp-handoff-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:20px 0;max-width:700px}
@media(max-width:600px){.hp-handoff-grid{grid-template-columns:1fr}}
.hp-handoff-box{padding:20px;border-radius:14px;border:1px solid rgba(200,162,78,0.12)}
.hp-handoff-box.pass{border-color:rgba(34,197,94,0.25);background:rgba(34,197,94,0.03)}
.hp-handoff-box.fail{border-color:rgba(239,68,68,0.25);background:rgba(239,68,68,0.03)}
.hp-handoff-title{font-weight:700;font-size:.95em;margin-bottom:10px}
.hp-handoff-item{font-size:.8em;color:#999;padding:4px 0;border-bottom:1px solid rgba(255,255,255,0.04)}
.hp-info-box{padding:16px 20px;border-radius:12px;font-size:.88em;margin:20px 0;line-height:1.5;border-left:4px solid}
.hp-info-box.info{background:rgba(59,130,246,0.06);border-color:#3b82f6;color:#93c5fd}
.hp-info-box.warn{background:rgba(249,115,22,0.06);border-color:#f97316;color:#fdba74}
.hp-info-box.danger{background:rgba(239,68,68,0.06);border-color:#ef4444;color:#fca5a5}
.hp-info-box strong{color:inherit}
.hp-info-box .hp-info-title{font-weight:700;margin-bottom:4px;display:block}
[data-md-color-scheme="default"] .hp-info-box.info{color:#1d4ed8}
[data-md-color-scheme="default"] .hp-info-box.warn{color:#c2410c}
[data-md-color-scheme="default"] .hp-info-box.danger{color:#dc2626}
.hp-hero-metrics{display:flex;justify-content:center;gap:32px;flex-wrap:wrap;margin:24px 0 8px}
.hp-hero-metric{text-align:center}
.hp-hero-metric-val{font-size:1.6em;font-weight:700;color:var(--hp-gold,#C8A24E)}
.hp-hero-metric-label{font-size:.75em;color:#888}
.hp-queue{display:flex;gap:10px;align-items:center;justify-content:center;flex-wrap:wrap;padding:20px;margin:16px 0}
.hp-queue-item{padding:7px 14px;border-radius:8px;font-size:.82em;font-weight:600}
.hp-queue-arrow{font-size:1.2em;color:#555}
[data-md-color-scheme="default"] .hp-card{background:rgba(200,162,78,0.04)}
[data-md-color-scheme="default"] .hp-chat-body{background:rgba(240,240,240,0.5)}
[data-md-color-scheme="default"] .hp-chat-msg.agent{background:#e5e7eb;color:#111}
[data-md-color-scheme="default"] .hp-chat-msg.lead{background:#dcfce7;color:#111}
[data-md-color-scheme="default"] .hp-chat-msg.hunter{background:#fce7f3;color:#111}
[data-md-color-scheme="default"] .hp-chat-msg.system{background:rgba(34,197,94,0.08);color:#16a34a}
</style>

<div class="hp-hero-metrics">
  <div class="hp-hero-metric"><div class="hp-hero-metric-val" data-count="41">0</div><div class="hp-hero-metric-label">Workflows</div></div>
  <div class="hp-hero-metric"><div class="hp-hero-metric-val" data-count="7">0</div><div class="hp-hero-metric-label">Departamentos</div></div>
  <div class="hp-hero-metric"><div class="hp-hero-metric-val" data-count="12">0</div><div class="hp-hero-metric-label">Filas RabbitMQ</div></div>
  <div class="hp-hero-metric"><div class="hp-hero-metric-val" data-count="12">0</div><div class="hp-hero-metric-label">Integrações</div></div>
  <div class="hp-hero-metric"><div class="hp-hero-metric-val" data-count="3">0</div><div class="hp-hero-metric-label">Bancos PostgreSQL</div></div>
</div>

<hr>

<div class="hp-panel-tabs" id="panelTabs">
  <button class="hp-panel-tab active" data-tab="overview">🏠 Visão Geral</button>
  <button class="hp-panel-tab" data-tab="journey">🗺️ Jornada do Lead</button>
  <button class="hp-panel-tab" data-tab="agent">🤖 Agente IA</button>
  <button class="hp-panel-tab" data-tab="clinicas">🏥 Clínicas</button>
  <button class="hp-panel-tab" data-tab="rules">📋 PRD &amp; Regras</button>
</div>

<div class="hp-panel-section active" id="sec-overview">
<h2 class="hp-section-title">Departamentos</h2>
<div class="hp-cards hp-cards-3">
<div class="hp-card"><span class="hp-card-badge">6</span><span class="hp-card-icon">🤖</span><div class="hp-card-title">IA Harmoniza</div><div class="hp-card-sub">Agente de IA, Follow-ups, Métricas diárias, Monitoramento de custos, Tool Transferir</div></div>
<div class="hp-card"><span class="hp-card-badge">20</span><span class="hp-card-icon">💼</span><div class="hp-card-title">Comercial</div><div class="hp-card-sub">Pipeline completo: Typeform → Pipedrive → Distribuição → WhatsApp → Pixel</div></div>
<div class="hp-card"><span class="hp-card-badge">5</span><span class="hp-card-icon">🎯</span><div class="hp-card-title">Hunters</div><div class="hp-card-sub">CRM ClickUp, automação de ganho/perda, integração WhatsApp</div></div>
<div class="hp-card"><span class="hp-card-badge">7</span><span class="hp-card-icon">⚙️</span><div class="hp-card-title">Operação</div><div class="hp-card-sub">Meta Ads monitor, gestão de clientes, retroativos, links de formulário</div></div>
<div class="hp-card"><span class="hp-card-badge">3</span><span class="hp-card-icon">📍</span><div class="hp-card-title">Tracking</div><div class="hp-card-sub">Pipeline server-side: GTM → Typeform → Enriquecimento → Facebook CAPI</div></div>
<div class="hp-card"><span class="hp-card-badge">2</span><span class="hp-card-icon">📋</span><div class="hp-card-title">Templates</div><div class="hp-card-sub">Blocos reutilizáveis: Parser ClickUp e padrão RabbitMQ</div></div>
<div class="hp-card"><span class="hp-card-badge">4</span><span class="hp-card-icon">📝</span><div class="hp-card-title">Formulários</div><div class="hp-card-sub">Sync CRUD de formulários ClickUp ↔ PostgreSQL em tempo real</div></div>
</div>
<h2 class="hp-section-title">Stack Tecnológica</h2>
<div class="hp-cards hp-cards-6">
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">⚡</span><div class="hp-card-title">n8n</div><div class="hp-card-sub">Orquestração</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">🐰</span><div class="hp-card-title">RabbitMQ</div><div class="hp-card-sub">Mensageria</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">🧠</span><div class="hp-card-title">Claude</div><div class="hp-card-sub">IA Principal</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">🔄</span><div class="hp-card-title">GPT-5</div><div class="hp-card-sub">Fallback IA</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">🎤</span><div class="hp-card-title">Whisper</div><div class="hp-card-sub">Transcrição</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">👁️</span><div class="hp-card-title">Gemini</div><div class="hp-card-sub">Vídeo/Docs</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">💾</span><div class="hp-card-title">Supabase</div><div class="hp-card-sub">PostgreSQL ×3</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">⚡</span><div class="hp-card-title">Redis</div><div class="hp-card-sub">Fila de Msgs</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">📱</span><div class="hp-card-title">UaZapi</div><div class="hp-card-sub">WhatsApp API</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">📊</span><div class="hp-card-title">Pipedrive</div><div class="hp-card-sub">CRM Deals</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">✅</span><div class="hp-card-title">ClickUp</div><div class="hp-card-sub">CRM Hunters</div></div>
<div class="hp-card" style="text-align:center"><span class="hp-card-icon">📍</span><div class="hp-card-title">Meta CAPI</div><div class="hp-card-sub">Tracking Pixel</div></div>
</div>
</div>

<div class="hp-panel-section" id="sec-journey">
<h2 class="hp-section-title">Jornada do Lead</h2>
<p class="hp-section-desc">Clique em cada etapa para ver detalhes.</p>
<div class="hp-journey" id="journeySteps">
  <div class="hp-journey-step" data-step="0"><span class="hp-journey-num">1</span><span class="hp-journey-icon">📝</span><div class="hp-journey-label">Formulário</div><div class="hp-journey-desc">Lead preenche Typeform Anti-Curioso</div></div>
  <div class="hp-journey-step" data-step="1"><span class="hp-journey-num">2</span><span class="hp-journey-icon">🤖</span><div class="hp-journey-label">&lt; 2 min</div><div class="hp-journey-desc">Agente IA inicia conversa no WhatsApp</div></div>
  <div class="hp-journey-step" data-step="2"><span class="hp-journey-num">3</span><span class="hp-journey-icon">💬</span><div class="hp-journey-label">Qualificação</div><div class="hp-journey-desc">Descobre dores, apresenta protocolo</div></div>
  <div class="hp-journey-step" data-step="3"><span class="hp-journey-num">4</span><span class="hp-journey-icon">🔥</span><div class="hp-journey-label">Engajamento</div><div class="hp-journey-desc">3+ mensagens com interesse real</div></div>
  <div class="hp-journey-step" data-step="4"><span class="hp-journey-num">5</span><span class="hp-journey-icon">🎯</span><div class="hp-journey-label">Handoff</div><div class="hp-journey-desc">Hunter assume — lead não percebe</div></div>
  <div class="hp-journey-step" data-step="5"><span class="hp-journey-num">6</span><span class="hp-journey-icon">📅</span><div class="hp-journey-label">Agendamento</div><div class="hp-journey-desc">Hunter agenda consulta presencial</div></div>
</div>
<h2 class="hp-section-title">Simulador de Conversa</h2>
<p class="hp-section-desc">Clique em <strong>Próxima</strong> para ver como o agente qualifica um lead em tempo real.</p>
<div class="hp-chat" id="chatSim">
  <div class="hp-chat-header"><div class="hp-chat-avatar">👩‍⚕️</div><div><div class="hp-chat-name">Clínica Dra. Renata</div><div class="hp-chat-status">online</div></div></div>
  <div class="hp-chat-body" id="chatBody"><div class="hp-chat-empty">Clique em "Próxima" para simular a conversa</div></div>
  <div class="hp-chat-controls"><button class="hp-chat-btn hp-chat-btn-primary" id="chatNext">Próxima (1/8)</button><button class="hp-chat-btn hp-chat-btn-reset" id="chatReset">↻</button></div>
</div>
<h2 class="hp-section-title">Follow-up Automático</h2>
<p class="hp-section-desc">Cadência automática para leads que não respondem — 5 mensagens em 7 dias.</p>
<div class="hp-followups">
  <div class="hp-followup"><div class="hp-followup-icon">💬</div><div class="hp-followup-num">Follow-up #1</div><div class="hp-followup-time">4h após msg inicial</div><div class="hp-followup-tom">Lembrete leve</div></div>
  <div class="hp-followup"><div class="hp-followup-icon">✨</div><div class="hp-followup-num">Follow-up #2</div><div class="hp-followup-time">24h após #1</div><div class="hp-followup-tom">Reforço de valor</div></div>
  <div class="hp-followup"><div class="hp-followup-icon">⏰</div><div class="hp-followup-num">Follow-up #3</div><div class="hp-followup-time">48h após #2</div><div class="hp-followup-tom">Urgência suave</div></div>
  <div class="hp-followup"><div class="hp-followup-icon">🙏</div><div class="hp-followup-num">Follow-up #4</div><div class="hp-followup-time">72h após #3</div><div class="hp-followup-tom">Última tentativa</div></div>
  <div class="hp-followup"><div class="hp-followup-icon">👋</div><div class="hp-followup-num">Follow-up #5</div><div class="hp-followup-time">48h após #4</div><div class="hp-followup-tom">Despedida aberta</div></div>
</div>
<div class="hp-info-box danger"><span class="hp-info-title">⚠️ Após 7 dias sem resposta</span>Lead move automaticamente para <strong>Nutrição (PRD 003)</strong></div>
</div>

<div class="hp-panel-section" id="sec-agent">
<h2 class="hp-section-title">Arquitetura do Agente — 92 nós</h2>
<div class="hp-flow-container">
  <div class="hp-flow-title">Fluxo simplificado do workflow principal</div>
  <svg viewBox="0 0 520 330" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;display:block;margin:0 auto">
    <defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="#666"></path></marker></defs>
    <line x1="260" y1="38" x2="260" y2="68" stroke="#555" stroke-width="1.5" marker-end="url(#arr)"></line>
    <line x1="260" y1="100" x2="260" y2="130" stroke="#555" stroke-width="1.5" marker-end="url(#arr)"></line>
    <line x1="260" y1="162" x2="260" y2="188" stroke="#555" stroke-width="1.5" marker-end="url(#arr)"></line>
    <line x1="260" y1="188" x2="100" y2="208" stroke="#555" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arr)"></line>
    <line x1="260" y1="188" x2="260" y2="208" stroke="#555" stroke-width="1.5" marker-end="url(#arr)"></line>
    <line x1="260" y1="188" x2="420" y2="208" stroke="#555" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arr)"></line>
    <line x1="260" y1="240" x2="260" y2="268" stroke="#555" stroke-width="1.5" marker-end="url(#arr)"></line>
    <line x1="260" y1="240" x2="420" y2="268" stroke="#555" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arr)"></line>
    <rect x="170" y="12" width="180" height="28" rx="8" fill="rgba(34,197,94,0.12)" stroke="rgba(34,197,94,0.3)" stroke-width="1"></rect>
    <text x="260" y="31" text-anchor="middle" fill="#22c55e" font-size="11" font-weight="600" font-family="Inter,sans-serif">WhatsApp - Msg do Lead</text>
    <rect x="150" y="72" width="220" height="28" rx="8" fill="rgba(200,162,78,0.12)" stroke="rgba(200,162,78,0.3)" stroke-width="1"></rect>
    <text x="260" y="91" text-anchor="middle" fill="#C8A24E" font-size="11" font-weight="600" font-family="Inter,sans-serif">Validacao (Typeform? Transferido?)</text>
    <rect x="175" y="134" width="170" height="28" rx="8" fill="rgba(239,68,68,0.12)" stroke="rgba(239,68,68,0.3)" stroke-width="1"></rect>
    <text x="260" y="153" text-anchor="middle" fill="#ef4444" font-size="11" font-weight="600" font-family="Inter,sans-serif">Fila Redis (agrupa msgs)</text>
    <rect x="20" y="212" width="160" height="28" rx="8" fill="rgba(59,130,246,0.12)" stroke="rgba(59,130,246,0.3)" stroke-width="1"></rect>
    <text x="100" y="231" text-anchor="middle" fill="#3b82f6" font-size="10" font-weight="600" font-family="Inter,sans-serif">Media (Whisper / Gemini)</text>
    <rect x="180" y="212" width="160" height="28" rx="8" fill="rgba(168,85,247,0.12)" stroke="rgba(168,85,247,0.3)" stroke-width="1"></rect>
    <text x="260" y="231" text-anchor="middle" fill="#a855f7" font-size="11" font-weight="600" font-family="Inter,sans-serif">Claude Sonnet 4</text>
    <rect x="345" y="212" width="150" height="28" rx="8" fill="rgba(249,115,22,0.12)" stroke="rgba(249,115,22,0.3)" stroke-width="1"></rect>
    <text x="420" y="231" text-anchor="middle" fill="#f97316" font-size="10" font-weight="600" font-family="Inter,sans-serif">Fallback GPT-5</text>
    <rect x="180" y="272" width="160" height="28" rx="8" fill="rgba(34,197,94,0.12)" stroke="rgba(34,197,94,0.3)" stroke-width="1"></rect>
    <text x="260" y="291" text-anchor="middle" fill="#22c55e" font-size="11" font-weight="600" font-family="Inter,sans-serif">Formatar + Enviar</text>
    <rect x="345" y="272" width="150" height="28" rx="8" fill="rgba(236,72,153,0.12)" stroke="rgba(236,72,153,0.3)" stroke-width="1"></rect>
    <text x="420" y="291" text-anchor="middle" fill="#ec4899" font-size="10" font-weight="600" font-family="Inter,sans-serif">Handoff (Tool Transferir)</text>
  </svg>
</div>
<h2 class="hp-section-title">Modelos de IA</h2>
<div class="hp-cards hp-cards-3">
  <div class="hp-card"><span class="hp-card-icon">🧠</span><div class="hp-card-title" style="color:#a855f7">Claude Sonnet 4</div><div class="hp-card-sub">IA Principal — qualificação e conversa com o lead</div></div>
  <div class="hp-card"><span class="hp-card-icon">🔄</span><div class="hp-card-title" style="color:#22c55e">GPT-5</div><div class="hp-card-sub">Fallback — ativa quando Claude dá rate limit</div></div>
  <div class="hp-card"><span class="hp-card-icon">🛡️</span><div class="hp-card-title" style="color:#3b82f6">Claude Sonnet 4.5</div><div class="hp-card-sub">Contingência — backup extra de segurança</div></div>
  <div class="hp-card"><span class="hp-card-icon">📝</span><div class="hp-card-title" style="color:#f97316">GPT-4o Mini</div><div class="hp-card-sub">Resumo — gera resumo da conversa no handoff</div></div>
  <div class="hp-card"><span class="hp-card-icon">🎤</span><div class="hp-card-title" style="color:#ec4899">OpenAI Whisper</div><div class="hp-card-sub">Transcrição — áudio do lead para texto</div></div>
  <div class="hp-card"><span class="hp-card-icon">👁️</span><div class="hp-card-title" style="color:#C8A24E">GPT-4o + Gemini</div><div class="hp-card-sub">Visão — análise de imagens, vídeos e documentos</div></div>
</div>
<h2 class="hp-section-title">Fila Inteligente (Redis)</h2>
<p class="hp-section-desc">Quando o lead envia várias msgs seguidas ("oi" + "tudo bem?" + áudio), o sistema agrupa tudo e responde de uma vez.</p>
<div class="hp-queue">
  <span class="hp-queue-item" style="background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.3);color:#ef4444">Msg 1</span>
  <span class="hp-queue-item" style="background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.3);color:#ef4444">Msg 2</span>
  <span class="hp-queue-item" style="background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.3);color:#ef4444">Msg 3</span>
  <span class="hp-queue-arrow">→</span>
  <span class="hp-queue-item" style="background:rgba(168,85,247,0.12);border:1px solid rgba(168,85,247,0.3);color:#a855f7">Redis Queue</span>
  <span class="hp-queue-arrow">→</span>
  <span class="hp-queue-item" style="background:rgba(34,197,94,0.12);border:1px solid rgba(34,197,94,0.3);color:#22c55e">1 resposta</span>
</div>
</div>

<div class="hp-panel-section" id="sec-clinicas">
<h2 class="hp-section-title">Base de Conhecimento — Clínicas</h2>
<div class="hp-cards hp-cards-3">
<div class="hp-card"><span class="hp-card-icon">✨</span><div style="display:flex;justify-content:space-between;align-items:center"><div class="hp-card-title">Dra. Renata Rezende</div><span class="hp-status hp-status-ok">Completo</span></div><div style="display:inline-block;padding:3px 10px;border-radius:6px;background:rgba(200,162,78,0.12);color:#C8A24E;font-size:.8em;font-weight:600;margin:6px 0">Protocolo RR</div><div class="hp-card-sub">Público: Mulheres, 35-55 anos</div><div class="hp-card-tags"><span class="hp-card-tag">Flacidez</span><span class="hp-card-tag">Bigode chinês</span><span class="hp-card-tag">Rugas</span><span class="hp-card-tag">Olhar cansado</span></div></div>
<div class="hp-card"><span class="hp-card-icon">💎</span><div style="display:flex;justify-content:space-between;align-items:center"><div class="hp-card-title">Dra. Gabriela Veloso</div><span class="hp-status hp-status-ok">Completo</span></div><div style="display:inline-block;padding:3px 10px;border-radius:6px;background:rgba(168,85,247,0.12);color:#a855f7;font-size:.8em;font-weight:600;margin:6px 0">Protocolo GV</div><div class="hp-card-sub">Público: Mulheres, 35-55 anos</div><div class="hp-card-tags"><span class="hp-card-tag">Rosto caído</span><span class="hp-card-tag">Linhas de marionete</span><span class="hp-card-tag">Flacidez</span></div></div>
<div class="hp-card"><span class="hp-card-icon">🌸</span><div style="display:flex;justify-content:space-between;align-items:center"><div class="hp-card-title">Dra. Aline di Toro</div><span class="hp-status hp-status-warn">Incompleto</span></div><div style="display:inline-block;padding:3px 10px;border-radius:6px;background:rgba(236,72,153,0.12);color:#ec4899;font-size:.8em;font-weight:600;margin:6px 0">Protocolo Lumine FACE</div><div class="hp-card-sub">Público: A preencher</div></div>
<div class="hp-card"><span class="hp-card-icon">🌿</span><div style="display:flex;justify-content:space-between;align-items:center"><div class="hp-card-title">Dra. Raquel</div><span class="hp-status hp-status-ok">Completo</span></div><div style="display:inline-block;padding:3px 10px;border-radius:6px;background:rgba(34,197,94,0.12);color:#22c55e;font-size:.8em;font-weight:600;margin:6px 0">Protocolo New Naturee</div><div class="hp-card-sub">Público: Mulheres, 35-55 anos</div><div class="hp-card-tags"><span class="hp-card-tag">Flacidez</span><span class="hp-card-tag">Bigode chinês</span><span class="hp-card-tag">Olheiras</span><span class="hp-card-tag">Rugas</span></div></div>
<div class="hp-card"><span class="hp-card-icon">💫</span><div style="display:flex;justify-content:space-between;align-items:center"><div class="hp-card-title">Dra. Karise</div><span class="hp-status hp-status-ok">Completo</span></div><div style="display:inline-block;padding:3px 10px;border-radius:6px;background:rgba(59,130,246,0.12);color:#3b82f6;font-size:.8em;font-weight:600;margin:6px 0">Protocolo Lumi Lift</div><div class="hp-card-sub">Público: Mulheres, 35-55 anos</div><div class="hp-card-tags"><span class="hp-card-tag">Rosto derretendo</span><span class="hp-card-tag">Linhas de marionete</span><span class="hp-card-tag">Olhar cansado</span></div></div>
</div>
<div class="hp-info-box warn"><span class="hp-info-title">⚠️ Ação necessária</span>Completar dados da <strong>Dra. Aline di Toro</strong> — Protocolo Lumine FACE (informações sobre protocolo, dores, casos de sucesso)</div>
</div>

<div class="hp-panel-section" id="sec-rules">
<h2 class="hp-section-title">Limitações do Agente (Regras Rígidas)</h2>
<div class="hp-rules">
  <div class="hp-rule danger"><span class="hp-rule-icon">🚫</span><span class="hp-rule-text">NÃO pode prometer desconto ou condição especial</span></div>
  <div class="hp-rule danger"><span class="hp-rule-icon">🚫</span><span class="hp-rule-text">NÃO pode agendar consulta (só Hunter agenda)</span></div>
  <div class="hp-rule danger"><span class="hp-rule-icon">🚫</span><span class="hp-rule-text">NÃO pode passar preço</span></div>
  <div class="hp-rule danger"><span class="hp-rule-icon">🚫</span><span class="hp-rule-text">NÃO pode falar de procedimentos fora do protocolo</span></div>
  <div class="hp-rule critical"><span class="hp-rule-icon">👻</span><span class="hp-rule-text">Handoff invisível — lead NUNCA percebe a troca</span></div>
  <div class="hp-rule success"><span class="hp-rule-icon">💕</span><span class="hp-rule-text">Tom acolhedor, se passa por humano</span></div>
  <div class="hp-rule success"><span class="hp-rule-icon">⏱️</span><span class="hp-rule-text">Resposta em &lt; 90 segundos</span></div>
  <div class="hp-rule success"><span class="hp-rule-icon">🌙</span><span class="hp-rule-text">Disponibilidade 24/7</span></div>
</div>
<h2 class="hp-section-title">Checklist de Funcionalidades</h2>
<p class="hp-section-desc">Clique nos itens para marcar/desmarcar.</p>
<div class="hp-checklist" id="checklist">
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Iniciar conversa &lt; 2min após formulário</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Mensagem personalizada com dados do formulário</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Tom acolhedor, se passa por humano</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Qualificação (dores, contexto, protocolo)</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Handoff invisível para Hunter</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Follow-up automático (5 msgs / 7 dias)</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Budget alto → Hunter direto (sem agente)</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Resumo da conversa no handoff</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Processamento de áudio (Whisper)</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Processamento de imagem (GPT-4o)</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Processamento de vídeo (Gemini)</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Dashboard de métricas diárias</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Monitoramento de custos por API</div></div>
  <div class="hp-check-item checked"><div class="hp-check-box">✓</div><div class="hp-check-label">Sistema de contingência (fallback IA)</div></div>
</div>
<h2 class="hp-section-title">Critérios de Handoff</h2>
<div class="hp-handoff-grid">
<div class="hp-handoff-box pass"><div class="hp-handoff-title" style="color:#22c55e">✅ PASSA PRA HUNTER</div><div class="hp-handoff-item">→ Budget ALTO no formulário (direto)</div><div class="hp-handoff-item">→ 3+ mensagens com engajamento</div><div class="hp-handoff-item">→ Interesse explícito em agendar</div><div class="hp-handoff-item">→ Pergunta que agente não sabe</div><div class="hp-handoff-item">→ Pediu pra falar com humano</div></div>
<div class="hp-handoff-box fail"><div class="hp-handoff-title" style="color:#ef4444">🚫 NÃO PASSA</div><div class="hp-handoff-item">→ Lead não responde</div><div class="hp-handoff-item">→ Respostas monossilábicas (sem engajamento)</div><div class="hp-handoff-item">→ Diz que não tem interesse agora</div><div class="hp-handoff-item">→ Sem curiosidade sobre o protocolo</div></div>
</div>
<div class="hp-info-box info"><span class="hp-info-title">ℹ️ Definição de Engajamento</span>Resposta com mais de 5 palavras · Fez pergunta de volta · Demonstrou curiosidade sobre o protocolo · Compartilhou informação pessoal (dor, desejo, frustração)</div>
</div>

<script>
(function(){
  document.querySelectorAll('.hp-panel-tab').forEach(function(tab){
    tab.addEventListener('click',function(){
      document.querySelectorAll('.hp-panel-tab').forEach(function(t){t.classList.remove('active')});
      document.querySelectorAll('.hp-panel-section').forEach(function(s){s.classList.remove('active')});
      tab.classList.add('active');
      var sec=document.getElementById('sec-'+tab.getAttribute('data-tab'));
      if(sec)sec.classList.add('active');
    });
  });
  document.querySelectorAll('.hp-journey-step').forEach(function(step){
    step.addEventListener('click',function(){
      var w=step.classList.contains('active');
      document.querySelectorAll('.hp-journey-step').forEach(function(s){s.classList.remove('active')});
      if(!w)step.classList.add('active');
    });
  });
  var msgs=[
    {from:'agent',text:'Olá, Denise! Sou a Ana, consultora da Dra. Renata Rezende! Vi que você se inscreveu e fiquei impressionada com o quanto você se conhece 😊'},
    {from:'lead',text:'Oi Ana! Sim, já pesquisei bastante...'},
    {from:'agent',text:'Denise, o que você gostaria de ver de diferente no seu rosto agora que talvez não tenha alcançado nos últimos procedimentos?'},
    {from:'lead',text:'Queria resolver as linhas de marionete e o bigode chinês de uma vez, cansei de botox que não resolve tudo'},
    {from:'agent',text:'Entendi! O Protocolo RR trata TODAS essas queixas de forma integrada. É um protocolo que olha seu rosto como um todo e resolve de forma harmônica!'},
    {from:'lead',text:'Que interessante! Como funciona na prática?'},
    {from:'system',text:'Lead qualificada — 3+ msgs com engajamento — HANDOFF para Hunter'},
    {from:'hunter',text:'Denise, que bom que você se interessou! Eu sou a Camila, vou te explicar tudo e agendar sua avaliação com a Dra. Renata'}
  ];
  var step=0,body=document.getElementById('chatBody'),btn=document.getElementById('chatNext'),rst=document.getElementById('chatReset');
  function addMsg(){
    if(step>=msgs.length)return;
    if(step===0)body.innerHTML='';
    var m=msgs[step],d=document.createElement('div');
    d.className='hp-chat-msg '+m.from;
    if(m.from==='hunter'){d.innerHTML='<span class="hp-chat-label hp-chat-label-hunter">HUNTER</span>'+m.text}
    else{d.textContent=m.text}
    body.appendChild(d);body.scrollTop=body.scrollHeight;step++;
    if(step>=msgs.length){btn.textContent='Conversa finalizada';btn.disabled=true}
    else{btn.textContent='Próxima ('+(step+1)+'/'+msgs.length+')'}
  }
  function reset(){step=0;body.innerHTML='<div class="hp-chat-empty">Clique em "Próxima" para simular a conversa</div>';btn.textContent='Próxima (1/'+msgs.length+')';btn.disabled=false}
  if(btn)btn.addEventListener('click',addMsg);
  if(rst)rst.addEventListener('click',reset);
  document.querySelectorAll('.hp-check-item').forEach(function(item){
    item.addEventListener('click',function(){
      item.classList.toggle('checked');
      item.querySelector('.hp-check-box').textContent=item.classList.contains('checked')?'✓':'';
    });
  });
  function counters(){
    document.querySelectorAll('[data-count]').forEach(function(el){
      var t=parseInt(el.getAttribute('data-count')),c=0,s=Math.max(1,Math.floor(t/30));
      var i=setInterval(function(){c+=s;if(c>=t){c=t;clearInterval(i)}el.textContent=c+'+'},40);
    });
  }
  if(document.readyState==='complete'){counters()}else{window.addEventListener('load',counters)}
})();
</script>