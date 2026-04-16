---
kind: knowledge_card
id: bld_knowledge_card_threat_model
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for threat_model production
quality: 9.2
title: "Knowledge Card Threat Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [threat_model, builder, knowledge_card]
tldr: "Domain knowledge for threat_model production"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Domain Overview

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
Threat modeling for AI systems focuses on identifying, analyzing, and mitigating risks posed by malicious actors exploiting vulnerabilities in AI design, training, or deployment. Unlike safety policies, which govern acceptable behavior, threat models prioritize adversarial scenarios such as data poisoning, model inversion, and evasion attacks. The rise of AI in critical domains (e.g., healthcare, finance) has increased demand for structured risk assessments that align with standards like NIST SP 800-160 and ISO/IEC 23894.

Key challenges include mapping abstract AI risks (e.g., bias amplification) to tangible threats and ensuring models remain robust against evolving attack techniques. Effective threat models integrate technical (e.g., adversarial robustness) and operational (e.g., supply chain risks) dimensions, often requiring cross-disciplinary collaboration between security, data science, and compliance teams.

## Key Concepts
| Concept              | Definition                                                                 | Source                          |
|----------------------|----------------------------------------------------------------------------|---------------------------------|
| Threat Agent         | Entity capable of exploiting vulnerabilities (e.g., hackers, adversarial data sources) | NIST SP 800-160                 |
| Attack Vector        | Pathway through which a threat agent compromises the system (e.g., poisoned training data) | ISO/IEC 23894                   |
| Vulnerability        | Weakness in AI system design or implementation enabling exploitation       | MITRE ATT&CK for AI             |
| Risk Exposure        | Likelihood and impact of a threat materializing                             | OECD AI Principles              |
| Adversarial Example  | Input crafted to mislead AI models without altering semantic intent       | Goodfellow et al. (2015)        |
| Model Inversion      | Reconstructing sensitive training data from model outputs                 | Fredrikson et al. (2015)        |
| Evasion Attack       | Manipulating inputs to bypass model detection (e.g., spam filters)        | Biggio et al. (2013)            |
| Data Poisoning       | Corrupting training data to degrade model performance or inject bias      | Papernot et al. (2018)          |

## Industry Standards
- NIST AI Risk Management Framework (RMF)
- ISO/IEC 23894:2021 (AI Trustworthiness)
- MITRE ATT&CK for AI (adversarial tactics)
- OECD AI Principles (risk governance)
- arXiv:2106.11346 (AI Security Taxonomy)

## Common Patterns
1. **Adversarial Training** – Hardening models against known attack patterns.
2. **Input Sanitization** – Filtering inputs to prevent injection attacks.
3. **Model Watermarking** – Embedding fingerprints to detect unauthorized use.
4. **Federated Learning** – Decentralizing data to reduce poisoning risks.
5. **Red Teaming** – Simulating adversarial attacks during development.

## Pitfalls
- Overlooking supply chain risks in third-party model components.
- Assuming model robustness without validating against real-world attack surfaces.
- Confusing threat modeling with compliance checklists (e.g., GDPR).
- Neglecting post-deployment monitoring for evolving threats.
- Failing to quantify risk exposure in terms of business impact.
