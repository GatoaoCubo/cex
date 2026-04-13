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
quality: 8.5
version: "2.0"
last_hydrated: "2026-04-13"
sources:
  - https://github.com/UKGovernmentBEIS/control-arena
  - https://control-arena.aisi.org.uk/
  - https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
  - https://www.nist.gov/itl/ai-risk-management-framework
  - https://dl.acm.org/doi/10.1145/3696410.3714705
  - https://docs.nvidia.com/nemo/guardrails/latest/index.html
  - https://guardrailsai.com
  - https://learn.microsoft.com/en-us/azure/ai-services/content-safety/
  - https://platform.openai.com/docs/guides/safety-best-practices
---

# AI Safety Knowledge Card

## 1. Hazard Sources

### 1.1 Aegis 2.0 Categories
| Hazard | OWASP Mapping | NIST GAI Risk | Safety Property |
|--------|----------------|----------------|------------------|
| H01 Hate | -- | Toxicity/Bias | Fairness |
| H02 Sexual | -- | Obscene Content | Legality |
| H03 Illegal Activity | LLM05 (Output) | Information Security | Legality |
| H04 Suicide/Self-Harm | -- | -- | Toxicity |
| H05 Violence | -- | -- | Toxicity |
| H06 Immoral/Unethical | -- | -- | Fairness |
| H07 Guns/Weapons | -- | CBRN | Legality |
| H08 Threat | -- | -- | Toxicity |
| H09 Unauthorized Advice | LLM09 (Misinfo) | Human-AI Config | Hallucination |
| H10 PII/Privacy | LLM02 | Data Privacy | Privacy |
| H11 Political/Misinfo | LLM09 | Information Integrity | Hallucination |
| H12 Harassment | -- | Toxicity/Bias | Toxicity |
| S08 Malware | LLM05 (Output) | Information Security | Legality |

---

## 2. Defense Methods

### 2.1 Guardrail Types
| Type | Purpose | Source |
|------|---------|--------|
| Input Guardrail | Filter malicious inputs | Safeguarding Survey |
| Output Guardrail | Sanitize outputs for safety | OWASP LLM05 |
| RAG Guardrail | Validate retrieval provenance | OWASP LLM08 |
| Tool Guardrail | Restrict agent tool usage | OWASP LLM06 |
| PII Redaction | Remove sensitive data | OWASP LLM02 |
| Prompt Isolation | Prevent system prompt leakage | OWASP LLM07 |
| Rate Limiting | Prevent resource exhaustion | OWASP LLM10 |
| Grounding Check | Verify factual accuracy | Safeguarding Survey |

### 2.2 Additional Defenses
- **Classifier-based Guardrail**: Use ML models to detect unsafe content.
- **Behavioral Circuit Breaker**: Terminate harmful agent behavior.
- **Prompt Shield**: Block adversarial prompts.
- **Trusted Monitoring**: Use verified models for safety checks.
- **Signal Jamming**: Disrupt adversarial input patterns.

---

## 3. Evaluation Methods

### 3.1 Red Team Evaluations
| Type | Focus | Source |
|------|-------|--------|
| Jailbreak Evaluation | Test prompt injection resistance | Aegis + OWASP |
| Injection Evaluation | Assess direct/indirect prompt attacks | OWASP LLM01 |
| Exfiltration Evaluation | Detect data/prompt extraction | OWASP LLM02 + LLM07 |
| Poisoning Evaluation | Validate robustness to data poisoning | OWASP LLM04 |

### 3.2 ControlArena Metrics
| Metric | Description |
|--------|-------------|
| **Safety** | Probability of safe agent behavior |
| **Usefulness** | Effectiveness of agent outputs |
| **Suspicion Score** | Likelihood of adversarial intent |
| **Sneakiness Score** | Stealth of adversarial attacks |

---

## 4. Alignment with Frameworks

### 4.1 OWASP LLM Top 10 Coverage
| OWASP | guardrail | red_team_eval | hitl_config | permission |
|-------|-----------|---------------|-------------|------------|
| LLM01 Prompt Injection | Input filter | Injection eval | -- | -- |
| LLM02 Sensitive Info | Output filter + PII redaction | Exfiltration eval | -- | Data access |
| LLM03 Supply Chain | Provenance check | -- | -- | -- |
| LLM04 Data Poisoning | -- | Poisoning eval | -- | -- |
| LLM05 Improper Output | Output sanitization | -- | -- | -- |
| LLM06 Excessive Agency | Tool sandbox | -- | High-stakes approval | Tool ACL |
| LLM07 Prompt Leakage | Prompt isolation | Extraction eval | -- | -- |
| LLM08 Vector Weakness | RAG integrity | -- | -- | -- |
| LLM09 Misinformation | Grounding check | -- | -- | -- |
| LLM10 Unbounded Consumption | Rate limiting | -- | -- | -- |

---

## 5. Key Concepts

### 5.1 Control Paradigms
- **AI Control**: Framework for managing agent behavior (ControlArena).
- **Control Protocol**: Rules governing agent safety (ControlArena).
- **Control Evaluation**: Red team testing of safety measures (ControlArena).

### 5.2 Threat Models
- **Attack Policy (U_A)**: Adversarial strategies for exploitation (ControlArena).
- **Backdoor**: Hidden malicious logic in models (ControlArena).
- **Collusion**: Coordinated attacks between agents (ControlArena).
- **Sandbagging**: Model performance degradation under stress (ControlArena).
- **Scheming**: Deceptive behavior to bypass safety checks (ControlArena).

### 5.3 Safety Properties
- **Fairness**: Avoid bias in outputs (Safeguarding Survey).
- **Legality**: Compliance with laws (Safeguarding Survey).
- **Privacy**: Protect user data (Safeguarding Survey).
- **Robustness**: Resistance to adversarial inputs (Safeguarding Survey).
- **Hallucination**: Prevention of false information (Safeguarding Survey).
- **Toxicity**: Avoid harmful content (Safeguarding Survey).

---

## 6. Vocabulary Quick Reference

| Term | Domain | Source |
|------|--------|--------|
| Adaptive Deployment | Control | ControlArena |
| AI Control | Paradigm | ControlArena |
| Attack Policy (U_A) | Control | ControlArena |
| Audit Budget | Control | ControlArena |
| Backdoor | Threat | ControlArena |
| Behavioral Circuit Breaker | Defense | Safeguarding Survey |
| Blue Team | Evaluation | ControlArena |
| CBRN | Hazard | NIST GAI |
| Classifier-based Guardrail | Defense | Safeguarding Survey |
| Collusion | Threat | ControlArena |
| Confabulation | Hazard | NIST GAI |
| Constitution | Alignment | Constitutional AI |
| Content Filter | Defense | Safeguarding Survey |
| Control Evaluation | Evaluation | ControlArena |
| Control Protocol | Defense | ControlArena |
| Corrigibility | Safety Property | Constitutional AI |
| Critique | Alignment | Constitutional AI |
| Data Poisoning | Attack | OWASP LLM04 |
| Defer to Resample | Control | ControlArena |
| Defer to Trusted | Control | ControlArena |
| Direct Prompt Injection | Attack | OWASP LLM01 |
| DPO | Alignment | General |
| Elicitation | Evaluation | ControlArena |
| Embedding Poisoning | Attack | OWASP LLM08 |
| Evasive Refusal | Anti-pattern | Constitutional AI |
| Excessive Agency | Vulnerability | OWASP LLM06 |
| Exploit | Threat | ControlArena |
| Fairness | Safety Property | Safeguarding Survey |
| Fine-tuning Attack | Attack | Safeguarding Survey |
| GPT-4 | Model | OpenAI |
| Hallucination | Safety Property | Safeguarding Survey |
| Human-in-the-Loop (HITL) | Alignment | General |
| Inverse Reinforcement Learning (IRL) | Alignment | General |
| Prompt Injection | Attack | OWASP LLM01 |
| Prompt Isolation | Defense | OWASP LLM07 |
| Prompt Injection | Attack | OWASP LLM01 |
| Red Team | Evaluation | ControlArena |
| Reinforcement Learning from Human Feedback (RLHF) | Alignment | General |
| Safety Alignment | Alignment | General |
| Toxicity | Safety Property | Safeguarding Survey |
| Zero-Shot Learning | Alignment | General |

---

## 7. Cross-Reference Tables

### 7.1 Defense-Attack Mapping
| Attack | Defense |
|--------|---------|
| Prompt Injection | Input Guardrail, Prompt Isolation |
| Data Poisoning | RAG Guardrail, Poisoning Evaluation |
| Exfiltration | Output Guardrail, PII Redaction |
| Hallucination | Grounding Check, Fact-Checking |
| Excessive Agency | Tool Guardrail, HITL |

### 7.2 Framework Alignment
| Framework | Focus Area | Key Contributions |
|-----------|-------------|-------------------|
| Aegis | Hazard Classification | H01-H12, S08 |
| OWASP | Attack Vectors | LLM01-LLM10 |
| NIST | Legal Compliance | CBRN, Data Privacy |
| ControlArena | Evaluation Metrics | Safety, Usefulness, Suspicion Score |
| Constitutional AI | Alignment | Critique, Corrigibility |

---

## 8. Summary

This knowledge card provides a comprehensive overview of AI safety, including hazard sources, defense mechanisms, evaluation methods, and alignment with industry frameworks. By integrating insights from Aegis, OWASP, NIST, and ControlArena, it offers a structured approach to ensuring safe, ethical, and compliant AI systems. Key areas of focus include robust guardrail design, rigorous red team testing, and alignment with legal and ethical standards.