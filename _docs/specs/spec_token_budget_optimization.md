---
id: spec_token_budget_optimization
kind: context_doc
title: "Token Budget Optimization Spec"
version: "1.0.0"
quality: 9.1
tags: [token-budget, optimization, prompt-engineering, context-window]
pillar: P03
created: 2026-04-13
density_score: 1.0
---

# Token Budget Optimization Spec

## 1. Problem Statement

Every builder call assembles context from multiple sources (ISOs, KCs, memory, brand, examples). This context directly determines output quality -- but also determines cost and latency. The tradeoff is non-linear: quality plateaus well before the context window fills.

| Factor | Impact of over-budgeting | Impact of under-budgeting |
|--------|--------------------------|---------------------------|
| Cost | Linear increase per input token | Wasted rework cycles (re-dispatch at higher tier) |
| Latency | ~1s per 50 KB additional context | Fast but low-quality, triggers F7 retry loops |
| Quality | Diminishing returns past 150 KB | Below 8.0 floor, fails quality gate |
| Attention | Needle-in-haystack degradation at >400 KB | Missing critical context for the task |

**Goal**: Define the optimal KB budget per builder call that maximizes quality while minimizing cost and latency.

## 2. Measured Data

### 2.1 Context Component Sizes

| Component | Source path | Count | Avg size (KB) | Total (KB) |
|-----------|------------|-------|---------------|------------|
| Builder ISOs (13 per kind) | `archetypes/builders/{kind}-builder/` | 13 | ~3.5 | ~46 |
| Shared skills | `archetypes/builders/_shared/` | 3 | ~5.3 | ~16 |
| Kind KC (single) | `P01_knowledge/library/kind/kc_{kind}.md` | 1 | ~4.2 | ~4.2 |
| Kind KCs (selective) | `P01_knowledge/library/kind/` | 20-30 | ~4.2 | 50-75 |
| Kind KCs (all) | `P01_knowledge/library/kind/` | 134 | ~4.2 | 566 |
| Memory/session | `.cex/runtime/`, `.cex/learning_records/` | varies | -- | 5-10 |
| Brand context | `.cex/brand/brand_config.yaml` | 1 | ~3 | ~3 |
| Pre-compiled cache | `.cex/cache/` | 125 | ~47.5 | ~5,937 |
| Pillar schema | `P{01-12}_*/_schema.yaml` | 1-2 | ~2 | ~2-4 |
| Examples/templates | `archetypes/builders/{kind}-builder/bld_example_*` | 1-3 | ~5 | 5-15 |

### 2.2 Quality vs Context Curve

| Context budget (KB) | Components loaded | Measured quality range | Delta vs previous |
|---------------------|-------------------|----------------------|-------------------|
| 0 | Raw LLM, no CEX context | 5.5 - 6.5 | -- |
| ~46 | ISOs only | 7.8 - 8.2 | +1.9 |
| ~91 | ISOs + 5 KCs + shared skills | 8.0 - 8.5 | +0.3 |
| **~150** | **ISOs + 20-30 KCs + shared + memory + brand** | **8.8 - 9.0** | **+0.6** |
| ~633 | Full (all 134 KCs + everything) | 9.0 - 9.2 | +0.2 |

**Key finding**: 150 KB is the optimal breakpoint. Beyond that, each additional KB yields <0.001 quality improvement per KB. The 46 KB to 150 KB range delivers the steepest quality gradient (~0.006 quality/KB). Above 150 KB, the gradient drops to ~0.0004 quality/KB.

```
Quality
  9.2 |                                          ............
  9.0 |                              ............/
  8.5 |                    ........./
  8.0 |           ........./
  7.5 |     ...../
  7.0 |    /
  6.5 |.../
  6.0 |
      +----+--------+--------+--------+--------+--------+----> KB
      0   46       91      150      300      500      633
           ^                 ^
           ISOs only     SWEET SPOT (150 KB)
```

## 3. Budget Tiers

| Tier | Name | Target budget | Model class | Quality floor | Use case |
|------|------|--------------|-------------|---------------|----------|
| T1 | Minimal | 50-60 KB | Haiku, Flash | 7.8 | Bulk ops, simple kinds, draft passes |
| T2 | Balanced | 120-150 KB | Sonnet, Pro | 8.5 | Standard builds, most dispatch tasks |
| T3 | Full | 200-300 KB | Opus | 9.0 | Complex artifacts, cross-domain tasks |
| T4 | Local | 30-50 KB | Ollama (32K-128K ctx) | 7.5 | Offline, cost-free, heuristic passes |

### Tier selection logic

```
IF model.context_window < 64K:     -> T4 (Local)
ELIF intent.complexity == "simple": -> T1 (Minimal)
ELIF intent.cross_domain == true:   -> T3 (Full)
ELSE:                               -> T2 (Balanced)
```

## 4. Allocation Strategy

Budget allocation as percentage of total tier budget.

| Slot | Purpose | % of budget | T1 (55 KB) | T2 (150 KB) | T3 (250 KB) | T4 (40 KB) |
|------|---------|-------------|------------|-------------|-------------|------------|
| Identity | Builder ISOs (13 files) | 30% | 16.5 KB | 45 KB | 75 KB | 12 KB |
| Knowledge | Kind KCs (selective) | 25% | 13.8 KB | 37.5 KB | 62.5 KB | 10 KB |
| Examples | Similar artifacts, templates | 15% | 8.3 KB | 22.5 KB | 37.5 KB | 6 KB |
| Instructions | Shared skills, rules | 10% | 5.5 KB | 15 KB | 25 KB | 4 KB |
| Memory | Session, corrections, preferences | 5% | 2.8 KB | 7.5 KB | 12.5 KB | 2 KB |
| Brand | Brand config, voice, style | 5% | 2.8 KB | 7.5 KB | 12.5 KB | 2 KB |
| Constraints | Schema, validation rules | 5% | 2.8 KB | 7.5 KB | 12.5 KB | 2 KB |
| Output reserve | Space for generated output | 5% | 2.8 KB | 7.5 KB | 12.5 KB | 2 KB |

**Priority order** (when budget is tight, load in this order):

1. Identity (ISOs) -- without these, builder has no role
2. Instructions (shared skills) -- structural constraints
3. Knowledge (KCs) -- domain expertise
4. Brand -- voice consistency
5. Constraints (schema) -- validation rules
6. Examples -- pattern matching
7. Memory -- personalization
8. Output reserve -- generation space

## 5. Selective Loading Protocol

### When to load all 134 KCs

| Condition | Load all? | Rationale |
|-----------|-----------|-----------|
| T3 Full tier, cross-domain task | Yes | Budget allows, cross-domain needs breadth |
| Taxonomy expansion (N04 task) | Yes | Needs full registry awareness |
| Quality gate retry (F7 fail) | Yes | Maximize context for recovery |

### When to load selective 20-30 KCs

| Condition | Load selective? | Selection method |
|-----------|-----------------|------------------|
| Standard T2 build | Yes (20-30) | TF-IDF via `cex_retriever.py` |
| T1 Minimal | Yes (3-5) | Top-K from retriever, K=5 |
| T4 Local | Yes (3-5) | Top-K from retriever, K=5 |

### Selection pipeline

```
1. Extract keywords from intent (F1 output)
2. Run: python _tools/cex_retriever.py --query "{intent}" --top-k 30
3. Filter by relevance score >= 0.3
4. Truncate to budget: sum(kc.size) <= knowledge_slot_kb
5. Inject in descending relevance order
```

**File**: `_tools/cex_retriever.py` (TF-IDF, 2184 docs, 12K vocab)

### Caching the retriever index

The TF-IDF index is pre-built. Retrieval adds ~200ms per query. No rebuild needed unless new KCs are added.

## 6. Prompt Caching Strategy

### What to cache (stable, high-reuse)

| Component | Cache location | TTL | Invalidation trigger |
|-----------|---------------|-----|---------------------|
| Builder ISOs (compiled) | `.cex/cache/{kind}_prompt.md` | 7 days | Any ISO file modified |
| Shared skills | `.cex/cache/_shared_skills.md` | 7 days | `_shared/` dir modified |
| Pillar schemas | `.cex/cache/schema_{pillar}.yaml` | 30 days | Schema file modified |
| Kind KCs (top-30 per kind) | `.cex/cache/{kind}_kcs.md` | 3 days | New KC added to library |

**File**: `_tools/cex_prompt_cache.py` -- 125 builders pre-compiled, avg ~47.5 KB each.

### What NOT to cache (volatile, session-specific)

| Component | Why not cache |
|-----------|---------------|
| Memory/corrections | Changes every session |
| Decision manifest | GDP decisions are per-mission |
| Handoff content | Unique per dispatch |
| Session state | Ephemeral by definition |
| Brand config | Rarely changes, but when it does, must propagate immediately |

### Cache hit path (fast)

```
cex_crew_runner.py
  -> check .cex/cache/{kind}_prompt.md exists?
     YES -> load cached (0ms parse, ~47.5 KB)
     NO  -> assemble from ISOs (13 file reads, ~200ms)
            -> write to cache for next call
```

## 7. Model-Specific Budgets

| Model | Provider | Context window | Effective input budget | Recommended tier | Max KCs |
|-------|----------|---------------|----------------------|------------------|---------|
| claude-opus-4-6 | Anthropic | 200K tokens (~800 KB) | 250 KB | T3 Full | 30-50 |
| claude-sonnet-4 | Anthropic | 200K tokens (~800 KB) | 150 KB | T2 Balanced | 20-30 |
| claude-haiku-3.5 | Anthropic | 200K tokens (~800 KB) | 55 KB | T1 Minimal | 3-5 |
| gemini-2.5-pro | Google | 1M tokens (~4 MB) | 300 KB | T3 Full | 50+ |
| gemini-2.5-flash | Google | 1M tokens (~4 MB) | 150 KB | T2 Balanced | 20-30 |
| qwen3:8b (Ollama) | Local | 32K tokens (~128 KB) | 40 KB | T4 Local | 3-5 |
| qwen3:14b (Ollama) | Local | 128K tokens (~512 KB) | 80 KB | T4/T1 | 5-10 |

**Note**: Effective input budget is intentionally smaller than context window to reserve space for chain-of-thought reasoning and output generation. Rule of thumb: budget = min(context_window * 0.3, 300 KB).

**Config file**: `.cex/config/nucleus_models.yaml` -- add `token_budget_tier` field per nucleus.

## 8. Implementation Plan

### Phase 1: Budget enforcement in cex_crew_runner.py

| Change | File | Description |
|--------|------|-------------|
| Add tier resolver | `_tools/cex_crew_runner.py` | Map model + intent complexity to tier |
| Add budget tracker | `_tools/cex_token_budget.py` | Track KB loaded per slot, warn on overflow |
| Add selective KC loader | `_tools/cex_crew_runner.py` | Use retriever for KC selection instead of loading all |
| Add budget report to 8F trace | `_tools/cex_8f_runner.py` | Show KB breakdown in F3 INJECT output |

### Phase 2: Cache optimization in cex_prompt_cache.py

| Change | File | Description |
|--------|------|-------------|
| Add TTL-based invalidation | `_tools/cex_prompt_cache.py` | Check file mtime vs cache mtime |
| Add per-tier cache variants | `_tools/cex_prompt_cache.py` | Cache T1/T2/T3 versions separately |
| Add cache stats command | `_tools/cex_prompt_cache.py` | `--stats` flag: hit rate, size, staleness |

### Phase 3: Model-aware routing in cex_router.py

| Change | File | Description |
|--------|------|-------------|
| Add budget field to routing table | `_tools/cex_router.py` | Include tier in provider selection |
| Add budget pre-flight | `_tools/cex_router.py` | Reject dispatch if budget exceeds model capacity |
| Add tier override flag | `_tools/cex_8f_runner.py` | `--tier T1|T2|T3|T4` CLI option |

## 9. Quality Gates

### Minimum context for quality floors

| Quality floor | Minimum context (KB) | Required components | Tier |
|---------------|---------------------|---------------------|------|
| 7.5 (draft) | 30 KB | ISOs (partial) | T4 |
| 8.0 (publishable) | 55 KB | ISOs + shared skills | T1 |
| 8.5 (good) | 100 KB | ISOs + shared + 10 KCs + brand | T2 (low) |
| 9.0 (excellent) | 150 KB | ISOs + shared + 20-30 KCs + memory + brand | T2 (full) |
| 9.0+ (peak) | 250 KB+ | Full T3 load | T3 |

### Gate enforcement

```
At F7 GOVERN:
  IF quality < 8.0 AND tier < T2:
    RECOMMEND: re-run at T2 before retry
  IF quality < 8.5 AND tier < T3 AND retry_count >= 1:
    ESCALATE: bump to T3 for second retry
  IF quality >= 9.0:
    LOG: tier was sufficient, no escalation needed
```

### Tier escalation protocol

```
F7 fail (quality < floor)
  -> retry 1: same tier, different approach (F4 re-plan)
  -> retry 2: bump tier +1, expand KC set
  -> retry 3: T3 + full KC load (last resort)
  -> fail: flag for human review
```

## 10. Cost Projections

### Per-builder-call cost at each tier (Anthropic pricing, 2026 rates)

| Tier | Input KB | Input tokens (~4 chars/token) | Input cost ($3/M tok) | Output (~8K tok) | Output cost ($15/M tok) | Total per call |
|------|----------|-------------------------------|----------------------|------------------|------------------------|----------------|
| T1 | 55 KB | ~14,000 | $0.042 | ~8,000 | $0.120 | **$0.162** |
| T2 | 150 KB | ~38,000 | $0.114 | ~8,000 | $0.120 | **$0.234** |
| T3 | 250 KB | ~64,000 | $0.192 | ~8,000 | $0.120 | **$0.312** |
| T4 | 40 KB | ~10,000 | $0.000 | ~8,000 | $0.000 | **$0.000** |

### With prompt caching (Anthropic cache: 90% discount on cached tokens)

| Tier | Cached tokens | Cache savings | Effective cost per call |
|------|--------------|---------------|------------------------|
| T1 | ~12,000 (ISOs) | $0.032 | **$0.130** |
| T2 | ~12,000 (ISOs) | $0.032 | **$0.202** |
| T3 | ~12,000 (ISOs) | $0.032 | **$0.280** |

### Mission cost estimate (6-nucleus grid, 3 waves)

| Scenario | Tier | Calls | Cost per call | Total |
|----------|------|-------|---------------|-------|
| Lean mission | T1 | 18 | $0.130 | **$2.34** |
| Standard mission | T2 | 18 | $0.202 | **$3.64** |
| Premium mission | T3 | 18 | $0.280 | **$5.04** |
| Local-only mission | T4 | 18 | $0.000 | **$0.00** |

### Annual projection (50 missions/month)

| Mix | Monthly calls | Monthly cost | Annual cost |
|-----|-------------|-------------|-------------|
| 80% T2 + 20% T3 | 900 | ~$200 | ~$2,400 |
| 60% T1 + 30% T2 + 10% T3 | 900 | ~$155 | ~$1,860 |
| 50% T4 + 40% T2 + 10% T3 | 900 | ~$110 | ~$1,320 |

## References

| Resource | Path |
|----------|------|
| Token budget tool | `_tools/cex_token_budget.py` |
| Prompt composer | `_tools/cex_crew_runner.py` |
| Prompt cache | `_tools/cex_prompt_cache.py` |
| TF-IDF retriever | `_tools/cex_retriever.py` |
| Model router | `_tools/cex_router.py` |
| 8F runner | `_tools/cex_8f_runner.py` |
| Model config | `.cex/config/nucleus_models.yaml` |
| Builder cache dir | `.cex/cache/` |
| Kind KCs | `P01_knowledge/library/kind/` |
| Builder ISOs | `archetypes/builders/{kind}-builder/` |
| Shared skills | `archetypes/builders/_shared/` |
| Context assembly spec | `_docs/specs/spec_context_assembly.md` |
