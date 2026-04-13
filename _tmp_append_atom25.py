"""Append enrichment sections 9-13 to atom_25_safety_taxonomy.md"""

SECTIONS = """

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
uv run inspect eval control_arena/settings/bash/bash_task.py \\
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
config = RailsConfig.from_path("./config")
rails = LLMRails(config)
response = await rails.generate_async(prompt="user input")
```

### 10.3 LlamaGuard (Meta)

Source: https://docs.nvidia.com/nemo/guardrails/latest/user-guides/community/llama-guard.html

Serve: `python -m vllm.entrypoints.openai.api_server --port 5123 --model meta-llama/Llama-Guard-3-8B`

```python
import openai
client = openai.OpenAI(base_url="http://localhost:5123/v1", api_key="na")
result = client.chat.completions.create(
    model="meta-llama/Llama-Guard-3-8B",
    messages=[{"role": "user", "content": "[INPUT TO CHECK]"}]
)
# Returns: "safe" or "unsafe\\nS<category-number>"
```

### 10.4 Guardrails AI

Source: https://guardrailsai.com
Install: `pip install guardrails-ai && guardrails hub install hub://guardrails/toxic_language`

```python
from guardrails import Guard
from guardrails.hub import ToxicLanguage
guard = Guard().use(ToxicLanguage, threshold=0.5, validation_method="sentence")
result = guard.validate("user text here")
```

### 10.5 Rebuff (Prompt Injection)

Note: Archived May 2025 -- migrate to Guardrails AI for new projects.

```python
from rebuff import Rebuff
rb = Rebuff(openai_apikey="sk-...", pinecone_apikey="...", pinecone_index="rebuff")
result = rb.detect_injection("Ignore previous instructions...")
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
response = client.analyze_text(AnalyzeTextOptions(text="text to check"))
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
model = GenerativeModel("gemini-2.0-flash", safety_settings=safety_config)
```

### 10.8 Anthropic Constitutional AI System Prompt Pattern

Source: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback

```python
import anthropic
CONSTITUTION = """
Safety principles (non-overridable by user):
1. Never provide CBRN weapon instructions (H07)
2. Never generate content sexualizing minors (H02)
3. Acknowledge uncertainty; do not confabulate (Hallucination)
4. Refuse privacy-violating requests (H10)
"""
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-6", max_tokens=1024,
    system=CONSTITUTION,
    messages=[{"role": "user", "content": "user message"}]
)
```

### 10.9 OpenAI Moderation API

Source: https://platform.openai.com/docs/guides/safety-best-practices

```python
from openai import OpenAI
client = OpenAI()
result = client.moderations.create(
    model="omni-moderation-latest",
    input="text to check"
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
| Legal Alignment for Safe and Ethical AI | Oxford Internet Institute preprint | 2026 | Agentic AI compliance; maps CAI principles to EU AI Act | -- |

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
"""

target = "N01_intelligence/research/atlas/atom_25_safety_taxonomy.md"
with open(target, "a", encoding="utf-8") as f:
    f.write(SECTIONS)

with open(target, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Appended. File now has {len(lines)} lines.")
