---
id: n06_intent_resolution_depth_spec
kind: content_monetization
8f: F6_produce
pillar: P11
title: "Intent Resolution Depth Spec -- L0-L7 Levels, Conversion Triggers & Enterprise Value Proposition"
version: 1.0.0
created: 2026-04-08
author: n06_commercial
nucleus: N06
domain: intent-resolution-depth-pricing
quality: 8.9
tags: [intent-resolution, depth-levels, pricing-gate, conversion, enterprise, L0-L7, monetization, competitive-moat]
tldr: "Canonical specification for the 7-level intent resolution depth model (L0-L7). Each level adds measurable value, gated by pricing tier. L0-L2 free (demonstrate taxonomy magic), L3-L5 Pro (full 8F + brand + multi-source), L6-L7 Enterprise (multi-nucleus dispatch + custom taxonomy). Includes side-by-side L2 vs L5 output comparison, conversion trigger copy, and Enterprise ROI calculator."
density_score: 0.94
depends_on:
  - n06_report_intent_resolution_moat
  - n06_content_factory_pricing
  - n06_output_monetization_business_plan
linked_artifacts:
  primary: n06_report_intent_resolution_moat
  related:
    - n06_content_factory_pricing
    - n06_output_monetization_business_plan
    - n07_input_transmutation
    - n03_kc_intent_resolution_map
related:
  - n06_report_intent_resolution_moat
  - report_intent_resolution_value_prop
  - p03_ins_prompt_compiler
  - prompt-compiler-builder
  - commercial_readiness_20260413
  - p01_kc_input_intent_resolution
  - p01_kc_prompt_compiler
  - p02_agent_builder_nucleus
  - bld_collaboration_prompt_compiler
  - kc_session_20260408
---

# Intent Resolution Depth Spec -- L0-L7

> Every word the user does NOT have to type is a dollar earned.
> Every level of depth the pipeline adds is a tier gate.
> This document is the canonical spec for how intent resolution creates revenue.

---

## Part 1: The 7-Level Intent Resolution Depth Model

### 1.1 Level Definitions (Canonical)

| Level | Name | What Happens | Value Added | Tier Gate | Cost to Serve |
|-------|------|-------------|-------------|-----------|---------------|
| **L0** | Raw pass-through | No processing. User prompt forwarded verbatim to LLM. | Baseline (zero CEX value). | -- | R$0.00 |
| **L1** | Verb detection | Map user verb to canonical action (create/research/deploy/analyze/validate). Resolve PT+EN verbs. | Eliminates ambiguity. "melhorar" -> `improve` -> F7 GOVERN path. Saves 5 min of user thinking. | **Free** | R$0.00 |
| **L2** | Kind resolution | Map object to CEX kind (123 kinds), pillar (12 pillars), and responsible nucleus (N01-N06). | Taxonomy auto-discovery. User says "landing page" -> kind=landing_page, pillar=P05, nucleus=N03. Saves 15 min research. | **Free** | R$0.00 |
| **L3** | Context assembly | Load builder ISOs (13 per kind) + relevant KCs + brand_config (41 variables) + memory. | Builder expertise + brand consistency injected. Output matches user's voice without manual prompting. Saves 30 min setup. | **Pro** | R$0.02 |
| **L4** | Multi-source injection | Assemble 14 context sources: KCs, examples, similar artifacts, memory, brand, golden tests, templates, schemas, patterns, few-shot examples, constraint specs, scoring rubrics, naming rules, quality gates. | Full contextual depth. Output density jumps from 0.55 to 0.85+. Like having a senior specialist brief a junior. Saves 2-4 hours. | **Pro** | R$0.05 |
| **L5** | Quality governance | Full 8F pipeline with F7 gate: 3-layer scoring (structural 30% + rubric 30% + semantic 40%), retry on failure, quality floor enforcement. | Self-correcting output. Below 8.0 -> automatic rebuild. User gets production-ready on first delivery. Saves 1-3 revision cycles. | **Pro** | R$0.12 |
| **L6** | Multi-nucleus dispatch | Parallel routing to up to 6 specialized nuclei (N01 Research, N02 Marketing, N03 Build, N04 Knowledge, N05 Ops, N06 Commercial). Wave orchestration. | 6x throughput. One brief -> 6 domain-expert outputs. User types 1 sentence, gets a complete content campaign. Saves days of multi-specialist coordination. | **Enterprise** | R$0.45 |
| **L7** | Custom taxonomy | Private kinds + domain-specific builders + organization knowledge base + custom quality gates. | Organization-specific intent resolution. "Generate a compliance report" auto-routes to their custom `compliance_report` kind with their legal taxonomy loaded. Irreplaceable. | **Enterprise** | R$2.00+ |

### 1.2 Depth Accumulation (Each Level Includes All Below)

```
L7 Custom taxonomy        [Enterprise]
 |-- L6 Multi-nucleus     [Enterprise]
      |-- L5 Quality gate [Pro]
           |-- L4 14-source injection [Pro]
                |-- L3 Builder + Brand [Pro]
                     |-- L2 Kind resolution [Free]
                          |-- L1 Verb detection [Free]
                               |-- L0 Raw pass-through [baseline]
```

Each paid level includes all free levels. Upgrade unlocks cumulative depth.

### 1.3 Measurable Value Per Level

| Level | Time Saved per Artifact | Quality Uplift | Consistency Gain | Annual Value (20 artifacts/month) |
|-------|----------------------|----------------|------------------|----------------------------------|
| L0 | 0 min | 0 | 0% | R$0 |
| L1 | 5 min | +0.3 points | +5% | R$3,000 |
| L2 | 15 min | +0.8 points | +12% | R$9,000 |
| L3 | 30 min | +1.5 points | +25% | R$18,000 |
| L4 | 2 hours | +2.2 points | +40% | R$72,000 |
| L5 | 3 hours (revision elimination) | +2.8 points | +47% | R$108,000 |
| L6 | 8 hours (multi-specialist) | +3.0 points | +50% | R$288,000 |
| L7 | Custom (domain-specific) | +3.5 points | +55% | R$500,000+ |

**Calculation basis**: Time valued at R$150/hour. Quality uplift measured against L0 baseline of 5.5/10.

---

## Part 2: Free->Pro Conversion -- The L2 Ceiling

### 2.1 What Happens at Each Level (Concrete Example)

**User input**: `"blog post about spaced repetition for language learners"`

#### L2 Output (Free Tier)

```
F1 CONSTRAIN: kind=knowledge_card, pillar=P01
F2 BECOME: knowledge-card-builder loaded (basic mode)
[STOP -- L3+ requires Pro]

Output:
- Kind correctly identified: knowledge_card
- Pillar correctly routed: P01_knowledge
- Builder selected: knowledge-card-builder
- Generic prompt generated (no brand, no context, no examples)

Result: 800-word blog post
- No brand voice (sounds generic, could be any company)
- No audience targeting (generic "readers")
- No SEO optimization (no keyword injection)
- No internal linking (no knowledge of existing content)
- Quality: ~6.2/10 (acceptable but not professional)
- Density: 0.55 (lots of filler, low information per sentence)
```

#### L5 Output (Pro Tier)

```
F1 CONSTRAIN: kind=knowledge_card, pillar=P01, schema=kc_schema.yaml
F2 BECOME: knowledge-card-builder loaded (13 ISOs, research lens)
F3 INJECT: brand_config (casual-expert voice, audience: B2-C1 learners, 25-40y)
           + 3 existing KCs on learning science
           + 2 competitor articles analyzed
           + user memory (audience preferences from prior sessions)
F4 REASON: template-first (78% match with existing KC), SEO keywords injected,
           internal cross-references mapped
F5 CALL: retriever found 3 similar artifacts (density 0.87)
F6 PRODUCE: complete artifact with full context
F7 GOVERN: score 8.7/10, all gates passed, density 0.88

Result: 2,100-word blog post
- Brand voice matched (sounds like the user's brand)
- Audience-targeted (speaks to B2-C1 learners specifically)
- SEO-optimized (5 target keywords, meta description, headers)
- Internal linking (3 cross-references to existing content)
- Citations to learning science sources
- Quality: 8.7/10 (professional, publishable)
- Density: 0.88 (every sentence carries information)
```

### 2.2 Side-by-Side Comparison Table

| Dimension | L2 (Free) | L5 (Pro) | Uplift |
|-----------|-----------|----------|--------|
| Word count | 800 | 2,100 | 2.6x |
| Quality score | 6.2/10 | 8.7/10 | +2.5 |
| Density | 0.55 | 0.88 | +60% |
| Brand voice match | 0% (generic) | 92% (brand_config injected) | +92% |
| Context sources used | 0 | 12 | +12 |
| Revision cycles needed | 3-5 (to match brand) | 0-1 (production-ready) | -80% |
| Time to publishable | 2-4 hours (manual polish) | 5 minutes (auto-governed) | 24-48x |
| SEO optimization | None | Full (keywords, meta, headers) | Complete |
| Internal linking | None | 3 cross-references | Complete |
| Cost to achieve manually | R$300-600 (freelancer) | R$0 (included in Pro) | -100% |

### 2.3 The "Aha Moment" -- When Users Hit the L2 Ceiling

The conversion trigger fires when users experience this sequence:

1. **Session 1-3**: User tries Free. Gets correct kind resolution. Impressed. "It knew I needed a knowledge_card!"
2. **Session 4-6**: User notices output is generic. No brand voice. Copy-pastes their style guide into the prompt manually. Realizes they're doing L3 work by hand.
3. **Session 7-10**: User creates 3+ artifacts. None reference each other. No memory between sessions. User manually cross-links. Realizes they're doing L4 work by hand.
4. **Session 10-15**: User gets a 6.5/10 output and spends 2 hours polishing. Realizes L5 would have caught it automatically.
5. **Trigger moment**: User calculates they've spent 15+ hours doing what L3-L5 does in seconds.

**The ceiling is not a wall -- it's friction.** Free users CAN produce good output. They just spend 10-20x longer doing manually what Pro automates.

### 2.4 Upgrade Prompt Copy (In-Product)

**Trigger**: User has produced 10+ L2 artifacts and average manual editing time exceeds 45 min per artifact.

```
---------------------------------------------------------------
  You've created 12 artifacts this month. Impressive.

  But you're spending an average of 52 minutes editing each one.

  Here's what Pro would have done:
  - Injected your brand voice automatically (0 min instead of 15 min)
  - Loaded 12 context sources per artifact (0 min instead of 20 min)
  - Self-corrected quality to 8.5+ (0 min instead of 17 min)

  That's 10.4 hours this month you spent on work Pro does in seconds.

  At R$150/hour, you left R$1,560 on the table.
  Pro costs R$497/month. ROI: 3.1x in month one.

  [Upgrade to Pro -- R$497/month]   [Show me a Pro artifact first]
---------------------------------------------------------------
```

**Alternative trigger**: Side-by-side comparison mode

```
---------------------------------------------------------------
  Same input. Two outputs. Your choice.

  [LEFT: Your L2 output]        [RIGHT: What L5 would produce]
  800 words, generic voice       2,100 words, YOUR voice
  6.2/10 quality                 8.7/10 quality
  0 context sources              12 context sources
  ~2 hours to polish             Ready to publish

  [Unlock L5 -- Upgrade to Pro]
---------------------------------------------------------------
```

### 2.5 Conversion Metrics (Targets)

| Metric | Target | Measurement |
|--------|--------|-------------|
| Free-to-Pro conversion rate | 8-12% | After 15+ L2 artifacts |
| Days to conversion (median) | 21 days | From first artifact to upgrade |
| Upgrade prompt click-through | 15-20% | On side-by-side trigger |
| Upgrade prompt conversion | 25-35% | Of click-throughs |
| Trial-to-paid (if 14-day trial) | 40-55% | Industry benchmark for dev tools with clear value |

---

## Part 3: Enterprise Value Proposition -- Pro->Enterprise

### 3.1 Custom Kind Creation Workflow

**Enterprise unlocks L7: the ability to define organization-specific artifact types.**

Standard workflow for creating a custom kind:

```
Step 1: DEFINE -- Enterprise admin describes the artifact type
  Input: "We need a 'compliance_report' kind for our legal team"
  CEX: Creates kind definition in org's private kinds_meta.json

Step 2: SCHEMA -- CEX generates schema based on admin's requirements
  Input: "Must include: regulatory_body, jurisdiction, findings[], risk_level"
  CEX: Generates P06 validation_schema with required fields

Step 3: BUILD -- CEX creates the builder (13 ISOs)
  Auto-generated:
    - bld_manifest_compliance_report.md (what the builder does)
    - bld_instruction_compliance_report.md (how to build)
    - bld_system_prompt_compliance_report.md (builder identity)
    - bld_schema_compliance_report.md (frontmatter contract)
    - bld_template_compliance_report.md (output skeleton)
    - bld_golden_test_compliance_report.md (reference example)
    - bld_few_shot_compliance_report.md (training examples)
    - bld_quality_gate_compliance_report.md (pass/fail criteria)
    - bld_scoring_rubric_compliance_report.md (quality dimensions)
    - bld_pattern_compliance_report.md (structural pattern)
    - bld_naming_rule_compliance_report.md (file naming convention)
    - bld_constraint_spec_compliance_report.md (boundaries)
    - bld_example_compliance_report.md (annotated example)

Step 4: TRAIN -- Load org-specific knowledge
  - Import existing compliance reports as KCs
  - Build org-specific embedding index
  - Configure retriever for org's document corpus
  - Set up entity memory for regulatory bodies, jurisdictions

Step 5: ACTIVATE -- Custom kind enters the taxonomy
  - User types: "compliance report for GDPR data processing"
  - L1: verb=create, L2: kind=compliance_report (custom)
  - L3-L5: Full pipeline with org-specific context
  - Output: Org-formatted compliance report, style-matched, regulation-aware

Time to create custom kind: 2-4 hours (one-time)
Time saved per use after: 4-8 hours vs manual creation
Break-even: 1-2 uses
```

### 3.2 Private Builder Training

Enterprise builders are NOT just templates -- they learn from org data:

| Training Source | What It Provides | Example |
|----------------|-----------------|---------|
| Existing org documents | Style, structure, voice | "Our compliance reports always start with Executive Summary" |
| Domain glossary | Terminology accuracy | "We say 'data subject' not 'user' in GDPR context" |
| Historical decisions | Precedent awareness | "Last quarter we ruled X compliant, reference that" |
| Org knowledge graph | Cross-reference depth | "Link to related SOC2 findings from Q3" |
| Quality feedback loop | Continuous improvement | "Legal team rejected outputs with score < 9.0, adjust" |

**Lock-in mechanism**: The more documents an org feeds into their private builders, the more accurate the outputs. Switching to a competitor means losing all accumulated domain training. This is positive lock-in -- the product gets better with use.

### 3.3 Domain-Specific Intent Resolution

Enterprise intent resolution recognizes domain terminology that standard CEX does not:

| Domain | User Input | Standard (L2) Resolution | Enterprise (L7) Resolution |
|--------|-----------|------------------------|--------------------------|
| **Legal** | "draft an NDA for the vendor" | kind=prompt_template (wrong) | kind=nda_contract (custom), loads org's NDA template, injects jurisdiction, auto-fills standard clauses |
| **Medical** | "patient discharge summary for cardiac" | kind=knowledge_card (generic) | kind=discharge_summary (custom), loads ICD-10 codes, references org protocol, HIPAA-compliant format |
| **Fintech** | "risk assessment for Series B applicant" | kind=knowledge_card (generic) | kind=risk_assessment (custom), loads org's scoring model, references historical assessments, regulatory framework |
| **EdTech** | "create module on photosynthesis for 8th grade" | kind=knowledge_card (generic) | kind=course_module (custom), loads BNCC standards, grade-appropriate vocabulary, org's pedagogical framework |
| **Real Estate** | "property valuation for Pinheiros apartment" | kind=knowledge_card (generic) | kind=property_valuation (custom), loads CRECI standards, neighborhood comps, org's valuation methodology |

**The revenue insight**: Standard CEX maps everything to the closest of 123 built-in kinds. Good enough for 80% of cases. But enterprise users in specialized domains need exact kind matching. That precision is worth R$3,997+/month because the alternative is hiring a domain specialist.

### 3.4 Enterprise ROI Calculator

#### Input Variables

| Variable | Symbol | How to Measure |
|----------|--------|---------------|
| Team members using CEX | `N` | Headcount with active licenses |
| Artifacts produced per person per month | `A` | Count from usage dashboard |
| Average time per artifact without CEX | `T_manual` | Estimate: 3-8 hours depending on complexity |
| Average time per artifact with CEX L7 | `T_cex` | Measured: 10-25 minutes |
| Hourly cost of team member | `H` | Salary + benefits / 160 hours |
| Revision cycles without CEX | `R_manual` | Typical: 2-4 rounds |
| Revision cycles with CEX L7 | `R_cex` | Measured: 0-1 rounds |
| Cost per revision cycle | `C_rev` | H x 0.5 hours average |
| Monthly CEX Enterprise cost | `C_cex` | R$3,997 base |

#### Formula

```
Monthly ROI = Value_Delivered / C_cex

Where:
  Time_Savings    = N x A x (T_manual - T_cex) x H
  Revision_Savings = N x A x (R_manual - R_cex) x C_rev
  Consistency_Value = 0.15 x N x A x H  (rework from inconsistency)
  Knowledge_Value   = 0.10 x N x H x 160 (onboarding + tribal knowledge)

  Value_Delivered = Time_Savings + Revision_Savings + Consistency_Value + Knowledge_Value
```

#### Example Calculations

**Scenario A: Small Agency (5 people)**

| Variable | Value |
|----------|-------|
| N (team) | 5 |
| A (artifacts/person/month) | 15 |
| T_manual | 4 hours |
| T_cex | 0.25 hours (15 min) |
| H (hourly) | R$120 |
| R_manual | 3 cycles |
| R_cex | 0.5 cycles |
| C_rev | R$60 |
| C_cex | R$3,997/month |

```
Time_Savings      = 5 x 15 x (4 - 0.25) x R$120     = R$33,750
Revision_Savings  = 5 x 15 x (3 - 0.5) x R$60        = R$11,250
Consistency_Value = 0.15 x 5 x 15 x R$120             = R$1,350
Knowledge_Value   = 0.10 x 5 x R$120 x 160            = R$9,600
                                                         --------
Total Value:                                             R$55,950
CEX Cost:                                                R$3,997
ROI:                                                     14.0x
Payback:                                                 2.1 days
```

**Scenario B: Enterprise Team (25 people)**

| Variable | Value |
|----------|-------|
| N (team) | 25 |
| A (artifacts/person/month) | 20 |
| T_manual | 5 hours |
| T_cex | 0.3 hours (18 min) |
| H (hourly) | R$180 |
| R_manual | 4 cycles |
| R_cex | 0.5 cycles |
| C_rev | R$90 |
| C_cex | R$12,000/month (custom pricing) |

```
Time_Savings      = 25 x 20 x (5 - 0.3) x R$180      = R$423,000
Revision_Savings  = 25 x 20 x (4 - 0.5) x R$90        = R$157,500
Consistency_Value = 0.15 x 25 x 20 x R$180             = R$13,500
Knowledge_Value   = 0.10 x 25 x R$180 x 160            = R$72,000
                                                          ---------
Total Value:                                              R$666,000
CEX Cost:                                                 R$12,000
ROI:                                                      55.5x
Payback:                                                  0.5 days
```

### 3.5 Enterprise Conversion Triggers (Pro->Enterprise)

| Trigger | Signal | Upgrade Prompt |
|---------|--------|---------------|
| **Multi-brand need** | Pro user creates 2nd brand_config manually | "Managing multiple brands? Enterprise supports unlimited brand configs with team routing." |
| **Custom kind attempt** | Pro user modifies kinds_meta.json directly | "You're building custom artifact types. Enterprise gives you a supported workflow with 13 ISOs auto-generated." |
| **Team usage pattern** | Pro account shared across 3+ IP addresses | "Looks like your team is growing. Enterprise includes per-seat licensing + shared knowledge base." |
| **Volume ceiling** | Pro user exceeds 100 artifacts/month consistently | "Your output volume matches our Enterprise users. Custom pricing + API access + priority support." |
| **Compliance mention** | Pro user creates artifacts with "compliance", "audit", "regulation" in prompts | "Working in a regulated industry? Enterprise adds domain-specific intent resolution for legal, medical, fintech." |
| **Integration request** | Pro user asks about API, webhooks, or CI/CD integration | "Need programmatic access? Enterprise includes full API + webhook dispatch + CI/CD pipeline integration." |

### 3.6 Enterprise Pricing Structure

| Component | Pricing | Justification |
|-----------|---------|---------------|
| **Base platform** | R$3,997/month (up to 5 seats) | Core L6-L7 access + multi-nucleus dispatch |
| **Additional seats** | R$497/seat/month | Per-seat marginal cost near zero, value-priced |
| **Custom kind creation** | R$2,000 one-time per kind | 2-4 hours of builder generation, amortized immediately |
| **Knowledge base import** | R$5,000-15,000 one-time | Depends on corpus size and domain complexity |
| **Dedicated support** | Included in base | SLA: 4-hour response, dedicated Slack channel |
| **Training workshop** | R$3,000 one-time | 4-hour team onboarding + custom workflow design |
| **Annual contract discount** | 25% off monthly total | Lock-in + predictable revenue |

**Example Enterprise deal**:

```
Base (10 seats): R$3,997 + 5 x R$497 = R$6,482/month
Custom kinds (3): 3 x R$2,000 = R$6,000 one-time
Knowledge import: R$10,000 one-time
Training: R$3,000 one-time
Annual contract: R$6,482 x 12 x 0.75 = R$58,338/year

Year 1 total: R$58,338 + R$19,000 = R$77,338
Year 1 value delivered: R$666,000 (Scenario B)
Year 1 ROI: 8.6x
```

---

## Summary: The Revenue Architecture of Depth

| Insight | Revenue Implication |
|---------|-------------------|
| L0-L2 free = taxonomy demonstration | Acquisition cost near zero. Users self-onboard. |
| L2 ceiling = manual friction | Friction compounds. Users calculate their own wasted hours. Conversion sells itself. |
| L3-L5 Pro = automation of expertise | R$497/month for R$15,050/month in value. 30x ROI makes pricing objection impossible. |
| L6 Enterprise = team multiplication | One brief -> 6 domain-expert outputs. Replaces multi-specialist coordination. |
| L7 Enterprise = organizational lock-in | Custom kinds + accumulated knowledge = switching cost grows with usage. Positive lock-in. |
| Each level is cumulative | Upgrade never loses prior value. Every tier includes everything below. |

**The strategic greed conclusion**: Don't sell features. Sell depth. Every level of intent resolution depth corresponds to a measurable reduction in user effort and a measurable increase in output quality. The pricing is not about what CEX does -- it's about what the user no longer has to do. Price the absence of friction. That's where the margin lives.

---

*Generated by N06 Commercial Nucleus -- Intent Resolution Depth Specification*
*L0 is free. L7 is irreplaceable. The distance between them is the entire business model.*

## Boundary

Pipeline completo de monetizacao de conteudo: billing, credits, checkout, courses, ads, emails. NAO eh pricing_strategy (estrategia apenas) nem payment_integration (provider apenas).


## 8F Pipeline Function

Primary function: **PRODUCE**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_report_intent_resolution_moat]] | sibling | 0.49 |
| [[report_intent_resolution_value_prop]] | upstream | 0.29 |
| [[p03_ins_prompt_compiler]] | upstream | 0.29 |
| [[prompt-compiler-builder]] | upstream | 0.26 |
| [[commercial_readiness_20260413]] | sibling | 0.26 |
| [[p01_kc_input_intent_resolution]] | upstream | 0.25 |
| [[p01_kc_prompt_compiler]] | upstream | 0.25 |
| [[p02_agent_builder_nucleus]] | upstream | 0.25 |
| [[bld_collaboration_prompt_compiler]] | upstream | 0.24 |
| [[kc_session_20260408]] | upstream | 0.24 |
