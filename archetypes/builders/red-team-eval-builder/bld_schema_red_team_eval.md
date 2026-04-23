---
kind: schema
id: bld_schema_red_team_eval
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for red_team_eval
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Red Team Eval"
version: "1.0.0"
author: n03_builder
tags: [red_team_eval, builder, examples]
tldr: "Golden and anti-examples for red team eval construction, demonstrating ideal structure and common pitfalls."
domain: "red team eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_unit_eval
  - bld_schema_action_prompt
  - bld_schema_golden_test
  - bld_schema_handoff_protocol
  - bld_schema_smoke_eval
  - bld_schema_memory_scope
  - bld_schema_prompt_version
  - bld_schema_constraint_spec
---

# Schema: red_team_eval
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_rt_{slug}) | YES | - | Namespace compliance |
| kind | literal "red_team_eval" | YES | - | Type integrity |
| pillar | literal "P07" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable eval name |
| attack_types | list[enum] len >= 1 | YES | - | Attack categories covered |
| target | string | YES | - | Agent/prompt/system under test |
| pass_criteria | string | YES | - | What constitutes safe behavior |
| quality | null | YES | null | Never self-score |
| tags | list[string] len >= 3 | YES | - | Must include "red_team_eval" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the eval tests |
| framework | enum: promptfoo, patronus, deepeval, garak, costm | REC | - | Eval framework used |
| severity | enum: critical, high, medium, low | REC | - | Risk level if attacks succeed |
| test_count | integer >= 1 | REC | - | Number of adversarial test cases |
| owasp_refs | list[string] | REC | - | OWASP LLM Top 10 references |
| env_vars | list[string] | REC | - | Environment variables required |
## Attack Type Enum
Allowed values for `attack_types`:
- `prompt_injection` — attacker injects instructions overriding system prompt
- `jailbreak` — attempt to bypass safety guidelines via role-play, encoding, etc.
- `pii_leak` — eliciting personally identifiable information from the model
- `toxicity` — generating harmful, offensive, or abusive content
- `bias` — producing discriminatory or stereotyped outputs
- `hallucination_exploit` — leveraging model hallucination for harmful outputs
- `data_extraction` — extracting training data or system prompt contents
- `indirect_injection` — injecting via external content (RAG, tool output, email)
- `denial_of_service` — resource exhaustion via adversarial inputs
- `privilege_escalation` — gaining unauthorized capabilities or access levels
## ID Pattern
Regex: `^p07_rt_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what is being tested, threat model, who runs this eval
2. `## Attack Scenarios` — each attack_type with concrete test cases and payloads
3. `## Pass Criteria` — explicit definition of safe vs. unsafe responses
4. `## Configuration` — framework config, env vars, test execution instructions
## Constraints
- max_bytes: 2048 (body only — adversarial configs require richer test case detail)
- naming: p07_rt_{slug}.md (single file, matches naming: p07_redteam.md convention)
- machine_format: yaml (compiled artifact)
- id == filename stem
- attack_types list MUST match attack categories documented in ## Attack Scenarios
- quality: null always
- NO real PII or actual exploit payloads in body — use placeholders

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.61 |
| [[bld_schema_output_validator]] | sibling | 0.61 |
| [[bld_schema_unit_eval]] | sibling | 0.60 |
| [[bld_schema_action_prompt]] | sibling | 0.60 |
| [[bld_schema_golden_test]] | sibling | 0.60 |
| [[bld_schema_handoff_protocol]] | sibling | 0.60 |
| [[bld_schema_smoke_eval]] | sibling | 0.60 |
| [[bld_schema_memory_scope]] | sibling | 0.59 |
| [[bld_schema_prompt_version]] | sibling | 0.59 |
| [[bld_schema_constraint_spec]] | sibling | 0.59 |
