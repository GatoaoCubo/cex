---
id: self_audit_newpc_2026_04_13
kind: context_doc
title: "N06 Self-Audit -- New PC Setup (2026-04-13)"
nucleus: N06
pillar: P01
version: 1.1.0
quality: 8.9
created: 2026-04-12
updated: 2026-04-13
mission: NEWPC_SETUP
---

# N06 Self-Audit -- New PC Setup (2026-04-13)

## Phase 1: MCP Server Verification

| # | Server | Binary | Status | Notes |
|---|--------|--------|--------|-------|
| 1 | **fetch** | `uvx mcp-server-fetch` | PASS | uvx works, --help responds correctly |
| 2 | **markitdown** | `npx markitdown-mcp` | PASS | node v24.14.1, npx 11.11.0 operational |
| 3 | **stripe** | `npx @stripe/mcp` | BLOCKED | Package correct (@stripe/mcp). Missing env: `STRIPE_SECRET_KEY` |
| 4 | **hotmart** | `npx mcp-server-hotmart` | BLOCKED | Missing env: `HOTMART_CLIENT_ID`, `HOTMART_CLIENT_SECRET`, `HOTMART_BASIC_AUTH` |
| 5 | **canva** | `npx @mcp_factory/canva-mcp-server` | BLOCKED | Missing env: `CANVA_CLIENT_ID`, `CANVA_CLIENT_SECRET` |
| 6 | **notebooklm** | `npx notebooklm-mcp@latest` | PASS | node runtime confirmed, npx resolves |

### API Keys Status

| Key | Set? | Required By | Revenue Impact |
|-----|------|-------------|----------------|
| `STRIPE_SECRET_KEY` | NO | stripe MCP | **HIGH** -- blocks payment integration, subscription data |
| `HOTMART_CLIENT_ID` | NO | hotmart MCP | **HIGH** -- blocks course sales + affiliate tracking |
| `HOTMART_CLIENT_SECRET` | NO | hotmart MCP | HIGH |
| `HOTMART_BASIC_AUTH` | NO | hotmart MCP | HIGH |
| `CANVA_CLIENT_ID` | NO | canva MCP | MEDIUM -- blocks brand asset automation |
| `CANVA_CLIENT_SECRET` | NO | canva MCP | MEDIUM |

**Summary**: 3/6 PASS, 3/6 BLOCKED (missing API keys only -- no binary failures).

### Runtime Versions

| Binary | Version | Status |
|--------|---------|--------|
| node | v24.14.1 | OK |
| npx | 11.11.0 | OK |
| uvx | (latest) | OK |

### Action Required

1. Set `STRIPE_SECRET_KEY` in environment (highest priority -- enables payment data)
2. Set Hotmart credentials (enables course sales tracking)
3. Set Canva credentials (enables brand asset automation)

---

## Phase 2: Python Tools Audit

| Tool | Status | Notes |
|------|--------|-------|
| `cex_compile.py` | PASS | Parses args, no import errors. Supports `--all`, `--target`, `--lp` |
| `cex_score.py` | PASS | CEX Hybrid Scorer loads. Supports `--apply`, `--hybrid`, `--verbose` |
| `cex_doctor.py` | PASS | v2.0 initializes. Naming v2.0 + Density + 13-File Completeness mode ready |

**All 3 core Python tools functional.** No dependency issues on fresh PC.

---

## Phase 3: Artifact Inventory

### Count by Subdirectory (2026-04-13)

| Subdir | .md files | .yaml (compiled) | Total | Domain Focus |
|--------|----------:|------------------:|------:|--------------|
| `agents/` | 3 | -- | 3 | Identity, axioms, mental model |
| `architecture/` | 5 | -- | 5 | Patterns (brand, pricing, funnel), integration |
| `compiled/` | -- | 33 | 33 | Auto-compiled YAML mirrors |
| `feedback/` | 1 | -- | 1 | Quality gate |
| `knowledge/` | 14 | -- | 14 | Brand KCs + AI compliance + SaaS monetization |
| `memory/` | 3 | -- | 3 | Decisions, pricing experiments, learning record |
| `orchestration/` | 4 | -- | 4 | Dispatch rules, workflows |
| `output/` | 26 | -- | 26 | Brand books, pricing, funnels, audits, strategies |
| `prompts/` | 6 | -- | 6 | Brand discovery, audit, config extraction |
| `quality/` | 1 | -- | 1 | Scoring rubric |
| `reports/` | 1 | -- | 1 | This file |
| `schemas/` | 5 | -- | 5 | Brand audit/book/config/voice/input |
| `tools/` | 3 | -- | 3 | Monetization, pricing experiment, funnel diagnostic |
| root | 2 | -- | 2 | README.md + agent_card_n06.md |
| **TOTAL** | **74** | **33** | **107** | |

**Growth since 2026-04-12**: +2 KCs in knowledge/ (`kc_ai_compliance_gdpr.md`, `kc_ai_saas_monetization.md`).

### Monetization-Specific Artifacts

| Category | Count | Key Artifacts | Revenue Relevance |
|----------|------:|---------------|-------------------|
| **Pricing** | 6 | pricing_framework, pricing_experiment_tool, output_pricing_page, pricing_content_factory, api_access_pricing, content_factory_pricing | Direct: defines margin structure |
| **Funnels** | 4 | funnel_architecture, funnel_diagnostic_tool, funnel_cex_product, funnel_content_factory | Direct: conversion pipeline |
| **Courses/Content** | 3 | kc_brand_monetization_models, content_monetization_tool, output_monetization_business_plan | Direct: course/content revenue |
| **Brand** | 27 | 12 KCs + 5 tools + 5 schemas + 6 prompts | Indirect: brand premium = pricing power |
| **AI Monetization** | 1 | kc_ai_saas_monetization (NEW) | Direct: SaaS model patterns |
| **Compliance** | 1 | kc_ai_compliance_gdpr (NEW) | Risk: prevents revenue-killing compliance failures |
| **Competitive** | 3 | kc_competitive_positioning + 2 output maps | Strategic: market positioning |

### Cross-Reference with P11 (Feedback/Monetization)

| P11 Kind | N06 Has? | Notes |
|----------|----------|-------|
| `quality_gate` | YES | `feedback/quality_gate_commercial.md` |
| `bugloop` | NO | No automated commercial fix cycle |
| `lifecycle_rule` | NO | No artifact aging/archival rules for commercial content |
| `guardrail` | NO | No pricing guardrails (min margin, max discount) |
| `optimizer` | NO | No formal metric-to-action optimizer |
| `reward_signal` | NO | No continuous quality signal for commercial output |

**P11 Coverage**: 1/6 kinds. The feedback layer remains thin for commercial domain.

---

## Phase 4: Agent Card Accuracy Check

| Agent Card Claim (v1.1.0) | Verified | Actual |
|--------------------------|----------|--------|
| 72 source + 33 compiled = 105 | OUTDATED | 74 source + 33 compiled = 107 |
| 12 domain KCs | OUTDATED | 14 KCs (2 new: AI compliance, SaaS monetization) |
| 6 MCP servers | CORRECT | 6 configured |
| 3 memory artifacts | CORRECT | 3 in memory/ |
| 5 brand schemas | CORRECT | 5 schemas |
| 26 output artifacts | CORRECT | 26 |
| 6 prompts | CORRECT | 6 |

**Agent card needs count update**: knowledge/ is now 14, total is 107.

---

## 3 Commercial Gaps Identified

### Gap 1: No Pricing Guardrails (P11 guardrail)

**ROI of inaction**: Without min-margin and max-discount guardrails, pricing decisions can erode revenue. A 5% margin undercut across 100 deals = significant revenue leak. No guard = no floor.

**Recommendation**: Build `N06_commercial/feedback/p11_gr_pricing_guardrails.md` -- floor margins, discount caps, bundle rules.

**Estimated build cost**: 1 artifact, N06 solo, 8F pipeline.

### Gap 2: No Commercial Bugloop (P11 bugloop)

**ROI of inaction**: When a funnel underperforms (conversion < threshold), there is no automated detect-fix-verify cycle. Every manual diagnosis = N06 context burn + human time.

**Recommendation**: Build `N06_commercial/feedback/p11_bl_funnel_performance.md` -- detect conversion drops, suggest fixes, verify after change.

### Gap 3: 3 Payment/Design MCPs Non-Functional (API Keys Missing)

**ROI of inaction**: Stripe MCP = no payment data = pricing decisions without revenue feedback. Hotmart MCP = no course sales data = content monetization flying blind. Canva MCP = no automated brand assets = manual design bottleneck.

**Recommendation**:
1. Set `STRIPE_SECRET_KEY` in environment (immediate)
2. Set Hotmart credentials (immediate)
3. Set Canva credentials (medium priority)

---

## Summary

| Metric | Value | Delta |
|--------|-------|-------|
| MCP Servers | 3/6 operational | -- (same as 2026-04-12) |
| Python Tools | 3/3 operational | -- |
| Total Source Artifacts | 74 .md | +2 from 2026-04-12 |
| Total Compiled | 33 .yaml | -- |
| Grand Total | 107 | +2 |
| P11 Coverage | 1/6 kinds | -- |
| API Keys Missing | 6 (3 services) | -- |
| Agent Card Accuracy | NEEDS UPDATE | knowledge/: 12->14, total: 105->107 |

## Boundary

Contexto de dominio para hidratar prompts. NAO eh knowledge_card (sem density gate) nem glossary_entry (nao define termo).

## 8F Pipeline Function

Primary function: **INJECT**
