---
id: n01_atom_18_korea_india
kind: knowledge_card
pillar: P01
title: "Atom 18: Korean + Indian LLM Agent Ecosystems"
version: 1.0.0
created: 2026-04-13
author: n01_intelligence
domain: research-intelligence
quality: 8.9
tags: [atom, korea, india, sovereign-ai, mcp, voice-first, multilingual, agent, moe]
tldr: "Korea builds MCP platforms + MoE agents (PlayMCP, P-C-G, Solar Pro3); India builds voice-first multilingual agents (Sarvam 105B, Krutrim Kruti, Indic LLM Arena). Both pursue sovereign AI with government backing."
density_score: 0.92
---

# Atom 18: Korean + Indian LLM Agent Ecosystems

**Scope**: Sovereign LLM programs, agent architectures, MCP platforms, voice-first design, multilingual coverage.
**Period**: 2025-Q2 to 2026-Q2 | **Sources**: 25+ | **Date**: 2026-04-13

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

**Training pipeline**: Three-stage -- pre-training (sigmoid-based expert routing), SFT (curated prompts), RL (asynchronous GRPO with adaptive curriculum). All stages developed and executed in-house on domestic compute.

**Inference optimization**: 3-6x throughput on H100; 1.5-3x on L40S. Apple Silicon MXFP4 delivers 20-40% higher throughput. Disaggregated serving architecture.

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

### 2.3 AI4Bharat Indic LLM Arena

**The Language-Context-Safety Evaluation Triad**:

| Dimension | What It Measures | India-Specific Examples |
|-----------|-----------------|----------------------|
| **Language** | Code-mixing fluency (Hinglish, Tanglish), script handling, multilingual coherence | "Book a cab to Koramangala, wahan se Indiranagar jaana hai" (Hindi-English mix) |
| **Context** | Cultural and regional appropriateness, local knowledge | Gift suggestions for housewarming reflect Indian practices, not Western norms; agriculture/finance/healthcare region-specific queries |
| **Safety** | India-specific harms: regional bias, communal misinformation, caste-based stereotypes | Detecting caste stereotypes, communal tension amplification, regional discrimination |

**Scoring**: Human-in-the-loop via anonymous side-by-side comparisons. Bradley-Terry model for statistically robust rankings from user votes. Not automated metrics -- humans judge cultural nuance.

**Phases**:

| Phase | Scope | Status |
|-------|-------|--------|
| Phase 1 | Text across multiple Indian languages + code-mixed | Live |
| Phase 2 | Vision + audio (omni-modal) | Planned |
| Phase 3 | Agentic tasks: PDFs, web search, tool-calls | Planned |

**CEX relevance**: The Language-Context-Safety triad is a transferable evaluation framework. Any non-English agent system needs equivalent dimensions. Code-mixing evaluation is particularly important -- real users do not speak "pure" languages.

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

### 3.2 MoE as Universal Strategy

Both ecosystems converge on MoE as the cost-performance architecture for sovereign agents:

| Model | Total | Active | Ratio |
|-------|-------|--------|-------|
| Kakao Kanana-2 | 32B | 3B | 10.7:1 |
| Upstage Solar Pro3 | 102B | 12B | 8.5:1 |
| Sarvam 105B | 105B | 10.3B | 10.2:1 |
| Sarvam 30B | 30B | 2.4B | 12.5:1 |

MoE ratios of 8-12:1 are the sweet spot -- frontier reasoning at mid-tier inference cost. This is particularly important for sovereign deployments where domestic compute is constrained.

### 3.3 Key Patterns for CEX

| Pattern | Source | CEX Mapping |
|---------|--------|-------------|
| MCP marketplace | PlayMCP (Kakao) | P04_tools: MCP server registry with auth bridging |
| Role-separated agents | P-C-G (Korean research) | 8F pipeline: F4=Planner, F5=Caller, F6=Generator |
| Korean-first value policy | P-C-G paper | Non-English agent value handling in cex_router.py |
| Voice-first input | Krutrim/Kruti | P05_output: voice modality for agent interaction |
| 22-language tokenizer | Sarvam AI | P01_knowledge: multilingual tokenizer efficiency |
| Language-Context-Safety eval | Indic LLM Arena | P07_evaluation: culture-aware scoring rubric |
| Code-mix fluency | AI4Bharat | P03_prompt: Hinglish/Tanglish prompt handling |
| Sovereign compute | Both ecosystems | P09_config: domestic infra routing preference |

---

## 4. Signals and Implications

### 4.1 For Agent Builders

1. **MCP is going mainstream in Asia**. PlayMCP proves the pattern scales to platform ecosystems. Expect similar MCP marketplaces from Naver, LINE, WeChat.

2. **P-C-G validates modular agent architecture**. The Planner-Caller-Generator separation with role-specialized SLMs is more token-efficient than monolithic agent approaches. This aligns with CEX's multi-nucleus design.

3. **Voice-first is not optional for non-English markets**. Krutrim's architecture decision reflects a billion-user reality: typing in English is a barrier. Agent systems targeting global markets need voice input as a primary modality.

4. **22-language tokenizer efficiency is a moat**. Sarvam's custom tokenizer reduces cost per token for underserved languages. This makes multilingual agents economically viable at scale.

5. **Code-mixing is the real evaluation frontier**. Pure language benchmarks miss how people actually talk. Hinglish, Tanglish, and similar code-mixed varieties are the true test of multilingual models.

### 4.2 Confidence Assessment

| Claim | Confidence | Evidence |
|-------|-----------|----------|
| Korea leads Asia in MCP adoption | HIGH | PlayMCP live, Kakao ecosystem integration |
| P-C-G is production-viable for Korean agents | MEDIUM | Paper only, no production deployment reported |
| Sarvam 105B is competitive with global models | HIGH | MMLU 90.6, Math500 98.6, Apache 2.0 release |
| Krutrim/Kruti will scale to 100M+ users | LOW | 100K downloads, 13 languages, unproven distribution |
| Both governments will sustain funding | HIGH | $175M (Korea) + $1.1B (India) already committed |
| MoE 8-12:1 ratio is the sovereign architecture standard | HIGH | 4/4 major models use this ratio |

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
- [SK Telecom A.X K1 at MWC 2026](https://telecomlead.com/telecom-services/sk-telecom-showcases-full-stack-ai-strategy-at-mwc-2026-with-a-x-k1-model-and-ai-infrastructure-innovations-124676)
- [SK Telecom A.X K1 519B Announcement](https://www.prnewswire.com/news-releases/sk-telecom-unveils-ax-k1-koreas-first-500b-scale-hyperscale-ai-model-302649835.html)
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
- [South Korea LLM Powerhouses Overview](https://www.marktechpost.com/2025/08/21/meet-south-koreas-llm-powerhouses-hyperclova-ax-solar-pro-and-more/)
