---
id: n06_self_audit_20260408
kind: context_doc
pillar: P01
title: "N06 Self-Audit -- Commercial Tools & MCP Status (Claude-Native)"
version: 1.0.0
created: 2026-04-08
author: n06_commercial
nucleus: N06
domain: commercial-audit
quality: 9.0
tags: [self-audit, N06, mcp, tools, claude-native, commercial]
tldr: "N06 MCP audit: 2/6 servers working (fetch, notebooklm-partial), 2/6 need auth (canva, notebooklm), 2/6 not loaded (stripe, hotmart). Brand tools: 5/5 scripts exist. Claude Code features: --name, --continue already available."
density_score: 0.92
related:
  - agent_card_n06
  - self_audit_newpc_2026_04_13
  - p02_mm_commercial_nucleus
  - p08_ac_brand_nucleus
  - n06_sdk_validation_audit
  - spec_n06_brand_verticalization
  - self_audit_newpc_n02
  - p02_agent_commercial_nucleus
  - p02_agent_brand_nucleus
  - p08_ac_commercial_nucleus
---

# N06 Self-Audit -- Commercial Tools & MCP Status

> Audit date: 2026-04-08 | Mission: CLAUDE_NATIVE | Wave: 2
> Runtime: Claude Code native (opus-4-6, 1M context, Anthropic Max)

---

## 1. MCP Server Status

| Server | Config | Loaded | Auth | Status | ROI Assessment |
|--------|--------|--------|------|--------|----------------|
| **fetch** | .mcp-n06.json | YES | N/A | WORKING | HIGH -- competitor scraping, market research. Zero cost. |
| **markitdown** | .mcp-n06.json | YES | N/A | AVAILABLE | MEDIUM -- doc ingestion for brand discovery. Needs testing. |
| **canva** | .mcp-n06.json | YES | FAIL (401) | BROKEN | MEDIUM -- visual identity generation. Needs CANVA_CLIENT_ID + SECRET. |
| **notebooklm** | .mcp-n06.json | YES | NOT AUTH | PARTIAL | HIGH -- content repurposing pipeline. Server healthy, needs setup_auth. |
| **stripe** | .mcp-n06.json | NO | N/A | NOT LOADED | HIGH -- revenue data, subscription management. Needs STRIPE_SECRET_KEY env var. |
| **hotmart** | .mcp-n06.json | NO | N/A | NOT LOADED | MEDIUM -- course sales data. Needs HOTMART_CLIENT_ID + SECRET + BASIC_AUTH. |

### Summary

- **Working**: 1/6 (fetch)
- **Partial**: 2/6 (markitdown available, notebooklm healthy but unauthenticated)
- **Broken**: 1/6 (canva -- 401 invalid_access_token)
- **Not loaded**: 2/6 (stripe, hotmart -- env vars missing)

### Fix Priority (by revenue impact)

1. **Stripe** -- direct revenue visibility. Set `STRIPE_SECRET_KEY` in environment.
2. **NotebookLM** -- content distribution pipeline. Run `setup_auth` with Google account.
3. **Canva** -- brand asset generation. Set `CANVA_CLIENT_ID` + `CANVA_CLIENT_SECRET`.
4. **Hotmart** -- course sales. Set 3 env vars. Lower priority until courses launch.

---

## 2. Brand Tools Status

| Tool | Script | Exists | Windows-Safe | Notes |
|------|--------|--------|-------------|-------|
| brand_inject.py | _tools/brand_inject.py | YES | YES | Replaces {{BRAND_*}} tokens. Functional. |
| brand_validate.py | _tools/brand_validate.py | YES | YES | Validates brand_config.yaml (13 required fields). |
| brand_propagate.py | _tools/brand_propagate.py | YES | PARTIAL | Pushes brand to all nuclei. Some Windows path issues reported in prior audit. |
| brand_audit.py | _tools/brand_audit.py | YES | PARTIAL | Scores brand consistency. Some encoding issues on cp1252 terminals. |
| brand_ingest.py | _tools/brand_ingest.py | YES | YES | Scans messy folders for brand signals. |

### Tool Health: 5/5 exist, 3/5 fully Windows-safe, 2/5 have encoding edge cases.

**Recommendation**: Run `python _tools/cex_sanitize.py --fix --scope _tools/brand_*` to ensure ASCII compliance on all brand tools.

---

## 3. N06 Artifact Inventory (2026-04-08)

| Subdir | Count | Delta from 04-02 |
|--------|------:|-------------------|
| agents/ | 3 | +2 (axiom, mental_model) |
| architecture/ | 4 | +3 (patterns: brand, pricing, funnel) |
| compiled/ | 19 | +6 |
| feedback/ | 1 | -- |
| knowledge/ | 12 | +2 |
| memory/ | 3 | +3 (NEW subdir) |
| orchestration/ | 4 | +2 |
| output/ | 17 | +8 (brand book, voice guide, visual identity, etc.) |
| prompts/ | 6 | +2 |
| quality/ | 1 | -- |
| schemas/ | 4 | -- |
| tools/ | 3 | +2 (pricing experiment, funnel diagnostic) |
| **TOTAL** | **77** | **+28 since 04-02** |

**Growth rate**: 28 artifacts in 6 days = 4.7 artifacts/day. Healthy pace.

---

## 4. PI Reference Scan Result

| Search Pattern | Hits in N06_commercial/ |
|----------------|------------------------|
| pi_wrapper, PI app, prompt intelligence | **0** |
| npm package, app store | **0** |
| wrapper (as delivery mechanism) | **0** |
| subscription (as pricing model -- LEGITIMATE) | 40+ (all valid) |

**Verdict**: N06 is **CLEAN** of PI references. No remediation needed.

---

## 5. Model Configuration

| Field | Old Value | Current Value | Source |
|-------|-----------|---------------|--------|
| agent_card model | sonnet | **opus-4-6** | Fixed this audit |
| agent_card tldr | "Sonnet model" | **"Opus 4.6 model"** | Fixed this audit |
| nucleus_models.yaml | opus-4-6 | opus-4-6 | Already correct |
| .mcp-n06.json | 6 servers | 6 servers | Current |

---

## 6. Claude Code Features Assessment

| Feature | Available | N06 Value |
|---------|-----------|-----------|
| `--name` (session naming) | YES | Tag sessions: "brand-discovery", "pricing-audit" |
| `--continue` (session resume) | YES | Resume long brand discovery interviews |
| `--fork-session` (safe context resume) | YES | Branch pricing experiments without losing main context |
| Sub-agents (5 parallel) | YES | Run brand audit + pricing + funnel in parallel |
| 1M context window | YES | Load ALL 12 brand KCs (180KB) + full brand book in one session |
| MCP servers | YES | 6 configured, 1-3 working |
| Hooks (pre-commit) | YES | ASCII enforcement on all code output |

### Claude Code Features N06 Should Leverage More

1. **Sub-agents for parallel brand audit**: Spawn 3 agents -- one per dimension (voice, visual, positioning) -- score in parallel
2. **Session naming for brand discovery**: `--name brand-discovery-clientX` keeps context clean
3. **Fork for pricing experiments**: Test 3 pricing models in forked sessions, compare results
4. **1M context for full brand ingestion**: Load competitor docs + brand book + all KCs simultaneously

---

## 7. Gaps & Recommendations

| Gap | Severity | Action | ROI |
|-----|----------|--------|-----|
| Stripe MCP not connected | HIGH | Set STRIPE_SECRET_KEY env var | Direct revenue visibility |
| NotebookLM not authenticated | HIGH | Run setup_auth with {{BRAND_EMAIL}} | Content distribution pipeline |
| Canva auth broken | MEDIUM | Refresh CANVA_CLIENT_ID + SECRET | Visual asset automation |
| No golden tests for commercial outputs | MEDIUM | Create test fixtures in N06_commercial/tests/ | Quality regression detection |
| Only 2 dedicated builders (content_monetization, tagline) | LOW | Register pricing-builder, funnel-builder in kinds_meta.json | Wider commercial artifact coverage |
| brand_propagate/audit Windows encoding | LOW | Run cex_sanitize.py --fix | Eliminates cp1252 crashes |

---

## ROI Summary

**Cost of this audit**: ~10 minutes of N06 context
**Value**: Identified 2 HIGH-priority MCP fixes (Stripe, NotebookLM) that unlock revenue visibility and content distribution. Fixed stale model references. Confirmed PI cleanup complete.
**Next action**: Fix Stripe env var (5 seconds, unlocks payment data), then NotebookLM auth (2 minutes, unlocks content pipeline).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n06]] | sibling | 0.46 |
| [[self_audit_newpc_2026_04_13]] | sibling | 0.42 |
| [[p02_mm_commercial_nucleus]] | downstream | 0.40 |
| [[p08_ac_brand_nucleus]] | downstream | 0.39 |
| [[n06_sdk_validation_audit]] | sibling | 0.39 |
| [[spec_n06_brand_verticalization]] | downstream | 0.38 |
| [[self_audit_newpc_n02]] | sibling | 0.35 |
| [[p02_agent_commercial_nucleus]] | downstream | 0.34 |
| [[p02_agent_brand_nucleus]] | downstream | 0.32 |
| [[p08_ac_commercial_nucleus]] | downstream | 0.32 |
