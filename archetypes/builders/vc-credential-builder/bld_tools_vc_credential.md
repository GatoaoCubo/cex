---
kind: tools
id: bld_tools_vc_credential
pillar: P04
llm_function: CALL
purpose: Tools available for vc_credential production
quality: 8.9
title: "Tools VC Credential"
version: "1.0.0"
author: n04_wave7
tags: [vc_credential, builder, tools, DID, data-integrity, W3C]
tldr: "Tools available for vc_credential production"
domain: "vc_credential construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_vc_credential
  - bld_knowledge_card_vc_credential
  - bld_instruction_vc_credential
  - bld_tools_code_of_conduct
  - bld_tools_ontology
  - p03_sp_vc_credential_builder
  - p10_qg_vc_credential
  - p10_lr_vc_credential_builder
  - bld_tools_contributor_guide
  - bld_tools_validation_schema
---

## Production Tools
| Tool             | Purpose                              | When                         |
|------------------|--------------------------------------|------------------------------|
| cex_compile.py   | Compile VC YAML to JSON-LD           | After draft produced         |
| cex_score.py     | Score VC against quality gates       | Post-production validation   |
| cex_retriever.py | Fetch similar VC examples            | During context assembly      |
| cex_doctor.py    | Validate VC structure and fields     | Pre-commit check             |
| cex_validator.py | JSON Schema validation of claims     | credentialSchema check       |

## Validation Tools
| Tool               | Purpose                              | When                         |
|--------------------|--------------------------------------|------------------------------|
| did_resolver       | Resolve DID to DID Document          | Issuer/subject DID check     |
| vc_verifier        | Verify data-integrity proof          | Proof validation             |
| status_list_check  | Check credentialStatus revocation    | Before credential presentation|
| jsonld_processor   | Expand/compact JSON-LD document      | Context normalization        |

## External References
- W3C VC 2.0 spec: https://www.w3.org/TR/vc-data-model-2.0/
- W3C Data Integrity: https://www.w3.org/TR/vc-data-integrity/
- StatusList2021: https://www.w3.org/TR/vc-bitstring-status-list/
- DID Core 1.0: https://www.w3.org/TR/did-core/
- ecdsa-rdfc-2022 cryptosuite: https://www.w3.org/TR/vc-di-ecdsa/

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_vc_credential]] | downstream | 0.36 |
| [[bld_knowledge_card_vc_credential]] | upstream | 0.33 |
| [[bld_instruction_vc_credential]] | upstream | 0.33 |
| [[bld_tools_code_of_conduct]] | sibling | 0.29 |
| [[bld_tools_ontology]] | sibling | 0.28 |
| [[p03_sp_vc_credential_builder]] | upstream | 0.27 |
| [[p10_qg_vc_credential]] | downstream | 0.24 |
| [[p10_lr_vc_credential_builder]] | downstream | 0.24 |
| [[bld_tools_contributor_guide]] | sibling | 0.23 |
| [[bld_tools_validation_schema]] | sibling | 0.23 |
