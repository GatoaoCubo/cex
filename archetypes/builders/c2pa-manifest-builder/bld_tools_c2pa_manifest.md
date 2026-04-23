---
kind: tools
id: bld_tools_c2pa_manifest
pillar: P04
llm_function: CALL
purpose: Tools available for c2pa_manifest production
quality: 8.9
title: "Tools C2PA Manifest"
version: "1.0.0"
author: n04_wave7
tags: [c2pa_manifest, builder, tools, C2PA, COSE, JUMBF, c2pa-rs]
tldr: "Tools available for c2pa_manifest production"
domain: "c2pa_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_c2pa_manifest
  - p10_lr_c2pa_manifest_builder
  - bld_architecture_c2pa_manifest
  - c2pa-manifest-builder
  - p03_sp_c2pa_manifest_builder
  - bld_instruction_c2pa_manifest
  - bld_collaboration_c2pa_manifest
  - bld_output_template_c2pa_manifest
  - bld_tools_agent_grounding_record
  - bld_tools_vc_credential
---

## Production Tools
| Tool             | Purpose                              | When                         |
|------------------|--------------------------------------|------------------------------|
| cex_compile.py   | Compile manifest YAML to JSON        | After draft produced         |
| cex_score.py     | Score manifest against quality gates | Post-production validation   |
| cex_retriever.py | Fetch similar manifest examples      | During context assembly      |
| cex_doctor.py    | Validate manifest structure          | Pre-commit check             |
| cex_validator.py | MIME type and assertion validation   | Schema compliance check      |

## Validation Tools
| Tool                            | Purpose                                | When                        |
|---------------------------------|----------------------------------------|-----------------------------|
| c2pa-rs (Rust)                  | Sign and verify C2PA manifests         | Signing and validation      |
| c2pa-js (Node)                  | JavaScript C2PA SDK for web platforms  | Browser/Node environments   |
| verify.contentauthenticity.org  | CAI public verification portal         | Post-build smoke test       |
| cose_validator                  | Validate COSE_Sign1 signature block    | Cryptographic verification  |
| jumbf_parser                    | Parse JUMBF box structure in media     | Embedding verification      |

## External References
- C2PA 2.3 Spec: https://spec.c2pa.org/specifications/specifications/2.3/
- c2pa-rs (Rust SDK): https://github.com/contentauth/c2pa-rs
- CAI SDK (JavaScript): https://github.com/contentauth/c2pa-js
- CAI Verify Portal: https://verify.contentauthenticity.org
- C2PA Digital Source Types: https://cv.iptc.org/newscodes/digitalsourcetype/

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_c2pa_manifest]] | upstream | 0.56 |
| [[p10_lr_c2pa_manifest_builder]] | downstream | 0.55 |
| [[bld_architecture_c2pa_manifest]] | downstream | 0.44 |
| [[c2pa-manifest-builder]] | downstream | 0.44 |
| [[p03_sp_c2pa_manifest_builder]] | upstream | 0.43 |
| [[bld_instruction_c2pa_manifest]] | upstream | 0.41 |
| [[bld_collaboration_c2pa_manifest]] | downstream | 0.38 |
| [[bld_output_template_c2pa_manifest]] | downstream | 0.36 |
| [[bld_tools_agent_grounding_record]] | sibling | 0.35 |
| [[bld_tools_vc_credential]] | sibling | 0.32 |
