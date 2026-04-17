---
id: bld_tools_aggregate_root
kind: knowledge_card
pillar: P06
title: "Aggregate Root Builder -- Tools"
version: 1.0.0
quality: 6.5
llm_function: CALL
tags: [builder, aggregate_root, tools]
density_score: 1.0
updated: "2026-04-17"
---

# Aggregate Root Builder -- Tools

Builder domain: domain model entity. Primary nucleus: N03.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar aggregate_root artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_aggregate_root.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `aggregate_root`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/aggregate-root-builder/bld_examples_aggregate_root.md` | Reference examples | F3 INJECT |
| `archetypes/builders/aggregate-root-builder/bld_schema_aggregate_root.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing aggregate_root artifacts
python _tools/cex_retriever.py --query "DDD entry point entity that enforces invariants"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
