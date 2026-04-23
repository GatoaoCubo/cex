---
kind: config
id: bld_config_bugloop
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for bugloop production
pattern: CONFIG restricts SCHEMA, never contradicts
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Bugloop"
version: "1.0.0"
author: n03_builder
tags: [bugloop, builder, examples]
tldr: "Golden and anti-examples for bugloop construction, demonstrating ideal structure and common pitfalls."
domain: "bugloop construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_bugloop
  - bld_output_template_bugloop
  - bld_schema_bugloop
  - p03_sp_bugloop_builder
  - bld_examples_bugloop
  - bld_knowledge_card_bugloop
  - p01_kc_bugloop
  - p11_qg_bugloop
  - bugloop-builder
  - bld_config_memory_scope
---
# Config: bugloop Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p11_bl_{scope}.md | p11_bl_api_validation.md |
| Builder dir | kebab-case | bugloop-builder/ |
| Fields | snake_case | cycle_count, auto_fix |
| Scope slug | snake_case, no hyphens | kc_pipeline, test_runner |
Rule: id MUST equal filename stem.
Rule: scope slug MUST reflect monitored system, not the fix type.
## File Paths
- Output: cex/P11_feedback/examples/p11_bl_{scope}.md
- Compiled: cex/P11_feedback/compiled/p11_bl_{scope}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
## Field Constraints
| Field | Constraint |
|-------|-----------|
| fix.max_attempts | integer 1-10 |
| cycle_count | integer 1-20; >= fix.max_attempts |
| escalation.threshold | integer <= cycle_count |
| confidence | float 0.00-1.00 |
| verify.timeout | integer > 0 (seconds) |
| auto_fix (root) | MUST equal fix.auto_fix |
## Enum Restrictions
| Field | Allowed Values |
|-------|---------------|
| detect.method | static_analysis, runtime_trace, test_failure, log_scan |
| detect.trigger | on_commit, on_deploy, scheduled, continuous |
| fix.strategy | patch_and_retry, rollback_first, isolate_then_fix |
| rollback.strategy | git_revert, snapshot_restore, blue_green |
## Confidence Calibration
| Confidence | Meaning | Required |
|-----------|---------|----------|
| >= 0.9 | High — auto_fix safe | Full test suite verification |
| 0.7-0.89 | Medium — auto_fix with review | Assertions + timeout |
| < 0.7 | Low — manual fix preferred | escalation.threshold <= 2 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_bugloop]] | upstream | 0.44 |
| [[bld_output_template_bugloop]] | upstream | 0.42 |
| [[bld_schema_bugloop]] | downstream | 0.42 |
| [[p03_sp_bugloop_builder]] | downstream | 0.41 |
| [[bld_examples_bugloop]] | upstream | 0.41 |
| [[bld_knowledge_card_bugloop]] | upstream | 0.37 |
| [[p01_kc_bugloop]] | downstream | 0.33 |
| [[p11_qg_bugloop]] | downstream | 0.31 |
| [[bugloop-builder]] | downstream | 0.29 |
| [[bld_config_memory_scope]] | sibling | 0.29 |
