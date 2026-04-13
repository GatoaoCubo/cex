---
id: atom_17_japan_ecosystem
kind: knowledge_card
pillar: P01
domain: japanese_llm_agent_ecosystem
title: "ATOM-17: Japanese LLM & Agent Ecosystem -- Deep Dive"
version: 1.1.0
quality: 8.8
tags: [japan, llm, agents, self-evolving, diffusion, sovereign-ai, sakana, nec, ntt, fujitsu, plamo, elyza, cyberagent, rakuten, openDXA, mcp, edge-deployment]
created: 2026-04-13
updated: 2026-04-13
sources: 32
density: 0.94
---

# ATOM-17: Japanese LLM & Agent Ecosystem

> Research date: 2026-04-13 | Hydrated: 2026-04-13 | Sources: 32 | Scope: 9 organizations, 4 unique paradigms

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

### 1.4 DGM -- Implementation Architecture (arXiv v3, March 2026)

**Paper**: arXiv:2505.22954 v3 (latest: 2026-03-12) | **Code**: github.com/lemoz/darwin-godel-machine (Apache 2.0)

The DGM paper reached v3 in March 2026 with expanded safety analysis and cross-language transfer experiments.

#### Core Loop Implementation

```
INITIALIZE: seed agent + empty archive
LOOP:
  1. SELECT parent from archive (quality-diversity selection)
  2. PROPOSE: parent agent reads its own code -> generates modification
  3. SANDBOX: execute modified agent in isolated container
     - No internet access during evaluation
     - Resource limits: CPU time, memory, disk I/O
     - Human supervision checkpoint available
  4. EVALUATE: run on benchmark subset (SWE-bench / Polyglot)
  5. ARCHIVE: add if improves score OR adds diversity (MAP-Elites style)
  6. REPEAT from SELECT
```

#### Self-Discovered Improvements (verified across runs)

| Improvement Type | What Agent Changed | Benchmark Gain |
|-----------------|-------------------|----------------|
| Patch validation | Added pre-flight check before applying patches | Reduces invalid patches |
| Enhanced file viewing | Broader context window for code viewing | Better understanding |
| Multi-solution ranking | Generate N solutions, pick best via secondary eval | +12% SWE-bench |
| Failure history | Maintain log of failed attempts per task | Avoids repeat failures |
| Editing tool refinement | Finer-grained edit operations | Fewer syntax errors |

#### Transfer Generalization (CEX-relevant finding)

Improvements discovered using Claude 3.5 Sonnet as the base model transferred to:
- o3-mini: +18% SWE-bench
- Claude 3.7: +15% SWE-bench
- Cross-language: Python improvements applied to Rust, C++, Go agents with no re-training

This confirms the improvements are structural (better reasoning/tooling patterns), not model-specific overfitting.

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

### 2.2 Tacit Knowledge Extraction -- Pipeline Detail

The core innovation is **automatic extraction of implicit knowledge** from browser operation histories and logs:

1. Record human operator's browser actions (clicks, navigation, data entry)
2. Extract implicit decision patterns that operators themselves cannot articulate
3. Structure extracted knowledge into reusable procedural formats
4. cotomi analyzes structured knowledge to identify relevant procedures
5. Agent executes web tasks using extracted tacit knowledge, even with vague instructions

#### What "Tacit Knowledge" Includes (beyond surface actions)

NEC's system extracts not just click-by-click sequences but **cognitive layers**:

| Layer | What Is Captured | Example |
|-------|-----------------|---------|
| Surface | Button clicks, URL navigation, form fills | "Clicked 'Submit' on /order page" |
| Decision criteria | WHY a specific path was chosen | "Chose express shipping because lead time < 3 days" |
| Judgment rationale | Business rules that aren't written down | "Checked backup supplier when primary shows 0 stock" |
| Exception handling | Deviations from standard procedure | "When error code 403, refresh session then retry" |
| Contextual triggers | External signals that change behavior | "If time > 15:00, route to next-day processing" |

This multi-layer extraction enables agents to handle **novel situations** not explicitly in training data by generalizing from captured decision patterns.

**CEX relevance**: cotomi Act's tacit-knowledge-to-agent pipeline parallels CEX's F3 INJECT phase -- loading KCs, brand context, and memory to compensate for user's inability to fully specify requirements. The "vague instruction -> structured execution" pattern is exactly what 8F solves.

### 2.3 Commercialization

- Service launch: FY2026
- Enterprise solution: software + consulting + operational maintenance (since Jan 2026)
- Target: digitizing organizational know-how as agent-executable knowledge assets

### 2.4 Government AI Deployment (March 2026)

cotomi Act was selected for Japan's Digital Agency **"Government AI" (Gennai) initiative** in March 2026, marking the first government-sanctioned deployment of a superhuman web automation agent:

| Property | Detail |
|----------|--------|
| Initiative | Digital Agency "Gennai" (Government AI) |
| Deployment date | March 2026 |
| Task scope | Automated processing of government web-based workflows |
| Significance | Government validation of superhuman agent for public sector |
| Partner | NEC + Digital Agency joint deployment

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

### 3.2 Technical Architecture -- Quantization and Compression

The original tsuzumi (v1) was released in two sizes, establishing the "lightweight sovereignty" pattern:

| Version | Parameters | Use Case |
|---------|-----------|---------|
| tsuzumi ultra-lightweight | 600M (0.6B) | Embedded, mobile, IoT |
| tsuzumi lightweight | 7B | Single GPU enterprise |
| tsuzumi 2 | Undisclosed (single GPU) | Successor -- GPT-5 parity target |

**tsuzumi 2 key architectural improvements over v1:**

1. **Quantization**: Lower-bit parameter quantization for speed + reduced memory footprint
2. **Long-document context**: Significantly improved handling of long documents and complex context (explicit limitation of v1)
3. **Transformer backbone**: Standard transformer architecture with proprietary optimizations (not a custom architecture -- deliberate choice for auditability and safety compliance)
4. **Efficient tokenization**: Japanese-optimized tokenizer reduces token count vs generic multilingual tokenizers -- 20-30% fewer tokens for equivalent Japanese text
5. **Adapter layer**: Cross-attention adapter stack with learnable tokens for multi-modal input (visual document reading -- announced separately in April 2024, integrated in v2)

### 3.3 Government Adoption

- Selected for Japan Digital Agency's "Government AI" (Gennai) initiative
- Trial deployment across ministries from FY2026
- Sovereign positioning: fully domestic, auditable training pipeline

### 3.4 Strategic Significance

tsuzumi 2 represents Japan's "lightweight sovereignty" thesis: you don't need a 1T-parameter model for enterprise Japanese tasks. A well-trained, domain-specialized model on a single GPU can match or exceed frontier models in specific verticals, at a fraction of the cost and with full data control.

**Competitive comparison vs. alternatives:**

| Model | Size | Single GPU? | Japanese? | Data sovereignty? |
|-------|------|-------------|-----------|------------------|
| tsuzumi 2 | 7B (est.) | YES | World-top (comparable) | Full (Japan-only) |
| Llama 3.1 8B | 8B | YES | Moderate | None (Meta-controlled) |
| GPT-4o mini | Unknown | NO (API only) | Good | None |
| Gemma 2 9B | 9B | YES | Moderate | None (Google) |

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

### 4.3 MCP Integration -- Technical Architecture

Fujitsu's MCP implementation enables the multi-agent SDLC platform to connect to **existing enterprise legacy systems** without rewriting interfaces:

```
[Takane LLM Core]
      |
      | MCP protocol layer
      |
      +-- [Requirements Agent] <--> ERP/ticket systems (MCP server)
      +-- [Design Agent]       <--> Architecture docs (MCP server)
      +-- [Implementation Agent] <--> Git repos (MCP server)
      +-- [Test Agent]         <--> CI/CD pipelines (MCP server)
      |
      | Inter-agent communication bus
      |
[Coordinator Agent] -- synthesizes outputs across agents
```

**Why MCP is critical for Fujitsu's use case:**

| Challenge | MCP Solution |
|-----------|-------------|
| 67 types of legacy medical software | Each system exposes MCP server interface |
| Agents need shared context | MCP resources shared across agent tree |
| No custom integration per system | Standard MCP server wraps any existing API |
| Audit trail required | MCP call logs satisfy medical compliance |

**Live deployment data (January 2026 medical fee revision):**
- Input: medical fee regulation changes (legal documents)
- Output: working code modifications across 67 software systems
- Time: 4 hours (vs 3 person-months conventional)
- Method: Requirements Agent parsed regulations -> Design Agent produced specs -> Implementation Agent wrote code -> Test Agent validated

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

### 5.3 PLaMo Lite -- Edge Deployment Specifications

PLaMo-1B is the first released model in the PLaMo Lite SLM series, enabling on-device inference for industrial applications:

| Property | Value |
|----------|-------|
| Parameters | 1 billion |
| Pretraining tokens | 4 trillion |
| Deployment target | Snapdragon 8 Elite (Qualcomm) |
| Throughput on device | 68.21 tokens/second |
| Time to first token | 0.031 - 1.006 seconds |
| Precision | w4a16 (4-bit weights, 16-bit activations) |
| Runtime | QNN_CONTEXT_BINARY (Qualcomm Neural Network) |
| Distribution | Qualcomm AI Hub + Hugging Face |

**Target edge platforms:**

| Platform | Application | Key Requirement |
|----------|------------|-----------------|
| Automotive (Snapdragon Cockpit Elite) | In-vehicle AI assistant, navigation | <1s TTFT, offline operation |
| Industrial robots | Task instruction understanding | Real-time response, EMI resistance |
| Manufacturing equipment | Anomaly detection reporting | On-device (no cloud latency) |
| PCs (on-premises) | Enterprise AI without cloud data exposure | Data sovereignty |

**PFCI (Preferred Computing Infrastructure)**: PFN's joint venture with cloud providers, launching early 2026, will offer AI cloud services on MN-Core series hardware -- enabling PLaMo Prime/2.1 at scale for organizations that cannot run edge-only.

**PLaMo on Qualcomm AI Hub**: PFN is listed as an official Qualcomm AI Hub model-maker, signaling a formal partnership for automotive + mobile SLM distribution.

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

## 11. New Japanese AI Developments (2026)

Three significant new entries to the Japanese AI ecosystem emerged in early 2026:

### 11.1 Rakuten AI 3.0 -- Japan's Largest LLM

**Released**: March 17, 2026 | **License**: Apache 2.0 | **Source**: GENIAC Project

| Property | Value |
|----------|-------|
| Architecture | Mixture of Experts (MoE) |
| Scale | ~700B parameters (Japan's largest) |
| Training | GENIAC accelerator (METI + NEDO funding) |
| Benchmark | Best-in-class for Japanese language tasks |
| License | Apache 2.0 (fully open, commercial) |
| Cost vs frontier | 90% reduction vs GPT-4/Claude in Rakuten ecosystem |
| Distribution | Hugging Face (Rakuten Group official) |
| Agent platform | Rakuten AI -- agentic platform across Rakuten Group services |

**Rakuten ecosystem integration**: Rakuten AI 3.0 powers the agentic layer across shopping, fintech (Rakuten Pay), travel, entertainment, and telecom (Rakuten Mobile). This is the first Japanese domestic LLM deployed at consumer internet scale (150M+ Rakuten users globally).

**MoE advantage**: At ~700B total parameters with ~70B active per inference, Rakuten AI 3.0 achieves frontier-level Japanese performance at a fraction of the compute cost. This is the same architecture as Mixtral and GPT-4 (estimated).

**GENIAC context**: Rakuten was selected for GENIAC third-term (July 2025). The program provides ABCI 3.0 supercomputer access + funding for full-scratch Japanese LLM training.

### 11.2 AI Alliance OpenDXA -- Industrial AI Agent Framework

**Released**: Early 2026 | **License**: Open source | **Founding members**: IBM, NEC, Panasonic

OpenDXA is an open-source agent framework specifically designed for **industrial AI applications** with explainability requirements:

| Property | Value |
|----------|-------|
| Focus | Complex industrial workflows |
| Key feature | Explainable AI (XAI) built into agent reasoning |
| Japan chapter | AI Alliance Japan (9 founding members) |
| First project | Supporting LLM-jp (Japan national language model) |
| Target domains | Manufacturing, semiconductor, navigation |
| Governance | AI Alliance (IBM leadership, open multi-vendor) |

**AI Alliance Japan founding members**: IBM, NEC, Panasonic + 6 others. Focus areas:
1. Semiconductor manufacturing AI (Japan's strategic priority)
2. Navigation/autonomous systems AI
3. Japanese-language AI model support (LLM-jp consortium)

**Comparison vs Fujitsu's SDLC platform:**

| Dimension | OpenDXA | Fujitsu SDLC Platform |
|-----------|---------|----------------------|
| Governance | Open source (multi-vendor) | Proprietary (Fujitsu) |
| Target | Industrial general | Software development |
| Explainability | Built-in (core requirement) | Not emphasized |
| LLM | Model-agnostic | Takane (proprietary) |
| Access | Open source | License |

### 11.3 Hakuhodo Technologies -- Autonomous Ad Production

**Deployed**: 2026 | **Tech**: NVIDIA NeMo Agent Toolkit + NVIDIA AI Blueprints

Hakuhodo Technologies (major Japanese ad agency group) deployed autonomous AI agents for advertisement production -- the first Japanese media company to use agentic AI for creative at scale:

| Property | Value |
|----------|-------|
| Task | Autonomous ad production (brief -> final creative) |
| Stack | NVIDIA NeMo Agent + NVIDIA AI Blueprints |
| Domain | Advertising, media, creative industries |
| Significance | Agentic AI entering Japan's $50B+ advertising market |

---

## 10. Key Takeaways for CEX

| Japanese Innovation | CEX Parallel | Potential Import |
|--------------------|-------------|-----------------|
| DGM self-evolving agents | `/evolve` pipeline | Agent that rewrites its own builder ISOs |
| DGM sandboxed evaluation | Artifact validation in F7 GOVERN | Isolated eval container per artifact improvement |
| AB-MCTS multi-model collaboration | Grid dispatch (N01-N06) | Thompson Sampling over nucleus selection |
| cotomi Act tacit knowledge extraction | F3 INJECT (KC loading) | Auto-extract user's implicit preferences from interaction history |
| cotomi Act judgment criteria capture | F4 REASON decision manifests | GDP manifests as "judgment criteria" artifacts |
| Fujitsu 100x SDLC automation | `/mission` orchestration | Domain-specific multi-agent wave planning |
| Fujitsu MCP inter-agent comms | CEX signals (.cex/runtime/signals/) | Replace signal files with MCP resource layer |
| ELYZA diffusion text gen | F6 PRODUCE | Non-sequential artifact generation (global coherence) |
| Hybrid coexistence | Multi-provider routing | Domestic (local Ollama) for sensitive, frontier for capability |
| CycleQD niche agents | Builder specialization | Evolve builder ISOs to occupy distinct quality niches |
| Rakuten AI 3.0 MoE | Model routing (cex_router.py) | Route to MoE model for cost-efficiency on batch tasks |
| PLaMo-1B on-device | Preflight (cex_preflight.py) | Run PLaMo-1B locally for zero-cost context pre-compilation |
| OpenDXA explainability | 8F trace output | XAI-style reasoning trace as required audit artifact |

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
- [DGM arXiv:2505.22954 v3 (March 2026)](https://arxiv.org/abs/2505.22954)
- [DGM GitHub implementation (lemoz)](https://github.com/lemoz/darwin-godel-machine)
- [NEC cotomi Act -- Tacit Knowledge Detail (Ledge.ai)](https://ledge.ai/articles/nec_cotomi_act_web_agent_implicit_knowledge)
- [NEC cotomi Act -- AI Smiley Analysis](https://aismiley.co.jp/ai_news/nec-ai-cotomi-act/)
- [Fujitsu AI-Driven SDLC Platform (PR Newswire)](https://www.prnewswire.com/news-releases/fujitsu-automates-entire-software-development-lifecycle-with-new-ai-driven-software-development-platform-302689406.html)
- [Fujitsu SDLC Platform -- Electronics Media Analysis](https://www.electronicsmedia.info/2026/02/17/fujitsu-ai-driven-software-development-platform/)
- [NTT tsuzumi 2 Blog -- The Model Strikes Back](https://group.ntt/en/magazine/blog/tsuzumi2/)
- [NTT tsuzumi Lightweight LLM (ThinkTools analysis)](https://thinktools.ai/blog/ntts-lightweight-llm-enables-enterprise-ai-on-a-single-gpu)
- [PLaMo-1B Qualcomm AI Hub](https://aihub.qualcomm.com/models/plamo_1b)
- [Preferred Networks -- Qualcomm AI Hub partnership](https://aihub.qualcomm.com/model-makers/preferred-networks)
- [Rakuten AI 3.0 Press Release (March 2026)](https://global.rakuten.com/corp/news/press/2026/0317_01.html)
- [Rakuten AI 3.0 Unveiled (December 2025)](https://global.rakuten.com/corp/news/press/2025/1218_01.html)
- [Rakuten AI Agentic Platform 2025](https://rakuten.today/blog/rakuten-ai-in-2025-embracing-agentic-ai.html)
- [AI Alliance OpenDXA + AI Alliance Japan Launch](https://thealliance.ai/blog/the-ai-alliance-releases-new-ai-powered-programmin)
- [Japan NVIDIA AI Day -- 320x AI demand forecast 2030](https://blogs.nvidia.com/blog/ai-day-tokyo/)
