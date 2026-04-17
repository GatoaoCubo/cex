---
id: bld_tools_data_contract
kind: knowledge_card
pillar: P06
title: "Data Contract Builder -- Tools"
version: 1.0.0
quality: null
llm_function: CALL
tags: [builder, data_contract, tools]
---

# Data Contract Builder -- Tools

Builder domain: data governance. Primary nucleus: N03.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar data_contract artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_data_contract.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `data_contract`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/data-contract-builder/bld_examples_data_contract.md` | Reference examples | F3 INJECT |
| `archetypes/builders/data-contract-builder/bld_schema_data_contract.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing data_contract artifacts
python _tools/cex_retriever.py --query "Schema agreement between producer and consumer"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
