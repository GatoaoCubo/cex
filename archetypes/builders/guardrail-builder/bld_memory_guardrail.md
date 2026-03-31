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
agent_node: edison
keywords: [guardrail, severity, enforcement, block, warn, log, bypass_policy, concrete_rule, safety, access_control]
memory_scope: project
observation_types: [user, feedback, project, reference]
---
## Summary
A guardrail defines safety restrictions with concrete, matchable rules and explicit enforcement. Its value comes from being unambiguous — the enforcement layer must be able to evaluate whether a given input or output triggers the rule. Severity classification drives enforcement mode, and every guardrail must document how it can be bypassed in an emergency.
## Pattern
1. Rules are concrete and matchable: name the exact pattern, field, operation, or value range. "Block requests where output contains PII fields: ssn, credit_card, dob" is enforceable. "Be careful with sensitive data" is not.
2. `severity` is one of four values: `critical`, `high`, `medium`, `low`.
3. `enforcement` matches severity:
   - `critical` / `high` -> `block` (pre-execution hook or output filter; request never completes)
   - `medium` -> `warn` (monitoring alert fired; request completes with warning logged)
   - `low` -> `log` (audit trail only; no interruption)
4. Every guardrail, including critical ones, includes a `## Bypass Policy` section: who can authorize override, what process is followed, and how overrides are audited.
5. Guardrail controls safety behavior (what the system must not do). Permission controls access (who can use the system). These are separate artifacts.
6. `id` slug uses underscores: `p11_gr_dest_cmds` not `p11_gr_dest-cmds`.
## Anti-Pattern
- Subjective rules like "be careful" or "handle responsibly" — enforcement cannot match these.
- `severity: "important"` or `severity: "danger"` — invalid enum values, rejected by schema.
- `enforcement: "stop"` or `enforcement: "prevent"` — invalid enum values; use block/warn/log.
- No bypass policy on critical guardrails — leaves incident responders with no override path.
- Using block enforcement for low-severity guardrails — fires on benign inputs, causes alert fatigue, gets disabled.
- Combining access control rules with safety rules in one guardrail — conflation makes both harder to audit and maintain.
## Context
