---
id: n00_tagline_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Tagline -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, tagline, p03, n00, archetype, template]
density_score: 0.98
related:
  - bld_schema_tagline
  - bld_collaboration_tagline
  - tagline-builder
  - bld_tools_tagline
  - bld_knowledge_card_tagline
  - bld_output_template_tagline
  - kc_tagline
  - bld_memory_tagline
  - bld_quality_gate_tagline
  - bld_system_prompt_tagline
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A tagline is a short, memorable phrase that captures the essence of a brand, product, or campaign in a single sentence or fragment. It distills the brand's core value proposition, emotional resonance, and differentiation into the fewest possible words. The output is a set of tagline variants with rationale, tested against brand voice and target audience criteria.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `tagline` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| tagline_text | string | yes | The primary tagline candidate |
| variants | list | no | Alternative tagline options ranked by score |
| brand_alignment | string | no | Explanation of how it reflects brand values |
| max_words | integer | no | Word limit constraint applied during generation |

## When to use
- When N02 Marketing needs a campaign or product tagline anchored to brand voice
- When a brand_config.yaml is being populated with the brand's core messaging
- When A/B testing messaging variants for landing pages or ad campaigns

## Builder
`archetypes/builders/tagline-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind tagline --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: tl_cex_main_2026
kind: tagline
pillar: P03
nucleus: n02
title: "CEX Main Tagline 2026"
version: 1.0
quality: null
---
tagline_text: "The enterprise brain that scales with you."
max_words: 8
brand_alignment: "Reflects composability, sovereignty, and self-assimilation pillars"
variants:
  - "Build once. Know everything."
  - "Your AI. Your rules. Your growth."
```

## Related kinds
- `prompt_template` (P03) -- templates used to generate tagline variants at scale
- `landing_page` (P05) -- primary deployment surface for the tagline artifact
- `brand_voice` (P01) -- knowledge card that constrains tagline tone and vocabulary
- `content_monetization` (P11) -- commercial context that taglines must support

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_tagline]] | downstream | 0.55 |
| [[bld_collaboration_tagline]] | downstream | 0.46 |
| [[tagline-builder]] | related | 0.45 |
| [[bld_tools_tagline]] | downstream | 0.44 |
| [[bld_knowledge_card_tagline]] | sibling | 0.40 |
| [[bld_output_template_tagline]] | downstream | 0.38 |
| [[kc_tagline]] | sibling | 0.38 |
| [[bld_memory_tagline]] | downstream | 0.38 |
| [[bld_quality_gate_tagline]] | downstream | 0.38 |
| [[bld_system_prompt_tagline]] | related | 0.37 |
