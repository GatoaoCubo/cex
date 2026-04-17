---
id: bld_tools_canary_config
kind: knowledge_card
pillar: P09
title: "Canary Config Builder -- Tools"
version: 1.0.0
quality: null
llm_function: CALL
tags: [builder, canary_config, tools]
---

# Canary Config Builder -- Tools

Builder domain: deployment resilience. Primary nucleus: N05.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar canary_config artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_canary_config.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `canary_config`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/canary-config-builder/bld_examples_canary_config.md` | Reference examples | F3 INJECT |
| `archetypes/builders/canary-config-builder/bld_schema_canary_config.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing canary_config artifacts
python _tools/cex_retriever.py --query "Gradual traffic rollout with automatic rollback"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
