---
id: atom_22_memory_taxonomy
kind: knowledge_card
pillar: P01_knowledge
title: "Atomic Research 22: Agent Memory Taxonomy -- Complete Survey Synthesis"
version: 1.0
quality: 8.9
tags: [memory, taxonomy, LLM-agents, episodic, semantic, procedural, skill-library, consolidation, RAG, survey]
created: 2026-04-13
author: n01_intelligence
domain: agent memory systems
sources:
  - "arxiv:2404.13501 (Survey on Memory Mechanism of LLM-based Agents, ACM TOIS)"
  - "arxiv:2602.19320 (Anatomy of Agentic Memory, Feb 2026)"
  - "arxiv:2504.15965 (From Human Memory to AI Memory)"
  - "arxiv:2602.12430 (Agent Skills for LLMs)"
  - "arxiv:2603.07670 (Memory for Autonomous LLM Agents, Mar 2026)"
tldr: "Unified memory taxonomy from 5 surveys: 3 temporal scopes (working/episodic/semantic+procedural), 4 agentic structures (lightweight-semantic, entity-centric, episodic-reflective, structured-hierarchical), 5 storage substrates, 3 control policies, 3 core operations (write-manage-read), and skill libraries as procedural memory. Mapped to 5 CEX kinds."
---

# Atomic Research 22: Agent Memory Taxonomy

## 1. Temporal Scope (Duration-Based Classification)

The foundational split mirrors human cognitive science (Atkinson-Shiffrin model).

### 1.1 Working Memory (Short-Term)

| Property | Description |
|----------|-------------|
| Definition | Whatever fits inside the current context window |
| Cognitive analog | Baddeley's central executive + phonological loop + visuospatial sketchpad |
| Capacity | Bounded by context window (4K-1M tokens depending on model) |
| Persistence | Single session / single task |
| Formats | System prompt, recent messages, scratchpad, chain-of-thought traces |
| Bottleneck | Token budget -- everything competes for the same window |

The "From Human Memory to AI Memory" paper (2504.15965) identifies **four quadrants** of working memory by crossing Object (Personal vs System) x Form (Parametric vs Non-Parametric):

| Quadrant | Object | Form | Example |
|----------|--------|------|---------|
| I | Personal | Non-Parametric | Real-time context supplementation from user profile |
| III | Personal | Parametric | Temporarily enhanced contextual understanding |
| V | System | Non-Parametric | Complex reasoning scratchpad (chain-of-thought) |
| VII | System | Parametric | KV-Cache reuse, prompt caching |

### 1.2 Long-Term Memory

Persists across sessions. Three subtypes from cognitive science, all mapped to AI:

#### 1.2.1 Episodic Memory (Explicit/Declarative)

| Property | Description |
|----------|-------------|
| Definition | Concrete experience records with context (who, what, when, where) |
| Cognitive analog | Tulving's episodic memory -- autobiographical events |
| Content | Tool calls, conversation turns, environment observations, task outcomes |
| Example | "User asked for DD/MM/YYYY format on 2026-04-10 in session #47" |
| Storage | Vector-indexed stores with timestamp + importance metadata |
| Retrieval | Embedding similarity + recency decay + importance weighting |
| AI quadrant (2504.15965) | Quadrant II: Personal, Non-Parametric, Long-Term |

#### 1.2.2 Semantic Memory (Explicit/Declarative)

| Property | Description |
|----------|-------------|
| Definition | Abstracted, de-contextualized knowledge -- facts without episodes |
| Cognitive analog | Tulving's semantic memory -- general world knowledge |
| Content | Consolidated patterns, user preferences, domain facts, entity attributes |
| Example | "User prefers DD/MM/YYYY" (stripped of episode context) |
| Formation | Consolidation from episodic records via clustering/summarization |
| Storage | Knowledge graphs, structured records, parametric weights |
| AI quadrants (2504.15965) | Quadrant IV (Personal, Parametric, Long-Term) + Quadrant VIII (System, Parametric, Long-Term) |

#### 1.2.3 Procedural Memory (Implicit/Non-Declarative)

| Property | Description |
|----------|-------------|
| Definition | Reusable skills, executable plans, learned procedures |
| Cognitive analog | Motor skills, habits, conditioned responses |
| Content | Code libraries, plan templates, tool-use sequences, SOPs |
| Example | Voyager's JavaScript skill library indexed by natural language descriptions |
| Storage | Executable repositories, SKILL.md files, compiled plan templates |
| Retrieval | Natural language description matching, task-type routing |
| AI quadrant (2504.15965) | Quadrant VI: System, Non-Parametric, Long-Term |

### 1.3 Sensory Memory (Input Buffer)

| Property | Description |
|----------|-------------|
| Definition | Brief storage of raw input before processing |
| Cognitive analog | Iconic (visual) and echoic (auditory) memory, ~250ms |
| AI equivalent | Tokenization, input parsing, modality conversion |
| Persistence | Transient -- consumed immediately by encoder |

---

## 2. Four Agentic Memory Structures (Anatomy of Agentic Memory, 2602.19320)

The Anatomy paper organizes MAG (Memory-Augmented Generation) systems by **structure**, orthogonal to temporal scope.

### 2.1 Lightweight Semantic Memory

| Property | Description |
|----------|-------------|
| Definition | Independent textual units embedded in vector space, retrieved via top-k similarity |
| Subdivisions | RL-optimized compression, heuristic/prompt-optimized, context window management, token-level |
| Strengths | Simple, scalable, fast retrieval |
| Weakness | Loses structured relationships; semantic similarity != task relevance |
| Representative | Standard RAG systems (FAISS, Chroma, Pinecone) |

### 2.2 Entity-Centric and Personalized Memory

| Property | Description |
|----------|-------------|
| Definition | Information organized around explicit entities using structured records or attribute-value pairs |
| Subdivisions | Entity-centric memory (structured entity records) + personalized memory (persistent user profiles) |
| Strengths | Preserves entity relationships; supports complex queries |
| Weakness | Requires upfront schema design |
| Representative | Knowledge graphs, entity databases, user profile stores |

### 2.3 Episodic and Reflective Memory

| Property | Description |
|----------|-------------|
| Definition | Interactions organized into episodes or higher-level summaries with periodic consolidation |
| Subdivisions | Episodic buffer with learned control, episodic recall for exploration, episodic reflection & consolidation, episodic utility learning |
| Strengths | Captures temporal dynamics; enables learning from experience |
| Weakness | Summarization drift; over-generalization risk |
| Representative | Generative Agents (Park et al. 2023), Reflexion |

### 2.4 Structured and Hierarchical Memory

| Property | Description |
|----------|-------------|
| Definition | Explicit organization over stored information using graphs or multi-tier storage |
| Subdivisions | Graph-structured memory, OS-inspired hierarchical memory, policy-optimized memory management |
| Strengths | Rich relational queries; principled capacity management |
| Weakness | Orchestration complexity; cold-start problem |
| Representative | MemGPT (OS-inspired tiers), temporal knowledge graphs |

---

## 3. The 3D-8Q Taxonomy (From Human Memory to AI Memory, 2504.15965)

Three dimensions, eight quadrants:

| Dimension | Values | Description |
|-----------|--------|-------------|
| **Object** | Personal vs System | Who benefits -- user modeling vs system reasoning |
| **Form** | Parametric vs Non-Parametric | Embedded in weights vs stored externally |
| **Time** | Short-Term vs Long-Term | Session-scoped vs cross-session |

### Complete Eight-Quadrant Map

| Q | Object | Form | Time | Role | Function |
|---|--------|------|------|------|----------|
| I | Personal | Non-Parametric | Short-Term | Working Memory | Real-time context supplementation |
| II | Personal | Non-Parametric | Long-Term | Episodic Memory | Cross-session personalization |
| III | Personal | Parametric | Short-Term | Working Memory | Temporarily enhanced understanding |
| IV | Personal | Parametric | Long-Term | Semantic Memory | Knowledge integration into weights |
| V | System | Non-Parametric | Short-Term | Working Memory | Complex reasoning scratchpad |
| VI | System | Non-Parametric | Long-Term | Procedural Memory | Historical experiences for refinement |
| VII | System | Parametric | Short-Term | Working Memory | KV-Cache, prompt caching |
| VIII | System | Parametric | Long-Term | Semantic Memory | Foundational knowledge base (pre-training) |

---

## 4. Storage Substrates (Representational Formats)

| Substrate | Characteristics | Strengths | Limitations |
|-----------|-----------------|-----------|-------------|
| **Context-resident text** | Summaries, scratchpads, CoT traces | Fully transparent, zero infrastructure | Capacity-limited, summarization drift |
| **Vector-indexed stores** | Dense embeddings + ANN search (FAISS, HNSW) | Scales to millions of records | Loses structured relationships |
| **Structured stores** | SQL databases, key-value maps, knowledge graphs | Preserves relational structure; complex queries | Requires upfront schema design |
| **Executable repositories** | Code libraries, tool definitions, plan templates | Direct skill invocation; avoids regeneration errors | Requires verification and maintenance |
| **Hybrid stores** | Multiple tiers with different access patterns | Balances transparency, scale, queryability | Orchestration complexity |

---

## 5. Control Policies (Who Decides Memory Operations)

| Policy | Mechanism | Strengths | Weaknesses |
|--------|-----------|-----------|------------|
| **Heuristic** | Hard-coded rules (top-k, summarize every N turns, expire after D days) | Predictable, debuggable | Context-blind |
| **Prompted self-control** | Memory ops exposed as tool calls; LLM decides when to invoke | Flexible, adaptive | Quality depends on instruction-following |
| **Learned control** | Memory ops trained as RL policy actions | Discovers non-obvious strategies (e.g., preemptive summarization) | Expensive to train; interpretability challenges |

---

## 6. Memory Operations (Write-Manage-Read Loop)

### 6.1 Write Path (Encoding)

| Operation | Description |
|-----------|-------------|
| Filtering | Reject low-signal records (noise, redundancy) |
| Canonicalization | Normalize dates, names, quantities |
| Deduplication | Merge overlapping entries |
| Priority scoring | Rank by task relevance and novelty |
| Metadata tagging | Timestamp, source, task label, confidence |
| Importance scoring | Self-assessed importance (1-10) for retrieval weighting |

### 6.2 Manage Path (Consolidation + Maintenance)

| Operation | Description |
|-----------|-------------|
| **Consolidation** | Episodic -> semantic transitions; offline clustering + abstraction |
| **Compression** | Rolling summaries; hierarchical abstraction (turn -> session -> topic) |
| **Contradiction resolution** | Flag conflicts; source attribution; temporal versioning |
| **Temporal versioning** | Prefer newest records; track record lineage |
| **Eviction** | LRU, LFU, or learned priority scoring under capacity constraints |
| **Forgetting** | Time-based expiration, policy-triggered discard, machine unlearning |
| **Reconsolidation** | Reactivate stored memory, modify/update to adapt to new information |
| **Reflection** | Cluster observations; extract higher-order generalizations from episodes |

### 6.3 Read Path (Retrieval)

| Operation | Description |
|-----------|-------------|
| Query formulation | LLM reformulation, multi-query fan-out, subgoal-based signals |
| Two-stage retrieval | Fast filtering (BM25/metadata) -> slow reranking (cross-encoder) |
| Retrieval gating | Decide whether retrieval is necessary (Self-RAG pattern) |
| Token budgeting | Dynamically allocate context space between memory and task |
| Caching | High-frequency records (user preferences) pre-loaded |
| Multi-signal scoring | Recency (exponential decay) x relevance (embedding) x importance (self-assessed) |

---

## 7. Memory Consolidation and Tiering

### 7.1 Consolidation Mechanisms

| Mechanism | Description | Cognitive Analog |
|-----------|-------------|-----------------|
| Summarization | Compress episodes into compact representations | Sleep-based memory consolidation |
| Reflection synthesis | Cluster observations -> extract higher-order rules | Metacognition |
| Temporal-hierarchical trees | Nest summaries at turn/session/topic granularity | Hippocampal replay |
| Episodic -> semantic promotion | De-contextualize recurring patterns into facts | Systems consolidation |
| Graph restructuring | LLM-driven reorganization of knowledge graph edges | Schema assimilation |

### 7.2 Tiering Architecture (OS-Inspired)

| Tier | Analog | Access Speed | Capacity | Content |
|------|--------|-------------|----------|---------|
| **Main context (RAM)** | Working memory | Instant (in-context) | Limited (context window) | System prompt, recent messages, active records |
| **Recall storage (disk)** | Episodic LTM | Fast (DB query) | Large (millions of records) | Searchable database of all past interactions |
| **Archival storage (cold)** | Semantic LTM | Slow (vector search) | Very large | Documents, long-term knowledge, compressed history |

### 7.3 Eviction Strategies

| Strategy | Description | Risk |
|----------|-------------|------|
| LRU (Least Recently Used) | Evict oldest-accessed records | Loses infrequent but critical info |
| LFU (Least Frequently Used) | Evict least-accessed records | Cold-start bias against new records |
| Importance-weighted | Learned priority scoring | Requires accurate importance estimation |
| Time-based expiration | TTL with linear/exponential decay | Silent loss if TTL too aggressive |
| Capacity-triggered compression | Summarize when buffer exceeds threshold | Summarization drift |

---

## 8. Skill Libraries as Procedural Memory (2602.12430)

### 8.1 Definition

Agent skills are "self-contained packages comprising a structured instruction file (SKILL.md), optional scripts, reference documents, and assets." They differ from tools: "tools execute and return results, whereas skills prepare the agent to solve a problem by injecting procedural knowledge."

### 8.2 Three-Level Progressive Disclosure

| Level | Content | Load Timing | Token Cost |
|-------|---------|-------------|------------|
| L1 | SKILL.md metadata (name, description) | Startup | ~dozens tokens per skill |
| L2 | Full procedural instructions | On skill trigger | Hundreds to thousands |
| L3 | Executable scripts, technical appendices | On-demand | Variable |

### 8.3 Six Acquisition Modalities

| Method | Mechanism | Key Result |
|--------|-----------|------------|
| **Human-authored** | Manual SKILL.md creation | 62k+ GitHub stars within months (Claude Code) |
| **RL with libraries** | SAGE sequential rollouts + skill-integrated reward | 8.9% improvement, 59% fewer tokens |
| **Autonomous discovery** | SEAgent curriculum generation + specialist-to-generalist | 11.3% -> 34.5% success gains |
| **Structured bases** | CUA-Skill parameterized graphs | 57.5% SOTA on GUI tasks |
| **Compositional synthesis** | Dynamic skill selection/composition | 91.6% on AIME benchmark |
| **Skill compilation** | Multi-agent -> single-agent compression | Phase transition at critical library size |

### 8.4 Skills vs Tools vs RAG

| Dimension | Agent Skills | Tools (MCP) | RAG Passages |
|-----------|-------------|-------------|-------------|
| Role | Procedural knowledge injection | Action execution | Factual retrieval |
| Content | Workflows + code + permissions | API endpoints | Document chunks |
| Activation | Context modification (hidden) | Explicit invocation | Query-triggered |
| Effect | Changes how agent thinks | Changes what agent can do | Changes what agent knows |
| Persistence | Permanent in skill library | Session-configured | Index-dependent |

### 8.5 Security Considerations

26.1% of skills in the wild contain at least one vulnerability. Three-component governance framework:
1. **Verification gates**: Static analysis -> LLM semantic check -> behavioral sandbox -> permission validation
2. **Trust tiers**: T1 (unvetted, instruction-only) -> T2 (verified) -> T3 (vendor-certified) -> T4 (trusted partner)
3. **Lifecycle trust evolution**: Runtime monitoring with promotion/demotion based on behavior

---

## 9. Representative Systems Timeline

| System | Year | Primary Memory | Substrate | Control |
|--------|------|---------------|-----------|---------|
| RAG | 2020 | Retrieval-augmented semantic | Vector index | Heuristic |
| ReAct | 2022 | Trajectory traces | Context-resident | Heuristic |
| Reflexion | 2023 | Reflective episodic | Context-resident | Prompted |
| Generative Agents | 2023 | Episodic + reflective | Vector-indexed | Heuristic (recency/relevance/importance) |
| Voyager | 2023 | Procedural (skill library) | Executable code | Heuristic |
| MemGPT | 2024 | Hierarchical virtual (OS-inspired) | Hybrid (context + DB + vector) | Prompted (tool calls) |
| MIRIX | 2025 | Multi-module (6 types) | Hybrid | Prompted |
| MemoryOS | 2025 | OS-inspired hierarchical | Hybrid | Learned |
| Agentic Memory | 2026 | Unified STM/LTM | Hybrid | Learned (RL policy) |

---

## 10. Benchmarks and Evaluation

### 10.1 Key Benchmarks

| Benchmark | Year | Tokens | Sessions | Focus |
|-----------|------|--------|----------|-------|
| HotpotQA | 2018 | ~1K | 1 | Factual QA (saturated for memory eval) |
| LoCoMo | 2024 | ~20K | 35 | Factual QA + event summarization + dialogue |
| MemBench | 2025 | ~100K | N/A | Factual vs reflective; effectiveness/efficiency/capacity |
| MemoryAgentBench | 2025 | Variable | Multi-turn | 4 competencies: retrieval, learning, understanding, forgetting |
| LongMemEval-M | 2025 | >1M | Variable | Requires external memory (exceeds any context window) |
| MemoryArena | 2026 | Multi-session | Agentic tasks | Active memory use (passive recall models drop to 40-60%) |

### 10.2 Four-Layer Evaluation Stack (2603.07670)

| Layer | What It Measures |
|-------|-----------------|
| L1 Task Effectiveness | Success rate, factual correctness, plan completion |
| L2 Memory Quality | Precision/recall of retrieved records, contradiction rate, staleness, coverage |
| L3 Efficiency | Latency per operation, prompt tokens consumed, storage growth |
| L4 Governance | Privacy leakage, deletion compliance, access-scope violations |

### 10.3 Context Saturation Gap

Critical metric from Anatomy paper (2602.19320): `Delta = Score_MAG - Score_FullContext`. A benchmark meaningfully evaluates agentic memory only when Delta >> 0 (tasks exceed effective context capacity).

---

## 11. Architecture Deployment Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **A: Monolithic Context** | All memory in prompt; zero infrastructure | Short-lived agents, prototyping |
| **B: Context + Retrieval Store** | Working memory in context; LTM in vector/structured store | Coding assistants, enterprise copilots (workhorse) |
| **C: Tiered with Learned Control** | Multiple tiers with RL-trained orchestration | Long-running, high-stakes deployments |

---

## 12. Open Research Frontiers

1. **Principled consolidation** -- estimating importance without future knowledge
2. **Causally grounded retrieval** -- beyond semantic similarity to "what caused this?"
3. **Trustworthy reflection** -- avoiding self-reinforcing errors in reflection loops
4. **Learning to forget** -- selective forgetting under safety constraints + machine unlearning
5. **Multimodal embodied memory** -- fusing text, vision, audio, proprioception
6. **Multi-agent memory governance** -- access control, consensus protocols for shared stores
7. **Memory-efficient architectures** -- sparse retrieval, compressed vectors
8. **Neuroscience integration** -- spreading activation, reconsolidation, spaced repetition
9. **Foundation models for memory** -- task-agnostic memory controllers
10. **Standardized evaluation** -- GLUE-style leaderboard for memory systems

---

## 13. Mapping to CEX Kinds

| Taxonomy Concept | CEX Kind | Pillar | CEX Role |
|-----------------|----------|--------|----------|
| **Entity facts** (semantic memory about entities) | `entity_memory` | P10 | Stores facts about specific entities (people, orgs, concepts). Quadrant II/IV in 3D-8Q. |
| **Memory access policy** (which memory, who reads) | `memory_scope` | P02 | Configures per-agent memory access -- maps to control policy layer (heuristic/prompted/learned). |
| **Compressed history** (consolidation output) | `memory_summary` | P10 | Rolling summaries, hierarchical abstractions. The OUTPUT of consolidation operations. |
| **Memory classification** (type taxonomy + decay) | `memory_type` | P10 | Classifies memory by source, confidence, decay rate. Maps directly to this taxonomy's temporal scope + 3D-8Q quadrants. |
| **Search index** (retrieval infrastructure) | `knowledge_index` | P10 | BM25/FAISS indexes. The READ PATH infrastructure -- substrate for vector-indexed stores. |

### CEX Coverage Gaps Identified

| Taxonomy Concept | Status in CEX | Recommendation |
|-----------------|---------------|----------------|
| Procedural memory / skill library | No dedicated kind | Consider `skill_definition` kind (P04 or P03) for SKILL.md-style packages |
| Episodic memory (raw episodes) | Partially covered by `learning_record` (P11) | `learning_record` captures corrections, not full episode traces |
| Reflection / meta-memory | No dedicated kind | Consider `reflection_record` kind (P10) for synthesized generalizations |
| Memory consolidation policy | No dedicated kind | Could extend `memory_type` with consolidation rules |
| Memory tiering config | No dedicated kind | Could extend `memory_scope` with tier definitions (RAM/disk/cold) |
| Multi-signal retrieval scoring | Partially in `knowledge_index` config | Add recency/importance weighting to index config |

### CEX Memory Architecture Pattern

CEX currently operates as **Pattern B** (Context + Retrieval Store):
- Working memory: context window (CLAUDE.md + rules + handoff + agent card)
- Long-term episodic: `.cex/learning_records/`, `.cex/runtime/signals/`
- Long-term semantic: `P01_knowledge/library/` (knowledge cards), `entity_memory` instances
- Long-term procedural: `archetypes/builders/` (13 ISOs per kind = skill packages)
- Retrieval: `cex_retriever.py` (TF-IDF), `cex_memory_select.py` (keyword + LLM)

The builder ISO system (`bld_manifest`, `bld_instruction`, `bld_system_prompt` x 13 per kind) is **functionally equivalent to a skill library** with three-level progressive disclosure:
- L1: `kinds_meta.json` entries (name + description) = startup metadata
- L2: `bld_manifest` + `bld_instruction` = procedural instructions on trigger
- L3: `bld_system_prompt` + shared skills = full execution context on demand

---

## Sources

- [Survey on Memory Mechanism of LLM-based Agents (ACM TOIS)](https://arxiv.org/abs/2404.13501)
- [Anatomy of Agentic Memory (Feb 2026)](https://arxiv.org/abs/2602.19320)
- [From Human Memory to AI Memory (Apr 2025)](https://arxiv.org/abs/2504.15965)
- [Agent Skills for LLMs (Feb 2026)](https://arxiv.org/abs/2602.12430)
- [Memory for Autonomous LLM Agents (Mar 2026)](https://arxiv.org/abs/2603.07670)
- [Agent Memory Paper List (GitHub)](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)
