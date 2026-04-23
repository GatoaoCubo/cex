---
kind: tools
id: bld_tools_env_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for env_config production
quality: 9.1
title: "Tools Env Config"
version: "1.0.0"
author: n03_builder
tags: [env_config, builder, examples]
tldr: "Golden and anti-examples for env config construction, demonstrating ideal structure and common pitfalls."
domain: "env config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_path_config
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_runtime_rule
  - bld_tools_prompt_version
  - bld_tools_feature_flag
  - bld_tools_handoff_protocol
  - bld_tools_output_validator
  - bld_tools_chunk_strategy
---

# Tools: env-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing env_config artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, env_config kind |
| CEX Examples | P09_config/examples/ | Real env_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09_env_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| .env files | Project .env, .env.example | Existing variable definitions |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, variables list matches catalog,
body <= 4096 bytes, quality == null, no actual secret values in artifact.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_env_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-env-config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_path_config]] | sibling | 0.73 |
| [[bld_tools_retriever_config]] | sibling | 0.73 |
| [[bld_tools_memory_scope]] | sibling | 0.71 |
| [[bld_tools_cli_tool]] | sibling | 0.71 |
| [[bld_tools_runtime_rule]] | sibling | 0.71 |
| [[bld_tools_prompt_version]] | sibling | 0.69 |
| [[bld_tools_feature_flag]] | sibling | 0.69 |
| [[bld_tools_handoff_protocol]] | sibling | 0.68 |
| [[bld_tools_output_validator]] | sibling | 0.68 |
| [[bld_tools_chunk_strategy]] | sibling | 0.68 |
