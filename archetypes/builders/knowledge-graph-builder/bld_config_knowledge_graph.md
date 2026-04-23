---
kind: config
id: bld_config_knowledge_graph
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints for knowledge_graph
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 30
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.2
title: "Config: knowledge_graph production rules"
version: "1.0.0"
author: n03_builder
tags: [knowledge_graph, builder, config, P09]
tldr: "Naming, paths, size limits, and operational constraints for knowledge_graph artifact production."
domain: "knowledge graph construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_instruction_knowledge_graph
  - p10_lr_knowledge_graph_builder
  - bld_knowledge_card_knowledge_graph
  - p11_qg_knowledge_graph
  - bld_schema_knowledge_graph
  - p03_sp_knowledge_graph_builder
  - p01_kc_knowledge_graph
  - knowledge-graph-builder
  - bld_examples_knowledge_graph
  - bld_collaboration_knowledge_graph
---

# Config: knowledge_graph Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_kg_{name}.md` | `p01_kg_competitive_intel.md` |
| Compiled YAML | `p01_kg_{name}.yaml` | `p01_kg_competitive_intel.yaml` |
| Builder directory | kebab-case | `knowledge-graph-builder/` |
| Frontmatter fields | snake_case | `entity_types`, `relation_types`, `storage_backend` |
| Name slug | snake_case, lowercase, no hyphens | `competitive_intel`, `biomedical`, `legal_contracts` |
| Entity type names | PascalCase | `Organization`, `Product`, `Technology` |
| Relation type names | snake_case | `acquired`, `competes_with`, `developed_by` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths

1. Output: `P01_knowledge/examples/p01_kg_{name}.md`
2. Compiled: `P01_knowledge/compiled/p01_kg_{name}.yaml`

## Size Limits (aligned with SCHEMA)

1. Body: max 8192 bytes
2. Total (frontmatter + body): ~10000 bytes
3. Density: >= 0.85 (no filler)

## Entity Type Constraints

| Constraint | Value | Rationale |
|-----------|-------|-----------|
| Min entity types | 1 | HARD gate H07 |
| Recommended entity types | 3-10 | Fewer = precision, more = noise |
| Max entity types | 20 | Above 20, extraction quality collapses |
| Naming convention | PascalCase | Matches graph database node label conventions |
| Extraction hints | required | Enables schema-constrained extraction |
| Example instances | required | 2-3 per type minimum |

## Relation Type Constraints

| Constraint | Value | Rationale |
|-----------|-------|-----------|
| Min relation types | 1 | HARD gate H08 |
| Recommended relation types | 5-15 | Sufficient coverage without over-specification |
| Source type required | YES | HARD gate H09 consistency check |
| Target type required | YES | HARD gate H09 consistency check |
| Directionality required | YES | Traversal semantics depend on this |
| Naming convention | snake_case | Consistent with relation predicate conventions |

## Storage Backend Enum

| Value | When to use | Scale |
|-------|-------------|-------|
| in_memory | Prototyping, development, testing | < 10k nodes |
| json | Simple persistence, read-heavy | < 50k nodes |
| falkordb | Production, high throughput, Redis ecosystem | < 1M nodes |
| neo4j | Full production, complex Cypher, large graphs | Unlimited |

## Traversal Strategy Enum

| Value | Query types answered | Use when |
|-------|---------------------|---------|
| local | Entity-centric: "what do I know about X?" | Entity lookup, direct relation queries |
| global | Theme-centric: "what are the main patterns?" | Corpus synthesis, trend analysis |
| hybrid | Both local and global | Default recommendation |

## Dedup Strategy Enum

| Value | Method | Threshold | Cost |
|-------|--------|-----------|------|
| exact | String equality | N/A | Zero |
| fuzzy | Edit distance + embedding similarity | 0.85 default | Low |
| llm | LLM judgment on ambiguous pairs | N/A | High |

## Metadata

```yaml
id: bld_config_knowledge_graph
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_config_knowledge_graph.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_knowledge_graph]] | upstream | 0.46 |
| [[p10_lr_knowledge_graph_builder]] | downstream | 0.45 |
| [[bld_knowledge_card_knowledge_graph]] | upstream | 0.45 |
| [[p11_qg_knowledge_graph]] | downstream | 0.44 |
| [[bld_schema_knowledge_graph]] | upstream | 0.42 |
| [[p03_sp_knowledge_graph_builder]] | upstream | 0.40 |
| [[p01_kc_knowledge_graph]] | upstream | 0.38 |
| [[knowledge-graph-builder]] | upstream | 0.37 |
| [[bld_examples_knowledge_graph]] | upstream | 0.34 |
| [[bld_collaboration_knowledge_graph]] | downstream | 0.32 |
