---
kind: output_template
id: bld_output_template_competitive_matrix
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for competitive_matrix production
quality: 9.2
title: "Output Template Competitive Matrix"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [competitive_matrix, builder, output_template]
tldr: "Feature-parity grid + battle card + Gartner MQ positioning template for competitive matrix"
domain: "competitive_matrix construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_competitive_matrix
  - bld_knowledge_card_competitive_matrix
  - p08_pat_pricing_framework
  - bld_output_template_knowledge_card
  - p10_out_benchmark_report
  - p03_sp_competitive_matrix_builder
  - p01_qg_competitive_matrix
  - pricing_optimization_memory
  - p01_kc_supabase_api
  - p06_schema_competitive_analysis
---

```yaml
---
id: p01_cm_{{slug}}.md
kind: competitive_matrix
pillar: P01
title: "{{market_segment}} Competitive Matrix"
version: "1.0.0"
author: "{{analyst_name}}"
domain: "{{market_domain}}"
quality: null
tags: [{{market_tag}}, competitive_matrix, battle_card]
tldr: "{{our_product}} vs {{competitor_count}} competitors on {{dimension_count}} dimensions"
competitors: [{{competitor_1}}, {{competitor_2}}, {{competitor_3}}]
metrics: [{{metric_1}}, {{metric_2}}, {{metric_3}}]
analysis_date: "{{YYYY-MM-DD}}"
key_insights: "{{top_differentiator_one_sentence}}"
---
```

## Market Context
| Field | Value |
|-------|-------|
| Segment | {{market_segment}} |
| Analysis Date | {{YYYY-MM-DD}} |
| Data Sources | {{source_list}} |
| Analyst | {{analyst_name}} |

## Feature Parity Grid
<!-- Rows = capabilities, Cols = us + competitors. Use: Yes / No / Partial / Roadmap -->

| Capability | {{our_product}} | {{competitor_1}} | {{competitor_2}} | {{competitor_3}} | Notes |
|------------|-----------------|------------------|------------------|------------------|-------|
| {{feature_1}} | {{val}} | {{val}} | {{val}} | {{val}} | {{note}} |
| {{feature_2}} | {{val}} | {{val}} | {{val}} | {{val}} | {{note}} |
| {{feature_3}} | {{val}} | {{val}} | {{val}} | {{val}} | {{note}} |

<!-- feature_n: specific capability, not vague category -->
<!-- val: Yes / No / Partial / Roadmap (Q{{quarter}} {{year}}) -->

## Gartner MQ Positioning (Qualitative)
<!-- Completeness of Vision x Ability to Execute per Gartner MQ methodology -->

| Vendor | Ability to Execute (1-5) | Completeness of Vision (1-5) | Quadrant |
|--------|--------------------------|------------------------------|----------|
| {{our_product}} | {{score}} | {{score}} | {{Leaders/Challengers/Visionaries/Niche}} |
| {{competitor_1}} | {{score}} | {{score}} | {{quadrant}} |
| {{competitor_2}} | {{score}} | {{score}} | {{quadrant}} |

## Battle Card: Us vs {{primary_competitor}}
<!-- Sales-ready, one-competitor-at-a-time comparison -->

| Dimension | {{our_product}} | {{primary_competitor}} | Win Reason |
|-----------|-----------------|------------------------|------------|
| {{capability_1}} | {{our_strength}} | {{their_weakness}} | {{why_we_win}} |
| {{capability_2}} | {{our_strength}} | {{their_weakness}} | {{why_we_win}} |
| Pricing | {{our_pricing}} | {{their_pricing}} | {{pricing_rationale}} |
| Support | {{our_support}} | {{their_support}} | {{support_rationale}} |
| Integrations | {{our_count}}+ | {{their_count}}+ | {{integration_rationale}} |

**Their likely objection:** "{{competitor_objection}}"
**Our counter:** "{{objection_counter}}"

## Pricing Comparison
| Vendor | Entry Tier | Mid Tier | Enterprise | Pricing Model |
|--------|-----------|----------|------------|---------------|
| {{our_product}} | {{price}} | {{price}} | {{price}} | {{per_user/flat/usage}} |
| {{competitor_1}} | {{price}} | {{price}} | {{price}} | {{model}} |
| {{competitor_2}} | {{price}} | {{price}} | {{price}} | {{model}} |

## Strategic Insights
**Our top differentiators:**
1. {{differentiator_1}} -- vs {{competitor_benefiting_from}}
2. {{differentiator_2}} -- vs {{competitor_benefiting_from}}
3. {{differentiator_3}} -- vs {{competitor_benefiting_from}}

**Gaps to address:**
- {{gap_1}} ({{competitor_leading_here}} leads here)
- {{gap_2}} ({{competitor_leading_here}} leads here)

**Anti-FUD guide:**
<!-- Factual responses to common competitor FUD claims -->
- If prospect says "{{competitor_fud_claim}}": respond with "{{factual_response_with_source}}"

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_competitive_matrix]] | downstream | 0.35 |
| [[bld_knowledge_card_competitive_matrix]] | upstream | 0.28 |
| [[p08_pat_pricing_framework]] | downstream | 0.26 |
| [[bld_output_template_knowledge_card]] | sibling | 0.26 |
| [[p10_out_benchmark_report]] | downstream | 0.25 |
| [[p03_sp_competitive_matrix_builder]] | upstream | 0.23 |
| [[p01_qg_competitive_matrix]] | downstream | 0.22 |
| [[pricing_optimization_memory]] | downstream | 0.21 |
| [[p01_kc_supabase_api]] | upstream | 0.19 |
| [[p06_schema_competitive_analysis]] | downstream | 0.18 |
