# 💰 Custos por Workflow

<div id="custos-loading" style="text-align:center; padding:20px; color:#999;">Carregando dados de custos...</div>

<div id="custos-error" style="display:none; text-align:center; padding:20px; color:#ff5555; background:rgba(255,85,85,0.1); border-radius:8px; margin:16px 0;">
  ⚠️ Não foi possível carregar os custos. Verifique a conexão.
</div>

<div id="custos-content" style="display:none;" markdown>

## Última Semana

<div class="hp-metrics-grid">
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="c-total-usd">$—</span>
    <span class="hp-metric-label">Custo Total (USD)</span>
    <span class="hp-metric-desc">Todas as APIs combinadas</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="c-total-brl">R$ —</span>
    <span class="hp-metric-label">Custo Total (BRL)</span>
    <span class="hp-metric-desc" id="c-cotacao">Câmbio: R$ 5,80</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="c-por-lead">R$ —</span>
    <span class="hp-metric-label">Custo por Lead</span>
    <span class="hp-metric-desc" id="c-leads-count">— leads no período</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="c-por-handoff">R$ —</span>
    <span class="hp-metric-label">Custo por Handoff</span>
    <span class="hp-metric-desc" id="c-handoffs-count">— handoffs no período</span>
  </div>
</div>

## Breakdown por API

<div class="hp-metrics-grid">
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="c-anthropic" style="color:#a855f7;">$—</span>
    <span class="hp-metric-label">🟣 Anthropic (Claude)</span>
    <span class="hp-metric-desc" id="c-anthropic-tokens">— tokens</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="c-openai" style="color:#22c55e;">$—</span>
    <span class="hp-metric-label">🟢 OpenAI (GPT + Whisper)</span>
    <span class="hp-metric-desc" id="c-openai-tokens">— tokens</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="c-google" style="color:#3b82f6;">$—</span>
    <span class="hp-metric-label">🔵 Google (Gemini)</span>
    <span class="hp-metric-desc">Vídeo e documentos</span>
  </div>
</div>

<div id="c-alert-box" style="display:none; margin:20px 0; padding:16px; border-radius:8px; background:rgba(255,85,85,0.1); border:1px solid #ff5555;">
  🚨 <strong>Alerta:</strong> <span id="c-alert-text"></span>
</div>

<div id="c-ok-box" style="display:none; margin:20px 0; padding:16px; border-radius:8px; background:rgba(46,125,50,0.1); border:1px solid #2E7D32;">
  ✅ <strong>Custos dentro do esperado</strong> — threshold: <span id="c-threshold"></span>/semana
</div>

## Histórico Semanal

<table id="tabela-custos">
  <thead>
    <tr>
      <th>Período</th>
      <th>Leads</th>
      <th>Handoffs</th>
      <th>Anthropic</th>
      <th>OpenAI</th>
      <th>Google</th>
      <th>Total (USD)</th>
      <th>Total (BRL)</th>
      <th>$/Lead</th>
    </tr>
  </thead>
  <tbody id="tbody-custos">
    <tr><td colspan="9" style="text-align:center; color:#999;">Carregando...</td></tr>
  </tbody>
</table>

## ROI Estimado

<div class="hp-metrics-grid">
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="c-roi">—x</span>
    <span class="hp-metric-label">ROI Estimado</span>
    <span class="hp-metric-desc">Receita potencial / Custo IA</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="c-receita">R$ —</span>
    <span class="hp-metric-label">Receita Potencial</span>
    <span class="hp-metric-desc">Handoffs × 50% conversão × R$ 15k</span>
  </div>
</div>

<div id="c-periodo-ref" style="text-align:center; margin-top:24px; font-size:0.8em; color:#666;">
  Período: — | Atualizado em: —
</div>

---

## Referência de Preços

| Modelo | Input (por 1M tokens) | Output (por 1M tokens) | Uso |
|:-------|:----------------------|:-----------------------|:----|
| Claude Sonnet 4 | $3.00 | $15.00 | Agente principal |
| Claude Sonnet 4.5 | $3.00 | $15.00 | Contingência |
| GPT-5 | $2.00 | $8.00 | Fallback |
| GPT-4o Mini | $0.15 | $0.60 | Resumos |
| Whisper | $0.006/min | — | Transcrição |
| Gemini Flash | $0.075 | $0.30 | Vídeo/docs |

</div>

<script>
const SUPABASE_URL = 'https://jauunacntwpztmzgpeft.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_FOMLi0oiTU9Iya7MlpLkYw_NWoKTGYS';

const headers = {
  'apikey': SUPABASE_ANON_KEY,
  'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
  'Content-Type': 'application/json'
};

function fmt(n, decimals) {
  return parseFloat(n || 0).toFixed(decimals ?? 2);
}

function fmtBR(n) {
  return parseFloat(n || 0).toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function fmtTokens(n) {
  const v = parseInt(n || 0);
  if (v >= 1000000) return (v / 1000000).toFixed(1) + 'M';
  if (v >= 1000) return (v / 1000).toFixed(1) + 'k';
  return v.toString();
}

async function carregarCustos() {
  try {
    const res = await fetch(
      `${SUPABASE_URL}/rest/v1/custos_semanais?order=periodo_fim.desc&limit=12`,
      { headers }
    );

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const dados = await res.json();

    if (!dados || dados.length === 0) {
      document.getElementById('custos-loading').style.display = 'none';
      document.getElementById('custos-error').style.display = 'block';
      document.getElementById('custos-error').innerHTML = '📭 Nenhum dado de custos encontrado. Execute o workflow "Monitoramento de Custos Semanal" no n8n.';
      return;
    }

    // Última semana
    const h = dados[0];

    document.getElementById('c-total-usd').textContent = `$${fmt(h.custo_total_usd)}`;
    document.getElementById('c-total-brl').textContent = `R$ ${fmtBR(h.custo_total_brl)}`;
    document.getElementById('c-cotacao').textContent = `Câmbio: R$ ${fmt(h.cotacao_usd_brl)}`;
    document.getElementById('c-por-lead').textContent = `R$ ${fmtBR(h.custo_por_lead)}`;
    document.getElementById('c-por-handoff').textContent = `R$ ${fmtBR(h.custo_por_handoff)}`;
    document.getElementById('c-leads-count').textContent = `${h.leads_no_periodo || 0} leads no período`;
    document.getElementById('c-handoffs-count').textContent = `${h.handoffs_no_periodo || 0} handoffs no período`;

    document.getElementById('c-anthropic').textContent = `$${fmt(h.anthropic_custo_usd, 4)}`;
    document.getElementById('c-openai').textContent = `$${fmt(h.openai_custo_usd, 4)}`;
    document.getElementById('c-google').textContent = `$${fmt(h.google_custo_usd, 4)}`;
    document.getElementById('c-anthropic-tokens').textContent = `${fmtTokens(h.anthropic_tokens_input)} in / ${fmtTokens(h.anthropic_tokens_output)} out`;
    document.getElementById('c-openai-tokens').textContent = `${fmtTokens(h.openai_tokens_input)} in / ${fmtTokens(h.openai_tokens_output)} out`;

    // Alerta
    if (h.acima_do_threshold) {
      document.getElementById('c-alert-box').style.display = 'block';
      document.getElementById('c-alert-text').textContent = `Custo de $${fmt(h.custo_total_usd)} excedeu o threshold de $${fmt(h.threshold_usd)}/semana`;
    } else {
      document.getElementById('c-ok-box').style.display = 'block';
      document.getElementById('c-threshold').textContent = `$${fmt(h.threshold_usd)}`;
    }

    // ROI
    const handoffs = h.handoffs_no_periodo || 0;
    const conversao = 0.5;
    const ticketMedio = 15000;
    const receitaPotencial = handoffs * conversao * ticketMedio;
    const custoBrl = parseFloat(h.custo_total_brl || 0);
    const roi = custoBrl > 0 ? Math.round(receitaPotencial / custoBrl) : 0;

    document.getElementById('c-roi').textContent = `${roi.toLocaleString('pt-BR')}x`;
    document.getElementById('c-receita').textContent = `R$ ${receitaPotencial.toLocaleString('pt-BR')}`;

    if (roi >= 100) document.getElementById('c-roi').style.color = '#2E7D32';
    else if (roi >= 10) document.getElementById('c-roi').style.color = '#C8A24E';
    else document.getElementById('c-roi').style.color = '#ff5555';

    // Período
    document.getElementById('c-periodo-ref').textContent =
      `Período: ${h.periodo_inicio} → ${h.periodo_fim} | Atualizado em: ${new Date(h.calculado_em).toLocaleString('pt-BR')}`;

    // Tabela histórica
    const tbody = document.getElementById('tbody-custos');
    tbody.innerHTML = '';

    dados.forEach(d => {
      const row = document.createElement('tr');
      const custoLead = d.leads_no_periodo > 0 ? `R$ ${fmtBR(d.custo_por_lead)}` : '—';
      row.innerHTML = `
        <td>${d.periodo_inicio} → ${d.periodo_fim}</td>
        <td>${d.leads_no_periodo || 0}</td>
        <td>${d.handoffs_no_periodo || 0}</td>
        <td>$${fmt(d.anthropic_custo_usd, 4)}</td>
        <td>$${fmt(d.openai_custo_usd, 4)}</td>
        <td>$${fmt(d.google_custo_usd, 4)}</td>
        <td>$${fmt(d.custo_total_usd)}</td>
        <td>R$ ${fmtBR(d.custo_total_brl)}</td>
        <td>${custoLead}</td>
      `;
      if (d.acima_do_threshold) row.style.background = 'rgba(255,85,85,0.08)';
      tbody.appendChild(row);
    });

    // Mostrar
    document.getElementById('custos-loading').style.display = 'none';
    document.getElementById('custos-content').style.display = 'block';

  } catch (err) {
    console.error('Erro ao carregar custos:', err);
    document.getElementById('custos-loading').style.display = 'none';
    document.getElementById('custos-error').style.display = 'block';
  }
}

document.addEventListener('DOMContentLoaded', carregarCustos);
if (document.readyState !== 'loading') carregarCustos();
</script>