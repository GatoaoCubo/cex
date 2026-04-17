---
id: n00_prompt_technique_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Prompt Technique -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, prompt_technique, p03, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A prompt_technique documents a specific prompting method or pattern (few-shot, chain-of-thought, role prompting, self-consistency) with canonical examples, applicability conditions, and expected quality impact. It serves as a reusable knowledge artifact injected during F3 INJECT to inform how builders construct their prompts. The output is a structured technique card that nuclei can reference when choosing how to elicit optimal model behavior.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `prompt_technique` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| technique_name | string | yes | Canonical name (few-shot, CoT, role, self-consistency) |
| when_to_apply | list | yes | Conditions under which this technique outperforms alternatives |
| example | string | yes | Minimal canonical example of the technique in use |
| quality_impact | string | no | Expected improvement on which quality dimension |

## When to use
- When injecting prompting knowledge into a builder that is constructing system_prompts or templates
- When documenting a newly discovered prompting pattern for reuse across nuclei
- When the F3 INJECT step needs technique recommendations based on task type

## Builder
`archetypes/builders/prompt_technique-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind prompt_technique --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: pt_few_shot_structured_output
kind: prompt_technique
pillar: P03
nucleus: n04
title: "Few-Shot Structured Output Technique"
version: 1.0
quality: null
---
technique_name: few-shot
when_to_apply:
  - "Output must follow strict schema"
  - "Model has not seen the format in training data"
example: |
  Input: customer complaint
  Output: {"sentiment": "negative", "category": "billing", "urgency": "high"}
quality_impact: "Reduces format errors by ~60% on structured output tasks"
```

## Related kinds
- `reasoning_strategy` (P03) -- higher-level strategy that selects prompt_techniques
- `prompt_template` (P03) -- artifact that embeds prompt_technique patterns
- `prompt_optimizer` (P03) -- tool that tests and ranks prompt_techniques empirically
- `knowledge_card` (P01) -- the KC format used to store prompt_technique knowledge
