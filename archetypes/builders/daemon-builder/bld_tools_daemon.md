---
kind: tools
id: bld_tools_daemon
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for daemon production
quality: 9.1
title: "Tools Daemon"
version: "1.0.0"
author: n03_builder
tags: [daemon, builder, examples]
tldr: "Golden and anti-examples for daemon construction, demonstrating ideal structure and common pitfalls."
domain: "daemon construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_cli_tool
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_prompt_version
  - bld_tools_path_config
  - bld_tools_handoff_protocol
  - bld_tools_output_validator
  - bld_tools_chunk_strategy
  - bld_tools_runtime_rule
  - bld_tools_client
---

# Tools: daemon-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing daemon artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, daemon kind |
| CEX Examples | P04_tools/examples/ | Real daemon artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_daemon |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| systemd docs | freedesktop.org/software/systemd | Unit file conventions |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, schedule is concrete,
body <= 1024 bytes, quality == null, signal_handling includes SIGTERM.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_daemon
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-daemon.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_cli_tool]] | sibling | 0.74 |
| [[bld_tools_retriever_config]] | sibling | 0.73 |
| [[bld_tools_memory_scope]] | sibling | 0.73 |
| [[bld_tools_prompt_version]] | sibling | 0.71 |
| [[bld_tools_path_config]] | sibling | 0.70 |
| [[bld_tools_handoff_protocol]] | sibling | 0.70 |
| [[bld_tools_output_validator]] | sibling | 0.70 |
| [[bld_tools_chunk_strategy]] | sibling | 0.70 |
| [[bld_tools_runtime_rule]] | sibling | 0.69 |
| [[bld_tools_client]] | sibling | 0.69 |
