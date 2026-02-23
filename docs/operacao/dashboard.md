# 📊 Dashboard de Métricas

<div id="dash-loading" style="text-align:center; padding:20px; color:#999;">Carregando métricas do Supabase...</div>

<div id="dash-error" style="display:none; text-align:center; padding:20px; color:#ff5555; background:rgba(255,85,85,0.1); border-radius:8px; margin:16px 0;">
  ⚠️ Não foi possível carregar as métricas. Verifique a conexão.
</div>

<div id="dash-content" style="display:none;" markdown>

## Métricas de Ontem

<div class="hp-metrics-grid">
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="m-leads-novos">—</span>
    <span class="hp-metric-label">Leads Novos</span>
    <span class="hp-metric-desc">Entraram no dia</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="m-leads-total">—</span>
    <span class="hp-metric-label">Leads Total</span>
    <span class="hp-metric-desc">Base acumulada</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="m-handoffs">—</span>
    <span class="hp-metric-label">Handoffs</span>
    <span class="hp-metric-desc">Transferidos para Hunter</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="m-taxa">—%</span>
    <span class="hp-metric-label">Taxa de Qualificação</span>
    <span class="hp-metric-desc">Handoffs / Leads novos</span>
    <span class="hp-metric-target">Meta: >40%</span>
  </div>
</div>

## Performance da IA

<div class="hp-metrics-grid">
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="m-followups">—</span>
    <span class="hp-metric-label">Follow-ups Enviados</span>
    <span class="hp-metric-desc">Reengajamento automático</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="m-reengajamento">—%</span>
    <span class="hp-metric-label">Taxa Reengajamento</span>
    <span class="hp-metric-desc">Responderam após follow-up</span>
    <span class="hp-metric-target">Meta: >20%</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="m-ratelimits">—</span>
    <span class="hp-metric-label">Rate Limits</span>
    <span class="hp-metric-desc">Contingências acionadas</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="m-erros">—</span>
    <span class="hp-metric-label">Erros</span>
    <span class="hp-metric-desc">Execuções com falha</span>
  </div>
</div>

## Custo Operacional

<div class="hp-metrics-grid">
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="m-custo-usd">$—</span>
    <span class="hp-metric-label">Custo IA (USD)</span>
    <span class="hp-metric-desc">Anthropic + OpenAI</span>
  </div>
  <div class="hp-metric-card">
    <span class="hp-metric-value" id="m-custo-brl">R$ —</span>
    <span class="hp-metric-label">Custo IA (BRL)</span>
    <span class="hp-metric-desc">Câmbio R$ 5,80</span>
  </div>
</div>

<div id="m-data-ref" style="text-align:center; margin-top:24px; font-size:0.8em; color:#666;">
  Dados referentes a: —
</div>

---

## Últimos 7 Dias

<table id="tabela-semana">
  <thead>
    <tr>
      <th>Data</th>
      <th>Leads</th>
      <th>Handoffs</th>
      <th>Taxa</th>
      <th>Follow-ups</th>
      <th>Rate Limits</th>
      <th>Custo (USD)</th>
    </tr>
  </thead>
  <tbody id="tbody-semana">
    <tr><td colspan="7" style="text-align:center; color:#999;">Carregando...</td></tr>
  </tbody>
</table>

</div>

<script>
// =============================================
// CONFIG — Altere aqui com seus dados
// =============================================
const SUPABASE_URL = 'https://jauunacntwpztmzgpeft.supabase.co';
const SUPABASE_ANON_KEY ='sb_publishable_FOMLi0oiTU9Iya7MlpLkYw_NWoKTGYS';
// =============================================

const headers = {
  'apikey': SUPABASE_ANON_KEY,
  'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
  'Content-Type': 'application/json'
};

async function carregarMetricas() {
  try {
    // Buscar últimos 7 dias
    const res = await fetch(
      `${SUPABASE_URL}/rest/v1/metricas_diarias?order=data.desc&limit=7`,
      { headers }
    );

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const dados = await res.json();

    if (!dados || dados.length === 0) {
      document.getElementById('dash-loading').style.display = 'none';
      document.getElementById('dash-error').style.display = 'block';
      document.getElementById('dash-error').innerHTML = '📭 Nenhuma métrica encontrada ainda. Execute o workflow "Métricas Diárias" no n8n.';
      return;
    }

    // Preencher cards com o dia mais recente
    const hoje = dados[0];

    document.getElementById('m-leads-novos').textContent = hoje.leads_novos ?? 0;
    document.getElementById('m-leads-total').textContent = (hoje.leads_total ?? 0).toLocaleString('pt-BR');
    document.getElementById('m-handoffs').textContent = hoje.handoffs_realizados ?? 0;
    document.getElementById('m-taxa').textContent = (hoje.taxa_qualificacao ?? 0) + '%';
    document.getElementById('m-followups').textContent = hoje.followups_enviados ?? 0;
    document.getElementById('m-reengajamento').textContent = (hoje.taxa_reengajamento ?? 0) + '%';
    document.getElementById('m-ratelimits').textContent = hoje.rate_limits ?? 0;
    document.getElementById('m-erros').textContent = hoje.erros_execucao ?? 0;

    const custoUsd = parseFloat(hoje.custo_total_ia ?? 0).toFixed(2);
    const custoBrl = (custoUsd * 5.80).toFixed(2);
    document.getElementById('m-custo-usd').textContent = `$${custoUsd}`;
    document.getElementById('m-custo-brl').textContent = `R$ ${custoBrl}`;

    // Data de referência
    const dataRef = new Date(hoje.data + 'T00:00:00');
    document.getElementById('m-data-ref').textContent =
      `Dados referentes a: ${dataRef.toLocaleDateString('pt-BR')} — atualizado em ${new Date(hoje.calculado_em).toLocaleString('pt-BR')}`;

    // Colorir taxa de qualificação
    const taxaEl = document.getElementById('m-taxa');
    const taxaVal = parseFloat(hoje.taxa_qualificacao ?? 0);
    if (taxaVal >= 40) taxaEl.style.color = '#2E7D32';
    else if (taxaVal >= 20) taxaEl.style.color = '#C8A24E';
    else taxaEl.style.color = '#ff5555';

    // Colorir erros
    const errosEl = document.getElementById('m-erros');
    const errosVal = parseInt(hoje.erros_execucao ?? 0);
    if (errosVal === 0) errosEl.style.color = '#2E7D32';
    else if (errosVal <= 5) errosEl.style.color = '#C8A24E';
    else errosEl.style.color = '#ff5555';

    // Tabela dos últimos 7 dias
    const tbody = document.getElementById('tbody-semana');
    tbody.innerHTML = '';

    dados.forEach(d => {
      const data = new Date(d.data + 'T00:00:00').toLocaleDateString('pt-BR');
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${data}</td>
        <td>${d.leads_novos ?? 0}</td>
        <td>${d.handoffs_realizados ?? 0}</td>
        <td>${(d.taxa_qualificacao ?? 0)}%</td>
        <td>${d.followups_enviados ?? 0}</td>
        <td>${d.rate_limits ?? 0}</td>
        <td>$${parseFloat(d.custo_total_ia ?? 0).toFixed(2)}</td>
      `;
      tbody.appendChild(row);
    });

    // Mostrar conteúdo
    document.getElementById('dash-loading').style.display = 'none';
    document.getElementById('dash-content').style.display = 'block';

  } catch (err) {
    console.error('Erro ao carregar métricas:', err);
    document.getElementById('dash-loading').style.display = 'none';
    document.getElementById('dash-error').style.display = 'block';
  }
}

// Carregar ao abrir a página
document.addEventListener('DOMContentLoaded', carregarMetricas);
// Fallback caso DOMContentLoaded já tenha disparado
if (document.readyState !== 'loading') carregarMetricas();
</script>
