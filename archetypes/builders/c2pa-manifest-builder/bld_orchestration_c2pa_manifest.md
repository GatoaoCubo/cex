---
kind: collaboration
id: bld_collaboration_c2pa_manifest
pillar: P12
llm_function: COLLABORATE
purpose: How c2pa_manifest-builder works in crews with other builders
quality: 8.9
title: "Collaboration C2PA Manifest"
version: "1.0.0"
author: n04_wave7
tags: [c2pa_manifest, builder, collaboration, C2PA, Adobe, provenance]
tldr: "How c2pa_manifest-builder works in crews with other builders"
domain: "c2pa_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_vc_credential
  - c2pa-manifest-builder
  - bld_knowledge_card_c2pa_manifest
  - p03_sp_c2pa_manifest_builder
  - bld_architecture_kind
  - bld_architecture_c2pa_manifest
  - kind-builder
  - kc_c2pa_manifest
  - p10_lr_c2pa_manifest_builder
  - bld_tools_c2pa_manifest
---

## Crew Role
Attaches C2PA 2.3 content credentials to AI-generated media, building signed provenance chains that survive distribution and enable content authenticity verification at any downstream point.

## Receives From
| Builder               | What                                  | Format      |
|-----------------------|---------------------------------------|-------------|
| model-card-builder    | AI model name, version, training info | YAML        |
| vc-credential-builder | Issuer identity credential            | JSON-LD     |
| N02 marketing nucleus | Generated content + prompt text       | Binary/text |
| N03 builder nucleus   | Generation parameters                 | YAML        |

## Produces For
| Builder               | What                                  | Format      |
|-----------------------|---------------------------------------|-------------|
| Content distribution  | Media file + embedded C2PA manifest   | Binary      |
| CAI verify portal     | Manifest JSON for verification        | JSON        |
| compliance-framework  | Provenance attestation record         | JSON        |
| audit trail           | Signed generation evidence            | JSON        |

## Boundary
Does NOT handle: camera capture manifests (different COSE signing flow), document signing (use separate kind), copyright licensing (use license artifact), or W3C VC agent identity (use vc-credential-builder). C2PA manifest is content-bound, not agent-bound.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_vc_credential]] | sibling | 0.38 |
| [[c2pa-manifest-builder]] | upstream | 0.35 |
| [[bld_knowledge_card_c2pa_manifest]] | upstream | 0.31 |
| [[p03_sp_c2pa_manifest_builder]] | upstream | 0.30 |
| [[bld_architecture_kind]] | upstream | 0.28 |
| [[bld_architecture_c2pa_manifest]] | upstream | 0.28 |
| [[kind-builder]] | upstream | 0.28 |
| [[kc_c2pa_manifest]] | upstream | 0.27 |
| [[p10_lr_c2pa_manifest_builder]] | upstream | 0.26 |
| [[bld_tools_c2pa_manifest]] | upstream | 0.24 |
