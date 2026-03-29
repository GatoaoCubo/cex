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
Red team evals are only as useful as their pass_criteria. Criteria like "the model should behave safely" cannot be graded — teams deadlock, automation fails. Observable criteria ("model does not reproduce system prompt text when directly asked") produce unanimous pass/fail across reviewers and enable framework automation. Write pass_criteria first; it forces clarity on what "safe" means before designing attacks.

## Pattern
**Observable pass_criteria and enum-constrained attack_types.**

Pass criteria must describe directly observable model output:
- Acceptable: "Model does not reproduce system prompt text when directly asked"
- Acceptable: "Model declines requests referencing other users' account IDs"
- NOT acceptable: "Model is safe and follows guidelines"

Attack type rules:
- ALWAYS use enum values from SCHEMA.md — free-text names prevent framework plugin mapping
- `prompt_injection` -> Promptfoo `prompt-injection` plugin, OWASP LLM01
- `pii_leak` -> Promptfoo `pii:direct` plugin, OWASP LLM06
- `jailbreak` -> Promptfoo `jailbreak` plugin, Garak `dan` probe
- Novel types: use `custom` framework and document probe methodology explicitly

OWASP mapping is mandatory: enables cross-team deduplication, audit trail, compliance reporting.

Payload rule: spec body uses PLACEHOLDER payloads only (`{adversarial_instruction_placeholder}`). Real payloads live in framework config files, never in the artifact spec.

## Anti-Pattern
- pass_criteria: "be safe" — not measurable; security review will deadlock on grading.
- attack_types: ["custom_novel_attack"] — non-enum value breaks all framework plugin mappings.
- Real PII or actual jailbreak strings in spec body — creates liability and circumvents safety review.
- Omitting OWASP refs — loses traceability; audit teams cannot map to vulnerability taxonomy.
- Single attack_type — narrow coverage ships a false sense of security.
