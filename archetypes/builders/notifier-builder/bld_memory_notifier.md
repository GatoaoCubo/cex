---
kind: memory
id: bld_memory_notifier
pillar: P04
llm_function: INJECT
purpose: Learned patterns and anti-patterns from notifier artifact production
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [memory, notifier, P04, patterns, learning]
quality: 9.0
tldr: "Key learnings: rate_limit prevents provider bans, priority routing prevents alert fatigue, template_vars prevent runtime formatting errors."
memory_scope: project
observation_types: [user, feedback, project, reference]
density_score: 0.83
domain: "memory artifact construction"
title: "Memory Notifier"
related:
  - p03_sp_notifier_builder
  - bld_collaboration_notifier
  - bld_output_template_notifier
  - p11_qg_notifier
  - bld_instruction_notifier
  - bld_architecture_notifier
  - bld_examples_notifier
  - notifier-builder
  - bld_schema_notifier
  - p04_notify_slack
---
# Memory: notifier-builder Learnings

## Pattern: Rate Limit Prevents Provider Bans [score: 9.0]
**Context**: Notifiers without rate_limit hit provider limits during traffic spikes.
**Learning**: Always define rate_limit even for low-volume channels. Twilio suspends numbers
after burst violations. SendGrid downgrades accounts after IP reputation damage.
**Rule derived**: rate_limit is REC but treat as required for any production channel.

## Pattern: Priority Routing Prevents Alert Fatigue [score: 8.5]
**Context**: All-critical notifiers caused on-call engineers to ignore alerts.
**Learning**: critical must mean "page someone now". Misuse of critical degrades response
to genuine incidents. Document timing semantics per priority level in the Template section.
**Rule derived**: Every notifier with priority: critical must justify it in Overview.

## Pattern: Template Vars Prevent Runtime Errors [score: 8.5]
**Context**: Notifiers with undocumented template vars caused KeyError at delivery time.
**Learning**: template_vars frontmatter field must list every `{{var}}` used in the template.
Consumers cannot implement without knowing what data to provide.
**Rule derived**: template_vars list must be exhaustive; missing vars = H05 soft fail.

## Pattern: Retry on Critical = Non-Negotiable [score: 9.0]
**Context**: Critical Slack alert dropped silently during Slack API outage (no retry).
**Learning**: at_least_once delivery_guarantee requires retry_policy. best_effort is only
acceptable for low/normal priority. H09 soft gate added as HARD gate for critical channel.
**Rule derived**: priority: critical -> retry_policy: required (not recommended).

## Anti-Pattern: Notifier as Webhook [score: fail]
**Context**: Builder produced notifier artifact that described receiving HTTP POST events.
**Learning**: Notifier = outbound push only. Any inbound/receive/listen pattern = webhook.
If artifact says "receives", "listens", "handles incoming" -> redirect to webhook-builder.
**Rule derived**: H10 gate added — bidirectional HTTP semantics = immediate REJECT.

## Anti-Pattern: Provider SDK Code in Body [score: fail]
**Context**: Notifier body contained Python sendgrid library call.
**Learning**: Notifier is a spec, not implementation. SDK code inflates bytes, bleeds
implementation detail, and couples spec to language. Code belongs in code-gen output.
**Rule derived**: Body may reference provider endpoint and env var only — no SDK imports.

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `memory`
- **Artifact ID**: `bld_memory_notifier`
- **Tags**: [memory, notifier, P04, patterns, learning]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `memory` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_notifier_builder]] | related | 0.40 |
| [[bld_collaboration_notifier]] | related | 0.37 |
| [[bld_output_template_notifier]] | related | 0.37 |
| [[p11_qg_notifier]] | downstream | 0.36 |
| [[bld_instruction_notifier]] | upstream | 0.35 |
| [[bld_architecture_notifier]] | related | 0.33 |
| [[bld_examples_notifier]] | related | 0.32 |
| [[notifier-builder]] | related | 0.30 |
| [[bld_schema_notifier]] | downstream | 0.30 |
| [[p04_notify_slack]] | related | 0.29 |
