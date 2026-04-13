---
id: atom_16_minimax_kimi_glm
kind: knowledge_card
pillar: P01
title: "MiniMax M2/M2.7 + Kimi K2.5 + GLM-5.1 -- Chinese Agentic Tool-Calling Paradigms"
version: 0.2.0
quality: 8.8
tags: [minimax, kimi, moonshot, zhipu, glm, tool-calling, interleaved-thinking, agent-swarm, all-tools, cispo, parl, chinese-ai, self-evolution, decentralized-agents]
sources:
  - https://www.minimax.io/news/why-is-interleaved-thinking-important-for-m2
  - https://platform.minimax.io/docs/guides/text-m2-function-call
  - https://www.minimax.io/news/post-training-experience-and-insights-for-agent-models
  - https://github.com/MiniMax-AI/MiniMax-M2
  - https://www.minimax.io/news/minimax-m25
  - https://www.minimax.io/news/minimax-m27-en
  - https://arxiv.org/pdf/2506.13585
  - https://swift.readthedocs.io/en/latest/Instruction/GRPO/AdvancedResearch/CISPO.html
  - https://github.com/MiniMax-AI/Mini-Agent
  - https://github.com/MoonshotAI/Kimi-K2.5
  - https://arxiv.org/html/2602.02276v1
  - https://www.kimi.com/blog/kimi-k2-5
  - https://medium.com/@kimi_moonshot/meet-ok-computer-the-agent-mode-in-kimi-2fb0dbf05ce0
  - https://aiagentindex.mit.edu/2025/kimi-ok-computer/
  - https://www.analyticsvidhya.com/blog/2026/04/glm-5-1/
  - https://lushbinary.com/blog/glm-5-1-vectordbbench-6000-tool-calls-21k-qps/
  - https://lushbinary.com/blog/glm-5-1-developer-guide-long-horizon-agentic-coding/
  - https://www.emergentmind.com/topics/cispo-algorithm
  - https://developer.nvidia.com/blog/minimax-m2-7-advances-scalable-agentic-workflows-on-nvidia-platforms-for-complex-ai-applications/
  - https://www.marktechpost.com/2026/04/12/minimax-just-open-sourced-minimax-m2-7-a-self-evolving-agent-model-that-scores-56.22-on-swe-pro-and-57.0-on-terminal-bench-2/
date: 2026-04-13
---

# MiniMax M2 + Kimi K2.5 + GLM-5.1 -- Chinese Agentic Tool-Calling Paradigms

Three Chinese AI labs have independently developed tool-calling paradigms that
diverge significantly from the OpenAI/Anthropic/Google function-calling standard.
Each introduces vocabulary, training methods, and architectural patterns with no
direct Western equivalent. This atom catalogs those unique concepts.

---

## 1. Model Summary

| Dimension | MiniMax M2/M2.5 | Kimi K2.5 | GLM-5.1 (Z.ai) |
|-----------|-----------------|-----------|-----------------|
| Org | MiniMax (Beijing) | Moonshot AI (Beijing) | Z.ai / Zhipu AI (Beijing) |
| Release | Oct 2025 (M2), Feb 2026 (M2.5) | Jan 2026 | Apr 2026 |
| Architecture | MoE 230B total, 10B active | MoE 1T total, 32B active | MoE 744B total, 40B active |
| Context | 128K (M2), 1M (M2.5) | 256K | 200K (202,752 tokens) |
| Key innovation | Interleaved Thinking + CISPO | Agent Swarm + 300-step chains | All Tools + 6000+ tool calls |
| SWE-Bench Verified | 69.4% (M2), 80.2% (M2.5) | 76.8% | 58.4% (SWE-Bench Pro) |
| BrowseComp | 44.0% (M2), 76.3% (M2.5) | 78.4% (swarm) | 90.6% (GLM-4.5 web) |
| Cost model | $1/hr at 100 tok/s (M2.5) | 76% cheaper than Opus 4.5 | Open-weight (self-host) |

---

## 2. MiniMax M2 -- Interleaved Thinking

### 2.1 Core Concept: Interleaved Thinking

Standard chain-of-thought (CoT) front-loads all reasoning before action. MiniMax
M2 interleaves reasoning tokens between tool calls: **plan -> act -> reflect**,
carrying accumulated state across turns.

| Pattern | Standard CoT | Interleaved Thinking |
|---------|-------------|---------------------|
| Sequence | think...think...think -> act | think -> act -> think -> act -> think |
| State | Discarded between turns | Preserved across all turns |
| Failure mode | Must re-derive context each turn | Accumulated understanding compounds |
| Wrapping | N/A | `<think>...</think>` tags in output |

**Critical requirement**: The entire `response_message` including `reasoning_details`
MUST be preserved in conversation history. Dropping thinking state causes:
- State drift (cumulative understanding breaks down)
- Self-correction weakens
- Planning degrades

**Benchmark impact of preserving thinking state:**

| Benchmark | With state | Without state | Delta |
|-----------|-----------|---------------|-------|
| SWE-Bench Verified | 69.4% | 67.2% | +3.3% |
| Tau-2 | 87 | 64 | +35.9% |
| BrowseComp | 44.0% | 31.4% | +40.1% |
| GAIA | 75.7% | 67.9% | +11.5% |
| xBench | 72.0% | 66.0% | +9.1% |

The BrowseComp +40% delta demonstrates interleaved thinking is disproportionately
valuable for multi-step agentic tasks over single-turn reasoning.

### 2.2 API Integration

Two SDK formats for thinking content:

| SDK | Format | How thinking appears |
|-----|--------|---------------------|
| Anthropic SDK | Content block `type: "thinking"` | Separate block in `response.content` list |
| OpenAI SDK | `<think>` tags in content string | Inline, parse manually |
| OpenAI SDK + split | `extra_body={"reasoning_split": True}` | Separate `reasoning_details` field |

### 2.3 CISPO Training Method

**CISPO = Clipped IS-weight Policy Optimization**

A reinforcement learning algorithm replacing PPO/GRPO for training agentic models.

| Dimension | PPO/GRPO | CISPO |
|-----------|----------|-------|
| What gets clipped | Individual token probabilities | Importance sampling weights (whole-sequence) |
| Gradient coverage | Low-probability tokens get zero gradient | ALL tokens contribute to gradients |
| Stability | Unstable on long structured output | Stable on code generation + tool chains |
| Speed | Baseline | 2x faster than DAPO |
| Quality | Baseline | Matches DAPO at 50% training steps |

CISPO is critical for MoE training stability. MiniMax continued using CISPO through
M2.1 and M2.5 releases.

**M2.1 enhancements**: Added multiple importance sampling (MIS) and PPO-based
trajectory filtering to handle external environment noise from tool call results.
This filters anomalous long-tail statistics caused by unpredictable tool outputs.

**FP32 precision fix**: A non-obvious discovery -- the prediction layer (LLM head)
must run at FP32 precision. Lower precision causes training-inference inconsistency,
preventing sustained reward gains during RL.

### 2.4 WebExplorer Framework

A two-phase synthetic data pipeline for training web agents:

| Phase | What happens | Output |
|-------|-------------|--------|
| Exploration | Agents freely browse the web, constructing information-rich seed questions | Seed question bank |
| Evolution | Iterative complexity increases via removal, obfuscation, substitution | Complex queries (7.9 -> 9.9 avg reasoning turns) |

WebExplorer is combined with a Playwright-based browser tool suite for evaluation.
Used for BrowseComp and GAIA benchmarks. The same framework is used in M2.5 with
context management improvements achieving 76.3% BrowseComp.

### 2.5 Post-Training Data Categories

| Category | Method | Source |
|----------|--------|--------|
| SWE Scaling | Real-data-driven | GitHub PRs -> Docker environments -> verifiable tasks |
| AppDev | Expert-driven | Full-stack dev with expert-in-the-loop rubric rewards |
| WebExplorer | Synthetic | Long-horizon web search with evolved complexity |

### 2.6 Unique Vocabulary

| Term | Definition | Western equivalent |
|------|-----------|-------------------|
| **Interleaved Thinking** | CoT woven between tool calls, state preserved | No direct equivalent (closest: ReAct, but ReAct discards state) |
| **CISPO** | RL algorithm clipping IS-weights not tokens | Alternative to PPO/GRPO (no Western adoption yet) |
| **State drift** | Degradation from dropping prior reasoning context | Context window fragmentation |
| **Reasoning snapshots** | Explainable checkpoints within problem-solving | N/A |
| **WebExplorer** | Synthetic web-agent training data pipeline | No direct equivalent |
| **Forge** | MiniMax internal RL framework for arbitrary agent scaffolds | N/A (proprietary) |
| **Agent-as-a-Verifier** | Using agent execution for dynamic verification vs static LLM judge | N/A |
| **Multi-scaffold training** | Training across different context management patterns | N/A |
| **Office Skills** | Standardized tool modules for Word/PPT/Excel loaded by file type | N/A |

---

## 3. Kimi K2.5 -- Long-Chain Tool Calling + Agent Swarm

### 3.1 Core Concept: 300-Step Tool Chains

Most Western models degrade after 30-50 sequential tool calls. Kimi K2.5
maintains stable execution across 200-300 sequential tool calls without drift.

The model executes dynamic cycles:
```
think -> search -> browser -> think -> code -> think -> verify -> ...
```

Each cycle generates and refines hypotheses, verifies evidence, and constructs
coherent answers. This interleaved reasoning decomposes ambiguous, open-ended
problems into clear, actionable subtasks across hundreds of steps.

### 3.2 Agent Swarm Architecture

| Component | Specification |
|-----------|--------------|
| Max sub-agents | 100 dynamically instantiated |
| Orchestrator steps | 15 max |
| Sub-agent steps | 100 max each |
| Parallelization gain | 4.5x execution time reduction |
| BrowseComp lift | 60.6% -> 78.4% (+29% from parallelization alone) |

The orchestrator dynamically spawns specialized sub-agents (e.g., AI Researcher,
Physics Researcher, Fact Checker) based on task requirements -- NOT predefined types.
This is self-directed, coordinated swarm-like execution.

### 3.3 PARL Training Technique

**PARL = Parallel-Agent Reinforcement Learning**

A novel RL method for training concurrent multi-agent orchestration:

| Training phase | Reward signal | Purpose |
|---------------|---------------|---------|
| Early | Reward parallel execution | Prevent serial collapse |
| Late | 80% completion quality + 20% critical path efficiency | Prevent artificial task splitting |

**Critical steps metric**: Measures the slowest sub-agent per stage, mirroring
critical path analysis from project management. This prevents the swarm from
splitting tasks without actual performance benefit.

### 3.4 OK Computer -- Virtual Computer Agent Mode

Launched September 2025. Transforms Kimi from chatbot into autonomous agent with
its own virtual computer.

| Capability | Detail |
|-----------|--------|
| Tools | 20+ integrated: file system, browser, terminal, code interpreter, image/audio gen |
| Model | Powered by K2 Turbo |
| Training | End-to-end RL (native agent, not prompt-based) |
| Execution | Dozens of reasoning cycles + tool calls per task |
| Deliverables | Websites, web apps, presentations, data visualizations |
| Pricing | Free (up to 3 requests, grayscale testing) |

**Key distinction from Western agents**: OK Computer is NOT a wrapper/scaffold
around an LLM. The model IS the agent, trained end-to-end via RL to use tools
natively. Western agents (LangChain, CrewAI) are prompt-engineered scaffolds
around base models.

### 3.5 Four Operating Modes

| Mode | Behavior | Tool budget |
|------|----------|-------------|
| Instant | Fast response, no reasoning | Minimal |
| Thinking | Extended CoT, temp=0.6 | Moderate |
| Agent | Single-agent with tool access | 200-300 steps |
| Agent Swarm | Multi-agent parallel execution | 100 agents x 100 steps |

### 3.6 Unique Vocabulary

| Term | Definition | Western equivalent |
|------|-----------|-------------------|
| **Agent Swarm** | Dynamic multi-agent parallel decomposition | Closest: AutoGen/CrewAI, but those are scaffolds not native |
| **PARL** | Parallel-Agent Reinforcement Learning | No equivalent (multi-agent RL for orchestration) |
| **OK Computer** | Virtual computer agent mode with native tool access | Closest: Claude computer use, but OK Computer is RL-trained |
| **Serial collapse** | Failure mode where swarm degenerates into sequential execution | N/A |
| **Critical steps metric** | Slowest sub-agent per stage (critical path) | Critical path analysis (borrowed from PM) |
| **Native agent** | Model trained end-to-end as agent, not scaffolded | N/A (Western agents are scaffolded) |
| **Kimi Code** | Open-source coding CLI tool | Equivalent: Claude Code, Gemini CLI |
| **WideSearch** | Deep search mode, 100 steps for both main and sub-agents | Deep Research (Google/OpenAI) |

---

## 4. GLM-5.1 (Z.ai / Zhipu) -- All Tools Paradigm

### 4.1 Core Concept: All Tools

Introduced in GLM-4 (2024), matured through GLM-4.5/4.6/5.1. The model
autonomously decides which tools to deploy and when, without explicit
function-calling instructions.

| Dimension | Standard function calling (OpenAI) | All Tools (GLM) |
|-----------|------------------------------------|-----------------|
| Tool selection | User provides tool list, model picks | Model autonomously determines need |
| Invocation trigger | Explicit `function_call` parameter | Thinking mode decides during generation |
| Tool tokens | Standard output tokens | Special `[tool_call]` tokens in architecture |
| Execution model | Sequential call-response | Iterative: call -> feedback -> refine -> call |

The model doesn't need to be told WHEN to call a tool. It figures that out as
part of its token generation process (thinking mode).

### 4.2 Architecture: GLM-5.1

| Component | Specification |
|-----------|--------------|
| Total parameters | 744B |
| Active per token | 40B (top-8 routing + 1 shared expert) |
| Expert count | 256 |
| Layers | 78 (3 dense + 75 sparse MoE) |
| Hidden size | 6144 |
| Attention heads | 96 |
| Attention type | Multi-head Latent Attention + DeepSeek Sparse Attention |
| Context | 200K (202,752 tokens) |
| Training data | 15T general text + 7-8T code/QA tokens |
| Inference optimization | Speculative Decoding via Multi-Token Prediction (MTP) |

### 4.3 Thinking Mode (Autonomous Tool Selection)

When `"thinking": {"type": "enabled"}` is set:
1. Model plans the solving process step by step
2. Autonomously determines if tools are needed
3. Outputs structured JSON for each tool call
4. Integrates external tool results into reasoning
5. Synthesizes final answer

This is distinct from Western "tool use" where the developer explicitly enables
and describes tools. GLM's thinking mode makes tool selection an emergent property
of the reasoning process.

### 4.4 Long-Horizon Agentic Performance

GLM-5.1 pushes sustained tool use far beyond typical Western limits:

| Metric | Value |
|--------|-------|
| VectorDBBench iterations | 655 |
| Tool functions executed | 6,000+ |
| Sustained performance after | 1,000+ tool calls |
| QPS gain (VectorDBBench) | 21,500 QPS (6x improvement) |
| KernelBench ML gain | 3.6x (vs GLM-5's 2.6x) |
| Linux desktop build | 8 hours autonomous (plan, test, debug) |

Most Western models plateau after a few dozen tool calls. GLM-5.1 maintains
improvement trajectories across hundreds of optimization rounds.

### 4.5 "Boring Magic" -- Reliability Philosophy

GLM's unique engineering philosophy for tool calling:
- Correct JSON keys every time
- Proper argument types, no hallucinated params
- Well-formed outputs, refuses unknown tools
- Zero hallucination target in tool calls

This contrasts with Western models that prioritize capability breadth over
call-by-call reliability.

### 4.6 Training Lineage

| Method | What it does |
|--------|-------------|
| AgentTuning | Custom instruction-tuning with high-quality agent-environment interaction trajectories |
| LongAlign | Proprietary long-context alignment recipe (128K-1M) |
| SFT | From authentic human prompts + interactions |
| RLHF | Addresses response rejection, safety, bilingual coherence, multi-turn stability |

**AgentTuning** is unique: it uses structured trajectory data from real agent
interactions with environments, not just conversation pairs. This trains the model
on the full cycle of plan -> tool call -> observe result -> adapt.

### 4.7 GLMs Platform (Custom Agents)

Z.ai's equivalent of GPT Builder, but with deeper functional integration:
- Users create custom agents with embedded or external tools
- Tools are first-class citizens, not add-ons
- The "All Tools" paradigm extends to user-created agents

### 4.8 Unique Vocabulary

| Term | Definition | Western equivalent |
|------|-----------|-------------------|
| **All Tools** | Model autonomously decides tool use during generation | No equivalent (Western models need explicit tool lists) |
| **Thinking Mode** | Dual-operation state: CoT reasoning + autonomous tool selection | Closest: extended thinking, but without autonomous tool trigger |
| **[tool_call] tokens** | Special tokens in architecture for tight tool coupling | Function calling tokens (but architectural, not prompt-level) |
| **Boring Magic** | Reliability-first philosophy for tool calling | N/A (Western focus is capability, not reliability) |
| **Agent Brain** | Model as autonomous orchestrator of external services | N/A |
| **AgentTuning** | SFT on agent-environment interaction trajectories | No equivalent (RLHF focuses on conversations, not tool trajectories) |
| **LongAlign** | Proprietary long-context alignment recipe | RoPE scaling / YaRN (but LongAlign is alignment, not positional encoding) |
| **GLMs** | Custom agent creation platform with deep tool integration | GPT Builder / Gems (but deeper tool integration) |

---

## 5. Cross-Framework Comparison: What's NOT in Western Models

### 5.1 Concepts With No Western Equivalent

| Concept | Origin | Why it matters |
|---------|--------|---------------|
| **Interleaved Thinking** | MiniMax M2 | State preservation across tool calls. Western ReAct discards reasoning between steps. |
| **CISPO** | MiniMax | RL that clips IS-weights not tokens. Enables stable MoE training for agentic models. |
| **Agent Swarm (native)** | Kimi K2.5 | RL-trained multi-agent orchestration. Western swarms are scaffolded (CrewAI, AutoGen). |
| **PARL** | Kimi K2.5 | RL specifically for training parallel agent coordination. No Western research equivalent. |
| **OK Computer** | Kimi | Model-as-agent with virtual computer. Western agents are scaffolds around models. |
| **All Tools** | GLM-4/5.1 | Autonomous tool selection during generation. Western models require explicit tool lists. |
| **[tool_call] tokens** | GLM-4.6 | Architectural-level tool integration. Western tool calling is prompt-level. |
| **AgentTuning** | GLM-4 | SFT on agent-environment trajectories. Western RLHF trains on conversations. |
| **300-step chains** | Kimi K2 | Stable execution across 200-300 tool calls. Western models degrade after 30-50. |
| **6000+ tool calls** | GLM-5.1 | Sustained improvement across thousands of iterations. No Western equivalent tested. |

### 5.2 Thinking Mode Integration Spectrum

| Model | Thinking integration | Tool trigger |
|-------|---------------------|-------------|
| OpenAI o3 | Think first, act after | Explicit function_call parameter |
| Anthropic Claude | Extended thinking block, then response | Tool use blocks in response |
| Google Gemini | Think then act | Function declarations in config |
| MiniMax M2 | **Interleaved** (think-act-think-act) | Standard function calling |
| Kimi K2.5 | **Interleaved** (think-search-think-code) | Native agent training |
| GLM-5.1 | **Autonomous** (thinking mode decides) | `[tool_call]` tokens emerge from generation |

### 5.3 Training Method Comparison

| Method | Model | What's different |
|--------|-------|-----------------|
| RLHF/DPO | Western standard | Trains on conversation preference pairs |
| CISPO | MiniMax | Clips IS-weights, not tokens. 2x faster. |
| PARL | Kimi | Multi-agent parallel RL. Prevents serial collapse. |
| AgentTuning | GLM | SFT on agent-environment trajectories, not conversations |
| WebExplorer | MiniMax | Synthetic complexity evolution for web search training |

### 5.4 Scale of Tool Use

| Model | Max sequential tool calls | Max parallel agents | Sustained iterations |
|-------|--------------------------|--------------------|--------------------|
| Claude (Anthropic) | ~20-50 (practical limit) | 1 (MCP-based) | Limited |
| GPT-4 (OpenAI) | ~20-30 (practical limit) | 1 (parallel function calls) | Limited |
| MiniMax M2.5 | 100 (WebExplorer scaffold) | 1 | Hundreds |
| Kimi K2.5 | 200-300 | 100 (Agent Swarm) | 1,500 total via swarm |
| GLM-5.1 | 1,000+ | 1 (autonomous) | 6,000+ tool functions |

---

## 6. Implications for CEX Architecture

### 6.1 Interleaved Thinking (MiniMax)

CEX's 8F pipeline runs F1-F8 sequentially. Interleaved thinking suggests a
revision where reasoning (F4) re-enters after each tool call (F5), not just once.
Pattern: F1 -> F2 -> F3 -> F4 -> F5 -> **F4b** -> F5b -> **F4c** -> F6 -> F7 -> F8.

### 6.2 Agent Swarm (Kimi)

CEX's grid dispatch is a static wave model. Kimi's Agent Swarm uses dynamic
instantiation based on task analysis. Potential: N07 could dynamically create
sub-agent types per task rather than routing to fixed N01-N06 nuclei.

### 6.3 All Tools (GLM)

CEX requires explicit tool specification in handoffs. GLM's All Tools approach
suggests nuclei could autonomously discover and invoke tools based on task context,
reducing handoff verbosity.

### 6.4 300-Step Chains (Kimi)

Current CEX dispatches are shallow (3-10 tool calls typical). Kimi demonstrates
stable 200-300 step execution is achievable with proper training. This validates
the dispatch-depth rule's push for deeper nucleus utilization.

### 6.5 CISPO for Local Models

If CEX ever fine-tunes local models (Ollama), CISPO's 2x training speed advantage
over DAPO makes it the preferred RL algorithm for agentic fine-tuning.

---

## 7. Key Benchmarks (Side-by-Side)

| Benchmark | MiniMax M2.5 | Kimi K2.5 | GLM-5.1 | Claude Opus 4.6 | GPT-5.4 |
|-----------|-------------|-----------|---------|----------------|---------|
| SWE-Bench Verified | 80.2% | 76.8% | -- | -- | -- |
| SWE-Bench Pro | -- | -- | 58.4% | 57.3% | 57.7% |
| AIME 2025 | -- | 96.1% | 95.3% | -- | 98.7% |
| GPQA Diamond | -- | 87.6% | 86.2% | -- | 94.3% |
| BrowseComp | 76.3% | 78.4% (swarm) | 90.6% (GLM-4.5) | -- | -- |
| KernelBench | -- | -- | 3.6x gain | -- | -- |
| Tau-2 | 87 | -- | -- | -- | -- |

---

## 8. Complete Vocabulary Registry

### 8.1 MiniMax Vocabulary

| Term | Category | Definition |
|------|----------|-----------|
| Interleaved Thinking | Reasoning | CoT tokens woven between tool calls with state preservation |
| CISPO | Training | Clipped IS-weight Policy Optimization -- RL clipping sequences not tokens |
| State drift | Failure mode | Degradation from dropping prior reasoning context between turns |
| Reasoning snapshots | Observability | Explainable checkpoints within multi-step problem-solving |
| WebExplorer | Data pipeline | Synthetic web-search training via exploration + complexity evolution |
| Forge | Infrastructure | Internal RL framework supporting arbitrary agent scaffolds |
| Agent-as-a-Verifier | Evaluation | Dynamic verification via agent execution vs static LLM judgment |
| Multi-scaffold training | Training | Training across different context management and execution patterns |
| Office Skills | Product | Standardized tool modules for office formats, loaded by file type |
| MIS | Training | Multiple Importance Sampling for handling tool-call noise |
| reasoning_split | API | Parameter to separate thinking into dedicated field vs inline tags |

### 8.2 Kimi Vocabulary

| Term | Category | Definition |
|------|----------|-----------|
| Agent Swarm | Architecture | Dynamic multi-agent parallel decomposition with up to 100 sub-agents |
| PARL | Training | Parallel-Agent Reinforcement Learning for concurrent orchestration |
| OK Computer | Product | Virtual computer agent mode with 20+ native tools |
| Serial collapse | Failure mode | Swarm degenerating into sequential single-agent execution |
| Critical steps metric | Evaluation | Slowest sub-agent per stage, borrowed from critical path analysis |
| Native agent | Architecture | Model trained end-to-end as agent (not scaffolded around base model) |
| WideSearch | Feature | Deep search mode allowing 100 steps for main + sub-agents |
| Kimi Code | Product | Open-source coding CLI (equivalent to Claude Code) |
| Vision-grounded coding | Capability | Generating code from UI designs and video workflows |

### 8.3 GLM / Z.ai Vocabulary

| Term | Category | Definition |
|------|----------|-----------|
| All Tools | Paradigm | Model autonomously decides tool use during generation without explicit lists |
| Thinking Mode | Architecture | Dual-operation state enabling CoT + autonomous tool selection |
| [tool_call] tokens | Architecture | Special tokens for architectural-level tool coupling |
| Boring Magic | Philosophy | Reliability-first approach: correct JSON, proper types, zero hallucination |
| Agent Brain | Architecture | Model as autonomous orchestrator of external services |
| AgentTuning | Training | SFT on structured agent-environment interaction trajectories |
| LongAlign | Training | Proprietary long-context alignment recipe for 128K-1M tokens |
| GLMs | Product | Custom agent creation platform with deep tool integration |
| Speculative Decoding / MTP | Inference | Multi-token prediction head for parallel token generation |
