---
quality: 8.4
quality: 8.3
id: p11_cfw_cex_ai_act
kind: compliance_framework
8f: F1_constrain
pillar: P11
title: "Compliance Framework: CEX vs EU AI Act (GPAI Provider Obligations)"
version: "1.0.0"
created: "2026-04-19"
updated: "2026-04-19"
author: "n05_operations"
domain: "ai_governance"
regulatory_scope: "EU AI Act 2024/1689 -- GPAI provider obligations (Art. 51-56)"
enforcement_mechanisms: "Fines up to EUR 15M or 3% global turnover (Art. 101); market withdrawal"
tags: [compliance_framework, eu_ai_act, gpai, operations, ai_governance]
tldr: "Maps CEX system to EU AI Act GPAI provider obligations (Art. 51-56): transparency, copyright, technical docs, downstream info."
related:
  - bld_output_template_compliance_framework
  - bld_knowledge_card_gpai_technical_doc
  - bld_knowledge_card_conformity_assessment
  - gpai-technical-doc-builder
  - bld_output_template_conformity_assessment
  - bld_instruction_conformity_assessment
  - bld_examples_conformity_assessment
  - bld_collaboration_gpai_technical_doc
  - bld_collaboration_conformity_assessment
  - bld_tools_conformity_assessment
density_score: 1.0
---

## 1. Executive Overview

**System**: CEXAI (Cognitive Exchange AI) -- Typed Knowledge System for LLM Agents
**Applicable Regulations**: EU AI Act 2024/1689 (GPAI provisions, Art. 51-56)
**Jurisdictions**: EU (primary), international (by extension for EU-deployed instances)
**Risk Classification**: GPAI model integrator (not high-risk AI system per se; CEX orchestrates GPAI models)
**Compliance Officer**: System owner (per-instance; see brand_config.yaml)
**Last Review**: 2026-04-19
**Next Audit Due**: 2026-07-19

CEX integrates multiple GPAI models (Claude, Gemini, Ollama local models) as an orchestration layer. Under the EU AI Act, CEX is a **downstream deployer** of GPAI models (Art. 25) and must ensure GPAI provider obligations are met or documented as delegated to upstream providers.

## 2. Regulatory Scope Matrix

| Regulation | Version | Applicability | Reason | Primary Articles |
|-----------|---------|--------------|--------|-----------------|
| EU AI Act | 2024/1689 | Applicable | Orchestrates GPAI models for enterprise use | Art. 51-56 (GPAI), Art. 25 (deployer) |
| GDPR | 2016/679 | Applicable | Processes user data in prompts/memory | Art. 5, 6, 13, 25, 30, 32 |
| EU Copyright Directive | 2019/790 | Applicable | Training data transparency obligation | Art. 4 (TDM exception) |
| NIST AI RMF | 1.0 (2023) | Voluntary reference | Risk management best practice | GOVERN, MAP, MEASURE, MANAGE |
| ISO/IEC 42001 | 2023 | Voluntary reference | AI management system standard | Clause 6, 8, 9, 10 |

## 3. GPAI Provider Obligations Mapping (Art. 51-56)

| Obligation | Article | CEX Implementation | Evidence | Status |
|-----------|---------|-------------------|----------|--------|
| Technical documentation | Art. 53(1)(a) | 300 kind schemas + 12 ISOs per builder + CLAUDE.md | archetypes/builders/*/bld_schema_*.md | Compliant |
| Transparency policy | Art. 53(1)(b) | Agent cards declare model, tools, capabilities | N0X_*/P08_architecture/agent_card_n0X.md | Compliant |
| Copyright compliance policy | Art. 53(1)(c) | Delegated to upstream GPAI providers (Anthropic, Google) | Provider ToS references | Delegated |
| Training data summary | Art. 53(1)(d) | CEX does not train models; delegates to providers | N/A for orchestrator | Not Applicable |
| Downstream provider info | Art. 53(2) | nucleus_models.yaml declares all providers + fallback chains | .cex/config/nucleus_models.yaml | Compliant |
| Systemic risk assessment | Art. 55 | Not applicable (CEX is not a GPAI model with systemic risk) | N/A | Not Applicable |
| Model evaluation | Art. 55(2) | Per-provider: Anthropic publishes model cards; Google publishes Gemini reports | External provider docs | Delegated |
| Serious incident reporting | Art. 62 | Incident report template + safety_policy escalation protocol | N05_operations/P11_feedback/safety_policy_cex_agent_output.md | Compliant |

## 4. Gap Analysis

| Requirement | Regulation/Article | Current State | Gap | Remediation Plan | Owner | Target Date |
|------------|-------------------|--------------|-----|-----------------|-------|-------------|
| Machine-readable GPAI provider disclosure | Art. 53(1)(b) | Agent cards exist but not in standardized machine-readable format | No EU AI Office template adopted yet | Adopt template when EU AI Office publishes (expected H2 2026) | N05 | 2026-12-31 |
| Copyright compliance documentation | Art. 53(1)(c) | Delegated to upstream providers | No CEX-level documentation of delegation chain | Create delegation_record artifact citing provider ToS | N04 | 2026-06-30 |
| Post-market monitoring formal plan | Art. 72 (if high-risk deployed) | cex_quality_monitor.py + cex_doctor.py exist | Not formalized as EU AI Act PMM plan | Formalize as conformity_assessment artifact | N05 | 2026-07-31 |

**Summary:**
- Total requirements mapped: 8
- Fully compliant: 4
- Delegated to upstream provider: 2
- Not applicable: 2
- Gaps requiring remediation: 3

## 5. Data Protection Provisions (GDPR)

| Data Subject Right | Legal Basis | Mechanism | SLA | Implemented |
|-------------------|------------|-----------|-----|------------|
| Right to access (Art. 15) | Legitimate interest | Export from .cex/runtime/ + memory files | 30 days | Yes |
| Right to erasure (Art. 17) | Legitimate interest | Delete .cex/runtime/*, memory files, git history rewrite | 30 days | Partial (git rewrite requires manual) |
| Right to portability (Art. 20) | Consent | Export as .md/.yaml (native CEX format) | 30 days | Yes |
| Opt-out of automated decisions (Art. 22) | Legitimate interest | GDP protocol: user decides WHAT, LLM decides HOW | Immediate | Yes |

**DPIA**: Required for instances processing sensitive data (healthcare, legal verticals).
**Legal basis**: Legitimate interest for enterprise knowledge management; consent for personal data in prompts.

## 6. CEX-Specific Controls

| Control | Implementation | Artifact Reference |
|---------|---------------|-------------------|
| Quality gate enforcement | 8F pipeline F7 GOVERN; no artifact published below 8.0 | .claude/rules/8f-reasoning.md |
| No self-scoring | quality: null rule enforced by pre-commit hook | safety_policy_cex_agent_output.md SR01 |
| Audit trail | Signal writer + git commit history + .cex/runtime/audit/ | _tools/signal_writer.py |
| Multi-runtime transparency | nucleus_models.yaml declares provider per nucleus | .cex/config/nucleus_models.yaml |
| Data minimization | Context window configs limit injected context | N05_operations/P09_config/context_window_config_n05.md |
| Access control | RBAC policy per nucleus | N05_operations/P09_config/p09_rbac_n05.md |

## 7. Audit and Monitoring

| Audit Type | Frequency | Method | Last Conducted | Next Due |
|-----------|-----------|--------|----------------|----------|
| Internal compliance review | Quarterly | cex_doctor.py + cex_flywheel_audit.py | 2026-04-19 | 2026-07-19 |
| Quality system audit | Continuous | cex_quality_monitor.py snapshots | Ongoing | - |
| Provider compliance check | Semi-annual | Review upstream provider ToS + model cards | 2026-04-19 | 2026-10-19 |

## 8. Enforcement and Remediation

| Violation Type | Consequence | Notification | Remediation SLA |
|---------------|-------------|-------------|-----------------|
| GPAI Art. 53 non-compliance | Up to EUR 15M or 3% global turnover (Art. 101(2)) | EU AI Office | As directed |
| GDPR Art. 83(5) severe | Up to EUR 20M or 4% global turnover | DPA within 72h | Immediate |
| Internal quality violation | Artifact blocked; nucleus re-dispatched | N07 orchestrator | Same session |

## 9. Version Control

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 1.0.0 | 2026-04-19 | n05_operations | Initial framework: GPAI obligations + GDPR + gap analysis | Peer review pending |

## 10. Attestation

> This compliance framework documents CEX's current state of regulatory alignment
> as of 2026-04-19. It is a living document updated quarterly or upon regulatory change.
> Outstanding gaps are documented in Section 4 with committed remediation plans.
> Quality field remains null pending peer review per CEX governance rules.

## References

- EU AI Act: Regulation (EU) 2024/1689
- GDPR: Regulation (EU) 2016/679
- NIST AI RMF 1.0: https://airc.nist.gov/Home
- ISO/IEC 42001:2023 AI Management Systems
- Anthropic Usage Policy (referenced for Claude provider obligations)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_compliance_framework]] | upstream | 0.53 |
| [[bld_knowledge_card_gpai_technical_doc]] | upstream | 0.38 |
| [[bld_knowledge_card_conformity_assessment]] | upstream | 0.37 |
| [[gpai-technical-doc-builder]] | related | 0.35 |
| [[bld_output_template_conformity_assessment]] | upstream | 0.31 |
| [[bld_instruction_conformity_assessment]] | upstream | 0.30 |
| [[bld_examples_conformity_assessment]] | upstream | 0.25 |
| [[bld_collaboration_gpai_technical_doc]] | downstream | 0.24 |
| [[bld_collaboration_conformity_assessment]] | downstream | 0.24 |
| [[bld_tools_conformity_assessment]] | upstream | 0.24 |
