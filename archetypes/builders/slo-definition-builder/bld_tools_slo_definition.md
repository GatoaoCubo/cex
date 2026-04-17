---
id: bld_tools_slo_definition
kind: knowledge_card
pillar: P09
title: "Slo Definition Builder -- Tools"
version: 1.0.0
quality: null
llm_function: CALL
tags: [builder, slo_definition, tools]
---

# Slo Definition Builder -- Tools

Builder domain: SRE reliability. Primary nucleus: N05.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar slo_definition artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_slo_definition.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `slo_definition`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/slo-definition-builder/bld_examples_slo_definition.md` | Reference examples | F3 INJECT |
| `archetypes/builders/slo-definition-builder/bld_schema_slo_definition.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing slo_definition artifacts
python _tools/cex_retriever.py --query "Measurable service level objective with error budget"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
