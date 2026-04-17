---
id: n00_c2pa_manifest_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "C2PA Manifest -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, c2pa_manifest, p10, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A c2pa_manifest is a C2PA 2.3 content credential that cryptographically attests the provenance and modification history of AI-generated media. It embeds a tamper-evident chain of custody directly into the media artifact, enabling downstream consumers to verify authenticity and identify AI involvement.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `c2pa_manifest` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| c2pa_version | string | yes | C2PA spec version (e.g. "2.3") |
| claim_generator | string | yes | Software that generated the manifest |
| assertions | array | yes | List of C2PA assertions (ai.generated, c2pa.actions, etc.) |
| signature_info | object | yes | Certificate and signing timestamp |
| media_hash | string | yes | SHA-256 or similar hash of bound media |
| ingredient_refs | array | no | References to parent media manifests |

## When to use
- When publishing AI-generated images, audio, or video that must carry provenance
- When building pipelines that comply with content authenticity standards (CAI, C2PA)
- When downstream consumers need to verify whether media was AI-generated

## Builder
`archetypes/builders/c2pa_manifest-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind c2pa_manifest --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: c2pa_n02_campaign_img_001
kind: c2pa_manifest
pillar: P10
nucleus: n02
title: "Example C2PA Manifest"
version: 1.0
quality: null
---
# C2PA Content Credential
c2pa_version: "2.3"
claim_generator: "CEX/1.0"
assertions: [ai.generated, c2pa.actions.placed]
media_hash: "sha256:abc123..."
```

## Related kinds
- `vc_credential` (P10) -- W3C Verifiable Credential for agent identity, complementary provenance layer
- `agent_grounding_record` (P10) -- per-inference provenance that feeds into the manifest
- `audit_log` (P11) -- immutable log referencing manifests for compliance
