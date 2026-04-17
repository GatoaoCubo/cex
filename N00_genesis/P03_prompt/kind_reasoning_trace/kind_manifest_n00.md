---
id: n00_reasoning_trace_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Reasoning Trace -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, reasoning_trace, p03, n00, archetype, template]
density_score: 0.98
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A reasoning_trace is a structured chain-of-thought reasoning record with confidence scores at each step, capturing the intermediate reasoning steps an agent used to arrive at its conclusion. It provides auditability, enables regression analysis when conclusions degrade, and serves as training data for fine-tuning. The output is a structured log of the agent's reasoning process with explicit confidence annotations and conclusion derivation.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `reasoning_trace` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| task_id | string | yes | ID of the task this trace was produced for |
| steps | list | yes | Ordered reasoning steps with step_text and confidence |
| conclusion | string | yes | Final conclusion derived from the reasoning chain |
| strategy_used | string | no | ID of the reasoning_strategy that generated this trace |

## When to use
- When an agent must produce auditable reasoning for governance or compliance review
- When capturing reasoning output to use as fine-tuning signal for smaller models
- When debugging why an agent reached an incorrect conclusion by inspecting step-level confidence

## Builder
`archetypes/builders/reasoning_trace-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind reasoning_trace --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rt_competitor_pricing_analysis_20260415
kind: reasoning_trace
pillar: P03
nucleus: n01
title: "Competitor Pricing Analysis Trace"
version: 1.0
quality: null
---
task_id: t_edtech_pricing_research
strategy_used: rs_cot_analysis_n01
steps:
  - step: 1
    text: "Identified 6 EdTech SaaS competitors from market scan"
    confidence: 0.92
  - step: 2
    text: "Extracted pricing tiers from public pages"
    confidence: 0.85
conclusion: "Median price point is $49/mo; 4/6 use feature-gated tiers"
```

## Related kinds
- `reasoning_strategy` (P03) -- strategy that produced this trace
- `learning_record` (P11) -- longer-term learning derived from reasoning_trace analysis
- `benchmark` (P07) -- uses reasoning_traces to evaluate model reasoning quality
- `knowledge_card` (P01) -- distilled knowledge extracted from high-confidence traces
