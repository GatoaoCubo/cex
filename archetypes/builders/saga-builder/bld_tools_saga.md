---
id: bld_tools_saga
kind: knowledge_card
pillar: P12
title: "Saga Builder -- Tools"
version: 1.0.0
quality: null
llm_function: CALL
tags: [builder, saga, tools]
---

# Saga Builder -- Tools

Builder domain: distributed systems. Primary nucleus: N07.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar saga artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_saga.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `saga`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/saga-builder/bld_examples_saga.md` | Reference examples | F3 INJECT |
| `archetypes/builders/saga-builder/bld_schema_saga.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing saga artifacts
python _tools/cex_retriever.py --query "Distributed transaction with compensating actions"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
