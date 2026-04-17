---
id: bld_tools_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Tools"
version: 1.0.0
quality: null
llm_function: CALL
tags: [builder, value_object, tools]
---

# Value Object Builder -- Tools

Builder domain: domain model type. Primary nucleus: N03.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar value_object artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_value_object.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `value_object`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/value-object-builder/bld_examples_value_object.md` | Reference examples | F3 INJECT |
| `archetypes/builders/value-object-builder/bld_schema_value_object.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing value_object artifacts
python _tools/cex_retriever.py --query "Immutable typed value defined by attributes alone"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
