---
kind: knowledge_card
id: bld_knowledge_card_sandbox_spec
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for sandbox_spec production
quality: 9.2
title: "Knowledge Card Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, knowledge_card]
tldr: "Domain knowledge for sandbox_spec production"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_sandbox_spec
  - sandbox-spec-builder
  - bld_instruction_sandbox_spec
  - kc_sandbox_spec
  - bld_examples_sandbox_spec
  - bld_knowledge_card_audit_log
  - p03_sp_sandbox_spec_builder
  - p09_qg_sandbox_spec
  - bld_examples_compliance_checklist
  - audit-log-builder
---

## Domain Overview
Sandbox_spec artifacts define the isolated environment enterprise buyers and regulated industries require before signing. Where playground_config optimizes for PLG conversion, sandbox_spec optimizes for procurement: separate tenant, separate data, signed audit trail, compliance evidence. Reference implementations include Stripe test mode (dual-key pattern: test_ vs live_ prefixes), AWS Firecracker micro-VMs (sub-125ms boot, KVM isolation), Google gVisor (user-space kernel), and HIPAA/PCI-DSS mandated test environments.

Sandbox is an enterprise procurement gate. Without a credible sandbox_spec, deals stall in legal review for weeks. The spec must name the isolation technology, the data boundary, the compliance mapping, and the teardown guarantee.

## Key Concepts
| Concept | Definition | Source |
|---|---|---|
| Dual-key isolation | Test and live credentials share no blast radius | Stripe test mode |
| Micro-VM isolation | KVM-backed VM with <125ms boot | AWS Firecracker |
| User-space kernel | Syscall interception for container hardening | Google gVisor |
| Separate tenant | Distinct DB + compute + network per customer | Snowflake, AWS GovCloud |
| Compliance profile | Evidence bundle mapping controls to frameworks | ISO 27001 SoA, SOC 2 |
| Audit immutability | Append-only log with cryptographic chain | AWS CloudTrail, GCP Cloud Audit |
| Teardown policy | Automated destruction + cert of deletion | PCI-DSS 3.2.1 req 9.8 |
| Data residency | Region-locked storage + compute | GDPR Art 44, Schrems II |

## Industry Standards
- PCI-DSS v4.0 sandbox isolation and segmentation requirements
- HIPAA 164.312 technical safeguards and 164.308 administrative safeguards
- ISO/IEC 27001:2022 A.8.31 separation of development, test, production
- SOC 2 Trust Services Criteria (CC6.1 logical access, CC7.1 change management)
- NIST SP 800-190 application container security guide
- NIST SP 800-53 Rev 5 AC-4 information flow enforcement
- GDPR Article 32 security of processing
- FedRAMP Moderate baseline (for US federal pilots)

## Common Patterns
1. Dual-key prefix scheme (test_ vs live_) enforced at API gateway.
2. Micro-VM per tenant for enterprise pilots (Firecracker or Nitro Enclaves).
3. Separate VPC + account for sandbox traffic, zero peering to prod.
4. Ephemeral lifecycle with automated teardown and deletion certificate.
5. Compliance evidence auto-exported (SOC 2 evidence collector pattern).
6. Read-only replica of anonymized prod data for realistic pilots.
7. Tamper-evident audit log with cryptographic chain (e.g., QLDB-style).

## Pitfalls
- Sandbox shares credentials or network with prod -- instant procurement fail.
- No teardown cert -- legal blocks renewal until proof of deletion arrives.
- Compliance mapping absent -- buyer's security review returns with 40 questions.
- Sandbox treated as playground (too permissive, no audit, fails SOC 2).
- No data residency control -- blocks EU and regulated-sector deals.
- Missing upgrade path from sandbox pilot to production tenant -- deal dies.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_sandbox_spec]] | downstream | 0.42 |
| [[sandbox-spec-builder]] | downstream | 0.35 |
| [[bld_instruction_sandbox_spec]] | downstream | 0.31 |
| [[kc_sandbox_spec]] | sibling | 0.28 |
| [[bld_examples_sandbox_spec]] | downstream | 0.28 |
| [[bld_knowledge_card_audit_log]] | sibling | 0.27 |
| [[p03_sp_sandbox_spec_builder]] | downstream | 0.27 |
| [[p09_qg_sandbox_spec]] | downstream | 0.26 |
| [[bld_examples_compliance_checklist]] | downstream | 0.25 |
| [[audit-log-builder]] | downstream | 0.22 |
