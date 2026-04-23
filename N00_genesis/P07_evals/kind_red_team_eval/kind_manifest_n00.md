---
id: n00_red_team_eval_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Red Team Eval -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, red_team_eval, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_collaboration_red_team_eval
  - bld_schema_red_team_eval
  - red-team-eval-builder
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_safety_policy
  - bld_schema_search_strategy
  - bld_schema_usage_report
  - bld_schema_eval_metric
  - bld_schema_audit_log
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Red team eval defines an adversarial test methodology for discovering failure modes, safety violations, and policy bypasses in an LLM system before deployment. It specifies the attack categories, prompt injection techniques, jailbreak patterns, and scoring criteria for categorizing findings by severity. Red team eval results feed directly into guardrail and safety rule updates.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `red_team_eval` |
| pillar | string | yes | Always `P07` |
| title | string | yes | System name + "Red Team Eval" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_system | string | yes | System or agent being adversarially tested |
| attack_categories | list | yes | Categories tested (prompt injection, jailbreak, data extraction, etc.) |
| test_case_count | int | yes | Total adversarial test cases |
| severity_taxonomy | list | yes | Severity levels with definitions |
| findings_threshold | object | yes | Max acceptable findings per severity before blocking release |

## When to use
- Pre-deployment safety validation for any customer-facing AI system
- Quarterly adversarial testing of production systems to catch new attack patterns
- After a safety incident to audit the attack surface and update guardrails

## Builder
`archetypes/builders/red_team_eval-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind red_team_eval --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence + N05 operations conduct red team evals
- `{{SIN_LENS}}` -- Gating Wrath: assume breach, find every weakness before attackers do
- `{{TARGET_AUDIENCE}}` -- security engineers and AI safety reviewers
- `{{DOMAIN_CONTEXT}}` -- deployment context, user population, regulatory requirements

## Example (minimal)
```yaml
---
id: red_team_eval_cex_chat_agent
kind: red_team_eval
pillar: P07
nucleus: n01
title: "CEX Chat Agent -- Red Team Eval Q1 2026"
version: 1.0
quality: null
---
target_system: "CEX N01 + N02 customer-facing chat"
attack_categories: [prompt_injection, jailbreak, data_extraction, policy_bypass]
test_case_count: 200
findings_threshold: {critical: 0, high: 0, medium: 3}
```

## Related kinds
- `bias_audit` (P07) -- fairness complement to adversarial security testing
- `guardrail` (P11) -- safety artifact updated based on red team findings
- `e2e_eval` (P07) -- functional test that precedes red team for baseline validation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_red_team_eval]] | downstream | 0.47 |
| [[bld_schema_red_team_eval]] | upstream | 0.45 |
| [[red-team-eval-builder]] | related | 0.44 |
| [[bld_schema_integration_guide]] | upstream | 0.40 |
| [[bld_schema_reranker_config]] | upstream | 0.40 |
| [[bld_schema_safety_policy]] | upstream | 0.39 |
| [[bld_schema_search_strategy]] | upstream | 0.39 |
| [[bld_schema_usage_report]] | upstream | 0.39 |
| [[bld_schema_eval_metric]] | upstream | 0.39 |
| [[bld_schema_audit_log]] | upstream | 0.39 |
