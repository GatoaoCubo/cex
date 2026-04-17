---
id: n00_model_registry_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Model Registry -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, model_registry, p10, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A model_registry tracks the versioning, lineage, and artifact metadata of LLM models and fine-tuned checkpoints used in the CEX system. It is the governance record that ensures reproducibility by linking model versions to the training data, evaluation results, and deployment configurations that produced them.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `model_registry` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| model_id | string | yes | Canonical model identifier (e.g. claude-sonnet-4-6) |
| provider | string | yes | Model provider (anthropic \| openai \| google \| local) |
| context_window | integer | yes | Maximum context tokens |
| training_cutoff | date | yes | Knowledge cutoff date |
| benchmark_scores | object | no | Key benchmark results (MMLU, HumanEval, etc.) |
| deployment_status | enum | yes | active \| deprecated \| experimental |
| successor_model | string | no | Model ID that replaces this one |

## When to use
- When adding a new model to the CEX routing table
- When deprecating an old model and tracking its replacement
- When producing a compliance report that requires model version provenance

## Builder
`archetypes/builders/model_registry-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind model_registry --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: mr_claude_sonnet_4_6
kind: model_registry
pillar: P10
nucleus: n07
title: "Example Model Registry Entry"
version: 1.0
quality: null
---
# Model: claude-sonnet-4-6
provider: anthropic
context_window: 200000
training_cutoff: 2025-08-01
deployment_status: active
```

## Related kinds
- `model_provider` (P02) -- provider configuration that this registry entry belongs to
- `fallback_chain` (P02) -- routing chain that references registry entries
- `agent_grounding_record` (P10) -- inference records citing specific model versions
