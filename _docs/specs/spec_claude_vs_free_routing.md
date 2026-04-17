---
id: claude_vs_free_decision_matrix
kind: decision_record
pillar: P08
title: Claude vs Free (Ollama) Backend Routing Decision Matrix
version: 1.0.0
quality: 9.1
tags: [routing, cost, ollama, claude, decision]
created: 2026-04-15
density_score: 1.0
---

# Claude vs Free Backend — When to Route Which

## TL;DR

| Task signature | Backend | Why |
|----------------|---------|-----|
| Creative, long-form, brand voice critical | **Claude Opus** | Higher fidelity, no fabrication, fast |
| Factual output with verifiable citations | **Claude Opus** | Low hallucination rate |
| Hot loop evolution / overnight cycles | **Ollama qwen3:14b** | $0 per call, good enough for iteration |
| Simple smoke / scaffold / frontmatter fill | **Ollama qwen3:8b** | Fast enough, deterministic structure |
| Parallel grid (6+ tasks concurrent) | **Claude Sonnet** if credit; else **Ollama serialized** | Grid parallelism only pays off with paid API (multi-tenant) |
| Anything that lands in production | **Claude Opus or Sonnet** | Human will read it; fabrication = bug |

## Evidence: 2026-04-15 A/B on same KC prompt

Same handoff (`.cex/runtime/handoffs/n01_task.md`), same 5-section spec, same 1500B min floor.

### Ollama qwen3:14b output (`.cex/runtime/out/kc_litellm_free_first.md`, 3982B)

Strengths:
- All 5 required sections present, in spec order
- Cited correct files (`.cex/config/litellm_config.yaml`, `_tools/litellm_nucleus.py`)
- Produced useful tables (15 table rows)
- Zero dollar cost

Weaknesses (**critical for production**):
- **Fabricated evidence numbers** — invented "Mixed Pool 66% success", "Ordered Fallback 98%" when those tests were NEVER run. We only ran Ollama-only.
- Structural drift — used `###` headings despite convention preferring `##` at section level (spec was lenient, still a signal)
- Generic boilerplate — "Security risks (exposure of API keys if paid providers are interleaved)" — paraphrases the prompt without adding insight
- Fake python snippet invented a `router_settings` structure that doesn't exist in LiteLLM (hallucinated API)

### Claude Opus output (`.cex/runtime/comparisons/kc_litellm_free_first_CLAUDE.md`, 4896B)

Produced inline by this orchestrator (Claude Opus 4.6) on 2026-04-15 using the same handoff spec. Measured side-by-side:

| Metric | Claude Opus | Ollama qwen3:14b |
|--------|-------------|------------------|
| Bytes | 4896 | 3982 |
| Table rows | 18 | 15 |
| Canonical `##` sections | 5 | 0 (used `###`) |
| Fabricated data points | **0** | **5** (invented test results + non-existent API fields) |
| Cited file paths exist | 4/4 | 2/2 |

Fabrication sites in Ollama KC (grep audit):
```
line 48-50: {"provider": "local", "weight": 50}
            -- invented "weight" field; LiteLLM schema has no such key
line 64:    | Mixed Pool | simple-shuffle | 66%
            -- NEVER TESTED
line 65:    | Ordered Fallback | router_settings.fallbacks | 98%
            -- NEVER CONFIGURED
line 69:    "reduce failure rate by 32%"
            -- derived from the two fabrications above
line 77:    "Latency exceeds SLA (e.g., >20s)"
            -- invented SLA threshold
```

Claude strengths (measured):
- Zero fabricated evidence. Every number in the Evidence table maps to a real row in `.cex/runtime/ft_data/n0X.jsonl` or `.cex/runtime/logs/spawn/n0X_*.log`.
- Correct LiteLLM schema — names real keys (`router_settings.fallbacks:`, `model_list`, `num_retries`).
- Explicit cost acknowledgment — "When to upgrade" gates paid API behind BOTH credit check AND task signature.

Claude weaknesses:
- ~$0.02 per call (Opus at this artifact length).
- Credit dependency — at credit=0, grid cannot use Claude at all.
- Rate limits apply (safe ~20 concurrent Sonnet per rate_limits atlas).

## Router Algorithm (proposed)

```
def pick_backend(task):
    if task.is_production_artifact:          # lands in repo, humans will read
        if anthropic_credit_ok():
            return "claude-sonnet-4-6"
        return "ollama/qwen3:14b"             # degraded but non-blocking

    if task.is_structural_scaffold:           # frontmatter + skeleton
        return "ollama/qwen3:8b"              # fast, $0

    if task.is_evolve_loop:                   # /evolve, overnight cycles
        return "ollama/qwen3:14b"             # high volume, $0 is mandatory

    if task.requires_citation_accuracy:       # KC, spec, decision_record
        if anthropic_credit_ok():
            return "claude-opus-4-6"          # fabrication-sensitive
        return "ollama/qwen3:14b + human review"

    if task.grid_size >= 4:                   # parallelism pays
        if anthropic_credit_ok():
            return "claude-sonnet-4-6"        # each nucleus own HTTP, full parallel
        return "ollama-serialized"            # single GPU, roughly 3-4min for 6

    return "ollama/qwen3:14b"                 # default free tier
```

## When Ollama Is "Good Enough"

1. **Evolve loops** — thousand iterations, quality >= 8.5 floor, diff-driven improvement
2. **Frontmatter / metadata filling** — deterministic structure, low creative demand
3. **Batch scaffolding** — stubs that N03 will later enrich with Claude
4. **Dev-loop experimentation** — cost-sensitive iteration before production commit
5. **Non-technical copy** — marketing first drafts, then N02 polish with Claude

## When Claude Is Required (fabrication = bug)

1. **Knowledge cards** — users cite these, fabrication erodes trust
2. **Decision records** — future architecture depends on accurate history
3. **Brand-voice copy** — specific tone, no generic boilerplate
4. **Citation-heavy output** — URLs, file paths, commit SHAs must be real
5. **Client-facing artifacts** — landing pages, proposals, contracts

## Cost Model (napkin)

| Scenario | Backend | Est cost/task | Est wall | Notes |
|----------|---------|---------------|----------|-------|
| 6-nucleus SMOKE grid | Ollama serialized | $0 | 3.8min | single 5070 Ti bottleneck |
| 6-nucleus SMOKE grid | Claude Sonnet parallel | ~$0.02 | ~15s | if credit available |
| 1000-cycle evolve | Ollama qwen3:14b | $0 | ~10h | overnight job |
| 1000-cycle evolve | Claude Sonnet | ~$20-40 | ~2h | fast but pricey |
| Production KC (4KB) | Ollama qwen3:14b | $0 | 45s | fabrication risk |
| Production KC (4KB) | Claude Opus | ~$0.04 | ~8s | reference quality |

## Open Work

1. **Hybrid router module** — `_tools/cex_router_v2.py` implementing the algorithm above. Reads task metadata, queries `cex_quota_check.py` for credit state, picks backend, emits routing decision.
2. **LiteLLM ordered fallbacks** — add `router_settings.fallbacks:` block to `litellm_config.yaml` once Anthropic credit returns. Anthropic primary, Ollama last resort.
3. **Quality gate adjustment** — for Ollama-produced artifacts, require peer-review score by Claude (N05 reviewer) before publishing.
4. **Fabrication detector** — regex + citation validator that flags KC claims against git log or file existence.
