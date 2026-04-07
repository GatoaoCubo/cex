---
kind: tools
id: bld_tools_feature_flag
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for feature_flag production
quality: 9.1
title: "Tools Feature Flag"
version: "1.0.0"
author: n03_builder
tags: [feature_flag, builder, examples]
tldr: "Golden and anti-examples for feature flag construction, demonstrating ideal structure and common pitfalls."
domain: "feature flag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Tools: feature-flag-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing feature_flag artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, feature_flag kind |
| CEX Examples | P09_config/examples/ | Real feature_flag artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09 types |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, default_state enum, rollout
integer 0-100, category enum, body <= 1536 bytes, quality == null.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_feature_flag
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-feature-flag.md
```
