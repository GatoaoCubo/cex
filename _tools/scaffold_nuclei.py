#!/usr/bin/env python3
"""scaffold_nuclei.py - Generate fractal 7x12 nucleus directory structure.

Usage:
  python _tools/scaffold_nuclei.py --dry-run
  python _tools/scaffold_nuclei.py --create
  python _tools/scaffold_nuclei.py --create --nucleus N03
"""

import argparse, yaml
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent

NUCLEI = {
    "N01": {"dir": "N01_intelligence", "label": "Inteligencia & Pesquisa", "fn": "research",
            "focus": "Mercado, competitors, trends, data analysis, benchmarks"},
    "N02": {"dir": "N02_marketing", "label": "Marketing & Comunicacao", "fn": "marketing",
            "focus": "Copy, branding, ads, social media, audience, funnels"},
    "N03": {"dir": "N03_engineering", "label": "Producao & Engenharia", "fn": "engineering",
            "focus": "Code, components, infra, CI/CD, architecture, APIs"},
    "N04": {"dir": "N04_knowledge", "label": "Conhecimento & Seguranca", "fn": "knowledge",
            "focus": "Indexacao, RAG, compliance, infosec, documentation"},
    "N05": {"dir": "N05_operations", "label": "Operacoes & Automacao", "fn": "operations",
            "focus": "Deploy, monitoring, pipelines, automation, testing"},
    "N06": {"dir": "N06_commercial", "label": "Comercial & Financeiro", "fn": "commercial",
            "focus": "Pricing, sales funnels, e-commerce, financial reports"},
    "N07": {"dir": "N07_admin", "label": "Administracao & Orquestracao", "fn": "admin",
            "focus": "Strategy, OKRs, cross-nucleus coordination, governance"},
}

LPS = {f"P{i:02d}": d for i, d in enumerate([
    ("P01_knowledge","Knowledge"), ("P02_model","Model"), ("P03_prompt","Prompt"),
    ("P04_tools","Tools"), ("P05_output","Output"), ("P06_schema","Schema"),
    ("P07_evals","Evals"), ("P08_architecture","Architecture"), ("P09_config","Config"),
    ("P10_memory","Memory"), ("P11_feedback","Feedback"), ("P12_orchestration","Orchestration"),
], 1)}

LP_PRIMARY = {
    "N01": ["P01","P07"], "N02": ["P03","P05"], "N03": ["P02","P04","P06"],
    "N04": ["P01","P10"], "N05": ["P04","P12"], "N06": ["P05","P09"],
    "N07": ["P08","P11","P12"],
}

def scaffold(only=None, dry=True):
    count = 0
    for nid, n in NUCLEI.items():
        if only and nid != only:
            continue
        ndir = ROOT / n["dir"]

        # NUCLEUS.md
        nmd = ndir / "NUCLEUS.md"
        primaries = ", ".join(LP_PRIMARY.get(nid, []))
        content = f"""---
id: {nid.lower()}
type: nucleus
label: "{n['label']}"
function: {n['fn']}
created: {date.today().isoformat()}
version: "1.0.0"
---

# {nid}: {n['label']}

## Funcao
{n['focus']}

## LPs Primarios
{primaries}

## Estrutura
12 LPs completos, cada um com _schema.yaml (herda root), templates/, examples/, compiled/.
"""
        if dry:
            print(f"  CREATE {nmd.relative_to(ROOT)}")
        else:
            ndir.mkdir(parents=True, exist_ok=True)
            nmd.write_text(content, encoding="utf-8")
        count += 1

        # 12 LPs
        for lpid, (lpdir_name, lpname) in LPS.items():
            lpdir = ndir / lpdir_name
            is_primary = lpid in LP_PRIMARY.get(nid, [])
            role = "primary" if is_primary else "secondary"

            for sub in ["templates", "examples", "compiled"]:
                d = lpdir / sub
                if dry:
                    print(f"  MKDIR  {d.relative_to(ROOT)}/")
                else:
                    d.mkdir(parents=True, exist_ok=True)
                    (d / ".gitkeep").touch()
                count += 1

            # _schema.yaml
            schema_content = f"""# {nid}/{lpdir_name}/_schema.yaml
# Inherits: ../../{lpdir_name}/_schema.yaml
# Nucleus: {n['label']} | Role: {role}
inherits: "../../{lpdir_name}/_schema.yaml"
nucleus: {nid}
role: {role}
fields_add: {{}}
constraints_override: {{}}
"""
            sp = lpdir / "_schema.yaml"
            if dry:
                print(f"  CREATE {sp.relative_to(ROOT)}")
            else:
                sp.write_text(schema_content, encoding="utf-8")
            count += 1

            # README.md
            readme_content = f"""# {nid}/{lpdir_name} — {n['label']}
**Role**: {role.upper()} | **LP**: {lpid} {lpname}
Domain: {lpname} artifacts for {n['fn']}.
"""
            rp = lpdir / "README.md"
            if dry:
                print(f"  CREATE {rp.relative_to(ROOT)}")
            else:
                rp.write_text(readme_content, encoding="utf-8")
            count += 1

    return count

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--create", action="store_true")
    p.add_argument("--nucleus", type=str)
    a = p.parse_args()
    if not a.dry_run and not a.create:
        a.dry_run = True
    nc = 1 if a.nucleus else len(NUCLEI)
    print(f"CEX Fractal Scaffold: {nc} nuclei x 12 LPs")
    print(f"{'DRY RUN' if a.dry_run else 'CREATING'}...\n")
    c = scaffold(only=a.nucleus, dry=a.dry_run)
    print(f"\nTotal: {c} items {'(dry)' if a.dry_run else 'created'}")

if __name__ == "__main__":
    main()
