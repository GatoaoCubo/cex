---
kind: collaboration
id: bld_collaboration_vc_credential
pillar: P12
llm_function: COLLABORATE
purpose: How vc_credential-builder works in crews with other builders
quality: 8.9
title: "Collaboration VC Credential"
version: "1.0.0"
author: n04_wave7
tags: [vc_credential, builder, collaboration, W3C, DID, issuer]
tldr: "How vc_credential-builder works in crews with other builders"
domain: "vc_credential construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_agent
  - bld_collaboration_c2pa_manifest
  - bld_architecture_kind
  - bld_collaboration_model_card
  - vc-credential-builder
  - kind-builder
  - agent-builder
  - bld_collaboration_agent_computer_interface
  - bld_collaboration_system_prompt
  - bld_collaboration_role_assignment
---

## Crew Role
Issues cryptographically verifiable identity and provenance credentials for AI agents, binding agent personas to claims that external verifiers can check without contacting the issuer.

## Receives From
| Builder             | What                              | Format      |
|---------------------|-----------------------------------|-------------|
| agent-builder (P02) | Agent DID and capability profile  | YAML        |
| model-card-builder  | Model training provenance claims  | Markdown    |
| compliance-framework-builder | Regulatory claim definitions | YAML  |
| N07 orchestrator    | Issuance request + issuer DID key | JSON        |

## Produces For
| Builder              | What                                | Format      |
|----------------------|-------------------------------------|-------------|
| agent-builder (P02)  | Issued VC for agent credential store| JSON-LD     |
| c2pa-manifest-builder | Issuer VC for content credential chain | JSON-LD |
| audit-trail system   | Verifiable provenance record        | JSON-LD     |
| external API gateway | Trust token for cross-domain auth   | JSON-LD     |

## Boundary
Does NOT handle: Verifiable Presentations (aggregated VC envelope), DID document construction, JWT-encoded VCs (vc-jose-cose profile), or API key authentication (use secret_config). DID resolution is an external tool call, not produced by this builder.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent]] | sibling | 0.35 |
| [[bld_collaboration_c2pa_manifest]] | sibling | 0.35 |
| [[bld_architecture_kind]] | upstream | 0.31 |
| [[bld_collaboration_model_card]] | sibling | 0.30 |
| [[vc-credential-builder]] | upstream | 0.29 |
| [[kind-builder]] | upstream | 0.29 |
| [[agent-builder]] | upstream | 0.29 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.28 |
| [[bld_collaboration_system_prompt]] | sibling | 0.28 |
| [[bld_collaboration_role_assignment]] | sibling | 0.27 |
