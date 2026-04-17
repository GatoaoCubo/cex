---
id: n00_llm_evaluation_scenario_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Llm Evaluation Scenario -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, llm_evaluation_scenario, p07, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
LLM evaluation scenario defines a HELM (Stanford CRFM) compatible evaluation scenario specification for a capability or domain. It covers scenario taxonomy (task, subject, language), prompt adaptation, metric selection, and reproducibility metadata. Scenarios enable benchmarking CEX nucleus outputs against the HELM leaderboard or running custom HELM-style evaluations for domain-specific capabilities.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `llm_evaluation_scenario` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Capability name + "HELM Scenario" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| helm_scenario_name | string | yes | HELM canonical scenario identifier |
| task_type | enum | yes | qa / summarization / classification / generation / reasoning |
| subject | string | yes | Domain or subject area |
| prompt_format | string | yes | Prompt template following HELM conventions |
| metrics | list | yes | HELM metrics used (exact_match, f1, rouge, etc.) |
| num_instances | int | yes | Number of instances in the scenario |

## When to use
- Benchmarking a CEX nucleus against HELM-standardized tasks for reproducibility
- Adding a custom capability domain to the HELM evaluation framework
- Publishing comparable results to the broader LLM research community

## Builder
`archetypes/builders/llm_evaluation_scenario-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind llm_evaluation_scenario --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence defines; compares across providers
- `{{SIN_LENS}}` -- Analytical Envy: standardized, reproducible, publicly comparable
- `{{TARGET_AUDIENCE}}` -- ML researchers and engineers comparing model capabilities
- `{{DOMAIN_CONTEXT}}` -- capability domain, benchmark suite context, comparison models

## Example (minimal)
```yaml
---
id: llm_evaluation_scenario_cex_intent_resolution
kind: llm_evaluation_scenario
pillar: P07
nucleus: n01
title: "CEX Intent Resolution -- HELM Scenario"
version: 1.0
quality: null
---
helm_scenario_name: cex_intent_resolution_v1
task_type: classification
subject: "AI orchestration intent mapping"
metrics: [exact_match, f1]
num_instances: 500
```

## Related kinds
- `eval_framework` (P07) -- framework that runs HELM scenarios
- `eval_dataset` (P07) -- data used to populate the scenario instances
- `benchmark` (P07) -- wraps the scenario in a broader performance measurement
