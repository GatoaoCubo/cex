---
id: p02_handoff_protocol
kind: handoff_protocol
pillar: P02
version: 1.0.0
title: "Template — Handoff Protocol"
tags: [template, handoff, protocol, agent, transfer]
tldr: "Defines how control transfers between agents or nuclei. Specifies trigger conditions, payload schema, acknowledgment rules, and failure handling for agent-to-agent handoffs."
quality: 9.0
domain: "model configuration"
density_score: 0.85
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
---

# Handoff Protocol: [PROTOCOL_NAME]

## Purpose
[WHY this handoff exists — what task requires transferring control between agents]

## Participants

| Role | Agent/Nucleus | Responsibility |
|------|--------------|----------------|
| Sender | [SOURCE_AGENT] | [Packages state, initiates handoff] |
| Receiver | [TARGET_AGENT] | [Validates payload, continues work] |
| Observer | [N07 / monitor] | [Logs handoff, detects failures] |

## Trigger Conditions
Handoff activates when:
- [CONDITION_1 — e.g., task exceeds sender's domain boundary]
- [CONDITION_2 — e.g., pipeline stage requires different expertise]
- [CONDITION_3 — e.g., explicit dispatch from orchestrator]

## Payload Schema
```yaml
handoff:
  id: "[UUID]"
  from: "[SENDER_ID]"
  to: "[RECEIVER_ID]"
  timestamp: "[ISO8601]"
  task: "[TASK_DESCRIPTION]"
  context:
    state: [ACCUMULATED_STATE]
    constraints: [RELEVANT_CONSTRAINTS]
    priority: [low | medium | high | critical]
  artifacts: ["[PATH_1]", "[PATH_2]"]
```

## Acknowledgment
- **Timeout**: [SECONDS]s — if receiver doesn't ACK, trigger fallback
- **ACK format**: `{handoff_id, status: "accepted" | "rejected", reason?}`
- **On reject**: [RETRY_WITH_CONTEXT | ESCALATE_TO_N07 | ABORT]

## Failure Handling
| Failure | Response | Escalation |
|---------|----------|------------|
| Receiver unreachable | Retry 2x, then escalate | N07 re-dispatch |
| Payload invalid | Return to sender with errors | Sender fixes + resend |
| Receiver rejects | Try alternate receiver | N07 manual resolution |
| Timeout | Kill + log + try fallback | Alert + checkpoint |

## Quality Gate
- [ ] Both sender and receiver identified
- [ ] Payload schema defined with required fields
- [ ] ACK timeout configured
- [ ] At least 2 failure scenarios handled
