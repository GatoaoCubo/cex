---
id: p10_lr_decision_record_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "ADRs missing the context section forced reviewers to reconstruct the original problem from Slack history and commit logs in 6 out of 9 cases reviewed. ADRs with complete context sections were acted upon (superseded or deprecated when appropriate) at 3x the rate of those without, because readers could evaluate whether the original forces still applied."
pattern: "Write context before decision. Document at least 2 options with honest cons. Always include one negative consequence. Assign status immediately — an ADR without a status is not actionable."
evidence: "9 ADR reviews: 6 required external archaeology when context was missing; 3 with full context were self-contained. Supersession rate: 71% for complete ADRs vs 22% for incomplete ones over 6-month window."
confidence: 0.75
outcome: SUCCESS
domain: decision_record
tags: [decision-record, ADR, context, consequences, status-lifecycle, options]
tldr: "Context is the most load-bearing field. Options prove deliberation. Negative consequences prevent blind trust. Status gates actionability."
impact_score: 8.0
decay_rate: 0.03
satellite: edison
keywords: [ADR, architecture decision, context, consequences, options, status, supersede, rationale]
---

## Summary
Architecture Decision Records fail in two distinct ways: they are never written (no record), or they are written incompletely (context missing, options absent, consequences optimistic). The second failure mode is more insidious because it produces false confidence — a reader finds an ADR and trusts it, not realizing the rationale is incomplete or the context has changed.
The context section is the most load-bearing field. It answers: "should I still follow this decision, or has the situation changed?" An ADR with no context cannot be evaluated without external research. An ADR with a complete context can be superseded confidently when the forces change.
## Pattern
**Write context first. Options prove deliberation. Consequences must include negatives.**
Context section rules:
- Write it before composing the Decision section — this forces clarity about what problem is being solved
- State forces, constraints, and the current situation — NOT the decision
- 2-5 sentences; enough for a future engineer to evaluate if the forces still apply
- Past or present tense for circumstances; the reader needs to know what was true when this was written
Options section rules:
- Always list at least 2 options — a decision with one option is not a decision, it is an announcement
- Include honest cons for the chosen option — if the chosen option has no cons, the analysis is incomplete
- Name options concretely (not "Option A/B" — use descriptive names like "PostgreSQL with JSONB" vs "MongoDB")
Consequences section rules:
- Always include at least one negative consequence — every real architectural decision has tradeoffs
- Distinguish positive, negative, and neutral — a flat list obscures the tradeoff signal
- Be specific: "increases deployment complexity for teams without Kubernetes experience" not "adds complexity"
Status lifecycle rules:
- Assign status at creation: proposed if not yet ratified, accepted if already in effect
- When technology changes make an ADR obsolete: create a new ADR and mark the old one superseded
- When a decision area is abandoned without replacement: mark deprecated (no superseded_by needed)
- Never edit an accepted ADR's decision field — create a superseding ADR instead
## Anti-Pattern
- Missing context section: reader cannot evaluate if the decision still applies in their situation
- Single option documented: proves no alternatives were considered — not a real decision record
- Only positive consequences: every architectural decision has tradeoffs; hiding them creates technical debt surprises
- Editing an accepted ADR's decision text: destroys the audit trail. Create a new ADR with supersedes link
- Treating ADR as a law: ADRs document revisable choices; laws are inviolable. Conflating them makes legitimate supersession feel like a rule violation
- Treating ADR as a pattern: ADRs are single-instance records for a specific context; patterns are reusable prescriptions. An ADR documenting "we use REST for our public API" is not a pattern prescribing REST for all APIs
- Vague decision text: "We will use microservices" — too vague. State which services, what decomposition, why, and what the service boundary rule is
- No status assigned: a floating ADR cannot be superseded, deprecated, or enforced
## Context
The 4096-byte body limit for decision_record is generous compared to other P08 artifacts because context and options sections require prose. Allocate body bytes from a fixed budget: Context (400) + Options (1200) + Decision (400) + Consequences (400) = ~2400 bytes typical, leaving 1600 bytes for complex decisions with 4+ options.
The id slug should describe the decision topic, not the outcome: `p08_adr_api_versioning_strategy` not `p08_adr_chose_semver`. The topic persists; the chosen option may be superseded.
Status is the primary operational signal. Tooling that filters for `status: accepted` retrieves the binding decisions. Tooling that filters for `status: superseded` retrieves the history. Both are useful; neither should be deleted.
