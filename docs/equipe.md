# Equipe

<style>
/* ===== HERO ===== */
.hp-equipe-hero{text-align:center;padding:32px 20px 24px;border-bottom:1px solid rgba(200,162,78,0.15);margin-bottom:32px}
.hp-equipe-hero p{color:#999;font-size:.95em;max-width:640px;margin:0 auto 24px;line-height:1.6}
.hp-equipe-stats{display:flex;justify-content:center;gap:40px;flex-wrap:wrap;margin-top:20px}
.hp-equipe-stat{text-align:center}
.hp-equipe-stat-val{font-size:1.8em;font-weight:700;color:var(--hp-gold,#C8A24E);display:block}
.hp-equipe-stat-label{font-size:.75em;color:#888;text-transform:uppercase;letter-spacing:.5px}

/* ===== PILARES ===== */
.hp-pilares{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin:0 0 40px}
.hp-pilar{text-align:center;padding:24px 16px;border-radius:14px;border:1px solid rgba(200,162,78,0.1);background:rgba(200,162,78,0.02);transition:all .3s}
.hp-pilar:hover{border-color:rgba(200,162,78,0.35);transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,0.1)}
.hp-pilar-icon{font-size:2em;margin-bottom:8px;display:block}
.hp-pilar-title{font-weight:700;font-size:.95em;margin-bottom:4px}
.hp-pilar-desc{font-size:.78em;color:#888;line-height:1.4}

/* ===== TEAM GRID ===== */
.hp-team-section-title{font-size:1.2em;font-weight:700;color:var(--hp-gold,#C8A24E);margin:40px 0 8px;padding-bottom:8px;border-bottom:1px solid rgba(200,162,78,0.2)}
.hp-team-section-desc{color:#888;font-size:.85em;margin-bottom:20px}

.hp-team-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:24px;margin:24px 0}

.hp-team-card{background:rgba(200,162,78,0.02);border:1px solid rgba(200,162,78,0.12);border-radius:16px;padding:0;overflow:hidden;transition:all .4s cubic-bezier(.4,0,.2,1);position:relative}
.hp-team-card:hover{border-color:rgba(200,162,78,0.5);transform:translateY(-5px);box-shadow:0 16px 40px rgba(0,0,0,0.15)}
.hp-team-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,transparent,var(--hp-gold,#C8A24E),transparent);opacity:0;transition:opacity .4s}
.hp-team-card:hover::before{opacity:1}

.hp-team-card-header{padding:28px 24px 16px;display:flex;align-items:center;gap:18px}

.hp-team-photo{width:72px;height:72px;border-radius:50%;object-fit:cover;border:3px solid rgba(200,162,78,0.3);flex-shrink:0;transition:border-color .3s}
.hp-team-card:hover .hp-team-photo{border-color:var(--hp-gold,#C8A24E)}

.hp-team-photo-placeholder{width:72px;height:72px;border-radius:50%;background:linear-gradient(135deg,rgba(200,162,78,0.15),rgba(200,162,78,0.05));border:3px solid rgba(200,162,78,0.2);flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:1.8em;transition:border-color .3s}
.hp-team-card:hover .hp-team-photo-placeholder{border-color:var(--hp-gold,#C8A24E)}

.hp-team-info h3{margin:0 0 2px;font-size:1.1em;font-weight:700}
.hp-team-role{display:inline-block;padding:2px 10px;border-radius:12px;font-size:.72em;font-weight:600;margin-top:2px}
.hp-team-role.founder{background:rgba(200,162,78,0.15);color:var(--hp-gold,#C8A24E)}
.hp-team-role.dev{background:rgba(59,130,246,0.12);color:#60a5fa}
.hp-team-role.hunter{background:rgba(236,72,153,0.12);color:#ec4899}
.hp-team-role.ops{background:rgba(34,197,94,0.12);color:#22c55e}
.hp-team-role.design{background:rgba(168,85,247,0.12);color:#a855f7}
.hp-team-role.marketing{background:rgba(249,115,22,0.12);color:#f97316}

.hp-team-card-body{padding:0 24px 20px}
.hp-team-bio{font-size:.82em;color:#999;line-height:1.55;margin:0 0 14px}

.hp-team-tags{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:14px}
.hp-team-tag{padding:2px 8px;border-radius:4px;font-size:.68em;background:rgba(255,255,255,0.04);color:#777;border:1px solid rgba(255,255,255,0.06)}

.hp-team-links{display:flex;gap:8px}
.hp-team-links a{display:flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:8px;color:#888;border:1px solid rgba(200,162,78,0.12);transition:all .25s;text-decoration:none}
.hp-team-links a:hover{color:var(--hp-gold,#C8A24E);border-color:rgba(200,162,78,0.4);background:rgba(200,162,78,0.06);transform:scale(1.1)}

/* ===== ADD MEMBER CTA ===== */
.hp-team-add{border:2px dashed rgba(200,162,78,0.2);border-radius:16px;padding:40px 24px;text-align:center;transition:all .3s;cursor:default;min-height:200px;display:flex;flex-direction:column;align-items:center;justify-content:center}
.hp-team-add:hover{border-color:rgba(200,162,78,0.4);background:rgba(200,162,78,0.02)}
.hp-team-add-icon{font-size:2.5em;margin-bottom:8px;opacity:.4}
.hp-team-add-title{font-weight:600;font-size:.9em;color:#888;margin-bottom:4px}
.hp-team-add-desc{font-size:.75em;color:#666;line-height:1.4}

/* ===== TEMPLATE BOX ===== */
.hp-template-box{margin:32px 0;padding:20px 24px;border-radius:14px;border:1px solid rgba(200,162,78,0.15);background:rgba(200,162,78,0.02)}
.hp-template-title{font-size:1em;font-weight:700;color:var(--hp-gold,#C8A24E);margin-bottom:4px;display:flex;align-items:center;gap:8px}
.hp-template-desc{font-size:.82em;color:#888;margin-bottom:14px;line-height:1.5}
.hp-template-code{background:rgba(0,0,0,0.3);border-radius:10px;padding:16px;overflow-x:auto;font-size:.78em;line-height:1.6;color:#aaa;font-family:'JetBrains Mono',monospace;border:1px solid rgba(255,255,255,0.06)}
.hp-template-code .comment{color:#555}
.hp-template-code .tag{color:#C8A24E}
.hp-template-code .attr{color:#60a5fa}
.hp-template-code .value{color:#22c55e}

[data-md-color-scheme="default"] .hp-team-card{background:rgba(200,162,78,0.03)}
[data-md-color-scheme="default"] .hp-template-code{background:rgba(0,0,0,0.05)}
</style>

<!-- ===== HERO ===== -->
<div class="hp-equipe-hero">
  <p>A HarmonizaPRO nasceu da união entre estratégia digital e tecnologia para transformar clínicas de harmonização facial em negócios de alto desempenho.</p>
  <div class="hp-equipe-stats">
    <div class="hp-equipe-stat"><span class="hp-equipe-stat-val">4+</span><span class="hp-equipe-stat-label">Anos de mercado</span></div>
    <div class="hp-equipe-stat"><span class="hp-equipe-stat-val">200+</span><span class="hp-equipe-stat-label">Clínicas transformadas</span></div>
    <div class="hp-equipe-stat"><span class="hp-equipe-stat-val">R$ 30M+</span><span class="hp-equipe-stat-label">Vendidos em procedimentos</span></div>
    <div class="hp-equipe-stat"><span class="hp-equipe-stat-val">41+</span><span class="hp-equipe-stat-label">Workflows ativos</span></div>
  </div>
</div>


<!-- ===== FUNDADORES ===== -->
<h2 class="hp-team-section-title">Fundadores</h2>
<p class="hp-team-section-desc">Quem criou e lidera a operação HarmonizaPRO.</p>

<div class="hp-team-grid">

<div class="hp-team-card">
  <div class="hp-team-card-header">
    <img src="/assets/luciano.jpg" alt="Luciano Alberti" class="hp-team-photo">
    <div class="hp-team-info">
      <h3>Luciano Alberti</h3>
      <span class="hp-team-role founder">Sócio-Fundador</span>
    </div>
  </div>
  <div class="hp-team-card-body">
    <p class="hp-team-bio">Estrategista digital responsável pela metodologia que já gerou múltiplos milhões para clínicas de harmonização facial. Criador do Protocolo Miss e da operação comercial que transforma clínicas em negócios premium.</p>
    <div class="hp-team-tags">
      <span class="hp-team-tag">Estratégia</span>
      <span class="hp-team-tag">Comercial</span>
      <span class="hp-team-tag">Protocolo Miss</span>
    </div>
    <div class="hp-team-links">
      <a href="https://www.linkedin.com/in/luciano-alberti-2188431b9/" target="_blank" title="LinkedIn">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
      </a>
      <a href="https://www.instagram.com/lucianoaalberti/" target="_blank" title="Instagram">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
      </a>
    </div>
  </div>
</div>

</div>

<!-- ===== TIME TÉCNICO ===== -->
<h2 class="hp-team-section-title">Time Técnico</h2>
<p class="hp-team-section-desc">Quem constrói e mantém a infraestrutura de automação e IA.</p>

<div class="hp-team-grid">

<div class="hp-team-card">
  <div class="hp-team-card-header">
    <img src="/assets/pedro.jpg" alt="Pedro Vinicius" class="hp-team-photo">
    <div class="hp-team-info">
      <h3>Pedro Vinicius</h3>
      <span class="hp-team-role dev">Developer</span>
    </div>
  </div>
  <div class="hp-team-card-body">
    <p class="hp-team-bio">Desenvolvedor responsável pela arquitetura e implementação de toda a infraestrutura de automação. Constrói os workflows n8n, integrações com APIs (UaZapi, Supabase, Claude AI) e os agentes de IA que qualificam leads.</p>
    <div class="hp-team-tags">
      <span class="hp-team-tag">n8n</span>
      <span class="hp-team-tag">Claude AI</span>
      <span class="hp-team-tag">Supabase</span>
      <span class="hp-team-tag">UaZapi</span>
    </div>
    <div class="hp-team-links">
      <a href="https://www.linkedin.com/in/pedro-vinicius-8472351b7/" target="_blank" title="LinkedIn">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
      </a>
      <a href="https://github.com/viniciusDias1001" target="_blank" title="GitHub">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
      </a>
    </div>
  </div>
</div>

<!-- ===== CARD PLACEHOLDER: Adicionar novos membros ===== -->
<div class="hp-team-add">
  <div class="hp-team-add-icon">+</div>
  <div class="hp-team-add-title">Adicionar membro</div>
  <div class="hp-team-add-desc">Copie o template abaixo para adicionar<br>um novo membro à equipe</div>
</div>

</div>

<!-- ===== TEMPLATE PARA NOVOS MEMBROS ===== -->
<div class="hp-template-box">
  <div class="hp-template-title">📋 Template — Adicionar novo membro</div>
  <div class="hp-template-desc">Copie o bloco abaixo, cole dentro da <code>&lt;div class="hp-team-grid"&gt;</code> da seção correta e preencha os dados. Para a foto, coloque a imagem em <code>docs/assets/</code>.</div>
  <div class="hp-template-code">
<span class="comment">&lt;!-- NOVO MEMBRO: [Nome] --&gt;</span><br>
<span class="tag">&lt;div</span> <span class="attr">class</span>=<span class="value">"hp-team-card"</span><span class="tag">&gt;</span><br>
&nbsp;&nbsp;<span class="tag">&lt;div</span> <span class="attr">class</span>=<span class="value">"hp-team-card-header"</span><span class="tag">&gt;</span><br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">&lt;!-- OPÇÃO A: Com foto --&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;img</span> <span class="attr">src</span>=<span class="value">"/assets/nome.jpg"</span> <span class="attr">alt</span>=<span class="value">"Nome"</span> <span class="attr">class</span>=<span class="value">"hp-team-photo"</span><span class="tag">&gt;</span><br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">&lt;!-- OPÇÃO B: Sem foto (emoji placeholder) --&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">&lt;!-- &lt;div class="hp-team-photo-placeholder"&gt;👤&lt;/div&gt; --&gt;</span><br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;div</span> <span class="attr">class</span>=<span class="value">"hp-team-info"</span><span class="tag">&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;h3&gt;</span>Nome Completo<span class="tag">&lt;/h3&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">&lt;!-- Roles: founder, dev, hunter, ops, design, marketing --&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;span</span> <span class="attr">class</span>=<span class="value">"hp-team-role dev"</span><span class="tag">&gt;</span>Cargo<span class="tag">&lt;/span&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;/div&gt;</span><br>
&nbsp;&nbsp;<span class="tag">&lt;/div&gt;</span><br>
&nbsp;&nbsp;<span class="tag">&lt;div</span> <span class="attr">class</span>=<span class="value">"hp-team-card-body"</span><span class="tag">&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;p</span> <span class="attr">class</span>=<span class="value">"hp-team-bio"</span><span class="tag">&gt;</span>Descrição breve...<span class="tag">&lt;/p&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;div</span> <span class="attr">class</span>=<span class="value">"hp-team-tags"</span><span class="tag">&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;span</span> <span class="attr">class</span>=<span class="value">"hp-team-tag"</span><span class="tag">&gt;</span>Skill 1<span class="tag">&lt;/span&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;span</span> <span class="attr">class</span>=<span class="value">"hp-team-tag"</span><span class="tag">&gt;</span>Skill 2<span class="tag">&lt;/span&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;/div&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;div</span> <span class="attr">class</span>=<span class="value">"hp-team-links"</span><span class="tag">&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">&lt;!-- Adicione links de redes sociais aqui --&gt;</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">&lt;/div&gt;</span><br>
&nbsp;&nbsp;<span class="tag">&lt;/div&gt;</span><br>
<span class="tag">&lt;/div&gt;</span>
  </div>
</div>

<div style="text-align:center;padding:20px 0;color:#555;font-size:.8em">
  <strong>Cores disponíveis para roles:</strong><br>
  <span style="color:#C8A24E">■</span> founder · 
  <span style="color:#60a5fa">■</span> dev · 
  <span style="color:#ec4899">■</span> hunter · 
  <span style="color:#22c55e">■</span> ops · 
  <span style="color:#a855f7">■</span> design · 
  <span style="color:#f97316">■</span> marketing
</div>