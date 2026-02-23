#!/usr/bin/env python3
"""
HarmonizaPRO — Gerador de documentação a partir de exports JSON do n8n.

Uso:
    python tools/generate_docs.py

Coloque os JSON exportados do n8n em: workflows/exports/
Os docs serão gerados em: docs/workflows/
"""

import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "workflows" / "exports"
OUT = ROOT / "docs" / "workflows"


def load_workflow(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def summarize(workflow: dict) -> dict:
    nodes = workflow.get("nodes", [])
    name = workflow.get("name", "Workflow sem nome")

    # Detectar webhook
    webhook = next((n for n in nodes if "webhook" in n.get("type", "").lower()), None)
    webhook_info = None
    if webhook:
        params = webhook.get("parameters", {})
        webhook_info = {
            "method": params.get("httpMethod", "POST"),
            "path": params.get("path", "<não detectado>"),
            "name": webhook.get("name", "Webhook"),
        }

    # Contar tipos de nós
    type_counts = Counter(n.get("type") for n in nodes)

    # Detectar tabelas Supabase e operações
    sb = [n for n in nodes if n.get("type") == "n8n-nodes-base.supabase"]
    supabase_tables = defaultdict(set)
    for n in sb:
        params = n.get("parameters", {})
        table = params.get("tableId")
        op = params.get("operation")
        if table:
            supabase_tables[table].add(op or "unknown")

    # Detectar HTTP requests (UaZapi e outros)
    http_nodes = [n for n in nodes if n.get("type") == "n8n-nodes-base.httpRequest"]
    http_endpoints = []
    for n in http_nodes:
        params = n.get("parameters", {})
        http_endpoints.append({
            "name": n.get("name", "HTTP Request"),
            "method": params.get("method", "GET"),
            "url": params.get("url", "<não detectado>"),
        })

    # Detectar nós de AI/LLM
    ai_nodes = [n for n in nodes if "agent" in n.get("type", "").lower() or "llm" in n.get("type", "").lower() or "openai" in n.get("type", "").lower() or "anthropic" in n.get("type", "").lower()]
    ai_info = []
    for n in ai_nodes:
        ai_info.append({
            "name": n.get("name", "AI Node"),
            "type": n.get("type"),
        })

    return {
        "name": name,
        "webhook": webhook_info,
        "type_counts": type_counts,
        "supabase_tables": supabase_tables,
        "http_endpoints": http_endpoints,
        "ai_nodes": ai_info,
        "node_count": len(nodes),
    }


def render_md(summary: dict, export_path: Path) -> str:
    w = summary["webhook"]
    webhook_line = f"- **Webhook:** `{w['method']} /{w['path']}` (nó: {w['name']})" if w else "- **Trigger:** <preencher>"

    # Supabase
    sb_lines = []
    for table, ops in sorted(summary["supabase_tables"].items()):
        ops_txt = ", ".join(sorted(o for o in ops if o))
        sb_lines.append(f"- `{table}` — operações: {ops_txt}")
    sb_block = "\n".join(sb_lines) if sb_lines else "- (nenhuma detectada)"

    # HTTP endpoints
    http_lines = []
    for e in summary["http_endpoints"]:
        http_lines.append(f"- `{e['method']}` — {e['name']} — `{e['url']}`")
    http_block = "\n".join(http_lines) if http_lines else "- (nenhum detectado)"

    # AI nodes
    ai_lines = []
    for a in summary["ai_nodes"]:
        ai_lines.append(f"- {a['name']} (`{a['type']}`)")
    ai_block = "\n".join(ai_lines) if ai_lines else "- (nenhum detectado)"

    # Top tipos de nós
    top_types = summary["type_counts"].most_common(10)
    types_block = "\n".join([f"- `{t}`: {c}" for t, c in top_types])

    return f"""# {summary['name']}

> **Arquivo n8n (export):** `{export_path.as_posix()}`  
> **Nós totais:** {summary['node_count']}  
> **Status:** <preencher>  
> **Owner:** <preencher>  
> **Última revisão:** <YYYY-MM-DD>

## Objetivo

- <preencher em 1–3 bullets>

## Quando roda (Trigger)

{webhook_line}

## Entradas esperadas (Payload)

```json
{{
  "chat_id": "...",
  "sender": "...",
  "message": "..."
}}
```

## Saídas

- <preencher>

## Integrações e dependências

### Supabase (detectado do JSON)

{sb_block}

### HTTP Requests (detectado do JSON)

{http_block}

### AI / LLM (detectado do JSON)

{ai_block}

### Tipos de nós mais usados (top 10)

{types_block}

## Regras de negócio

**Handoff:**

- <preencher>

**Follow-up:**

- <preencher>

**Tokens/custos:**

- <preencher>

## Fluxo em alto nível (resumo)

1. <preencher>
2. <preencher>
3. <preencher>

## Nós críticos

| Nó | Motivo | Como detectar | Como corrigir |
|----|--------|--------------|---------------|
| <preencher> | | | |

## Testes (casos)

**Caso 1:** <preencher>

**Caso 2:** <preencher>

## Changelog

| Data | Mudança | Por quem |
|------|---------|----------|
| <preencher> | | |
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    exports = list(EXPORTS.glob("*.json"))
    if not exports:
        print(f"⚠️  Nenhum JSON encontrado em: {EXPORTS}")
        print(f"   Coloque os exports do n8n em: {EXPORTS}")
        return

    for export in exports:
        wf = load_workflow(export)
        s = summarize(wf)

        slug = export.stem.lower().replace(" ", "-")
        out_md = OUT / f"{slug}.md"
        out_md.write_text(
            render_md(s, export_path=export.relative_to(ROOT)),
            encoding="utf-8"
        )
        print(f"✅ Gerado: {out_md}")

    print(f"\n📋 Total: {len(exports)} workflow(s) processado(s)")
    print(f"   Agora preencha as partes humanas nos arquivos gerados em: {OUT}")


if __name__ == "__main__":
    main()
