---
id: kc_threat_model
kind: knowledge_card
8f: F3_inject
title: Threat Model
version: 1.0.0
quality: 8.6
pillar: P01
density_score: 0.98
related:
  - bld_knowledge_card_threat_model
  - kc_ai_rmf_profile
  - p03_sp_threat_model_builder
  - atom_24_nist_vocabulary
  - bld_instruction_threat_model
  - bld_examples_threat_model
  - kc_ai_compliance_gdpr
  - p09_kc_data_residency
  - bld_knowledge_card_dataset_card
  - p10_lr_threat_model_builder
---

# Threat Model
A structured approach to identifying, assessing, and mitigating risks in AI systems.

## Key Components
- **Assets**: Identify critical data, systems, and services.
- **Threats**: Potential malicious actions (e.g., data breaches, model poisoning).
- **Vulnerabilities**: Weaknesses in systems or processes.
- **Risks**: Likelihood and impact of threats exploiting vulnerabilities.
- **Mitigation Strategies**: Controls to reduce risks (e.g., encryption, access controls).

## Risk Assessment
- **Criteria**: Use qualitative (low/medium/high) or quantitative (probability × impact) metrics.
- **Prioritization**: Focus on high-impact risks first.

## Examples
- **Data Breach**: Unauthorized access to sensitive data.
- **Model Poisoning**: Manipulating training data to degrade model performance.
- **Bias in Outputs**: Systematic errors in AI decisions due to flawed data.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_threat_model]] | sibling | 0.34 |
| [[kc_ai_rmf_profile]] | sibling | 0.27 |
| [[p03_sp_threat_model_builder]] | downstream | 0.26 |
| [[atom_24_nist_vocabulary]] | sibling | 0.24 |
| [[bld_instruction_threat_model]] | downstream | 0.23 |
| [[bld_examples_threat_model]] | downstream | 0.23 |
| [[kc_ai_compliance_gdpr]] | sibling | 0.22 |
| [[p09_kc_data_residency]] | sibling | 0.22 |
| [[bld_knowledge_card_dataset_card]] | sibling | 0.21 |
| [[p10_lr_threat_model_builder]] | downstream | 0.20 |
