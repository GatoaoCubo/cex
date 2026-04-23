---
kind: tools
id: bld_tools_validation_schema
pillar: P04
llm_function: CALL
purpose: Tools available for validation_schema production
quality: 9.1
title: "Tools Validation Schema"
version: "1.0.0"
author: n03_builder
tags: [validation_schema, builder, examples]
tldr: "Golden and anti-examples for validation schema construction, demonstrating ideal structure and common pitfalls."
domain: "validation schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_input_schema
  - bld_tools_response_format
  - bld_tools_golden_test
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_unit_eval
  - bld_tools_cli_tool
  - bld_tools_validator
  - bld_tools_interface
  - bld_tools_scoring_rubric
---

# Tools: validation-schema-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing validation_schemas | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P06_schema/_schema.yaml | Field definitions for validation_schema |
| CEX Examples | P06_schema/examples/ | Existing schema artifacts |
| Target schemas | {lp_dir}/_schema.yaml | Field definitions of target kinds |
| SEED_BANK | archetypes/SEED_BANK.yaml | P06_output_schema seeds |
| validate_kc.py | _tools/validate_kc.py | Reference implementation of KC validation |
| JSON Schema spec | https://json-schema.org | Industry standard reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
1. [ ] YAML parses
2. [ ] id matches p06_vs_ prefix
3. [ ] fields_count >= 1
4. [ ] on_failure in [reject, warn, auto_fix]
5. [ ] format in [json, yaml]
6. [ ] target_kind non-empty

## Metadata

```yaml
id: bld_tools_validation_schema
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-validation-schema.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_input_schema]] | sibling | 0.64 |
| [[bld_tools_response_format]] | sibling | 0.59 |
| [[bld_tools_golden_test]] | sibling | 0.57 |
| [[bld_tools_retriever_config]] | sibling | 0.56 |
| [[bld_tools_memory_scope]] | sibling | 0.56 |
| [[bld_tools_unit_eval]] | sibling | 0.56 |
| [[bld_tools_cli_tool]] | sibling | 0.56 |
| [[bld_tools_validator]] | sibling | 0.56 |
| [[bld_tools_interface]] | sibling | 0.55 |
| [[bld_tools_scoring_rubric]] | sibling | 0.55 |
