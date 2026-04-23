---
kind: output_template
id: bld_output_template_vc_credential
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for vc_credential production
quality: 8.9
title: "Output Template VC Credential"
version: "1.0.0"
author: n04_wave7
tags: [vc_credential, builder, output_template, w3c, vc-2.0, did]
tldr: "Template with vars for vc_credential production"
domain: "vc_credential construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_vc_credential
  - p10_qg_vc_credential
  - bld_instruction_vc_credential
  - bld_examples_vc_credential
  - bld_tools_vc_credential
  - p03_sp_vc_credential_builder
  - bld_knowledge_card_vc_credential
  - vc-credential-builder
  - p10_lr_vc_credential_builder
  - bld_collaboration_vc_credential
---

```yaml
---
id: p10_vc_{{name}}.md
kind: vc_credential
pillar: P10
title: "{{credential_type}} for {{subject_name}}"
version: "1.0.0"
issuer_did: "{{issuer_did}}"
subject_did: "{{subject_did}}"
credential_type: "{{credential_type}}"
valid_from: "{{valid_from}}"
valid_until: "{{valid_until}}"
cryptosuite: "{{cryptosuite}}"
domain: "{{domain}}"
quality: null
tags: [W3C, verifiable-credential, VC-2.0, DID, {{domain_tag}}]
tldr: "{{credential_type}} credential issued by {{issuer_name}} for {{subject_name}}"
author: "{{author}}"
created: "{{date}}"
updated: "{{date}}"
---
```

## Credential Document

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "{{domain_context_url}}"
  ],
  "id": "https://{{issuer_domain}}/credentials/{{uuid}}",
  "type": ["VerifiableCredential", "{{credential_type}}"],
  "issuer": {
    "id": "{{issuer_did}}",
    "name": "{{issuer_name}}"
  },
  "validFrom": "{{valid_from}}",
  "validUntil": "{{valid_until}}",
  "credentialSubject": {
    "id": "{{subject_did}}",
    "{{claim_key}}": "{{claim_value}}"
  },
  "credentialSchema": {
    "id": "{{schema_registry_url}}/{{schema_id}}",
    "type": "JsonSchemaValidator2018"
  },
  "credentialStatus": {
    "id": "{{status_list_url}}#{{status_index}}",
    "type": "StatusList2021Entry",
    "statusPurpose": "revocation",
    "statusListIndex": "{{status_index}}",
    "statusListCredential": "{{status_list_url}}"
  },
  "refreshService": {
    "id": "{{refresh_service_url}}",
    "type": "ManualRefreshService2018"
  }
}
```

## Proof Block

```json
{
  "proof": {
    "type": "DataIntegrityProof",
    "cryptosuite": "{{cryptosuite}}",
    "created": "{{proof_created}}",
    "verificationMethod": "{{issuer_did}}#{{key_id}}",
    "proofPurpose": "assertionMethod",
    "proofValue": "{{base58_or_multibase_proof}}"
  }
}
```

## Usage Context
| Scenario | Presented To | Verification Method |
|----------|-------------|---------------------|
| Agent authentication | Verifier service | DID resolution + proof check |
| Provenance attestation | Audit trail | credentialSchema validation |
| Compliance proof | Regulatory body | credentialStatus check |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_vc_credential]] | downstream | 0.48 |
| [[p10_qg_vc_credential]] | downstream | 0.43 |
| [[bld_instruction_vc_credential]] | upstream | 0.42 |
| [[bld_examples_vc_credential]] | downstream | 0.39 |
| [[bld_tools_vc_credential]] | upstream | 0.32 |
| [[p03_sp_vc_credential_builder]] | upstream | 0.30 |
| [[bld_knowledge_card_vc_credential]] | upstream | 0.29 |
| [[vc-credential-builder]] | downstream | 0.27 |
| [[p10_lr_vc_credential_builder]] | downstream | 0.27 |
| [[bld_collaboration_vc_credential]] | downstream | 0.20 |
