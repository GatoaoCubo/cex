---
kind: examples
id: bld_examples_vc_credential
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of vc_credential artifacts
quality: 8.9
title: "Examples VC Credential"
version: "1.0.0"
author: n04_wave7
tags: [vc_credential, builder, examples, w3c, vc-2.0, did, data-integrity]
tldr: "Golden and anti-examples of vc_credential artifacts"
domain: "vc_credential construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://cex.ai/ns/agent-identity/v1"
  ],
  "id": "https://cex.ai/credentials/agent-n03-capability-2026",
  "type": ["VerifiableCredential", "AgentCapabilityCredential"],
  "issuer": {
    "id": "did:web:cex.ai",
    "name": "CEX Nucleus N07 Orchestrator"
  },
  "validFrom": "2026-04-14T00:00:00Z",
  "validUntil": "2027-04-14T00:00:00Z",
  "credentialSubject": {
    "id": "did:key:z6MkAgent03BuilderXXXX",
    "capabilityDomain": "artifact-construction",
    "qualityFloor": "9.0",
    "pipeline": "8F",
    "nucleusRole": "N03-Builder"
  },
  "credentialSchema": {
    "id": "https://cex.ai/schemas/agent-capability/v2",
    "type": "JsonSchemaValidator2018"
  },
  "credentialStatus": {
    "id": "https://cex.ai/status/list/2026#42",
    "type": "StatusList2021Entry",
    "statusPurpose": "revocation",
    "statusListIndex": "42",
    "statusListCredential": "https://cex.ai/status/list/2026"
  },
  "proof": {
    "type": "DataIntegrityProof",
    "cryptosuite": "ecdsa-rdfc-2022",
    "created": "2026-04-14T00:00:00Z",
    "verificationMethod": "did:web:cex.ai#key-1",
    "proofPurpose": "assertionMethod",
    "proofValue": "z3xWg4LKd..."
  }
}
```

## Anti-Example 1: Legacy VC 1.x Fields
```json
{
  "@context": ["https://www.w3.org/2018/credentials/v1"],
  "issuanceDate": "2026-04-14",
  "issuer": "https://cex.ai"
}
```
**Why it fails**: Uses VC 1.x context and deprecated `issuanceDate` field. VC 2.0 requires `https://www.w3.org/ns/credentials/v2` context and `validFrom` (not `issuanceDate`). Non-DID issuer violates agent identity requirement.

## Anti-Example 2: Missing Proof
```json
{
  "@context": ["https://www.w3.org/ns/credentials/v2"],
  "id": "https://cex.ai/credentials/test",
  "type": ["VerifiableCredential"],
  "issuer": "did:web:cex.ai",
  "validFrom": "2026-04-14T00:00:00Z",
  "credentialSubject": {"id": "did:key:z6Mk..."}
}
```
**Why it fails**: No proof block. A VC without a data-integrity proof is an unsigned claim -- not verifiable. Also missing credentialSchema and credentialStatus.

## Anti-Example 3: JWT Encoding in Wrong Kind
**Why it fails**: JWT-encoded VCs belong to the vc-jose-cose profile kind. This kind exclusively handles JSON-LD with data-integrity proofs. Mixing encoding formats causes verifier confusion.
