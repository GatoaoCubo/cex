---
kind: tools
id: bld_tools_input_schema
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for input_schema production
quality: 9.1
title: "Tools Input Schema"
version: "1.0.0"
author: n03_builder
tags: [input_schema, builder, examples]
tldr: "Golden and anti-examples for input schema construction, demonstrating ideal structure and common pitfalls."
domain: "input schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_validator
  - bld_tools_validation_schema
  - bld_tools_interface
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_constraint_spec
  - bld_tools_prompt_version
  - bld_tools_function_def
  - bld_tools_path_config
---

# Tools: input-schema-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing input_schemas in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P06_schema/_schema.yaml | Field definitions for input_schema |
| CEX Examples | P06_schema/examples/ | Real input_schema artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P06_input_schema seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| JSON Schema spec | https://json-schema.org/ | Type/constraint patterns |
| Pydantic docs | https://docs.pydantic.dev/ | Coercion/default patterns |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet for input_schemas.
Manually check each QUALITY_GATES.md gate against produced artifact:
1. [ ] YAML parses without error
2. [ ] id matches p06_is_ prefix
3. [ ] fields list is non-empty
4. [ ] each field has name and type
5. [ ] quality is null
6. [ ] optional fields have defaults

## Metadata

```yaml
id: bld_tools_input_schema
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-input-schema.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_validator]] | sibling | 0.67 |
| [[bld_tools_validation_schema]] | sibling | 0.66 |
| [[bld_tools_interface]] | sibling | 0.63 |
| [[bld_tools_retriever_config]] | sibling | 0.62 |
| [[bld_tools_memory_scope]] | sibling | 0.62 |
| [[bld_tools_cli_tool]] | sibling | 0.61 |
| [[bld_tools_constraint_spec]] | sibling | 0.61 |
| [[bld_tools_prompt_version]] | sibling | 0.60 |
| [[bld_tools_function_def]] | sibling | 0.59 |
| [[bld_tools_path_config]] | sibling | 0.59 |
