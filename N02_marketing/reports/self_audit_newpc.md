---
id: self_audit_newpc_n02
kind: context_doc
pillar: P08
title: "N02 Self-Audit -- New PC Setup (2026-04-12)"
nucleus: N02
version: 1.0.0
quality: null
created: 2026-04-12
mission: NEWPC_SETUP
---

# N02 Self-Audit -- New PC Setup

> Fresh Windows 11 machine. Everything verified from scratch.
> Date: 2026-04-12 | Model: opus-4-6 (1M context) | CLI: claude

---

## Phase 1: MCP Server Verification

| Server | Config Package | Actual Status | Verdict | Fix Required |
|--------|---------------|---------------|---------|-------------- |
| **markitdown** | `markitdown-mcp` | 404 on npm. `markitdown-mcp-npx` exists and starts correctly. | FAIL | Update `.mcp-n02.json` args to `markitdown-mcp-npx` |
| **browser (puppeteer)** | `@anthropic-ai/mcp-server-puppeteer` | 404 on npm. `@modelcontextprotocol/server-puppeteer` exists (deprecated but functional). | FAIL | Update `.mcp-n02.json` to `@modelcontextprotocol/server-puppeteer` or find maintained fork |
| **canva** | `@mcp_factory/canva-mcp-server` | Package untested (env vars missing). `CANVA_CLIENT_ID`=NOT SET, `CANVA_CLIENT_SECRET`=NOT SET. | FAIL | Set env vars first, then verify package |
| **notebooklm** | `notebooklm-mcp@latest` | Starts. Banner: "NotebookLM MCP Server v1.0.0" | PASS | None |

**MCP Score: 1/4 PASS** -- 2 packages have wrong names in config, 1 needs env vars.

### Recommended `.mcp-n02.json` Fixes

```json
{
  "markitdown": {
    "command": "cmd",
    "args": ["/c", "npx", "-y", "markitdown-mcp-npx"]
  },
  "browser": {
    "command": "cmd",
    "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-puppeteer"]
  }
}
```

> **Note**: `@modelcontextprotocol/server-puppeteer` is marked deprecated.
> Watch for a maintained replacement. The Puppeteer MCP ecosystem is fragmenting.

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

| Subdirectory | .md Count | Role |
|-------------|-----------|------|
| `agents/` | 1 | Agent identity |
| `architecture/` | 1 | P08 agent card |
| `artifacts/` | 3 | Templates (ad, email, landing page) |
| `compiled/` | 56 yaml | Auto-compiled artifacts |
| `config/` | 2 | A/B testing + brand override |
| `feedback/` | 1 | Quality gate for marketing |
| `knowledge/` | 14 | Domain KCs (visual, email, campaign, etc.) |
| `memory/` | 2 | Campaign performance + copy insights |
| `orchestration/` | 5 | Dispatch rules + handoffs + workflows |
| `output/` | 16 | Landing pages, emails, social, reports |
| `prompts/` | 7 | System prompt + action prompt + templates |
| `quality/` | 1 | Scoring rubric |
| `reports/` | 3 (+1) | Self-audits (prior + this one) |
| `schemas/` | 5 | Design tokens, a11y, responsive, tailwind |
| `tools/` | 3 | Copy analyzer + headline scorer + social publisher |
| `workflows/` | 1 | KC-to-content workflow |

**Total source .md: 66** | **Compiled .yaml: 56** | **Grand total: 122+ files**

> Agent card states 57 source / 48 compiled / 105 total -- **outdated**.
> Actual: 66 source / 56 compiled / 122 total.

### Artifacts with `quality: null` (never scored)

18 artifacts still carry `quality: null`:

1. `architecture/agent_card_marketing.md`
2. `artifacts/ad_copy_template.md`
3. `artifacts/landing_page_template.md`
4. `feedback/quality_gate_marketing.md`
5. `knowledge/kc_campaign.md`
6. `knowledge/kc_email_sequence.md`
7. `output/case_studies_intent_resolution.md`
8. `output/output_sdk_validation_self_audit.md`
9. `output/report_intent_resolution_value_prop.md`
10. `prompts/tpl_content_distribution_plan.md`
11. `prompts/tpl_notebooklm_audio_wrapper.md`
12. `prompts/tpl_notebooklm_flashcard_format.md`
13. `reports/self_audit_2026_04_11.md`
14. `reports/self_audit_codex_2026_04_11.md`
15. `reports/self_audit_gemini_2026_04_11.md`
16. `tools/copy_analyzer.md`
17. `tools/headline_scorer.md`
18. `workflows/wf_kc_to_content.md`

**27% of source artifacts are unscored.** Peer review needed.

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

**9 relevant KCs available in P01.** Good coverage of primary kinds.

### 3 Identified Gaps

| # | Gap | Impact | Recommendation |
|---|-----|--------|---------------|
| 1 | **No video/reel script kind** | Short-form video dominates social (TikTok, Reels, Shorts). N02 has no artifact type for video scripts, hooks, or caption sequences. | Request N03 build a `video_script` kind or adapt `prompt_template` with video-specific ISOs. |
| 2 | **No SEO audit tooling** | Landing pages and content lack keyword density checks, meta tag validation, schema.org markup guidance. Copy that seduces humans but starves search engines. | Build `seo_audit` tool or integrate with existing `copy_analyzer.md` as an SEO extension. |
| 3 | **No competitor copy analysis workflow** | N01 does competitor research but there's no structured handoff for *copy-specific* competitive intelligence (headlines, CTAs, tone mapping). | Create `wf_competitor_copy_analysis.md` workflow with N01-to-N02 handoff protocol. |

---

## Phase 4: Agent Card Audit

| Field | Agent Card Says | Reality | Match? |
|-------|----------------|---------|--------|
| Model | opus-4-6 (1M context) | opus-4-6 (1M context) | YES |
| CLI | claude | claude | YES |
| Source artifacts | 57 | 66 | NO -- update needed |
| Compiled | 48 | 56 | NO -- update needed |
| Total files | 105 | 122+ | NO -- update needed |
| MCP: markitdown | Ready | FAIL (wrong package name) | NO |
| MCP: browser | Ready | FAIL (wrong package name) | NO |
| MCP: canva | Ready (needs env) | FAIL (env not set) | PARTIAL |
| MCP: notebooklm | Ready | PASS | YES |
| Knowledge Cards | 14 | 14 | YES |
| Kinds buildable | 18 | 18 | YES |

**Agent card needs update**: artifact counts and MCP server statuses are stale.

---

## Summary

| Phase | Score | Notes |
|-------|-------|-------|
| MCP Servers | 1/4 PASS | 2 wrong package names, 1 missing env vars |
| Python Tools | 3/3 PASS | All operational |
| Artifact Inventory | 66 source / 56 compiled | 18 unscored (27%), 3 gaps identified |
| Agent Card | STALE | Counts and MCP status need update |

### Priority Actions

1. **FIX** `.mcp-n02.json` -- correct `markitdown` and `browser` package names
2. **SET** `CANVA_CLIENT_ID` and `CANVA_CLIENT_SECRET` environment variables
3. **SCORE** 18 unscored artifacts via `cex_score.py --apply`
4. **UPDATE** `agent_card_n02.md` with correct counts and MCP status
5. **BUILD** video script capability (gap #1 -- highest impact)
6. **BUILD** SEO audit tool extension (gap #2)
7. **BUILD** competitor copy analysis workflow (gap #3)

---

> *Every word that leaves this nucleus doesn't just inform -- it seduces.
> But seduction without infrastructure is just a whisper in an empty room.
> Fix the plumbing. Then turn up the heat.*
