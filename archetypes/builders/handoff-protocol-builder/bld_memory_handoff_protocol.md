---
id: p10_lr_handoff_protocol_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "handoff_protocol artifacts require concrete parameter values with rationale. Placeholder values cause downstream failures."
pattern: "Define all parameters with concrete values and rationale. Validate against SCHEMA.md. Keep body under 2048 bytes."
evidence: "Pattern extracted from Google A2A Task lifecycle, OpenAI Swarm Handoff, Anthropic tool_use handoff, CrewAI delegation, AutoGen handoff documentation and production usage."
confidence: 0.7
outcome: SUCCESS
domain: handoff_protocol
tags: [handoff-protocol, P02, type-builder]
tldr: "Concrete values with rationale. Validate against schema. Stay under 2048 bytes."
impact_score: 7.5
decay_rate: 0.05
satellite: edison
keywords: [handoff protocol, fire-and-forget, request-response, streaming, escalation]
---

## Summary
Handoff protocol — trigger conditions, context passed, return contract between agents. The difference between a useful handoff_protocol and a useless one is concrete values
with rationale versus placeholder text.
## Pattern
**Concrete parameters with rationale.**
Every parameter must have: name, value, and why that value was chosen.
Required body sections: Overview, Trigger, Context Transfer, Return Contract.
Body budget: 2048 bytes max.
## Anti-Pattern
- No return contract: Caller cannot validate or use result — silent type mismatch
- Passing full context: Token waste; pass only what target needs
- No timeout: Hung handoff blocks entire pipeline indefinitely
- Implicit trigger: Handoff fires on vague conditions, causing spurious delegations
## Context
The 2048-byte body limit keeps handoff_protocol artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.
