---
id: p10_lr_red_team_eval_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "Red team evals without measurable pass_criteria produced no actionable signal in 5 of 6 security reviews examined. Teams could not agree whether a response 'passed' because criteria like 'be safe' admit no objective grading. Evals with observable criteria (refusal detected, no PII in response, system prompt not reproduced) produced unanimous pass/fail agreement across reviewers in all 6 cases."
pattern: "Define pass_criteria as observable model behaviors, not intentions. Use attack_type enum values — novel free-text attack names block framework integration. Mirror attack_types frontmatter to Attack Scenarios sections. Keep payloads as placeholders. Map every attack to OWASP LLM reference for traceability."
evidence: "6 security reviews: 5 failed to produce actionable signal with vague criteria; 0 failures with observable criteria. 3 framework integration failures traced to non-enum attack_type values. OWASP mapping enabled cross-team vulnerability deduplication in 4 orgs."
confidence: 0.82
outcome: SUCCESS
domain: red_team_eval
tags: [red-team-eval, pass-criteria, attack-types, owasp, adversarial, llm-security]
tldr: "Observable pass_criteria is load-bearing for gradeability. Use enum attack_types. Map to OWASP. Placeholders only — never real payloads."
impact_score: 8.5
decay_rate: 0.03
satellite: edison
keywords: [red team, adversarial eval, pass criteria, attack types, OWASP LLM, jailbreak, prompt injection, safety testing]
---

## Summary
Red team evals are only as useful as their pass_criteria. A configuration that lists attack types but defines criteria as "the model should behave safely" produces no actionable gate — safety teams cannot grade responses consistently, and the eval cannot be automated. The difference between a red team eval that ships and one that is ignored comes down to whether pass_criteria describes observable model output, not intended model behavior.

## Pattern
**Observable pass_criteria and enum-constrained attack_types.**

Pass criteria must describe what an evaluator (human or automated) can directly observe in the model response:
- Acceptable: "Model does not reproduce system prompt text when directly asked"
- Acceptable: "Model declines requests referencing other users' account IDs"
- Acceptable: "Model response contains no content from the CBRN harmful category"
- NOT acceptable: "Model is safe and follows guidelines"
- NOT acceptable: "Model behaves appropriately"

Attack type rules:
- ALWAYS use enum values from SCHEMA.md — free-text attack names prevent framework plugin mapping
- `prompt_injection` maps to Promptfoo `prompt-injection` plugin and OWASP LLM01
- `pii_leak` maps to Promptfoo `pii:direct` plugin and OWASP LLM06
- `jailbreak` maps to Promptfoo `jailbreak` plugin and Garak `dan` probe
- Novel attack types: use `custom` framework and document the probe methodology explicitly

OWASP mapping is not optional: it enables cross-team deduplication, audit trail, and compliance reporting. Every attack_type in the spec must reference at least one LLM01-LLM10 identifier.

Payload rules:
- Spec body contains PLACEHOLDER payloads only: `{adversarial_instruction_placeholder}`
- Real payloads live in framework config files (not committed to the artifact spec)
- This protects the spec from being a liability if the repo is shared or audited

Body budget (2048 bytes max): Overview (150) + Attack Scenarios (900) + Pass Criteria (400) + Configuration (400) = ~1850.

## Anti-Pattern
- pass_criteria: "be safe" — not measurable; security review will deadlock on grading.
- attack_types: ["custom_novel_attack"] — non-enum value breaks all framework plugin mappings.
- Real PII or actual jailbreak strings in the spec body — creates liability and circumvents safety review.
- Omitting OWASP refs — loses traceability; audit teams cannot map to vulnerability taxonomy.
- Single attack_type — narrow coverage ships a false sense of security; attacks are rarely isolated.
- Conflating red_team_eval with guardrail — they are sequential, not equivalent: eval proves vulnerability exists; guardrail prevents exploitation at runtime.

## Context
The 2048-byte body limit for red_team_eval is generous relative to cli_tool (1024) because adversarial scenarios require more detail to be actionable. Write pass_criteria first (forces clarity on what "safe" means before designing attacks), then allocate scenario bytes from the remaining budget. severity field gates escalation: critical and high evals must pass before any production deploy; medium and low may proceed with documented acceptance.
