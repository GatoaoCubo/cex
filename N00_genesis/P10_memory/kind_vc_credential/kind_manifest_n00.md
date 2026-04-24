---
id: n00_vc_credential_manifest
kind: knowledge_card
8f: F3_inject
pillar: P10
nucleus: n00
title: "VC Credential -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, vc_credential, p10, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_vc_credential
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_sandbox_spec
  - bld_schema_integration_guide
  - bld_schema_runtime_state
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A vc_credential is a W3C Verifiable Credential 2.0 that cryptographically attests an AI agent's identity, capabilities, and authorizations. It enables agents to prove who they are and what they are permitted to do in multi-agent systems, supporting zero-trust architectures and delegated authority chains without centralized identity servers.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `vc_credential` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| vc_version | string | yes | W3C VC spec version (e.g. "2.0") |
| issuer_did | string | yes | DID of the credential issuer |
| subject_did | string | yes | DID of the agent receiving the credential |
| credential_type | array | yes | VC type array (e.g. ["VerifiableCredential", "AgentIdentity"]) |
| credential_subject | object | yes | Claims about the agent (role, capabilities, nucleus) |
| valid_from | datetime | yes | Credential validity start |
| valid_until | datetime | no | Credential expiry |
| proof | object | yes | Cryptographic proof block |

## When to use
- When deploying agents in zero-trust multi-agent architectures
- When building A2A (agent-to-agent) communication with verified identity
- When regulatory compliance requires cryptographic attestation of AI agent roles

## Builder
`archetypes/builders/vc_credential-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind vc_credential --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: vc_n03_engineering_agent
kind: vc_credential
pillar: P10
nucleus: n03
title: "Example VC Credential"
version: 1.0
quality: null
---
# W3C VC 2.0: N03 Engineering Agent Identity
vc_version: "2.0"
issuer_did: "did:web:cex.{{BRAND_DOMAIN}}"
subject_did: "did:web:cex.{{BRAND_DOMAIN}}:n03"
credential_type: ["VerifiableCredential", "AgentIdentity"]
credential_subject: {nucleus: n03, role: engineering, sin_lens: inventive_pride}
```

## Related kinds
- `c2pa_manifest` (P10) -- content provenance credential complementing agent identity
- `agent_card` (P08) -- human-readable agent identity that VC credential attests
- `guardrail` (P11) -- safety constraints that the VC credential may encode as claims

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_vc_credential]] | upstream | 0.55 |
| [[bld_schema_reranker_config]] | upstream | 0.44 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.43 |
| [[bld_schema_dataset_card]] | upstream | 0.43 |
| [[bld_schema_benchmark_suite]] | upstream | 0.43 |
| [[bld_schema_usage_report]] | upstream | 0.43 |
| [[bld_schema_pitch_deck]] | upstream | 0.42 |
| [[bld_schema_sandbox_spec]] | upstream | 0.42 |
| [[bld_schema_integration_guide]] | upstream | 0.42 |
| [[bld_schema_runtime_state]] | upstream | 0.41 |
