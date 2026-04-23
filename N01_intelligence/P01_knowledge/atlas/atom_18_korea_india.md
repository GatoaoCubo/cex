---
id: n01_atom_18_korea_india
kind: knowledge_card
pillar: P01
title: "Atom 18: Korean + Indian LLM Agent Ecosystems"
version: 1.2.0
created: 2026-04-13
updated: 2026-04-13
author: n01_intelligence
domain: research-intelligence
quality: 8.9
tags: [atom, korea, india, sovereign-ai, mcp, voice-first, multilingual, agent, moe, tokenizer, rl-training, benchmark, omni-modal, sovereignty-controversy, peri-ln, vikram]
tldr: "Korea builds MCP platforms + MoE agents (PlayMCP, P-C-G, Solar Pro3, HyperCLOVA X Think, SEED Omni-8B); India builds voice-first multilingual agents (Sarvam 105B/Vikram-30B, Krutrim-2, BharatGen PARAM-2, Indic LLM Arena). Both converge on 128-expert MoE + sovereign compute. 2026 adds omni-modal Naver 8B, Korea sovereignty controversy (Naver Qwen encoder 99.5% cosine), India AI Impact Summit Feb 2026 launches 3 sovereign models."
density_score: 0.96
related:
  - p01_kc_mcp_server
  - bld_memory_mcp_server
  - atom_15_qwen_deepseek
  - atom_16_minimax_kimi_glm
  - bld_memory_agent_card
  - atom_03_openai_agents_sdk
  - bld_collaboration_mcp_server
  - mcp-server-builder
  - p01_kc_terminology_rosetta_stone
  - bld_tools_mcp_server
---

# Atom 18: Korean + Indian LLM Agent Ecosystems

**Scope**: Sovereign LLM programs, agent architectures, MCP platforms, voice-first design, multilingual coverage, RL training pipelines, tokenizer design.
**Period**: 2025-Q2 to 2026-Q2 | **Sources**: 35+ | **Date**: 2026-04-13 (v1.1 enriched)

---

## 1. Korea: The MCP + MoE Agent Wave

### 1.1 Kakao Kanana-2 + PlayMCP

**Kanana-2** (Dec 2025, open-source):

| Spec | Value |
|------|-------|
| Architecture | MoE with MLA (Multi-head Latent Attention) |
| Total params | 32B |
| Active params | ~3B per token (8 active experts) |
| Context | 32,768 tokens native |
| Languages | 6 (Korean, English, Japanese, Chinese, Thai, Vietnamese) |
| Variants | Base, Instruct, Thinking |
| Inference | 2x speed on H100 vs dense equivalent |
| Tool-calling | 3x improvement over Kanana-1.5 in multi-turn tool use |
| License | Open-source |

Kanana-2 uses MoE + MLA to run 32B total params with only 3B active -- extreme efficiency for on-device and cost-sensitive agent deployments.

**PlayMCP** (beta Aug 2025) -- Korea's first MCP platform:

| Feature | Detail |
|---------|--------|
| What | Open MCP marketplace where developers register, share, and test MCP servers |
| Access | Any developer with a Kakao account |
| Analogy | "Just as a USB port connects devices, MCP connects AI models to external systems" |
| Built-in servers | KakaoTalk chat, Talk Calendar, KakaoMap, Gift giving, Melon (music) |
| Toolbox | Users select MCP tools and use them in ChatGPT/Claude with single Kakao auth |
| Ecosystem play | External partners connect to Kakao AI via PlayMCP + AI Agent Builder |
| Target | Full agentic AI ecosystem differentiation by end of 2026 |

**CEX relevance**: PlayMCP is the MCP pattern applied at platform scale -- a marketplace for MCP servers with single-auth bridging to multiple AI clients. This validates the MCP-as-interop thesis. The Toolbox feature (select tools, use across ChatGPT/Claude) is the user-facing MCP aggregator pattern.

#### 1.1b Kanana-2 Architecture Deep Dive

Full internal configuration (from HuggingFace model card):

| Parameter | Value |
|-----------|-------|
| Total layers | 48 |
| Dense layers | 1 (first layer, no expert routing) |
| Vocabulary size | 128,256 tokens |
| Total experts per FFN layer | 128 |
| Selected experts per token | 6 (routed) + 2 (shared, always active) |
| Effective active params | ~3B (8 experts x small FFN each) |
| Native context | 32,768 tokens |
| Extended context | 128K via YaRN (rope_scaling factor 4.0) |
| Attention type | MLA (Multi-head Latent Attention) |
| Reasoning parser compat | deepseek_r1 (vLLM --reasoning-parser flag) |

**Expert routing**: 6 routed + 2 shared per token. Shared experts fire on every token regardless of routing decision -- they carry cross-domain knowledge that all tokens need. The 6 routed experts handle token-specific specialization. This dual design (shared + routed) is adapted from DeepSeek-V2/V3 MoE architecture and reduces routing instability compared to pure top-K selection.

**MLA mechanism**: Compresses key-value cache into low-rank latent vectors, dramatically reducing KV-cache memory at inference. Critical for long-context agent deployments where KV cache is the memory bottleneck.

**Benchmark scores (Kanana-2-30b-a3b-thinking)**:

| Benchmark | Score | Context |
|-----------|-------|---------|
| MMLU-Pro | 75.3% | Multi-domain reasoning |
| GPQA Diamond | 61.3% | Graduate-level science |
| AIME 2024 | 78.3% | Math competition |
| AIME 2025 | 72.7% | Math competition (newer) |
| LiveCodeBench | 60.8% | Live coding eval |
| BFCL-v3 Live Tool Calling | 75.6% | Function-calling accuracy |
| BFCL-v3 Multi-Turn | 34.3% | Multi-turn tool use |

**Tool-calling gap**: BFCL-v3 single-turn (75.6%) vs multi-turn (34.3%) reveals a 41-point drop in multi-turn tool use. This is the key weakness for agentic deployments where conversations span many turns with accumulated tool context.

### 1.2 Naver HyperCLOVA X Think

| Spec | Value |
|------|-------|
| Architecture | Vision-language Transformer with optional thinking mode |
| Params | 32B (SEED variant) |
| Pre-training | ~6T tokens (Korean + English, augmented with synthetic Korean data) |
| Context | 128K tokens (multimodal) |
| Agent eval | 87% on telecom customer-support tool-use benchmark (highest among Korean models) |
| Modalities | Text + vision (omni-modal agent candidate) |
| Release | Technical report June 2025; SEED-Think-32B on HuggingFace Dec 2025 |

Key contribution: controllable reasoning via optional "thinking mode" -- the model can switch between fast inference and deep chain-of-thought on demand. Agent tool-use at 87% on domain-specific Korean benchmark signals production-grade capability for Korean enterprise.

#### 1.2b HyperCLOVA X Think: Post-Training Pipeline

**Technical report**: arXiv:2601.03286 (HyperCLOVA X 32B Think, Jan 2026)

Post-training proceeds in two stages:

| Stage | Goal | Method |
|-------|------|--------|
| Stage 1: Multimodal SFT | Inject vision-language capability | Supervised fine-tuning on vision+text pairs |
| Stage 2: RL alignment | Reasoning + agentic + human alignment | Multiple RL methods (paper details) |

The staged approach mirrors o1/DeepSeek-R1: capability injection via SFT first, then alignment refinement via RL. Not end-to-end -- SFT grounds multimodal understanding before RL begins.

**KCSAT 2026**: Evaluated on Korea's national college entrance exam (Math, 2026 version) -- requires integrating textual instructions with complex diagrams. Result: top 4% of human examinees. More rigorous than MATH-500 because it tests visual+textual co-reasoning on real examination material.

**Artificial Analysis Intelligence Index**: Score 44 -- above EXAONE 4.0 32B (prior Korean leader). Index aggregates across reasoning, coding, and instruction-following.

**Architecture deep dive (Peri-LN + muP)**: HyperCLOVA X 32B Think uses a Peri-LN (Peripheral LayerNorm) Transformer scaled with muP (maximal update parametrization). Peri-LN places layer normalization at both the entry and exit of each sub-layer, improving gradient stability across depth. muP enables zero-shot hyperparameter transfer from small proxy models to the full 32B scale -- learning rates and initialization calibrated on a 100M proxy generalize to 32B without re-tuning. This is the same scaling methodology used by Cerebras/GPT-NeoX research and reduces the compute cost of hyperparameter search at frontier scale.

**Three-stage pre-training curriculum**: Context window expands across stages (short -> medium -> 128K). Stage 1 trains on general corpus at 4K context. Stage 2 adds long-context data at 32K. Stage 3 extends to 128K with rope scaling + synthetic long-doc mixtures. This staged approach prevents the instability seen when training on long-context from scratch.

**Post-training: RL from Verifiable Rewards (RLVR)**: Rather than RLHF from human preferences, HyperCLOVA X Think uses RLVR -- RL training with rewards derived from verifiable answers (math correctness, code execution, factual verification). This is the same paradigm as DeepSeek-R1 and o1: no human preference labels needed, just a ground-truth verifier. More scalable for reasoning tasks where correctness is binary.

**GPT-4.1 comparison on KCSAT STEM**: The vision-augmented variant of HyperCLOVA X Think matches or exceeds GPT-4.1 on KCSAT STEM -- Korea's national college entrance exam science/math problems, which require joint vision+text reasoning on real examination diagrams. Achieving top 4% of human examinees on math + STEM parity with GPT-4.1 with substantially lower training compute is the key headline result.

**Additional size variant**: 14B (HyperCLOVAX-SEED-Think-14B) for cost-sensitive deployments.

**tau-Bench Telecom specifics**: Multi-step simulation of telecom customer service -- booking, troubleshooting, escalation. 87% is currently the highest published score among Korean models on this domain-specific agent benchmark.

#### 1.2c HyperCLOVA X SEED Omni-8B (Dec 2025 -- Any-to-Any Multimodal)

Released Dec 26, 2025 alongside SEED Think-32B. A distinct model -- smaller, omni-modal, not reasoning-focused.

| Spec | Value |
|------|-------|
| Architecture | Decoder-only Transformer with modality-specific encoders + decoders |
| Params | 8B |
| Modalities (input) | Text + vision + audio |
| Modalities (output) | Text + vision (generation/editing) + speech (TTS) |
| Context | 32K tokens |
| Vision encoder | Alibaba Qwen2.5-VL (acknowledged external component) |
| Audio encoder | OpenAI Whisper (acknowledged external component) |
| License | Open-weight |
| Inference system | OmniServe (OpenAI-compatible API, GitHub: NAVER-Cloud-HyperCLOVA-X/OmniServe) |

**Architecture pattern**: Modality-specific encoders project visual/audio inputs into continuous embeddings, interleaved with text tokens in a shared decoder-only backbone. Modality-specific decoders reconstruct images and audio from the shared sequence. Single next-token prediction interface unifies all modalities -- no separate generation heads per modality, just token prediction over an extended vocabulary that includes visual and audio tokens.

**Korean TTS benchmark (MOS, 30 listeners)**:

| Model | MOS (Korean TTS) |
|-------|-----------------|
| HyperCLOVA X 8B Omni | 4.22 / 5 |
| Next-best rival (unnamed) | 3.40 / 5 |
| Gap | +0.82 |

A 0.82 MOS gap is substantial in voice quality evaluation (MOS scale 1-5). This positions Omni-8B as the Korean TTS quality leader among open models.

**Omni-8B vs Think-32B**:

| Dimension | SEED Omni-8B | SEED Think-32B |
|-----------|-------------|---------------|
| Primary use | Omni-modal AI assistant | Reasoning + vision agent |
| Modalities | Text+vision+audio (in+out) | Text+vision (in), Text (out) |
| Params | 8B | 32B |
| Strengths | Voice output, multimodal generation | Deep reasoning, KCSAT, math |
| Context | 32K | 128K |

**Transparency note**: Naver explicitly acknowledges Qwen2.5-VL (Alibaba) as vision encoder and Whisper (OpenAI) as audio encoder. This disclosure becomes significant in light of the Jan 2026 sovereignty controversy (see section 1.7 below).

**CEX relevance**: Any-to-any omni models at 8B scale are the new baseline for voice-enabled agent systems. OmniServe's OpenAI-compatible API is the production deployment pattern for multimodal agents.

### 1.3 Upstage Solar Pro3

| Spec | Value |
|------|-------|
| Architecture | MoE, 102B total, 12B active per token |
| Context | 128K tokens |
| Languages | Korean (primary), English, Japanese |
| Agent perf | 2x agentic benchmark scores vs Solar Pro2 (March 2026 update) |
| Schema compliance | 100% structured output compliance |
| RL technique | SnapPO (proprietary reinforcement learning) |
| Cost | Same price and TPS as Solar Pro2 despite larger model |
| Domains | Finance, healthcare, legal (agent workflows) |

Solar Pro3 is the most explicitly agent-specialized Korean model. The 102B/12B MoE ratio gives frontier-class reasoning at mid-tier compute cost. 100% schema compliance is critical for tool-calling agents that must produce valid JSON.

### 1.4 SK Telecom A.X Ecosystem

| Component | Detail |
|-----------|--------|
| A.X 4.0 | Proprietary LLM (conversational + multimodal), completed early 2025 |
| A.X K1 | 519B hyperscale model; Phase 2 of sovereign AI project (Jan 2026) |
| Roadmap | Upgrade from 519B to 1T+ params with multimodal |
| A. auto | In-car AI controlling infotainment + vehicle hardware via A.X 4.0 |
| Internal agents | 2,000+ AI agents used internally (marketing, legal, PR) |
| Consortium | SK Telecom + Krafton + 42dot + Rebellions for sovereign AI |

SKT's strategy: vertical integration from foundation model (A.X K1) through consumer app (A.) to automotive (A. auto). The 2,000 internal agents demonstrate enterprise-scale agentic deployment.

### 1.5 P-C-G Architecture (Planner-Caller-Generator)

**Paper**: "SLM-Based Agentic AI with P-C-G: Optimized for Korean Tool Use" (Sep 2025, arXiv:2509.19369)

| Component | Role | Key Innovation |
|-----------|------|----------------|
| **Planner** | Produces initial batch plan with limited on-demand replanning | Batch planning reduces round-trips |
| **Caller** | Returns normalized call object after joint schema-value validation | Catches invalid calls BEFORE execution |
| **Generator** | Integrates tool outputs into final answer | Clean separation of reasoning from synthesis |

**Korean-first value policy**: Addresses the code-switching problem where Korean queries + English API schemas cause execution failures. The policy keeps values in Korean by default, translating only at the API boundary. This reduces failures caused by Korean-to-English switching in parameter values.

**Evaluation coverage**: Single-chain, multi-chain, missing-parameters, missing-functions scenarios. LLM-as-a-Judge protocol averaged over 5 runs.

**Key finding**: Role-specialized SLMs (small language models) are a cost-effective alternative for Korean tool-use agents. Competitive accuracy with reduced token consumption and acceptable latency.

**CEX relevance**: P-C-G mirrors the CEX 8F pipeline's separation of concerns -- F4 REASON (Planner), F5 CALL (Caller), F6 PRODUCE (Generator). The Korean-first value policy is relevant for any non-English agent system.

### 1.6 Korean Sovereign AI Consortium (240B Won Program)

| Consortium Lead | Partners | Focus |
|----------------|----------|-------|
| Naver Cloud | (ecosystem) | General-purpose sovereign LLM |
| SK Telecom | Krafton, 42dot, Rebellions | General + industry-specific agents |
| Upstage | Nota, Lablup, Flitto | Solar WBL -- match global frontrunners |
| LG AI Research | LG Uplus, LG CNS, FuriosaAI | Enterprise AI stack |
| NC AI | Universities, Lotte Innovate | 200B-parameter foundation model |

**Timeline**: Phase 2 testing through June 2026; final evaluation December 2026.
**Budget**: 240 billion won (~$175M USD) from Ministry of Science and ICT.
**Goal**: Sovereign LLMs on domestic infrastructure, reducing dependence on US providers.

### 1.7 Korea Sovereignty Controversy (Jan 2026): What Counts as "Independent" AI?

The 240B won program hit turbulence in January 2026 when plagiarism allegations emerged against two of the five selected consortia.

**The Naver Case**:

| Dimension | Detail |
|-----------|--------|
| Allegation | HyperCLOVA X SEED 32B Think vision encoder = Alibaba Qwen2.4 encoder |
| Evidence | Cosine similarity: 99.5%; Pearson correlation: 98.9% between encoder weight values |
| Naver response | Acknowledged; called it "strategic adoption of a verified external encoder" for ecosystem compatibility |
| Government position | Unclear -- no formal definition of what "developed from scratch" requires |

**The Upstage Case**:

| Dimension | Detail |
|-----------|--------|
| Allegation | Solar Open 100B copied Zhipu AI GLM-4.5-Air (Chinese model) |
| Upstage response | Public verification session Jan 2, 2026, Gangnam: showed training logs, checkpoints, experimental data |
| CEO statement | "Foundation model trained from scratch, built on original data" |
| Outcome | Case closed quickly; hard questions remained open |

**Broader implication -- the definition problem**:

The controversy exposed the absence of a formal definition for "sovereign AI" in Korean policy. The government has not answered: Is component reuse (encoders, tokenizers) acceptable? What percentage of weights must be original? Does fine-tuning a foreign base count? This is not unique to Korea -- the EU AI Act and India's IndiaAI Mission face the same definitional gap. Any sovereign AI program that funds model development without defining "development from scratch" will face these disputes.

**CEX relevance**: For N01 intelligence tracking, this is the canonical case study on sovereignty definitions. When benchmarking a model as "sovereign," verify: (1) base model origin, (2) encoder origin, (3) tokenizer origin, (4) training data origin. A model with 4/4 domestic is fully sovereign; 3/4 is hybrid. The Naver case = 2/4 (Korean base + Korean data + foreign vision encoder + foreign audio encoder in Omni-8B).

---

## 2. India: Voice-First + 22-Language Coverage

### 2.1 Sarvam AI (105B, 22 Languages)

| Spec | Value |
|------|-------|
| Architecture | MoE Transformer, MLA compression, 128 sparse experts |
| Total params | 105B |
| Active params | ~10.3B per token |
| Training data | 12T tokens (code, web, math, multilingual) |
| Languages | 22 scheduled Indian languages + English (23 total), 12 scripts |
| Context | Long-context via rotary positional embeddings + optimized KV-cache |
| MMLU | 90.6 |
| Math500 | 98.6 |
| AIME 25 | 96.7% (with tools) |
| License | Apache 2.0 |
| Compute | IndiaAI Mission domestic infrastructure |

**Tokenizer design**: Custom tokenizer optimized for all 22 Indian languages across 12 scripts. Significantly outperforms competing tokenizers on fertility scores (tokens per word) for low-resource languages like Odia, Santali, Manipuri. This is the foundational innovation -- efficient tokenization makes multilingual inference affordable.

**Tokenizer fertility benchmark** (tokens per word; lower = better):

| Tokenizer | Average | Low-resource (Odia/Santali/Manipuri) |
|-----------|---------|--------------------------------------|
| GPT-4 / Llama-3 (global models) | 4-8 | 6-12 (degraded) |
| Sarvam custom tokenizer | 1.4-2.1 | 1.6-2.3 (maintains parity) |
| Improvement | ~3-5x | ~3-5x |

A 4x fertility reduction means 4x fewer tokens per inference call on Indian-language queries -- direct cost reduction that makes commercial viability feasible without US-scale compute budgets.

**Training pipeline** (three-stage, all in-house):

| Stage | Key Technical Detail |
|-------|---------------------|
| Pre-training (12T tokens) | Sigmoid-based expert routing (not softmax). Improves expert load balancing; reduces routing collapse during training. |
| SFT | Curated open + synthetic prompts. Safety fine-tuning uses India-specific risk taxonomy + internal model spec inspired by frontier model constitutions. |
| RL (GRPO) | Asynchronous GRPO. Adaptive sampling: dynamically allocates rollouts based on information-gain metric from current pass rate per prompt. |

**Sigmoid vs softmax routing**: Standard MoE uses softmax gating, where probability mass is normalized across all experts. Sigmoid gating treats each expert independently (binary-like decision), preventing the "rich get richer" collapse where a few experts receive most routing decisions. This is the same technique DeepSeek-V2 uses to maintain expert utilization diversity.

**Architecture contrast (30B vs 105B)**:

| Spec | Sarvam 30B | Sarvam 105B |
|------|-----------|------------|
| Attention | GQA (Grouped Query Attention) | MLA (Multi-head Latent Attention) |
| Training tokens | 16T | 12T |
| Experts | 128 | 128 |
| Active params | 2.4B | 10.3B |

The 30B uses GQA (standard KV-cache reduction), while 105B uses MLA (deeper compression). This reflects the same attention evolution seen in DeepSeek-V2 to V3: MLA is preferable at larger scale where KV memory becomes the bottleneck.

**Additional benchmark scores**:

| Benchmark | 105B | 30B |
|-----------|------|-----|
| GPQA Diamond | 78.7 | -- |
| Indian language (avg) | 90% | -- |
| Math500 | 98.6 | 97.0 |
| HumanEval | -- | 92.1 |
| LiveCodeBench v6 | -- | 70.0 |

**Inference optimization**: 3-6x throughput on H100; 1.5-3x on L40S. Apple Silicon MXFP4 delivers 20-40% higher throughput. 105B uses vocabulary parallelism + disaggregated serving for long-context efficiency.

**30B companion model**: 30B total / 2.4B active params, GQA, 128 experts. Trained on 16T tokens. HumanEval: 92.1, LiveCodeBench v6: 70.0.

### 2.2 Krutrim (Ola) -- Voice-First Agentic AI

| Spec | Value |
|------|-------|
| Product | Kruti (consumer AI assistant) |
| Launch | June 12, 2025 |
| Modalities | Text + voice (voice-first by design) |
| Languages | 13 at launch; roadmap to 24 by 2026 |
| Backend | Open-source LLMs + proprietary Krutrim V2 |
| Capabilities | Book cabs, pay bills, generate images, multi-step task execution |
| Downloads | ~100K on Google Play (as of search date) |

**Voice-first thesis**: "India is a voice-first world. We are building voice-first models." This is not a feature -- it is the core architecture decision. India's semi-urban and rural population cannot type in English; voice input in native language is the only viable interface.

**Agentic capabilities**: Kruti reasons, plans, and executes multi-step tasks. Unlike chatbots that answer questions, Kruti performs actions (booking, payment, scheduling). This is the agentic pattern applied to consumer mobile.

**Scaling challenge**: 100K downloads is modest. The 13-to-24 language expansion and Ola's existing ride-hailing distribution (massive install base) are the growth levers.

#### 2.2b Krutrim-2: Foundation Model (12B, 22 Languages)

While Kruti is the consumer product, Krutrim-2 is the foundation model powering it -- released separately as open-weight.

| Spec | Value |
|------|-------|
| Architecture | Dense Transformer (Mistral-NeMo base) |
| Params | 12B |
| Context | 128K tokens |
| Languages | English + 22 Indian languages |
| Training period | Dec 2024 - Jan 2025 |
| Training data | Curated English, Indic, code, math, books, synthetic mix |
| Alignment | SFT (cross-task instruction following) + DPO (human preference alignment) |
| Claim | Best-in-class on Indic tasks; surpasses models 5-10x its size |
| License | Available on HuggingFace |

**Multi-stage training**: Context size and batch size varied at each stage for stable training. The multi-stage approach (not a single continuous run) allows curriculum-style data mixing -- earlier stages focus on language breadth, later stages on reasoning depth.

**Dense vs MoE**: Unlike Sarvam (MoE), Krutrim-2 uses a dense architecture (Mistral-NeMo). Trade-off: simpler deployment, no expert routing overhead, but higher per-token compute than equivalent MoE. At 12B dense, comparable to Sarvam 30B active (2.4B) in inference cost? No -- 12B dense is ~5x more compute per token than 2.4B active. Krutrim prioritizes simplicity and hardware compatibility over efficiency.

### 2.3 AI4Bharat Indic LLM Arena

**The Language-Context-Safety Evaluation Triad**:

| Dimension | What It Measures | India-Specific Examples |
|-----------|-----------------|----------------------|
| **Language** | Code-mixing fluency (Hinglish, Tanglish), script handling, multilingual coherence | "Book a cab to Koramangala, wahan se Indiranagar jaana hai" (Hindi-English mix) |
| **Context** | Cultural and regional appropriateness, local knowledge | Gift suggestions for housewarming reflect Indian practices, not Western norms; agriculture/finance/healthcare region-specific queries |
| **Safety** | India-specific harms: regional bias, communal misinformation, caste-based stereotypes | Detecting caste stereotypes, communal tension amplification, regional discrimination |

**Battle protocol** (step-by-step):

1. User inputs a prompt in any Indian language or code-mixed variety
2. System routes to two anonymous models simultaneously (Model A, Model B)
3. User sees both responses -- model identities hidden
4. User votes: A wins / B wins / Tie
5. Bradley-Terry algorithm processes accumulated votes into statistically robust rankings
6. After thousands of battles: leaderboard with confidence intervals

**Why Bradley-Terry**: Simple win-rate rankings are biased by uneven matchup distributions (some models get easier opponents). Bradley-Terry fits a probabilistic model to the full pairwise comparison matrix, producing rankings that account for the strength of opponents. The same statistical framework used by chess rating systems (Elo is a special case).

**Anonymization enforces fairness**: Model identity hidden during voting eliminates brand bias -- judges cannot favor GPT-4 because they "know" it is GPT-4. This is critical given the prestige gap between global API providers and Indian models.

**Phases**:

| Phase | Scope | Status |
|-------|-------|--------|
| Phase 1 | Text across multiple Indian languages + code-mixed | Live (since Nov 2025) |
| Phase 2 | Vision + audio (omni-modal evaluation) | Planned |
| Phase 3 | Agentic tasks: PDFs, web search, tool-calls | Planned |

**Infrastructure**: Supported by Google Cloud. IIT Madras (AI4Bharat lab) operates it as a national public resource.

**CEX relevance**: The Language-Context-Safety triad is a transferable evaluation framework. Any non-English agent system needs equivalent dimensions. Code-mixing evaluation is particularly important -- real users do not speak "pure" languages. The Bradley-Terry methodology is directly applicable to CEX's peer-review scoring layer for non-English artifacts.

### 2.4 India 2026: New Sovereign Model Releases

#### 2.4.0 India AI Impact Summit 2026 (Feb 16-21, New Delhi)

Three sovereign AI models unveiled simultaneously at the India AI Impact Summit 2026, held February 16-21, New Delhi. Organized under the IndiaAI Mission (budget: INR 10,372 crore / $1.1B). Models: Sarvam (two models), BharatGen Param2, Gnani.ai Vachana.

The summit marks the first coordinated sovereign AI release event outside the US/EU/China axis -- three models from one country in one week, all trained on domestic infrastructure. Comparable in strategic intent to China's coordinated DeepSeek/Qwen/Baidu releases, but with a different thesis: public infrastructure + voice-first vs commercial API dominance.

**Sarvam "Vikram" (demo name)**: Sarvam's 30B model was showcased at the summit under the demonstration name "Vikram," honoring Vikram Sarabhai (eminent Indian physicist and astronomer who founded ISRO). Official release followed on March 6, 2026 under Apache 2.0 as Sarvam-30B. The naming is a deliberate cultural signal -- connecting India's AI sovereignty narrative to its space program legacy.

| Model family | Demo/product name | Params | Official release |
|-------------|------------------|--------|-----------------|
| Sarvam 30B | Vikram (demo) | 30B (2.4B active) | March 6, 2026 -- Apache 2.0 |
| Sarvam 105B | (no separate demo name) | 105B (10.3B active) | March 6, 2026 -- Apache 2.0 |
| BharatGen PARAM-2 | PARAM-2 | 17B | Feb 2026 -- public digital good |
| Gnani.ai Vachana | Inya VoiceOS | Speech models | Feb 2026 -- enterprise |

**BharatGen PARAM-2** (Feb 2026, India AI Impact Summit, New Delhi):

| Spec | Value |
|------|-------|
| Architecture | MoE |
| Params | 17B |
| Languages | 22 scheduled Indian languages |
| Training data | Bharat Data Sagar initiative (India-centric curated dataset) |
| License | National public digital good (not proprietary) |
| Operator | BharatGen (government-backed) |
| Deployment | Governance, healthcare, education, finance, citizen services |
| Live demo | MahaGPT -- built with MITRA + Maharashtra government for urban development workflows |

PARAM-2 is differentiated from Sarvam/Krutrim by its public infrastructure model: distributed as a national digital good, not a commercial API. Any state government, hospital, or school can integrate it without proprietary lock-in. This is the "public AI infrastructure" thesis -- AI as a utility, not a product.

**Tech Mahindra Project Indus** (2026):

| Spec | Value |
|------|-------|
| Params | 8B |
| Language focus | Hindi-first |
| Domain | Education (digital classrooms, adaptive tutoring) |
| Architecture | Not disclosed |

Vertical specialization: 8B is far smaller than Sarvam/PARAM-2, but domain focus (education Hindi) may outperform general models on that vertical. Confirms the India market is bifurcating: general-purpose sovereign LLMs (Sarvam, PARAM-2) + domain-specialized fine-tunes (Project Indus, MahaGPT).

**Gnani.ai Vachana** (2026):

| Product | Type | Detail |
|---------|------|--------|
| Vachana STT | Speech-to-text | Optimized for Indic languages |
| Vachana TTS | Text-to-speech | Optimized for Indic languages |
| Infrastructure | India-only data centres | Sovereign compute requirement |

Voice layer specialist. While Sarvam/Krutrim target full-stack LLMs, Gnani focuses on the voice modality exclusively -- the entry point for rural/semi-urban users who cannot type. STT + TTS as building blocks for any voice-first agent.

**India 2026 Model Landscape Summary**:

| Model | Params | Architecture | Specialty | Open? |
|-------|--------|-------------|-----------|-------|
| Sarvam 105B | 105B (10.3B active) | MoE + MLA | Full-stack, 22 languages | Apache 2.0 |
| Sarvam 30B | 30B (2.4B active) | MoE + GQA | Full-stack, 22 languages | Apache 2.0 |
| BharatGen PARAM-2 | 17B | MoE | Sovereign governance | Public digital good |
| Krutrim-2 | 12B | Dense (Mistral-NeMo) | Consumer + 22 languages | HuggingFace |
| Tech Mahindra Project Indus | 8B | Not disclosed | Hindi education | Enterprise |
| Gnani.ai Vachana | -- | Speech models | STT/TTS for Indic | Enterprise |

**Gnani.ai Vachana -- Inya VoiceOS (2026 addition)**: Revealed at the summit: Vachana TTS can clone a human voice in 12 Indian languages using fewer than 10 seconds of audio. This is the voice cloning specification: 10-second sample -> multilingual voice clone across 12 Indic languages. Deployed inside India-only data centres for sovereignty compliance. The voice cloning capability positions Gnani for government and broadcast use cases where localized voice IDs are legally required.

---

## 3. Comparative Analysis

### 3.1 Korea vs India: Strategic Posture

| Dimension | Korea | India |
|-----------|-------|-------|
| **Primary driver** | Platform ecosystems (Kakao, Naver, SKT) | Sovereignty + inclusion (government + startups) |
| **Agent architecture** | MCP platforms + tool-calling MoE | Voice-first + multilingual coverage |
| **Gov funding** | 240B won ($175M) for 5 consortia | INR 10,372 crore ($1.1B) IndiaAI Mission |
| **Language challenge** | 1 primary (Korean) + 5 secondary | 22 constitutional languages + 12 scripts |
| **MoE adoption** | Universal (Kanana-2: 32B/3B, Solar: 102B/12B) | Universal (Sarvam: 105B/10.3B, 30B/2.4B) |
| **Open-source** | Strong (Kanana-2, HyperCLOVA SEED, Solar) | Strong (Sarvam Apache 2.0) |
| **Consumer product** | KakaoTalk + Naver integration | Kruti (Ola) voice assistant |
| **Enterprise** | SKT 2,000 internal agents | Sarvam API + enterprise |
| **Evaluation** | Domain-specific benchmarks (telecom, finance) | Indic LLM Arena (Language-Context-Safety) |
| **Omni-modal** | HyperCLOVA X 8B Omni (text+vision+audio in+out, Dec 2025) | Gnani.ai Vachana TTS (12-language voice cloning, <10s sample) |
| **Sovereignty dispute** | YES: Naver Qwen encoder 99.5% cosine similarity (Jan 2026) | NO equivalent controversy; models more explicitly built from scratch |
| **MCP ecosystem** | PlayMCP live (10K+ public MCP servers globally, AAIF governance) | No equivalent MCP platform; tool calling via Sarvam API |

### 3.2 MoE as Universal Strategy

Both ecosystems converge on MoE as the cost-performance architecture for sovereign agents. Expanded with 2026 releases:

| Model | Total | Active | Ratio | Attention | Expert count |
|-------|-------|--------|-------|-----------|-------------|
| Kakao Kanana-2 | 32B | 3B | 10.7:1 | MLA | 128 (6 routed + 2 shared) |
| Upstage Solar Pro3 | 102B | 12B | 8.5:1 | -- | -- |
| Sarvam 105B | 105B | 10.3B | 10.2:1 | MLA | 128 (sigmoid routing) |
| Sarvam 30B | 30B | 2.4B | 12.5:1 | GQA | 128 (sigmoid routing) |
| BharatGen PARAM-2 | 17B | -- | -- | -- | MoE (unspecified) |
| Krutrim-2 | 12B | 12B (dense) | 1:1 | -- | None (dense) |

**Convergence pattern**: MoE with 128 experts appears in Kanana-2, Sarvam 30B, and Sarvam 105B independently. This is not coincidence -- 128 experts is the DeepSeek-V2/V3 sweet spot where expert specialization is high enough to matter but routing overhead is manageable.

**MLA as long-context standard**: Both Kanana-2 and Sarvam 105B (the flagship models) use MLA. DeepSeek-V2 introduced MLA in 2024; by 2026 it is adopted by Korea and India's top models. Confirms MLA is becoming the attention mechanism of choice for sovereign frontier models.

MoE ratios of 8-12:1 (for routed-only count) are the sweet spot -- frontier reasoning at mid-tier inference cost. This is particularly important for sovereign deployments where domestic compute is constrained.

### 3.3 Key Patterns for CEX

| Pattern | Source | CEX Mapping |
|---------|--------|-------------|
| MCP marketplace | PlayMCP (Kakao) | P04_tools: MCP server registry with auth bridging |
| Role-separated agents | P-C-G (Korean research) | 8F pipeline: F4=Planner, F5=Caller, F6=Generator |
| Korean-first value policy | P-C-G paper | Non-English agent value handling in cex_router.py |
| Voice-first input | Krutrim/Kruti, Gnani.ai | P05_output: voice modality for agent interaction |
| 22-language tokenizer | Sarvam AI | P01_knowledge: multilingual tokenizer efficiency |
| Language-Context-Safety eval | Indic LLM Arena | P07_evaluation: culture-aware scoring rubric |
| Bradley-Terry ranking | Indic LLM Arena | P07_evaluation: pairwise comparison for peer scoring |
| Code-mix fluency | AI4Bharat | P03_prompt: Hinglish/Tanglish prompt handling |
| Sigmoid expert routing | Sarvam (pre-training) | P09_config: expert routing for MoE inference configs |
| Shared + routed experts | Kanana-2 (DeepSeek-style) | P02_model: dual expert design in agent model configs |
| Asynchronous GRPO + adaptive sampling | Sarvam RL | P07_evaluation: RL training signal for reward_signal artifacts |
| Sovereign compute | Both ecosystems | P09_config: domestic infra routing preference |
| Public AI infrastructure | BharatGen PARAM-2 | P12_orchestration: multi-tenant model dispatch for public services |

---

## 4. Signals and Implications

### 4.1 For Agent Builders

1. **MCP is going mainstream in Asia**. PlayMCP proves the pattern scales to platform ecosystems. Expect similar MCP marketplaces from Naver, LINE, WeChat.

2. **P-C-G validates modular agent architecture**. The Planner-Caller-Generator separation with role-specialized SLMs is more token-efficient than monolithic agent approaches. This aligns with CEX's multi-nucleus design.

3. **Voice-first is not optional for non-English markets**. Krutrim's architecture decision reflects a billion-user reality: typing in English is a barrier. Agent systems targeting global markets need voice input as a primary modality.

4. **22-language tokenizer efficiency is a moat**. Sarvam's custom tokenizer reduces cost per token for underserved languages by 3-5x (fertility: 1.4-2.1 vs 4-8 for global models). This makes multilingual agents economically viable at scale.

5. **Code-mixing is the real evaluation frontier**. Pure language benchmarks miss how people actually talk. Hinglish, Tanglish, and similar code-mixed varieties are the true test of multilingual models.

6. **Multi-turn tool use is the weak link in Korean models**. Kanana-2's BFCL gap (75.6% single-turn vs 34.3% multi-turn) reveals that current Korean models excel at single-shot tool calls but degrade significantly over conversation turns. This is the key capability gap for production agentic deployments.

7. **Sigmoid routing prevents expert collapse**. Sarvam's use of sigmoid (not softmax) for MoE gating is an implementation detail with large training stability implications. When building or configuring MoE models, sigmoid routing should be the default for sovereign models trained on limited compute.

8. **India is bifurcating into general sovereign + domain specialists**. Sarvam/PARAM-2 cover general-purpose, while Project Indus (education Hindi), MahaGPT (governance), and Gnani.ai (voice) target verticals. The ecosystem is maturing past "one model to rule them all."

9. **Public AI infrastructure is a viable distribution model**. PARAM-2's national digital good model avoids proprietary lock-in for government and public services. This contrasts with the commercial API model and has implications for regulated industries (healthcare, education, legal).

10. **Omni-modal at 8B is the new voice-agent baseline**. HyperCLOVA X 8B Omni delivers text+vision+audio in+out at 8B scale with Korean TTS MOS 4.22/5. Any-to-any capability in a deployable open-weight model sets the floor for voice agent systems in 2026. Systems that separate STT+LLM+TTS into three models are already architecturally behind.

11. **Sovereignty requires a multi-layer definition**. The Korea controversy reveals that "sovereign AI" must specify: base architecture origin, pre-training data origin, encoder/tokenizer origin, and fine-tuning compute origin. Models scoring 2/4 on these dimensions (e.g., Korean base + Korean data, but foreign vision encoder + foreign audio encoder) should be classified as hybrid-sovereign, not fully sovereign. This is the right framework for N01 competitive intelligence on any national AI program.

12. **RLVR (RL from Verifiable Rewards) is replacing RLHF for reasoning models**. HyperCLOVA X Think, DeepSeek-R1, and o1 all use verifiable reward signals (math, code, factual correctness) instead of human preference labels. This is both cheaper (no labeling cost) and more scalable (programmatic verification). Expect the RLHF market to contract as RLVR-trained models dominate reasoning benchmarks.

13. **MCP ecosystem has reached protocol governance maturity**. MCP donated to Linux Foundation's Agentic AI Foundation (AAIF) in December 2025. Co-founded by Anthropic, Block, and OpenAI. Over 10,000 public MCP servers as of April 2026. PlayMCP in Korea operates within this now-governance-mature ecosystem. The AAIF governance model (Linux Foundation) mirrors successful OS foundations (CNCF, ASF) -- MCP is on a trajectory to become critical infrastructure, not a product.

### 4.2 Confidence Assessment

| Claim | Confidence | Evidence |
|-------|-----------|----------|
| Korea leads Asia in MCP adoption | HIGH | PlayMCP live, Kakao ecosystem integration |
| P-C-G is production-viable for Korean agents | MEDIUM | Paper only, no production deployment reported |
| Sarvam 105B is competitive with global models | HIGH | MMLU 90.6, Math500 98.6, GPQA 78.7, Apache 2.0 release |
| Krutrim-2 surpasses models 5-10x its size on Indic tasks | MEDIUM | Claimed by Ola, not independently benchmarked vs Sarvam |
| Krutrim/Kruti will scale to 100M+ users | LOW | 100K downloads, 13 languages, unproven distribution |
| Both governments will sustain funding | HIGH | $175M (Korea) + $1.1B (India) already committed |
| MoE 128-expert design is the sovereign architecture standard | HIGH | 3/3 top sovereign models independently choose 128 experts |
| MLA superseding GQA for flagship models | HIGH | Kanana-2 + Sarvam 105B both use MLA; GQA relegated to smaller variants |
| Bradley-Terry is the right ranking framework for human evals | HIGH | AI4Bharat + Chatbot Arena + LMSYS all use it; chess ratings proven |
| Krutrim-2 dense is a cost disadvantage vs MoE at same compute | HIGH | 12B dense = ~5x compute vs 2.4B active Sarvam 30B per token |
| HyperCLOVA X 8B Omni is the open-weight Korean TTS leader | HIGH | MOS 4.22 vs 3.40 next-best; 0.82 gap is statistically large on 5-point scale |
| Naver's vision encoder = Qwen encoder (>99% similarity) | HIGH | Cosine 99.5% + Pearson 98.9% from independent analysis; Naver acknowledged |
| Korean national AI program will complete without disqualifying either consortium | MEDIUM | Government has not defined "developed from scratch"; political pressure to succeed |
| RLVR will replace RLHF as standard reasoning alignment | HIGH | HyperCLOVA Think + DeepSeek-R1 + o1 all use RLVR; human labeling cost is the bottleneck |
| Sarvam Vikram-30B official release (Apache 2.0) happened March 6, 2026 | HIGH | Multiple independent sources confirm date and license |

---

## Sources

- [Kakao PlayMCP Beta Launch](https://www.businesskorea.co.kr/news/articleView.html?idxno=249395)
- [Kakao PlayMCP Toolbox](https://www.kakaocorp.com/page/detail/11865?lang=ENG)
- [Kakao Kanana-2 Open Source](https://www.koreatimes.co.kr/business/tech-science/20251219/kakao-open-sources-kanana-2-model-optimized-for-agentic-ai)
- [Kanana-2 Thinking on HuggingFace](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-thinking)
- [HyperCLOVA X Think Technical Report](https://arxiv.org/abs/2506.22403)
- [HyperCLOVA X SEED Think 32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B)
- [Naver HyperCLOVA X Think Press Release](https://www.navercorp.com/en/media/pressReleasesDetail?seq=33066)
- [Upstage Solar Pro3 Announcement](https://en.sedaily.com/news/2026/03/24/upstage-unveils-agent-specialized-llm-solar-pro3)
- [Solar Pro3 Agentic Performance](https://www.upstage.ai/blog/en/solar-pro-3-0323)
- [SK Telecom A.X K1 at MWC 2026](https://telecomlead.com/telecom-services/sk-telecom-showcases-full-stack-ai-strategy-at-mwc-2026-with-a-x-k1-model-and-ai-infrastructure-innovations-124676) <!-- allowlist-secret -->
- [SK Telecom A.X K1 519B Announcement](https://www.prnewswire.com/news-releases/sk-telecom-unveils-ax-k1-koreas-first-500b-scale-hyperscale-ai-model-302649835.html) <!-- allowlist-secret -->
- [P-C-G Architecture Paper](https://arxiv.org/abs/2509.19369)
- [Korean Sovereign AI 5 Consortia](https://www.koreatimes.co.kr/business/tech-science/20250804/5-consortia-selected-to-carry-out-koreas-national-ai-foundation-model-project)
- [Korea Sovereign AI Initiative](https://thediplomat.com/2025/07/south-koreas-sovereign-ai-gambit-a-high-stakes-experiment-in-autonomy/)
- [Sarvam 30B and 105B Blog](https://www.sarvam.ai/blogs/sarvam-30b-105b)
- [Sarvam 105B on HuggingFace](https://huggingface.co/sarvamai/sarvam-105b)
- [Sarvam AI Wikipedia](https://en.wikipedia.org/wiki/Sarvam_AI)
- [Krutrim Kruti Launch](https://www.outlookbusiness.com/news/olas-krutrim-launches-agentic-ai-assistant-kruti)
- [Kruti Agentic AI Analysis](https://aufaittechnologies.com/blog/kruti-agentic-ai-india-launch/)
- [AI4Bharat Indic LLM Arena Blog](https://ai4bharat.iitm.ac.in/blog/indic-llm-arena)
- [Indic LLM Arena Platform](https://arena.ai4bharat.org/)
- [Indic LLM Arena Analytics Vidhya Review](https://www.analyticsvidhya.com/blog/2025/11/indic-llm-arena/)
- [South Korea LLM Powerhouses Overview](https://www.marktechpost.com/2025/08/21/meet-south-koreas-llm-powerhouses-hyperclova-ax-solar-pro-and-more/)
- [HyperCLOVA X 32B Think Technical Report (arXiv)](https://arxiv.org/abs/2601.03286)
- [HyperCLOVA X SEED Think 32B HuggingFace](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B)
- [HyperCLOVA X SEED Think 14B HuggingFace](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B)
- [Kanana-2-30b-a3b-thinking HuggingFace](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-thinking)
- [Kanana-2-30b-a3b-instruct HuggingFace](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct)
- [Sarvam 30B and 105B Technical Blog](https://www.sarvam.ai/blogs/sarvam-30b-105b)
- [Sarvam 105B Open Source (buildfastwithai)](https://www.buildfastwithai.com/blogs/sarvam-105b-india-s-open-source-llm-for-22-indian-languages-2026)
- [Krutrim-2: Best-in-Class Indic LLM](https://tech.olakrutrim.com/krutrim-2-a-best-in-class-large-language-model-for-indic-languages/)
- [Krutrim-2 HuggingFace](https://huggingface.co/krutrim-ai-labs/Krutrim-2-instruct)
- [BharatGen PARAM-2 Launch (BharatGen blog)](https://bharatgen.com/param-2-launch-bharatgen-sovereign-ai-22-languages/)
- [BharatGen PARAM-2 at AI Impact Summit 2026 (DQ India)](https://www.dqindia.com/esdm/bharatgen-unveils-17b-parameter-sovereign-multilingual-ai-model-at-india-ai-impact-summit-2026-11132799)
- [India Sovereign AI Stack 2026 (Inc42)](https://inc42.com/features/from-llms-to-verticalisation-indias-sovereign-ai-stack-takes-shape/)
- [Sarvam AI India Frugal AI (Rest of World)](https://restofworld.org/2026/india-frugal-ai-sarvam-krutrim-sovereign/)
- [Best Korean LLMs Leaderboard 2026](https://benchlm.ai/leaderboards/korean-llm)
- [HyperCLOVA X 8B Omni arXiv](https://arxiv.org/abs/2601.01792)
- [HyperCLOVA X 8B Omni HuggingFace](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Omni-8B)
- [OmniServe GitHub (NAVER)](https://github.com/NAVER-Cloud-HyperCLOVA-X/OmniServe)
- [Korea National AI Plagiarism Controversy (Korea Times)](https://www.koreatimes.co.kr/amp/business/tech-science/20260107/national-ai-model-project-faces-controversies-over-plagiarism-claims)
- [Upstage Sovereignty Dispute (KoreaTechDesk)](https://koreatechdesk.com/upstage-ai-plagiarism-dispute-korea)
- [Korea Standards for National AI (UPI)](https://www.upi.com/Top_News/World-News/2026/01/08/sovereign-ai/3341767918326/)
- [AI Summit 2026 Three Sovereign Models (FreePressJournal)](https://www.freepressjournal.in/tech/ai-summit-2026-meet-the-3-sovereign-ai-llm-models-that-were-unveiled-in-delhi-to-rival-global-tech-giants)
- [India AI Impact Summit 2026 Wikipedia](https://en.wikipedia.org/wiki/India_AI_Impact_Summit_2026)
- [India Launches Three AI Models at AI Summit (Electronics For You)](https://www.electronicsforyou.biz/industry-buzz/india-launches-three-of-its-own-ai-models-at-ai-summit-2026/)
- [Sarvam-30B HuggingFace](https://huggingface.co/sarvamai/sarvam-30b)
- [Sarvam 105B API Docs](https://docs.sarvam.ai/api-reference-docs/getting-started/models/sarvam-105b)
- [MCP Registry Official Blog (Anthropic)](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/)
- [Sovereign AI in Asia 2026 (DigitalInAsia)](https://digitalinasia.com/2026/03/21/sovereign-ai-asia-every-country-building-own-llm/)
- [HyperCLOVA X 32B Think arXiv](https://arxiv.org/abs/2601.03286)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_mcp_server]] | sibling | 0.28 |
| [[bld_memory_mcp_server]] | downstream | 0.26 |
| [[atom_15_qwen_deepseek]] | sibling | 0.24 |
| [[atom_16_minimax_kimi_glm]] | sibling | 0.22 |
| [[bld_memory_agent_card]] | downstream | 0.20 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.20 |
| [[bld_collaboration_mcp_server]] | downstream | 0.20 |
| [[mcp-server-builder]] | downstream | 0.20 |
| [[p01_kc_terminology_rosetta_stone]] | sibling | 0.20 |
| [[bld_tools_mcp_server]] | downstream | 0.19 |
