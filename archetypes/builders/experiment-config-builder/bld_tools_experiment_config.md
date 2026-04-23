---
kind: tools
id: bld_tools_experiment_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for experiment_config production
quality: 9.1
title: "Tools Experiment Config"
version: "1.0.0"
author: n03_builder
tags: [experiment_config, builder, tools, P09]
tldr: "Tools for experiment_config: brain_query for duplicate check, cex_compile for validation, cex_score for quality scoring."
domain: "experiment config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_tools_path_config
  - bld_tools_retriever_config
  - bld_tools_runtime_rule
  - bld_tools_feature_flag
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_env_config
  - bld_tools_prompt_version
  - bld_tools_handoff_protocol
  - bld_tools_effort_profile
---

# Tools: experiment-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing experiment_config artifacts for same domain | Phase 1 (check duplicates) | CONDITIONAL |
| cex_compile.py | Compile .md to .yaml after artifact write | Phase 3 | AVAILABLE |
| cex_score.py | Score artifact quality (3-layer rubric) | Phase 3 | AVAILABLE |
| cex_retriever.py | Find similar experiment configs for reference | Phase 1 | AVAILABLE |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, experiment_config kind |
| CEX Examples | P09_config/examples/ | Real experiment_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09_experiment_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, config layer |
| Experiment registry | .cex/experiments/results.tsv | Past experiment outcomes |

## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Compile Command
```bash
python _tools/cex_compile.py P09_config/examples/p09_ec_{name_slug}.md
```

## Score Command
```bash
python _tools/cex_score.py --apply P09_config/examples/p09_ec_{name_slug}.md
```

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `^p09_ec_[a-z][a-z0-9_]+$`,
variants list starts with "control", traffic_split sums to 100, primary_metric is single,
body <= 4096 bytes, quality == null.

## Pipeline Integration
1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata
```yaml
id: bld_tools_experiment_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_tools_experiment_config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_path_config]] | sibling | 0.65 |
| [[bld_tools_retriever_config]] | sibling | 0.63 |
| [[bld_tools_runtime_rule]] | sibling | 0.62 |
| [[bld_tools_feature_flag]] | sibling | 0.62 |
| [[bld_tools_memory_scope]] | sibling | 0.61 |
| [[bld_tools_cli_tool]] | sibling | 0.61 |
| [[bld_tools_env_config]] | sibling | 0.60 |
| [[bld_tools_prompt_version]] | sibling | 0.60 |
| [[bld_tools_handoff_protocol]] | sibling | 0.59 |
| [[bld_tools_effort_profile]] | sibling | 0.59 |
