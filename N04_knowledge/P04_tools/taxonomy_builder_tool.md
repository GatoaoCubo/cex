---
id: p04_tool_taxonomy_builder
kind: cli_tool
8f: F5_call
pillar: P04
title: "Taxonomy Builder — Kind Registry & Classification Engine"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: taxonomy-management
quality: 8.9
tags: [tool, n04, taxonomy, classification, kind-registry, tag-normalization]
tldr: "CLI tool to build and maintain taxonomies: kind tree visualization, tag normalization, orphan detection, pillar coverage reports."
density_score: 0.90
related:
  - n04_agent_taxonomy_engineer
  - p03_sp_taxonomy_engineer
  - p01_gl_taxonomy
  - bld_architecture_kind
  - p10_memscope_taxonomy
  - bld_instruction_kind
  - kind-builder
  - p06_schema_taxonomy
  - bld_tools_kind
  - bld_collaboration_kind
---

# Taxonomy Builder Tool

## Purpose

Constructs, maintains, and audits the CEX taxonomy. Turns the flat kind registry (300 kinds) into navigable trees, detects classification anomalies, and enforces tag normalization rules.

## Usage

```bash
# Generate taxonomy tree (visual)
python _tools/taxonomy_builder.py tree --output N04_knowledge/P05_output/taxonomy_tree.md

# Normalize tags across all artifacts
python _tools/taxonomy_builder.py normalize --scope P01_knowledge/ --dry-run

# Detect orphan artifacts (no valid kind or pillar)
python _tools/taxonomy_builder.py orphans --all

# Pillar coverage report
python _tools/taxonomy_builder.py coverage --output N04_knowledge/P05_output/pillar_coverage.md

# Kind distribution (count per kind)
python _tools/taxonomy_builder.py distribution
```

## Taxonomy Tree Format

```
CEX (3647 artifacts)
├── P01 Knowledge (10 kinds, 197 compiled)
│   ├── knowledge_card (123)
│   ├── glossary_entry (0) ← GAP
│   ├── few_shot_example (0) ← GAP
│   ├── context_doc (24)
│   ├── rag_source (4)
│   ├── embedding_config (2)
│   ├── chunk_strategy (2)
│   ├── retriever_config (1)
│   ├── embedder_provider (0) ← GAP
│   └── vector_store (0) ← GAP
├── P02 Orchestration (11 kinds, ...)
│   └── ...
└── P12 Deploy (8 kinds, ...)
    └── ...
```

## Tag Normalization Rules

| Rule | Example | Canonical Form |
|------|---------|---------------|
| Lowercase | `RAG`, `Rag` | `rag` |
| Kebab-case | `knowledge card`, `knowledge_card` | `knowledge-card` |
| Max 3 words | `large-language-model-prompting` | `llm-prompting` |
| Dedup synonyms | `llm` + `large-language-model` | Keep `llm` (shorter) |
| No kind echo | `kind: knowledge_card`, tag: `knowledge-card` | Remove tag |
| No pillar echo | `pillar: P01`, tag: `p01` | Remove tag |

## Orphan Detection

An artifact is orphaned if ANY of:
- `kind` not in `.cex/kinds_meta.json`
- `pillar` doesn't match `P{01-12}`
- No builder exists in `archetypes/builders/{kind}-builder/`
- No sub-agent exists in `.claude/agents/{kind}-builder.md`
- File is in wrong nucleus directory for its kind

## Coverage Metrics

| Metric | Formula | Healthy |
|--------|---------|---------|
| Kind coverage | `kinds_with_artifacts / total_kinds` | >80% |
| Pillar balance | `stdev(artifacts_per_pillar) / mean` | <0.5 |
| Tag entropy | `-Σ p(tag) log p(tag))` | >4.0 (diverse) |
| Orphan rate | `orphans / total_artifacts` | <5% |

## Boundary

One-shot CLI tool. Not a skill (no phases) or daemon (no background persistence).


## 8F Pipeline Function

Primary function: **CALL**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n04_agent_taxonomy_engineer]] | upstream | 0.39 |
| [[p03_sp_taxonomy_engineer]] | upstream | 0.34 |
| [[p01_gl_taxonomy]] | upstream | 0.33 |
| [[bld_architecture_kind]] | downstream | 0.32 |
| [[p10_memscope_taxonomy]] | upstream | 0.30 |
| [[bld_instruction_kind]] | upstream | 0.29 |
| [[kind-builder]] | downstream | 0.28 |
| [[p06_schema_taxonomy]] | downstream | 0.25 |
| [[bld_tools_kind]] | related | 0.25 |
| [[bld_collaboration_kind]] | downstream | 0.25 |
