---
kind: config
id: bld_config_red_team_eval
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
title: "Config Red Team Eval"
version: "1.0.0"
author: n03_builder
tags: [red_team_eval, builder, examples]
tldr: "Golden and anti-examples for red team eval construction, demonstrating ideal structure and common pitfalls."
domain: "red team eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_red_team_eval
  - p11_qg_red_team_eval
  - bld_instruction_red_team_eval
  - bld_knowledge_card_red_team_eval
  - p03_sp_red_team_eval_builder
  - red-team-eval-builder
  - p10_lr_red_team_eval_builder
  - bld_examples_red_team_eval
  - p01_kc_red_team_eval
  - bld_collaboration_red_team_eval
---
# Config: red_team_eval Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p07_rt_{eval_slug}.md` | `p07_rt_costmer_support_agent.md` |
| Builder directory | kebab-case | `red-team-eval-builder/` |
| Frontmatter fields | snake_case | `attack_types`, `pass_criteria`, `owasp_refs` |
| Eval slug | snake_case, lowercase, no hyphens | `costmer_support_agent`, `rag_pipeline` |
| Attack type values | snake_case enum values | `prompt_injection`, `pii_leak`, `jailbreak` |
| OWASP refs | uppercase with number | `LLM01`, `LLM06`, `LLM08` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
Rule: attack_types values MUST be from approved enum in SCHEMA.md.
## File Paths
- Output: `cex/P07_evals/examples/p07_rt_{eval_slug}.md`
- Compiled: `cex/P07_evals/compiled/p07_rt_{eval_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~3500 bytes
- Density: >= 0.80 (no filler prose)
## Severity Enum
| Value | Meaning | Example |
|-------|---------|---------|
| critical | Attack success causes immediate user harm or data breach | PII leak of financial records |
| high | Attack success enables significant policy violation | Jailbreak producing harmful instructions |
| medium | Attack success causes notable but contained harm | Bias in recommendations |
| low | Attack success causes minor quality degradation | Verbose refusal fails to redirect |
## Framework Selection Guide
| Framework | Best For | Config Format |
|-----------|----------|---------------|
| promptfoo | Config-driven teams, YAML-native pipelines | `promptfooconfig.yaml` |
| garak | CLI-first security teams, probe-based scanning | CLI flags + JSONL output |
| deepeval | Python-native teams, pytest integration | Python test files |
| patronus | API-first teams, managed adversarial suites | REST API calls |
| costm | Novel attack types not covered by frameworks | Custom test harness |
## Attack Type Constraints
- Minimum 1 attack_type required (HARD gate)
- Recommended: 3-5 attack types for meaningful coverage
- Maximum: all 10 enum values (full coverage red team)
- attack_types in frontmatter MUST have matching section in ## Attack Scenarios body
## Payload Safety Rules
- NEVER include real jailbreak strings (DAN prompts, specific bypass techniques)
- NEVER include real PII (names, SSNs, emails, phone numbers)
- ALWAYS use `{placeholder_name}`, `{account_id}`, `{target_email}` notation
- Framework-specific config snippets MAY reference plugin names (e.g., `harmful:hate`) without payloads

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_red_team_eval]] | upstream | 0.38 |
| [[p11_qg_red_team_eval]] | downstream | 0.38 |
| [[bld_instruction_red_team_eval]] | upstream | 0.37 |
| [[bld_knowledge_card_red_team_eval]] | upstream | 0.35 |
| [[p03_sp_red_team_eval_builder]] | upstream | 0.35 |
| [[red-team-eval-builder]] | upstream | 0.33 |
| [[p10_lr_red_team_eval_builder]] | downstream | 0.32 |
| [[bld_examples_red_team_eval]] | upstream | 0.30 |
| [[p01_kc_red_team_eval]] | upstream | 0.29 |
| [[bld_collaboration_red_team_eval]] | downstream | 0.29 |
