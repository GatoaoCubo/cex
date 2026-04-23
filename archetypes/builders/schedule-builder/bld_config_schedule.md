---
kind: config
id: bld_config_schedule
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Schedule"
version: "1.0.0"
author: n03_builder
tags: [schedule, builder, examples]
tldr: "Golden and anti-examples for schedule construction, demonstrating ideal structure and common pitfalls."
domain: "schedule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_schedule
  - p03_sp_schedule_builder
  - bld_instruction_schedule
  - bld_schema_schedule
  - bld_examples_schedule
  - p11_qg_schedule
  - p10_lr_schedule_builder
  - bld_collaboration_schedule
  - bld_output_template_schedule
  - p01_kc_schedule
---
# Config: schedule Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p12_sched_{name}.md` | `p12_sched_daily_report.md` |
| Builder directory | kebab-case | `schedule-builder/` |
| Frontmatter fields | snake_case | `trigger_type`, `workflow_ref`, `catch_up` |
| Schedule slug (id) | snake_case, lowercase, no hyphens | `daily_report`, `weekly_sync` |
| Workflow ref | matches target workflow id exactly | `p13_wf_daily_report` |
| Cron fields | standard 5-field POSIX or 6-field with seconds | `0 9 * * MON-FRI` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
Rule: id prefix MUST be `p12_sc_`. File prefix MUST be `p12_sched_`.
## File Paths
- Output: `cex/P12_orchestration/examples/p12_sched_{name}.md`
- Compiled: `cex/P12_orchestration/compiled/p12_sched_{name}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2000 bytes
- Density: >= 0.80 (no filler)
## Trigger Type Enum
| Value | When to use |
|-------|-------------|
| cron | Fixed time expression (daily, weekly, monthly) |
| interval | Every N minutes/hours regardless of clock time |
| event | External event fires the trigger (file arrival, API call) |
| manual | Human or API call only — no automatic firing |
| one_shot | Single future execution, then disabled |
## Timezone Rules
| Rule | Detail |
|------|--------|
| Always declare timezone | UTC assumption breaks DST transitions |
| Use IANA tz database names | "America/Sao_Paulo" not "BRT-3" |
| Business schedules | Use local timezone of the business unit |
| Data pipeline schedules | UTC preferred to avoid DST ambiguity |
## Concurrency Defaults
| max_concurrent | Default when |
|---------------|-------------|
| 1 | All schedules (prevent resource exhaustion) |
| > 1 | Only when workflow is stateless and idempotent |
| null | FORBIDDEN — always declare an explicit integer |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_schedule]] | upstream | 0.41 |
| [[p03_sp_schedule_builder]] | upstream | 0.41 |
| [[bld_instruction_schedule]] | upstream | 0.37 |
| [[bld_schema_schedule]] | upstream | 0.34 |
| [[bld_examples_schedule]] | upstream | 0.33 |
| [[p11_qg_schedule]] | downstream | 0.33 |
| [[p10_lr_schedule_builder]] | downstream | 0.33 |
| [[bld_collaboration_schedule]] | downstream | 0.33 |
| [[bld_output_template_schedule]] | upstream | 0.30 |
| [[p01_kc_schedule]] | downstream | 0.30 |
