---
kind: instruction
id: bld_instruction_vc_credential
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for vc_credential
quality: 8.9
title: "Instruction VC Credential"
version: "1.0.0"
author: n04_wave7
tags: [vc_credential, builder, instruction, w3c, did, proof]
tldr: "Step-by-step production process for vc_credential"
domain: "vc_credential construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH
1. Identify issuer DID method (did:web, did:key, did:jwk) and resolve DID document.
2. Define subject claims: what attributes are being attested (agent capabilities, compliance status, training data provenance).
3. Select credentialSchema: JSON Schema or OWL ontology reference for claim validation.
4. Choose proof cryptosuite: ecdsa-rdfc-2022 (secp256r1) or eddsa-rdfc-2022 (Ed25519).
5. Determine credentialStatus mechanism: StatusList2021 bitstring revocation list endpoint.
6. Identify refreshService endpoint if credential has TTL and needs auto-renewal.

## Phase 2: COMPOSE
1. Reference SCHEMA.md for required VC 2.0 fields (id, type, issuer, validFrom, credentialSubject, proof).
2. Set @context: ["https://www.w3.org/ns/credentials/v2", additional domain contexts].
3. Assign id as unique IRI: https://issuer.example/credentials/[uuid].
4. Set type array: ["VerifiableCredential", "[domain_type]Credential"].
5. Set issuer as DID string or issuer object with name and id fields.
6. Set validFrom (ISO 8601, required) and validUntil (ISO 8601, optional).
7. Populate credentialSubject with id (subject DID) and claim properties.
8. Add credentialSchema with id (schema IRI) and type (JsonSchemaValidator2018).
9. Add credentialStatus with id (status list URL) and statusListIndex.
10. Generate proof block: type, cryptosuite, created, verificationMethod, proofPurpose, proofValue.
11. Validate proof against W3C Data Integrity spec before finalizing.

## Phase 3: VALIDATE
- [ ] @context includes https://www.w3.org/ns/credentials/v2
- [ ] issuer is a valid DID or DID URL
- [ ] credentialSubject.id is a valid DID
- [ ] proof.cryptosuite is ecdsa-rdfc-2022 or eddsa-rdfc-2022
- [ ] credentialStatus.type is StatusList2021Entry
- [ ] validFrom is ISO 8601 datetime
- [ ] Domain keywords present: W3C, verifiable-credential, VC-2.0, DID, issuer, subject, proof
