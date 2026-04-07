---
kind: tools
id: bld_tools_builder
pillar: P04
llm_function: CALL
purpose: Tools, APIs, and data sources for the meta-builder
quality: 9.1
title: "Tools Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Tools: _builder-builder

## CEX Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_schema_hydrate.py | Hydrate universal fields | After ISO generation |
| cex_compile.py | .md → .yaml compilation | After save |
| cex_doctor.py | Builder health check (13 builder specs, sizes) | After build |
| cex_hooks.py | Pre/post validation | Before commit |
| cex_materialize.py | Builder ISOs → sub-agent .md | After builder complete |
| cex_score.py | 5D quality scoring | Peer review |
| signal_writer.py | Inter-nucleus signals | After complete |

## Data Sources
| Source | Path | Data |
|--------|------|------|
| Meta-templates (13) | archetypes/builders/_builder-builder/bld_meta_*.md | ISO templates |
| TAXONOMY_LAYERS | archetypes/TAXONOMY_LAYERS.yaml | Kind→pillar mapping |
| KIND_META | .cex/kinds_meta.json | Kind registry |
| bld_norms | archetypes/builders/bld_norms.md | 23 validation rules |
| SEED_BANK | archetypes/SEED_BANK.yaml | Builder seeds |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-builder.md
```
