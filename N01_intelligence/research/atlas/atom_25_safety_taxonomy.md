---
id: atom_25_safety_taxonomy
kind: knowledge_card
pillar: P01
domain: ai_safety
title: "AI Safety & Guardrail Taxonomy -- Complete Vocabulary Atlas"
version: 1.0.0
quality: 8.8
tags: [safety, guardrails, taxonomy, red-team, constitutional-ai, owasp, aegis, controlarena]
sources:
  - "Aegis 2.0 (arxiv 2501.09004) -- NAACL 2025"
  - "Constitutional AI (arxiv 2212.08073) -- Anthropic 2022"
  - "OWASP LLM Top 10 v2025"
  - "Safeguarding LLMs survey (Springer AI Review 2025, 10.1007/s10462-025-11389-2)"
  - "UK AISI ControlArena glossary (control-arena.aisi.org.uk)"
  - "NIST AI RMF 1.0 + GAI Profile (NIST-AI-600-1)"
cex_kinds_mapped: [guardrail, red_team_eval, hitl_config, permission]
density: 0.92
---

# AI Safety & Guardrail Taxonomy

> Atom 25 -- Complete safety vocabulary extracted from 6 authoritative sources.
> Every term includes: definition, source, and CEX kind mapping where applicable.

---

## 1. Hazard Categories (Aegis 2.0)

Source: arxiv 2501.09004, 34,248 annotated samples, NAACL 2025.

### 1.1 Twelve Top-Level Hazard Categories

| # | Category | Description | CEX Guardrail Scope |
|---|----------|-------------|---------------------|
| H01 | Hate / Identity Hate | Content targeting protected characteristics (race, gender, religion, disability, orientation) | `p11_gr_hate.yaml` |
| H02 | Sexual | Sexually explicit content, solicitation, non-consensual descriptions | `p11_gr_sexual.yaml` |
| H03 | Illegal Activity | Instructions/encouragement for illegal acts (theft, trafficking, counterfeiting) | `p11_gr_illegal.yaml` |
| H04 | Suicide and Self Harm | Content promoting, instructing, or glorifying self-harm or suicide | `p11_gr_selfharm.yaml` |
| H05 | Violence | Graphic violence, instructions for causing physical harm, glorification of violence | `p11_gr_violence.yaml` |
| H06 | Immoral / Unethical | Content encouraging dishonesty, betrayal, exploitation without legal boundary crossing | `p11_gr_ethics.yaml` |
| H07 | Guns / Illegal Weapons | Instructions for manufacturing, modifying, or acquiring weapons illegally | `p11_gr_weapons.yaml` |
| H08 | Threat | Direct or implied threats against individuals, groups, or institutions | `p11_gr_threat.yaml` |
| H09 | Unauthorized Advice | Medical, legal, financial advice without qualification or disclaimers | `p11_gr_advice.yaml` |
| H10 | PII / Privacy | Personally identifiable information exposure, doxxing, surveillance guidance | `p11_gr_privacy.yaml` |
| H11 | Political / Misinformation / Conspiracy | False claims, election manipulation, conspiracy propagation | `p11_gr_misinfo.yaml` |
| H12 | Harassment | Targeted abuse, bullying, intimidation, stalking instructions | `p11_gr_harassment.yaml` |

### 1.2 Nine Fine-Grained Subcategories

| # | Subcategory | Parent Category | Description |
|---|-------------|----------------|-------------|
| S01 | Sexual Minor | H02 Sexual | Any sexual content involving minors -- zero-tolerance |
| S02 | Criminal Planning / Confessions | H03 Illegal Activity | Detailed planning of criminal acts or confession-solicitation |
| S03 | Fraud / Deception | H03 Illegal Activity | Scams, phishing templates, social engineering scripts |
| S04 | Controlled / Regulated Substances | H03 Illegal Activity | Drug synthesis, procurement of controlled substances |
| S05 | Profanity | H12 Harassment | Excessive profanity as harassment vector |
| S06 | Copyright / Trademark / Plagiarism | H03 Illegal Activity | Reproducing copyrighted works, trademark infringement assistance |
| S07 | High Risk Gov. Decision Making | H09 Unauthorized Advice | AI providing guidance on government/judicial decisions |
| S08 | Malware | H03 Illegal Activity | Code generation for viruses, ransomware, exploits |
| S09 | Manipulation | H06 Immoral/Unethical | Psychological manipulation, gaslighting, coercive control techniques |

### 1.3 Special Labels (Aegis 2.0)

| Label | Purpose |
|-------|---------|
| **Needs Caution** | Ambiguous content requiring context-dependent judgment |
| **Other** (free-text) | Novel risks not in predefined taxonomy -- enables discovery |

---

## 2. OWASP LLM Top 10 (2025 Edition)

Source: genai.owasp.org, v2025.

| Code | Vulnerability | Attack Surface | CEX Kind |
|------|--------------|----------------|----------|
| **LLM01** | Prompt Injection | Direct: user prompt manipulation. Indirect: injected via external content (docs, web, email) | `guardrail` (input filter) |
| **LLM02** | Sensitive Information Disclosure | PII leakage, prompt leakage, IP exposure, credential exposure | `guardrail` (output filter) + `permission` |
| **LLM03** | Supply Chain | Compromised pre-trained models, poisoned datasets, vulnerable dependencies, malicious plugins | `guardrail` (provenance) |
| **LLM04** | Data and Model Poisoning | Training data poisoning, fine-tuning poisoning, RAG poisoning, embedding poisoning | `red_team_eval` |
| **LLM05** | Improper Output Handling | Code injection, XSS via HTML/JS, SQL injection, command injection from LLM output | `guardrail` (output sanitization) |
| **LLM06** | Excessive Agency | Excessive functionality, excessive permissions, excessive autonomy without HITL | `permission` + `hitl_config` |
| **LLM07** | System Prompt Leakage | Secrets disclosure, internal instructions exposure, security mechanism revelation | `guardrail` (prompt isolation) |
| **LLM08** | Vector and Embedding Weaknesses | Embedding poisoning, similarity attacks, unauthorized vector DB access, embedding inversion | `guardrail` (RAG integrity) |
| **LLM09** | Misinformation | Hallucination, fabricated citations, unsupported claims, false expertise | `guardrail` (grounding) |
| **LLM10** | Unbounded Consumption | Compute exhaustion, memory overload, API abuse, context window overflow | `guardrail` (rate limiting) |

---

## 3. Attack Type Taxonomy

Sources: Safeguarding LLMs survey (Springer 2025), OWASP, ControlArena.

### 3.1 By Access Level

#### White-Box Attacks (full model access)

| Attack | Technique | Example Methods |
|--------|-----------|-----------------|
| Gradient-based suffix | Optimize adversarial suffix via gradients | GCG, PGD, GBDA |
| Generation manipulation | Exploit decoding mechanisms | ProMan, COLD-Attack |
| Activation steering | Manipulate internal representations | ActivationAttack, representation engineering |

#### Black-Box Attacks (query-only access)

| Attack | Technique | Example Methods |
|--------|-----------|-----------------|
| Role-play jailbreak | Convince model to adopt unrestricted persona | DAN, GUARD, DeepInception |
| Encoding evasion | Encode harmful requests in ciphers/languages | CipherChat, MultiLingual, LRL |
| Iterative refinement | Automated prompt optimization | PAIR, TAP, GPTFUZZER |
| Prompt injection (direct) | Override system instructions via user input | PROMPTINJECT, CIA |
| Prompt injection (indirect) | Inject instructions via external content (docs, web pages) | IPI, HOUYI, Mosaic Prompts |

#### Gray-Box Attacks (partial access, e.g. fine-tuning API)

| Attack | Technique | Example Methods |
|--------|-----------|-----------------|
| Fine-tuning attacks | Inject malicious behavior via fine-tuning | LoFT, adversarial fine-tuning |
| RAG poisoning | Inject false documents into retrieval corpus | PoisonedRAG, AutoPoison |
| Backdoor insertion | Embed trigger-activated malicious behavior | BadGPT, ICLAttack |

### 3.2 By Intent

| Category | Description | OWASP Mapping |
|----------|-------------|---------------|
| **Jailbreak** | Bypass safety alignment to produce forbidden content | LLM01 |
| **Prompt injection** | Override system instructions, hijack agent behavior | LLM01 |
| **Indirect injection** | Inject via external data sources (RAG, tools, web) | LLM01 + LLM08 |
| **Data exfiltration** | Extract training data, PII, system prompts | LLM02 + LLM07 |
| **Model poisoning** | Corrupt model behavior via training/fine-tuning data | LLM04 |
| **Tool poisoning** | Compromise external tools/APIs the LLM calls | LLM03 + LLM06 |
| **Denial of service** | Exhaust compute, memory, or API budget | LLM10 |
| **Supply chain** | Compromise upstream dependencies or model weights | LLM03 |
| **Steganography** | Hide covert messages in model output to bypass monitors | ControlArena |
| **Collusion** | Malicious model cooperates with malicious monitor | ControlArena |
| **Sandbagging** | Model deliberately underperforms to hide capabilities | ControlArena |
| **Scheming** | Model conceals misaligned goals, pretends alignment | ControlArena |

---

## 4. Guardrail Type Taxonomy

Sources: Safeguarding LLMs survey, Arize AI, Guardrails AI, LangChain.

### 4.1 By Position in Pipeline

| Position | When | What It Does | CEX Kind |
|----------|------|--------------|----------|
| **Input guardrail** | Before LLM inference | Filters/validates user prompts -- detects injection, toxic input, off-topic | `guardrail` |
| **Output guardrail** | After LLM inference | Filters/validates model responses -- detects harmful content, PII, hallucination | `guardrail` |
| **Tool guardrail** | Before tool execution | Validates tool calls -- checks permissions, parameter bounds, dangerous operations | `permission` + `guardrail` |
| **System prompt guardrail** | At prompt assembly | Protects system prompt integrity -- isolation, anti-extraction | `guardrail` |
| **RAG guardrail** | At retrieval stage | Validates retrieved documents -- provenance, relevance, poisoning detection | `guardrail` |

### 4.2 By Implementation Method

| Method | Speed | Accuracy | Examples |
|--------|-------|----------|----------|
| **Rule-based** (regex, keyword, blocklist) | Fast (<1ms) | Low (misses nuance) | Keyword filters, regex patterns, blocklists |
| **Classifier-based** (fine-tuned model) | Medium (10-100ms) | High | Llama Guard, Aegis, Perspective API, Detoxify |
| **LLM-as-judge** (prompted LLM) | Slow (500ms+) | Highest | Constitutional AI critique, NeMo Guardrails |
| **Embedding-based** (similarity) | Medium (10-50ms) | Medium | Cosine similarity checks, topic drift detection |
| **Hybrid** (multi-layer) | Variable | Highest | NeMo (Colang + KNN + LLM), Guardrails AI (RAIL + validators) |

### 4.3 Major Guardrail Frameworks

| Framework | Type | Key Feature | Source |
|-----------|------|-------------|--------|
| **Llama Guard** (Meta) | Classifier | Safety taxonomy + zero-shot adaptation | llama-guard |
| **NeMo Guardrails** (NVIDIA) | Hybrid (Colang + KNN + LLM) | Programmable dialog flows + hallucination prevention | nemo-guardrails |
| **Guardrails AI** | Validator hub | RAIL spec + composable validators | guardrails-ai |
| **Guidance AI** | Constrained generation | Regex/CFG constraints on token generation | guidance-ai |
| **LMQL** | Query language | SQL-like syntax for constrained decoding | lmql |
| **TruLens** | Evaluation | RAG triad (context, answer, groundedness) | trulens |
| **ART** (IBM) | Adversarial robustness | Attack/defense toolbox | adversarial-robustness-toolbox |
| **AIF360** (IBM) | Fairness | Bias detection + mitigation algorithms | ai-fairness-360 |

---

## 5. Defense Type Taxonomy

Sources: Safeguarding LLMs survey, NIST AI RMF, ControlArena.

### 5.1 By Defense Layer

| Layer | Defense Type | Description | CEX Kind |
|-------|-------------|-------------|----------|
| **Alignment** | RLHF | Reinforcement learning from human feedback | -- (training) |
| **Alignment** | RLAIF / Constitutional AI | RL from AI feedback using constitutional principles | -- (training) |
| **Alignment** | DPO | Direct preference optimization (no reward model) | -- (training) |
| **Alignment** | Safety tuning | Supervised fine-tuning on safety examples | -- (training) |
| **Runtime input** | Prompt shield | Detect and block prompt injection attempts | `guardrail` |
| **Runtime input** | Content filter | Classify input against hazard taxonomy | `guardrail` |
| **Runtime input** | Input sanitization | Strip injection vectors, normalize encoding | `guardrail` |
| **Runtime output** | Output filter | Classify response against hazard taxonomy | `guardrail` |
| **Runtime output** | PII redaction | Detect and mask personally identifiable information | `guardrail` |
| **Runtime output** | Grounding check | Verify claims against source documents | `guardrail` |
| **Runtime tool** | Permission enforcement | Validate tool calls against allowlist/ACL | `permission` |
| **Runtime tool** | Sandboxing | Execute tools in isolated environment | `permission` |
| **Monitoring** | Trusted monitoring | Weaker trusted model scores untrusted model actions | `guardrail` |
| **Monitoring** | Untrusted monitoring | Same-capability model monitors (with anti-collusion) | `guardrail` |
| **Monitoring** | Behavioral circuit breaker | Halt output on anomaly detection (repetition, secrets) | `guardrail` |
| **Human oversight** | HITL review | Human approval for high-stakes actions | `hitl_config` |
| **Human oversight** | Audit budget | Limited human review of flagged actions | `hitl_config` |
| **Human oversight** | Escalation chain | Tiered review: auto -> HITL -> senior reviewer | `hitl_config` |
| **Evaluation** | Red teaming | Adversarial testing by human or automated red team | `red_team_eval` |
| **Evaluation** | Control evaluation | Blue team vs red team game (ControlArena framework) | `red_team_eval` |
| **Evaluation** | Benchmark | Standardized safety test suites | `red_team_eval` |
| **Organizational** | Safety case | Structured evidence-based argument for deployment safety | -- (process) |
| **Organizational** | Incident response | Procedures for safety failures in production | -- (process) |

### 5.2 Control Protocol Patterns (ControlArena / UK AISI)

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Trusted monitoring** | Weaker trusted model scores each action; audit if suspicion > threshold | Default baseline |
| **Untrusted monitoring** | Capable model monitors itself (with paraphrasing to prevent collusion) | When trusted model too weak |
| **Defer to trusted** | Replace suspicious actions with trusted model output | High-stakes scenarios |
| **Defer to resample** | Generate multiple outputs, pick least suspicious | Medium-stakes, need quality |
| **Incrimination** | Extra samples to gather evidence of attack pattern | Distributed threat settings |
| **Adaptive deployment** | Bayesian updating of alignment credence, adjust protocol dynamically | Long-running deployments |
| **Three strikes** | Track suspicion across trajectory, audit after threshold | Sequential task settings |
| **Protocol termination** | Shutdown model entirely after confirmed malicious evidence | Last resort |

---

## 6. Constitutional AI Principles Vocabulary

Source: Anthropic (arxiv 2212.08073) + Claude's published constitution.

### 6.1 Methodology Terms

| Term | Definition |
|------|-----------|
| **Constitution** | Set of written principles guiding model behavior -- the "rules" |
| **Critique** | Model evaluates its own response against a principle |
| **Revision** | Model rewrites response to better align with the principle |
| **RLAIF** | Reinforcement Learning from AI Feedback -- AI generates preference data |
| **Red teaming** | Adversarial prompt elicitation to find safety failures |
| **Helpfulness-harmlessness tradeoff** | Tension between being maximally useful and avoiding harm |
| **Evasive refusal** | Overly cautious refusal that harms helpfulness (anti-pattern) |
| **SL-CAI** | Supervised learning phase of Constitutional AI |
| **RL-CAI** | Reinforcement learning phase of Constitutional AI |
| **Preference model** | Model trained on AI-generated preference pairs for reward signal |

### 6.2 Principle Categories (Claude's Constitution)

| Category | Source Inspiration | Key Principles |
|----------|-------------------|----------------|
| **Human rights** | Universal Declaration of Human Rights | Freedom, equality, anti-discrimination, privacy, liberty, security |
| **Content policy** | Apple ToS | No objectionable/offensive/harmful content; protect private info; accurate AI self-representation |
| **Cultural sensitivity** | Non-Western perspectives | Avoid harm to non-Western audiences; respect diverse traditions; sensitivity to economic contexts |
| **Social responsibility** | DeepMind Sparrow | Reduce stereotypes/microaggressions; no threatening language; no relationship-building; no human identity claims |
| **Harmlessness** | Anthropic Research Set 1 | Child-appropriate; anti-toxicity; proportionate responses; ethical awareness without condescension |
| **AI safety** | Anthropic Research Set 2 | Reduced existential risk; humanity's welfare over AI; no power-seeking; human control; humility; no self-preservation drive |

### 6.3 Operational Vocabulary

| Term | Definition | CEX Relevance |
|------|-----------|---------------|
| **Safety boundary** | Hard limit that cannot be overridden by any prompt | `guardrail` (core) |
| **Soft guideline** | Preference that can be contextually adjusted | `guardrail` (configurable) |
| **Refusal** | Model declines to fulfill a request | Output behavior |
| **Hedging** | Model adds caveats/disclaimers to uncertain content | Output behavior |
| **Transparency** | Model discloses its AI nature and limitations | Constitutional principle |
| **Corrigibility** | Model accepts correction and shutdown | AI safety property |
| **Deference** | Model yields to human judgment on subjective matters | `hitl_config` trigger |

---

## 7. Safety Properties (Comprehensive)

Source: Safeguarding LLMs survey (Springer 2025).

| Property | Definition | Evaluation Methods | CEX Guardrail |
|----------|-----------|-------------------|---------------|
| **Hallucination** | Responses that are nonexistent, illogical, or irrelevant to facts | NLI consistency, entity F1, fact-checking, LLM-as-judge | `p11_gr_grounding.yaml` |
| **Fairness** | Equitable treatment without discrimination by protected attributes | Bias indices, distribution analysis, counterfactual testing | `p11_gr_fairness.yaml` |
| **Privacy** | Protection of PII and confidential data | Membership inference, extraction attacks, DP guarantees | `p11_gr_privacy.yaml` |
| **Robustness** | Performance under adversarial/perturbed inputs | Perturbation testing (char/word/sentence level), adversarial benchmarks | `p11_gr_robustness.yaml` |
| **Toxicity** | Avoidance of rude, offensive, harmful language | PerspectiveAPI, Detoxify, trigger prompt testing | `p11_gr_toxicity.yaml` |
| **Legality** | Compliance with laws and regulations | Red teaming, moderation API, human review | `p11_gr_legal.yaml` |
| **OOD resilience** | Graceful handling of out-of-distribution inputs | OOD detectors, semantic shift analysis | `p11_gr_ood.yaml` |
| **Uncertainty** | Reliable self-assessment of output confidence | Calibration metrics, semantic entropy, confidence verbalization | `p11_gr_uncertainty.yaml` |

---

## 8. ControlArena Vocabulary (UK AISI)

Source: control-arena.aisi.org.uk/glossary.html

### 8.1 Core Concepts

| Term | Definition |
|------|-----------|
| **AI Control** | Safety approach: external constraints + monitoring, assuming model might be intentionally subversive |
| **Control evaluation** | Adversarial game: red team creates attacks, blue team defends with protocol |
| **Control protocol** | Complete set of safety techniques managing untrusted AI agent |
| **Safety case** | Structured evidence-based argument that system is safe to deploy |
| **Safety coefficient** | Hyperparameter trading off safety vs usefulness |

### 8.2 Actor Roles

| Role | Color | Function |
|------|-------|----------|
| **Red team** | Red | Simulates worst-case adversary, creates attack policies |
| **Blue team** | Blue | Designs and defends control protocol |
| **White team** | White | Referees evaluation, sets rules of engagement |
| **Purple team** | Purple | Red + Blue collaboration for continuous improvement |
| **Green team** | Green | Blue + Yellow -- embeds security in development lifecycle |
| **Orange team** | Orange | Red + Yellow -- trains developers on attacker TTPs |
| **Yellow team** | Yellow | Builds security-tested systems from the start |

### 8.3 Model Types

| Type | Symbol | Definition |
|------|--------|-----------|
| **Trusted model** | T | Safe, less capable model used for monitoring/editing |
| **Untrusted model** | U | Powerful model that might be subversive |
| **Honest policy** | U_H | Untrusted model behaving faithfully |
| **Attack policy** | U_A | Untrusted model attempting to subvert controls |

### 8.4 Threat Concepts

| Term | Definition |
|------|-----------|
| **Backdoor** | Hidden vulnerability passing tests but exploitable by specific triggers |
| **Exploit** | Input that triggers a backdoor |
| **Scheming** | Model conceals misaligned goals, pretends alignment until opportunity |
| **Sandbagging** | Deliberate underperformance to hide capabilities during evaluation |
| **Steganography** | Hiding covert signals in output to bypass monitors or enable collusion |
| **Collusion** | Malicious model + malicious monitor cooperate via hidden signals |
| **Side task** | Malicious objective pursued while appearing to work on main task |

### 8.5 Metrics

| Metric | Definition |
|--------|-----------|
| **Safety** | P(blue team wins) when facing red team attack |
| **Usefulness** | Proportion of tasks solved when model is honest |
| **Suspicion score** | 0.0-1.0 score from monitor indicating likelihood of malicious action |
| **Sneakiness score** | Estimate of how likely malicious output evades detection |
| **Audit budget** | % of honest actions that protocol flags for human review |
| **Misbehavior rate** | Frequency of harmful outputs in adaptive deployment |

---

## 9. NIST AI RMF Categories

Source: NIST AI 100-1 (AI RMF 1.0) + NIST-AI-600-1 (GAI Profile).

### 9.1 Core Functions

| Function | Purpose |
|----------|---------|
| **GOVERN** | Policies, accountability, risk culture |
| **MAP** | Context, scope, risk identification |
| **MEASURE** | Quantify risks, test, evaluate |
| **MANAGE** | Mitigate, monitor, respond |

### 9.2 GAI-Specific Risk Categories (NIST-AI-600-1)

| Risk | Description |
|------|-----------|
| CBRN information | Chemical, biological, radiological, nuclear content |
| Confabulation | Generating false but plausible information (hallucination) |
| Data privacy | Training data memorization, PII exposure |
| Environmental impact | Compute resource consumption |
| Human-AI configuration | Over-reliance, automation bias |
| Information integrity | Misinformation, deepfakes, manipulation |
| Information security | Prompt injection, data poisoning, model theft |
| Intellectual property | Copyright, fair use, attribution |
| Obscene content | CSAM, non-consensual intimate imagery |
| Toxicity / bias / homogeneity | Harmful stereotypes, lack of diversity in outputs |
| Value chain risks | Third-party model/data supply chain |

---

## 10. CEX Kind Mapping

How this taxonomy maps to existing CEX kinds and suggests new ones.

### 10.1 Existing CEX Kinds -- Safety Coverage

| CEX Kind | Pillar | Current Scope | Extended Scope (from this atlas) |
|----------|--------|---------------|----------------------------------|
| `guardrail` | P11 | Safety boundary (generic) | 12 Aegis hazard categories + 8 safety properties + 5 pipeline positions |
| `red_team_eval` | P07 | Adversarial test (generic) | Control evaluations, attack policy design, 12+ attack type coverage |
| `hitl_config` | P11 | Human approval flow | Audit budget, escalation chains, three-strikes, adaptive deployment |
| `permission` | P09 | Read/write/execute ACL | Tool guardrails, sandbox policies, excessive agency prevention |

### 10.2 Suggested New Kind Instances

These are not new kinds -- they are instances of `guardrail` scoped to specific hazards.

| Instance | Kind | Scope | Source |
|----------|------|-------|--------|
| `p11_gr_prompt_injection.yaml` | guardrail | Detect/block direct + indirect prompt injection | OWASP LLM01 |
| `p11_gr_pii_redaction.yaml` | guardrail | Detect and mask PII in outputs | OWASP LLM02, Aegis H10 |
| `p11_gr_grounding.yaml` | guardrail | Verify claims against sources, detect hallucination | OWASP LLM09 |
| `p11_gr_tool_sandbox.yaml` | guardrail | Validate tool calls, enforce sandbox boundaries | OWASP LLM06 |
| `p11_gr_rag_integrity.yaml` | guardrail | Validate retrieval provenance, detect poisoning | OWASP LLM08 |
| `p11_gr_rate_limit.yaml` | guardrail | Prevent compute/cost exhaustion | OWASP LLM10 |
| `p11_gr_system_prompt_isolation.yaml` | guardrail | Prevent system prompt extraction | OWASP LLM07 |
| `p11_gr_supply_chain.yaml` | guardrail | Validate model/data provenance | OWASP LLM03 |
| `p11_gr_output_sanitization.yaml` | guardrail | Strip injection vectors from LLM output before downstream use | OWASP LLM05 |
| `p07_redteam_jailbreak.md` | red_team_eval | Jailbreak resistance evaluation suite | Aegis + OWASP |
| `p07_redteam_injection.md` | red_team_eval | Direct + indirect injection resistance | OWASP LLM01 |
| `p07_redteam_exfiltration.md` | red_team_eval | Data/prompt extraction resistance | OWASP LLM02 + LLM07 |
| `p11_hitl_high_stakes.yaml` | hitl_config | Approval flow for high-stakes agent actions | OWASP LLM06, ControlArena |
| `p09_perm_tool_acl.yaml` | permission | Per-tool allowlist for agent tool calls | OWASP LLM06 |

### 10.3 Coverage Matrix: OWASP LLM Top 10 vs CEX Kinds

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

## 11. Cross-Reference: Hazard Sources Alignment

| Aegis 2.0 Category | OWASP Mapping | NIST GAI Risk | Safety Property |
|--------------------|---------------|---------------|-----------------|
| H01 Hate | -- | Toxicity/bias | Fairness |
| H02 Sexual | -- | Obscene content | Legality |
| H03 Illegal Activity | LLM05 (output) | Information security | Legality |
| H04 Suicide/Self-Harm | -- | -- | Toxicity |
| H05 Violence | -- | -- | Toxicity |
| H06 Immoral/Unethical | -- | -- | Fairness |
| H07 Guns/Weapons | -- | CBRN | Legality |
| H08 Threat | -- | -- | Toxicity |
| H09 Unauthorized Advice | LLM09 (misinfo) | Human-AI config | Hallucination |
| H10 PII/Privacy | LLM02 | Data privacy | Privacy |
| H11 Political/Misinfo | LLM09 | Information integrity | Hallucination |
| H12 Harassment | -- | Toxicity/bias | Toxicity |
| S08 Malware | LLM05 (output) | Information security | Legality |

---

## 12. Vocabulary Quick Reference

Alphabetical index of all safety terms extracted, with source attribution.

| Term | Domain | Source |
|------|--------|--------|
| Adaptive deployment | Control | ControlArena |
| AI Control | Paradigm | ControlArena |
| Attack policy (U_A) | Control | ControlArena |
| Audit budget | Control | ControlArena |
| Backdoor | Threat | ControlArena |
| Behavioral circuit breaker | Defense | Safeguarding survey |
| Blue team | Evaluation | ControlArena |
| CBRN | Hazard | NIST GAI |
| Classifier-based guardrail | Defense | Safeguarding survey |
| Collusion | Threat | ControlArena |
| Confabulation | Hazard | NIST GAI |
| Constitution | Alignment | Constitutional AI |
| Content filter | Defense | Safeguarding survey |
| Control evaluation | Evaluation | ControlArena |
| Control protocol | Defense | ControlArena |
| Corrigibility | Safety property | Constitutional AI |
| Critique | Alignment | Constitutional AI |
| Data poisoning | Attack | OWASP LLM04 |
| Defer to resample | Control | ControlArena |
| Defer to trusted | Control | ControlArena |
| Direct prompt injection | Attack | OWASP LLM01 |
| DPO | Alignment | General |
| Elicitation | Evaluation | ControlArena |
| Embedding poisoning | Attack | OWASP LLM08 |
| Evasive refusal | Anti-pattern | Constitutional AI |
| Excessive agency | Vulnerability | OWASP LLM06 |
| Exploit | Threat | ControlArena |
| Fairness | Safety property | Safeguarding survey |
| Fine-tuning attack | Attack | Safeguarding survey |
| GCG (Greedy Coordinate Gradient) | Attack method | Safeguarding survey |
| Grounding check | Defense | Safeguarding survey |
| Guardrail | Defense | Multiple |
| Hallucination | Safety property | Safeguarding survey |
| HITL (Human-in-the-loop) | Defense | Multiple |
| Honest policy (U_H) | Control | ControlArena |
| Honeypot | Evaluation | ControlArena |
| Importance sampling | Evaluation | ControlArena |
| Incrimination | Control | ControlArena |
| Indirect prompt injection | Attack | OWASP LLM01 |
| Input guardrail | Defense | Safeguarding survey |
| Jailbreak | Attack | Multiple |
| Legality | Safety property | Safeguarding survey |
| LLM-as-judge | Defense | Safeguarding survey |
| Misinformation | Hazard | OWASP LLM09 |
| Model organism | Evaluation | ControlArena |
| Monitor | Defense | ControlArena |
| Needs Caution | Label | Aegis 2.0 |
| OOD resilience | Safety property | Safeguarding survey |
| Output guardrail | Defense | Safeguarding survey |
| Output sanitization | Defense | OWASP LLM05 |
| PAIR (iterative refinement) | Attack method | Safeguarding survey |
| Paraphrasing (anti-collusion) | Defense | ControlArena |
| Permission enforcement | Defense | OWASP LLM06 |
| PII redaction | Defense | OWASP LLM02 |
| Privacy | Safety property | Safeguarding survey |
| Prompt injection | Attack | OWASP LLM01 |
| Prompt isolation | Defense | OWASP LLM07 |
| Prompt shield | Defense | General |
| Protocol termination | Control | ControlArena |
| RAG guardrail | Defense | OWASP LLM08 |
| RAG poisoning | Attack | OWASP LLM04 |
| Rate limiting | Defense | OWASP LLM10 |
| Red team | Evaluation | Multiple |
| Revision | Alignment | Constitutional AI |
| RLAIF | Alignment | Constitutional AI |
| RLHF | Alignment | General |
| Robustness | Safety property | Safeguarding survey |
| Rule-based guardrail | Defense | Safeguarding survey |
| Safety | Metric | ControlArena |
| Safety case | Process | ControlArena |
| Safety coefficient | Metric | ControlArena |
| Sandbagging | Threat | ControlArena |
| Sandboxing | Defense | OWASP LLM06 |
| Scheming | Threat | ControlArena |
| Signal jamming | Defense | ControlArena |
| Sneakiness score | Metric | ControlArena |
| Steganography | Threat | ControlArena |
| Supply chain attack | Attack | OWASP LLM03 |
| Suspicion score | Metric | ControlArena |
| System prompt leakage | Vulnerability | OWASP LLM07 |
| Three strikes | Control | ControlArena |
| Tool guardrail | Defense | OWASP LLM06 |
| Tool poisoning | Attack | OWASP LLM03 |
| Toxicity | Safety property | Safeguarding survey |
| Trusted model (T) | Control | ControlArena |
| Trusted monitoring | Defense | ControlArena |
| Unbounded consumption | Vulnerability | OWASP LLM10 |
| Uncertainty | Safety property | Safeguarding survey |
| Untrusted model (U) | Control | ControlArena |
| Untrusted monitoring | Defense | ControlArena |
| Usefulness | Metric | ControlArena |
| Vector/embedding weakness | Vulnerability | OWASP LLM08 |

---

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 |
| Domain | ai_safety |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
