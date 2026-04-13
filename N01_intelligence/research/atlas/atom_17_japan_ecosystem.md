---
id: atom_17_japan_ecosystem
kind: knowledge_card
pillar: P01
domain: japanese_llm_agent_ecosystem
title: "ATOM-17: Japanese LLM & Agent Ecosystem -- Deep Dive"
version: 1.0.0
quality: 8.8
tags: [japan, llm, agents, self-evolving, diffusion, sovereign-ai, sakana, nec, ntt, fujitsu, plamo, elyza, cyberagent]
created: 2026-04-13
sources: 23
density: 0.92
---

# ATOM-17: Japanese LLM & Agent Ecosystem

> Research date: 2026-04-13 | Sources: 23 | Scope: 7 organizations, 3 unique paradigms

## Executive Summary

Japan's AI ecosystem operates on a **hybrid coexistence strategy**: domestic LLMs for sovereignty-sensitive workloads (government, medical, finance) coexisting with frontier US models for general capability. The ecosystem produces three globally unique contributions:

1. **Self-evolving agents** (Sakana AI) -- agents that rewrite their own code via evolutionary pressure
2. **Diffusion-based text generation** (ELYZA) -- non-autoregressive LLM architecture applied to Japanese
3. **Tacit knowledge extraction** (NEC cotomi Act) -- converting implicit human expertise into agent behavior, achieving superhuman web task performance

Japan's $6.34B sovereign AI initiative (2025-2026) funds this ecosystem through GENIAC accelerator grants, ABCI 3.0 supercomputer access, and Rapidus 2nm chip fabrication.

---

## 1. Sakana AI -- Evolutionary Intelligence

**Founded**: 2023 (Tokyo) | **Founders**: ex-Google Brain (Llion Jones, David Ha)

### 1.1 Darwin Godel Machine (DGM)

Self-improving coding agent that rewrites its own Python codebase through evolutionary selection.

| Property | Value |
|----------|-------|
| Mechanism | Agent reads own code, proposes modifications, validates empirically |
| Selection | Darwinian: maintain archive of diverse agent variants |
| SWE-bench | 20.0% -> 50.0% (2.5x improvement through self-evolution) |
| Polyglot | 14.2% -> 30.7% (surpasses hand-designed Aider agent) |
| Transfer | Improvements found with Claude 3.5 Sonnet transfer to o3-mini, Claude 3.7 |
| Cross-lang | Python-discovered improvements transfer to Rust, C++, Go |
| Paper | arXiv:2505.22954 (May 2025) |

**Self-discovered improvements include**: patch validation steps, enhanced file viewing, improved editing tools, multi-solution generation with ranking, maintaining histories of failed attempts.

**CEX relevance**: DGM's evolutionary loop (modify -> evaluate -> select -> archive) maps directly to CEX's `/evolve` pipeline. The archive-of-variants concept parallels CEX's quality-gated artifact improvement cycle. Key difference: DGM evolves the agent itself; CEX evolves artifacts produced by fixed agents.

### 1.2 AB-MCTS / TreeQuest -- Collective Intelligence at Inference Time

Inference-time scaling algorithm enabling multiple frontier LLMs to collaborate on problem-solving.

| Property | Value |
|----------|-------|
| Algorithm | Adaptive Branching Monte Carlo Tree Search |
| Balancing | Thompson Sampling across depth (refine) vs width (restart) |
| Multi-LLM | Treats model selection as multi-armed bandit problem |
| ARC-AGI-2 (single) | o4-mini: 27.5% Pass@250 (vs 23% repeated sampling) |
| ARC-AGI-2 (multi) | Gemini-2.5-Pro + o4-mini + DeepSeek-R1-0528: 30%+ Pass@250 |
| Open source | Apache 2.0 (TreeQuest framework) |

**Unique insight**: One LLM's incorrect output serves as a useful hint for another LLM to reach the correct solution. The combination outperforms any individual model -- emergence through collaboration, not scale.

**CEX relevance**: AB-MCTS's multi-model collaboration mirrors CEX's multi-nucleus grid dispatch. N01-N06 each bring different "model personalities" (research vs build vs marketing). TreeQuest's depth-vs-width balancing maps to CEX's wave planning (sequential depth vs parallel width).

### 1.3 Evolutionary Model Merging

Automated discovery of effective model combinations using evolutionary optimization.

| Property | Value |
|----------|-------|
| Method | Evolutionary search over merge recipes (no gradient training) |
| Compute | Minimal -- merging existing models, not training new ones |
| Published | Nature Machine Intelligence (accepted Jan 2025) |
| Follow-up | CycleQD (ICLR 2025) -- evolving swarms of niche LLM agents |
| Tools | Integrated into mergekit, Optuna Hub |

**CycleQD** evolves a population of specialized LLM agents, each occupying a distinct niche, to solve complex agentic workflows. This is quality-diversity optimization applied to agent populations.

---

## 2. NEC cotomi Act -- Tacit Knowledge Agents

**Parent**: NEC Corporation | **LLM base**: cotomi (NEC's proprietary generative AI)

### 2.1 WebArena Benchmark: Superhuman Performance

| Metric | Score |
|--------|-------|
| cotomi Act task success rate | **80.4%** |
| Human baseline | 78.2% |
| Status | First global AI to exceed human performance on WebArena |
| Benchmark scope | EC sites, forums, collaborative development, CMS, map search |

### 2.2 Tacit Knowledge Extraction

The core innovation is **automatic extraction of implicit knowledge** from browser operation histories and logs:

1. Record human operator's browser actions (clicks, navigation, data entry)
2. Extract implicit decision patterns that operators themselves cannot articulate
3. Structure extracted knowledge into reusable procedural formats
4. cotomi analyzes structured knowledge to identify relevant procedures
5. Agent executes web tasks using extracted tacit knowledge, even with vague instructions

**CEX relevance**: cotomi Act's tacit-knowledge-to-agent pipeline parallels CEX's F3 INJECT phase -- loading KCs, brand context, and memory to compensate for user's inability to fully specify requirements. The "vague instruction -> structured execution" pattern is exactly what 8F solves.

### 2.3 Commercialization

- Service launch: FY2026
- Enterprise solution: software + consulting + operational maintenance (since Jan 2026)
- Target: digitizing organizational know-how as agent-executable knowledge assets

---

## 3. NTT tsuzumi 2 -- Lightweight Sovereign LLM

**Parent**: NTT (Nippon Telegraph and Telephone) | **Approach**: Full-scratch development

### 3.1 Design Philosophy

| Property | Value |
|----------|-------|
| Hardware | Runs on **single GPU** |
| Performance | Comparable to GPT-5 across most tasks |
| Japanese | World-top among comparable-size models |
| Training | Full-scratch (no open-source base model dependency) |
| Domain strength | Finance, medical, public sector |
| Data sovereignty | Complete control over training data, rights compliance |

### 3.2 Government Adoption

- Selected for Japan Digital Agency's "Government AI" (Gennai) initiative
- Trial deployment across ministries from FY2026
- Sovereign positioning: fully domestic, auditable training pipeline

### 3.3 Strategic Significance

tsuzumi 2 represents Japan's "lightweight sovereignty" thesis: you don't need a 1T-parameter model for enterprise Japanese tasks. A well-trained, domain-specialized model on a single GPU can match or exceed frontier models in specific verticals, at a fraction of the cost and with full data control.

---

## 4. Fujitsu Takane -- Multi-Agent SDLC Platform

**Parent**: Fujitsu | **LLM**: Takane (proprietary)

### 4.1 AI-Driven Software Development Platform

| Property | Value |
|----------|-------|
| Scope | Full SDLC: requirements -> design -> implementation -> integration testing |
| Architecture | Multiple AI agents collaborating per development stage |
| Protocol | MCP (Model Context Protocol) + inter-agent communication |
| Automation | Full -- no human intervention required |
| Productivity | **100x** (3 person-months -> 4 hours on medical fee revision) |
| Launch | January 2026 (Japan, medical sector first) |

### 4.2 Agent Framework Features

- Low-code / no-code tools for agent development
- MCP support for existing system integration
- Inter-agent communication for coordinated multi-agent operation
- Takane LLM with 94% memory reduction via quantization

### 4.3 Sector Expansion

| Timeline | Sectors |
|----------|---------|
| Jan 2026 | Medical (67 types of medical/government software) |
| FY2026 end | Finance, manufacturing, retail, public services |
| FY2027+ | Customer and partner access |

**CEX relevance**: Fujitsu's multi-agent SDLC platform is architecturally similar to CEX's grid dispatch. Multiple specialized agents (like CEX's N01-N06) collaborate on a complex task, communicating via a protocol layer (MCP / CEX signals). The 100x productivity claim on medical fee revisions demonstrates the power of domain-specialized multi-agent orchestration.

---

## 5. PLaMo (Preferred Networks) -- Full-Scratch Japanese LLM

**Parent**: Preferred Networks (PFN) | **Headquarters**: Tokyo

### 5.1 Model Family

| Model | Purpose | License |
|-------|---------|---------|
| PLaMo Prime | Commercial flagship | Proprietary |
| PLaMo 2.1 Prime | Agent-capable (automated tool calling) | Proprietary |
| PLaMo Lite | Edge devices (cars, manufacturing) | Proprietary |
| PLaMo Translate | Japanese translation specialist | Proprietary |
| PLaMo-100B-Pretrained | Research (non-commercial) | Non-commercial |
| PLaMo-fin-base | Financial domain | Proprietary |

### 5.2 Key Differentiators

- **Full-scratch training**: No dependency on Meta/Google base models
- **PLaMo Translate**: Selected for Japan Digital Agency's Gennai project (FY2026+)
- **Edge deployment**: PLaMo Lite targets automotive and manufacturing -- unique positioning
- **Agent capabilities**: PLaMo 2.1 Prime includes automated tool calling (Oct 2025)

### 5.3 Government Presence

Both PLaMo Translate and NTT's tsuzumi 2 were selected for the Digital Agency's Gennai project, signaling Japan's commitment to multi-vendor domestic AI infrastructure for government operations.

---

## 6. ELYZA -- Diffusion-Based Text Generation

**Parent**: ELYZA, Inc. (SoftBank subsidiary) | **Base**: Dream-v0-Instruct-7B

### 6.1 Architecture: Discrete Diffusion Masked Language Model (DDMLM)

Unlike autoregressive LLMs that generate tokens left-to-right sequentially:

```
Autoregressive:  [START] -> token1 -> token2 -> token3 -> ... -> [END]
                 (sequential, O(n) steps for n tokens)

Diffusion:       [MASK][MASK][MASK][MASK][MASK]
                 -> [MASK][token2][MASK][MASK][MASK]    (step 1: partial reveal)
                 -> [token1][token2][MASK][token4][MASK] (step 2: more reveal)
                 -> [token1][token2][token3][token4][token5] (step N: complete)
                 (iterative denoising, parallel decoding possible)
```

### 6.2 Training Pipeline

| Stage | Data | Scale |
|-------|------|-------|
| Base | Dream-v0-Instruct-7B | Pre-trained |
| Continued pretraining | Japanese text corpus | ~62B tokens |
| Instruction tuning | Japanese instruction data | ~1.8B tokens (10 epochs) |

### 6.3 Unique Properties

| Property | Value |
|----------|-------|
| Step reduction | Up to **8x fewer diffusion steps** while maintaining quality |
| Parallel decoding | Multiple tokens generated simultaneously (not sequential) |
| Parameters | 7B |
| Models released | Base + Instruct variants on Hugging Face |
| Paper | arXiv:2508.15487 (Aug 2025) |

### 6.4 Why Diffusion LLMs Matter

1. **Parallel generation**: Potential latency reduction vs autoregressive models
2. **Global coherence**: All tokens refined simultaneously -- better long-range consistency
3. **Data efficiency**: Reports indicate diffusion LLMs outperform autoregressive models when training data is limited (high-epoch, small unique corpus)
4. **New inference paradigm**: Step count (not token count) as primary compute dimension
5. **Japanese advantage**: Limited Japanese training data makes diffusion's data efficiency particularly valuable

**CEX relevance**: Diffusion LLMs represent a paradigm shift from sequential to parallel text generation. If matured, this could change how CEX's F6 PRODUCE operates -- instead of streaming tokens, generating complete artifacts via iterative refinement (similar to how image diffusion models work).

---

## 7. CyberAgent -- Open-Source Japanese LLM

**Parent**: CyberAgent, Inc. | **Focus**: Ad tech, internet services

### 7.1 CyberAgentLM3-22B (CALM3)

| Property | Value |
|----------|-------|
| Parameters | 22.5 billion |
| Training | From scratch, 2.0 trillion tokens |
| Performance | Equivalent to Llama-3-70B-Instruct (Nejumi leaderboard 3) |
| License | Apache 2.0 (fully commercial) |
| Release | July 2024 |
| Architecture | Decoder-only |

### 7.2 DeepSeek-R1 Japanese Adaptations

| Model | Base | Release |
|-------|------|---------|
| DeepSeek-R1-Distill-Qwen-32B-Japanese | DeepSeek-R1-Distill-Qwen-32B | Jan 2025 |
| DeepSeek-R1-Distill-Qwen-14B-Japanese | DeepSeek-R1-Distill-Qwen-14B | Jan 2025 |

### 7.3 Self-Improve Experimental

CyberAgent released `calm3-22b-chat-selfimprove-experimental`, indicating active research into self-improvement training loops -- aligning with the broader Japanese ecosystem's interest in self-evolving systems.

---

## 8. Cross-Cutting Themes

### 8.1 Hybrid Coexistence Strategy

Japan does NOT attempt to out-scale US frontier labs. Instead:

| Layer | Strategy | Examples |
|-------|----------|---------|
| Frontier general | Use US models (GPT-5, Claude, Gemini) | Via API, cloud partnerships |
| Domain-specific | Domestic models, full data sovereignty | tsuzumi 2 (medical/finance), PLaMo-fin (finance) |
| Edge / embedded | Lightweight domestic models | PLaMo Lite (cars), tsuzumi 2 (single GPU) |
| Government | Strictly domestic | Gennai project (tsuzumi 2 + PLaMo Translate) |
| Agent layer | Domestic orchestration over any model | cotomi Act, Fujitsu agent framework |

This is **not** "build our own GPT-5." It is "control the agent layer and domain adaptation while consuming frontier models as commodities."

### 8.2 Self-Evolving Systems (Unique to Japan's Ecosystem)

| System | What Evolves | Mechanism |
|--------|-------------|-----------|
| DGM (Sakana) | The agent's own code | Evolutionary selection over code variants |
| CycleQD (Sakana) | Population of specialized agents | Quality-diversity optimization |
| Evolutionary Model Merge (Sakana) | Model weights | Evolutionary search over merge recipes |
| AB-MCTS (Sakana) | Inference strategy | Thompson Sampling over depth/width/model |
| CALM3-selfimprove (CyberAgent) | Training data/process | Self-improvement training loops |

Sakana AI alone contributes four distinct self-evolving paradigms. This is the densest concentration of evolutionary AI research outside of DeepMind.

### 8.3 Government AI Infrastructure

| Component | Provider | Status |
|-----------|----------|--------|
| Gennai (Digital Agency) | tsuzumi 2 + PLaMo Translate | Trial FY2026 |
| ABCI 3.0 (supercomputer) | AIST | Available since Jan 2025 |
| GENIAC (accelerator) | METI | Active, computing grants |
| Sovereign AI budget | Government | $6.34B (1 trillion yen) |
| 2nm chip fabrication | Rapidus Corp | Pilot -> full-wafer 2025 |
| Sovereign cloud | SoftBank + Oracle Alloy | $12.7B data centers |

### 8.4 Diffusion vs Autoregressive -- Emerging Paradigm Split

| Dimension | Autoregressive | Diffusion (DDMLM) |
|-----------|---------------|-------------------|
| Generation | Sequential (left-to-right) | Parallel (iterative denoising) |
| Latency | O(n) sequential steps | O(k) steps, k << n possible |
| Coherence | Local (each token sees only left context) | Global (all positions refined together) |
| Data efficiency | Requires massive unique data | Strong with limited data (high epoch) |
| Maturity | Production-ready | Experimental (7B scale) |
| Japanese advantage | Limited Japanese data is a bottleneck | Limited data is less penalizing |

---

## 9. Competitive Positioning Map

```
                    SCALE (parameters)
                    |
          1T+ ......|...... SoftBank Sarashina (planned)
                    |
         100B ......|...... PLaMo-100B (research)
                    |
          22B ......|...... CyberAgent CALM3-22B
                    |
           7B ......|...... ELYZA Diffusion 7B, tsuzumi 2
                    |
          <7B ......|...... PLaMo Lite (edge)
                    |
                    +------------------------------------------
                         Domain     General    Agent     Self-evolving
                         Specialist Purpose    Layer     System
                         |          |          |         |
                         tsuzumi2   CALM3      cotomi    DGM
                         PLaMo-fin  PLaMo      Act       CycleQD
                         Takane     Prime      Fujitsu   AB-MCTS
```

---

## 10. Key Takeaways for CEX

| Japanese Innovation | CEX Parallel | Potential Import |
|--------------------|-------------|-----------------|
| DGM self-evolving agents | `/evolve` pipeline | Agent that rewrites its own builder ISOs |
| AB-MCTS multi-model collaboration | Grid dispatch (N01-N06) | Thompson Sampling over nucleus selection |
| cotomi Act tacit knowledge extraction | F3 INJECT (KC loading) | Auto-extract user's implicit preferences from interaction history |
| Fujitsu 100x SDLC automation | `/mission` orchestration | Domain-specific multi-agent wave planning |
| ELYZA diffusion text gen | F6 PRODUCE | Non-sequential artifact generation (global coherence) |
| Hybrid coexistence | Multi-provider routing | Domestic (local Ollama) for sensitive, frontier for capability |
| CycleQD niche agents | Builder specialization | Evolve builder ISOs to occupy distinct quality niches |

---

## Sources

- [Sakana AI -- Darwin Godel Machine](https://sakana.ai/dgm/)
- [Sakana AI -- AB-MCTS / TreeQuest](https://sakana.ai/ab-mcts/)
- [Darwin Godel Machine (arXiv:2505.22954)](https://arxiv.org/abs/2505.22954)
- [Sakana AI -- Evolutionary Model Merge](https://sakana.ai/evolutionary-model-merge/)
- [Sakana AI -- CycleQD](https://sakana.ai/cycleqd/)
- [NEC cotomi Act Press Release](https://jpn.nec.com/press/202508/20250827_02.html)
- [NEC cotomi Act Enterprise Solution](https://jpn.nec.com/press/202512/20251203_01.html)
- [NTT tsuzumi 2 R&D](https://www.rd.ntt/e/research/LLM_tsuzumi.html)
- [NTT tsuzumi 2 Press Release](https://group.ntt/en/newsrelease/2025/10/20/251020a.html)
- [NTT tsuzumi 2 -- Global Insights](https://www.global.ntt/insights-hub/ntts-tsuzumi-2/)
- [Fujitsu AI Platform Launch](https://global.fujitsu/en-global/pr/news/2026/01/26-02)
- [Fujitsu AI-Driven SDLC Platform](https://global.fujitsu/en-global/pr/news/2026/02/17-01)
- [PFN PLaMo 2.1 Prime](https://www.preferred.jp/en/news/pr20251007-2)
- [PFN PLaMo Translate -- Government Adoption](https://www.preferred.jp/en/news/pr20251202)
- [PLaMo 2 Technical Report (arXiv)](https://arxiv.org/html/2509.04897v1)
- [ELYZA Diffusion Base (Hugging Face)](https://huggingface.co/elyza/ELYZA-Diffusion-Base-1.0-Dream-7B)
- [ELYZA Diffusion Instruct (Hugging Face)](https://huggingface.co/elyza/ELYZA-Diffusion-Instruct-1.0-Dream-7B)
- [CyberAgent CALM3-22B (Hugging Face)](https://huggingface.co/cyberagent/calm3-22b-chat)
- [CyberAgent DeepSeek-R1 Japanese](https://huggingface.co/cyberagent/DeepSeek-R1-Distill-Qwen-32B-Japanese)
- [Japan Sovereign AI -- Asia Times](https://asiatimes.com/2025/09/inside-japans-struggle-to-build-sovereign-ai/)
- [Japan $6B Sovereign AI Initiative](https://markets.financialcontent.com/wral/article/tokenring-2026-1-13-japans-6-billion-sovereign-ai-gamble-a-bold-bid-for-silicon-and-software-independence)
- [The Decoder -- DGM](https://the-decoder.com/sakana-ais-darwin-godel-machine-evolves-by-rewriting-its-own-code-to-boost-performance/)
- [The Decoder -- AB-MCTS](https://the-decoder.com/sakana-ais-new-algorithm-lets-large-language-models-work-together-to-solve-complex-problems/)
