---
quality: 9.1
quality: 8.4
id: kc_mcp_access_matrix
kind: knowledge_card
pillar: P09
title: "MCP Access Matrix -- Per-Nucleus Server Allocation"
version: "1.0.0"
created: "2026-04-20"
updated: "2026-04-20"
author: "knowledge-card-builder"
domain: security
tags: [security, mcp, access-control, open-source]
nucleus: N07
tldr: "Per-nucleus MCP server allocation: N07 is read-only gateway; N01 gets search/fetch; N03/N05 get GitHub write; N06 gets Stripe; zero paid keys required for base operation."
when_to_use: "Auditing MCP surface area, configuring a new contributor environment, or verifying least-privilege assignments per nucleus."
keywords: [mcp-access, nucleus-mcp, mcp-security, server-allocation]
long_tails:
  - "which MCP servers does each CEX nucleus have access to"
  - "how to run CEX without paid API keys"
axioms:
  - "NEVER grant N07 write operations on GitHub -- read-only by policy"
  - "ALWAYS mark optional premium MCP servers as disabled: true by default"
  - "IF a nucleus has no MCP config, it receives pre-compiled context from N07 handoffs only"
linked_artifacts:
  primary: null
  related: [kc_mcp_preflight_context]
density_score: 0.91
data_source: ".mcp-n0[1-7].json (ground truth)"
---

# MCP Access Matrix -- Per-Nucleus Server Allocation

## Quick Reference
```yaml
topic: mcp_access_matrix
scope: All 7 nuclei (N01-N07), Claude runtime only
owner: N07 (security authority)
criticality: high
```

## Overview

N07 is the sole MCP gateway for pre-flight context gathering. Each nucleus (N01-N06)
has its own MCP overlay (`.mcp-n0X.json`) for domain-specific tools when running on
Claude. Non-Claude runtimes (Codex, Gemini, Ollama) receive pre-compiled context via
N07 handoffs -- they never hold direct MCP credentials.

## Per-Nucleus MCP Matrix

| Nucleus | Config | Servers | Access Level | Purpose |
|---------|--------|---------|-------------|---------|
| N01 Intelligence | .mcp-n01.json | brave-search, fetch, firecrawl, markitdown, notebooklm | Read+Search | Research, competitive intel |
| N02 Marketing | .mcp-n02.json | markitdown, browser(puppeteer), canva, notebooklm | Read+Create | Creative assets, browser automation |
| N03 Engineering | .mcp-n03.json | github, fetch, canva | Read+Write | Code access, design assets |
| N04 Knowledge | .mcp-n04.json | supabase, postgres, fetch, firecrawl, notebooklm | Read+Query | Data ingestion, knowledge base |
| N05 Operations | .mcp-n05.json | github, postgres | Read+Write | CI/CD, infrastructure |
| N06 Commercial | .mcp-n06.json | fetch, markitdown, stripe, canva, notebooklm | Read+Transact | Business content, payments |
| N07 Orchestrator | .mcp-n07.json | github(read-only), fetch, markitdown, firecrawl(opt), brave-search(opt) | READ-ONLY | Pre-flight context gathering |

## N07 Security Constraints

1. **GitHub**: ONLY `get_*`, `list_*`, `search_*` operations. All create/update/merge/push/fork/delete DENIED by policy in `n07.json` comment and operational rules.
2. **Firecrawl**: ONLY scrape/search/map. `disabled: true` by default -- requires `FIRECRAWL_API_KEY`.
3. **Brave-search**: Read-only by nature. `disabled: true` by default -- requires `BRAVE_API_KEY`. Free tier: 2000 queries/month.
4. **Fetch**: No auth, public URLs only. No credential injection.
5. **Markitdown**: Pure document conversion, no auth, no external calls.

## Server Inventory

| Server | Auth Required | Default | Used By |
|--------|--------------|---------|---------|
| github | GITHUB_TOKEN | enabled | N03, N05, N07 |
| fetch | none | enabled | N01, N03, N04, N06, N07 |
| markitdown | none | enabled | N01, N02, N06, N07 |
| notebooklm | none | enabled | N01, N02, N04, N06 |
| browser(puppeteer) | none | enabled | N02 |
| canva | CANVA_CLIENT_ID+SECRET | enabled | N02, N03, N06 |
| postgres | DB URL | enabled | N04, N05 |
| supabase | SUPABASE_ACCESS_TOKEN | enabled | N04 |
| stripe | STRIPE_SECRET_KEY | enabled | N06 |
| firecrawl | FIRECRAWL_API_KEY | disabled(N07) | N01, N04, N07(opt) |
| brave-search | BRAVE_API_KEY | disabled(N07) | N01, N07(opt) |
| playwright | CDP endpoint | disabled(root) | N07(root) |

## Graceful Degradation

| Missing Key | Behavior |
|-------------|----------|
| GITHUB_TOKEN | GitHub server absent from session; no crash |
| FIRECRAWL_API_KEY | Server `disabled: true` by default; phase 0 skips silently |
| BRAVE_API_KEY | Server `disabled: true` by default; phase 0 skips silently |
| CANVA_CLIENT_ID/SECRET | Canva server unavailable; N02/N03/N06 lose design tool only |
| STRIPE_SECRET_KEY | Stripe unavailable; N06 loses payment operations only |
| SUPABASE_ACCESS_TOKEN | Supabase unavailable; N04 falls back to raw postgres or file KCs |
| All keys missing | Phase 0 returns empty external context; nuclei get ISOs + KCs only |

## Contributor Safety

- **Zero paid API keys** required for base functionality
- `fetch` + `markitdown` + `notebooklm` work with no keys
- `github` token is free (any GitHub account, read scope sufficient for N07)
- Optional premium providers (`firecrawl`, `brave-search`) clearly marked `disabled: true`
- Each `.mcp-n0X.json` is self-contained -- contributors activate only what they need

## References

- Config files: `.mcp-n01.json` through `.mcp-n07.json` (ground truth)
- Root union config: `.mcp.json` (N07 default when no overlay specified)
- N07 operational rules: `.claude/rules/n07-orchestrator.md`
- Preflight context tool: `_tools/cex_preflight.py`
