---
kind: tools
id: bld_tools_compression_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for compression_config production
quality: 9.0
title: "Tools Compression Config"
version: "1.0.0"
author: n03_builder
tags: [compression_config, builder, examples]
tldr: "Golden and anti-examples for compression config construction, demonstrating ideal structure and common pitfalls."
domain: "compression config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_memory_scope
  - bld_tools_retriever_config
  - bld_tools_cli_tool
  - bld_tools_path_config
  - bld_tools_prompt_version
  - bld_tools_chunk_strategy
  - bld_tools_runtime_rule
  - bld_tools_output_validator
  - bld_tools_handoff_protocol
  - bld_tools_function_def
---

# Tools: compression-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing compression_config artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| cex_token_budget.py | Read token budget to calibrate trigger_ratio and max_summary_tokens | Phase 1 (understand limits) | AVAILABLE |
| cex_memory_types.py | List memory types to define preserve_types and decay_weights | Phase 1 (type catalog) | AVAILABLE |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions, compression_config kind |
| CEX Examples | P10_memory/examples/ | Real compression_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P10_compression_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, memory layer |
| Wire 6 | P04_skill/library/p04_skill_compact.md | Compact skill that consumes compression_config |
| Token Budget Tool | _tools/cex_token_budget.py | Runtime token counting and budget allocation |
| Memory Types | _tools/cex_memory_types.py | Memory type taxonomy (correction/preference/convention/context) |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, strategy enum valid,
trigger_ratio in range, preserve_types includes system_prompt, decay_weights defined,
body <= 4096 bytes, quality == null.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_memory_scope]] | sibling | 0.61 |
| [[bld_tools_retriever_config]] | sibling | 0.59 |
| [[bld_tools_cli_tool]] | sibling | 0.58 |
| [[bld_tools_path_config]] | sibling | 0.57 |
| [[bld_tools_prompt_version]] | sibling | 0.56 |
| [[bld_tools_chunk_strategy]] | sibling | 0.56 |
| [[bld_tools_runtime_rule]] | sibling | 0.56 |
| [[bld_tools_output_validator]] | sibling | 0.55 |
| [[bld_tools_handoff_protocol]] | sibling | 0.55 |
| [[bld_tools_function_def]] | sibling | 0.55 |
