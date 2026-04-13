---
id: self_audit_newpc_2026_04_12
kind: context_doc
title: "N06 Self-Audit -- New PC Setup (2026-04-12)"
nucleus: N06
pillar: P01
version: 1.0.0
quality: 8.9
created: 2026-04-12
mission: NEWPC_SETUP
---

# N06 Self-Audit -- New PC Setup (2026-04-12)

## Phase 1: MCP Server Verification

| # | Server | Binary | Status | Notes |
|---|--------|--------|--------|-------|
| 1 | **fetch** | `uvx mcp-server-fetch` | PASS | uvx works, dependencies downloaded successfully |
| 2 | **markitdown** | `npx markitdown-mcp` | PASS | npx resolves and runs |
| 3 | **stripe** | `npx @stripe/mcp` | BLOCKED | Package fixed to `@stripe/mcp`. Missing env: `STRIPE_SECRET_KEY` |
| 4 | **hotmart** | `npx mcp-server-hotmart` | BLOCKED | Missing env: `HOTMART_CLIENT_ID`, `HOTMART_CLIENT_SECRET`, `HOTMART_BASIC_AUTH` |
| 5 | **canva** | `npx @mcp_factory/canva-mcp-server` | BLOCKED | Missing env: `CANVA_CLIENT_ID`, `CANVA_CLIENT_SECRET` |
| 6 | **notebooklm** | `npx notebooklm-mcp@latest` | PASS | v1.0.0 loads successfully |

### API Keys Status

| Key | Set? | Required By |
|-----|------|-------------|
| `STRIPE_SECRET_KEY` | NO | stripe MCP |
| `HOTMART_CLIENT_ID` | NO | hotmart MCP |
| `HOTMART_CLIENT_SECRET` | NO | hotmart MCP |
| `HOTMART_BASIC_AUTH` | NO | hotmart MCP |
| `CANVA_CLIENT_ID` | NO | canva MCP |
| `CANVA_CLIENT_SECRET` | NO | canva MCP |

**Summary**: 3/6 PASS, 3/6 BLOCKED (missing API keys).

### Action Required

1. Set `STRIPE_SECRET_KEY` in environment
2. Set Hotmart credentials (`HOTMART_CLIENT_ID`, `HOTMART_CLIENT_SECRET`, `HOTMART_BASIC_AUTH`) in environment
3. Set Canva credentials (`CANVA_CLIENT_ID`, `CANVA_CLIENT_SECRET`) in environment

---

## Phase 2: Python Tools Audit

| Tool | Status | Output |
|------|--------|--------|
| `cex_compile.py` | PASS | Shows usage, no import errors |
| `cex_score.py` | PASS | Shows usage, no import errors |
| `cex_doctor.py` | PASS | Runs header, no import errors |

**All 3 core Python tools functional.** No dependency issues on fresh PC.

---

## Phase 3: Artifact Inventory

### Count by Subdirectory

| Subdir | .md files | .yaml (compiled) | Total | Domain Focus |
|--------|----------:|------------------:|------:|--------------|
| `agents/` | 3 | -- | 3 | Identity, axioms, mental model |
| `architecture/` | 5 | -- | 5 | Patterns (brand, pricing, funnel), integration |
| `compiled/` | -- | 33 | 33 | Auto-compiled mirrors |
| `feedback/` | 1 | -- | 1 | Quality gate |
| `knowledge/` | 12 | -- | 12 | Brand KCs, monetization, ICP, competitive |
| `memory/` | 3 | -- | 3 | Decisions, pricing, learning record |
| `orchestration/` | 4 | -- | 4 | Dispatch rules, workflows |
| `output/` | 26 | -- | 26 | Brand book, pricing, funnels, audits, strategies |
| `prompts/` | 6 | -- | 6 | Brand discovery, audit, config extraction |
| `quality/` | 1 | -- | 1 | Scoring rubric |
| `reports/` | 2+1 | -- | 3 | Self-audits (this file included) |
| `schemas/` | 5 | -- | 5 | Brand audit/book/config/voice/input |
| `tools/` | 3 | -- | 3 | Monetization, pricing experiment, funnel diagnostic |
| **TOTAL** | **71+1** | **33** | **105** | |

### Monetization-Specific Artifacts

| Category | Artifacts | Revenue Relevance |
|----------|-----------|-------------------|
| **Pricing** | `pattern_pricing_framework.md`, `pricing_experiment_tool.md`, `output_pricing_page.md`, `pricing_content_factory.md`, `api_access_pricing.md`, `content_factory_pricing.md` | Direct: defines how money is made |
| **Funnels** | `pattern_funnel_architecture.md`, `funnel_diagnostic_tool.md`, `funnel_cex_product.md`, `funnel_content_factory.md` | Direct: conversion pipeline |
| **Courses** | `kc_brand_monetization_models.md`, `content_monetization_tool.md`, `output_monetization_business_plan.md` | Direct: course/content revenue |
| **Brand** | 12 brand KCs + 5 brand tools + 4 schemas + 6 prompts | Indirect: brand premium = pricing power |
| **Competitive** | `kc_competitive_positioning.md`, `output_competitive_map.md`, `output_competitive_business.md` | Strategic: market positioning |

### Cross-Reference with P11 (Feedback/Monetization)

P11 schema defines these kinds:

| P11 Kind | N06 Has? | Notes |
|----------|----------|-------|
| `quality_gate` | YES | `feedback/quality_gate_commercial.md` |
| `bugloop` | NO | No automated commercial fix cycle |
| `lifecycle_rule` | NO | No artifact aging/archival rules for commercial content |
| `guardrail` | NO | No pricing guardrails (min margin, max discount) |
| `optimizer` | NO | No formal metric-to-action optimizer |
| `reward_signal` | NO | No continuous quality signal for commercial output |

**Gap**: N06 has 1/6 P11 kinds. The feedback layer is thin for commercial domain.

---

## Phase 4: Agent Card Accuracy Check

| Agent Card Claim | Verified | Actual |
|-----------------|----------|--------|
| 55 source + 19 compiled = 74 | OUTDATED | 72 source + 33 compiled = 105 |
| 12 domain KCs | CORRECT | 12 in `knowledge/` |
| 6 MCP servers | CORRECT | 6 configured (1 wrong package) |
| 3 memory artifacts | CORRECT | 3 in `memory/` |
| 4 brand schemas | OUTDATED | 5 schemas (added `input_schema_content_order.md`) |
| 15 output artifacts | OUTDATED | 26 output artifacts |
| 2 prior self-audit reports | CORRECT | 2 in `reports/` |

**Agent card needs update**: artifact counts have grown significantly since v1.0.0.

---

## 3 Commercial Gaps Identified

### Gap 1: No Pricing Guardrails (P11 guardrail)

**Cost of inaction**: Without min-margin and max-discount guardrails, pricing decisions can erode revenue. A 5% margin undercut across 100 deals = significant revenue leak.

**Recommendation**: Build `p11_gr_pricing_guardrails.yaml` -- floor margins, discount caps, bundle rules.

### Gap 2: No Commercial Bugloop (P11 bugloop)

**Cost of inaction**: When a funnel underperforms (conversion < threshold), there is no automated detect-fix-verify cycle. Manual diagnosis wastes N06 context.

**Recommendation**: Build `p11_bl_funnel_performance.md` -- detect conversion drops, suggest fixes, verify after change.

### Gap 3: Stripe API Key Not Set

**Cost of inaction**: `.mcp-n06.json` now correctly references `@stripe/mcp` (fixed). However, `STRIPE_SECRET_KEY` is still not set in environment. Payment integration remains non-functional until the key is configured.

**Recommendation**: Set `STRIPE_SECRET_KEY` in environment. Test with `npx -y @stripe/mcp` to verify connection.

---

## Summary

| Metric | Value |
|--------|-------|
| MCP Servers | 3/6 operational (3 blocked: missing API keys) |
| Python Tools | 3/3 operational |
| Total Artifacts | 105 (72 source + 33 compiled) |
| P11 Coverage | 1/6 kinds |
| Agent Card | Needs count update |
| Critical Fix | Set 6 API keys (Stripe, Hotmart, Canva) |
| Missing Keys | 6 API keys across 3 services |

## Boundary

Contexto de dominio para hidratar prompts. NAO eh knowledge_card (sem density gate) nem glossary_entry (nao define termo).


## 8F Pipeline Function

Primary function: **INJECT**
