---
id: p02_card_knowledge
kind: agent_card
8f: F2_become
pillar: P02
title: "N04 Knowledge Engineer — Agent Card"
version: 4.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.0
tags: [agent_card, n04, knowledge, engineer, routing, database]
tldr: "Knowledge Engineer routing card — 12 capabilities, triple-export (CEX+fine-tune+SQL), inter-nucleus knowledge flows."
density_score: 0.93
related:
  - n04_agent_knowledge
  - p03_sp_knowledge_nucleus
  - agent_card_n04
  - p12_mission_supabase_data_layer
  - p12_wf_knowledge
  - spec_n01_n04_verticalization
  - spec_n06_brand_verticalization
  - n04_dr_knowledge
  - bld_collaboration_supabase_data_layer
  - bld_collaboration_knowledge_card
---

# N04 Knowledge Engineer — Agent Card

## Routing
- **Priority**: 7
- **Keywords**: knowledge, KC, taxonomy, classify, index, embed, database, supabase, fine-tune, ML, dataset, export, gap, freshness, stale, RAG, search
- **Dispatch**: `bash _spawn/dispatch.sh solo n04 "task"`

## Provider
| Mode | Provider | When |
|------|----------|------|
| Structuring | Claude | Reasoning, classification, distillation |
| Bulk ingestion | Gemini | Large document processing |
| Fallback | Either | Rate limit on primary |

## Triple-Export Architecture
```
KC (.md) → cex_compile.py → .yaml (CEX internal)
KC (.md) → export_finetune → .jsonl (fine-tuning)
KC (.md) → export_sql → SQL INSERT (Supabase)
```

## Inter-Nucleus Knowledge Flows

| From | To N04 | What |
|------|--------|------|
| N01 | Research results | "Distill into KCs" |
| N03 | New builder patterns | "Document as pattern KC" |
| N06 | Brand knowledge | "Index brand archetypes" |
| N07 | Gap detection | "Fill missing KCs" |

| From N04 | To | What |
|----------|-----|------|
| Kind KC | N03 | Builder knowledge injection |
| Domain KC | N01 | Research context |
| Brand KC | N06 | Brand knowledge base |
| Fine-tune set | External | Model training data |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n04_agent_knowledge]] | upstream | 0.38 |
| [[p03_sp_knowledge_nucleus]] | downstream | 0.37 |
| [[agent_card_n04]] | upstream | 0.37 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.32 |
| [[p12_wf_knowledge]] | downstream | 0.32 |
| [[spec_n01_n04_verticalization]] | downstream | 0.32 |
| [[spec_n06_brand_verticalization]] | downstream | 0.30 |
| [[n04_dr_knowledge]] | related | 0.29 |
| [[bld_collaboration_supabase_data_layer]] | downstream | 0.29 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.29 |
