---
kind: tools
id: bld_tools_formatter
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for formatter production
quality: 9.1
title: "Tools Formatter"
version: "1.0.0"
author: n03_builder
tags: [formatter, builder, examples]
tldr: "Golden and anti-examples for formatter construction, demonstrating ideal structure and common pitfalls."
domain: "formatter construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_output_validator
  - bld_tools_prompt_version
  - bld_tools_runtime_rule
  - bld_tools_path_config
  - bld_tools_constraint_spec
  - bld_tools_handoff_protocol
  - bld_tools_boot_config
---

# Tools: formatter-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing formatters to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | SCHEMA.md (this builder) | Field definitions, rule object |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P05_formatter |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Existing formatters | P05_output/examples/p05_fmt_*.md | Real formatter artifacts |
| Mustache spec | mustache.github.io | Template syntax reference |
| Jinja2 docs | jinja.palletsprojects.com | Template syntax reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == formatter, quality == null,
rule_count matches rules, target_format/input_type valid, at least 1 formatting rule.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_formatter
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-formatter.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_retriever_config]] | sibling | 0.70 |
| [[bld_tools_memory_scope]] | sibling | 0.69 |
| [[bld_tools_cli_tool]] | sibling | 0.69 |
| [[bld_tools_output_validator]] | sibling | 0.68 |
| [[bld_tools_prompt_version]] | sibling | 0.68 |
| [[bld_tools_runtime_rule]] | sibling | 0.68 |
| [[bld_tools_path_config]] | sibling | 0.67 |
| [[bld_tools_constraint_spec]] | sibling | 0.67 |
| [[bld_tools_handoff_protocol]] | sibling | 0.67 |
| [[bld_tools_boot_config]] | sibling | 0.67 |
