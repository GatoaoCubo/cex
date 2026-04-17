---
kind: tools
id: bld_tools_context_map
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for context_map production
quality: null
title: "Tools Context Map"
version: "1.0.0"
author: n03_builder
tags: [context_map, builder, tools]
tldr: "Tools: cex_compile, cex_doctor, cex_score. Data sources: DDD pattern KC, bounded context artifacts, system descriptions."
domain: "context map construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Tools: context-map-builder

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar context_map artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_context_map.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `context_map`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/context-map-builder/bld_examples_context_map.md` | Reference examples | F3 INJECT |
| `archetypes/builders/context-map-builder/bld_schema_context_map.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing context_map artifacts
python _tools/cex_retriever.py --query "context map bounded context DDD relationships"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```

## External References

| Reference | Purpose |
|-----------|---------|
| Evans DDD (2003) Chapter 14 | Canonical context mapping patterns |
| Vernon IDDD (2013) Chapter 3 | Extended pattern catalog |
| context-mapping.io | Visual context mapping tools |
| github.com/ddd-crew/context-mapping | DDD Crew context mapping cards |
| mermaid.js.org/syntax/flowchart | Mermaid diagram syntax for context maps |

## Validation Commands

| Command | Purpose | When |
|---------|---------|------|
| `python _tools/cex_compile.py {path}` | Compile .md to .yaml | F8 |
| `python _tools/cex_doctor.py` | Check builder health | F7 |
| `python _tools/cex_score.py {path} --apply` | Peer review + apply score | F7 |
| `python _tools/cex_retriever.py --query "context map DDD"` | Find similar artifacts | F5 |
| `git add {path} && git commit` | Version artifact | F8 |
| `python _tools/cex_index.py` | Update artifact index | F8 |
| `python _tools/cex_retriever.py --similar {path}` | Find duplicate BCs | F5 |
