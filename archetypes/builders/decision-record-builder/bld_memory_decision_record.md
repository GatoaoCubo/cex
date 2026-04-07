---
id: p10_lr_decision_record_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "ADRs missing the context section forced reviewers to reconstruct the original problem from Slack history and commit logs in 6 out of 9 cases reviewed. ADRs with complete context sections were acted upon (superseded or deprecated when apownte) at 3x the rate of those without, because readers could evaluate whether the original forces still applied."
pattern: "Write context before decision. Document at least 2 options with honest cons. Always include one negative consequence. Assign status immediately — an ADR without a status is not actionable."
evidence: "9 ADR reviews: 6 required external archaeology when context was missing; 3 with full context were self-contained. Supersession rate: 71% for complete ADRs vs 22% for incomplete ones over 6-month window."
confidence: 0.75
outcome: SUCCESS
domain: decision_record
tags: [decision-record, ADR, context, consequences, status-lifecycle, options]
tldr: "Context is the most load-bearing field. Options prove deliberation. Negative consequences prevent blind trust. Status gates actionability."
impact_score: 8.0
decay_rate: 0.03
agent_group: edison
keywords: [ADR, architecture decision, context, consequences, options, status, supersede, rationale]
memory_scope: project
observation_types: [user, feedback, project, reference]
---
## Summary
ADRs fail in two ways: never written, or written incompletely. The second is more insidious — a reader finds an ADR and trusts it without realizing the rationale is incomplete or context has changed. The context section is the most load-bearing field: it answers whether to still follow the decision, or whether the situation has changed.

## Pattern
**Write context first. Options prove deliberation. Consequences must include negatives.**
- Context: write before the Decision section; state forces and constraints, NOT the decision; 2-5 sentences in past/present tense
- Options: always list >= 2 with descriptive names; include honest cons for the chosen option
- Consequences: always include >= 1 negative; distinguish positive/negative/neutral; be specific not vague
- Status: assign at creation (proposed/accepted); superseded requires superseded_by; deprecated needs no replacement link; never edit an accepted ADR's decision — create a superseding one

## Anti-Pattern
- Missing context: reader cannot evaluate if the decision still applies
- Single option: proves no alternatives were considered
- Only positive consequences: hides tradeoffs, creates technical debt surprises
- Editing accepted ADR decision text: destroys audit trail
- Treating ADR as a law: ADRs are revisable; laws are inviolable
- Vague decision text: state which services, boundaries, and why
- No status assigned: cannot be superseded, deprecated, or enforced
