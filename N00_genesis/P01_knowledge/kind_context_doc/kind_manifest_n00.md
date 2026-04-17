---
id: n00_context_doc_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Context Doc -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, context_doc, p01, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Context Doc is a domain context artifact that provides background knowledge, terminology, and situational grounding for LLM agents operating in a specific domain. Unlike knowledge_card (atomic facts), a context_doc covers a broader conceptual area. It is injected into agent prompts via F3 INJECT to reduce hallucination and improve domain alignment.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `context_doc` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Domain or topic name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| domain | string | yes | Business or technical domain covered |
| scope | enum | yes | narrow\|medium\|broad -- breadth of coverage |
| audience | string | yes | Target consumer: agent, human, both |
| key_concepts | list | yes | Core concepts defined in this context |
| related_domains | list | no | Adjacent domains for cross-reference |

## When to use
- When an agent needs domain grounding before generating outputs
- When onboarding a nucleus to a new industry vertical
- When knowledge_cards are too atomic and a broader overview is needed

## Builder
`archetypes/builders/context_doc-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind context_doc --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- agent system or human reader
- `{{DOMAIN_CONTEXT}}` -- the domain being documented

## Example (minimal)
```yaml
---
id: context_doc_saas_pricing_fundamentals
kind: context_doc
pillar: P01
nucleus: n04
title: "SaaS Pricing Fundamentals"
version: 1.0
quality: null
---
domain: SaaS pricing strategy
scope: medium
audience: agent
key_concepts: [value-based pricing, tiering, freemium, expansion revenue]
```

## Related kinds
- `knowledge_card` (P01) -- atomic facts within the context
- `glossary_entry` (P01) -- term definitions within the domain
- `ontology` (P01) -- formal taxonomy for the domain
- `edtech_vertical` (P01) -- vertical-specific context specialization
