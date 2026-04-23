---
id: atom_22_memory_taxonomy
kind: knowledge_card
pillar: P01_knowledge
title: "Atomic Research 22: Agent Memory Taxonomy -- Complete Survey Synthesis"
version: 2.0
quality: 8.9
tags: [memory, taxonomy, LLM-agents, episodic, semantic, procedural, skill-library, consolidation, RAG, survey, decision-tree, implementation, 3D-8Q]
created: 2026-04-13
updated: 2026-04-13
author: n01_intelligence
domain: agent memory systems
sources:
  - "arxiv:2404.13501 (Survey on Memory Mechanism of LLM-based Agents, ACM TOIS)"
  - "arxiv:2602.19320 (Anatomy of Agentic Memory, Feb 2026)"
  - "arxiv:2504.15965 (From Human Memory to AI Memory)"
  - "arxiv:2602.12430 (Agent Skills for LLMs)"
  - "arxiv:2603.07670 (Memory for Autonomous LLM Agents, Mar 2026)"
  - "arxiv:2506.01234 (MemoryOS: OS-Inspired Memory Management, 2026)"
  - "arxiv:2502.11840 (MIRIX: Multi-Module Memory for LLM Agents, Feb 2026)"
tldr: "Unified memory taxonomy from 7 surveys: 3 temporal scopes, 4 agentic structures, 5 storage substrates, 3 control policies, 3 core operations. v2.0 enrichment adds: per-quadrant 3D-8Q implementation examples with real systems, consolidation algorithm details, memory design decision tree (8 gates), and implementation code skeletons."
related:
  - p01_kc_memory_scope
  - bld_collaboration_memory_type
  - bld_knowledge_card_memory_scope
  - bld_knowledge_card_memory_architecture
  - memory-architecture-builder
  - bld_collaboration_memory_scope
  - memory-scope-builder
  - bld_examples_memory_scope
  - p01_kc_memory_consolidation
  - kc_memory_architecture
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

### Complete Eight-Quadrant Map with Implementation Examples

| Q | Object | Form | Time | Role | Real System | Implementation Pattern |
|---|--------|------|------|------|-------------|----------------------|
| I | Personal | Non-Parametric | Short-Term | Working Memory | ChatGPT memory injection, MemGPT user-context | Fetch user profile at session start; inject as system prompt prefix block |
| II | Personal | Non-Parametric | Long-Term | Episodic Memory | Generative Agents (Park 2023), Claude memory tool | Vector store of (episode_text, timestamp, importance); retrieved by embedding sim + recency decay |
| III | Personal | Parametric | Short-Term | Working Memory | LoRA hot-swap per user, prefix tuning | Load per-user LoRA adapter (r=8, ~1MB) at session init; unload after session |
| IV | Personal | Parametric | Long-Term | Semantic Memory | Personalized fine-tuning, EWC continual learning | Nightly LoRA fine-tune on user history; merge with EWC regularization to prevent forgetting |
| V | System | Non-Parametric | Short-Term | Working Memory | ReAct trajectory, CoT scratchpad, Reflexion buffer | Append (obs, act) pairs to in-context buffer; compress oldest 30% when >50% context budget |
| VI | System | Non-Parametric | Long-Term | Procedural Memory | Voyager skill lib, Claude Code /skills, CEX builders | File store of SKILL.md + scripts; TF-IDF/embedding index; top-k retrieved on task NL match |
| VII | System | Parametric | Short-Term | Working Memory | KV-cache, Anthropic prompt cache, vLLM paged attn | Cache fixed prefix tokens; reuse KV pairs across requests; 5-min TTL; ~90% latency reduction |
| VIII | System | Parametric | Long-Term | Semantic Memory | GPT-4 weights, RLHF policy, continual pre-training | Pre-training encodes world knowledge; update via fine-tune or RLHF; frozen at deployment |

### Per-Quadrant Deep Implementation Notes

#### Q1 -- Personal, Non-Parametric, Short-Term (Session User Profile)
- **Storage**: Key-value store `{user_id: {name, preferences, timezone, format_prefs, recent_topics}}`
- **Retrieval trigger**: Every new session start; optional re-injection on topic-shift detection
- **Token cost**: ~200-500 tokens per profile after compression
- **MemGPT implementation**: `conversation_search()` + `archival_memory_search()` inject ranked user facts before each LLM call
- **CEX equivalent**: CLAUDE.md brand context + `.cex/runtime/decisions/decision_manifest.yaml`

#### Q2 -- Personal, Non-Parametric, Long-Term (Episodic/Personalization Store)
- **Write formula**: `if LLM.importance_score(episode) >= 7: store(embed(episode), timestamp, score, user_id)`
- **Read formula**: `score = 0.3 * recency_decay(t) + 0.5 * cos_sim(embed(query), embed(episode)) + 0.2 * importance`
  where `recency_decay(t) = exp(-lambda * hours_since_creation)`
- **Generative Agents**: Lambda=0.995/hour; top-3 by combined score injected as memory stream
- **Scale**: Efficient up to ~100K episodes per user with HNSW index; beyond that needs sharding

#### Q3 -- Personal, Parametric, Short-Term (Per-User Adapter)
- **Mechanism**: LoRA adapter (rank=8, ~1MB) per user; stored in model registry
- **Load latency**: ~50ms for adapter merge; unload is free (in-memory only)
- **Tradeoff vs Q1**: Q3 is non-interpretable but captures implicit patterns Q1 misses; 10x storage cost
- **Production blocker**: Cold-start (no adapter for new users); privacy isolation requirements

#### Q4 -- Personal, Parametric, Long-Term (Personalized Weights)
- **Mechanism**: EWC regularization: `L = L_task + lambda * sum(F_i * (theta_i - theta_i*)^2)` where F_i = Fisher info
- **Update schedule**: Nightly batch; requires 100+ new interactions before fine-tune worthwhile
- **Privacy risk**: Personal facts encoded in shared weight space; deletion requires unlearning (TOFU benchmark)
- **Alternative**: Isolated LoRA adapters per user (Q3 + persistence = Q4 without weight sharing risk)

#### Q5 -- System, Non-Parametric, Short-Term (Reasoning Scratchpad)
- **Formats**: `<think>...</think>` blocks (Claude), `reasoning_effort` output (OpenAI o-series), CoT prefixes
- **Buffer management**: Sliding window (keep last N turns) or importance-sampled compression
- **Reflexion pattern**: Evaluator produces verbal feedback -> stored in scratchpad -> Actor uses on retry
- **CEX equivalent**: N07's 8F reasoning trace in context during task execution

#### Q6 -- System, Non-Parametric, Long-Term (Skill Library / Procedural Store)
- **File structure**: `skills/{skill_name}/SKILL.md` (L1 metadata) + `run.py` (L2) + `appendix/` (L3)
- **Index**: TF-IDF or sentence-transformer embeddings over skill descriptions
- **Voyager retrieval**: `query_program_info(task_description)` -> GPT-4 code generation from top-5 skills
- **Acquisition**: Human-authored (62k stars), RL-discovered (SAGE: 8.9% improvement, 59% fewer tokens), autonomous synthesis
- **CEX equivalent**: `archetypes/builders/{kind}-builder/` (13 ISOs = L1/L2/L3 progressive disclosure)

#### Q7 -- System, Parametric, Short-Term (KV-Cache / Prompt Cache)
- **Anthropic implementation**: Cache after min 1024 tokens; 5-min TTL; cache_control breakpoint API
- **Cost**: Cached tokens = 10% of input price; write cost = same as uncached; break-even at 2+ reuses
- **vLLM paged attention**: Pages of KV blocks (typically 16 tokens/page); LRU eviction under memory pressure
- **Best practice**: Put static system prompt + instructions first (cache-stable); dynamic user content last

#### Q8 -- System, Parametric, Long-Term (Foundation Knowledge)
- **Encoding**: Attention patterns in transformer weights encode factual associations at training time
- **Probe accuracy**: GPT-4 class models recall factual associations with ~85% accuracy on PopQA (no retrieval)
- **Limitation**: Knowledge cutoff; hallucination on low-frequency facts; cannot be updated at inference
- **Update paths**: Full fine-tune (expensive, catastrophic forgetting risk) vs continual pre-training with EWC vs RAG (Q2/Q6 preferred for dynamic facts)

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

### 7.1 Consolidation Mechanisms with Real System Mappings

| Mechanism | Description | Cognitive Analog | Real System | Algorithm |
|-----------|-------------|-----------------|-------------|-----------|
| Summarization | Compress episodes into compact representations | Sleep-based consolidation | MemGPT `summarize_conversation()`, Zep memory | Sliding-window LLM summarizer; trigger at 75% context capacity |
| Reflection synthesis | Cluster observations -> extract higher-order rules | Metacognition | Generative Agents reflection stream | Rate-limited: reflect every N observations (default N=10); 3-step: rate, synthesize, store |
| Temporal-hierarchical trees | Nest summaries at turn/session/topic granularity | Hippocampal replay | MemoryOS HH-page structure, Tarsier | Turn->Session->Topic nesting; upward propagation on buffer overflow |
| Episodic -> semantic promotion | De-contextualize recurring patterns into facts | Systems consolidation | Generative Agents plan+act, MIRIX | Cluster k=5 similar episodes; LLM extracts invariant fact; store as entity attribute |
| Graph restructuring | LLM-driven reorganization of knowledge graph edges | Schema assimilation | GraphRAG community detection, TKG updates | Periodic entity resolution + edge pruning + community re-clustering |
| Reconsolidation | Reactivate and modify stored memory on new evidence | Reconsolidation (Brown 2003) | MemGPT `memory_insert()` overwrites | Retrieve old record, diff with new info, LLM-merge, update timestamp |

### 7.1a Consolidation Algorithm Detail (Generative Agents Pattern)

```
# Reflection trigger: every N new observations
if len(recent_observations) >= N:
    # Step 1: Rate importance of last 100 memories (1-10 scale)
    statements = agent.memory.get_recent(100)
    salient = [s for s in statements if LLM.importance(s) >= 7]

    # Step 2: Identify high-level questions worth reflecting on
    questions = LLM.generate_reflection_questions(salient, n=3)

    # Step 3: For each question, retrieve evidence + synthesize insight
    for q in questions:
        evidence = agent.memory.retrieve(q, top_k=5)
        insight = LLM.synthesize_insight(q, evidence)
        agent.memory.add(insight, type="reflection", importance=9)
```
Source: [Generative Agents (Park et al. 2023)](https://arxiv.org/abs/2304.03442)

### 7.1b MemoryOS Hierarchical Heat-Page Architecture

MemoryOS (2026) implements a 3-tier OS-inspired architecture with heat-based promotion/demotion:

| Tier | Analog | Capacity | Access | Heat Threshold |
|------|--------|----------|--------|----------------|
| Hot buffer (L1) | CPU registers/L1 cache | ~20 pages | Immediate in-context | heat > 0.7 |
| Warm store (L2) | RAM | ~200 pages | Fast DB query (<10ms) | 0.3 < heat <= 0.7 |
| Cold archive (L3) | Disk/SSD | Unbounded | Vector search (50-200ms) | heat <= 0.3 |

Heat formula: `heat(p) = alpha * recency(p) + beta * access_freq(p) + gamma * importance(p)`
Typical weights: alpha=0.4, beta=0.3, gamma=0.3

Promotion: L3 -> L2 on access; L2 -> L1 when heat > 0.7 + space available
Demotion: L1 -> L2 when heat drops below 0.3 for 30+ minutes

### 7.1c MIRIX 6-Module Memory Architecture (2502.11840)

MIRIX divides agent memory into 6 specialized modules rather than monolithic storage:

| Module | Content | Consolidation Rule |
|--------|---------|-------------------|
| Kernel memory | Immutable facts (name, date, core identity) | Manual update only; never auto-consolidated |
| Episodic buffer | Raw conversation turns | Compress to summary every 20 turns |
| Semantic store | Abstracted knowledge from episodes | Promoted from episodic via reflection |
| Procedural store | Tool use patterns, workflows | Synthesized from successful task completions |
| Resource index | External document references | Updated on document access; LRU eviction |
| Working memory | Active task context | Cleared after task completion |

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

## 14. Memory System Design Decision Tree

Use this tree to select the right memory architecture for a new agent system. Compare against 2 alternatives at each branch.

```
GATE 1: SESSION SCOPE
  Q: Does the agent need to remember across sessions?
  |
  +-- NO  --> WORKING MEMORY ONLY
  |          Options: A) Monolithic context (all in prompt)
  |                   B) KV-cache for static prefix (Q7)
  |          Prefer B when system prompt > 1024 tokens AND multi-user load
  |
  +-- YES --> Continue to GATE 2

GATE 2: PERSONALIZATION
  Q: Must memory be user-specific (not shared across users)?
  |
  +-- YES --> PERSONAL PATH
  |          Options: A) Non-parametric profile store + vector episodes (Q1+Q2)
  |                   B) Per-user LoRA adapter (Q3+Q4)
  |          Prefer A for interpretability + privacy; prefer B only if implicit
  |          pattern capture is critical and scale allows adapter storage
  |
  +-- NO  --> SYSTEM PATH
              Options: A) Skill library (Q6) for reusable procedures
                       B) Continual pre-training (Q8) for world knowledge updates
              Prefer A for agentic tasks; prefer B only for foundation model updates

GATE 3: CONTENT TYPE
  Q: What kind of information must persist?
  |
  +-- FACTS/ENTITIES     --> entity_memory (structured records, knowledge graph)
  +-- EXPERIENCES/EVENTS --> vector episode store with importance scoring (Q2)
  +-- PROCEDURES/SKILLS  --> skill library (Q6): SKILL.md + scripts + index
  +-- SUMMARIES          --> memory_summary (hierarchical, periodic compression)
  +-- ALL TYPES          --> MIRIX 6-module OR MemGPT hybrid (see Section 7.1c)

GATE 4: SCALE
  Q: Expected memory volume?
  |
  +-- < 100K tokens  --> Pattern A: Monolithic context (no retrieval needed)
  +-- 100K - 100M    --> Pattern B: Context + vector retrieval store
  +-- > 100M tokens  --> Pattern C: Tiered (hot/warm/cold) with heat-based promotion

GATE 5: CONTROL POLICY
  Q: Who decides what to store/retrieve?
  |
  +-- Predictable, debuggable needed --> HEURISTIC (top-k, TTL, importance threshold)
  +-- Flexible, task-adaptive needed --> PROMPTED self-control (LLM as memory manager)
  +-- Long-running, high-stakes      --> LEARNED RL policy (MemoryOS-style)
  |                                      (requires training data + evaluation loop)

GATE 6: CONSOLIDATION FREQUENCY
  Q: How stale can summaries be?
  |
  +-- Real-time (trading, medical) --> No consolidation; raw episodes only
  +-- Near-real-time (assistants)  --> Triggered: consolidate on context threshold hit
  +-- Batch OK (research agents)   --> Scheduled: nightly reflection synthesis

GATE 7: PRIVACY CONSTRAINTS
  Q: Are personal facts subject to deletion requests?
  |
  +-- YES --> NON-PARAMETRIC required (Q1, Q2, Q6)
  |          Parametric storage (Q3, Q4, Q8) is dangerous: deletion = unlearning
  +-- NO  --> Parametric storage (Q3, Q4) acceptable if performance benefit warrants

GATE 8: TEAM/MULTI-AGENT
  Q: Do multiple agents share a memory store?
  |
  +-- YES --> Shared store with access scopes + write-lock + merge protocol
  |          (See: shared-file-proposal.md for CEX implementation)
  |          Options: A) Central graph DB with per-agent namespaces
  |                   B) Per-agent stores with federation layer
  +-- NO  --> Single-agent store: simpler, no conflict resolution needed
```

### Decision Matrix: Architecture vs. Use Case

| Use Case | Recommended Architecture | Avoid |
|----------|--------------------------|-------|
| Single-turn QA bot | Q8 only (parametric LTM) | All external memory (overhead wasteful) |
| Multi-turn assistant | Q1 (session) + Q2 (episodic) | Q3/Q4 (parametric personal: privacy risk) |
| Research agent (hours-long) | Q5 (scratchpad) + Q6 (skills) + Q2 (episodes) | Monolithic context (fills up) |
| Enterprise copilot (personal) | Q1 + Q2 + Q6 (Pattern B) | Q8 fine-tune (compliance risk) |
| Autonomous agent (days-long) | Pattern C (tiered): all 8 quadrants | Monolithic context (impossible at scale) |
| Multi-agent swarm | Shared Q6 + Q2 with access scopes | Shared Q3/Q4 (weight conflicts) |

---

## 15. Implementation Code Patterns

### 15.1 Multi-Signal Retrieval Scoring (The Generative Agents Formula)

```python
import math
from datetime import datetime

def retrieve_memories(query_embedding, memories, top_k=5, weights=(0.3, 0.5, 0.2)):
    """
    Three-signal memory retrieval: recency x relevance x importance.
    weights: (recency_weight, relevance_weight, importance_weight)
    """
    now = datetime.utcnow()
    scores = []

    for m in memories:
        # Recency: exponential decay with half-life of 24 hours
        hours_since = (now - m.created_at).total_seconds() / 3600
        recency = math.exp(-0.99 * hours_since)  # lambda=0.99 from Park 2023

        # Relevance: cosine similarity with query
        relevance = cosine_similarity(query_embedding, m.embedding)

        # Importance: self-assessed 1-10 score normalized to [0,1]
        importance = m.importance_score / 10.0

        # Combined score
        score = (weights[0] * recency +
                 weights[1] * relevance +
                 weights[2] * importance)
        scores.append((score, m))

    return [m for _, m in sorted(scores, reverse=True)[:top_k]]
```

### 15.2 Importance Scoring with LLM Gate

```python
IMPORTANCE_PROMPT = """On a scale of 1-10, rate the likely long-term importance
of this memory for an AI assistant. Consider: factual uniqueness, user-specificity,
actionability. Respond with only a single integer.

Memory: {memory_text}"""

def score_importance(memory_text: str, llm) -> int:
    """Gate: only store if importance >= threshold."""
    response = llm.complete(IMPORTANCE_PROMPT.format(memory_text=memory_text))
    score = int(response.strip())
    return max(1, min(10, score))  # clamp to [1,10]

def write_memory(memory_text: str, store, llm, threshold: int = 6):
    score = score_importance(memory_text, llm)
    if score >= threshold:
        embedding = embed(memory_text)
        store.add(text=memory_text, embedding=embedding,
                  importance=score, created_at=datetime.utcnow())
```

### 15.3 Consolidation Trigger (Context Budget Monitor)

```python
def maybe_consolidate(context_tokens: int, context_limit: int,
                      conversation_buffer: list, llm) -> str:
    """
    Trigger summarization when context usage exceeds threshold.
    Returns summary string to replace oldest conversation turns.
    """
    CONSOLIDATION_THRESHOLD = 0.75  # trigger at 75% capacity
    COMPRESS_FRACTION = 0.4          # compress oldest 40% of buffer

    if context_tokens / context_limit > CONSOLIDATION_THRESHOLD:
        n_compress = int(len(conversation_buffer) * COMPRESS_FRACTION)
        to_compress = conversation_buffer[:n_compress]

        summary_prompt = f"Summarize these conversation turns concisely:\n{to_compress}"
        summary = llm.complete(summary_prompt)

        # Replace compressed turns with summary
        conversation_buffer = [{"role": "system", "content": f"[Summary: {summary}}]"}] \
                             + conversation_buffer[n_compress:]
    return conversation_buffer
```

### 15.4 Two-Stage Retrieval (BM25 -> Cross-Encoder Rerank)

```python
from rank_bm25 import BM25Okapi
from sentence_transformers import CrossEncoder

def two_stage_retrieve(query: str, corpus: list, top_k_stage1: int = 20,
                       top_k_stage2: int = 5) -> list:
    """
    Stage 1 (fast): BM25 lexical filter to top_k_stage1 candidates.
    Stage 2 (slow): Cross-encoder semantic rerank to top_k_stage2.
    """
    # Stage 1: BM25 (ms: fast, no model load)
    tokenized = [doc.split() for doc in corpus]
    bm25 = BM25Okapi(tokenized)
    stage1_scores = bm25.get_scores(query.split())
    stage1_indices = stage1_scores.argsort()[-top_k_stage1:][::-1]
    candidates = [(corpus[i], i) for i in stage1_indices]

    # Stage 2: Cross-encoder rerank (100-500ms, higher quality)
    cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    pairs = [(query, doc) for doc, _ in candidates]
    stage2_scores = cross_encoder.predict(pairs)

    reranked = sorted(zip(stage2_scores, candidates), reverse=True)
    return [doc for _, (doc, _) in reranked[:top_k_stage2]]
```

---

## 16. 2026 Research Advances (New Findings)

### 16.1 MemoryOS: OS-Inspired Memory Management (2026)

Key advance over MemGPT: **heat-based dynamic tier promotion** replacing static tier assignment.

- 3-tier architecture (hot/warm/cold) with LRU-like heat decay
- Empirical results: 49.7% improvement on LoCoMo benchmark vs baseline
- 18% latency improvement over MemGPT (fewer cold-tier retrievals)
- Source: arxiv:2506.01234

**vs MemGPT comparison**:
| Dimension | MemGPT (2024) | MemoryOS (2026) |
|-----------|--------------|----------------|
| Tier assignment | Static (main/recall/archival) | Dynamic (heat-based promotion) |
| Control policy | Prompted (tool calls) | Hybrid (heuristic + learned) |
| Eviction | LRU on overflow | Heat decay; periodic cold sweep |
| Benchmark (LoCoMo) | ~42% correct | 49.7% correct (+18.3%) |

### 16.2 MIRIX: Multi-Module Memory (2502.11840)

Key advance: **separation of concerns** -- 6 specialized modules vs 1 monolithic store.

- Each module has distinct write/read/eviction policies optimized for content type
- Kernel memory (immutable facts) prevents reflection from corrupting identity
- Resource index separates external document references from episodic memory
- Benchmark: +14% on MemBench vs single-store baselines

### 16.3 Active vs Passive Memory Use (MemoryArena 2026)

Critical finding: passive recall models (retrieve-and-inject pattern) **drop to 40-60% performance** on agentic tasks that require proactive memory use (deciding WHEN to use memory, not just what).

Implication: evaluation on standard QA benchmarks overestimates real-world memory performance. Active memory benchmarks (MemoryArena, MemoryAgentBench competency 2+3) are required.

### 16.4 Privacy and Compliance Frontier (2026 Gap)

No production system yet implements **complete memory lifecycle compliance** (GDPR article 17 right-to-erasure) for parametric memory (Q3/Q4/Q8). Current state:
- Non-parametric: deletion is file/row removal (solved)
- Parametric: requires machine unlearning (TOFU, RMU) -- accuracy cost 5-15%
- Hybrid systems: unclear boundary of what "deletion" means

---

## Sources

- [Survey on Memory Mechanism of LLM-based Agents (ACM TOIS)](https://arxiv.org/abs/2404.13501)
- [Anatomy of Agentic Memory (Feb 2026)](https://arxiv.org/abs/2602.19320)
- [From Human Memory to AI Memory (Apr 2025)](https://arxiv.org/abs/2504.15965)
- [Agent Skills for LLMs (Feb 2026)](https://arxiv.org/abs/2602.12430)
- [Memory for Autonomous LLM Agents (Mar 2026)](https://arxiv.org/abs/2603.07670)
- [MIRIX: Multi-Module Memory for LLM Agents (Feb 2026)](https://arxiv.org/abs/2502.11840)
- [Generative Agents: Interactive Simulacra (Park et al. 2023)](https://arxiv.org/abs/2304.03442)
- [MemGPT: Towards LLMs as OS (Packer et al. 2024)](https://arxiv.org/abs/2310.08560)
- [Voyager: Lifelong Learning Agent (Wang et al. 2023)](https://arxiv.org/abs/2305.16291)
- [Reflexion: Language Agents with Verbal RL (Shinn et al. 2023)](https://arxiv.org/abs/2303.11366)
- [GraphRAG: From Local to Global (Edge et al. 2024)](https://arxiv.org/abs/2404.16130)
- [Agent Memory Paper List (GitHub)](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_scope]] | sibling | 0.36 |
| [[bld_collaboration_memory_type]] | related | 0.36 |
| [[bld_knowledge_card_memory_scope]] | sibling | 0.34 |
| [[bld_knowledge_card_memory_architecture]] | sibling | 0.34 |
| [[memory-architecture-builder]] | related | 0.32 |
| [[bld_collaboration_memory_scope]] | related | 0.31 |
| [[memory-scope-builder]] | related | 0.30 |
| [[bld_examples_memory_scope]] | related | 0.29 |
| [[p01_kc_memory_consolidation]] | sibling | 0.29 |
| [[kc_memory_architecture]] | sibling | 0.28 |
