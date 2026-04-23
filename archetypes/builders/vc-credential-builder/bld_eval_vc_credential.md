---
kind: quality_gate
id: p10_qg_vc_credential
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for vc_credential
quality: 9.0
title: "Quality Gate VC Credential"
version: "1.0.0"
author: n04_wave7
tags: [vc_credential, builder, quality_gate, W3C, VC-2.0, DID, data-integrity]
tldr: "Quality gate with HARD and SOFT scoring for vc_credential"
domain: "vc_credential construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_vc_credential
  - bld_instruction_vc_credential
  - bld_tools_vc_credential
  - p10_lr_vc_credential_builder
  - p03_sp_vc_credential_builder
  - bld_knowledge_card_vc_credential
  - bld_output_template_vc_credential
  - p10_qg_c2pa_manifest
  - vc-credential-builder
  - p01_qg_faq_entry
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| W3C VC 2.0 compliance | 100% | equals | All required fields per spec |

## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing fields |
| H02 | ID matches pattern ^p10_vc_[a-z][a-z0-9_]+\.md$ | ID format mismatch |
| H03 | kind field is "vc_credential" | Kind field incorrect or missing |
| H04 | @context includes https://www.w3.org/ns/credentials/v2 | Missing or wrong VC context |
| H05 | issuer_did is valid DID (did: prefix) | Non-DID issuer |
| H06 | subject_did is valid DID | Non-DID subject |
| H07 | proof.cryptosuite is ecdsa-rdfc-2022 or eddsa-rdfc-2022 | Unsupported or missing cryptosuite |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | VC 2.0 field completeness (validFrom, type, credentialSubject, proof) | 0.30 | All present = 1.0, partial = 0.5, missing critical = 0 |
| D02 | credentialSchema reference quality (IRI valid, type correct) | 0.20 | Full reference = 1.0, partial = 0.5, absent = 0 |
| D03 | credentialStatus coverage (endpoint valid, statusListIndex set) | 0.20 | Full coverage = 1.0, partial = 0.5, absent = 0 |
| D04 | Proof block completeness (cryptosuite, verificationMethod, proofPurpose, proofValue) | 0.20 | Complete = 1.0, partial = 0.5, absent = 0 |
| D05 | Domain keyword density (W3C, verifiable-credential, DID, issuer, subject, proof) | 0.10 | 6+ keywords = 1.0, 4-5 = 0.7, <4 = 0.3 |

## Actions
| Score | Action |
|-------|--------|
| GOLDEN | >=9.5 | Auto-publish with no review |
| PUBLISH | >=8.0 | Auto-publish after validation |
| REVIEW | >=7.0 | Require manual review |
| REJECT | <7.0 | Reject and flag for correction |

## Bypass
| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Prototype credential (no live status endpoint) | N07 orchestrator | Escalation log with PROTOTYPE tag |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
