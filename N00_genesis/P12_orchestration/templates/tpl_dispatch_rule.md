---
# TEMPLATE: Dispatch Rule (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.dispatch_rule)
# Max 3072 bytes

id: p12_dr_{{SCOPE_SLUG}}
kind: dispatch_rule
8f: F8_collaborate
pillar: P12
title: "Dispatch Rule: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Dispatch Rule: {{SCOPE_NAME}}

## Routing Table
| Condition | Agent_group | Confidence |
|-----------|-----------|------------|
| {{KEYWORD_OR_SIGNAL_1}} | {{AGENT_GROUP_1}} | {{0.0_TO_1.0}} |
| {{KEYWORD_OR_SIGNAL_2}} | {{AGENT_GROUP_2}} | {{0.0_TO_1.0}} |
| {{KEYWORD_OR_SIGNAL_3}} | {{AGENT_GROUP_3}} | {{0.0_TO_1.0}} |

## Review Chain
<!-- 3-tier review: each tier reads code independently, does NOT trust prior tier's report -->
```yaml
review_chain:
  - role: implementer
    action: Execute task, self-review before reporting
    output: Implementation + self-review checklist
  - role: spec_reviewer
    action: Independent code read against spec (do NOT trust implementer report)
    output: PASS / CONCERNS list
  - role: quality_reviewer
    action: Only runs after spec_reviewer passes; checks non-functional (perf, security, style)
    output: PASS / REJECT with specific items
```

## Status Contract
<!-- Implementer MUST report one of these statuses -->

| Status | Meaning | Next Action |
|--------|---------|-------------|
| `DONE` | Task complete, all checks pass | Proceed to spec_reviewer |
| `DONE_WITH_CONCERNS` | Complete but has known issues | Reviewer decides severity |
| `BLOCKED` | Cannot proceed (missing dep, permission, unclear spec) | Escalate to orchestrator |
| `NEEDS_CONTEXT` | Insufficient info to start | Return to dispatch with context request |

## Fallbacks
- No match: {{DEFAULT_ROUTE}}
- Conflict: {{TIEBREAKER_RULE}}
- Escalation: {{ESCALATION_ROUTE}}
