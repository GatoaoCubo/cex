---
id: p06_schema_taxonomy
kind: schema
8f: F1_constrain
pillar: P06
title: "Taxonomy Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.0
tags: [schema, n04, taxonomy, classification, kind, pillar, domain]
tldr: "Classification rules: kind (from kinds_meta.json) × pillar (P01-P12) × domain. Decision tree for ambiguous cases."
density_score: 0.93
related:
  - p08_pat_nucleus_fractal
  - cex_llm_vocabulary_whitepaper
  - kc_llm_vocabulary_atlas
  - bld_architecture_agent
  - bld_knowledge_card_kind
  - p01_kc_agent
  - bld_architecture_memory_architecture
  - bld_architecture_dataset_card
  - bld_architecture_system_prompt
  - p01_kc_workflow_orchestration
---

# Taxonomy Contract

## Three Axes

| Axis | Source of Truth | Count |
|------|----------------|-------|
| Kind | .cex/kinds_meta.json | 105 |
| Pillar | P01-P12 directories | 12 |
| Domain | KC domain field | Open (validated per nucleus) |

## Classification Decision Tree
```
1. What IS it? → kind (agent, workflow, schema, knowledge_card, ...)
2. WHERE does it live? → pillar (P01=knowledge, P02=identity, ...)
3. WHAT ABOUT? → domain (llm_patterns, operations, brand, ...)
```

## Pillar Quick Reference

| Pillar | Name | Kinds |
|--------|------|-------|
| P01 | Knowledge | knowledge_card, rag_source, embedding_config |
| P02 | Identity | agent, persona |
| P03 | Prompts | system_prompt, prompt_template |
| P04 | Tools | cli_tool, mcp_server, skill |
| P06 | Constraints | schema, constraint_spec |
| P07 | Quality | scoring_rubric |
| P08 | Patterns | pattern, axiom |
| P11 | Feedback | quality_gate |
| P12 | Orchestration | workflow, dag, dispatch_rule |

## Ambiguity Rules
- If it teaches HOW → knowledge_card (P01)
- If it validates WHAT → quality_gate (P11)
- If it sequences STEPS → workflow (P12)
- If it defines WHO → agent (P02)
- If it constrains FORMAT → schema (P06)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_pat_nucleus_fractal]] | downstream | 0.32 |
| [[cex_llm_vocabulary_whitepaper]] | upstream | 0.29 |
| [[kc_llm_vocabulary_atlas]] | upstream | 0.26 |
| [[bld_architecture_agent]] | downstream | 0.25 |
| [[bld_knowledge_card_kind]] | upstream | 0.24 |
| [[p01_kc_agent]] | upstream | 0.24 |
| [[bld_architecture_memory_architecture]] | downstream | 0.24 |
| [[bld_architecture_dataset_card]] | downstream | 0.23 |
| [[bld_architecture_system_prompt]] | downstream | 0.23 |
| [[p01_kc_workflow_orchestration]] | upstream | 0.23 |
