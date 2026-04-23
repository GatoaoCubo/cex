---
kind: tools
id: bld_tools_unit_eval
pillar: P04
llm_function: CALL
purpose: Tools available for unit_eval production
quality: 9.0
title: "Tools Unit Eval"
version: "1.0.0"
author: n03_builder
tags: [unit_eval, builder, examples]
tldr: "Golden and anti-examples for unit eval construction, demonstrating ideal structure and common pitfalls."
domain: "unit eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_golden_test
  - bld_tools_e2e_eval
  - bld_tools_smoke_eval
  - bld_tools_validation_schema
  - bld_tools_scoring_rubric
  - bld_tools_retriever_config
  - bld_tools_cli_tool
  - bld_tools_memory_scope
  - bld_tools_lifecycle_rule
  - bld_tools_input_schema
---

# Tools: unit-eval-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing unit_evals | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions for unit_eval |
| CEX Examples | P07_evals/examples/ | Existing unit_eval artifacts |
| Builder QG files | archetypes/builders/*/QUALITY_GATES.md | Gate refs for assertions |
| Target builders | archetypes/builders/{target}/ | Target schema and gates |
| SEED_BANK | archetypes/SEED_BANK.yaml | P07_unit_eval seeds |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Manually check each QUALITY_GATES.md gate against produced artifact.
1. [ ] YAML parses
2. [ ] id matches p07_ue_ prefix
3. [ ] assertions is non-empty list
4. [ ] each assertion has gate_ref
5. [ ] timeout is positive integer

## Metadata

```yaml
id: bld_tools_unit_eval
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-unit-eval.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_golden_test]] | sibling | 0.69 |
| [[bld_tools_e2e_eval]] | sibling | 0.68 |
| [[bld_tools_smoke_eval]] | sibling | 0.67 |
| [[bld_tools_validation_schema]] | sibling | 0.64 |
| [[bld_tools_scoring_rubric]] | sibling | 0.61 |
| [[bld_tools_retriever_config]] | sibling | 0.61 |
| [[bld_tools_cli_tool]] | sibling | 0.61 |
| [[bld_tools_memory_scope]] | sibling | 0.61 |
| [[bld_tools_lifecycle_rule]] | sibling | 0.60 |
| [[bld_tools_input_schema]] | sibling | 0.60 |
