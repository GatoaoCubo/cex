---
id: bld_tools_constitutional_rule
kind: knowledge_card
pillar: P11
title: "Constitutional Rule Builder -- Tools"
version: 1.0.0
quality: 6.5
llm_function: CALL
tags: [builder, constitutional_rule, tools]
density_score: 1.0
updated: "2026-04-17"
---

# Constitutional Rule Builder -- Tools

Builder domain: safety alignment. Primary nucleus: N07.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar constitutional_rule artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_constitutional_rule.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `constitutional_rule`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/constitutional-rule-builder/bld_examples_constitutional_rule.md` | Reference examples | F3 INJECT |
| `archetypes/builders/constitutional-rule-builder/bld_schema_constitutional_rule.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing constitutional_rule artifacts
python _tools/cex_retriever.py --query "Absolute agent behavioral constraint, non-overridable"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
