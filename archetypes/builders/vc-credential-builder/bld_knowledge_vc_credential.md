---
kind: knowledge_card
id: bld_knowledge_card_vc_credential
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for vc_credential production
quality: 9.2
title: "Knowledge Card VC Credential"
version: "1.0.0"
author: n04_wave7
tags: [vc_credential, builder, knowledge_card, W3C, verifiable-credential, VC-2.0, DID, issuer, subject, proof, data-integrity, credentialSchema, refreshService]
tldr: "Domain knowledge for vc_credential production"
domain: "vc_credential construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_vc_credential_builder
  - vc-credential-builder
  - bld_tools_vc_credential
  - bld_instruction_vc_credential
  - p10_lr_vc_credential_builder
  - kc_vc_credential
  - bld_collaboration_vc_credential
  - p10_qg_vc_credential
  - bld_examples_vc_credential
  - bld_schema_vc_credential
---

## Domain Overview
W3C Verifiable Credentials 2.0 (May 2025 REC) provides a standard data model for expressing credentials in a cryptographically verifiable, machine-readable format. In AI agent ecosystems, VCs enable decentralized identity: an AI agent can hold credentials issued by a trusted authority (N07 orchestrator, enterprise CA) attesting its capabilities, compliance status, or training data provenance -- without contacting the issuer at verification time.

Enterprise adoption is accelerating as machine-to-human identity ratios reach 144:1. OpenAgents.org launched DID-bound agent credentials in Feb 2026. The W3C VC 2.0 Recommendation (May 2025) stabilizes the data model, making it a production-ready foundation for cross-domain agent trust.

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| Verifiable Credential (VC) | Tamper-evident claim set issued by a known party, cryptographically signed | W3C VC 2.0 REC |
| Decentralized Identifier (DID) | W3C-standardized IRI for subject/issuer identity without central registry | W3C DID Core 1.0 |
| Data Integrity Proof | Cryptographic signature over credential document; ecdsa-rdfc-2022 or eddsa-rdfc-2022 | W3C Data Integrity 1.0 |
| credentialSchema | Reference to JSON Schema or OWL ontology validating credentialSubject claims | VC 2.0 Section 5.5 |
| credentialStatus | Endpoint for real-time revocation check via StatusList2021 bitstring | VC 2.0 Section 5.6 |
| refreshService | Endpoint for automated credential renewal before expiry | VC 2.0 Section 5.4 |
| Verifiable Presentation (VP) | Envelope aggregating multiple VCs for a single verification session | W3C VC 2.0 REC |
| Holder | Entity that controls the credential and presents it to verifiers | W3C VC 2.0 REC |
| Verifier | Entity that receives and validates the credential proof | W3C VC 2.0 REC |

## W3C VC 2.0 vs 1.x Breaking Changes
| Field | VC 1.x (deprecated) | VC 2.0 (required) |
|-------|---------------------|-------------------|
| Context URL | https://www.w3.org/2018/credentials/v1 | https://www.w3.org/ns/credentials/v2 |
| Issuance field | issuanceDate | validFrom |
| Expiry field | expirationDate | validUntil |
| Proof suite | Ed25519Signature2020 | eddsa-rdfc-2022 |

## Industry Standards
- W3C Verifiable Credentials Data Model 2.0 (May 2025 Recommendation)
- W3C DID Core 1.0 (July 2022 Recommendation)
- W3C Data Integrity 1.0 (cryptographic proof suites)
- StatusList2021 (Bitstring Status List v1.0, W3C Working Draft)
- IETF RFC 8037 (Ed25519 for JOSE)
- OpenID4VP / SIOP v2 (VP presentation protocols)

## Common Patterns
1. Agent capability attestation: N07 issues vc_credential to N03 attesting build pipeline capabilities.
2. Provenance chain: AI-generated content credential links to model training data VC.
3. Compliance proof: VC attesting GDPR data-handling compliance presented to auditors.
4. Cross-domain trust: Agent presents VC to external API for authorization without API keys.

## Pitfalls
- Using VC 1.x context with VC 2.0 fields (context mismatch causes validation failure).
- Omitting credentialSchema reference (makes claims unvalidatable by verifiers).
- Using HTTP (not HTTPS) for status list or DID:web endpoints.
- Forgetting that proofValue is base58btc or multibase-encoded, not raw bytes.
- Treating VP (presentation) and VC (credential) as the same artifact type.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_vc_credential_builder]] | downstream | 0.51 |
| [[vc-credential-builder]] | downstream | 0.50 |
| [[bld_tools_vc_credential]] | downstream | 0.43 |
| [[bld_instruction_vc_credential]] | downstream | 0.40 |
| [[p10_lr_vc_credential_builder]] | downstream | 0.39 |
| [[kc_vc_credential]] | sibling | 0.38 |
| [[bld_collaboration_vc_credential]] | downstream | 0.35 |
| [[p10_qg_vc_credential]] | downstream | 0.33 |
| [[bld_examples_vc_credential]] | downstream | 0.32 |
| [[bld_schema_vc_credential]] | downstream | 0.32 |
