---
id: p12_wf_commercial_nucleus
kind: workflow
pillar: P12
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: n06_commercial
title: Commercial Nucleus Workflows
steps_count: 12
execution_mode: sequential
error_recovery: retry
max_retries: 2
timeout_ms: 1800000
spawn_delay_ms: 3000
quality: 8.9
tags: [workflow, commercial, N06, course-launch, pricing-strategy, funnel-build]
tldr: Three core N06 workflows — Course Launch, Pricing Strategy, and Funnel Build — each with defined steps, signals, and outputs.
density_score: 0.90
---

# Commercial Nucleus Workflows

Three core workflows for N06 monetization operations. Each is self-contained and signals on completion.

---

## Workflow 1: Course Launch

**Goal**: Take a topic + audience → validated course with pricing, outline, and funnel ready for Hotmart/Kiwify.

### Steps

#### Step 1: define_transformation_arc [N06]
- **Action**: Define student before/after state. Name the specific pain, desire, and measurable outcome.
- **Input**: topic, target audience, expert's unique mechanism
- **Output**: transformation_arc.md (before → milestones → after)
- **Signal**: `arc_defined`

#### Step 2: build_course_outline [N06]
- **Action**: Structure 4-8 modules with 3-5 lessons each. Each module = one milestone in the arc.
- **Input**: transformation_arc.md
- **Output**: course_outline.md (modules + lesson titles + durations)
- **Signal**: `outline_complete`
- **Depends on**: Step 1

#### Step 3: design_pricing_tiers [N06]
- **Action**: Apply tiered pricing framework. Basic/Pro/VIP. Anchor to transformation value.
- **Input**: course_outline.md + audience research
- **Output**: pricing_tiers.md (3 tiers, prices, inclusions, rationale, revenue model)
- **Signal**: `pricing_defined`
- **Depends on**: Step 2

#### Step 4: write_sales_page [N06]
- **Action**: Write VSL script + sales page copy (headline, pain agitation, mechanism, proof, offer, CTA).
- **Input**: transformation_arc.md + pricing_tiers.md
- **Output**: sales_page_copy.md
- **Signal**: `copy_complete`
- **Depends on**: Steps 1, 3

#### Step 5: design_upsell_sequence [N06]
- **Action**: Define order bump + OTO1 + OTO2 + downsell. Price, take rate estimates, LTV projection.
- **Input**: pricing_tiers.md + sales_page_copy.md
- **Output**: upsell_sequence.md
- **Signal**: `upsells_defined`
- **Depends on**: Steps 3, 4

---

## Workflow 2: Pricing Strategy

**Goal**: Given a product and audience → validated price with tiers, rationale, and revenue model.

### Steps

#### Step 1: assess_transformation_value [N06]
- **Action**: Interview-style prompts to quantify outcome value: income gain, time saved, pain eliminated.
- **Input**: product description, target audience, desired outcome
- **Output**: value_assessment.md (outcome value, certainty factor, speed factor → price range)
- **Signal**: `value_assessed`

#### Step 2: benchmark_market_pricing [N01 or manual]
- **Action**: Identify 3-5 competitor prices for similar transformation. Document positioning intent.
- **Input**: product category, audience segment
- **Output**: market_benchmarks.md
- **Signal**: `benchmarks_ready`

#### Step 3: design_tier_table [N06]
- **Action**: Build 3-tier pricing table with inclusions, price ratios, and psychological anchors.
- **Input**: value_assessment.md + market_benchmarks.md
- **Output**: tier_table.md (Basic/Pro/VIP with prices and inclusions)
- **Signal**: `tiers_designed`
- **Depends on**: Steps 1, 2

#### Step 4: model_revenue [N06]
- **Action**: Project revenue scenarios (conservative/realistic/optimistic) at each tier with conversion assumptions.
- **Input**: tier_table.md + estimated traffic/audience size
- **Output**: revenue_model.md (3 scenarios × 3 tiers with AOV, LTV, MRR projections)
- **Signal**: `revenue_modeled`
- **Depends on**: Step 3

---

## Workflow 3: Funnel Build

**Goal**: Given an offer → complete TOFU→BOFU funnel with copy for each stage.

### Steps

#### Step 1: map_funnel_stages [N06]
- **Action**: Define TOFU/MOFU/BOFU stages. Assign artifact per stage (ad, lead magnet, webinar, sales page, email sequence).
- **Input**: offer details, audience, traffic source
- **Output**: funnel_map.md (stages → artifact types → conversion benchmarks)
- **Signal**: `funnel_mapped`

#### Step 2: write_tofu_hooks [N06]
- **Action**: Write 5 ad hooks / organic post headlines targeting the pain point. CTA to lead magnet.
- **Input**: funnel_map.md + audience pain
- **Output**: tofu_hooks.md
- **Signal**: `tofu_ready`
- **Depends on**: Step 1

#### Step 3: build_mofu_sequence [N06]
- **Action**: Write lead magnet outline + 3-email nurture sequence moving prospect to BOFU.
- **Input**: funnel_map.md + tofu_hooks.md
- **Output**: mofu_sequence.md
- **Signal**: `mofu_ready`
- **Depends on**: Steps 1, 2

#### Step 4: write_bofu_close [N06]
- **Action**: Write sales page or VSL close sequence — proof, offer stack, urgency, guarantee, CTA.
- **Input**: mofu_sequence.md + pricing tier table
- **Output**: bofu_close.md
- **Signal**: `bofu_ready`
- **Depends on**: Steps 2, 3

## Workflow Signals

| Signal | Written to | Meaning |
|--------|-----------|---------|
| `arc_defined` | `.cex/runtime/signals/n06_arc.json` | Transformation arc ready |
| `outline_complete` | `.cex/runtime/signals/n06_outline.json` | Course structure done |
| `pricing_defined` | `.cex/runtime/signals/n06_pricing.json` | Pricing tiers ready |
| `copy_complete` | `.cex/runtime/signals/n06_copy.json` | Sales copy ready |
| `upsells_defined` | `.cex/runtime/signals/n06_upsells.json` | Upsell sequence ready |
| `funnel_mapped` | `.cex/runtime/signals/n06_funnel.json` | Full funnel map ready |
