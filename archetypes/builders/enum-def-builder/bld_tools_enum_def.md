---
kind: tools
id: bld_tools_enum_def
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for enum_def production
quality: 9.0
title: "Tools Enum Def"
version: "1.0.0"
author: n03_builder
tags: [enum_def, builder, examples]
tldr: "Golden and anti-examples for enum def construction, demonstrating ideal structure and common pitfalls."
domain: "enum def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_input_schema
  - bld_tools_validation_schema
  - bld_tools_cli_tool
  - bld_tools_retriever_config
  - bld_tools_runtime_rule
  - bld_tools_memory_scope
  - bld_tools_function_def
  - bld_tools_validator
  - bld_tools_prompt_version
  - bld_tools_path_config
---

# Tools: enum-def-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing enum_def artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P06_schema/_schema.yaml | Field definitions, enum_def kind |
| CEX Examples | P06_schema/examples/ | Real enum_def artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P06_enum_def |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |

## Framework Reference Targets
| Framework | Use case | Version |
|-----------|----------|---------|
| JSON Schema | Universal schema validation | draft-07 / 2020-12 |
| Pydantic | Python data models and API validation | v2.x |
| Zod | TypeScript runtime validation | v3.x |
| GraphQL | API schema definition | June 2018 spec |
| TypeScript | Static type checking | 5.x |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `^p06_enum_[a-z][a-z0-9_]+$`,
values list >= 2 entries, values list matches ## Values body section names, deprecated
subset of values, default in values, body <= 1024 bytes, quality == null, extensible declared.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_input_schema]] | sibling | 0.61 |
| [[bld_tools_validation_schema]] | sibling | 0.59 |
| [[bld_tools_cli_tool]] | sibling | 0.59 |
| [[bld_tools_retriever_config]] | sibling | 0.59 |
| [[bld_tools_runtime_rule]] | sibling | 0.58 |
| [[bld_tools_memory_scope]] | sibling | 0.58 |
| [[bld_tools_function_def]] | sibling | 0.58 |
| [[bld_tools_validator]] | sibling | 0.57 |
| [[bld_tools_prompt_version]] | sibling | 0.57 |
| [[bld_tools_path_config]] | sibling | 0.57 |
