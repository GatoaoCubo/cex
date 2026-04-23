---
kind: schema
id: bld_schema_hook
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for hook
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Hook"
version: "1.0.0"
author: n03_builder
tags: [hook, builder, examples]
tldr: "Golden and anti-examples for hook construction, demonstrating ideal structure and common pitfalls."
domain: "hook construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_hook_config
  - bld_schema_smoke_eval
  - bld_schema_action_prompt
  - bld_schema_handoff_protocol
  - bld_schema_retriever_config
  - bld_schema_unit_eval
  - bld_schema_golden_test
  - bld_schema_output_validator
  - bld_schema_workflow
  - bld_schema_memory_scope
---

# Schema: hook
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_hook_{slug}) | YES | - | Namespace compliance |
| kind | literal "hook" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| trigger_event | enum [pre_tool_use, post_tool_use, session_start, session_end, user_prompt_submit, stop, subagent_stop, pre_compact, permission_request, notification, costm] | YES | - | Which event fires this hook |
| script_path | string | YES | - | Path to executable script |
| execution | enum [pre, post, both] | YES | - | When hook runs relative to event |
| blocking | boolean | YES | - | Whether hook blocks event processing |
| domain | string | YES | - | Domain this hook serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "hook" |
| tldr | string <= 160ch | YES | - | Dense summary |
| timeout | integer (ms) | YES | 5000 | Max execution time before kill |
| conditions | list[string] | REC | [] | Conditions that must be true to trigger |
| async | boolean | REC | false | Whether hook runs asynchronously |
| error_handling | enum [ignore, log, fail, retry] | REC | "log" | Behavior on hook failure |
| logging | boolean | REC | true | Whether hook execution is logged |
| environment | list[string] | REC | [] | Env vars passed to script |
| keywords | list[string] | REC | - | Brain search triggers |
| density_score | float 0.80-1.00 | OPT | - | Content density |
## Condition Object
```yaml
condition:
  field: string (event property to check)
  operator: enum [equals, not_equals, contains, matches, exists]
  value: string (comparison value)
```
## ID Pattern
Regex: `^p04_hook_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Trigger Configuration` — event, conditions, when/why it fires
2. `## Script` — script content or path with arguments
3. `## Input/Output` — what the hook receives from event and what it returns
4. `## Error Handling` — behavior per error_handling strategy
5. `## References` — sources and documentation
## Constraints
- max_bytes: 1024 (body only)
- naming: p04_hook_{slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- quality: null always
- trigger_event MUST be from the enum
- timeout MUST be > 0 and <= 30000 (30s max)
- script_path MUST be a valid relative or absolute path
- If blocking: true, timeout is mandatory and must be reasonable (<10s)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_hook_config]] | sibling | 0.64 |
| [[bld_schema_smoke_eval]] | sibling | 0.60 |
| [[bld_schema_action_prompt]] | sibling | 0.60 |
| [[bld_schema_handoff_protocol]] | sibling | 0.59 |
| [[bld_schema_retriever_config]] | sibling | 0.59 |
| [[bld_schema_unit_eval]] | sibling | 0.59 |
| [[bld_schema_golden_test]] | sibling | 0.58 |
| [[bld_schema_output_validator]] | sibling | 0.58 |
| [[bld_schema_workflow]] | sibling | 0.57 |
| [[bld_schema_memory_scope]] | sibling | 0.57 |
