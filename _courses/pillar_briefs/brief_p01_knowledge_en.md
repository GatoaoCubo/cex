---
quality: 8.1
id: kc_pillar_brief_p01_knowledge_en
kind: knowledge_card
pillar: P01
title: "P01 Knowledge — The Foundation Layer"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
language: en
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p01, knowledge, rag, embeddings, chunking, llm-engineering]
tldr: "Deep technical brief on P01 Knowledge: 30 kinds covering RAG, embeddings, chunking, knowledge graphs — universal LLM engineering patterns."
source_concepts: [kc_lens_index, mentor_context]
related:
  - kc_pillar_brief_p01_knowledge_pt
  - kc_pillar_brief_p02_model_en
  - cm_driver_01_structured_thinking
  - kc_lens_factory
  - kc_lens_index
updated: "2026-04-22"
---

# P01 Knowledge — The Foundation Layer: How LLMs Know What They Know

---

## The Universal Principle: Your AI Has Amnesia

Here is the most important thing to understand about any AI system you work with — ChatGPT, Claude, Gemini, a local Ollama model, anything: **it forgets everything between sessions.** Not partially. Completely. Every conversation starts from the same blank slate.

This is not a bug. It is a fundamental architectural property of transformer-based language models. The model's weights encode general language understanding built during training. But your specific facts — your product pricing, your company policies, your research findings, your customer history — exist nowhere in that model unless you put them there, every single time.

P01 Knowledge is the engineering discipline that solves this problem. The metaphor that sticks: **an AI without organized knowledge is a genius with amnesia — brilliant, capable of extraordinary reasoning, but starting from zero every single conversation.** P01 is the system that gives the genius a filing cabinet, a search engine, and a way to find the right facts before answering.

This is not a CEXAI-specific problem. It is universal. The same patterns — knowledge cards, RAG pipelines, embedding configs, retrieval tuning — appear in LangChain, LlamaIndex, Haystack, and every serious LLM production deployment. CEXAI's 12-pillar taxonomy gives these patterns canonical names and quality gates, but the underlying engineering applies whether you are using a $20/month ChatGPT subscription or a $200K enterprise deployment.

**The practical upshot:** if your AI is hallucinating, the root cause is almost always a P01 problem. The model is guessing because it does not have the right knowledge in its context window when it generates a response.

---

## What This Pillar Does

P01 Knowledge is the memory substrate of any LLM-based system. Where P03 governs what an agent *says*, P02 governs what an agent *is*, P01 governs what an agent *knows*. Without P01, every LLM call starts from scratch — hallucination fills the gap where knowledge should be. With P01 properly populated, the model operates on a curated, versioned, searchable corpus of distilled facts that it would otherwise lack or misremember.

In the 12-pillar CEXAI taxonomy, P01 is the furthest upstream: it feeds every other pillar. Prompt templates (P03) need domain knowledge injected into them. Agents (P02) need context about their domain loaded at boot. Evaluators (P07) need ground truth to compare against. Orchestrators (P12) need mission-relevant facts to plan waves intelligently. Everything that makes a language model produce reliable, domain-specific output flows from what you put into P01.

The pillar maps to one dominant LLM function: **INJECT**. In the 8F pipeline, INJECT is F3 — loading context into the model's working window before generation. Every P01 artifact is, at its core, a unit of injectable knowledge: dense, versioned, retrievable, bounded.

In framework-neutral terms, P01 answers three questions:

- **What facts do we have?** — `knowledge_card`, `context_doc`, `glossary_entry`, `citation`
- **How do we retrieve them?** — `chunk_strategy`, `embedding_config`, `retriever_config`, `vector_store`, `reranker_config`, `embedder_provider`
- **How do we structure them relationally?** — `knowledge_graph`, `ontology`, `graph_rag_config`, `agentic_rag`

The distinction between *content kinds* (the facts themselves) and *runtime kinds* (retrieval infrastructure) is critical for system design. Content kinds are written by humans or distilled by agents from external sources. Runtime kinds configure the machinery that makes content findable.

> **Why this matters for you:** Companies using structured knowledge bases with their AI report 40-60% fewer "I don't know" or hallucinated responses. The difference between a generic AI answer and a domain-expert AI answer is almost always whether you have invested in P01.

---

## The 30 Kinds in P01 — Reframed as Universal Capabilities

Instead of listing CEXAI kind names in isolation, here is each major capability explained as a universal LLM engineering concept — with a practical example you can try with any AI you already have.

### Core Content Kinds — The Knowledge Itself

| Kind | Universal Capability | Works With Any AI? |
|------|---------------------|-------------------|
| `knowledge_card` | Structured fact storage — one atomic, searchable fact per unit | Yes — ChatGPT, Claude, Gemini, local models |
| `context_doc` | Broad background injection — domain overview for prompt hydration | Yes — paste as context in any chat |
| `glossary_entry` | Term definitions — ensures AI uses your vocabulary, not generic terms | Yes — include in system prompt |
| `citation` | Grounded claims — every fact tied to a verifiable source | Yes — prevents hallucination at the root |
| `few_shot_example` | In-context learning — showing the AI exactly what format you want | Yes — the most universal LLM technique |
| `rag_source` | Live data pointers — URL + freshness metadata for external indexing | Yes — any RAG implementation |
| `dataset_card` | Dataset documentation — HuggingFace-style for fine-tuning or eval sets | Yes — standard across ML frameworks |
| `faq_entry` | Q&A pairs — canonical answers for support deflection | Yes — the simplest form of knowledge base |

**Try it now — Knowledge Card pattern with any AI:**
Open ChatGPT or Claude. Paste this:

> "I'm going to give you facts about my business. Store each as a separate, searchable fact with a category. Here is fact 1: Our refund policy allows returns within 30 days of purchase, no questions asked. Category: Policy."

You just created a knowledge card system in a single prompt. The category label is your retrieval tag. The separation of facts is your chunking. The "no questions asked" specificity is your density requirement. CEXAI formalizes this into a typed artifact with quality gates — but the concept works anywhere.

### RAG Infrastructure Kinds — The Retrieval Machinery

| Kind | Universal Capability | The Engineering Problem It Solves |
|------|---------------------|----------------------------------|
| `chunk_strategy` | How to feed long documents to AI | You cannot paste a whole book — you paste the right paragraph |
| `embedding_config` | How AI understands meaning, not just words | Semantic search finds "shipping complaint" even when the word "shipping" does not appear |
| `embedder_provider` | Which vector model to use | OpenAI, Cohere, Ollama (free local), Voyage — each with tradeoffs |
| `retriever_config` | Search tuning — recall vs precision | BM25 for exact terms; dense vectors for semantic; hybrid for production |
| `reranker_config` | Precision improvement after initial retrieval | Filters 20 candidates down to the 5 that actually answer the question |
| `vector_store` | Where vectors live | pgvector, Chroma, FAISS, Qdrant — persistence layer decisions |
| `graph_rag_config` | Relational knowledge retrieval | When "find similar documents" is not enough — you need "find documents connected to X via relationship Y" |
| `agentic_rag` | Agent-controlled retrieval loops | Multi-hop reasoning: find A, use A to find B, use B to answer |

**Try it now — RAG with zero code:**
Upload a PDF to Claude. Ask a question about it. That IS RAG — Retrieval Augmented Generation. The AI retrieved relevant chunks from your document and augmented its generation with them. The difference between that free-tier experience and a production RAG system is: (1) scale — thousands of documents, not one PDF; (2) precision — tuned chunking and reranking; (3) freshness — automated re-indexing when sources change.

**Try it now — Chunk Strategy intuition:**
Take a 10-page document. Paste all 10 pages into ChatGPT and ask a specific question. Then paste only the 2 paragraphs most relevant to that question and ask the same question. The focused version almost always wins. That is chunking — the discipline of feeding the RIGHT content, not all content.

**Try it now — Semantic Search intuition:**
Ask Claude: "Find anything related to customer frustration with delivery times." Watch it surface passages about logistics, fulfillment, wait times, and shipping — even when none of those passages use the exact phrase "delivery times." That is semantic search via embeddings. The AI understands meaning, not just character patterns.

### Structured Knowledge Kinds — Ontologies and Graphs

| Kind | Universal Capability | When Flat Search Fails |
|------|---------------------|----------------------|
| `knowledge_graph` | Entity + relationship maps | "What companies did OpenAI acquire?" requires traversal, not similarity search |
| `ontology` | Formal taxonomy — controlled vocabulary | Prevents the AI from using "customer" and "client" and "user" as synonyms |
| `repo_map` | Code-aware context extraction | Navigating large codebases for code-aware RAG |

### Vertical Industry Templates — Domain Compliance Pre-built

These are scaffolds, not generic documents. Each encodes the compliance patterns, integration standards, and domain vocabulary for a specific industry:

| Template | What It Pre-encodes |
|----------|---------------------|
| `ecommerce_vertical` | PCI-DSS patterns, cart abandonment, recommendation engine structures |
| `fintech_vertical` | SOC2, KYC/AML, fraud detection patterns |
| `healthcare_vertical` | HIPAA, HL7/FHIR, PHI handling rules |
| `legal_vertical` | Privilege rules, billable hour structures, contract analysis patterns |

> **Real-world impact:** A healthcare AI without `healthcare_vertical` knowledge will give generic answers about patient data. With it loaded, it knows HIPAA's minimum necessary standard, the difference between PHI and de-identified data, and which fields trigger disclosure rules. That is the difference between a demo and a deployable system.

### Commercial Intelligence Kinds

| Kind | Universal Capability |
|------|---------------------|
| `competitive_matrix` | Battle cards — feature comparison for sales enablement |
| `discovery_questions` | MEDDIC/BANT question banks for structured prospect qualification |
| `lineage_record` | Provenance chains — how was this knowledge derived? |
| `domain_vocabulary` | Canonical term registry — enforcing consistent language across a system |

---

## Key Engineering Patterns

### The knowledge_card as the Atomic Unit

The `knowledge_card` (KC) is the foundational artifact of P01. Everything else in P01 either feeds into KCs or serves to make them retrievable.

A KC has strict constraints:
- **max_bytes: 5120** — forces density, prevents bloat
- **density_score >= 0.8** — every sentence must carry non-obvious information; no filler
- **13 required frontmatter fields**: `id`, `kind`, `pillar`, `title`, `version`, `created`, `updated`, `author`, `domain`, `quality`, `tags`, `tldr`, `when_to_use`
- **naming pattern**: `p01_kc_{topic}.md` with a compiled `.yaml` sibling

Three KC subtypes exist with distinct body structures:
- **domain_kc**: vertical knowledge (quick_reference, key_concepts, golden_rules, visual_flow)
- **meta_kc**: cross-cutting system knowledge (executive_summary, patterns, anti_patterns, application)
- **kind_kc**: meta-knowledge about a CEXAI kind itself (spec, cross_framework_map, decision_tree)

The `tldr` and `title` fields are the primary BM25 ranking signals. Each `## ` heading defines an embedding chunk boundary. This means KC structure directly affects retrieval quality — poorly structured KCs are hard to find even when their content is correct.

**The universal lesson:** structured fact storage beats unstructured text at scale. When you have 5 facts in a system prompt, unstructured works fine. When you have 500 facts, you need a retrieval system that can find the right 5 from the 500. That is when KCs become essential.

Cross-references via `linked_artifacts` and `related` fields turn the KC corpus into a traversable graph. The CEXAI repo's `cex_retriever.py` currently uses TF-IDF over 2,184 documents with a 12K vocab; vector-backed retrieval is the upgrade path.

### The RAG Pipeline: Three Kinds as One System

The minimal RAG stack in P01 is three kinds working together:

```
chunk_strategy + embedding_config + retriever_config = RAG pipeline
```

1. **chunk_strategy** decides *how* to split documents before indexing. The canonical example in the CEXAI repo (`ex_chunk_strategy_recursive_1000.md`) uses RecursiveCharacterTextSplitter with `chunk_size=1000`, `chunk_overlap=200`, and markdown-aware separators (`\n## `, `\n### `, `\n#### `). It counts tokens with tiktoken (cl100k_base), not characters — alignment with the embedding model matters. Benchmarks on the repo corpus show 0.89 recall@5 with this config vs 0.81 without the 20% overlap.

2. **embedding_config** specifies the model, dimensions, and any provider-specific settings. The nomic-embed-text example in the repo uses 768 dimensions and runs locally via Ollama at zero API cost. Changing the embedding model requires a full reindex — this is a schema-level decision, not a runtime toggle.

3. **retriever_config** is where recall/precision tradeoffs are made. The hybrid retrieval pattern from `ex_retriever_config_hybrid_rag.md` combines BM25 (weight 0.3) for exact-term queries with FAISS dense search (weight 0.7) for semantic queries. A Cohere reranker narrows 20 initial candidates to the final top_k=5, delivering +12% MRR@5 vs no reranker. The fallback chain is explicit: Ollama down → BM25-only (recall drops ~50%); Cohere API down → RRF top 5, MRR@5 drops 12%.

This three-kind pattern maps directly to every major LLM engineering framework:

| P01 Kind | LangChain equivalent | LlamaIndex equivalent |
|----------|---------------------|----------------------|
| `chunk_strategy` | `RecursiveCharacterTextSplitter` | `SentenceSplitter` |
| `embedding_config` | `OpenAIEmbeddings` / `OllamaEmbeddings` | `OpenAIEmbedding` |
| `vector_store` | `FAISS`, `Chroma`, `PGVector` | `VectorStoreIndex` |
| `retriever_config` | `EnsembleRetriever` + `ContextualCompressionRetriever` | `VectorIndexRetriever` + `Reranker` |

> **Why this matters for you:** The difference between a $20/month ChatGPT subscription and a $200K enterprise AI deployment is — almost entirely — knowledge management. The enterprise system is not smarter. It has better-structured knowledge, better retrieval, and better injection. You can replicate 80% of that with open-source tools and a well-designed P01.

### Knowledge Graph and Ontology: Structured Relational Knowledge

Flat vector search handles "find documents similar to this query." It does not handle "what companies did OpenAI acquire?" or "what are the global themes in this corpus?" That requires `knowledge_graph` and `graph_rag_config`.

The `knowledge_graph` kind defines:
- **entity_types** — constrained whitelist (unconstrained extraction causes node explosion)
- **relation_types** — constrained whitelist (prevents hallucinated relations)
- **extraction_prompt** — the LLM prompt that extracts triplets (subject, predicate, object) from text
- **storage_backend** — `neo4j`, `falkordb`, `in_memory`, or `json`
- **traversal_strategy** — `local` (entity-centric), `global` (community summaries via Leiden/Louvain), or `hybrid`
- **dedup_strategy** — `exact`, `fuzzy`, or `llm` (entity resolution: "OpenAI" = "Open AI")

The key anti-pattern is using a knowledge graph where flat vector search is sufficient. The decision tree is clear: flat Q&A → vectors only; "themes/trends" questions → GraphRAG with community detection; known domain ontology → schema-constrained graph.

### Agentic RAG: When the Agent Drives Retrieval

Standard RAG is a fixed pipeline: query → embed → retrieve → inject. **Agentic RAG** (`agentic_rag` kind) turns retrieval into an agent-controlled loop: the agent decides *whether* to retrieve, *what* to retrieve, *how many hops* to take, and *when* retrieved information is sufficient before generating.

This pattern becomes necessary when:
- Queries require multi-hop reasoning (retrieve entity A, use A to query for B)
- Retrieved documents contain pointers to other documents that must also be retrieved
- The agent needs to evaluate retrieved content quality before committing to it

The implementation always wraps a `retriever_config` and adds an agent reasoning loop around it. The agent has explicit tools: `search(query)`, `fetch(url)`, `evaluate(docs)`, `synthesize(docs)`.

---

## Architecture Deep Dive

### Dependency Graph

```
external sources
      |
   rag_source ─────────────────────┐
      |                            |
  chunk_strategy                   |
      |                            v
  embedder_provider ──> knowledge_card ──> context_doc
      |                     |              glossary_entry
  embedding_config           |              citation
      |                  few_shot_example   dataset_card
  vector_store                |
      |                  knowledge_graph
  retriever_config        ontology
      |
  reranker_config
      |
  agentic_rag (wraps all of the above)
```

The flow is one-directional: raw sources are ingested, chunked, embedded, and stored. KCs are written from distilled facts. Retrieval infrastructure reads from vector stores to return KCs and other artifacts. The `knowledge_graph` sits parallel to flat retrieval and adds relational traversal.

### The Template-First Pattern

When building a new KC, the 8F pipeline applies Template-First at F4 REASON: if a similar KC exists (retrieval score >= 60%), adapt it rather than building from scratch. This is not a CEXAI-specific discipline — it maps directly to what experienced prompt engineers do manually: find an existing working prompt structure, adapt it, rather than starting from scratch each time.

### Knowledge Lifecycle

```
DISCOVER                 DISTILL               VALIDATE
external source ──> raw research ──> knowledge_card ──> quality gate
rag_source           cluster_kc        density >= 0.8    quality >= 7.0
                     _reference/

PERSIST              INDEX                 RETRIEVE          INJECT
git commit ──> cex_compile.py ──> cex_retriever.py ──> F3 INJECT
yaml sibling    TF-IDF / vector     top_k candidates    prompt context
```

The compile step produces a `.yaml` sibling for every `.md` artifact. This dual-format representation (human-readable Markdown + machine-parseable YAML) is what enables both content authoring and programmatic consumption.

Versioning is non-negotiable: the `version` field in frontmatter must increment on any content change. Silent drift is the most common failure mode in knowledge management systems.

---

## Real Examples from the Repository

### Example 1: `ex_knowledge_card_cex_lp01_knowledge.md`

This is the P01 self-describing KC — knowledge about the Knowledge pillar itself. Quality: 9.2, density_score: 1.0. Notable structural choices:

- The **Comparativo** table (six types × purpose × size × core flag) is maximally dense — six facts per cell.
- The **Flow** diagram shows the ingestion pipeline in 6 tokens per step.
- The `axioms` field contains machine-readable invariants: "ALWAYS version knowledge_cards" and "NEVER inject knowledge without a verifiable source." These are not for humans — they are retrieved and injected into builder prompts to constrain generation.
- `data_source` points to the Lewis et al. RAG paper (arXiv 2005.11401) — the empirical grounding for the retrieval-augmented generation approach.

### Example 2: `ex_chunk_strategy_recursive_1000.md`

A production-grade `chunk_strategy` artifact with benchmarks. Key technical detail: it uses **tiktoken** (cl100k_base) for length_function, not Python's `len()`. Character-based splitting misaligns with the embedding model's token space — a common bug that silently degrades recall. The quality gates embedded in the artifact are explicit thresholds: min 50 tokens (merge if smaller), max 1200 (re-split), no heading orphans (heading without >= 20 token body gets merged forward).

The "When NOT to Use" section is load-bearing engineering guidance: tabular data (CSV/JSON) → StructuredSplitter; source code → CodeSplitter with language-aware parsing; documents under 500 tokens → no chunking needed.

### Example 3: `ex_retriever_config_hybrid_rag.md`

The hybrid RAG retriever config includes a complete benchmark table (1,957-document corpus): MRR@5 = 0.82 for hybrid+rerank vs 0.71 for dense-only vs 0.54 for BM25-only. Latency at p50 is 180ms vs 45ms (dense) vs 12ms (BM25). This tradeoff table is the central engineering decision: if you need latency < 100ms, BM25-only. If you need recall > 0.85, hybrid+rerank. The config also includes fallback behavior for each dependency failure mode.

### Example 4: `library/kind/kc_knowledge_graph.md`

The knowledge graph kind KC demonstrates the cross-framework map pattern. It systematically maps the same concept across Microsoft GraphRAG, LlamaIndex KG, LangChain + Neo4j, LightRAG, Haystack, Amazon Neptune, and FalkorDB. This map serves two engineering purposes: (1) practitioners migrating between frameworks can find the equivalent concept; (2) the CEXAI builder uses it to generate correct imports and configuration for the target framework.

---

## Anti-Patterns — Universal Mistakes Everyone Makes

### Anti-Pattern 1: Trusting Built-In Knowledge Instead of Providing Your Own

This is the most expensive mistake. Deploying a raw LLM with no knowledge management, observing hallucination, and attempting to fix it with increasingly detailed system prompts. The root cause is that knowledge lives in the system prompt as undifferentiated text — not versioned, not retrievable, not density-gated, not grounded in sources. When knowledge changes, the system prompt must be rewritten by hand.

**Universal lesson:** your AI's training data is 18-24 months stale and covers your domain at the level of Wikipedia, not your company's internal expertise. The only way to give it current, specific, reliable knowledge is to inject it explicitly at generation time. That is P01.

### Anti-Pattern 2: Pasting Entire Documents Instead of Relevant Sections

The most common beginner mistake. Pasting a 50-page PDF into a chat and asking a specific question. The AI will answer — but it is working through noise, not signal. Chunking is the discipline of identifying and injecting the relevant sections, not the whole document.

**Universal lesson:** context window size is not a license to be lazy about knowledge management. More tokens does not mean better answers — it means more opportunities to dilute the relevant signal with irrelevant content.

### Anti-Pattern 3: Asking AI to "Remember" Without Giving It a System

"Remember this for next time" said to a stateless LLM is a wish, not an instruction. The AI will acknowledge it and forget it immediately. Memory requires external infrastructure: a database, a vector store, a file system, a knowledge card system. Any of these can work; none of them happen automatically.

**Universal lesson:** stateless is the default. Stateful requires deliberate engineering. P01 is that engineering.

### Anti-Pattern 4: KC Density Violations

Writing knowledge cards that contain filler ("This document provides an overview of...") causes two problems: (1) the density gate rejects them during validation; (2) if somehow admitted, they dilute retrieval signal. The `when_to_use` field is the retrieval trigger — it should be as specific as possible. Vague `when_to_use` values produce false positives in retrieval.

### Anti-Pattern 5: Instructions in Knowledge Cards

KCs answer "what is true." Instructions answer "what to do." Mixing these — writing "you should use hybrid search when..." instead of "hybrid search outperforms dense-only by 12% MRR@5 when..." — creates knowledge that belongs in P03 (prompt) rather than P01. The boundary is enforced by the `boundary` field in the schema and by F7 validation.

### Anti-Pattern 6: Flat Chunking by Character Count

Splitting by fixed character count ignores document structure. A 1000-character split through the middle of a code block produces two useless chunks. The correct approach is separator-hierarchy: split at heading level first, then paragraphs, then lines, then words — only falling to character splits as a last resort.

### Anti-Pattern 7: Single Embedding Model Across Mixed Collections

Mixing vectors from different embedding models in the same collection causes cosine similarity comparisons across incompatible spaces. The `vector_store` kind enforces `dimensions` as a required field specifically to catch this at configuration time rather than at query time.

### Anti-Pattern 8: Unconstrained Graph Extraction

Running entity extraction over a corpus without an explicit `entity_types` whitelist produces a graph with thousands of nodes, most of which are noise. The `knowledge_graph` kind requires `entity_types` and `relation_types` as required fields. Graph quality correlates directly with ontology specificity.

---

## Connection to Other Pillars

### P01 → P03 Prompt (knowledge feeds prompt construction)

This is the most direct dependency. F3 INJECT in the 8F pipeline loads P01 artifacts (KCs, context_docs, few_shot_examples) into the prompt at generation time. A prompt template (P03) without P01 injection is a static template; a prompt template with P01 injection becomes a dynamic, knowledge-grounded generation surface. The `context_window_config` (P03) specifies how many tokens from P01 to allocate — this is the token budget decision that determines how much knowledge can actually be injected.

**Universal lesson:** every sophisticated prompt you have ever seen that works reliably has P01 baked in — even informally. The "you are an expert in X, here are the relevant facts: [paste facts]" pattern IS knowledge injection. CEXAI just formalizes and automates it.

### P01 → P10 Memory (knowledge persists across sessions)

P10 Memory is the stateful extension of P01 Knowledge. Where a KC is versioned and stable (write-once-then-version), entity memories (P10) are mutable — they represent what the system has learned during interactions. The `knowledge_index` (P10) is the index that makes P01 content retrievable at runtime. The relationship: P01 provides the base knowledge corpus; P10 captures knowledge acquired through operation.

### P01 → P07 Evaluation (knowledge quality is evaluated)

Quality gates in the 8F pipeline (F7 GOVERN) compare generated artifacts against ground truth. That ground truth is P01. The `quality` field on every KC is assigned by peer review (never self-scored). `cex_score.py` runs three scoring layers: structural (30%, automated count-based), rubric (30%, quality gate dimensions), and semantic (40%, LLM evaluation when layers 1+2 pass threshold).

### P01 → P08 Architecture (knowledge informs architectural decisions)

Decision records (P08) reference KCs as evidence. When an architecture decision is made — "use hybrid retrieval over dense-only" — the KC containing the benchmark data is linked as the evidentiary source. This creates an audit trail from decision to data.

### P01 → P02 Model (agents are loaded with domain KCs at boot)

Agent boot configurations reference P01 KCs as mandatory context sources. The agent's `agent_card` (P08) lists which KCs must be injected at F3. This is how a customer support agent "knows" product features, pricing, and policies — not through fine-tuning but through structured KC injection at each invocation.

---

## The Fractal Principle and P01's Role

The CEXAI system applies the same 12-pillar structure at every scale. P01 is the first pillar that gets added when a prompt needs memory:

```
L0 Prompt: P03 only (static template, zero knowledge)
L1 Chain: P03 + P12 (chained prompts, no knowledge)
L2 Agent: P01 + P02 + P03 + P06 (knowledge injected, agent has identity)
L3 Runtime: +P04 + P09 (tools + configuration)
L4 Agent_group: +P10 + P11 (memory + feedback)
L5 System: all 12 pillars
```

The moment you need the agent to know anything domain-specific — pricing, regulations, product specs, competitive landscape — you activate P01. This is the threshold between a toy demo and a production-grade AI system.

The practical consequence for engineering teams: investment in P01 is what distinguishes LLM systems that improve over time (KC corpus grows, is versioned, is retrieved more precisely) from systems that degrade over time (system prompts inflate, become inconsistent, lose facts). P01 is where organizational knowledge becomes computable — not text thrown into a prompt, but typed, searchable, governed artifacts that any agent can consume.

---

## Decision Guide: Which P01 Kind to Use?

```
I have a domain fact to capture?
  |-- Single term definition? --> glossary_entry (max 512B)
  |-- Broad background context? --> context_doc (max 2048B)
  |-- Dense, searchable fact? --> knowledge_card (max 5120B, density >= 0.8)
  |-- External source to index? --> rag_source (URL + freshness)
  |-- Input/output teaching pair? --> few_shot_example

I need to build a RAG pipeline?
  |-- How to split my documents? --> chunk_strategy
  |-- Which vector model to use? --> embedding_config + embedder_provider
  |-- Where to store the vectors? --> vector_store
  |-- How to search? (recall/precision) --> retriever_config
  |-- Need to improve precision post-search? --> reranker_config
  |-- Agent needs to control the retrieval loop? --> agentic_rag

My domain has complex entity relationships?
  |-- Multi-hop queries needed? --> knowledge_graph + graph_rag_config
  |-- Need controlled vocabulary? --> ontology + domain_vocabulary

Building for a specific industry?
  |-- eCommerce, EdTech, Fintech, Healthcare, Legal, GovTech? --> corresponding vertical_template
```

This decision guide is executable through `_tools/cex_intent_resolver.py` — Python-first, zero LLM tokens, direct mapping of intent to kind via bilingual PT+EN patterns.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_pillar_brief_p01_knowledge_pt]] | translation | 1.00 |
| [[kc_pillar_brief_p02_model_en]] | sibling | 0.85 |
| [[cm_driver_01_structured_thinking]] | downstream | 0.60 |
| [[kc_lens_factory]] | upstream | 0.45 |
| [[kc_lens_index]] | upstream | 0.40 |
| [[mentor_context]] | upstream | 0.38 |
