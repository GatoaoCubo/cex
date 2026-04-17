---
id: n00_research_pipeline_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Research Pipeline -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, research_pipeline, p04, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A research_pipeline is a 7-stage deep research engine that systematically converts a research intent into a verified, cited intelligence artifact. The stages are: INTENT -> PLAN -> RETRIEVE -> RESOLVE -> SCORE -> SYNTHESIZE -> VERIFY. Each stage is a discrete tool call or LLM step, ensuring research is reproducible, source-tracked, and quality-gated. The output is a high-density knowledge artifact with confidence scores and full provenance.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `research_pipeline` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| domain | string | yes | Research domain (e.g., competitive_analysis, market_sizing) |
| source_types | list | yes | Permitted source types: web, local_kb, database, api |
| min_sources | integer | yes | Minimum sources required before SYNTHESIZE stage |
| output_kind | string | yes | Target artifact kind for synthesized output |

## When to use
- When N01 Intelligence is executing competitive, market, or technical deep research
- When a knowledge_card requires external sources that must be retrieved and verified
- When the user asks for research that spans multiple sources requiring citation and synthesis

## Builder
`archetypes/builders/research_pipeline-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind research_pipeline --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rp_competitor_pricing_edtech
kind: research_pipeline
pillar: P04
nucleus: n01
title: "EdTech Competitor Pricing Research"
version: 1.0
quality: null
---
domain: competitive_analysis
source_types: [web, local_kb]
min_sources: 6
output_kind: knowledge_card
```

## Related kinds
- `search_tool` (P04) -- web search tool used in the RETRIEVE stage
- `retriever` (P04) -- vector retriever used for local_kb sources in RETRIEVE stage
- `document_loader` (P04) -- document ingestion used in RESOLVE stage
- `knowledge_card` (P01) -- primary output artifact of research_pipeline SYNTHESIZE stage
