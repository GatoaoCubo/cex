---
kind: architecture
id: bld_architecture_vc_credential
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of vc_credential -- inventory, dependencies
quality: 9.0
title: "Architecture VC Credential"
version: "1.0.0"
author: n04_wave7
tags: [vc_credential, builder, architecture, W3C, DID, data-integrity]
tldr: "Component map of vc_credential -- inventory, dependencies"
domain: "vc_credential construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name            | Role                          | Pillar | Status  |
|---------------------|-------------------------------|--------|---------|
| bld_manifest        | Builder identity and routing  | P05    | Active  |
| bld_instruction     | Production process            | P03    | Active  |
| bld_system_prompt   | LLM persona and rules         | P03    | Active  |
| bld_schema          | VC 2.0 data model schema      | P06    | Active  |
| bld_quality_gate    | W3C compliance validation     | P11    | Active  |
| bld_output_template | JSON-LD + proof template      | P05    | Active  |
| bld_examples        | Golden and anti-examples      | P07    | Active  |
| bld_knowledge_card  | W3C VC domain knowledge       | P01    | Active  |
| bld_architecture    | Component map                 | P08    | Active  |
| bld_collaboration   | Workflow with agent-builder   | P12    | Active  |
| bld_config          | Naming, paths, limits         | P09    | Active  |
| bld_memory          | Learned credential patterns   | P10    | Active  |
| bld_tools           | DID resolution, crypto tools  | P04    | Active  |

## Dependencies
| From              | To                          | Type           |
|-------------------|-----------------------------|----------------|
| bld_schema        | W3C VC 2.0 spec             | normative      |
| bld_output_template | bld_schema               | constraint     |
| bld_quality_gate  | bld_schema + bld_examples   | validation     |
| bld_instruction   | bld_system_prompt           | dependency     |
| bld_collaboration | agent-builder (P02)         | coordination   |
| bld_tools         | DID resolver (external)     | integration    |

## Architectural Position
vc_credential occupies the P10 identity/provenance layer within CEX. It is the foundational trust token: agent-builder (P02) creates agent personas; vc_credential binds those personas to cryptographically verifiable claims. The issuer-holder-verifier triangle maps to N07 (issuer) -- nucleus (holder) -- external system or audit trail (verifier). Upstream: DID document (separate kind). Downstream: Verifiable Presentation (aggregated VC set), compliance_framework (P11).
