---
id: n00_memory_summary_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Memory Summary -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, memory_summary, p10, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A memory_summary is a compressed, distilled representation of a longer context or session history. It preserves the high-signal content from a large context window into a compact form that can be injected into future sessions, bridging the gap between what happened and what the model needs to know to continue effectively.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `memory_summary` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| source_session | string | yes | Session or context window being summarized |
| original_tokens | integer | yes | Token count of original context |
| summary_tokens | integer | yes | Token count of this summary |
| compression_ratio | float | yes | original_tokens / summary_tokens |
| key_decisions | array | yes | Critical decisions preserved verbatim |
| key_artifacts | array | no | IDs of artifacts produced in the summarized period |
| generated_at | datetime | yes | When this summary was created |

## When to use
- After /compact to persist what was in the pre-compact context
- When handing off a session to another nucleus that needs history
- When archiving a completed mission wave for future reference

## Builder
`archetypes/builders/memory_summary-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind memory_summary --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ms_n07_wave3_summary
kind: memory_summary
pillar: P10
nucleus: n07
title: "Example Memory Summary"
version: 1.0
quality: null
---
# Wave 3 Session Summary
source_session: wave3_2026_04_17
original_tokens: 180000
summary_tokens: 4200
compression_ratio: 42.8
key_decisions: ["Used hybrid routing", "N03 produced 7 artifacts"]
```

## Related kinds
- `compression_config` (P10) -- config that drove the compression producing this summary
- `session_state` (P10) -- session snapshot that may have been the compression source
- `handoff` (P12) -- may embed a memory_summary for cross-nucleus context transfer
