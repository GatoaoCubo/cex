---
id: bld_tools_alert_rule
kind: knowledge_card
pillar: P09
title: "Alert Rule Builder -- Tools"
version: 1.0.0
quality: null
llm_function: CALL
tags: [builder, alert_rule, tools]
---

# Alert Rule Builder -- Tools

Builder domain: monitoring observability. Primary nucleus: N05.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar alert_rule artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_alert_rule.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `alert_rule`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/alert-rule-builder/bld_examples_alert_rule.md` | Reference examples | F3 INJECT |
| `archetypes/builders/alert-rule-builder/bld_schema_alert_rule.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing alert_rule artifacts
python _tools/cex_retriever.py --query "Observable threshold condition triggering notification"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
