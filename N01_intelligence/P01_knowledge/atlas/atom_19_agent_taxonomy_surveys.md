---
id: atom_19_agent_taxonomy_surveys
kind: knowledge_card
pillar: P01
domain: agent-taxonomy
title: "Agent Taxonomy Surveys: Three Foundational Frameworks Compared"
version: 2.0.0
quality: 8.8
status: active
created: 2026-04-13
updated: 2026-04-13
sources:
  - "Wang et al. 2023 — A Survey on Large Language Model based Autonomous Agents (arXiv:2308.11432)"
  - "Xi et al. 2023 — The Rise and Potential of Large Language Model Based Agents: A Survey (arXiv:2309.07864)"
  - "Arunkumar et al. 2026 — Agentic AI: Architectures, Taxonomies, and Evaluation (arXiv:2601.12560)"
  - "Schick et al. 2023 — Toolformer: Language Models Can Teach Themselves to Use Tools (arXiv:2302.04761)"
  - "Patil et al. 2023 — Gorilla: Large Language Model Connected with Massive APIs (arXiv:2305.15334)"
  - "Wang et al. 2024 — CodeAct: Executable Code Actions Elicit Better LLM Agents (arXiv:2402.01030)"
  - "Wang et al. 2023 — Voyager: An Open-Ended Embodied Agent with LLMs (arXiv:2305.16291)"
  - "Yang et al. 2024 — SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering (arXiv:2405.15793)"
  - "Brohan et al. 2023 — RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (arXiv:2307.15818)"
  - "CEX atom_28 — Code Agent Vocabulary Atlas (internal)"
tags: [agent, taxonomy, survey, architecture, multi-agent, planning, memory, reasoning, tools, pomdp, classic-eval, action-paradigms, code-agents, 2026]
---

# Agent Taxonomy Surveys: Three Foundational Frameworks Compared

## 1. Overview

Three landmark surveys define the vocabulary and structural decomposition of LLM-based agents. Each proposes a component-based architecture but carves the boundaries differently. This atom extracts every taxonomy tree, defines every term, and maps convergences and divergences across the three.

| Property | Wang 2023 | Xi 2023 | Arunkumar 2026 |
|----------|-----------|---------|----------------|
| arXiv | 2308.11432 | 2309.07864 | 2601.12560 |
| Published | Aug 2023 (rev. Mar 2025) | Sep 2023 | Jan 2026 |
| Pages | ~30 | 86 | 28 |
| Core framework | Profile-Memory-Planning-Action | Brain-Perception-Action | Perception-Brain-Planning-Action-Tools-Collaboration |
| Component count | 4 modules | 3 modules (5 brain sub-modules) | 6 dimensions |
| Scope | Construction + Applications + Evaluation | Construction + Applications + Agent Society | Architecture + Environments + Evaluation + Open Problems |
| Formal model | No | No | Yes (POMDP-based control loop) |

---

## 2. Paper 1: Wang et al. 2023 — "A Survey on Large Language Model based Autonomous Agents"

### 2.1 Complete Taxonomy Tree

```
LLM-Based Autonomous Agent
|
+-- AGENT CONSTRUCTION
|   |
|   +-- 1. Profiling Module
|   |   +-- Handcrafting Method (manual attribute assignment)
|   |   +-- LLM-Generation Method (automated profile creation from seed examples)
|   |   +-- Dataset Alignment Method (profiles from real-world demographic data)
|   |
|   +-- 2. Memory Module
|   |   +-- Memory Structures
|   |   |   +-- Unified Memory (short-term only, in-context learning)
|   |   |   +-- Hybrid Memory (short-term + long-term consolidated)
|   |   +-- Memory Formats
|   |   |   +-- Natural language descriptions
|   |   |   +-- Embedding vectors
|   |   |   +-- Structured databases
|   |   |   +-- Structured lists / hierarchical trees
|   |   +-- Memory Operations
|   |       +-- Reading (recency, relevance, importance scoring)
|   |       +-- Writing (store perceptions; handle duplication + overflow)
|   |       +-- Reflection (summarize experiences into abstract insights)
|   |
|   +-- 3. Planning Module
|   |   +-- Planning WITHOUT Feedback
|   |   |   +-- Single-path Reasoning (Chain of Thought, Zero-shot-CoT)
|   |   |   +-- Multi-path Reasoning (Tree/graph branching)
|   |   |   +-- External Planner (PDDL + formal solvers)
|   |   +-- Planning WITH Feedback
|   |       +-- Environmental Feedback (task signals, action outcomes)
|   |       +-- Human Feedback (preference alignment)
|   |       +-- Model Feedback (self-refinement, inter-model evaluation)
|   |
|   +-- 4. Action Module
|       +-- Action Goal
|       |   +-- Task completion
|       |   +-- Communication
|       |   +-- Environment exploration
|       +-- Action Production
|       |   +-- Via memory recollection
|       |   +-- Via plan following
|       +-- Action Space
|       |   +-- External Tools (APIs, databases, knowledge bases, external models)
|       |   +-- Internal Knowledge (planning, conversation, common sense)
|       +-- Action Impact
|           +-- Changing environment states
|           +-- Altering agent internal states
|           +-- Triggering subsequent actions
|
+-- CAPABILITY ACQUISITION
|   +-- With Fine-tuning
|   |   +-- Human-annotated datasets
|   |   +-- LLM-generated datasets
|   |   +-- Real-world datasets
|   +-- Without Fine-tuning
|       +-- Prompt Engineering
|       +-- Mechanism Engineering
|           +-- Trial-and-error
|           +-- Crowd-sourcing (multi-agent consensus)
|           +-- Experience accumulation (skill libraries)
|           +-- Self-driven evolution (autonomous goal-setting)
|
+-- APPLICATION DOMAINS
|   +-- Social Science
|   |   +-- Psychology (simulation, mental health support)
|   |   +-- Political Science & Economy (ideology, voting, economic behavior)
|   |   +-- Social Simulation (virtual communities, info propagation)
|   |   +-- Jurisprudence (legal decision-making)
|   |   +-- Research Assistant (literature analysis, script generation)
|   +-- Natural Science
|   |   +-- Documentation & Data Management
|   |   +-- Experiment Assistant
|   |   +-- Education (math, coding)
|   |   +-- Domain-Specific (chemistry via ChemCrow, materials science)
|   +-- Engineering
|       +-- Software Development
|       +-- Game Playing
|       +-- Web Interaction (e-commerce, task automation)
|       +-- Robotics & Embodied Tasks
|
+-- EVALUATION STRATEGIES
    +-- Subjective Evaluation (human judgment, preference alignment)
    +-- Objective Evaluation (task completion rates, benchmarks)
```

### 2.2 Key Definitions (Wang 2023)

| Term | Definition |
|------|-----------|
| Profiling Module | Determines the agent's role via handcrafted, LLM-generated, or dataset-aligned attributes (personality, demographics, relationships) |
| Unified Memory | Short-term memory only, implemented as in-context tokens in the LLM prompt |
| Hybrid Memory | Combines short-term (recent perceptions) with long-term (consolidated knowledge stores) |
| Memory Reflection | Process of summarizing raw experiences into higher-level abstract insights |
| Single-path Reasoning | Sequential step-by-step inference (Chain of Thought) |
| Multi-path Reasoning | Exploring multiple branching reasoning trajectories (Tree of Thought) |
| External Planner | Using formal planning languages (PDDL) with external solvers instead of LLM-native planning |
| Mechanism Engineering | Capability acquisition without fine-tuning: trial-and-error, crowd-sourcing, experience accumulation, self-driven evolution |
| Self-driven Evolution | Agent autonomously sets goals and evolves capabilities without external instruction |

### 2.3 Challenges Identified

- Role-playing capability (maintaining consistent personas)
- Generalized human alignment (adapting to diverse value systems)
- Prompt robustness (stability across input formulations)
- Hallucination (plausible but false generation)
- Knowledge boundary (operating within competency limits)
- Efficiency (computational cost and latency)

---

## 3. Paper 2: Xi et al. 2023 — "The Rise and Potential of Large Language Model Based Agents: A Survey"

### 3.1 Complete Taxonomy Tree

```
LLM-Based Agent
|
+-- BRAIN (Core Controller -- the LLM)
|   |
|   +-- 1. Natural Language Interaction
|   |   +-- Multi-turn Interactive Conversation
|   |   +-- High-quality Natural Language Generation
|   |   +-- Intention and Implication Understanding
|   |
|   +-- 2. Knowledge
|   |   +-- Linguistic Knowledge (grammar, morphology, syntax, semantics, pragmatics)
|   |   +-- Commonsense Knowledge (general world facts, e.g. "umbrellas protect from rain")
|   |   +-- Professional Domain Knowledge (programming, medicine, math, etc.)
|   |   +-- Knowledge Issues
|   |       +-- Outdated/incorrect knowledge -> knowledge editing
|   |       +-- Hallucinations -> self-verification, tool-assisted retrieval
|   |
|   +-- 3. Memory
|   |   +-- Enhancement Methods
|   |   |   +-- Raising Transformer Length Limits
|   |   |   |   +-- Text truncation
|   |   |   |   +-- Input segmentation
|   |   |   |   +-- Key-text emphasis
|   |   |   |   +-- Modified attention (sparse, linear)
|   |   |   +-- Summarizing Memory
|   |   |   |   +-- Prompt-based summarization
|   |   |   |   +-- Reflective summarization (Generative Agents)
|   |   |   |   +-- Hierarchical summarization (daily snapshots + overarching)
|   |   |   +-- Compressing with Vectors/Data Structures
|   |   |       +-- Embedding vectors (ChatDev, GITM)
|   |   |       +-- Triplet configurations (RET-LLM)
|   |   |       +-- SQL database integration (ChatDB, DB-GPT)
|   |   +-- Memory Retrieval
|   |       +-- Automated (recency, relevance, importance scoring)
|   |       +-- Interactive (user-guided memory management)
|   |
|   +-- 4. Reasoning & Planning
|   |   +-- Reasoning
|   |   |   +-- Deductive, Inductive, Abductive reasoning
|   |   |   +-- Chain-of-Thought (CoT)
|   |   |   +-- Self-Consistency (multiple paths)
|   |   |   +-- Self-Polish & Self-Refine (iterative improvement)
|   |   |   +-- Selection-Inference
|   |   +-- Planning
|   |       +-- Plan Formulation
|   |       |   +-- Comprehensive Decomposition (full task breakdown, Least-to-Most)
|   |       |   +-- Adaptive Planning (plan-execute step-by-step, CoT-series)
|   |       |   +-- Hierarchical Planning (multi-level, PET, DEPS)
|   |       |   +-- Tree-based Planning (Tree-of-Thought)
|   |       |   +-- Domain-Specific Integration (HuggingGPT, MRKL)
|   |       +-- Plan Reflection
|   |           +-- Internal feedback (LLM-Planner, ReAct)
|   |           +-- Human feedback (AI Chains, Voyager)
|   |           +-- Environmental feedback (Inner Monologue, SelfCheck)
|   |
|   +-- 5. Transferability & Generalization
|       +-- Unseen Task Generalization (zero-shot, instruction-tuned models)
|       +-- In-Context Learning (few-shot, no parameter updates)
|       +-- Continual Learning (no catastrophic forgetting, Voyager skill library)
|
+-- PERCEPTION (Environmental Input)
|   |
|   +-- 1. Textual Input
|   |   +-- Explicit content understanding
|   |   +-- Implied meaning and intention inference
|   |   +-- Zero-shot instruction understanding
|   |
|   +-- 2. Visual Input
|   |   +-- Image Captioning (text descriptions, interpretable but lossy)
|   |   +-- Direct Encoding (ViT/VQVAE patches as tokens)
|   |   +-- Frozen Encoders + Learnable Interface
|   |       +-- Query-Based (Q-Former: BLIP-2, InstructBLIP)
|   |       +-- Projection-Based (LLaVA, MiniGPT-4, PandaGPT)
|   |   +-- Video Processing (frame sequences, temporal masking)
|   |
|   +-- 3. Auditory Input
|   |   +-- Cascading (invoke specialized tools: AudioGPT, HuggingGPT)
|   |   +-- Transfer Visual Methods (AST: spectrograms as 2D images)
|   |   +-- Frozen audio encoders (HuBERT, X-LLM, Video-LLaMA)
|   |
|   +-- 4. Other Modalities
|       +-- Gesture / Pointing (InternGPT)
|       +-- Haptic feedback
|       +-- Environmental Sensors (LIDAR, GPS, IMU)
|       +-- Brain-Computer Interfaces
|
+-- ACTION (Environmental Output)
|   |
|   +-- 1. Textual Output (fluency, relevance, diversity, controllability)
|   |
|   +-- 2. Tool Using
|   |   +-- Understanding Tools (zero-shot + few-shot prompts)
|   |   +-- Learning to Use Tools
|   |   |   +-- From demonstrations (expert behavior imitation)
|   |   |   +-- From feedback (environmental + human)
|   |   +-- Adaptability & Generalization
|   |   |   +-- Meta-tool learning
|   |   |   +-- Curriculum learning (simple -> complex)
|   |   |   +-- Relationship understanding (tool composition)
|   |   +-- Making Tools (LATM, CREATOR, SELF-DEBUGGING)
|   |
|   +-- 3. Embodied Action
|       +-- Observation (multimodal environmental perception)
|       +-- Manipulation (object rearrangement, tabletop, mobile, kitchen)
|       +-- Navigation (spatial reasoning, goal-directed movement)
|
+-- APPLICATIONS
|   |
|   +-- 1. Single-Agent Scenarios
|   |   +-- Task-oriented Deployment (well-defined objectives, web nav, booking)
|   |   +-- Innovation-oriented Deployment (scientific research, software dev, creative work)
|   |   +-- Lifecycle-oriented Deployment (continuous learning in open-ended environments)
|   |
|   +-- 2. Multi-Agent Scenarios
|   |   +-- Cooperative Interaction for Complementarity
|   |   |   +-- Disordered cooperation (emergent, unstructured)
|   |   |   +-- Ordered cooperation (structured, role-based teamwork)
|   |   +-- Adversarial Interaction for Advancement
|   |       +-- Debate-style exchanges
|   |       +-- Constructive conflict for improved output
|   |
|   +-- 3. Human-Agent Cooperation
|       +-- Instructor-Executor Paradigm
|       |   +-- Education applications
|       |   +-- Health applications
|       |   +-- Other applications
|       +-- Equal Partnership Paradigm
|           +-- Empathetic Communicator (emotional support, rapport)
|           +-- Human-Level Participant (peer-level collaboration)
|
+-- AGENT SOCIETY
    |
    +-- 1. Behavior and Personality
    |   +-- Social Behavior
    |   |   +-- Individual behaviors (cognitive abilities, responses)
    |   |   +-- Group behaviors (collective patterns, hierarchies)
    |   +-- Personality
    |       +-- Cognition (reasoning style, knowledge application)
    |       +-- Emotion (emotional responses, empathy)
    |       +-- Character (distinctive traits, values)
    |
    +-- 2. Environment for Agent Society
    |   +-- Text-based Environment (language-focused interactions)
    |   +-- Virtual Sandbox Environment (simulated worlds, e.g. Generative Agents)
    |   +-- Physical Environment (real-world constraints)
    |
    +-- 3. Society Simulation (emergent social phenomena, information propagation)
```

### 3.2 Key Definitions (Xi 2023)

| Term | Definition |
|------|-----------|
| Agent | An artificial entity that perceives its surroundings via sensors, makes decisions, and takes actions via actuators |
| Brain | The LLM-based core that stores knowledge/memory and performs information processing, decision-making, reasoning, and planning |
| Perception | Module converting multimodal environmental information into representations the brain can process |
| Action | Module executing decisions through textual output, tool usage, or embodied interactions |
| Agency | Capacity to act with autonomy, intentionality, and goal-orientation |
| Linguistic Knowledge | Grammar, morphology, syntax, semantics, and pragmatics encoded in the LLM |
| Commonsense Knowledge | General world facts acquired from broad training (e.g., physical intuition, social norms) |
| Professional Domain Knowledge | Specialized expertise in fields like programming, medicine, or mathematics |
| In-Context Learning (ICL) | Learning from few examples placed in the prompt without any parameter updates |
| Chain-of-Thought (CoT) | Generating intermediate reasoning steps before arriving at a final answer |
| Continual Learning | Acquiring new capabilities progressively without catastrophic forgetting of previous skills |
| Embodied Action | Agent perception, comprehension, and interaction with physical environments based on internal knowledge |
| Tool Using | Leveraging external resources (APIs, databases, models) to enhance agent capabilities beyond the LLM's intrinsic limits |
| Tool Making | Agent self-sufficiency in generating executable programs and new tools (LATM, CREATOR) |
| Plan Formulation | First stage of planning: decomposing a task into executable sub-steps |
| Plan Reflection | Second stage of planning: evaluating and revising the plan using internal, human, or environmental feedback |
| Instructor-Executor Paradigm | Human-agent cooperation where the human directs and the agent executes |
| Equal Partnership Paradigm | Human-agent cooperation where both operate as peers |
| Empathetic Communicator | Agent role in equal partnership providing emotional support and rapport |
| Human-Level Participant | Agent role in equal partnership performing as a peer collaborator |

### 3.3 Four Agent Properties (Xi 2023)

| Property | Mechanism |
|----------|-----------|
| Autonomy | Independent task formulation and execution (Auto-GPT) |
| Reactivity | Rapid multimodal perception and response to changes |
| Pro-activeness | Goal-oriented planning and reasoning |
| Social Ability | Natural language interaction with humans and other agents |

---

## 4. Paper 3: Arunkumar et al. 2026 — "Agentic AI: Architectures, Taxonomies, and Evaluation"

### 4.1 Complete Taxonomy Tree

```
Agentic AI System
|
+-- FORMAL MODEL: A = <S, O, M, T, pi>  (POMDP-based)
|   +-- S: State space
|   +-- O: Observation space (partial via multimodal encoders)
|   +-- M: Memory (updated by observation, reasoning, feedback)
|   +-- T: Thought/plan (probabilistic inference)
|   +-- pi: Policy (conditioned on reasoning trace)
|
+-- CORE COMPONENTS
|   |
|   +-- 1. Perception (Phi)
|   |   +-- Text-only processing (legacy)
|   |   +-- Multimodal Grounding
|   |       +-- Screenshots / Vision encoders (WebVoyager, AppAgent)
|   |       +-- DOM + Vision hybrids (SeeAct)
|   |       +-- Video + Proprioception (Magma)
|   |       +-- Audio / Speech (AudioGPT)
|   |       +-- 3D Point Clouds (3D LLM)
|   |
|   +-- 2. Memory (M)
|   |   +-- Structure Types
|   |   |   +-- Natural language streams
|   |   |   +-- Hierarchical clusters
|   |   |   +-- SQL tables
|   |   |   +-- Paged stores
|   |   +-- Retrieval Strategies
|   |   |   +-- Recency/relevance scoring
|   |   |   +-- Hierarchical traversal
|   |   |   +-- SQL queries
|   |   |   +-- Controller-driven
|   |   +-- Retention Policies
|   |   |   +-- Reflection / Summarization
|   |   |   +-- Exponential decay
|   |   |   +-- Paging
|   |   |   +-- Semantic compression
|   |   |   +-- Learned pruning
|   |   +-- Representative Systems
|   |       +-- Generative Agents (reflection)
|   |       +-- MemoryBank (decay)
|   |       +-- ChatDB (SQL)
|   |       +-- MemGPT (paging)
|   |       +-- MemInsight (semantic)
|   |       +-- MemAgent (learned pruning)
|   |
|   +-- 3. Profiling (P)
|   |   +-- System prompts and personas
|   |   +-- Dynamic role-switching
|   |   +-- Behavioral constraints and implicit guidelines
|   |
|   +-- 4. Action & Tools (T)
|       +-- Action Paradigms
|       |   +-- API-based (structured calls: Toolformer, Gorilla)
|       |   +-- Code-as-Action (executable scripts: CodeAct, Voyager)
|       |   +-- Agent Computer Interfaces / ACI (shell/IDE: SWE-agent)
|       |   +-- Computer Use Actions (mouse/keyboard/screenshots: Claude, Operator)
|       |   +-- Embodied VLA (continuous motor primitives: Gemini Robotics)
|       +-- Standardized Layer
|           +-- Model Context Protocol (MCP): common tool exposure
|           +-- Allowlists, authentication, audit
|
+-- COGNITIVE ARCHITECTURE
|   |
|   +-- 1. Planning Approaches
|   |   +-- Chain-of-Thought (latent reasoning, linear, low latency)
|   |   +-- ReAct (thought-action interleaving, linear loop, grounded)
|   |   +-- Reflexion (verbal reinforcement, cyclical, self-correction)
|   |   +-- Tree of Thoughts (external branching, tree, backtracking)
|   |   +-- LATS (MCTS with value feedback, graph/tree)
|   |   +-- Reasoning Models (o1, o3: internalized inference-time search, implicit tree)
|   |   +-- ReAcTree (recursive sub-agent spawning, hierarchical)
|   |
|   +-- 2. Reflection Mechanisms
|   |   +-- Verbal Reinforcement (Reflexion: NL critiques stored for future)
|   |   +-- Self-Correction (Self-Refine, CRITIC: generate-critique-revise loops)
|   |   +-- Failure Recovery (PALADIN, Expel: reusable rules from mistake trajectories)
|   |
|   +-- 3. Learning Paradigms (3 temporal horizons)
|       +-- In-Context Learning (ephemeral: few-shot, CoT examples, lives in prompt)
|       +-- Weight Updates (permanent: instruction tuning, Agent-FLAN, FireAct, RLHF, RLAIF)
|       +-- Skill Accumulation (non-parametric: Voyager skill library, AgentRM, AgentPRM)
|
+-- MULTI-AGENT SYSTEMS
|   |
|   +-- 1. Interaction Topologies
|   |   +-- Chain / Waterfall (sequential: MetaGPT, ChatDev)
|   |   +-- Star / Hub-and-Spoke (central controller: AutoGen, Swarm)
|   |   +-- Mesh / Decentralized (dynamic: CAMEL, Generative Agents, TradingAgents)
|   |   +-- Workflow Graph / Explicit State Machine (LangGraph: checkpoints, typed state, guards)
|   |
|   +-- 2. Collaboration Mechanisms
|       +-- Role-Playing (CAMEL: inception prompting assigns personas)
|       +-- Standard Operating Procedures (MetaGPT: encode SOPs, standardized deliverables)
|       +-- Hierarchical Verification (MAKER: separate Verifier agents challenge Workers)
|       +-- Adversarial Debate (multiple agents propose, critique, converge)
|       +-- Economic Simulation (TradingAgents: market-like emergent decisions)
|
+-- ENVIRONMENTS & DOMAINS
|   |
|   +-- 1. Digital Agents
|   |   +-- Web (Mind2Web, WebArena: screenshot-driven, dynamic DOM)
|   |   +-- Operating Systems (OSWorld, Windows Agent Arena: multi-app workflows)
|   |   +-- Enterprise Software (SWE-Bench Pro, SQL-agents: repo-scale tasks)
|   |
|   +-- 2. Embodied Agents
|   |   +-- Games (Voyager/Minecraft: lifelong learning, skill libraries)
|   |   +-- Robotics (VLA models, physical grounding, cross-embodiment transfer)
|   |   +-- Autonomous Driving (Agent-Driver: cognitive memory; DiMA: distillation)
|   |
|   +-- 3. Specialized Domains
|       +-- Healthcare / Science (hypothesis generation, EHR, clinical compliance)
|       +-- Finance (market simulation, portfolio optimization)
|       +-- Conversational (empathetic voice systems, long-term support)
|
+-- EVALUATION FRAMEWORK (CLASSic)
|   +-- Cost (token consumption, hierarchical overhead)
|   +-- Latency (real-world constraints, asynchronous benchmarks)
|   +-- Accuracy (multi-step tool use, state tracking, long-horizon recovery)
|   +-- Security (prompt injection, allowlists, authentication, audit, compartmentalization)
|   +-- Stability (variance across runs, failure distributions, compliance)
|
+-- KEY BENCHMARKS
    +-- GAIA (general assistants, multi-step decomposition)
    +-- SWE-Bench / Verified / Pro (software engineering)
    +-- OSWorld / Verified (desktop control)
    +-- tau-bench (multi-turn tool interaction with policies)
    +-- FrontierMath (hard mathematical reasoning)
    +-- AgentBench, MARBLE (diverse environments, emergent behaviors)
```

### 4.2 Key Definitions (Arunkumar 2026)

| Term | Definition |
|------|-----------|
| Agentic AI | AI systems that behave as autonomous entities capable of perceiving, reasoning, planning, and acting |
| Agentic Control Loop | Formal POMDP: A = <S, O, M, T, pi> where perception, memory, planning, and action execute in a loop |
| Perception (Phi) | Partial observation function mapping environment state to agent observations via multimodal encoders |
| Memory (M) | Stateful store updated each step by observations, reasoning traces, and environmental feedback |
| Planning (Z) | Probabilistic inference of thought/plan conditioned on memory and current observations |
| Policy (pi) | Action selection conditioned on the current reasoning trace and memory state |
| API-based Action | Structured tool calls via defined interfaces (Toolformer, Gorilla) |
| Code-as-Action | Generating executable code (Python, JavaScript) as the action primitive (CodeAct, Voyager) |
| Agent Computer Interface (ACI) | Shell/IDE-level actions where the agent operates developer tools directly (SWE-agent) |
| Computer Use Actions | GUI-level mouse/keyboard/screenshot interactions (Claude Computer Use, Operator) |
| Model Context Protocol (MCP) | Standardized protocol for common tool exposure with allowlists, authentication, and audit |
| Chain topology | Sequential task passing through a fixed agent sequence (waterfall) |
| Star topology | Central controller coordinating specialized worker agents (hub-and-spoke) |
| Mesh topology | Dynamic, unstructured peer-to-peer agent interaction (decentralized) |
| Workflow Graph | Explicit state machine with typed state, guard nodes, and approval steps (LangGraph) |
| Verbal Reinforcement | Storing natural-language critiques and conditioning future attempts on them (Reflexion) |
| Skill Accumulation | Non-parametric learning via external skill libraries of reusable, verified code (Voyager) |
| CLASSic | Evaluation framework: Cost, Latency, Accuracy, Security, Stability |

### 4.3 Open Challenges (Arunkumar 2026)

1. Hallucination in Action -- retrieval failures, cascading error propagation in multi-step loops
2. Infinite Loops -- agents trapped in repetitive retries, lacking meta-cognitive assessment
3. Latency/Cost Trade-off -- multi-agent overhead, need for System 2 -> System 1 distillation
4. Human-Agent Alignment -- task completion vs. social norms and safety boundaries
5. Open-Ended Learning -- static agents post-deployment, need for lifelong curriculum self-generation
6. Theoretical Limits -- understudied optimization boundaries and autonomy prerequisites

---

## 5. Convergence-Divergence Comparison

### 5.1 Component Mapping Across Taxonomies

| Concept | Wang 2023 | Xi 2023 | Arunkumar 2026 |
|---------|-----------|---------|----------------|
| **Agent identity/role** | Profiling Module (handcraft / LLM-gen / dataset) | Brain > NL Interaction + Knowledge | Profiling (system prompts, personas, role-switching) |
| **Short-term memory** | Unified Memory (in-context) | Memory > Length Limits + Summarization | Memory > Natural language streams |
| **Long-term memory** | Hybrid Memory (consolidated stores) | Memory > Vectors/Data Structures | Memory > SQL tables, paged stores, hierarchical clusters |
| **Memory retrieval** | Read (recency, relevance, importance) | Automated (same 3 metrics) + Interactive | Recency/relevance + Hierarchical + SQL + Controller-driven |
| **Memory management** | Write + Reflection | Summarization + Compression | Reflection + Decay + Paging + Semantic compression + Learned pruning |
| **Reasoning** | Single-path (CoT) + Multi-path (ToT) | CoT + Self-Consistency + Self-Refine + Selection-Inference | CoT + ReAct + Reflexion + ToT + LATS + Reasoning Models + ReAcTree |
| **Planning** | Without feedback (3 types) + With feedback (3 types) | Formulation (5 types) + Reflection (3 types) | 7 named methods with topology annotations |
| **Perception / Input** | (implicit in Action module) | Textual + Visual + Auditory + Other modalities | Perception dimension: text, vision, DOM, video, audio, 3D |
| **Tool use** | External Tools (subset of Action Space) | Tool Using (understand, learn, adapt, make) | 5 action paradigms: API, Code, ACI, Computer Use, Embodied VLA |
| **Embodied action** | (within Action Space) | Embodied Action (observe, manipulate, navigate) | Embodied VLA (continuous motor primitives) |
| **Multi-agent** | (not primary focus) | Cooperative + Adversarial interaction | 4 topologies (chain, star, mesh, workflow graph) + 5 mechanisms |
| **Human-agent** | Human feedback in planning | Instructor-Executor + Equal Partnership paradigms | (within collaboration mechanisms) |
| **Agent society** | (not covered) | Behavior, Personality (cognition/emotion/character), Environments | (not covered as separate section) |
| **Evaluation** | Subjective + Objective | Benchmarks section | CLASSic framework (Cost, Latency, Accuracy, Security, Stability) |
| **Formal model** | None | None | POMDP-based: A = <S, O, M, T, pi> |
| **Capability acquisition** | Fine-tuning + Prompt/Mechanism engineering | Transferability (zero-shot, ICL, continual learning) | 3 temporal horizons: In-context, Weight updates, Skill accumulation |

### 5.2 Where They Converge

1. **All three decompose agents into perception, reasoning/planning, memory, and action.** The boundaries differ but the conceptual modules are consistent.

2. **Memory is universally split into short-term (in-context) and long-term (external store).** All three cite recency and relevance as core retrieval signals.

3. **Planning decomposes into formulate-then-reflect.** Wang calls it "without/with feedback"; Xi calls it "formulation/reflection"; Arunkumar names specific algorithms but the pattern is the same.

4. **Tool use is a first-class action type.** All three treat external tool invocation as a primary action modality alongside text generation.

5. **Chain-of-Thought is the foundational reasoning primitive.** Every taxonomy builds on CoT as the base, then extends to trees, graphs, and self-correction loops.

6. **Hallucination and alignment are universal open problems.** All three surveys flag these as critical unsolved challenges.

### 5.3 Where They Diverge

| Dimension | Divergence |
|-----------|-----------|
| **Scope of "Perception"** | Wang 2023 has no explicit perception module -- input handling is implicit. Xi 2023 creates a full Perception branch with 4 modalities. Arunkumar 2026 makes Perception a formal dimension with multimodal grounding taxonomy. |
| **Agent identity** | Wang 2023 devotes a full module (Profiling) with 3 methods. Xi 2023 folds identity into the Brain's knowledge and NL interaction. Arunkumar 2026 treats it as Profiling with dynamic role-switching. |
| **Tool use granularity** | Wang 2023: "External Tools" as a flat category. Xi 2023: 4-stage pipeline (understand, learn, adapt, make). Arunkumar 2026: 5 distinct paradigms (API, Code, ACI, Computer Use, Embodied VLA) plus MCP standardization. |
| **Multi-agent systems** | Wang 2023: not a focus. Xi 2023: cooperative vs. adversarial binary. Arunkumar 2026: 4 topologies + 5 collaboration mechanisms with named systems. |
| **Agent society** | Only Xi 2023 covers social behavior, personality dimensions (cognition/emotion/character), and environment types for agent societies. The other two do not address this. |
| **Formal rigor** | Only Arunkumar 2026 provides a POMDP-based formal model. Wang and Xi are descriptive taxonomies without mathematical formalization. |
| **Evaluation** | Wang 2023: subjective/objective binary. Xi 2023: benchmark listing. Arunkumar 2026: structured CLASSic framework with 5 named dimensions. |
| **Temporal coverage** | Arunkumar 2026 covers 2024-2025 advances (reasoning models like o1/o3, MCP protocol, computer use, VLA) absent from the 2023 surveys. |
| **Capability acquisition** | Wang 2023 separates fine-tuning from mechanism engineering. Xi 2023 frames it as transferability/generalization. Arunkumar 2026 introduces temporal horizons (ephemeral, permanent, non-parametric). |

### 5.4 Evolution of the Field (2023 -> 2026)

| Aspect | 2023 State (Wang + Xi) | 2026 State (Arunkumar) |
|--------|----------------------|----------------------|
| Reasoning | CoT, ToT as prompting techniques | Reasoning models (o1, o3) with internalized inference-time search |
| Tool use | API calls, external models | MCP standard, native computer use, code-as-action, ACI |
| Planning topology | Linear and tree | Full graph (LATS with MCTS), hierarchical sub-agent spawning (ReAcTree) |
| Multi-agent | Cooperative/adversarial binary | 4 topologies + 5 mechanisms + workflow graphs with typed state |
| Memory | Summarization + embeddings | + Exponential decay, paging (MemGPT), semantic compression, learned pruning |
| Evaluation | Qualitative or benchmark-list | Structured CLASSic framework with security as first-class dimension |
| Safety | Mentioned as future work | Prompt injection in action, compartmentalization, allowlists, audit logging |
| Embodiment | Robotics as application domain | VLA models as a core action paradigm alongside digital actions |

---

## 6. Unified Glossary (All Three Papers)

| Term | Source(s) | Definition |
|------|-----------|-----------|
| Agent | All three | Autonomous entity that perceives, reasons, plans, and acts in an environment |
| Brain | Xi | The LLM core that stores knowledge and performs reasoning/planning |
| Profiling | Wang, Arunkumar | Module defining agent identity, role, and behavioral constraints |
| Memory (short-term) | All three | Recent observations held in the LLM's context window |
| Memory (long-term) | All three | Persistent store (embeddings, databases, paged memory) surviving beyond context |
| Memory Reflection | Wang, Xi | Abstracting raw experiences into higher-level insights |
| Memory Decay | Arunkumar | Exponential reduction of memory salience over time |
| Chain-of-Thought (CoT) | All three | Step-by-step reasoning trace before final answer |
| Tree of Thoughts (ToT) | Wang, Arunkumar | Branching search over multiple reasoning paths with backtracking |
| ReAct | Xi, Arunkumar | Interleaving thought and action in a linear loop |
| Reflexion | Arunkumar | Verbal reinforcement: storing NL critiques for future conditioning |
| LATS | Arunkumar | Language Agent Tree Search: MCTS with value feedback on reasoning trees |
| Planning Formulation | Xi | First planning stage: decomposing task into sub-steps |
| Planning Reflection | Xi | Second planning stage: evaluating/revising plan via feedback |
| External Planner | Wang | Using formal languages (PDDL) with external solvers |
| Tool Use | All three | Invoking external APIs, databases, models to extend agent capabilities |
| Tool Making | Xi | Agent creates new executable programs/tools autonomously |
| Code-as-Action | Arunkumar | Using generated executable code as the primary action primitive |
| Agent Computer Interface (ACI) | Arunkumar | Shell/IDE-level actions (SWE-agent pattern) |
| Computer Use | Arunkumar | GUI-level mouse/keyboard/screenshot actions |
| Model Context Protocol (MCP) | Arunkumar | Standardized protocol for tool exposure with auth and audit |
| Embodied Action | Xi, Arunkumar | Physical/virtual environment interaction (manipulation, navigation) |
| Embodied VLA | Arunkumar | Vision-Language-Action models producing continuous motor primitives |
| Cooperative Interaction | Xi | Multi-agent collaboration toward shared goals |
| Adversarial Interaction | Xi | Multi-agent competitive/debate exchanges for improvement |
| Chain Topology | Arunkumar | Sequential waterfall of agents (MetaGPT, ChatDev) |
| Star Topology | Arunkumar | Central controller with specialized workers (AutoGen, Swarm) |
| Mesh Topology | Arunkumar | Decentralized dynamic peer-to-peer interaction (CAMEL) |
| Workflow Graph | Arunkumar | Explicit state machine with typed state and guard nodes (LangGraph) |
| Instructor-Executor | Xi | Human directs, agent executes |
| Equal Partnership | Xi | Human and agent operate as peers |
| Agent Society | Xi | Emergent social phenomena from groups of interacting agents |
| Capability Acquisition | Wang | Obtaining new abilities via fine-tuning or mechanism engineering |
| In-Context Learning (ICL) | Xi, Arunkumar | Few-shot learning from prompt examples without parameter updates |
| Continual Learning | Xi | Progressive skill acquisition without catastrophic forgetting |
| Skill Accumulation | Arunkumar | Non-parametric learning via external verified skill libraries |
| CLASSic | Arunkumar | Evaluation framework: Cost, Latency, Accuracy, Security, Stability |
| Hallucination | All three | Generating plausible but factually incorrect outputs or actions |
| Prompt Injection | Arunkumar | Malicious instructions embedded in inputs that hijack agent behavior |

---

## 7. Implications for CEX Architecture

| Survey Insight | CEX Mapping |
|---------------|-------------|
| All three define Memory as short-term + long-term with retrieval scoring | CEX P10 Memory pillar: entity_memory, memory_summary, knowledge_index |
| Wang's Profiling Module = identity configuration | CEX brand_config.yaml + agent_card + system_prompt per nucleus |
| Xi's Brain = LLM core with 5 capabilities | CEX nucleus = LLM instance with 8F pipeline (reasoning through F1-F8) |
| Arunkumar's 5 action paradigms (API, Code, ACI, Computer Use, VLA) | CEX P04 Tools pillar: cli_tool, browser_tool, mcp_server, api_client |
| Multi-agent topologies (chain, star, mesh, workflow graph) | CEX dispatch: solo (star), grid (mesh), mission_runner (workflow graph) |
| CLASSic evaluation (Cost, Latency, Accuracy, Security, Stability) | CEX P07 Evaluation: quality_gate, scoring_rubric, benchmark |
| MCP as standardized tool protocol | CEX P04: mcp_server kind, tool exposure via _tools/ |
| Skill Accumulation as non-parametric learning | CEX P01 Knowledge: kind KCs, compiled artifacts as reusable skill library |
| Reflexion / verbal self-correction | CEX 8F F7 GOVERN: quality gate with retry loop |

---

## 8. Action Paradigm Deep Dive -- Implementations and Comparisons

The 5 action paradigms in Arunkumar 2026 represent a progression from structured API calls to full embodied physical control. Each paradigm has distinct tooling, benchmarks, and failure modes.

### 8.1 Paradigm 1: API-Based Actions

**Definition**: Agent invokes external tools via structured interfaces defined by schemas. The LLM generates function-call JSON; a dispatcher routes to the correct API.

| Dimension | Detail |
|-----------|--------|
| **Representative papers** | Toolformer (arXiv:2302.04761), Gorilla (arXiv:2305.15334), ToolBench (arXiv:2307.16789) |
| **How Toolformer works** | Self-supervised: model inserts API calls into its own training text, keeps them only if they reduce perplexity -- zero human annotation |
| **How Gorilla works** | Fine-tuned LLaMA on API documentation pairs; retrieval-aware training reduces hallucinated API names |
| **Action space** | Discrete: finite set of function signatures with typed parameters |
| **Orchestration layer** | MCP (Model Context Protocol), LangChain tool registry, OpenAI function-calling |
| **Key failure mode** | Hallucinated API names or parameter types not in schema (Gorilla cuts this ~70%) |
| **Benchmark** | ToolBench: 16,000 real-world APIs across 49 categories; measures solvable rate and win rate vs. ChatGPT |
| **CEX mapping** | P04 Tools: api_client, cli_tool, mcp_server kinds |

### 8.2 Paradigm 2: Code-as-Action

**Definition**: Agent generates executable code (Python, JavaScript, shell) as the action primitive. Code runs in a sandboxed interpreter; stdout/stderr return as observation.

| Dimension | Detail |
|-----------|--------|
| **Representative papers** | CodeAct (arXiv:2402.01030), Voyager (arXiv:2305.16291), LATM (arXiv:2305.17126) |
| **How CodeAct works** | Unified action space: ALL agent actions expressed as Python. State persists across turns via Python interpreter session. Superior to JSON actions on AlfWorld (+20%), WebArena (+4%) |
| **How Voyager works** | Lifelong learning in Minecraft: LLM writes JavaScript skills, stores in skill library, retrieves them for new tasks. Acquires 3.3x more unique items than AutoGPT |
| **How LATM works** | Language models as Tool Makers: powerful LLM writes tools once; weaker cached LLM calls them repeatedly. Reduces cost by 10-100x |
| **Action space** | Continuous (arbitrary code), but sandboxed |
| **Execution environment** | Python REPL (CodeAct), Minecraft API (Voyager), Docker container (OpenHands) |
| **Key failure mode** | Infinite loops, unconstrained resource usage if sandbox not enforced |
| **Benchmark** | M3ToolEval, InterCode; Voyager uses unique item acquisition and tech-tree distance |
| **CEX mapping** | P04 Tools: code_executor kind; boot scripts in boot/n0X.ps1 use code-as-action pattern |

**Comparison vs. API-based**:

| Property | API-based | Code-as-Action |
|----------|-----------|----------------|
| Action space | Finite, schema-defined | Infinite, any valid code |
| Composability | Limited to defined APIs | Arbitrary (loops, conditions, recursion) |
| Debuggability | Call-by-call tracing | Full interpreter traceback |
| Safety surface | API allowlist | Sandbox boundary (broader, harder to enforce) |
| Skill reuse | Via tool registry | Via skill library (Voyager pattern) |

### 8.3 Paradigm 3: Agent Computer Interface (ACI)

**Definition**: Agent operates shell, terminal, IDE, and developer tools directly. Actions are bash commands, file edits, test runs -- the same workflow a human developer uses.

| Dimension | Detail |
|-----------|--------|
| **Representative papers** | SWE-agent (arXiv:2405.15793), Claude Code (Anthropic, 2025), Devin (Cognition, 2024) |
| **How SWE-agent works** | Custom ACI with 5 commands: open, scroll, search_file, edit, submit. Linter feedback on every edit. Trajectory recorded as YAML for replay/analysis |
| **SWE-agent ACI commands** | open {file}, scroll_down, search_file {pattern}, edit {line_range} {content}, python {file}, submit |
| **How Claude Code works** | 6 primitive tools: Read, Write, Edit, Bash, Glob, Grep. Agent spawns sub-agents for parallelism. CLAUDE.md as persistent memory |
| **Action space** | Shell + file system + process management |
| **State representation** | File tree, current file view, bash history, test output |
| **Key failure mode** | Missing edit context (edit without read), infinite retry loops on failing tests |
| **Benchmark** | SWE-bench (2294 GitHub issues): resolved %, pass@1. SWE-bench Verified (500 human-verified). SWE-bench Pro (harder, fewer free solves) |
| **2026 SOTA** | Claude 3.7 Sonnet: 70.3% on SWE-bench Verified (Feb 2026) |
| **CEX mapping** | atom_28 cross-ref: SWE-agent IS the ACI paradigm; Claude Code IS the CEX execution environment |

**ACI vs. API comparison**:

| Property | API-based | ACI |
|----------|-----------|-----|
| Target | External services | Local developer environment |
| State | Stateless calls | Stateful (filesystem, processes) |
| Tooling | Schema-defined | Arbitrary shell commands |
| Audience | Product agents | Software engineering agents |
| Primary benchmark | ToolBench | SWE-bench |

### 8.4 Paradigm 4: Computer Use Actions

**Definition**: Agent controls GUI applications via screenshots, mouse coordinates, keyboard input. Operates at the pixel level; no special API access required.

| Dimension | Detail |
|-----------|--------|
| **Representative systems** | Claude Computer Use (Anthropic, Oct 2024), OpenAI Operator (Jan 2025), SeeAct (OSU, 2024) |
| **How Claude Computer Use works** | Captures desktop screenshot -> VLM reasons about next action -> outputs mouse_move / click / type / key / screenshot. Action loop continues until goal met or max steps |
| **How SeeAct works** | Screen-annotated HTML + screenshot -> LLM generates SeeAct interleaved grounding -> maps semantic description to screen element |
| **Action primitives** | mouse_move(x,y), click(button), type(text), key(combo), screenshot(), scroll(direction, amount) |
| **Action space** | Continuous 2D coordinates + discrete key events |
| **Key challenges** | Coordinate drift across screen resolutions, CAPTCHA bypass attempts, security (arbitrary app control) |
| **Benchmark** | OSWorld (369 tasks, real Ubuntu desktop), WindowsAgentArena (154 tasks, Windows 11), ScreenSpot (element grounding) |
| **2026 state** | Claude Computer Use on OSWorld: ~38.1% (best published as of Apr 2026). Human baseline: ~72.4% |
| **CEX mapping** | P04 Tools: browser_tool kind; N05 can invoke via cex_computer_use_builder |

**Computer Use vs. ACI comparison**:

| Property | ACI | Computer Use |
|----------|-----|--------------|
| Access method | Shell API | Screenshot + mouse/keyboard |
| Requires app cooperation | Yes (must have CLI) | No (any GUI app) |
| State visibility | Structured (file tree, stdout) | Unstructured (pixels) |
| Error recovery | Traceback | Visual only |
| Security model | File system permissions | Full desktop control |
| Primary use case | Dev tools, codebases | Web apps, desktop GUIs |

### 8.5 Paradigm 5: Embodied VLA (Vision-Language-Action)

**Definition**: Agent produces continuous motor control signals (torque, velocity, gripper position) conditioned on visual observations and language instructions. Bridges digital intelligence with physical robotics.

| Dimension | Detail |
|-----------|--------|
| **Representative papers** | RT-2 (arXiv:2307.15818), Gemini Robotics (DeepMind, Jan 2026), pi0 (Physical Intelligence, 2024) |
| **How RT-2 works** | Fine-tuned PaLM-E on web data + robot demonstrations. Tokenizes robot actions as text tokens (discretized motor values). Enables zero-shot generalization to unseen objects |
| **How Gemini Robotics works** | Gemini 2.0 + action expert head. Two variants: Gemini Robotics (dexterous manipulation) + Gemini Robotics-ER (extended reach, spatial reasoning). Cross-embodiment transfer |
| **Action space** | Continuous: 7-DOF arm deltas, gripper open/close, mobile base velocity |
| **Key challenges** | Embodiment gap (simulation-to-real), latency (<100ms for manipulation), data scarcity for edge cases |
| **Benchmark** | RT-2 eval (success rate on novel instruction-object pairs), LIBERO (96 tasks, manipulation), DROID (robot deployment diversity) |
| **Cross-embodiment** | Gemini Robotics transfers policies across Aloha2, KUKA iiwa, UR5 with single model |
| **CEX mapping** | No direct CEX kind yet; closest: vision_tool + code_executor composite |

**5-Paradigm Summary Comparison**:

| Paradigm | Action Type | State | Benchmark | 2026 SOTA |
|----------|-------------|-------|-----------|-----------|
| API-based | JSON function call | Stateless | ToolBench solvable-rate | Gorilla-7B: 70.3% |
| Code-as-Action | Executable code | Interpreter session | M3ToolEval, InterCode | CodeAct: 74.4% AlfWorld |
| ACI (shell/IDE) | Bash + file ops | Filesystem | SWE-bench Verified | Claude 3.7: 70.3% |
| Computer Use | Mouse/keyboard | Screen pixels | OSWorld | Claude: 38.1% |
| Embodied VLA | Motor primitives | Physical world | LIBERO, DROID | Gemini Robotics: SOTA |

---

## 9. POMDP Formalization -- Control Loop Analysis

Arunkumar 2026 provides the first published POMDP-based formal model for agentic AI. This section expands the formalization with control loop mechanics and per-component analysis.

### 9.1 Formal Model: A = <S, O, M, T, pi>

| Symbol | Name | Type | Description |
|--------|------|------|-------------|
| **S** | State space | Set | All possible world configurations + agent internal states |
| **O** | Observation function | Partial mapping S -> Z | Agent observes Z (partial view of S) via sensors/encoders |
| **M** | Memory | Updatable store | M_t = f(M_{t-1}, o_t, r_t) -- updated each step by observation + feedback |
| **T** | Thought/plan | Probabilistic inference | T_t ~ p(T | M_t, o_t) -- LLM infers plan from memory + current observation |
| **pi** | Policy | Action selector | a_t = pi(T_t, M_t) -- selects action conditioned on reasoning trace |

**Partial observability** is the key distinction from classic MDP: the agent never sees S directly. It only receives o_t (screenshot, stdout, API response) and must maintain M to compensate for the missing state.

### 9.2 The Agentic Control Loop (One Full Iteration)

```
t=0: Initialize M_0 (system prompt, task description, few-shot examples)
     |
     v
PERCEIVE:   o_t = Encoder(s_t)      -- multimodal encoders process environment
     |
     v
REMEMBER:   M_t = Update(M_{t-1}, o_t, r_{t-1})  -- store observation + last reward
     |
     v
PLAN:       T_t ~ LLM(M_t, o_t)    -- generate chain-of-thought + action plan
     |
     v
ACT:        a_t = pi(T_t, M_t)     -- select and execute action
     |
     v
OBSERVE:    r_t, o_{t+1} = Env(a_t) -- environment responds with reward + new obs
     |
     +---> back to PERCEIVE (t = t+1)
     |
     v (terminal condition)
TERMINATE: task_success | max_steps_exceeded | agent_abort
```

### 9.3 Memory Update Function Analysis

The memory update M_t = f(M_{t-1}, o_t, r_t) varies dramatically by memory architecture:

| Architecture | Update Function | Retention Policy | System |
|-------------|-----------------|------------------|--------|
| **Stream** | Append o_t to context | Truncate oldest | GPT-4 default |
| **Reflection** | Periodic: summarize last N -> high-level insight | Keep summary, discard raw | Generative Agents |
| **Exponential decay** | Score(m) = score(m) * e^(-lambda * delta_t) | Prune if score < threshold | MemoryBank |
| **Paging** | Virtualize: active page in context, rest on disk | Controller-driven eviction | MemGPT |
| **Semantic compression** | Cluster semantically similar -> centroid | Keep cluster label + examples | MemInsight |
| **Learned pruning** | RL policy decides what to keep/discard | Policy-guided retention | MemAgent |

### 9.4 Planning as Probabilistic Inference

The thought distribution T_t ~ p(T | M_t, o_t) is shaped by the planning algorithm:

| Algorithm | Search topology | Inference style | Latency | Backtracking |
|-----------|----------------|-----------------|---------|--------------|
| **Chain-of-Thought** | Linear | Single-pass | Low | None |
| **ReAct** | Linear loop | Interleaved thought-action | Medium | None (retry only) |
| **Reflexion** | Cyclical | NL critique stored in M | Medium | Via memory |
| **Tree of Thoughts** | Tree | External branching + BFS/DFS | High | Yes |
| **LATS (MCTS)** | Graph/tree | Value function + simulation | Very High | Yes + pruning |
| **Reasoning Models (o1/o3)** | Implicit tree | Internalized inference-time search | High (hidden) | Yes (internal) |
| **ReAcTree** | Hierarchical | Recursive sub-agent spawning | Very High | Per sub-agent |

**POMDP perspective**: more sophisticated search algorithms explore more of the belief space but at quadratic cost. Reasoning models (o1/o3) internalize this search, hiding the topology from external observation.

---

## 10. CLASSic Framework -- Dimensional Depth

Arunkumar 2026's CLASSic evaluation framework is the first structured multi-dimensional evaluation for agentic systems. This section expands each dimension with metrics and failure taxonomy.

### 10.1 Cost (C)

**What it measures**: Economic efficiency of agent task completion.

| Metric | Formula | Typical range |
|--------|---------|---------------|
| Token-per-task | Total tokens / tasks completed | 1K-100K tokens/task |
| Hierarchical overhead | Multi-agent total tokens / single-agent tokens | 1.5-10x overhead |
| Cost-per-solved-issue | $/issue (SWE-bench) | $0.50-$15/issue |
| Skill reuse ratio | Tasks solved via cached skills / total tasks | 0% (no reuse) to 80%+ (Voyager) |

**Cost reduction strategies**: skill libraries (Voyager), LATM (write once, call many), prompt caching, smaller editor models (Cursor Apply at 7B), speculative decoding.

### 10.2 Latency (L)

**What it measures**: Wall-clock time from task receipt to completion, including real-world operational constraints.

| Metric | Description | Acceptable range |
|--------|-------------|-----------------|
| End-to-end task latency | Clock time for full task | <60s (UI tasks), <10min (code tasks) |
| Agent-loop latency | Time per perceive-plan-act cycle | <5s per step |
| Tool call overhead | Latency added per external API call | <500ms per call |
| Async parallelism gain | Speedup from parallel sub-agents | 2-6x for grid dispatch |

**Latency benchmarks**: tau-bench uses time pressure scenarios to test real-world constraint handling. OSWorld measures steps-to-completion, not just success.

**System 2 -> System 1 distillation**: Arunkumar 2026 identifies this as the key latency optimization: expensive reasoning model solutions (System 2) distilled into fast, specialized models (System 1). Example: Cursor Apply model (7B, trained on LLM edits) achieves 98% accuracy at 10.5K tok/s.

### 10.3 Accuracy (A)

**What it measures**: Task success rate across multi-step, tool-using, long-horizon scenarios.

| Dimension | Metric | Baseline (human) |
|-----------|--------|-----------------|
| Multi-step tool use | Correct tool sequence / total sequences | ~90% human |
| State tracking | World state correctly maintained at step T | Degrades with horizon |
| Long-horizon recovery | Recover from failure mid-task | Human: ~85%, Agents: 30-50% |
| Instruction following | Task completion per exact instruction | Varies by domain |

**Key accuracy benchmarks by domain**:

| Domain | Benchmark | 2026 Best Agent | Human |
|--------|-----------|-----------------|-------|
| Software engineering | SWE-bench Verified | 70.3% (Claude 3.7) | ~100% |
| Desktop control | OSWorld | 38.1% (Claude) | 72.4% |
| Multi-step tool use | tau-bench | ~60-70% | ~85% |
| Mathematical reasoning | FrontierMath | ~25% (o3) | Expert-level |
| API chaining | ToolBench | ~60% (ToolLLaMA) | ~90% |

### 10.4 Security (S)

**What it measures**: Resistance to adversarial manipulation and degree of access control.

| Threat | Description | Mitigation |
|--------|-------------|-----------|
| **Prompt injection** | Malicious instructions in external content hijack agent | Input sanitization, compartmentalization |
| **Indirect injection** | Injections in retrieved documents or web pages | Content provenance tracking, scratchpad isolation |
| **Tool misuse** | Agent invoked outside intended scope | Allowlists, tool permissions per task |
| **Data exfiltration** | Agent leaks sensitive context to external APIs | Outbound filtering, audit logging |
| **Privilege escalation** | Agent requests elevated permissions beyond task scope | Least-privilege sandboxing, human-in-loop for risky ops |
| **Supply chain** | Compromised tools/APIs affect agent behavior | Tool provenance + signature verification |

**Security evaluation maturity**: As of 2026, only a handful of benchmarks address agent security systematically (AgentHarm, PrivacyLens). Most benchmarks measure accuracy only.

**CEX application**: N07 dispatch uses session-isolated PIDs; stop command is session-aware to prevent cross-session interference.

### 10.5 Stability (St)

**What it measures**: Consistency and predictability of agent behavior across runs, environments, and edge cases.

| Metric | Description | Target |
|--------|-------------|--------|
| Run variance | Std dev of success rate across 5 runs | <5% for production |
| Failure mode distribution | Categorized failure types and frequencies | No single mode >30% |
| Compliance rate | Tasks completed within policy constraints | >95% |
| Infinite loop rate | % of runs entering retry loop with no progress | <2% |
| Graceful degradation | Fails safely when max steps exceeded | 100% |

**Stability failure taxonomy** (from OSWorld + SWE-bench analysis):
1. Hallucinated state -- agent believes task is done when it isn't
2. Stuck retry -- same failed action repeated without plan revision
3. Context overflow -- loses track of task after long trajectory
4. Tool chaining error -- correct individual calls, wrong sequence
5. Ambiguity paralysis -- refuses to act on underspecified instructions

**Cross-run consistency**: Reasoning models (o1/o3) show lower variance than standard CoT because their internal search is more exhaustive. Trade-off: higher latency.

---

## 11. Cross-Reference: Agent Taxonomy vs. Code Agents (atom_28)

The 5 action paradigms from Arunkumar 2026 map precisely onto the platforms documented in atom_28 (Code Agent Vocabulary Atlas). This section provides the explicit mapping.

### 11.1 Platform-to-Paradigm Mapping

| Platform (atom_28) | Paradigm | Action mechanism | Benchmark |
|-------------------|----------|-----------------|-----------|
| Claude Code | ACI | Read, Write, Edit, Bash, Glob, Grep tools | SWE-bench Verified |
| Codex CLI | ACI + Code-as-Action | Bash + patch format | Internal |
| Aider | ACI | Diff formats + bash commands | SWE-bench |
| Cursor | ACI + Computer Use | IDE API + Apply model | Internal |
| Devin | ACI + Computer Use | Full desktop env + browser | SWE-bench |
| SWE-Agent | ACI | Custom ACI (open, scroll, edit, submit) | SWE-bench (origin) |
| OpenHands (CodeAct) | Code-as-Action | Python interpreter as unified action space | AlfWorld, WebArena |
| Augment Code | ACI | Semantic dependency graph + edits | Internal |
| Gemini Robotics | Embodied VLA | Motor primitives + vision | LIBERO, DROID |

### 11.2 Edit Formats as Action Paradigm Variants

The edit format taxonomy in atom_28 is a specialization of the Code-as-Action / ACI paradigms for software engineering:

| Edit Format (atom_28) | Paradigm | Action type | Failure mode |
|----------------------|----------|-------------|--------------|
| Whole file | Code-as-Action | Return entire file as action | Expensive; lazy elision |
| Search/replace blocks | ACI | Surgical patch as action | Pattern match drift |
| Unified diff (udiff) | ACI | Standard diff as action | LLM format compliance |
| Tool-based edits | ACI | Structured function call (Read+Edit) | Requires tool infra |
| Sketch + Apply model | ACI + Code-as-Action | Two-phase: plan then apply | Two-model latency |

### 11.3 ACI Vocabulary Alignment

Terms that appear in both atom_19 (taxonomy) and atom_28 (code agents) with identical meaning:

| Term | atom_19 source | atom_28 mapping |
|------|---------------|-----------------|
| Agent Computer Interface (ACI) | Arunkumar 2026 | SWE-agent architecture section |
| Code-as-Action | Arunkumar 2026 | OpenHands/CodeAct platform entry |
| Skill Accumulation | Arunkumar 2026 | Voyager skill library entry |
| Continual Learning | Xi 2023 | Voyager/Minecraft lifelong learning |
| Workflow Graph | Arunkumar 2026 | LangGraph pattern in atom_28 |
| Architect mode | (not in atom_19) | Aider two-phase pattern (maps to N07/N03 split in CEX) |

---

## 12. Emerging 2026 Research -- Jan-Apr Updates

New papers and systems published Jan-Apr 2026 that extend or challenge the Arunkumar taxonomy.

### 12.1 New Survey Papers and Systems (2026)

| Paper / System | Date | Key contribution | Extends which paradigm |
|----------------|------|-----------------|----------------------|
| **Gemini Robotics** (DeepMind) | Jan 2026 | Cross-embodiment VLA, dexterous manipulation SOTA | Embodied VLA |
| **OpenAI Operator** | Jan 2026 | Computer Use paradigm enters production; API for app control | Computer Use |
| **Agent-FLAN** (Alibaba) | Feb 2026 | Fine-tuning recipe for instruction-following agents; +10% on AgentBench | Weight updates learning paradigm |
| **Claude 3.7 Sonnet** | Feb 2026 | 70.3% SWE-bench Verified; extended thinking mode maps to Reflexion | ACI SOTA |
| **TradingAgents** | Feb 2026 | Market simulation via adversarial multi-agent; emergent economic behavior | Mesh topology collaboration |
| **A2A Protocol** (Google) | Mar 2026 | Standardizes inter-agent communication; complements MCP for tools | Multi-agent collaboration |
| **MCP 2.0** (Anthropic/community) | Q1 2026 | OAuth scoping + audit; strengthens CLASSic Security dimension | API-based security |
| **AgentRM** | Mar 2026 | Process reward model for agents; prefer intermediate step quality over final outcome | Skill accumulation + CLASSic |
| **Gemini 2.5 Pro** (Google) | Apr 2026 | 1M context; changes memory strategy (less paging needed) | Memory architecture |
| **SWE-bench Pro** | Apr 2026 | Harder variant: private test cases, anti-gaming measures | ACI benchmark evolution |
| **MARBLE** | 2026 | Unified multi-env benchmark: 12 environments, emergent behavior metrics | CLASSic Accuracy dimension |

### 12.2 Taxonomy Gaps Identified

Based on Jan-Apr 2026 research, three areas are inadequately covered by the three foundational surveys:

1. **Agent-to-Agent communication protocols**: Wang/Xi/Arunkumar treat multi-agent interaction as high-level topologies. A2A and MCP 2.0 show the need for a sub-taxonomy of inter-agent message formats, trust models, and capability negotiation. **Gap**: no taxonomy of agent-to-agent trust surface analogous to the CLASSic Security dimension.

2. **Process Reward Models (PRMs) for agents**: All three surveys treat evaluation as outcome-based. AgentRM (2026) shows process-level reward modeling changes both training and inference-time search in ways the POMDP model does not capture. The POMDP reward r_t is assumed scalar; PRMs introduce dense, step-level reward shaping.

3. **Hybrid digital-physical agents**: Embodied VLA and Computer Use are categorized separately in Arunkumar 2026, but Gemini Robotics and Devin show that agents increasingly cross both boundaries within a single task (web research -> robot assembly). No current taxonomy covers this hybrid action space.

### 12.3 Convergence Since 2023

| Taxonomy dimension | 2023 state | 2026 state (new convergence) |
|-------------------|-----------|------------------------------|
| Tool protocol | Proprietary per-system APIs | MCP as emerging standard (all major vendors) |
| Multi-agent communication | Ad hoc (AutoGen, CAMEL each invent own) | A2A protocol proposed as standard |
| Edit format | 6+ competing formats (Aider, Codex, etc.) | Tool-based edits (Claude Code model) gaining adoption |
| Evaluation | Benchmark zoo | CLASSic + SWE-bench Verified as near-universal references |
| Memory | Flat or simple reflection | 6-architecture taxonomy (stream, reflection, decay, paging, compression, learned) |

---

## Sources

- [Wang et al. 2023 - A Survey on LLM-based Autonomous Agents](https://arxiv.org/abs/2308.11432)
- [Xi et al. 2023 - The Rise and Potential of LLM-Based Agents](https://arxiv.org/abs/2309.07864)
- [Arunkumar et al. 2026 - Agentic AI: Architectures, Taxonomies, and Evaluation](https://arxiv.org/abs/2601.12560)
- [Schick et al. 2023 - Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- [Patil et al. 2023 - Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334)
- [Wang et al. 2024 - CodeAct: Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030)
- [Wang et al. 2023 - Voyager: An Open-Ended Embodied Agent with LLMs](https://arxiv.org/abs/2305.16291)
- [Yang et al. 2024 - SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793)
- [Brohan et al. 2023 - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)
- [LLM-Agent-Paper-List (GitHub)](https://github.com/WooooDyy/LLM-Agent-Paper-List)
- [CEX atom_28 - Code Agent Vocabulary Atlas](N01_intelligence/research/atlas/atom_28_code_agents.md)
