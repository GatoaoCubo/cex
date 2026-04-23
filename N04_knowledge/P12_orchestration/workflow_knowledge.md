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
related:
  - p12_wf_knowledge_pipeline
  - p03_sp_knowledge_nucleus
  - p02_card_knowledge
  - n04_agent_knowledge
  - p06_schema_export_format
  - p01_kc_knowledge_card
  - p11_qg_knowledge
  - agent_card_n04
  - bld_collaboration_knowledge_card
  - knowledge-index-builder
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_knowledge_pipeline]] | sibling | 0.40 |
| [[p03_sp_knowledge_nucleus]] | upstream | 0.35 |
| [[p02_card_knowledge]] | upstream | 0.34 |
| [[n04_agent_knowledge]] | upstream | 0.34 |
| [[p06_schema_export_format]] | upstream | 0.33 |
| [[p01_kc_knowledge_card]] | upstream | 0.25 |
| [[p11_qg_knowledge]] | upstream | 0.25 |
| [[agent_card_n04]] | upstream | 0.24 |
| [[bld_collaboration_knowledge_card]] | related | 0.23 |
| [[knowledge-index-builder]] | upstream | 0.23 |
