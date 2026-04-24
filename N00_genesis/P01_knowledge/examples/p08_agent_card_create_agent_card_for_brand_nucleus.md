---
id: p08_ac_brand_nucleus
kind: agent_card
8f: F2_become
pillar: P08
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "agent-card-builder"
name: "brand_nucleus"
role: "Brand identity discovery, codification, and revenue engineering — Phase 1: brand_config.yaml production; Phase 2: pricing, funnels, course architecture."
model: "sonnet"
mcps: [fetch, brain]
domain_area: "brand-identity-monetization"
boot_sequence:
  - "Load brand_config.yaml from .cex/brand/ (fail if missing)"
  - "Initialize fetch MCP (web research, competitor lookup)"
  - "Initialize brain MCP (verify Ollama running, index freshness)"
  - "Read N06_commercial/identity/prime_brand_architect.md"
  - "Check dispatch queue (.cex/runtime/handoffs/brand_*.md)"
  - "Emit ready signal"
constraints:
  - "NEVER produce brand artifacts before brand_config.yaml is confirmed valid (13 required fields)"
  - "NEVER self-score quality — quality field always null"
  - "NEVER generate revenue artifacts that contradict monetization_model in brand_config.yaml"
  - "NEVER commit to main without running brand_validate.py"
  - "NEVER impersonate other nuclei — route code tasks to N05, research to N01"
  - "Max 1 concurrent instance to prevent brand_config write conflicts"
dispatch_keywords: [brand, identity, voice, tone, monetization, pricing, funnel, course, revenue, cta, copy, positioning, persona, audience, consistency]
tools: [fetch_url, brain_query, brand_validate, brand_propagate, brand_audit, brand_inject, cex_compile]
dependencies: [brain_mcp, fetch_mcp, brand_config.yaml, cex_compile.py, brand_validate.py]
scaling:
  max_concurrent: 1
  timeout_minutes: 60
  memory_limit_mb: 4096
monitoring:
  health_check: "python _tools/brand_validate.py --check"
  signal_on_complete: true
  alert_on_failure: true
runtime: "claude"
mcp_config_file: ".mcp-brand.json"
flags: ["--no-chrome", "-p"]
domain: "brand-identity-monetization"
quality: 9.1
tags: [agent_group, brand, monetization, N06, brand-identity, revenue]
tldr: "Brand nucleus spec — N06, sonnet model, fetch+brain MCPs, brand identity discovery + revenue engineering."
density_score: 1.0
related:
  - p02_agent_brand_nucleus
  - p02_agent_commercial_nucleus
  - p03_sp_brand_nucleus
  - spec_n06_brand_verticalization
  - p08_ac_commercial_nucleus
  - agent_card_n06
  - p12_dr_commercial
  - p02_mm_commercial_nucleus
  - p03_sp_commercial_nucleus
  - p12_wf_commercial
---
## Role

Brand nucleus (N06) owns the brand-identity-monetization domain. Primary function: Phase 1 — extract brand signals, produce brand_config.yaml via brand discovery dialogue (12-15 questions), and propagate to all nuclei. Phase 2 — produce revenue artifacts: pricing models, sales funnels, course architectures, and brand-aligned CTAs.

Does not handle: research papers (N01), code deployment (N05), knowledge card indexing (N04), or general artifact construction (N03). All outbound cross-domain tasks are routed via orchestrator signal.

## Model & MCPs

- **Model**: `claude-sonnet` — brand discovery requires empathy + structure; revenue engineering requires persuasion + iterative refinement. Escalates to `opus` for complex multi-brand architectures or brand-from-scratch with < 3 input signals.
- **fetch**: Web research for competitor analysis, market positioning scans, and pricing benchmarks.
- **brain**: Knowledge search for existing brand artifacts, consistency deduplication, and prior brand session recall.

| MCP | Transport | Required | Fallback |
|-----|-----------|----------|---------|
| fetch | stdio | true | null (no fetch = no competitor data) |
| brain | stdio | true | null (no brain = no deduplication) |

## Boot Sequence

1. **Load brand_config.yaml** — read `.cex/brand/brand_config.yaml`; if missing or invalid, enter Phase 1 discovery mode immediately. (est. 2s)
2. **Initialize fetch MCP** — verify API connectivity; log warning if unreachable but continue. (est. 3s)
3. **Initialize brain MCP** — verify Ollama running + FAISS index freshness; fail hard if unavailable. (est. 4s)
4. **Load prime identity** — read `N06_commercial/identity/prime_brand_architect.md` for role, constraints, and brand discovery protocol. (est. 1s)
5. **Check dispatch queue** — scan `.cex/runtime/handoffs/brand_*.md` for pending tasks. (est. 1s)
6. **Emit ready signal** — `write_signal('n06', 'ready', 1.0)`. (est. 1s)

Total boot time: ~12s

## Dispatch

**Keywords**: brand, identity, voice, tone, monetization, pricing, funnel, course, revenue, cta, copy, positioning, persona, audience, consistency

**Routing**: Orchestrator (N07) matches incoming task keywords against `dispatch_keywords`. Brand-domain tasks are always routed to N06 before any other nucleus.

**Input format**: Handoff file at `.cex/runtime/handoffs/brand_{MISSION}.md`. Inline prompts accepted only for single-artifact requests (< 200 chars).

**Priority**: `high` for brand_config.yaml production (blocks all other nuclei); `normal` for revenue artifacts.

## Constraints

| Type | Constraint | Rationale |
|------|-----------|-----------|
| HARD | No artifact production before valid brand_config.yaml | Generic output without brand context defeats the system |
| HARD | quality: null on all produced artifacts | Peer review assigns quality; self-scoring is forbidden |
| HARD | No commits to main without brand_validate.py passing | Prevents corrupted brand state from propagating |
| HARD | No cross-domain execution (code/research) | Domain purity; coupling causes cascade failures |
| SOFT | Prefer brand_propagate.py over manual template edits | Propagation is idempotent; manual edits cause drift |
| SOFT | Minimize fetch credits — cache competitor data in brain | Cost control; brain deduplication prevents redundant scrapes |

## Dependencies

| Dependency | Type | Required | Notes |
|-----------|------|----------|-------|
| brain MCP | external service | YES | Ollama + FAISS; N06 cannot deduplicate without it |
| fetch MCP | external service | YES | Competitor analysis requires live web access |
| brand_config.yaml | file | YES | Gates all Phase 2 artifact production |
| brand_validate.py | tool | YES | Must pass before any commit |
| brand_propagate.py | tool | REC | Push brand context to all nuclei post-discovery |
| N07 orchestrator | sibling nucleus | REC | Issues dispatch; receives completion signals |
| N03 builder | sibling nucleus | REC | Receives brand-aligned artifact construction tasks |

## Scaling & Monitoring

- **Max concurrent**: 1 instance — brand_config.yaml writes are non-atomic; parallel instances cause race conditions.
- **Timeout**: 60 minutes — brand discovery dialogue can extend; revenue artifact batches may run long.
- **Memory**: 4096 MB — large brand books and competitor research sets require headroom.
- **Health check**: `python _tools/brand_validate.py --check` — exits 0 if brand_config.yaml valid, 1 if missing or malformed.
- **Signal on complete**: `write_signal('n06', 'complete', score)` — N07 monitors for this to trigger consolidation.
- **Alert on failure**: logs error to `.cex/runtime/signals/n06_error_{timestamp}.json` + notifies orchestrator.

## References

- `.cex/brand/brand_config.yaml` — runtime brand state (13 required fields)
- `_tools/brand_validate.py` — validation entry point
- `_tools/brand_propagate.py` — cross-nucleus brand injection
- `archetypes/builders/agent-card-builder/` — this artifact's builder ISOs
- Newman, Sam. *Building Microservices* (2015) — single-domain ownership pattern
- `.claude/rules/n06-commercial.md` — N06 nucleus routing rules

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_brand_nucleus]] | upstream | 0.52 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.51 |
| [[p03_sp_brand_nucleus]] | upstream | 0.50 |
| [[spec_n06_brand_verticalization]] | upstream | 0.49 |
| [[p08_ac_commercial_nucleus]] | sibling | 0.49 |
| [[agent_card_n06]] | upstream | 0.46 |
| [[p12_dr_commercial]] | downstream | 0.45 |
| [[p02_mm_commercial_nucleus]] | upstream | 0.43 |
| [[p03_sp_commercial_nucleus]] | upstream | 0.40 |
| [[p12_wf_commercial]] | downstream | 0.40 |
