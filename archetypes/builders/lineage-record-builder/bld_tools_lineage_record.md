---
id: bld_tools_lineage_record
kind: knowledge_card
pillar: P01
title: "Lineage Record Builder -- Tools"
version: 1.0.0
quality: null
llm_function: CALL
tags: [builder, lineage_record, tools]
---

# Lineage Record Builder -- Tools

Builder domain: data lineage. Primary nucleus: N04.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar lineage_record artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_lineage_record.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `lineage_record`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/lineage-record-builder/bld_examples_lineage_record.md` | Reference examples | F3 INJECT |
| `archetypes/builders/lineage-record-builder/bld_schema_lineage_record.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing lineage_record artifacts
python _tools/cex_retriever.py --query "Provenance chain of a knowledge artifact derivation"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
