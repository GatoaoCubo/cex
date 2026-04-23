---
id: p10_lr_guardrail_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Guardrails with subjective rules ('be careful with sensitive data') are unenforceable — enforcement logic cannot match against vague conditions. Missing bypass policy on critical guardrails causes incident escalation with no resolution path. Invalid severity values ('important', 'danger') and invalid enforcement values ('stop', 'prevent') fail schema validation on every build. Guardrails conflated with permissions (access control) grow to cover both and become unmanageable. Low-severity guardrails enforced with block create alert fatigue and get disabled."
pattern: "Rules must be concrete and matchable: specify exact patterns, field names, operation types, or value ranges that trigger the guardrail. Severity is one of four values: critical/high/medium/low. Enforcement matches severity: critical+high use block (pre-exec hook or output filter), medium uses warn (monitoring alert), low uses log (audit trail). Every guardrail — including critical — documents a bypass policy for emergency override. Guardrail controls safety behavior; permission controls access. Separate artifacts for each."
evidence: "10 guardrail artifacts reviewed. Subjective rules required rework to concrete form in 6 of 10. Missi..."
confidence: 0.75
outcome: SUCCESS
domain: guardrail
tags: [guardrail, security, enforcement, severity, bypass_policy, concrete_rules, safety]
tldr: "Rules must be concrete and matchable; enforcement must match severity; every guardrail needs a bypass policy."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [guardrail, severity, enforcement, block, warn, log, bypass_policy, concrete_rule, safety, access_control]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Guardrail"
density_score: 0.90
llm_function: INJECT
---
## Summary
A guardrail defines safety restrictions with concrete, matchable rules and explicit enforcement. Its value comes from being unambiguous — the enforcement layer must be able to evaluate whether a given input or output triggers the rule. Severity classification drives enforcement mode, and every guardrail must document how it can be bypassed in an emergency.
## Pattern
1. Rules are concrete and matchable: name the exact pattern, field, operation, or value range. "Block requests where output contains PII fields: ssn, credit_card, dob" is enforceable. "Be careful with sensitive data" is not.
2. `severity` is one of four values: `critical`, `high`, `medium`, `low`.
3. `enforcement` matches severity:
   - `critical` / `high` -> `block` (pre-execution hook or output filter; request never complete)
   - `medium` -> `warn` (monitoring alert fired; request complete with warning logged)
   - `low` -> `log` (audit trail only; no interruption)
4. Every guardrail, including critical ones, includes a `## Bypass Policy` section: who can authorize override, what process is followed, and how overrides are audited.
5. Guardrail controls safety behavior (what the system must not do). Permission controls access (who can use the system). These are separate artifacts.
6. `id` slug uses underscores: `p11_gr_dest_cmds` not `p11_gr_dest-cmds`.
## Anti-Pattern
1. Subjective rules like "be careful" or "handle responsibly" — enforcement cannot match these.
2. `severity: "important"` or `severity: "danger"` — invalid enum values, rejected by schema.
3. `enforcement: "stop"` or `enforcement: "prevent"` — invalid enum values; use block/warn/log.
4. No bypass policy on critical guardrails — leaves incident responders with no override path.
5. Using block enforcement for low-severity guardrails — fires on benign inputs, causes alert fatigue, gets disabled.
6. Combining access control rules with safety rules in one guardrail — conflation makes both harder to audit and maintain.
## Context

## Builder Context

This ISO operates within the `guardrail-builder` stack, one of 125
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

## Reference

```yaml
id: p10_lr_guardrail_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_guardrail_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | guardrail |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
