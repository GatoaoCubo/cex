---
id: n00_gpai_technical_doc_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "GPAI Technical Doc -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, gpai_technical_doc, p11, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A gpai_technical_doc is the EU AI Act General Purpose AI technical documentation required under Annex XI and Article 53, documenting training data, compute used, evaluation results, capabilities and limitations, and copyright compliance measures. It is mandatory for GPAI model providers making their models available in the EU market.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `gpai_technical_doc` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| model_name | string | yes | GPAI model identifier |
| training_data_desc | string | yes | Description of training data sources and filtering |
| compute_resources | object | yes | Training compute (FLOP, hardware, duration) |
| evaluation_results | array | yes | Benchmark results and evaluation methodology |
| known_limitations | array | yes | Documented capability limitations and failure modes |
| copyright_policy | string | yes | Text summarizing copyright compliance measures |
| systemic_risk | boolean | yes | Whether model exceeds 10^25 FLOP threshold |

## When to use
- When releasing a GPAI model or GPAI-based system in EU markets
- When a CEX deployment incorporates a third-party GPAI model requiring documentation
- When preparing for EU AI Office compliance review of GPAI capabilities

## Builder
`archetypes/builders/gpai_technical_doc-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind gpai_technical_doc --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: gpai_doc_claude_sonnet_4_6
kind: gpai_technical_doc
pillar: P11
nucleus: n07
title: "Example GPAI Technical Doc"
version: 1.0
quality: null
---
# GPAI Technical Documentation: claude-sonnet-4-6
model_name: claude-sonnet-4-6
systemic_risk: false
training_data_desc: "Pre-training on diverse internet + books + code; filtered for safety"
copyright_policy: "Anthropic responsible scaling policy + copyright compliance program"
```

## Related kinds
- `conformity_assessment` (P11) -- Annex IV assessment complementing GPAI docs
- `compliance_framework` (P11) -- EU AI Act framework this doc operates within
- `model_registry` (P10) -- model versioning record linked to this documentation
