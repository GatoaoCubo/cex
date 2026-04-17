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
