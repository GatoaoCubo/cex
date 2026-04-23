---
kind: tools
id: bld_tools_schedule
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for schedule production
quality: 9.0
title: "Tools Schedule"
version: "1.0.0"
author: n03_builder
tags: [schedule, builder, examples]
tldr: "Golden and anti-examples for schedule construction, demonstrating ideal structure and common pitfalls."
domain: "schedule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_workflow
  - bld_tools_checkpoint
  - bld_tools_function_def
  - bld_tools_prompt_version
  - bld_tools_output_validator
  - bld_tools_path_config
  - bld_tools_handoff_protocol
---

# Tools: schedule-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing schedule and workflow artifacts in pool | Phase 1 (resolve workflow_ref, check duplicates) | CONDITIONAL |
| crontab_validate | Validate cron expression syntax and compute next N fire times | Phase 1 (verify expression before committing) | [PLANNED] |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P12_orchestration/_schema.yaml | Field definitions, schedule kind |
| CEX Examples | P12_orchestration/examples/ | Real schedule artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P12_schedule |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Workflow Index | P12_orchestration/workflows/ | Resolvable workflow_ref ids |
## Cron Validation Reference
Key checks to run manually before output:
- Field count: exactly 5 (min hour dom month dow) or 6 (sec min hour dom month dow)
- Range validity: min 0-59, hour 0-23, dom 1-31, month 1-12, dow 0-7
- Step syntax: `*/N` valid; `N/M` valid; named months (JAN-DEC) and days (MON-SUN) valid
- Next-fire sanity: compute next 3 execution times and confirm they match intent
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern matches `^p12_sc_`, cron
expression is valid 5-field, workflow_ref non-empty, body <= 1024 bytes, quality == null,
all four body sections present (Overview, Trigger, Workflow, Policy).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_retriever_config]] | sibling | 0.52 |
| [[bld_tools_memory_scope]] | sibling | 0.52 |
| [[bld_tools_cli_tool]] | sibling | 0.52 |
| [[bld_tools_workflow]] | sibling | 0.51 |
| [[bld_tools_checkpoint]] | sibling | 0.51 |
| [[bld_tools_function_def]] | sibling | 0.51 |
| [[bld_tools_prompt_version]] | sibling | 0.50 |
| [[bld_tools_output_validator]] | sibling | 0.50 |
| [[bld_tools_path_config]] | sibling | 0.50 |
| [[bld_tools_handoff_protocol]] | sibling | 0.50 |
