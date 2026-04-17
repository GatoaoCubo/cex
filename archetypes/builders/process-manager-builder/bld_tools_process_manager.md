---
id: bld_tools_process_manager
kind: knowledge_card
pillar: P12
title: "Process Manager Builder -- Tools"
version: 1.0.0
quality: 6.5
llm_function: CALL
tags: [builder, process_manager, tools]
density_score: 1.0
updated: "2026-04-17"
---

# Process Manager Builder -- Tools

Builder domain: distributed orchestration. Primary nucleus: N07.

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity (13 ISOs present) | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar process_manager artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_process_manager.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `process_manager`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/process-manager-builder/bld_examples_process_manager.md` | Reference examples | F3 INJECT |
| `archetypes/builders/process-manager-builder/bld_schema_process_manager.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing process_manager artifacts
python _tools/cex_retriever.py --query "Event-driven multi-step process coordinator"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```
