---
id: bld_tools_event_stream
kind: knowledge_card
pillar: P04
title: "Event Stream Builder -- Tools"
version: 1.0.0
quality: 6.5
llm_function: CALL
tags: [builder, event_stream, tools]
density_score: 1.0
updated: "2026-04-17"
---

# Event Stream Builder -- Tools

Builder domain: streaming infrastructure. Primary nucleus: N05.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar event_stream artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_event_stream.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `event_stream`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/event-stream-builder/bld_examples_event_stream.md` | Reference examples | F3 INJECT |
| `archetypes/builders/event-stream-builder/bld_schema_event_stream.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing event_stream artifacts
python _tools/cex_retriever.py --query "Real-time ordered event sequence configuration"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
