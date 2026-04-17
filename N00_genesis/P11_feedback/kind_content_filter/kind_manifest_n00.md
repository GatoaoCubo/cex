---
id: n00_content_filter_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Content Filter -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, content_filter, p11, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A content_filter defines the input/output content filtering pipeline configuration, specifying which hazard categories are blocked, the filtering model, thresholds, and fallback behavior. It is the first and last line of defense ensuring that both user inputs and agent outputs conform to safety and content policy requirements before reaching or leaving the system.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `content_filter` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| filter_scope | enum | yes | input \| output \| both |
| hazard_categories | array | yes | Categories to filter (violence, hate, sexual, self-harm, etc.) |
| filter_model | string | yes | Model used for filtering (e.g. llama_guard_3) |
| block_threshold | float | yes | Score above which content is blocked (0.0-1.0) |
| fallback_action | enum | yes | block \| redact \| flag_for_review \| allow_with_warning |
| audit_blocked | boolean | yes | Whether blocked content is logged to audit_log |

## When to use
- When deploying a customer-facing CEX nucleus with public user input
- When building content pipelines for regulated industries (healthcare, finance, children)
- When implementing EU AI Act prohibited practices filtering (Article 5)

## Builder
`archetypes/builders/content_filter-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind content_filter --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cf_n02_marketing_output_filter
kind: content_filter
pillar: P11
nucleus: n02
title: "Example Content Filter"
version: 1.0
quality: null
---
# Content Filter: N02 Marketing Output
filter_scope: output
hazard_categories: [hate, deception, violence]
filter_model: llama_guard_3
block_threshold: 0.7
fallback_action: flag_for_review
audit_blocked: true
```

## Related kinds
- `guardrail` (P11) -- higher-level safety boundary that content_filter implements
- `safety_hazard_taxonomy` (P11) -- taxonomy defining the hazard categories referenced
- `hitl_config` (P11) -- human review flow triggered when content is flagged
