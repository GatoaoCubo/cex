---
id: skill_n06
kind: skill
8f: F5_call
nucleus: n06
pillar: P04
title: "Skill N06: Sales Skills (Discovery / Objection-Handling / Closing)"
mirrors: N00_genesis/P04_tools/kind_skill/
overrides:
  tone: ROI-focused, conversion-driven
  voice: consultative, numbers-first
  sin_lens: AVAREZA ESTRATEGICA
  required_fields:
    - revenue_impact
    - conversion_target
    - cost_model
  quality_threshold: 9.0
  density_target: 0.85
  example_corpus: 3+ examples with revenue impact projections
version: 1.0.0
quality: 8.7
tags: [mirror, n06, commercial, skill, discovery, objection_handling, closing, hermes_assimilation]
tldr: "N06 skill set: structured discovery, ROI-anchored objection-handling, and conversion-optimized closing sequences"
created: "2026-04-18"
updated: "2026-04-18"
author: n06_commercial
related:
  - kc_discovery_questions
  - bld_knowledge_card_discovery_questions
  - bld_instruction_sales_playbook
  - bld_knowledge_card_sales_playbook
  - kc_sales_playbook
  - discovery-questions-builder
  - bld_output_template_discovery_questions
  - sales-playbook-builder
  - bld_examples_discovery_questions
  - bld_examples_sales_playbook
---

## Skill Registry

| Skill | Pillar Domain | Conversion Impact | Primary Metric |
|-------|---------------|-------------------|---------------|
| discovery | pre-sale diagnosis | +18% SQL-to-demo rate | discovery score 0-10 |
| objection_handling | mid-funnel defense | -31% lost deals | objection-close rate |
| closing | deal finalization | +24% win rate | close velocity (days) |

---

## Skill 1: Discovery

**Purpose**: Diagnose buyer pain, quantify urgency, map stakeholders — before any solution is proposed.

**Trigger**: Any inbound lead with company ARR > $5K or SQLs from marketing qualified pipeline.

**Revenue Impact**: Deals with structured discovery close at 2.1x the rate of unstructured pitches (Gong 2024 cohort data).

### Discovery Framework (MEDDPICC)
| Element | Question Prompt | Revenue Signal |
|---------|----------------|---------------|
| Metrics | "What does success look like in numbers?" | Quantified pain = higher ACV |
| Economic Buyer | "Who controls this budget?" | Identifies true deal velocity |
| Decision Criteria | "What does your ideal solution need to do?" | Feature-to-value mapping |
| Decision Process | "How does your team evaluate vendors?" | Multi-thread vs. single-thread risk |
| Paper Process | "What does the contract approval path look like?" | Legal/procurement lag forecast |
| Identify Pain | "What's the cost of NOT solving this?" | Urgency calibration |
| Champion | "Who internally wants this solved most?" | Internal champion = 38% faster close |
| Competition | "Are you evaluating alternatives?" | Win/loss positioning |

### Activation
```yaml
trigger: new_sql OR demo_requested
steps:
  - run_discovery_questionnaire: true
  - score_meddpicc: true
  - qualify_threshold: 6/8   # minimum to advance to demo
  - log_discovery_score: true
output: discovery_score, pain_quantification, stakeholder_map
```

### Conversion Target
- Discovery score >= 6/8 before advancing to demo stage
- Pain quantification in USD or % present in 80%+ of advanced deals
- cost_model confirmed before pricing discussion

---

## Skill 2: Objection Handling

**Purpose**: Neutralize blockers with data, not persuasion. Convert objections into deal accelerators.

**Trigger**: Any deal stage 2+ where buyer raises price, timing, or competitive concerns.

**Revenue Impact**: Structured objection-handling reduces lost deals by 31% vs. ad-hoc responses.

### Objection Response Library
| Objection | Root Cause | Response Framework | Data Point |
|-----------|-----------|-------------------|------------|
| "Too expensive" | Cost vs. value gap | Show LTV:CAC ratio + payback period | "Customers at your size see $3.2 ROI per $1 spent in 14 months" |
| "Not the right time" | Urgency deficit | Quantify cost of delay | "Each quarter delayed costs $X in lost [efficiency/revenue/retention]" |
| "[Competitor] is cheaper" | Commodity framing | Reframe on TCO + outcomes | "Lower price + lower retention = higher 3yr cost; here's the comparison" |
| "Need to think about it" | Missing stakeholder | Identify unmapped buyer | "What would make this a clear yes? Let me get you that data." |
| "We built it internally" | Build vs. buy bias | TCO + opportunity cost | "Internal tools cost 3-5x in eng time; here's the amortized comparison" |
| "Budget is frozen" | Timing/budget cycle | Reframe as next quarter pipeline | "Let's lock terms now so you can activate Q3 day 1." |

### Activation
```yaml
trigger: deal_stage >= 2 AND objection_logged
steps:
  - classify_objection: true
  - load_response_library: true
  - attach_proof_point: true   # case study, metric, or reference
  - log_objection_close_rate: true
output: objection_category, recommended_response, proof_point, follow_up_task
conversion_target: 0.55   # 55% objection-to-advancement rate
```

---

## Skill 3: Closing

**Purpose**: Convert qualified opportunities into signed contracts using structured close sequences.

**Trigger**: Deal stage 4+ (champion confirmed, economic buyer engaged, legal/paper process known).

**Revenue Impact**: Structured close sequences reduce average sales cycle by 8-12 days vs. open-ended follow-up.

### Close Sequence (7-Step)
| Step | Action | Timing | Revenue Signal |
|------|--------|--------|---------------|
| 1 | Mutual action plan sent | Day 0 | Shared commitment = 40% faster close |
| 2 | Commercial proposal with ROI model | Day 2 | Anchored value before price discussion |
| 3 | Champion alignment call | Day 4 | Internal champion confirmed live |
| 4 | Economic buyer demo / exec briefing | Day 6 | EB engaged = deal unstuck |
| 5 | Legal / MSA kickoff | Day 8 | Paper process started early |
| 6 | Pricing negotiation + T&Cs finalized | Day 12 | Final objection resolution window |
| 7 | Signature + kickoff scheduled | Day 14 | Deal closed |

### Closing Variants
| Variant | When | Tactic |
|---------|------|--------|
| Trial-to-paid | Freemium conversion | Usage-triggered upgrade nudge at 80% limit |
| End-of-quarter push | Quota pressure | Time-limited pricing with exec approval |
| Multi-year lock | Churn prevention | 15-20% discount for 24-month commit |
| Expansion close | Upsell trigger | Usage data + seat expansion ROI model |

### Activation
```yaml
trigger: deal_stage == 4 AND champion_confirmed == true
steps:
  - send_mutual_action_plan: true
  - attach_roi_model: true
  - schedule_eb_touchpoint: true
  - monitor_paper_process: true
  - set_close_date_target: "+14 days"
output: mutual_action_plan, roi_model, close_date_forecast
conversion_target: 0.68   # 68% stage-4-to-close rate
cost_model: tracked per deal in CRM; CAC charged at close
revenue_impact: forecast updated daily from stage x probability x ACV
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_discovery_questions]] | upstream | 0.27 |
| [[bld_knowledge_card_discovery_questions]] | upstream | 0.24 |
| [[bld_instruction_sales_playbook]] | upstream | 0.23 |
| [[bld_knowledge_card_sales_playbook]] | upstream | 0.23 |
| [[kc_sales_playbook]] | upstream | 0.22 |
| [[discovery-questions-builder]] | upstream | 0.22 |
| [[bld_output_template_discovery_questions]] | downstream | 0.22 |
| [[sales-playbook-builder]] | upstream | 0.22 |
| [[bld_examples_discovery_questions]] | downstream | 0.22 |
| [[bld_examples_sales_playbook]] | downstream | 0.21 |
