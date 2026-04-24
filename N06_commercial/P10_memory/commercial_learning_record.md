---
id: commercial_learning_record
kind: learning_record
8f: F7_govern
pillar: P10
title: "Commercial Learning Record — N06"
nucleus: N06
version: 1.0.0
created: 2026-04-07
author: n06_commercial
domain: commercial_operations
quality: 9.0
tags: [learning-record, commercial, N06, brand, monetization, lessons]
tldr: "Lessons learned from N06 commercial operations — brand building, pricing, tool usage, pipeline discoveries."
scope: commercial_learning
density_score: 1.0
related:
  - agent_card_n06
  - p02_mm_commercial_nucleus
  - p08_pat_brand_pipeline
  - p02_agent_commercial_nucleus
  - p08_ac_brand_nucleus
  - p03_sp_brand_nucleus
  - n06_self_audit_20260408
  - p01_kc_cex_as_digital_asset
  - spec_n06_brand_verticalization
  - p02_agent_brand_nucleus
---

# Commercial Learning Record

## L01: Brand Config is the Single Source of Truth

`.cex/brand/brand_config.yaml` must be populated BEFORE any brand artifact is generated. Every other nucleus reads this file. If it's wrong, everything downstream is wrong.

**Cost of ignoring**: 7 nuclei propagate bad brand signals → expensive rework.
**Fix**: `brand_validate.py` runs pre-commit. Never skip.

## L02: GDP Saves More Than It Costs

Asking the user 5 questions upfront costs 2 minutes. Building the wrong thing costs 2 hours. The ROI of GDP is 60:1 on subjective decisions.

**When to GDP**: tone, audience, pricing model, naming, visual direction.
**When NOT to GDP**: file structure, compilation, indexing — these are HOW decisions.

## L03: Brand Propagation Must Be Atomic

`brand_propagate.py` updates all 7 nuclei. If it fails mid-way, some nuclei have new brand, some have old. This causes brand inconsistency.

**Fix**: Run propagation as atomic operation. Verify all 7 nuclei updated. If any fail, rollback all.

## L04: Pricing Pages Need Real Numbers

Generated pricing pages with placeholder "$X/mo" are worthless. Users see them and lose trust. Either have real pricing or don't ship a pricing page.

**Rule**: No pricing artifact ships with placeholder values. Use GDP to get real numbers first.

## L05: The Bootstrap Must Be Conversational

The original `cex_bootstrap.py` tried to ask all 13+ brand questions in a single form. Users abandoned mid-way.

**Fix**: Interactive conversation mode. 5-6 core questions first. Advanced questions optional. Save progress so users can resume.

## L06: Stripe MCP Needs Active Keys

The Stripe MCP server is available but requires `STRIPE_SECRET_KEY` in environment. Without it, all payment operations fail silently.

**Checklist before using Stripe MCP**:
1. Confirm `STRIPE_SECRET_KEY` is set
2. Confirm test vs live mode
3. Log every API call to prevent double-charges

## L07: Compiled YAMLs Are Not Optional

Every `.md` artifact in N06 must have a corresponding `.yaml` in `compiled/`. Other tools (retriever, query, router) read compiled YAMLs, not markdown. An artifact without a compiled version is invisible to the system.

**After every artifact creation**: Run `python _tools/cex_compile.py <file>` or `--all`.

## L08: Content Monetization ≠ Course Sales

Early assumption: "monetization = selling courses." Wrong. Content monetization includes:
- Courses (Hotmart)
- Subscriptions (Stripe)
- Sponsorships
- Affiliate revenue
- Premium content gates
- Community access fees

**Fix**: `content_monetization_tool.md` now covers all 6 revenue streams, not just courses.

## L09: Agent Card Self-Awareness Pays Off

Building the agent card (`agent_card_n06.md`) took 30 minutes. It prevented 3 task misroutes in the first grid dispatch (N07 was routing brand tasks to N02 instead of N06).

**ROI**: 30 min invested → 3× prevented rework at ~45 min each = 135 min saved = 4.5:1 ROI.

## L10: Memory Is the Cheapest Infrastructure

An empty `memory/` directory costs nothing to fix but causes repeated GDP questions, lost context, and duplicated analysis. Memory artifacts have the highest ROI per byte in the entire system.

**Rule**: After every significant session, append to the relevant memory file. 5 minutes now saves 30 minutes next session.

---

## Metrics

| Metric | Value |
|--------|-------|
| Lessons logged | 10 |
| Last updated | 2026-04-07 |
| Sessions contributing | 3 |
| Estimated rework prevented | ~6 hours |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n06]] | upstream | 0.43 |
| [[p02_mm_commercial_nucleus]] | upstream | 0.36 |
| [[p08_pat_brand_pipeline]] | upstream | 0.34 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.34 |
| [[p08_ac_brand_nucleus]] | upstream | 0.33 |
| [[p03_sp_brand_nucleus]] | upstream | 0.32 |
| [[n06_self_audit_20260408]] | upstream | 0.32 |
| [[p01_kc_cex_as_digital_asset]] | upstream | 0.31 |
| [[spec_n06_brand_verticalization]] | upstream | 0.31 |
| [[p02_agent_brand_nucleus]] | upstream | 0.31 |
