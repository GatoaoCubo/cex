---
id: n00_reward_signal_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Reward Signal -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, reward_signal, p11, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A reward_signal is a continuous quality feedback signal emitted after each artifact build or agent action, encoding whether the outcome was positive, negative, or neutral relative to the quality target. It is the primary training signal for the CEX self-improvement loop, enabling reinforcement-style learning without explicit human labeling after the initial quality gate configuration.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `reward_signal` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| source_artifact | string | yes | ID of the artifact that generated this signal |
| nucleus | string | yes | Nucleus that produced the artifact |
| signal_type | enum | yes | positive \| negative \| neutral |
| score | float | yes | Numeric quality score (0.0-10.0) |
| delta | float | yes | Score change from previous version (+/-) |
| dimensions | object | yes | Per-dimension breakdown (D1-D5 scores) |
| timestamp | datetime | yes | When signal was generated |

## When to use
- After every F7 GOVERN quality assessment in the 8F pipeline
- When building reward datasets for fine-tuning or RLHF training data
- When feeding the self_improvement_loop with actionable quality signals

## Builder
`archetypes/builders/reward_signal-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind reward_signal --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rs_n03_agent_card_001
kind: reward_signal
pillar: P11
nucleus: n03
title: "Example Reward Signal"
version: 1.0
quality: null
---
# Reward Signal: N03 Agent Card Build
source_artifact: agent_card_n05
signal_type: positive
score: 9.2
delta: +0.4
dimensions: {structural: 9.5, rubric: 9.0, semantic: 9.1}
```

## Related kinds
- `quality_gate` (P11) -- gate evaluation that produces this reward signal
- `learning_record` (P10) -- learning derived from this reward signal
- `self_improvement_loop` (P11) -- loop that consumes reward signals for evolution
