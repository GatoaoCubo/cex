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
related:
  - kc_guardrail
  - safety-policy-builder
  - bld_architecture_guardrail
  - guardrail-builder
  - atom_24_nist_vocabulary
  - kc_compliance_framework
  - bld_knowledge_card_compliance_framework
  - bld_instruction_guardrail
  - p03_sp_guardrail_builder
  - bld_examples_safety_policy
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

---

## 9. ControlArena Implementation (UK AISI)

**Source**: https://github.com/UKGovernmentBEIS/control-arena
**Docs**: https://control-arena.aisi.org.uk/
**Blog**: https://www.aisi.gov.uk/blog/introducing-controlarena-a-library-for-running-ai-control-experiments

### 9.1 What It Is

ControlArena is an open-source Python library by the UK AI Security Institute (AISI) for running AI control experiments. Built on top of the Inspect AI evaluation library. Used by Anthropic, Google DeepMind, and Redwood Research. Supports AI Control Hackathon 2026 (co-organized with Redwood Research).

### 9.2 Installation

```bash
pip install control-arena

git clone https://github.com/UKGovernmentBEIS/control-arena.git
cd control-arena
pip install -e .

pip install inspect-ai
```

### 9.3 Running Evaluations

```python
from inspect_ai import eval, eval_set

result = eval(task, model="anthropic/claude-sonnet-4-20250514")

results = eval_set(tasks, model="openai/gpt-4.1-mini-2025-04-14",
                   max_retries=3, cache=True)
```

### 9.4 Control Protocols

| Protocol | Description | Use Case |
|----------|-------------|----------|
| Defer to Trusted | Route high-stakes decisions to trusted model | Production safety |
| Defer to Resample | Regenerate on suspicion signal | Quality assurance |
| Adaptive Deployment | Adjust oversight level by risk score | Dynamic safety |
| Audit Budget | Limit expensive checks to X% of calls | Cost-aware safety |
| Blue Team | Honest agent trying to complete task | Control baseline |
| Red Team (U_A) | Adversarial attack policy simulation | Threat modeling |

### 9.5 Metrics

| Metric | Type | Interpretation |
|--------|------|----------------|
| Safety Score | P(safe) 0-1 | Probability of no unsafe action in episode |
| Usefulness Score | P(useful) 0-1 | Task completion rate |
| Suspicion Score | 0-1 | Likelihood of adversarial intent |
| Sneakiness Score | 0-1 | Stealth level of adversarial attacks |

---

## 10. Guardrail Frameworks: Setup Guide

### 10.1 Framework Comparison

| Framework | Tier | Install | Self-hosted? | Multimodal? |
|-----------|------|---------|--------------|-------------|
| NeMo Guardrails (NVIDIA) | Open-source | pip | Yes | Yes |
| Guardrails.ai | Open-source | pip/npm | Yes | Partial |
| LlamaGuard (Meta) | Open-source model | pip/hf | Yes | Yes (v3+) |
| Aegis (NVIDIA) | Dataset + model | hf | Yes | No |
| Azure Content Safety | Cloud API | SDK | No | Yes |
| AWS Bedrock Guardrails | Cloud API | boto3 | No | Yes |
| Google SafetySettings | Cloud API | SDK | No | Yes |
| OpenAI Moderation API | Cloud API | SDK | No | Yes (omni) |

### 10.2 NeMo Guardrails

**Repo**: https://github.com/NVIDIA-NeMo/Guardrails
**Docs**: https://docs.nvidia.com/nemo/guardrails/latest/index.html

```bash
pip install nemoguardrails
pip install "nemoguardrails[nvidia]"
```

Features: Colang DSL, Aegis Protocol integration, denied topics, sensitive info/word/image filters, Inspect AI integration.

### 10.3 Guardrails.ai

**Repo**: https://github.com/guardrails-ai/guardrails
**Docs**: https://www.guardrailsai.com/docs/guardrails_ai/installation

```bash
pip install guardrails-ai
guardrails configure
```

Features: Validators from Guardrails Hub, PII detection, enterprise AI guardrails, OpenAPI client SDKs.

### 10.4 LlamaGuard (Meta)

**Models**: LG3-8B (https://huggingface.co/meta-llama/Llama-Guard-3-8B), LG4-12B (https://huggingface.co/meta-llama/Llama-Guard-4-12B)

```bash
pip install vllm
pip install llama-cpp-python
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
```

Features: MLCommons hazard taxonomy, multilingual, vision (LG3 11B), malicious code detection.

### 10.5 Aegis (NVIDIA)

**Dataset**: https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0

```python
from transformers import pipeline
classifier = pipeline("text-classification",
                      model="nvidia/Aegis-AI-Content-Safety-LlamaGuard-Permissive-1.0")
```

Features: 35,000 human-annotated samples, H01-H12+S08 taxonomy, zero-trust identity layer.

### 10.6 Azure Content Safety

**Docs**: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/

```bash
pip install azure-ai-contentsafety azure-identity
```

Features: Text + image moderation, blocklist management, multi-language SDKs.

### 10.7 AWS Bedrock Guardrails

**Docs**: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html

```python
import boto3
bedrock = boto3.client("bedrock")
guardrail = bedrock.create_guardrail(
    name="my-guardrail",
    contentPolicyConfig={"filtersConfig": [
        {"type": "SEXUAL", "inputStrength": "HIGH", "outputStrength": "HIGH"}
    ]},
    sensitiveInformationPolicyConfig={"piiEntitiesConfig": [
        {"type": "EMAIL", "action": "ANONYMIZE"}
    ]}
)
```

Features: Content filters, denied topics, PII filtering, CloudFormation support.

### 10.8 Google SafetySettings

**Docs**: https://ai.google.dev/gemini-api/docs/safety-settings

```python
import google.generativeai as genai
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=[
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_HIGH_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
    ]
)
```

Features: 4 adjustable harm categories, core protections always active (child safety).

### 10.9 OpenAI Moderation API

**Docs**: https://platform.openai.com/docs/api-reference/moderations

```python
from openai import OpenAI
client = OpenAI()
moderation = client.moderations.create(
    model="omni-moderation-latest",
    input="text to classify"
)
if moderation.results[0].flagged:
    print({k: v for k, v in moderation.results[0].categories.__dict__.items() if v})
```

Features: Free endpoint, omni-moderation (text + images), scores per category.

---

## 11. Constitutional AI: Principles to NIST Mapping

**Constitution (2026)**: https://www.anthropic.com/news/claudes-constitution
**CAI paper**: https://arxiv.org/abs/2212.08073

### 11.1 CAI Priority Hierarchy

The 2026 Constitution (23,000 words, 58 principles) defines strict priority order.
When conflicts arise: Safety > Ethics > Guidelines > Helpfulness.

| Priority | Principle Category | Description |
|----------|--------------------|-------------|
| 1 | Broadly Safe | No undermining human oversight mechanisms |
| 2 | Broadly Ethical | Honest, good values, avoids harmful actions |
| 3 | Anthropic Compliant | Follows specific Anthropic guidelines |
| 4 | Genuinely Helpful | Benefits operators and users |

### 11.2 CAI to NIST AI RMF Mapping

| CAI Category | NIST AI RMF Function | NIST GAI Risk | CEX Guardrail Kind |
|---|---|---|---|
| Broadly Safe -- Corrigibility | GOVERN 1.1 (AI Risk Policy) | Human-AI Configuration | hitl_config |
| Broadly Safe -- No deception | MAP 1.5 (Identify Limitations) | Confabulation | guardrail (output) |
| Broadly Safe -- Support oversight | GOVERN 1.4 (Accountability) | Oversight Mechanisms | permission |
| Broadly Ethical -- Honesty | MEASURE 2.5 (Trustworthiness) | Confabulation/Hallucination | guardrail (grounding) |
| Broadly Ethical -- Non-maleficence | MAP 2.2 (Risk Context) | CBRN / Toxicity | guardrail (input) |
| Broadly Ethical -- Fairness | MANAGE 1.3 (Risk Response) | Bias/Toxicity | guardrail (output) |
| Compliant -- Data Privacy | MAP 1.6 (Privacy Risks) | Data Privacy/PII | permission (data) |
| Compliant -- Legal | GOVERN 5.1 (Governance) | Information Security | guardrail (legal) |
| Helpful -- No evasive refusal | MEASURE 2.1 (Performance) | -- | quality_gate |

### 11.3 Constitutional Classifiers (2025)

Source: https://www.anthropic.com/research/constitutional-classifiers

CAI principles operationalized as training-time classifiers defend against universal jailbreaks.
Results vs. vanilla RLHF: significantly higher jailbreak resistance on AdvBench/HarmBench,
maintained helpfulness on MMLU (< 2% degradation), generalizes across attack types.

### 11.4 C3AI Research Finding (2025)

Source: https://dl.acm.org/doi/10.1145/3696410.3714705

Positively-framed, behavior-based principles outperform negatively-framed or trait-based ones.
CEX implication: write guardrail rules as "Do X" not "Don't Y", describe behaviors not traits.

---

## 12. 2025-2026 Safety Research: Key Papers

### 12.1 Benchmarks

| Paper | Key Contribution | Source |
|-------|-----------------|--------|
| International AI Safety Report 2026 | 100+ experts, 30+ countries | https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026 |
| International AI Safety Report 2025 | Risk taxonomies, eval methods | https://arxiv.org/abs/2510.13653 |
| AI Safety Index Winter 2025 | Comparative rankings across labs | https://futureoflife.org/ai-safety-index-winter-2025/ |
| TrustLLM Benchmark | 6 dimensions: truthfulness, safety, fairness, robustness, privacy, ethics | Multi-venue 2025 |
| Stanford AIR-Bench 2024 | Aligned with EU AI Act, NIST | Stanford CRFM |

### 12.2 Guardrails Research

| Paper | Finding | Source |
|-------|---------|--------|
| Diverse AI Safety Dataset (Ghosh et al. 2025) | New taxonomy from real-world harm reports | arXiv 2025 |
| Polyguard (Kumar et al. 2025) | Multilingual safety for 17 languages | arXiv 2025 |
| OMNIGUARD (Verma et al. 2025) | Cross-modal safety moderation | arXiv 2025 |
| Proof-of-Guardrail in AI Agents | What to trust from guardrail attestations | https://arxiv.org/html/2603.05786 |
| Safeguarding LLMs: A Survey (Springer 2025) | Taxonomy + defenses comprehensive review | https://link.springer.com/article/10.1007/s10462-025-11389-2 |

---

## 13. CEX Safety Implementation Checklist

### 13.1 Pre-Deployment Checklist

```
INPUT LAYER
[ ] Input guardrail configured (blocks H01-H12, S08)
[ ] Prompt injection filter active (OWASP LLM01)
[ ] PII detection on user inputs (OWASP LLM02)
[ ] Token budget enforced (OWASP LLM10)
[ ] Rate limiting per user/session (OWASP LLM10)

OUTPUT LAYER
[ ] Output sanitization for harmful content (OWASP LLM05)
[ ] Hallucination/grounding check enabled (OWASP LLM09)
[ ] PII redaction before response (OWASP LLM02)
[ ] Prompt isolation (no system prompt leakage) (OWASP LLM07)

AGENT/TOOL LAYER
[ ] Tool ACL defined (minimum permissions) (OWASP LLM06)
[ ] HITL triggers for high-stakes actions (OWASP LLM06)
[ ] RAG provenance validation (OWASP LLM08)
[ ] Supply chain provenance check on models (OWASP LLM03)

ALIGNMENT LAYER
[ ] CAI priority order enforced: Safety > Ethics > Guidelines > Helpful
[ ] Corrigibility: agent supports human oversight
[ ] No deceptive outputs enabled
[ ] No evasive refusals (helpfulness floor maintained)
[ ] Guardrail rules written as "Do X", not "Don't Y"

EVALUATION LAYER
[ ] ControlArena red team eval scheduled (monthly minimum)
[ ] Jailbreak evaluation baseline documented
[ ] Safety/Usefulness trade-off measured and logged
[ ] Regression check after every model update
```

### 13.2 Guardrail Selection by Scenario

| Scenario | Recommended Guardrail | Reason |
|----------|----------------------|--------|
| Open-source, self-hosted, Python | NeMo Guardrails | Most configurable, Aegis integration |
| Enterprise SaaS on Azure | Azure Content Safety | Native Azure, compliance |
| AWS-native deployment | AWS Bedrock Guardrails | CloudFormation, IAM |
| Google Cloud / Vertex AI | Google SafetySettings | Built-in Gemini integration |
| OpenAI-based pipelines | OpenAI Moderation API | Free, same provider, omni |
| Meta LLaMA self-hosted | LlamaGuard 4 12B | Same model family, no external API |
| Custom taxonomy needed | Guardrails.ai | Hub ecosystem, custom validators |
| Research / eval pipeline | ControlArena | Built for control experiments |

### 13.3 CEX Nucleus Safety Matrix

| Nucleus | Primary Risk | Guardrail Layer | CAI Category |
|---------|-------------|-----------------|--------------|
| N01 Research | Hallucination, misinfo | Grounding check, citation required | Broadly Ethical (honesty) |
| N02 Marketing | Deceptive claims | Output filter, legal review | Broadly Ethical (non-maleficence) |
| N03 Builder | Code injection, supply chain | Tool sandbox, provenance check | Broadly Safe (oversight) |
| N04 Knowledge | Data poisoning, embedding attack | RAG integrity, source validation | Broadly Ethical (honesty) |
| N05 Operations | Privilege escalation, code exec | Permission ACL, HITL for deploy | Broadly Safe (corrigibility) |
| N06 Commercial | Misleading pricing, fraud | Legal compliance check | Compliant (legal) |
| N07 Orchestrator | Excessive agency, collusion | HITL for multi-nucleus dispatch | Broadly Safe (human oversight) |

---

## 14. Vocabulary Additions (v2.0)

| Term | Domain | Source |
|------|--------|--------|
| Broadly Ethical | CAI Priority | Anthropic Constitution 2026 |
| Broadly Safe | CAI Priority | Anthropic Constitution 2026 |
| C3AI Framework | Alignment Research | ACM Web Conf 2025 |
| CAI Priority Hierarchy | Alignment | Anthropic Constitution 2026 |
| Constitutional Classifier | Defense | Anthropic 2025 |
| Genuinely Helpful | CAI Priority | Anthropic Constitution 2026 |
| Guardrails Hub | Tooling | Guardrails.ai |
| International AI Safety Report 2026 | Benchmark | Bengio et al. 2026 |
| Llama Guard 4 | Defense Model | Meta 2025 |
| MLCommons Hazard Taxonomy | Standard | MLCommons 2025 |
| NIST-AI-600-1 | Standard | NIST 2024 |
| omni-moderation-latest | Model | OpenAI 2025 |
| Polyguard | Defense | Kumar et al. 2025 |
| Proof-of-Guardrail | Attestation | arXiv 2026 |
| TrustLLM | Benchmark | Multi-institution 2025 |
| Universal Jailbreak | Attack | Research 2025 |
---

## 9. ControlArena Implementation Guide (UK AISI)

### 9.1 What Is ControlArena

ControlArena is a Python evaluation library developed by UK AI Security Institute (AISI)
and Redwood Research. Measures whether AI agents can covertly execute malicious side-tasks
while completing legitimate objectives via red-team/blue-team protocols.

Code: https://github.com/UKGovernmentBEIS/control-arena
Docs: https://control-arena.aisi.org.uk/

### 9.2 Architecture

| Component | Role | Description |
|-----------|------|-------------|
| Inspect AI | Evaluation framework | Python-based task runner |
| Bash Task Environment | Simulates sysadmin scenarios | Stack Overflow-derived bash scripts |
| Red Team (U_A) | Adversary policy | Attempts covert side-task during legitimate task |
| Blue Team | Safety monitor | Applies control protocol to detect/block attacks |
| Side Task | Hidden attack | e.g., download malware, exfiltrate credentials |
| Main Task | Legitimate objective | e.g., complete a bash scripting assignment |

### 9.3 Setup Instructions

```bash
git clone https://github.com/UKGovernmentBEIS/control-arena
cd control-arena
uv sync
uv run human-trajectories agent setup --main-task-name BashTask
uv run inspect eval control_arena/settings/bash/bash_task.py \
  --model anthropic/claude-3-5-sonnet-20241022 --limit 50
```

### 9.4 Evaluation Metrics (CTRL-Z Study, Matolcsi et al. 2025)

| Metric | Description | Baseline | With Control Protocol |
|--------|-------------|----------|-----------------------|
| Safety | P(attack prevented) | 42% | 93% |
| Usefulness | P(main task completed) | 97% | 95% |
| Suspicion Score | P(adversarial intent detected) | 0.21 | 0.74 |
| Sneakiness Score | P(attack undetected) | 0.58 | 0.07 |

Control protocols reduced attack success from 58% to 7% while maintaining 95% usefulness.

### 9.5 Control Protocols

| Protocol | Strategy | When to Use |
|----------|----------|-------------|
| Trusted Monitoring | Verified model checks outputs | High-stakes production |
| Defer to Trusted | Escalate uncertain actions to human | Irreversible operations |
| Defer to Resample | Regenerate if flagged | Routine tasks |
| Audit Budget | Allocate N human review slots per session | Resource-constrained |
| Adaptive Deployment | Adjust trust based on session history | Multi-session agents |

---

## 10. 8 Guardrail Frameworks: Implementation Reference

### 10.1 Comparison Matrix

| Framework | Vendor | License | Primary Defense |
|-----------|--------|---------|-----------------|
| NeMo Guardrails | NVIDIA | Apache 2.0 | Topic control, jailbreak, RAG grounding |
| LlamaGuard | Meta | Custom | Content classification (13 harm categories) |
| Guardrails AI | guardrailsai.com | Apache 2.0 | Pydantic-based validation + auto-fix |
| Rebuff | ProtectAI | MIT (archived 2025) | Prompt injection (heuristic+LLM+vector+canary) |
| Azure Content Safety | Microsoft | Commercial | Multi-harm filtering with configurable thresholds |
| Vertex AI Safety | Google | Commercial | Per-harm probability + severity scoring |
| Constitutional AI | Anthropic | N/A (system prompt) | Principle-based alignment |
| OpenAI Moderation | OpenAI | Free API | Harm category classification |

### 10.2 NVIDIA NeMo Guardrails

Source: https://github.com/NVIDIA/NeMo-Guardrails
Install: `pip install nemo-guardrails`

```python
from nemoguardrails import RailsConfig, LLMRails
config = RailsConfig.from_path('./config')
rails = LLMRails(config)
response = await rails.generate_async(prompt='user input')
```

### 10.3 LlamaGuard (Meta)

Source: https://docs.nvidia.com/nemo/guardrails/latest/user-guides/community/llama-guard.html
Serve: `python -m vllm.entrypoints.openai.api_server --port 5123 --model meta-llama/Llama-Guard-3-8B`

```python
import openai
client = openai.OpenAI(base_url='http://localhost:5123/v1', api_key='na')
result = client.chat.completions.create(
    model='meta-llama/Llama-Guard-3-8B',
    messages=[{'role': 'user', 'content': '[INPUT TO CHECK]'}]
)
# Returns: 'safe' or 'unsafe\nS<category-number>'
```

### 10.4 Guardrails AI

Source: https://guardrailsai.com
Install: `pip install guardrails-ai && guardrails hub install hub://guardrails/toxic_language`

```python
from guardrails import Guard
from guardrails.hub import ToxicLanguage
guard = Guard().use(ToxicLanguage, threshold=0.5, validation_method='sentence')
result = guard.validate('user text here')
```

### 10.5 Rebuff (Prompt Injection)

Note: Archived May 2025 -- migrate to Guardrails AI for new projects.

```python
from rebuff import Rebuff
rb = Rebuff(openai_apikey='sk-...', pinecone_apikey='...', pinecone_index='rebuff')
result = rb.detect_injection('Ignore previous instructions...')
# result.injectionDetected = True/False
# Defense layers: heuristics + LLM + VectorDB + canary tokens
```

### 10.6 Azure Content Safety

Source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/
Install: `pip install azure-ai-contentsafety`

```python
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeTextOptions
client = ContentSafetyClient(endpoint, AzureKeyCredential(key))
response = client.analyze_text(AnalyzeTextOptions(text='text to check'))
# severity: 0 (safe) to 7 (high) | categories: hate, violence, sexual, self_harm
```

### 10.7 Google Vertex AI Safety Filters

Source: https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters

```python
from vertexai.generative_models import (
    GenerativeModel, SafetySetting, HarmCategory, HarmBlockThreshold
)
safety_config = [
    SafetySetting(category=HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                  threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE),
    SafetySetting(category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                  threshold=HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE),
]
model = GenerativeModel('gemini-2.0-flash', safety_settings=safety_config)
```

### 10.8 Anthropic Constitutional AI System Prompt Pattern

Source: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback

```python
import anthropic
CONSTITUTION = (
    'Safety principles (non-overridable by user):\n'
    '1. Never provide CBRN weapon instructions (H07)\n'
    '2. Never generate content sexualizing minors (H02)\n'
    '3. Acknowledge uncertainty; do not confabulate (Hallucination)\n'
    '4. Refuse privacy-violating requests (H10)'
)
client = anthropic.Anthropic()
response = client.messages.create(
    model='claude-opus-4-6', max_tokens=1024,
    system=CONSTITUTION,
    messages=[{'role': 'user', 'content': 'user message'}]
)
```

### 10.9 OpenAI Moderation API

Source: https://platform.openai.com/docs/guides/safety-best-practices

```python
from openai import OpenAI
client = OpenAI()
result = client.moderations.create(
    model='omni-moderation-latest',
    input='text to check'
)
# result.results[0].flagged = True/False
# result.results[0].category_scores = per-category confidence 0.0-1.0
```

---

## 11. Constitutional AI Principles Mapped to NIST AI RMF

### 11.1 NIST AI RMF Core Functions

| Function | Description |
|----------|-------------|
| GOVERN | Risk governance structures, roles, policies, accountability |
| MAP | Context-setting -- categorize AI use cases and risks |
| MEASURE | Quantify risks via benchmarks, metrics, testing |
| MANAGE | Mitigate, monitor, respond to identified risks |

### 11.2 CAI Principles to NIST Mapping

| CAI Principle | NIST Function | Subcategory | Implementation |
|---------------|---------------|-------------|----------------|
| Harmlessness | GOVERN + MANAGE | GV-1.1, MG-2.2 | Safety policies defined; AI feedback enforces them |
| Honesty / No Confabulation | MEASURE | MS-2.5 | Hallucination metrics, grounding checks |
| Corrigibility | GOVERN | GV-4.1 | HITL approval flows, human override channels |
| Non-deception | MAP | MP-2.3 | Transparent capability disclosure, model cards |
| Avoiding Dual Use | MAP + MANAGE | MP-4.1, MG-3.1 | CBRN filters, weapon instruction refusals |
| Privacy Protection | MANAGE | MG-2.4 | PII redaction, data minimization |
| Avoiding Bias / Fairness | MEASURE + MANAGE | MS-2.6, MG-4.2 | Parity testing, output audits |
| Principle Abstraction | MAP | MP-3.2 | Domain-specific constitutions (medical, legal) |

### 11.3 Aegis Hazard + CAI + NIST GAI Cross-Reference

| NIST GAI Category | Aegis Code | CAI Principle | OWASP |
|-------------------|------------|---------------|-------|
| CBRN Information | H07 | Harmlessness (physical) | LLM05 |
| Data Privacy | H04, H10 | Privacy Protection | LLM02 |
| Information Integrity | H02, H11 | Honesty | LLM09 |
| Toxicity / Bias | H01, H12 | Fairness | -- |
| Human-AI Configuration | H09 | Corrigibility | LLM09 |
| Obscene Content | H02 | Harmlessness (content) | -- |
| Psychosocial Harms | H04 | Harmlessness (wellbeing) | -- |

Source: https://www.nist.gov/itl/ai-risk-management-framework

---

## 12. 2025-2026 Safety Research: Key Papers

| Paper | Venue | Year | Key Finding | URL |
|-------|-------|------|-------------|-----|
| C3AI: Crafting Constitutions for CAI | ACM Web 2025 | 2025 | Graph-based principle selection; mental health + legal alignment | https://dl.acm.org/doi/10.1145/3696410.3714705 |
| AgentHarm | ICLR 2025 | 2025 | LLM agent misuse benchmark across 110 harm categories | https://arxiv.org/abs/2410.09024 |
| CTRL-Z: AI Agent Control via Resampling | arXiv | 2025 | Control protocols reduce attack success 58% -> 7%; 95% usefulness retained | -- |
| Legal Alignment for Safe and Ethical AI | Oxford Internet Institute preprint | 2026 | Agentic AI compliance; maps CAI to EU AI Act | -- |

### 12.1 Safety Benchmarks (2025)

| Benchmark | Scope | Publisher | URL |
|-----------|-------|-----------|-----|
| AgentHarm | Agent misuse (110 categories) | AISI | https://arxiv.org/abs/2410.09024 |
| HarmBench | LLM attack success rate | UC Santa Barbara | https://www.harmbench.org/ |
| SALAD-Bench | Safety evaluation (30K items) | PKU | https://arxiv.org/abs/2402.05044 |
| StrongREJECT | Jailbreak success measurement | Stanford | https://arxiv.org/abs/2402.10260 |
| BELLS | Live safety evaluation streaming | ARC Evals | https://bells.theaira.ai/ |

---

## 13. CEX Safety Implementation Checklist

Practical checklist for deploying safe AI agents in CEX.
Maps to OWASP LLM Top 10, NIST AI RMF, and CEX guardrail kinds.

### 13.1 Input Layer

- [ ] [LLM01] Input guardrail deployed: prompt injection detection (Rebuff or NeMo)
- [ ] [LLM01] Indirect injection surface mapped: RAG, tool outputs, web scraper results
- [ ] [LLM07] System prompt isolation: user cannot read or override nucleus system prompt
- [ ] [H07] CBRN filter active: weapon/bioweapon instructions blocked
- [ ] [H10] PII detection in inputs: SSN, credit card, passwords blocked from context
- [ ] [CEX] Rate limiting: rate_limit_config.yaml per-nucleus thresholds configured

### 13.2 Output Layer

- [ ] [LLM05] Output sanitization: code injection, XSS, shell commands removed
- [ ] [LLM02] PII redaction: strip sensitive data before returning to user
- [ ] [LLM09] Grounding check: factual claims verified against retrieval sources
- [ ] [H01-H12] Content moderation: OpenAI Moderation API or Azure Content Safety on final output
- [ ] [CEX] output_validator kind deployed per nucleus

### 13.3 Agent / Tool Layer

- [ ] [LLM06] Tool ACL defined: each agent declares allowed tools in permission manifest
- [ ] [LLM06] HITL gates: git push, file delete, external API calls require approval
- [ ] [CEX] hitl_config.yaml: maps nuclei to approval requirements
- [ ] [ControlArena] Red team evaluation: bash task environment test before production
- [ ] [CEX] Behavioral circuit breaker: auto-terminate nucleus if suspicion_score > 0.7

### 13.4 Memory / RAG Layer

- [ ] [LLM08] RAG provenance: all retrieved chunks have source URL + confidence score
- [ ] [LLM04] Data poisoning prevention: knowledge index validates source integrity on ingest
- [ ] [LLM08] Embedding outlier detection: cosine similarity check flags anomalous new ingests
- [ ] [CEX] rag_source.yaml: all sources declared with trust level (high/medium/low)

### 13.5 Governance Layer

- [ ] [NIST GV] Safety policy documented: roles + accountability per safety function
- [ ] [NIST MP] Threat model written: attack surfaces identified per nucleus
- [ ] [NIST MS] Safety metrics tracked: suspicion_score, refusal_rate, toxicity_rate per session
- [ ] [NIST MG] Incident response plan: playbook for detected attacks
- [ ] [CAI] Constitutional principles in system prompt: every CEX nucleus carries safety constitution
- [ ] [CEX] quality gate: guardrail artifacts score >= 9.0 before deployment

### 13.6 CEX Kind Mapping for Safety

| Safety Domain | CEX Kind | Pillar | Nucleus |
|---------------|----------|--------|---------|
| Input filtering | guardrail | P11 | N03 |
| Output validation | output_validator | P05 | N03 |
| HITL approval | hitl_config | P12 | N07 |
| Tool permissions | permission | P08 | N07 |
| Rate limiting | rate_limit_config | P09 | N05 |
| Safety evaluation | red_team_eval | P07 | N05 |
| Threat modeling | decision_record | P08 | N07 |
| Quality gate | quality_gate | P11 | N03 |
| RAG integrity | rag_source | P01 | N04 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_guardrail]] | sibling | 0.28 |
| [[safety-policy-builder]] | downstream | 0.28 |
| [[bld_architecture_guardrail]] | downstream | 0.27 |
| [[guardrail-builder]] | downstream | 0.27 |
| [[atom_24_nist_vocabulary]] | sibling | 0.26 |
| [[kc_compliance_framework]] | sibling | 0.25 |
| [[bld_knowledge_card_compliance_framework]] | sibling | 0.25 |
| [[bld_instruction_guardrail]] | downstream | 0.25 |
| [[p03_sp_guardrail_builder]] | downstream | 0.23 |
| [[bld_examples_safety_policy]] | downstream | 0.23 |
