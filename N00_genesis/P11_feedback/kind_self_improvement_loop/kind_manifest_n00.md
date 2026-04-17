---
id: n00_self_improvement_loop_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Self Improvement Loop -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, self_improvement_loop, p11, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A self_improvement_loop defines the agent or system self-evolution mechanism that continuously improves artifact quality, agent capabilities, or system performance over time by cycling through measure, improve, evaluate, and retain phases. It is the engine behind `cex_evolve.py` and the overnight improvement pipeline, turning reward signals into lasting quality gains.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `self_improvement_loop` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_scope | array | yes | Kinds or artifacts targeted for improvement |
| improvement_strategy | enum | yes | heuristic \| llm_agent \| hybrid |
| quality_threshold | float | yes | Artifacts below this score are candidates for improvement |
| keep_threshold | float | yes | Improved artifact must exceed this to replace original |
| cycle_budget_tokens | integer | yes | Maximum tokens per improvement cycle |
| max_cycles | integer | yes | Maximum improvement cycles before stopping |
| feedback_sources | array | yes | Sources driving improvement (reward_signal, learning_record, nps_survey) |

## When to use
- When running overnight quality improvement on artifacts below 9.0
- When building an autonomous quality flywheel for a specific nucleus
- When configuring `cex_evolve.py` with custom improvement parameters

## Builder
`archetypes/builders/self_improvement_loop-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind self_improvement_loop --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sil_overnight_quality_sweep
kind: self_improvement_loop
pillar: P11
nucleus: n07
title: "Example Self Improvement Loop"
version: 1.0
quality: null
---
# Self Improvement Loop: Overnight Quality Sweep
target_scope: [knowledge_card, agent_card]
improvement_strategy: hybrid
quality_threshold: 9.0
keep_threshold: 8.5
max_cycles: 1302
feedback_sources: [reward_signal, learning_record]
```

## Related kinds
- `reward_signal` (P11) -- primary feedback driving this loop
- `optimizer` (P11) -- optimizer that this loop may invoke for metric improvement
- `bugloop` (P11) -- sub-loop for code defect correction within the improvement cycle
