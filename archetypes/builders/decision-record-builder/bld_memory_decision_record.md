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
quality: 9.1
title: "Memory Decision Record"
density_score: 0.90
llm_function: INJECT
---
## Summary
ADRs fail in two ways: never written, or written incompletely. The second is more insidious — a reader finds an ADR and trusts it without realizing the rationale is incomplete or context has changed. The context section is the most load-bearing field: it answers whether to still follow the decision, or whether the situation has changed.

## Pattern
**Write context first. Options prove deliberation. Consequences must include negatives.**
1. Context: write before the Decision section; state forces and constraints, NOT the decision; 2-5 sentences in past/present tense
2. Options: always list >= 2 with descriptive names; include honest cons for the chosen option
3. Consequences: always include >= 1 negative; distinguish positive/negative/neutral; be specific not vague
4. Status: assign at creation (proposed/accepted); superseded requires superseded_by; deprecated needs no replacement link; never edit an accepted ADR's decision — create a superseding one

## Anti-Pattern
1. Missing context: reader cannot evaluate if the decision still applies
2. Single option: proves no alternatives were considered
3. Only positive consequences: hides tradeoffs, creates technical debt surprises
4. Editing accepted ADR decision text: destroys audit trail
5. Treating ADR as a law: ADRs are revisable; laws are inviolable
6. Vague decision text: state which services, boundaries, and why
7. No status assigned: cannot be superseded, deprecated, or enforced

## Metadata

```yaml
id: p10_lr_decision_record_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-decision-record-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | decision_record |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
