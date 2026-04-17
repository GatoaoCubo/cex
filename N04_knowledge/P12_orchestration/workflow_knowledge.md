---
id: p12_wf_knowledge
kind: workflow
pillar: P12
title: "N04 Workflow — Knowledge Lifecycle Pipeline"
version: 4.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
step_count: 8
quality: 9.0
tags: [workflow, n04, knowledge, lifecycle, pipeline, taxonomy]
tldr: "8-step KC lifecycle: ingest→classify→distill→structure→validate→index→export→monitor."
density_score: 0.93
---

# N04 Workflow — Knowledge Lifecycle

## Pipeline
```
INGEST → CLASSIFY → DISTILL → STRUCTURE → VALIDATE → INDEX → EXPORT → MONITOR
```

| Step | Action | Input | Output | Tool |
|------|--------|-------|--------|------|
| 1 | Ingest raw material | Docs, research, code, conversations | Raw text | markitdown MCP, manual |
| 2 | Classify | Raw text | kind × pillar × domain | kinds_meta.json, taxonomy_contract.md |
| 3 | Distill | Classified raw | Signal extracted, noise removed | kc_knowledge_distillation pattern |
| 4 | Structure | Distilled content | KC with frontmatter + sections | kc_structure_contract.md |
| 5 | Validate | Structured KC | Compile pass + density check | cex_compile.py, density >= 0.85 |
| 6 | Index | Validated KC | Search index updated | cex_index.py |
| 7 | Export | Indexed KC | YAML + JSONL + SQL | export_format_contract.md |
| 8 | Monitor | All KCs | Freshness alerts, gap reports | freshness_contract.md |

## Export Formats

| Format | Purpose | Consumer |
|--------|---------|----------|
| .yaml | CEX compiled artifact | All nuclei (compose_prompt) |
| .jsonl | Fine-tuning dataset | External LLM training |
| SQL | Database persistence | Supabase, vector search |
| .csv | ML feature datasets | Analytics, dashboards |

## Usage Guidelines

**When to use:**
- Converting messy research into structured knowledge cards
- Building systematic knowledge base for team/organization
- Preparing training data for fine-tuning models
- Creating searchable documentation from scattered sources

**Anti-patterns:**
- Skipping classification step (leads to wrong pillar placement)
- Accepting density < 0.85 (low information content)
- Manual indexing instead of using cex_index.py
- Creating KCs without monitoring freshness (stale knowledge)