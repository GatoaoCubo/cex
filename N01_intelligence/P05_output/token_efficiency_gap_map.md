---
id: token_efficiency_gap_map
kind: knowledge_card
8f: F3_inject
title: Token Efficiency Gap Map -- CEX Cost Optimization Playbook
version: 1.0.0
quality: 9.0
pillar: P01
created: 2026-04-12
tags: [efficiency, cost, tokens, optimization, tiered-execution, python-first]
nucleus: N01
density_score: 1.0
related:
  - p02_mc_claude_opus_4
  - kc_tool_first_patterns
  - kc_token_optimization_map
  - claude_vs_free_decision_matrix
  - self_audit_n03_builder_20260408
  - spec_token_budget_optimization
  - spec_infinite_bootstrap_loop
  - p01_kc_claude_model_capabilities_2026
  - p01_kc_cex_project_overview
  - p01_kc_caching
---

# Token Efficiency Gap Map

> Principle: The cheapest token is the one you never send.

## Cost Ladder

| Tier | Method | Cost/op | Latency | When to use |
|------|--------|---------|---------|-------------|
| T0 | Python script | $0 | instant | Deterministic ops: validation, indexing, template rendering |
| T1 | Ollama local (GPU) | $0 | 2-10s | Simple generation: frontmatter, summaries, structured output |
| T2 | Ollama local (CPU) | $0 | 5-30s | Bulk overnight: quality scoring, artifact evolve |
| T3 | Cheap cloud (Haiku/Flash) | $0.001 | 1-3s | Mid-complexity: creative copy, reformatting |
| T4 | Premium cloud (Opus) | $0.075 | 1-5s | Deep reasoning: orchestration, research, complex artifacts |

## Gap 1: Python-First Heuristics

Tasks that DO NOT need an LLM -- run .py instead.

| Task | Current (LLM) | Optimal (Python) | Savings |
|------|---------------|-------------------|---------|
| YAML validation | LLM reads and checks | pyyaml schema validation | 100% |
| Frontmatter extraction | LLM parses markdown | Regex + YAML parse | 100% |
| Kind resolution (simple) | LLM reasons | Dict lookup from kinds_meta.json | 100% |
| Quality scoring L1 (structural) | LLM evaluates | Count sections, bytes, frontmatter | 100% |
| Quality scoring L2 (rubric) | LLM evaluates | Boolean checks on H01-H07 | 100% |
| Report generation (data) | LLM writes prose | Template + data injection | 100% |
| Git diff analysis | LLM reads diffs | git diff --stat + Python parse | 100% |
| Artifact inventory | LLM scans dirs | pathlib + frontmatter parse | 100% |
| Verb resolution (PT/EN) | LLM maps | Python dict from prompt_compiler | 100% |
| Metaphor translation | LLM translates | Python dict from metaphor_dictionary | 100% |

## Gap 2: Prompt Caching

| Technique | Industry Source | Status |
|-----------|----------------|--------|
| Anthropic prompt caching (cache_control) | Claude API | NOT USED |
| Pre-compiled builder prompts | DSPy prompt compilation | NOT USED |
| Result memoization (hash prompt -> cached result) | functools.lru_cache | NOT USED |
| Embedding index cache (FAISS local) | LlamaIndex, ChromaDB | NOT USED |
| System prompt snapshot (compile once, load cached) | OpenAI cached system | NOT USED |

## Gap 3: Model Routing by Complexity

| Task Complexity | Current Model | Optimal Model | Cost Reduction |
|----------------|---------------|---------------|----------------|
| Frontmatter generation | Opus ($$$) | qwen3:8b ($0) | 100% |
| Simple rewording | Opus ($$$) | qwen3:14b ($0) | 100% |
| Code generation (structured) | Opus ($$$) | qwen3:14b ($0) | 100% |
| Quality scoring L3 | Opus ($$$) | Sonnet ($) | 80% |
| Sub-agent simple tasks | Opus ($$$) | qwen3:8b ($0) | 100% |
| Deep research | Opus | Opus | 0% (correct) |
| Complex orchestration | Opus | Opus | 0% (correct) |

## Gap 4: Selective Context Loading

| Current | Optimal | Savings |
|---------|---------|---------|
| Load all 13 ISOs per build | Load 3-5 relevant ISOs | ~60% context tokens |
| Full artifact body in prompt | Summary + reference pointer | ~70% context tokens |
| All 124 kind mappings | Top-10 likely kinds from TF-IDF | ~90% context tokens |
| Full metaphor dictionary | Only relevant domain subset | ~80% context tokens |

## Gap 5: Offline/Overnight Zero-Cost Operations

| Operation | Current Cost | With Ollama | Savings |
|-----------|-------------|-------------|---------|
| Evolve 131 quality:null artifacts | $0 (Max plan) but consumes quota | $0 (truly free, unlimited) | Preserves cloud quota for interactive |
| Mass compilation | Python ($0) | Python ($0) | Already optimal |
| Artifact regeneration | Claude Opus | Aider + qwen3:14b | 100% |
| Knowledge distillation | Claude Opus | Python extract + Ollama | 100% |

## Gap 6: Pre-computation Cache

| Pre-computable | Compute Once | Inject Forever |
|----------------|-------------|----------------|
| Kind -> pillar -> nucleus routing | Python dict from kinds_meta.json | Lookup in <1ms |
| Builder ISO compiled prompt | cex_skill_loader + serialize | Load from disk in <10ms |
| Quality gates boolean checklist | H01-H07 as Python functions | Evaluate in <1ms |
| Prompt compiler resolution table | Parse prompt_compiler seed artifact once | Dict lookup in <1ms |

## Implementation Priority

| Priority | Action | Token Savings | Effort |
|----------|--------|---------------|--------|
| P0 | Python-first kind resolution (dict lookup) | HIGH | 2h |
| P0 | Pre-compiled prompt cache to disk | HIGH | 3h |
| P1 | Tiered model routing (Ollama for simple tasks) | HIGH | 4h |
| P1 | Python structural scoring (L1+L2 without LLM) | MEDIUM | 2h |
| P2 | Selective ISO loading (3-5 instead of 13) | MEDIUM | 2h |
| P2 | Result memoization (hash -> cache) | MEDIUM | 1h |
| P3 | Ollama overnight evolve mode | MEDIUM | 3h |
| P3 | Anthropic prompt caching integration | LOW (Max plan) | 2h |

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_mc_claude_opus_4]] | downstream | 0.37 |
| [[kc_tool_first_patterns]] | sibling | 0.28 |
| [[kc_token_optimization_map]] | sibling | 0.26 |
| [[claude_vs_free_decision_matrix]] | downstream | 0.26 |
| [[self_audit_n03_builder_20260408]] | sibling | 0.25 |
| [[spec_token_budget_optimization]] | downstream | 0.25 |
| [[spec_infinite_bootstrap_loop]] | related | 0.24 |
| [[p01_kc_claude_model_capabilities_2026]] | sibling | 0.24 |
| [[p01_kc_cex_project_overview]] | sibling | 0.22 |
| [[p01_kc_caching]] | sibling | 0.22 |
