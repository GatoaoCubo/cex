---
quality: 7.9
id: kc_pillar_brief_p10_memory_en
kind: knowledge_card
pillar: P10
title: "P10 Memory — Your AI's Hippocampus"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
language: en
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p10, memory, context, rag, session-state, llm-engineering]
tldr: "P10 Memory covers everything an LLM needs to remember across sessions: entity memories, knowledge indexes, user models, learning records, and context compression — the hippocampus of your AI stack."
source_concepts: [kc_lens_index, mentor_context]
related:
  - kc_pillar_brief_p10_memory_pt
  - kc_pillar_brief_p01_knowledge_en
  - kc_pillar_brief_p09_config_en
  - kc_pillar_brief_p11_feedback_en
  - n00_p10_kind_index
density_score: 0.9
---

# P10 Memory — Your AI's Hippocampus: How It Remembers, Forgets, and Learns Over Time

---

## The Universal Principle: The Context Window Is Not Memory

Every AI practitioner who has shipped a production system eventually confronts the same brutal fact: **the context window is not memory. It is a whiteboard that gets erased at the end of every session.** The model does not remember your user from last week. It does not remember the bug it fixed yesterday. It does not remember which approach it already tried and which failed. Each context window is an island.

This is not a failure mode to work around — it is a fundamental constraint to engineer for. The hippocampus metaphor is apt: in humans, the hippocampus does not store long-term memories itself. It coordinates consolidation — taking the day's experiences and encoding the important ones into long-term storage while discarding the noise. P10 Memory is the engineering discipline that builds this consolidation system for AI.

Without P10, every LLM system is amnesiac by default. It can be brilliant within a context window, but that brilliance evaporates. With P10 properly engineered, your AI accumulates intelligence over time: it remembers what users prefer, it learns from past failures, it avoids repeating mistakes, it builds richer representations of recurring entities. It becomes more capable with every interaction rather than starting from zero.

This is universal. Memory management appears in LangChain as `ConversationBufferMemory`, `ConversationSummaryMemory`, `VectorStoreRetrieverMemory`. In LlamaIndex as `ChatMemoryBuffer`, `SemanticSplitterNodeParser`. In OpenAI's system as persistent instructions. In Anthropic's as persistent artifacts across Projects. The names differ; the underlying problem is identical: **how do you give a stateless model the illusion — and eventually the substance — of persistent intelligence?**

P10's 19 kinds provide a systematic answer, organized around a single primary LLM function: **INJECT**. Memory artifacts exist to be loaded into context at the right moment so the model has what it needs before generating a response. The architecture problem is not storage — any key-value store can hold text. The architecture problem is **retrieval timing, compression fidelity, and decay management**.

---

## What This Pillar Does

P10 Memory addresses four distinct memory engineering challenges that every production AI system faces:

**Challenge 1: Cross-session continuity** — How does the model remember what it discussed with user X three sessions ago? Answer: `entity_memory`, `user_model`, `session_backend`.

**Challenge 2: Operational learning** — How does the model accumulate lessons from its own runs rather than repeating the same mistakes? Answer: `learning_record`, `agent_grounding_record`, `procedural_memory`.

**Challenge 3: Context budget management** — The context window has a finite token budget. How do you compress months of history into a few hundred tokens without losing what matters? Answer: `memory_summary`, `compression_config`, `consolidation_policy`, `memory_type`.

**Challenge 4: Retrieval infrastructure** — Memory is useless if it cannot be found. How do you index accumulated knowledge so the right facts load at the right time? Answer: `knowledge_index`, `prompt_cache`, `runtime_state`.

In the 8F pipeline, P10 artifacts are read at F3 INJECT — they are the primary context injection mechanism for cross-session intelligence. Building them (learning records, entity memories, summaries) happens at F3b PERSIST — the sub-step where new knowledge is committed to durable storage after generation.

---

## All 19 Kinds in P10 — Universal Capability Reference

| Kind | Universal Capability | Primary Use Case |
|------|---------------------|-----------------|
| `entity_memory` | Structured persistent facts about a named entity | Customer profiles, product facts, competitor intel |
| `user_model` | Cross-session dialectic user representation | Personalization, preference tracking, adaptation |
| `knowledge_index` | BM25/FAISS search index configuration | Fast retrieval over large memory stores |
| `learning_record` | What worked/failed — operational intelligence | Agent self-improvement, failure avoidance |
| `session_state` | Ephemeral snapshot of current session | Short-term context passing between steps |
| `memory_summary` | Compressed representation of long history | Fitting months of history into a few hundred tokens |
| `runtime_state` | Variable mental state accumulated this session | Routing decisions, accumulated observations |
| `agent_grounding_record` | Per-inference provenance: tools called, chunks used | Auditability, reproducibility, debugging |
| `prompt_cache` | TTL and eviction config for cached prompt/completion pairs | Cost reduction via cache hits |
| `compression_config` | Tool output compression strategy | Preventing context overflow from large tool returns |
| `memory_architecture` | Complete memory system design document | System architecture planning |
| `memory_type` | Classification of memory by source, confidence, decay | Memory taxonomy for retrieval routing |
| `procedural_memory` | Skill and procedure storage/retrieval | How-to knowledge that transfers across sessions |
| `consolidation_policy` | Memory lifecycle management policy | What gets promoted to long-term, what gets pruned |
| `session_backend` | Per-user session persistence backend | Database selection for session storage |
| `model_registry` | Model versioning and artifact tracking | Which model version produced which output |
| `c2pa_manifest` | C2PA content credential for AI-generated media | Content provenance for regulatory compliance |
| `vc_credential` | W3C Verifiable Credential for AI agent identity | Agent identity and attestation |
| `workflow_run_crate` | RO-Crate workflow execution provenance | Scientific reproducibility |

---

## Key Engineering Patterns — Universal, Works With Any AI

### Pattern 1: The Memory Taxonomy (Four Types)

Not all memory is the same. Before engineering any memory system, categorize what you need to store:

| Type | Description | Decay Rate | Storage Format |
|------|------------|------------|---------------|
| **Correction** | "Last time I did X, it produced a wrong result" | Low — semi-permanent | learning_record |
| **Preference** | "This user prefers bullet points over paragraphs" | Medium — 6-12 months | user_model |
| **Convention** | "This codebase uses tabs, not spaces" | None — until changed | entity_memory |
| **Context** | "The current project is a React SPA" | High — session-level | session_state |

The decay rate matters for the retrieval design: permanent conventions should be injected on every call; session context should expire when the session ends; preferences should fade unless reinforced.

**Try this now (any AI):**
Before your next extended project conversation with ChatGPT or Claude, write a 200-word memory context document with these four sections: (1) Facts about the project that never change, (2) Your preferences for how you want responses formatted, (3) Decisions made so far, (4) Current session context. Paste it at the start. Observe the quality difference compared to not having it.

### Pattern 2: Entity Memory — The Relational Knowledge Pattern

An entity memory stores structured facts about a named entity — a person, company, product, or concept — in a format designed for retrieval and update:

```yaml
# Universal entity memory pattern
entity_name: "Acme Corp"
entity_type: company
attributes:
  founded: 2019
  sector: "B2B SaaS"
  hq: "Austin, TX"
  primary_contact: "Sarah Chen, CTO"
  pain_point: "manual compliance reporting"
  budget_range: "$50K-$200K/year"
relationships:
  - entity: "competitor_xyz"
    type: "direct_competitor"
  - entity: "partner_abc"
    type: "integration_partner"
confidence: 0.92
last_updated: "2026-04-22"
```

The key insight: this is not a document. It is a **structured record** where every field is independently updateable. When you learn that Acme Corp moved their HQ, you update one field. When a new CTO takes over, you update `primary_contact`. The entity memory evolves without invalidating the entire record.

**Works with any AI:** any vector database (Pinecone, Chroma, Weaviate, Qdrant) can store entity memories and retrieve them by entity name at the start of a session.

### Pattern 3: Memory Compression — The Hippocampus Consolidation Pattern

A user who has had 500 conversations with your AI has generated ~2 million tokens of session history. You cannot inject all of that into context. But you also cannot discard it. The solution is lossy compression with controlled fidelity:

**Level 1: Recent history** (last 10 turns) — verbatim, injected in full
**Level 2: Session summaries** (this week's sessions) — 100 tokens per session summary
**Level 3: Long-term summaries** (older than 30 days) — 20 tokens of extracted insights only
**Level 4: Entity memories** (permanent facts extracted from history) — structured records, no token decay

This is the `memory_summary` + `consolidation_policy` pattern in practice. The consolidation_policy governs when Level 1 gets promoted to Level 2, when Level 2 gets compressed to Level 3, and what facts get extracted into permanent entity memories before compression discards the original.

```yaml
# consolidation_policy example
session_to_summary_threshold: 10        # after 10 turns, write session summary
summary_to_longterm_threshold: 30d      # after 30 days, compress to long-term
entity_extraction_trigger: "any named entity mentioned 3+ times"
preservation_priority: [corrections, decisions, preferences, context]
```

### Pattern 4: Learning Records — The Self-Improvement Memory

A `learning_record` is the mechanism by which an AI system accumulates operational intelligence from its own runs. Every time a quality gate fails, every time a build approach succeeds, every time a tool call produces an unexpected result — that event should generate a learning record.

```yaml
# learning_record pattern
session_id: "session_20260422_n05"
nucleus: n05
outcome: failure
pattern: "BM25 index requires rebuild after adding new artifact kinds"
evidence: "cex_retriever returned 0 results for compression_config kind until index rebuilt"
applies_to: [knowledge_index, cex_retriever.py]
decay_rate: 0.0   # permanent — this is a system behavior, not a one-time observation
```

The `decay_rate: 0.0` for system behavior observations is critical. A learning that "exponential backoff needs 2s base, not 1s" is permanently true about the provider's behavior. But a learning that "user X preferred shorter responses in Q1" might decay by Q3 as preferences shift.

### Pattern 5: User Model — The Honcho Pattern

The most powerful memory pattern for user-facing AI systems is the cross-session user representation, sometimes called the Honcho pattern (from the open-source project by Plastic Labs). The idea: after every session, the AI extracts a structured representation of what it learned about this specific user — and injects that representation at the start of every future session.

```yaml
# user_model pattern
peer_id: "user_gato3"
communication_style: "terse, technical, autonomous"
domain_expertise: ["prompt engineering", "Python", "distributed systems"]
preferences:
  response_format: "tables over prose, bullet points for lists"
  language: "pt-br primary, EN for technical terms"
  decision_style: "wants options, decides fast, no over-explanation"
corrections_applied: ["never ask for confirmation on standard builds", "skip preamble"]
session_count: 47
last_interaction: "2026-04-22"
```

This user model gets richer with every session. By session 47, the AI has a highly calibrated representation of this specific user that dramatically improves response relevance — without any fine-tuning, without any model changes. Pure engineering.

### Pattern 6: Prompt Cache — The Cost Engineering Pattern

Prompt caching is the P10 mechanism with the highest immediate ROI. Every time your AI calls an LLM with the same system prompt + tool definitions preamble, you are paying for the same tokens repeatedly. Prompt caching reduces this to near-zero for the repeated portion.

```yaml
# prompt_cache configuration
ttl_seconds: 300              # 5-minute cache TTL matches Anthropic's cache window
eviction_strategy: lru        # evict least-recently-used when full
max_entries: 100
cache_key_method: content_hash
invalidation_trigger: "system_prompt_change"
storage_backend: redis        # local memory, Redis, or Memcached
```

At scale (a 100-agent grid), the savings from prompt caching are substantial: a 10K-token system prompt hit 100 times per session costs $0.30 uncached. With 5-minute TTL caching and 80% hit rate, that drops to $0.06. Multiply across all nuclei and daily runs.

---

## Architecture Deep Dive

### The Memory Stack — Four Layers

Production memory systems have four distinct architectural layers:

```
Layer 4: RETRIEVAL LAYER
         knowledge_index (BM25/FAISS)
         runtime_state (routing decisions)
              |
              v
Layer 3: COMPRESSION LAYER
         memory_summary (compressed history)
         compression_config (how to compress)
         consolidation_policy (when to promote/prune)
              |
              v
Layer 2: STORAGE LAYER
         entity_memory (structured facts)
         user_model (user representation)
         learning_record (operational intelligence)
         procedural_memory (skill storage)
         session_backend (database)
              |
              v
Layer 1: SESSION LAYER
         session_state (ephemeral, current session)
         prompt_cache (active cache)
         agent_grounding_record (current inference provenance)
```

The data flow: session layer captures events in real time. Compression layer consolidates them periodically. Storage layer persists the important artifacts. Retrieval layer makes them findable.

### Memory Boundary Violations — The Most Common Mistakes

| Conflation | Why It's Wrong | Correct Separation |
|------------|---------------|-------------------|
| Treating `session_state` like permanent storage | Sessions are ephemeral — server restart destroys them | Use `entity_memory` for facts you need next week |
| Using `knowledge_card` (P01) for user-specific facts | Knowledge cards are domain knowledge, not user state | `user_model` for user-specific, `entity_memory` for entity facts |
| Storing `runtime_state` without decay policy | Runtime state from yesterday is stale | Apply decay: 24-48h TTL on runtime observations |
| Skipping `agent_grounding_record` | No auditability when the AI produces a wrong answer | Record provenance at every inference |
| Compressing too aggressively | Over-compression loses critical context | Test compression fidelity against a holdout set before deploying |

### The Provenance Layer — New in P10

Three kinds in P10 address a growing regulatory and operational need: **provenance** — knowing exactly what data, model version, and tool calls produced a given AI output.

- `agent_grounding_record`: per-inference record of every RAG chunk used, every tool called, model version, and confidence scores
- `c2pa_manifest`: Coalition for Content Provenance and Authenticity manifest for AI-generated media
- `workflow_run_crate`: RO-Crate 1.2 format for scientific workflow reproducibility

These are not operational for every use case, but they are mandatory for regulated industries (healthcare, finance, legal) and increasingly expected by enterprise buyers.

---

## Real Examples from N00_genesis

### entity_memory in practice

File: `N00_genesis/P10_memory/ex_entity_memory_partner_profile.md`

A partner profile entity memory accumulates: company name, sector, primary contact, pain points, budget range, integration status, and last interaction date. Each session adds or updates fields. The AI never asks "can you remind me which company you're from?" — it already knows, because the entity memory was injected at session start.

### learning_record in practice

File: `N00_genesis/P10_memory/kind_learning_record/kind_manifest_n00.md`

The CEXAI system generates learning records after every quality gate failure and successful novel pattern discovery. Example pattern captured: "BM25 index misses new P10 artifacts if rebuild not triggered." This becomes a permanent reminder injected before every retrieval-related build task, preventing the same mistake from occurring twice.

### user_model structure

File: `N00_genesis/P10_memory/tpl_user_model.md`

The user model template captures: peer_id, communication style, domain expertise, format preferences, correction history, and session count. In CEXAI, N07 maintains a user_model for the operator that accumulates preferences over time — "never ask for GDP confirmation on standard builds," "prefer tables over prose," "terse English or PT-BR."

---

## Anti-Patterns — Universal Memory Engineering Mistakes

**Anti-pattern 1: Context stuffing**
Injecting the entire session history verbatim into every context window. At 200 sessions × 4K tokens each, that is 800K tokens — impossible on any model with a 200K context limit. Use `memory_summary` compression instead.

**Anti-pattern 2: One memory type for everything**
Mixing user preferences, entity facts, operational learnings, and session state into a single untyped blob. When you need to update one type, you have to parse the entire blob. Use the four-type taxonomy: correction, preference, convention, context.

**Anti-pattern 3: No decay policy**
Storing memories without expiration. A user preference from 18 months ago may no longer be valid. Operational learnings about a provider's behavior may change with API updates. Every memory artifact should declare a decay_rate or TTL.

**Anti-pattern 4: Retrieval by recency only**
Loading the most recent N memories regardless of relevance to the current query. A session about React components should not inject memories about Kubernetes configuration. Use semantic search (FAISS) or BM25 for relevance-ranked retrieval.

**Anti-pattern 5: No provenance on AI outputs**
Deploying AI in regulated contexts without `agent_grounding_record`. When the AI produces a wrong output, you need to know: what RAG chunks did it use? What was the model version? What tool did it call? Without provenance, root-cause analysis is guesswork.

**Anti-pattern 6: Forgetting to consolidate**
Accumulating session states without a consolidation policy. After 100 sessions, you have 100 ephemeral state blobs that should have been distilled into 10 entity memories and 5 learning records. Run consolidation after every session batch.

---

## Cross-Pillar Connections

Memory sits at the center of the 12-pillar system because intelligence requires both knowledge (P01) and memory (P10). The critical distinction:

| P01 Knowledge | P10 Memory |
|--------------|-----------|
| Domain facts — universal truths | Session facts — specific to this user/system |
| Never expires (until the world changes) | Decays over time |
| Shared across all users | Per-user or per-agent |
| RAG retrieval | Personalized injection |

| P10 feeds | To pillar | What it provides |
|----------|-----------|-----------------|
| User preferences | P02 | Agent adapts persona to known user |
| Operational learnings | P11 | Feedback loop consumes learning records |
| Provenance records | P07 | Evaluation uses grounding records as ground truth |
| Session state | P12 | Orchestrator reads runtime_state when planning next steps |

| P10 consumes | From pillar | What it uses |
|-------------|-------------|-------------|
| Knowledge cards | P01 | Seed entity memories from domain KC content |
| Quality scores | P11 | Quality gate outcomes generate learning records |
| Tool call results | P04 | Tool outputs feed compression_config |
| Workflow events | P12 | Checkpoint data populates workflow_run_crate |

---

## Try This Now — P10 Exercises for Any AI System

**Exercise 1: Entity Memory for Your Top 5 Customers (45 minutes)**
For your five most important customers/partners, write structured entity memory files. Include: company name, sector, primary contact, pain points, status, last interaction. Before your next customer-facing AI interaction, inject the relevant entity memory into the system prompt. Measure the improvement in response relevance.

**Exercise 2: Operational Learning Review (30 minutes)**
Think about the last 3 times your AI system produced a wrong or suboptimal result. For each: write a `learning_record` documenting the pattern and evidence. Add these as persistent context to your system prompt. Observe whether the same failures recur.

**Exercise 3: Memory Type Audit (1 hour)**
Survey everything your AI system currently "knows" about users and context. Categorize each piece of knowledge as: correction, preference, convention, or context. Assign decay rates. Remove anything that is stale. Notice how much of what you thought was "memory" was actually just unexamined context clutter.

**Exercise 4: Session Compression Design (2 hours)**
Design a consolidation policy for a system with 100+ sessions per user. Define: what triggers a session summary, what summary format captures maximum information per token, what triggers promotion to long-term entity memory. Implement a manual version using any LLM.

---

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_pillar_brief_p10_memory_pt]] | sibling (PT-BR) | 1.00 |
| [[kc_pillar_brief_p01_knowledge_en]] | upstream | 0.52 |
| [[kc_pillar_brief_p09_config_en]] | upstream | 0.45 |
| [[kc_pillar_brief_p11_feedback_en]] | downstream | 0.50 |
| [[kc_pillar_brief_p12_orchestration_en]] | downstream | 0.44 |
| [[n00_p10_kind_index]] | upstream | 0.70 |
| [[n00_entity_memory_manifest]] | upstream | 0.55 |
| [[n00_learning_record_manifest]] | upstream | 0.52 |
| [[mentor_context]] | upstream | 0.42 |
