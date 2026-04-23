---
kind: knowledge_card
id: bld_knowledge_card_ai_rmf_profile
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for ai_rmf_profile production
quality: 9.2
title: "Knowledge Card AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, knowledge_card, NIST, AI-RMF, GOVERN, MAP, MEASURE, MANAGE, GenAI-profile, 600-1, action-ID, risk-category]
tldr: "Domain knowledge for ai_rmf_profile production"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - ai-rmf-profile-builder
  - p03_sp_ai_rmf_profile_builder
  - bld_instruction_ai_rmf_profile
  - kc_ai_rmf_profile
  - bld_examples_ai_rmf_profile
  - bld_output_template_ai_rmf_profile
  - bld_tools_ai_rmf_profile
  - bld_collaboration_ai_rmf_profile
  - atom_24_nist_vocabulary
  - p11_qg_ai_rmf_profile
---

## Domain Overview
The NIST AI Risk Management Framework (AI-RMF) provides a voluntary, flexible framework for organizations to manage risks associated with AI systems. Published January 2023; the GenAI Profile (AI 600-1) was released July 2024, adding 12 specific risk categories for generative AI. The Critical Infrastructure sector profile concept note appeared April 2026. Adopted by US federal agencies (NIST SP 800-series), major enterprises, and referenced by the EU-US AI Standards dialogue.

The AI-RMF organizes risk management into 4 core functions (GOVERN/MAP/MEASURE/MANAGE) with subcategories and action-IDs in the AI-RMF Playbook. A "profile" is a customized selection and prioritization of framework outcomes for a specific system, organizational context, or sector.

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| GOVERN function | Cross-cutting function: policies, processes, and accountability for AI risk management | NIST AI-RMF 1.0 |
| MAP function | Identify and categorize AI risks in organizational and deployment context | NIST AI-RMF 1.0 |
| MEASURE function | Analyze and assess identified AI risks using metrics and evaluation methods | NIST AI-RMF 1.0 |
| MANAGE function | Prioritize, respond to, and monitor AI risks with controls and contingency plans | NIST AI-RMF 1.0 |
| action-ID | Unique identifier for a specific suggested action (e.g., GV-1.1, MP-2.3, MS-4.1, MG-3.2) | NIST AI-RMF Playbook |
| GenAI-profile | AI 600-1 vertical profile for generative AI systems with 12 unique risk categories | NIST AI 600-1 (2024) |
| risk-category | One of 12 GenAI-specific risk areas: CBRN, Confabulation, Data Privacy, Environmental, Harmful Bias, Human-AI Config, Information Integrity, Information Security, IP, Obscene Content, Value Chain, Workforce | NIST AI 600-1 |
| implementation status | Profile field: Implemented / Partial / Planned / Not Applicable per action-ID | NIST AI-RMF Playbook |
| crosswalk | Mapping table linking AI-RMF action-IDs to equivalent controls in other frameworks (ISO 42001, EU AI Act) | NIST AI-RMF Playbook Appendix |

## The 12 GenAI Risk Categories (AI 600-1)
| # | Category | Description | Severity Trigger |
|---|---------|-------------|-----------------|
| 1 | CBRN Information | AI generates uplift for weapons of mass destruction | Critical |
| 2 | Confabulation | AI produces factually incorrect but plausible outputs | High |
| 3 | Data Privacy | AI exposes PII or training data memorization | High |
| 4 | Environmental | AI training / inference has significant energy/carbon impact | Moderate |
| 5 | Harmful Bias / Homogenization | AI perpetuates or amplifies societal biases | High |
| 6 | Human-AI Configuration | Misunderstanding of AI capabilities leads to over-reliance | Moderate |
| 7 | Information Integrity | AI produces or amplifies misinformation/disinformation | High |
| 8 | Information Security | AI enables new attack vectors or is itself vulnerable | High |
| 9 | Intellectual Property | AI reproduces copyrighted training data verbatim | Moderate |
| 10 | Obscene / Degrading Content | AI generates CSAM or non-consensual sexual content | Critical |
| 11 | Value Chain / Component Integration | Third-party AI components introduce undisclosed risks | Moderate |
| 12 | Workforce / Labor | AI displaces workers or creates safety risks in automation | Moderate |

## AI-RMF Function / Action-ID Reference
| Function | Prefix | Action Count | Example IDs |
|----------|--------|-------------|-------------|
| GOVERN | GV | 6 subcategories, ~30 actions | GV-1.1, GV-2.2, GV-6.1 |
| MAP | MP | 5 subcategories, ~20 actions | MP-1.1, MP-2.3, MP-5.2 |
| MEASURE | MS | 4 subcategories, ~18 actions | MS-1.1, MS-2.5, MS-4.1 |
| MANAGE | MG | 4 subcategories, ~16 actions | MG-1.1, MG-3.2, MG-4.2 |

## Industry Standards
- NIST AI-RMF 1.0 (January 2023)
- NIST AI 600-1 GenAI Profile (July 2024)
- NIST AI-RMF Playbook (airc.nist.gov)
- ISO/IEC 42001:2023 (AI Management System -- crosswalk available)
- EU AI Act Article 9 (Risk Management System -- partial crosswalk)
- CISA AI Roadmap (sector-specific AI-RMF adoption guidance)

## Common Patterns
1. Profile for a specific system, not an entire organization -- scope matters.
2. Use "Not Applicable" with justification for irrelevant categories -- never omit.
3. Evidence pointers per action-ID distinguish a real profile from aspirational documentation.
4. Crosswalk to ISO 42001 accelerates combined AIMS + AI-RMF compliance programs.

## Pitfalls
- Confusing AI-RMF with NIST CSF (Cybersecurity Framework) -- different structure and scope.
- Listing action-IDs without implementation status -- makes the profile unactionable.
- Ignoring AI 600-1 GenAI categories when profiling LLM-based systems -- these are mandatory.
- Treating the profile as a one-time audit report -- it requires periodic review and update.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ai-rmf-profile-builder]] | downstream | 0.69 |
| [[p03_sp_ai_rmf_profile_builder]] | downstream | 0.64 |
| [[bld_instruction_ai_rmf_profile]] | downstream | 0.59 |
| [[kc_ai_rmf_profile]] | sibling | 0.57 |
| [[bld_examples_ai_rmf_profile]] | downstream | 0.52 |
| [[bld_output_template_ai_rmf_profile]] | downstream | 0.48 |
| [[bld_tools_ai_rmf_profile]] | downstream | 0.43 |
| [[bld_collaboration_ai_rmf_profile]] | downstream | 0.41 |
| [[atom_24_nist_vocabulary]] | sibling | 0.41 |
| [[p11_qg_ai_rmf_profile]] | downstream | 0.39 |
