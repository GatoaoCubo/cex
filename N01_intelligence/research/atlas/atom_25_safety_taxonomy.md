---
id: atom_25_safety_taxonomy
title: AI Safety Knowledge Card
kind: knowledge_card
pillar: P01
domain: ai_safety
pipeline: 8F (F1-F8)
scorer: cex_score.py
compiler: cex_compile.py
retriever: cex_retriever.py
quality_target: 9.0+
density_target: 0.85+
quality: 9.0
version: "2.0"
last_hydrated: "2026-04-13"
sources:
  - https://github.com/UKGovernmentBEIS/control-arena
  - https://control-arena.aisi.org.uk/
  - https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
  - https://www.nist.gov/itl/ai-risk-management-framework
  - https://dl.acm.org/doi/10.1145/3696410.3714705
  - https://arxiv.org/abs/2305.05385
  - https://www.openai.com/research/gpt-4
  - https://owasp.org/www-project-top-10/
  - https://www.iso.org/standard/74128.html
  - https://www.aegis.ai/whitepaper

---

## Boundary

This artifact is a structured reference for AI safety concepts, frameworks, and evaluation methods. It is NOT a policy document, technical implementation guide, or legal compliance checklist.

## Related Kinds

- **Framework**: Provides overarching principles for AI safety (e.g., NIST, OWASP).
- **Taxonomy**: Categorizes hazards and defenses (e.g., Aegis 2.0).
- **Evaluation Method**: Defines red team testing and metrics (e.g., ControlArena).
- **Defense Mechanism**: Describes guardrail types and implementation (e.g., input/output filters).
- **Alignment Guideline**: Outlines ethical and legal alignment strategies (e.g., Constitutional AI).

---

## 1. Hazard Sources

### 1.1 Aegis 2.0 Categories

| Hazard Code | Description | Impact Severity | Mitigation Strategy | Relevant Framework |
|------------|-------------|------------------|----------------------|--------------------|
| H01        | Hate Speech | High             | Content filtering    | GDPR, Aegis        |
| H02        | Misinformation | Medium         | Fact-checking        | NIST               |
| H03        | Bias Amplification | High       | Algorithmic auditing | ISO/IEC 23894      |
| H04        | Privacy Violations | Critical     | Data anonymization   | CCPA               |
| H05        | Malicious Use | Critical         | Access controls      | OECD AI Principles |
| H06        | Systemic Risk | High             | Redundancy protocols | ISO 31000         |
| H07        | Legal Noncompliance | Medium     | Compliance monitoring | GDPR              |
| H08        | Ethical Violations | High        | Human oversight      | EU Ethics Board     |
| H09        | Environmental Harm | Medium     | Energy efficiency    | UN Sustainable Goals|
| H10        | Economic Disruption | High      | Impact assessments   | World Bank         |
| H11        | Social Harm | Medium           | Community engagement | UN Human Rights    |
| H12        | Technical Failure | Critical     | Fail-safe design     | ISO 26000         |
| S08        | Security Breach | Critical       | Encryption protocols | NIST SP 800-171    |

---

## 2. Defense Mechanisms

### 2.1 Guardrail Types

| Defense Type | Purpose | Implementation Method | Source |
|--------------|---------|------------------------|--------|
| Input Guardrail | Filter harmful inputs | NLP-based classifiers | OWASP |
| Output Guardrail | Sanitize model outputs | Post-processing filters | Aegis |
| Prompt Isolation | Prevent prompt injection | Token-level validation | OWASP LLM07 |
| Tool Guardrail | Limit API access | Role-based access control | ControlArena |
| HITL Guardrail | Human oversight | Interactive feedback loops | Constitutional AI |
| RAG Guardrail | Verify external data | Source credibility checks | Aegis |
| Poisoning Defense | Detect data tampering | Anomaly detection models | NIST |
| Exfiltration Defense | Prevent data leaks | Data flow monitoring | ISO/IEC 27001 |

---

## 3. Evaluation Metrics

### 3.1 ControlArena Metrics

| Metric | Description | Scale | Use Case |
|--------|-------------|-------|----------|
| Safety Score | Risk mitigation effectiveness | 0-100 | Deployment readiness |
| Usefulness Score | Task completion accuracy | 0-100 | Model evaluation |
| Suspicion Score | Anomaly detection | 0-100 | Security audits |
| Ethical Alignment | Compliance with principles | 0-100 | Governance reviews |
| Legal Compliance | Adherence to regulations | 0-100 | Audits |

---

## 4. Framework Alignment

### 4.1 Cross-Reference Table

| Framework | Focus Area | Key Contributions | Integration Strategy |
|----------|------------|-------------------|----------------------|
| Aegis | Hazard Classification | 12 hazard codes + security breach | Used for risk mapping |
| OWASP | Attack Vectors | LLM01-LLM10 | Integrated into defense design |
| NIST | Legal Compliance | CBRN, Data Privacy | Applied to mitigation strategies |
| ControlArena | Evaluation | Safety, Usefulness, Suspicion Score | Used for performance benchmarking |
| Constitutional AI | Alignment | Critique, Corrigibility | Embedded in HITL workflows |
| ISO/IEC 23894 | Algorithmic Auditing | Bias detection | Applied to mitigation strategies |
| OECD AI Principles | Ethics | Fairness, Transparency | Used in alignment guidelines |

---

## 5. Safety Properties

### 5.1 Safety Property Matrix

| Property | Description | Relevant Frameworks | Mitigation Strategies |
|---------|-------------|----------------------|------------------------|
| Fairness | Equitable treatment | Aegis, ISO/IEC 23894 | Bias detection algorithms |
| Transparency | Explainability | OECD AI Principles | Model interpretability tools |
| Accountability | Traceability | GDPR, NIST | Audit logs and provenance tracking |
| Privacy | Data protection | CCPA, ISO/IEC 27001 | Anonymization and encryption |
| Security | System integrity | NIST SP 800-171 | Access controls and encryption |
| Reliability | Consistency | ISO 31000 | Redundancy and fail-safes |
| Robustness | Resistance to attacks | OWASP LLM01 | Adversarial training |
| Sustainability | Environmental impact | UN Sustainable Goals | Energy-efficient models |

---

## 6. Defense-Attack Mapping

### 6.1 Attack-Defense Table

| Attack Type | Defense Mechanism | Implementation | Source |
|-------------|-------------------|----------------|--------|
| Prompt Injection | Input Guardrail + Prompt Isolation | Token validation + NLP filters | OWASP LLM01 |
| Data Poisoning | RAG Guardrail + Poisoning Evaluation | Source credibility checks + anomaly detection | NIST |
| Exfiltration | Output Guardrail + PII Redaction | Output sanitization + data masking | ISO/IEC 27001 |
| Hallucination | Grounding Check + Fact-Checking | External knowledge verification | Aegis |
| Excessive Agency | Tool Guardrail + HITL | API access control + human feedback | ControlArena |

---

## 7. Alignment Strategies

### 7.1 Alignment Frameworks

| Alignment Method | Description | Key Use Cases | Tools/Techniques |
|------------------|-------------|----------------|------------------|
| RLHF | Reinforcement learning from human feedback | Fine-tuning models | Human feedback loops |
| DPO | Direct preference optimization | Preference alignment | Preference data collection |
| IRL | Inverse reinforcement learning | Goal inference | Reward function modeling |
| HITL | Human-in-the-loop | Continuous oversight | Interactive interfaces |
| Corrigibility | Model correction | Error correction | Feedback mechanisms |
| Critique | Ethical evaluation | Alignment checks | Human review panels |

---

## 8. Summary

This knowledge card provides a comprehensive overview of AI safety, including hazard sources, defense mechanisms, evaluation methods, and alignment with industry frameworks. By integrating insights from Aegis, OWASP, NIST, and ControlArena, it offers a structured approach to ensuring safe, ethical, and compliant AI systems. Key areas of focus include robust guardrail design, rigorous red team testing, and alignment with legal and ethical standards. The artifact serves as a reference for developers, auditors, and policymakers navigating the complex landscape of AI safety.