---
id: n00_few_shot_example_manifest
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "Few-Shot Example -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, few_shot_example, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_few_shot_example
  - bld_schema_multimodal_prompt
  - bld_schema_kind
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_prompt_technique
  - bld_schema_thinking_config
  - bld_collaboration_few_shot_example
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Few-Shot Example is a structured input/output demonstration pair used to guide LLM behavior through in-context learning. Each artifact captures one high-quality example of a task being performed correctly, annotated with reasoning. Injected into prompts via F3 INJECT, few-shot examples improve output format compliance and reduce hallucination.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `few_shot_example` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Task name this example demonstrates |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| task_kind | string | yes | The kind being demonstrated |
| input | string | yes | Example input (user request or data) |
| output | string | yes | Ideal output for this input |
| reasoning | string | no | Chain-of-thought annotation |
| difficulty | enum | no | easy\|medium\|hard |

## When to use
- When a builder needs demonstration examples for a new task type
- When output format compliance is low and examples would help
- When building prompt templates that require concrete demonstrations

## Builder
`archetypes/builders/few_shot_example-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind few_shot_example --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- the builder or prompt that will consume this
- `{{DOMAIN_CONTEXT}}` -- task domain and expected output format

## Example (minimal)
```yaml
---
id: few_shot_example_knowledge_card_creation
kind: few_shot_example
pillar: P01
nucleus: n04
title: "Knowledge Card Creation Example"
version: 1.0
quality: null
---
task_kind: knowledge_card
input: "Document the CEX 8F pipeline"
output: |
  ---
  id: kc_8f_pipeline
  kind: knowledge_card
  ...
  ---
  8F is a universal 8-function pipeline: F1 CONSTRAIN -> F8 COLLABORATE.
reasoning: "Frontmatter first, then atomic fact with density >= 0.85"
difficulty: medium
```

## Related kinds
- `knowledge_card` (P01) -- what this example demonstrates creating
- `prompt_template` (P03) -- template that includes few-shot examples
- `dataset_card` (P01) -- when aggregating many examples into a dataset

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_dataset_card]] | downstream | 0.43 |
| [[bld_schema_reranker_config]] | downstream | 0.42 |
| [[bld_schema_few_shot_example]] | downstream | 0.42 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.41 |
| [[bld_schema_kind]] | downstream | 0.40 |
| [[bld_schema_integration_guide]] | downstream | 0.39 |
| [[bld_schema_usage_report]] | downstream | 0.39 |
| [[bld_schema_prompt_technique]] | downstream | 0.39 |
| [[bld_schema_thinking_config]] | downstream | 0.39 |
| [[bld_collaboration_few_shot_example]] | downstream | 0.39 |
