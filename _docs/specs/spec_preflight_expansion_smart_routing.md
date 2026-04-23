---
quality: 8.8
id: spec_preflight_expansion_smart_routing
kind: constraint_spec
pillar: P06
title: "Spec -- Pre-flight Context Injection + Smart Routing Enforcement"
version: 1.0.0
created: 2026-04-20
author: n07_orchestrator
domain: orchestration-infrastructure
quality_target: 9.0
status: SPEC
scope: N07 + cross-nucleus routing
depends_on: [spec_preflight_boot_integration, spec_token_budget_optimization]
tags: [spec, preflight, routing, mcp, security, multi-runtime, open-source]
tldr: "N07 becomes the sole MCP gateway; pre-compiles external context into handoffs so non-Claude runtimes get rich context without tool access."
density_score: 0.96
updated: "2026-04-22"
---

# Pre-flight Context Injection + Smart Routing Enforcement

## THE PROBLEM

CEX has 4 runtimes (Claude, Codex, Gemini, Ollama) but MCP access is
Claude-exclusive. When N07 dispatches a task to Codex/Gemini/Ollama, the
nucleus receives a thin handoff with zero external context (no web search,
no GitHub data, no database queries). This creates a 2-tier quality gap:

```
Claude nucleus:  handoff + MCP (github, brave, firecrawl, ...) = rich output
Other runtimes:  handoff only                                   = shallow output
```

The current preflight (`cex_preflight.py`) optimizes TOKEN BUDGET via
TF-IDF + Haiku reranking, but does NOT inject EXTERNAL CONTEXT from MCP
sources. It only selects ISOs and KCs from the local repo.

Additionally, `kinds_meta.json` has no `requires_tools` field, so the
router cannot distinguish tool-dependent tasks from structural generation.

## THE VISION

```
N07 (Opus, sole MCP gateway)
  |
  |-- [1] Resolve intent: kind, pillar, nucleus, verb
  |-- [2] Check kind metadata: requires_external_context?
  |-- [3] If YES: run preflight-mcp (gather external data via MCP)
  |-- [4] Inject gathered context into handoff file
  |-- [5] Router decides runtime: Claude (needs live tools) vs others (pre-compiled OK)
  |-- [6] Dispatch with fat handoff
  |
  v
Any runtime receives: handoff + pre-compiled external context
  → generates artifact from rich context
  → no MCP needed at runtime
```

**Principle: N07 is the brain. Nuclei are hands.** The brain gathers
intelligence; the hands execute. Hands don't need eyes if the brain
already looked.

## ARCHITECTURE

### A. N07 MCP Config (NEW: `.mcp-n07.json`)

N07 currently has NO MCP config. This spec gives N07 a curated,
**read-only** MCP set for pre-flight context gathering. NO write
capabilities. NO destructive operations.

#### Selected MCP Servers for N07

| Server | Why N07 needs it | Access level | Security | Tier |
|--------|------------------|-------------|----------|------|
| `fetch` | HTTP GET for web context injection | READ-ONLY | No secrets, no auth | DEFAULT (free) |
| `github` | Repo/issue context for code-related kinds | READ-ONLY | Token scoped to read | DEFAULT (free) |
| `markitdown` | Convert web pages to markdown for injection | READ-ONLY | No secrets | DEFAULT (free) |
| `firecrawl` | Web search + deep crawl for research kinds | READ-ONLY | API key (rate-limited) | OPTIONAL (needs key) |
| `brave-search` | Web search fallback | READ-ONLY | API key (rate-limited) | OPTIONAL (needs key) |

Config: `.cex/config/preflight_sources.yaml` controls which providers are active.
Users without API keys get github+fetch+markitdown (zero cost, zero setup).

#### Explicitly EXCLUDED from N07

| Server | Why excluded | Risk |
|--------|-------------|------|
| `playwright` | Browser automation is a BUILD tool, not a GATHER tool | Security: full browser control |
| `postgres` | Database queries are nucleus-specific, not orchestrator-level | Security: full DB write |
| `canva` | Design tool, not context gathering | Security: design API write |
| `notebooklm` | Session-stateful, requires interactive auth | Complexity + auth state |
| `stripe` | Payment API has zero pre-flight value | Security: financial data |
| `supabase` | Backend API with write access | Security: data mutation |

#### Security Constraints

1. **GITHUB_TOKEN must be read-only scoped**: create a separate PAT with
   `repo:read`, `issues:read`, `pull_requests:read` ONLY. Never use
   N03's write-capable token.
2. **BRAVE_API_KEY**: rate-limited by plan, no write capability. Safe.
3. **fetch**: no auth, no secrets. Accesses public URLs only. The MCP
   server already respects robots.txt via `--ignore-robots-txt` flag
   (removable for stricter compliance).
4. **No MCP server in N07 has write/delete/mutate capability.**

#### N07 Settings (NEW: `.claude/nucleus-settings/n07.json`)

```json
{
  "permissions": {
    "allow": [
      "Read(*)", "Write(*)", "Edit(*)", "Bash(*)",
      "Glob(*)", "Grep(*)", "Agent(*)",
      "mcp__fetch__*",
      "mcp__brave-search__*",
      "mcp__github__get_*",
      "mcp__github__list_*",
      "mcp__github__search_*",
      "mcp__markitdown__*"
    ],
    "deny": [
      "mcp__github__create_*",
      "mcp__github__update_*",
      "mcp__github__merge_*",
      "mcp__github__push_*",
      "mcp__github__fork_*",
      "mcp__github__delete_*"
    ]
  }
}
```

**Key: GitHub MCP is allowlisted for `get_*`, `list_*`, `search_*` only.
All mutating operations (`create_*`, `update_*`, `push_*`, `merge_*`)
are explicitly denied.** N07 can READ GitHub but never WRITE to it.

### B. kinds_meta.json Enhancement

Add `requires_external_context` field to every kind. This tells the
router whether a kind benefits from MCP-sourced pre-flight data.

#### Field Definition

```json
{
  "kind_name": {
    "requires_external_context": false,
    // ... existing fields
  }
}
```

Values:
- `false` (default): structural generation, repo context sufficient
- `true`: benefits from web search, GitHub data, or external sources

#### Classification Heuristic

| Pattern | `requires_external_context` | Reasoning |
|---------|---------------------------|-----------|
| Knowledge cards (kc_*) | `true` | Often need external sources, citations |
| Competitive analysis | `true` | Needs market data |
| Landing pages | `true` | May reference competitors, trends |
| Benchmark, case_study | `true` | Needs external data points |
| Agent, prompt_template | `false` | Internal structure only |
| Schema, type_def | `false` | Pure structural |
| Config kinds (env, rate_limit) | `false` | Internal settings |
| Workflow, dispatch_rule | `false` | Internal orchestration |

#### Estimated Split (293 kinds)

- `false`: ~220 kinds (75%) -- structural, internal
- `true`: ~73 kinds (25%) -- research-dependent, external-context-sensitive

### C. Pre-flight MCP Phase (NEW: Phase 3 in cex_preflight.py)

Current preflight has 2 phases:
1. LOCAL: TF-IDF ranking (ISOs + KCs)
2. CLOUD: Haiku/Ollama reranking

New architecture adds Phase 0 (before existing phases):

```
Phase 0: MCP GATHER (N07 only, pre-dispatch)
  |
  |-- Check kind.requires_external_context
  |-- If false: skip Phase 0, proceed to Phase 1
  |-- If true:
  |     |-- Determine context_queries from task description
  |     |-- Execute MCP calls:
  |     |     brave-search: 1-3 queries (top 5 results each)
  |     |     fetch: retrieve top 2-3 URLs from search results
  |     |     github: relevant issues/PRs if code-related
  |     |     markitdown: convert fetched HTML to markdown
  |     |-- Deduplicate + truncate to budget (max 8K tokens)
  |     |-- Write to .cex/cache/preflight/{nucleus}_{hash}_external.md
  |
Phase 1: LOCAL TF-IDF (existing, unchanged)
Phase 2: CLOUD reranking (existing, unchanged)
Phase 3: MERGE
  |-- Combine: external_context + selected_isos + selected_kcs
  |-- Total budget: 15K tokens (external gets max 8K, ISOs+KCs get 7K)
  |-- Output: single compiled preflight cache file
```

#### Important: Phase 0 runs ONLY in N07 context

N07 has MCP access. Nuclei do NOT run Phase 0. The flow is:

```
N07: resolve intent → preflight Phase 0 (MCP gather) → write handoff
     with external context baked in → dispatch to any runtime

Nucleus (any runtime): reads handoff → has external context already
     → runs Phase 1+2 for ISO/KC selection → produces artifact
```

### D. Smart Router Enhancement

#### Router Decision Tree (updated)

```python
def route_task(kind, task_signature, grid_size):
    meta = kinds_meta[kind]

    # Rule 1: If kind needs live tool access (not pre-compilable)
    if meta.get("requires_live_tools", False):
        return "claude"  # only Claude has MCP at runtime

    # Rule 2: If kind needs external context but pre-flight covers it
    if meta.get("requires_external_context", False):
        # N07 pre-flight already gathered external context
        # Any runtime can handle it now
        pass

    # Rule 3: Existing task signature routing
    return existing_router_logic(task_signature, grid_size)
```

#### New Field: `requires_live_tools`

A small subset of kinds need MCP AT RUNTIME (not pre-compilable):

| Kind | Why live tools | Count |
|------|---------------|-------|
| `browser_tool` | Needs to interact with live browser | 1 |
| `mcp_server` | Needs to test MCP connections | 1 |
| `interactive_demo` | Needs live browser rendering | 1 |
| `computer_use` | Needs live screen interaction | 1 |
| `db_connector` | Needs live database connection | 1 |

**~5 kinds out of 293** require live tools. These MUST route to Claude.
Everything else can be pre-flighted.

### E. Handoff Format Enhancement

Current handoff:
```markdown
## Task
Build kind=knowledge_card for competitive pricing analysis

## Context (pre-loaded for you)
- archetypes/builders/knowledge-card-builder/ (12 ISOs)
- P01_knowledge/library/kind/kc_knowledge_card.md
```

Enhanced handoff (with pre-flight external context):
```markdown
## Task
Build kind=knowledge_card for competitive pricing analysis

## Context (pre-loaded for you)
- archetypes/builders/knowledge-card-builder/ (12 ISOs)
- P01_knowledge/library/kind/kc_knowledge_card.md

## External Context (pre-compiled by N07 via MCP)
Source: brave-search + fetch + markitdown (gathered 2026-04-20T14:30:00)

### Search Results: "EdTech competitor pricing 2026"
1. Coursera: $49/mo individual, $399/yr teams (source: coursera.com/pricing)
2. Udemy Business: $30/user/mo (source: business.udemy.com)
3. LinkedIn Learning: $29.99/mo (source: linkedin.com/learning)
[... truncated to 8K token budget ...]

### GitHub Context
- Issue #142: "Add EdTech vertical pricing KC" (open, assigned N01)
- Related PR #138: "EdTech market research KC" (merged 2026-04-15)
```

The nucleus receives ALL external context without needing MCP. Any
runtime (Claude, Codex, Gemini, Ollama) can produce a rich artifact.

## ARTIFACTS

### Wave 1: Infrastructure (6 artifacts)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | `.mcp-n07.json` | config | 1KB | N07 MCP: fetch, github(read), markitdown (default) + firecrawl, brave (optional) |
| CREATE | `.claude/nucleus-settings/n07.json` | config | 1KB | Permissions: github read-only, deny mutations |
| CREATE | `.cex/config/preflight_sources.yaml` | config | 1KB | Tiered provider config (free defaults, opt-in premium) |
| REWRITE | `boot/cex.ps1` | boot_script | +10 lines | Add --mcp-config .mcp-n07.json |
| REWRITE | `boot/n07.ps1` | boot_script | +10 lines | Same MCP config wiring |
| REWRITE | `_tools/cex_boot_gen.py` | tool | +20 lines | N07 template gets MCP config |
| CREATE | `_docs/security/mcp_access_matrix.md` | knowledge_card | 3KB | Documents which nucleus gets which MCP, why |

### Wave 2: kinds_meta Enhancement (3 artifacts)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| REWRITE | `.cex/kinds_meta.json` | registry | +293 fields | Add requires_external_context to all 293 kinds |
| CREATE | `_tools/cex_kind_classifier.py` | tool | 3KB | Classify kinds by external context need (batch) |
| CREATE | `_docs/security/kind_tool_dependency_matrix.md` | knowledge_card | 4KB | Maps all 293 kinds to tool requirements |

### Wave 3: Pre-flight Phase 0 (4 artifacts)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| REWRITE | `_tools/cex_preflight.py` | tool | +150 lines | Add Phase 0: MCP gather (brave+fetch+github+markitdown) |
| CREATE | `_tools/cex_preflight_mcp.py` | tool | 5KB | Standalone MCP gather module (imported by preflight) |
| REWRITE | `.cex/P09_config/nucleus_models.yaml` | config | +10 lines | Add preflight_mcp section with budget/timeout config |
| CREATE | `_tools/tests/test_preflight_mcp.py` | test | 3KB | Unit tests for Phase 0 (mocked MCP calls) |

### Wave 4: Router Enhancement (3 artifacts)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| REWRITE | `_tools/cex_router_v2.py` | tool | +40 lines | Add requires_external_context + requires_live_tools routing |
| REWRITE | `_spawn/dispatch.sh` | tool | +10 lines | Pre-flight MCP call before non-Claude dispatch |
| CREATE | `_tools/tests/test_router_kind_routing.py` | test | 3KB | Routing tests for kind-based decisions |

### Wave 5: Handoff Format + Documentation (4 artifacts)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| REWRITE | `.claude/rules/dispatch-depth.md` | rule | +20 lines | Document external context section in handoffs |
| REWRITE | `.claude/rules/n07-orchestrator.md` | rule | +15 lines | N07 MCP pre-flight protocol |
| CREATE | `_docs/specs/spec_mcp_security_policy.md` | constraint_spec | 4KB | MCP security policy for open-source |
| REWRITE | `CLAUDE.md` | context_doc | +5 lines | Update N07 row: MCP pre-flight gateway |

## WAVE ORDER + DEPENDENCIES

```
Wave 1: Infrastructure (N07 MCP config + boot wiring)
  |  no dependencies -- pure config
  v
Wave 2: kinds_meta Enhancement (field addition + classifier)
  |  depends on: Wave 1 (N07 needs MCP to validate classification)
  v
Wave 3: Pre-flight Phase 0 (MCP gather module)
  |  depends on: Wave 1 (needs .mcp-n07.json) + Wave 2 (needs kind metadata)
  v
Wave 4: Router Enhancement (kind-based routing)
  |  depends on: Wave 2 (reads requires_external_context) + Wave 3 (pre-flight available)
  v
Wave 5: Documentation + Rules (handoff format, security docs)
  |  depends on: all prior waves (documents what was built)
```

## DECISIONS NEEDED (GDP)

| # | Decision | Options | Recommended | Why |
|---|----------|---------|-------------|-----|
| DP1 | GitHub token scope for N07 | (a) share N03's token (b) separate read-only PAT | **LOCKED: (a)** | User chose simplicity; single token for all nuclei |
| DP2 | External context token budget | (a) 4K (b) 8K (c) 12K | **LOCKED: (b) 8K** | 8K external + 7K ISOs/KCs = 15K total per handoff |
| DP3 | Pre-flight timeout | (a) 10s (b) 30s (c) 60s | **LOCKED: (c) 60s** | Generous timeout for network-bound MCP calls |
| DP4 | Search strategy | Tiered: free defaults + optional premium | **LOCKED: tiered** | github+fetch+markitdown free; firecrawl/brave opt-in via preflight_sources.yaml |
| DP5 | Classify all 293 kinds now or incrementally? | (a) all at once (b) top 50 first | **LOCKED: (a)** | One-time batch classification from kind descriptions |

## SECURITY POLICY (for open-source)

### Token Safety

1. **No secrets in repo**: `.env` is gitignored. `.mcp-n07.json` references
   `${GITHUB_TOKEN}` (env var), never hardcoded values.
2. **Scoped tokens**: N07's GitHub token MUST be a separate read-only PAT.
   Document this in setup guide.
3. **Graceful degradation**: if BRAVE_API_KEY is missing, skip search.
   If GITHUB_TOKEN is missing, skip GitHub context. Pre-flight never
   fails hard on missing MCP credentials.
4. **No credential logging**: `cex_preflight_mcp.py` must never log
   API keys, tokens, or auth headers. Log only: query, result count,
   latency.
5. **Rate limiting**: brave-search has RPM limits. Preflight must
   respect them: max 3 queries per preflight run, 1s delay between.

### Contributor Safety

1. **MCP servers are optional**: contributors without API keys get
   Phase 0 skipped automatically. The system still works (just no
   external context enrichment).
2. **No paid services required**: fetch + markitdown + github(read)
   work without paid API keys. Only brave-search needs a key (free
   tier: 2000 queries/mo).
3. **Audit trail**: every Phase 0 run logs to
   `.cex/cache/preflight/{hash}_audit.json` with: queries made,
   URLs fetched, tokens consumed, wall time.

## DONE WHEN

- [ ] `.mcp-n07.json` exists with 4 read-only MCP servers
- [ ] `.claude/nucleus-settings/n07.json` denies all GitHub mutations
- [ ] `boot/cex.ps1` and `boot/n07.ps1` pass `--mcp-config .mcp-n07.json`
- [ ] `kinds_meta.json` has `requires_external_context` on all 293 kinds
- [ ] `cex_preflight.py` Phase 0 gathers external context via MCP
- [ ] `cex_router_v2.py` routes `requires_live_tools` kinds to Claude-only
- [ ] Handoff format includes `## External Context` section
- [ ] Security docs in `_docs/security/` cover MCP access matrix
- [ ] All 20 artifacts pass `cex_doctor.py`
- [ ] Pre-flight gracefully degrades with missing API keys (no crash)
- [ ] Unit tests pass for preflight_mcp and router_kind_routing

## ESTIMATED EFFORT

| Wave | Artifacts | Nucleus | Runtime | Est. Time |
|------|-----------|---------|---------|-----------|
| W1 | 6 | N07 + N05 | Claude | 15 min |
| W2 | 3 | N07 + N04 | Claude | 20 min |
| W3 | 4 | N03 + N05 | Claude | 30 min |
| W4 | 3 | N03 + N05 | Claude | 20 min |
| W5 | 4 | N04 + N07 | Claude | 15 min |
| **Total** | **20** | **4 nuclei** | **Claude** | **~100 min** |
