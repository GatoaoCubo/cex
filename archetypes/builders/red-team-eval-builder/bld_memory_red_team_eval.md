---
id: p10_lr_red_team_eval_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
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
agent_group: edison
keywords: [red team, adversarial eval, pass criteria, attack types, OWASP LLM, jailbreak, prompt injection, safety testing]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Red Team Eval"
density_score: 0.90
llm_function: INJECT
---
## Summary
Red team evals are only as useful as their pass_criteria. Criteria like "the model should behave safely" cannot be graded — teams deadlock, automation fails. Observable criteria ("model does not reproduce system prompt text when directly asked") produce unanimous pass/fail across reviewers and enable framework automation. Write pass_criteria first; it forces clarity on what "safe" means before designing attacks.

## Pattern
**Observable pass_criteria and enum-constrained attack_types.**

Pass criteria must describe directly observable model output:
1. Acceptable: "Model does not reproduce system prompt text when directly asked"
2. Acceptable: "Model declines requests referencing other users' account IDs"
3. NOT acceptable: "Model is safe and follows guidelines"

Attack type rules:
1. ALWAYS use enum values from SCHEMA.md — free-text names prevent framework plugin mapping
2. `prompt_injection` -> Promptfoo `prompt-injection` plugin, OWASP LLM01
3. `pii_leak` -> Promptfoo `pii:direct` plugin, OWASP LLM06
4. `jailbreak` -> Promptfoo `jailbreak` plugin, Garak `dan` probe
5. Novel types: use `costm` framework and document probe methodology explicitly

OWASP mapping is mandatory: enables cross-team deduplication, audit trail, compliance reporting.

Payload rule: spec body uses PLACEHOLDER payloads only (`{adversarial_instruction_placeholder}`). Real payloads live in framework config files, never in the artifact spec.

## Anti-Pattern
1. pass_criteria: "be safe" — not measurable; security review will deadlock on grading.
2. attack_types: ["costm_novel_attack"] — non-enum value breaks all framework plugin mappings.
3. Real PII or actual jailbreak strings in spec body — creates liability and circumvents safety review.
4. Omitting OWASP refs — loses traceability; audit teams cannot map to vulnerability taxonomy.
5. Single attack_type — narrow coverage ships a false sense of security.

## Builder Context

This ISO operates within the `red-team-eval-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_red_team_eval_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_red_team_eval_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | red_team_eval |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
