---
kind: tools
id: bld_tools_response_format
pillar: P04
llm_function: CALL
purpose: Tools available for response_format production
quality: 9.1
title: "Tools Response Format"
version: "1.0.0"
author: n03_builder
tags: [response_format, builder, examples]
tldr: "Golden and anti-examples for response format construction, demonstrating ideal structure and common pitfalls."
domain: "response format construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_validation_schema
  - bld_tools_function_def
  - bld_tools_input_schema
  - bld_tools_golden_test
  - bld_tools_benchmark
  - bld_tools_cli_tool
  - bld_tools_retriever_config
  - bld_tools_mcp_server
  - bld_tools_output_validator
  - bld_tools_memory_scope
---

# Tools: response-format-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing response_formats | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P05_output/_schema.yaml | Field definitions for response_format |
| CEX Examples | P05_output/examples/ | Existing format artifacts |
| Target schemas | {lp_dir}/_schema.yaml | Output requirements of target kinds |
| SEED_BANK | archetypes/SEED_BANK.yaml | P05_output_schema seeds |
| OpenAI docs | https://platform.openai.com/docs | Structured output patterns |
| Anthropic docs | https://docs.anthropic.com | Tool use output patterns |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
1. [ ] YAML parses
2. [ ] id matches p05_rf_ prefix
3. [ ] sections_count >= 1
4. [ ] format_type in valid enum
5. [ ] injection_point in valid enum
6. [ ] Example Output section present

## Metadata

```yaml
id: bld_tools_response_format
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-response-format.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_validation_schema]] | sibling | 0.61 |
| [[bld_tools_function_def]] | sibling | 0.59 |
| [[bld_tools_input_schema]] | sibling | 0.58 |
| [[bld_tools_golden_test]] | sibling | 0.57 |
| [[bld_tools_benchmark]] | sibling | 0.57 |
| [[bld_tools_cli_tool]] | sibling | 0.56 |
| [[bld_tools_retriever_config]] | sibling | 0.56 |
| [[bld_tools_mcp_server]] | sibling | 0.56 |
| [[bld_tools_output_validator]] | sibling | 0.55 |
| [[bld_tools_memory_scope]] | sibling | 0.55 |
