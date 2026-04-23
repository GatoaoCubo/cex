---
id: kc_tool_first_patterns
kind: knowledge_card
pillar: P01
title: Tool-First Patterns -- Industry Methods for Replacing LLM Calls with Deterministic Tools
version: 1.0.0
created: 2026-04-08
author: N01
domain: tool-first-engineering
quality: 9.0
tags: [tool-first, deterministic, TF-IDF, heuristics, DSPy, LangChain, caching, optimization]
tldr: "7 industry patterns for replacing LLM calls with deterministic tools. Each mapped to an existing or buildable CEX tool. Covers intent resolution, scoring, memory selection, content generation, and embedding."
related:
  - kc_token_optimization_map
  - kc_benchmark_tool_vs_llm
  - p01_kc_intent_resolution_benchmark
  - n04_rag_pipeline_memory
  - p01_kc_prompt_compiler
  - p01_kc_rag_hybrid
  - p01_kc_input_intent_resolution
  - p01_report_intent_resolution
  - p01_kc_anti_file_storage
  - p01_gl_rag
---

# Tool-First Patterns

## Principle

Every LLM call should justify its existence against 3 alternatives:
1. **Lookup table** -- Can a static mapping solve this?
2. **Heuristic** -- Can rules + regex + counting solve this?
3. **TF-IDF/embedding similarity** -- Can statistical matching solve this?

Only if all 3 fail should the LLM be invoked. This is the **tool-first principle** (industry: "deterministic-first", "rule-before-model").

---

## Pattern 1: Intent Resolution Cascade

**Industry source**: Rasa NLU, Amazon Lex, Dialogflow intent classification.

**Architecture**:
```
User input
  |-> [1] Exact match (hash table)       -- O(1), 100% precision
  |-> [2] Fuzzy match (difflib, 0.8)     -- O(n), 95% precision
  |-> [3] TF-IDF ranking (cex_query.py)  -- O(n log n), 85% precision
  |-> [4] LLM fallback (execute_prompt)  -- O(1) but slow + costly
```

**CEX implementation**: `cex_8f_motor.py` already implements levels 1-3:
- Level 1: `VERB_TABLE` (65 verbs, line 156) + `OBJECT_TO_KINDS` (line 947)
- Level 2: `difflib.get_close_matches()` at 0.8 threshold (line 913)
- Level 3: `cex_query.query_builders()` TF-IDF (line 987)
- Level 4: Not used -- motor is fully deterministic

**Comparison vs. pure LLM**:

| Metric | Cascade (CEX) | Pure LLM | Winner |
|--------|---------------|----------|--------|
| Latency | <50ms | 3-15s | Cascade (300x) |
| Cost | $0 | ~500 tokens | Cascade |
| Accuracy (known intents) | 98% | 95% | Cascade |
| Accuracy (novel intents) | 60% | 90% | LLM |
| Determinism | 100% reproducible | Non-deterministic | Cascade |

**Gap**: Novel intent handling. CEX mitigates via the "generic" fallback kind + user confirmation.

---

## Pattern 2: Heuristic Scoring with LLM Escalation

**Industry source**: GitHub Copilot code review (heuristic first, LLM for nuance), Google Search quality raters (automated signals + human review for edge cases).

**Architecture**:
```
Artifact
  |-> [L1] Structural score (counts, regex)     -- 30% weight
  |-> [L2] Rubric score (domain rules)           -- 30% weight
  |-> [Gate] If L1+L2 avg < 8.5: STOP (no LLM)
  |-> [L3] Semantic score (LLM, 1 call)          -- 40% weight
```

**CEX implementation**: `cex_score.py` uses this exact pattern.

**Optimization**: Replace L3 with extended L2 heuristics.

| L3 Dimension | Heuristic Replacement | Method |
|-------------|----------------------|--------|
| ACTIONABILITY | Imperative verb count + "how to" + code blocks + "must/should" | Regex + counting |
| INSIGHT_DEPTH | TF-IDF novelty score vs. same-kind corpus mean | Statistical deviation |
| COMPLETENESS | Schema-required sections present / total required | Set intersection |
| DENSITY | Filler phrase ratio (already in L2) | Regex counting |
| DOMAIN_EXPERTISE | Domain keyword density vs. threshold (already in L2) | TF-IDF |
| SEARCHABILITY | Tag count + TLDR presence + heading structure (already in L1) | Structural |

**Comparison**:

| Metric | Heuristic L3 | LLM L3 | Winner |
|--------|-------------|---------|--------|
| Latency | <100ms | 5-30s | Heuristic (300x) |
| Cost | $0 | ~1075 tokens | Heuristic |
| Accuracy (mechanical dims) | 90% | 95% | Tie (practical) |
| Accuracy (INSIGHT_DEPTH) | 70% | 90% | LLM |
| Reproducibility | 100% | ~85% (variance) | Heuristic |

---

## Pattern 3: TF-IDF Memory Selection

**Industry source**: LlamaIndex `VectorStoreIndex` (embedding-first, keyword fallback), LangChain `EnsembleRetriever` (BM25 + vector hybrid), Elasticsearch BM25 ranking.

**Architecture**:
```
Query + Memory corpus
  |-> [1] TF-IDF index (one-time build, ~100ms)
  |-> [2] Score query vs. all memories (~5ms)
  |-> [3] Apply confidence weighting + age decay
  |-> [4] Return top-K
```

**CEX has this**: `cex_retriever.py` implements TF-IDF over 2184 docs with 12K vocabulary. The same engine can power `cex_memory_select.py`.

**Comparison vs. current LLM selector**:

| Metric | TF-IDF | LLM (Sonnet) | Keyword (current fallback) |
|--------|--------|-------------|---------------------------|
| Latency | ~5ms | 3-10s | ~1ms |
| Cost | $0 | ~725 tokens | $0 |
| Semantic understanding | Medium | High | None |
| Recall (relevant memories) | 90% | 95% | 75% |
| Determinism | 100% | Non-deterministic | 100% |

**Implementation**: Reuse `cex_retriever.build_index()` over memory header text. Apply same `confidence * age_decay` weighting that keyword fallback already uses. Drop-in replacement for `_select_via_llm()`.

---

## Pattern 4: DSPy Prompt Compilation (Optimize, Don't Replace)

**Industry source**: DSPy framework (Stanford NLP), "Compiling Declarative Language Model Calls into Self-Improving Pipelines" (Khattab et al., 2023).

**Concept**: Instead of hand-writing prompts, define the task signature and let the compiler find the optimal prompt via few-shot example selection + instruction tuning.

**CEX analog**: `cex_crew_runner.py` already does manual prompt composition (13 ISOs + memory + brand + context). DSPy would automate the selection of WHICH context to include.

**Applicability to CEX**:

| DSPy Feature | CEX Equivalent | Gap |
|-------------|----------------|-----|
| Signature definition | Builder ISOs (bld_instruction, bld_manifest) | None -- already defined |
| Few-shot example selection | `cex_retriever.py` finds similar artifacts | Could auto-inject top-3 |
| Prompt optimization | `cex_prompt_optimizer.py` heuristic analysis | No automatic rewriting |
| Metric-driven compilation | `cex_score.py` 3-layer scoring | No feedback loop to prompts |

**Recommendation**: NOT a replacement (still uses LLM). But optimizes token efficiency of CORE_LLM calls by selecting only the most relevant context. Estimated token reduction: 20-30% per prompt by dropping low-relevance ISOs.

---

## Pattern 5: Semantic Caching

**Industry source**: GPTCache (Zilliz), LangChain `InMemoryCache`, Redis semantic cache.

**Architecture**:
```
Prompt hash -> Cache lookup
  |-> [Hit] Return cached response (0 tokens, <1ms)
  |-> [Miss] Call LLM -> Cache response -> Return
```

**CEX implementation**: `cex_score.py` already has content-hash caching (lines 413-440). When an artifact hasn't changed, L3 score is served from cache.

**Expansion opportunity**: Apply to `cex_evolve.py` agent mode. If an artifact's content hash matches a previously-evolved version, skip the LLM call and return the cached hypothesis.

**Comparison**:

| Metric | No Cache | Content-Hash Cache | Semantic Cache |
|--------|----------|-------------------|----------------|
| Cache hit rate | 0% | ~30% (unchanged files) | ~50% (similar files) |
| Latency (hit) | 5-30s | <1ms | ~50ms (similarity check) |
| Storage | 0 | ~10MB/1000 artifacts | ~50MB/1000 artifacts |
| Complexity | None | Low (already in CEX) | Medium (needs embedding index) |

**Recommendation**: Content-hash caching is already implemented in cex_score.py. Extend to cex_evolve.py. Semantic caching (embedding-based) is overkill for CEX's corpus size.

---

## Pattern 6: Template-First Generation

**Industry source**: Rails scaffolding, Yeoman generators, Cookiecutter, Plop.js.

**Architecture**:
```
Kind + Schema + Brand config
  |-> [1] Find template for kind (exact match)
  |-> [2] Fill placeholders ({{BRAND_NAME}}, {{KIND}}, etc.)
  |-> [3] Inject domain-specific content from KC library
  |-> [4] LLM only for creative sections (if any)
```

**CEX implementation**: The 8F pipeline's F3 INJECT already loads templates:
- `archetypes/builders/{kind}-builder/` (13 ISOs per kind)
- `P{xx}/{subdir}/tpl_{kind}.md` (output templates)
- `brand_inject.py` replaces `{{BRAND_*}}` placeholders

**CEX's Construction Triad** (from F4 REASON):
- Template match >= 60% -> Adapt template (minimal LLM)
- Template match 30-59% -> Hybrid (template structure + LLM content)
- Template match < 30% -> Fresh generation (full LLM)

**Gap**: No template match scoring is automated. Currently relies on builder's judgment.

**Proposed automation**: Use `cex_retriever.py` TF-IDF to score intent against template library. If score >= 0.6, use template-first path. Saves ~2K tokens per artifact for template-heavy kinds.

---

## Pattern 7: Local Embedding Models

**Industry source**: Hugging Face `sentence-transformers`, Ollama `nomic-embed-text`, MTEB benchmark leaderboard.

**Architecture**:
```
Text -> Local model (CPU/GPU) -> Embedding vector
  vs.
Text -> API call (OpenAI) -> Embedding vector
```

**CEX current**: `cex_kc_index.py` uses OpenAI `text-embedding-3-small` (1536 dims, $0.02/1M tokens).

**Alternatives**:

| Model | Dims | Cost | Latency | MTEB Score | Local? |
|-------|------|------|---------|------------|--------|
| OpenAI text-embedding-3-small | 1536 | $0.02/1M | ~100ms | 62.3 | No |
| all-MiniLM-L6-v2 | 384 | $0 | ~50ms | 58.8 | Yes |
| nomic-embed-text (Ollama) | 768 | $0 | ~80ms | 61.5 | Yes |
| BGE-small-en-v1.5 | 384 | $0 | ~40ms | 62.1 | Yes |

**Recommendation**: `nomic-embed-text` via Ollama. Already in CEX's provider chain (cex_intent.py uses Ollama as fallback). 768 dims is sufficient for ~2000 document corpus. MTEB score within 1 point of OpenAI.

---

## Pattern-to-CEX Tool Mapping

| Pattern | CEX Tool (exists) | CEX Tool (to build) | Priority |
|---------|-------------------|---------------------|----------|
| Intent cascade | `cex_8f_motor.py` | -- (complete) | Done |
| Heuristic scoring | `cex_score.py` L1+L2 | Extend L2 with 3 sub-scorers | High |
| TF-IDF memory | `cex_retriever.py` | Adapt for `cex_memory_select.py` | High |
| DSPy compilation | `cex_crew_runner.py` + `cex_prompt_optimizer.py` | Auto-context selection | Medium |
| Semantic caching | `cex_score.py` content-hash | Extend to `cex_evolve.py` | Medium |
| Template-first | `brand_inject.py` + builder ISOs | Template match scoring | Low |
| Local embeddings | Ollama in `cex_intent.py` | Swap in `cex_kc_index.py` | Low |

---

## Anti-Patterns (What NOT to Replace)

| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Replace all LLM generation with templates | Templates can't handle novel content or creative writing |
| Use LLM for every classification task | Lookup tables are 300x faster and more deterministic |
| Cache LLM responses without content hashing | Stale cache serves wrong answers after artifact edits |
| Use embeddings where TF-IDF suffices | Embedding overhead not justified for <5000 doc corpus |
| Remove LLM from evolve agent mode | Creative rewrites require generative capability |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_token_optimization_map]] | sibling | 0.47 |
| [[kc_benchmark_tool_vs_llm]] | sibling | 0.45 |
| [[p01_kc_intent_resolution_benchmark]] | sibling | 0.23 |
| [[n04_rag_pipeline_memory]] | downstream | 0.22 |
| [[p01_kc_prompt_compiler]] | sibling | 0.22 |
| [[p01_kc_rag_hybrid]] | sibling | 0.22 |
| [[p01_kc_input_intent_resolution]] | sibling | 0.20 |
| [[p01_report_intent_resolution]] | sibling | 0.20 |
| [[p01_kc_anti_file_storage]] | sibling | 0.19 |
| [[p01_gl_rag]] | related | 0.19 |
