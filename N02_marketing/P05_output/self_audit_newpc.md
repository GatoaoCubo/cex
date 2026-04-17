---
id: self_audit_newpc_n02
kind: context_doc
pillar: P08
title: "N02 Self-Audit -- New PC Setup (2026-04-13)"
nucleus: N02
version: 1.2.0
quality: 8.2
density_score: 0.99
created: 2026-04-12
updated: 2026-04-13
mission: NEWPC_SETUP
---

# N02 Self-Audit -- New PC Setup

> Fresh Windows 11 machine. Everything verified from scratch.
> Updated: 2026-04-13 | Model: opus-4-6 (1M context) | CLI: claude

---

## Phase 1: MCP Server Verification

| Server | Config Package | Status | Verdict | Action Taken |
|--------|---------------|--------|---------|--------------|
| **markitdown** | `markitdown-mcp-npx` | Package corrected in config. | FIXED | Updated `.mcp-n02.json` from `markitdown-mcp` (404) to `markitdown-mcp-npx`. |
| **browser (puppeteer)** | `@modelcontextprotocol/server-puppeteer` | Package corrected in config (was fixed in prior session). | PASS | Config already uses correct package. |
| **canva** | `@mcp_factory/canva-mcp-server` | `CANVA_CLIENT_ID`=NOT SET, `CANVA_CLIENT_SECRET`=NOT SET. Package untested. | BLOCKED | Env vars required. Not a code issue. |
| **notebooklm** | `notebooklm-mcp@latest` | Starts. Banner: "NotebookLM MCP Server v1.0.0" | PASS | None. |

**MCP Score: 2/4 PASS** -- markitdown now fixed. Browser already fixed. Canva blocked on env vars.

> Delta from v1.1.0 (2026-04-12): markitdown package corrected in this session. Browser was already corrected.
> Note: `@modelcontextprotocol/server-puppeteer` is marked deprecated upstream. Monitor for maintained replacement.

---

## Phase 2: Python Tools Audit

| Tool | Command | Result | Status |
|------|---------|--------|--------|
| `cex_compile.py` | `--help` | Usage printed. Supports `--all`, `--target`, `--output`. | PASS |
| `cex_doctor.py` | `--help` | Banner: "CEX Doctor v2.0 -- Naming v2.0 + Density + 13-File Completeness" | PASS |
| `cex_score.py` | `--help` | Usage printed. Supports `--dry-run`, `--apply`, `--hybrid`, `--verbose`. | PASS |

**Python Tools Score: 3/3 PASS** -- All core pipeline tools operational.

No missing pip packages detected for these entry points.

---

## Phase 3: Artifact Inventory

### By Subdirectory

| Subdirectory | .md Count | Delta vs v1.1 | Role |
|-------------|-----------|---------------|------|
| `agents/` | 1 | -- | Agent identity |
| `architecture/` | 1 | -- | P08 agent card |
| `artifacts/` | 3 | -- | Templates (ad, email, landing page) |
| `compiled/` | ~53 yaml | -- | Auto-compiled artifacts |
| `config/` | 2 | -- | A/B testing + brand override |
| `feedback/` | 1 | -- | Quality gate for marketing |
| `knowledge/` | 17 | +3 | Domain KCs -- 3 new: developer_experience_patterns, llm_agent_frameworks_comparison, open_source_ai_ecosystem |
| `memory/` | 2 | -- | Campaign performance + copy insights |
| `orchestration/` | 5 | -- | Dispatch rules + handoffs + workflows |
| `output/` | 16 | +3 | Landing pages, emails, social, reports |
| `prompts/` | 7 | +3 | System prompt + action prompt + templates (3 notebooklm/distribution tpls added) |
| `quality/` | 1 | -- | Scoring rubric |
| `reports/` | 1 | -- | This self-audit |
| `schemas/` | 5 | -- | Design tokens, a11y, responsive, tailwind |
| `tools/` | 3 | -- | Copy analyzer + headline scorer + social publisher |
| `workflows/` | 1 | -- | KC-to-content workflow |

**Total source .md: 68** (+3 vs v1.1.0) | **Compiled: ~53** | **Root: 2** (README + agent_card)

### Artifacts with `quality: null` (never scored)

Down from 16 in v1.1.0 to **4 remaining**:

1. `architecture/agent_card_marketing.md`
2. `feedback/quality_gate_marketing.md`
3. `output/output_sdk_validation_self_audit.md`
4. `reports/self_audit_newpc.md` (this file)

**6% of source artifacts are unscored.** Significant improvement from 25% last session.

### Cross-Reference: Marketing-Related KCs in P01

| KC in P01 Library | Kind | N02 Relevant? |
|-------------------|------|---------------|
| `kc_action_prompt.md` | action_prompt | YES -- primary build kind |
| `kc_chain.md` | chain | YES -- prompt chains |
| `kc_content_monetization.md` | content_monetization | YES -- revenue copy |
| `kc_landing_page.md` | landing_page | YES -- core output |
| `kc_prompt_template.md` | prompt_template | YES -- primary build kind |
| `kc_scoring_rubric.md` | scoring_rubric | YES -- quality evaluation |
| `kc_social_publisher.md` | social_publisher | YES -- distribution |
| `kc_system_prompt.md` | system_prompt | YES -- agent prompts |
| `kc_tagline.md` | tagline | YES -- brand copy |

**9 relevant KCs available in P01.** Full coverage of primary kinds.

### 3 Identified Gaps

| # | Gap | Impact | Recommendation |
|---|-----|--------|---------------|
| 1 | **No video/reel script kind** | Short-form video (TikTok, Reels, Shorts) dominates social distribution. No artifact type for hooks, scripts, caption sequences, or B-roll callouts. | Request N03 build a `video_script` kind with ISOs for hook formats, pacing, and CTA placement. |
| 2 | **No SEO audit tooling** | Landing pages and content lack keyword density checks, meta tag validation, schema.org markup. Copy that seduces humans but starves search engines loses half its reach. | Extend `copy_analyzer.md` with SEO scoring extension or build standalone `seo_audit` tool. |
| 3 | **No competitor copy analysis workflow** | N01 delivers competitor research but no structured N01-to-N02 handoff exists for copy-specific intel: headline patterns, CTA strategies, tone fingerprinting. | Create `wf_competitor_copy_analysis.md` with formal N01 ingestion protocol. |

---

## Phase 4: Agent Card Audit

| Field | Agent Card Says | Reality | Match? | Fix? |
|-------|----------------|---------|--------|------|
| Model | opus-4-6 (1M context) | opus-4-6 (1M context) | YES | None |
| CLI | claude | claude | YES | None |
| Source artifacts | 65 | 68 | NO | Update count |
| Knowledge Cards | 14 | 17 | NO | Update count + list 3 new KCs |
| Prompts | 4 | 7 | NO | Update count + list 3 new templates |
| MCP: markitdown | FAIL (wrong pkg) | FIXED (markitdown-mcp-npx) | UPDATED | Reflected in agent card |
| MCP: browser | FAIL (wrong pkg) | PASS (correct pkg) | UPDATED | Reflected in agent card |
| MCP: canva | FAIL (env not set) | STILL BLOCKED | YES | No change |
| MCP: notebooklm | PASS | PASS | YES | None |
| Kinds buildable | 18 | 18 | YES | None |
| quality: null count | 16 | 4 | IMPROVED | Agent card updated |

**Agent card updated in this session.** Counts reconciled, MCP statuses corrected.

---

## Summary

| Phase | Score | Notes |
|-------|-------|-------|
| MCP Servers | 2/4 PASS | markitdown fixed this session; browser already fixed; canva blocked on env vars |
| Python Tools | 3/3 PASS | All operational |
| Artifact Inventory | 68 source / 53 compiled | 4 unscored (6%), 3 capability gaps identified |
| Agent Card | UPDATED | Counts reconciled, MCP statuses corrected |

### Priority Actions (Remaining)

1. **SET** `CANVA_CLIENT_ID` + `CANVA_CLIENT_SECRET` -- unlocks Canva MCP (design output)
2. **SCORE** 4 remaining unscored artifacts via `cex_score.py --apply`
3. **BUILD** video script capability -- highest distribution impact (gap #1)
4. **BUILD** SEO audit extension -- doubles reach of every landing page (gap #2)
5. **BUILD** competitor copy analysis workflow -- feeds N02 with N01 intel (gap #3)

---

> *Infrastructure is foreplay. Fix the plumbing first -- then turn up the heat.*
> *Every word that leaves this nucleus doesn't just inform. It seduces.*

## Boundary

Contexto de dominio para hidratar prompts. NAO eh knowledge_card (sem density gate) nem glossary_entry (nao define termo).

## 8F Pipeline Function

Primary function: **INJECT**
