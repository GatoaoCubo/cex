---
kind: output_template
id: bld_output_template_customer_segment
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for customer_segment production
quality: 9.1
title: "Output Template Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, output_template]
tldr: "Template with vars for customer_segment production"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_customer_segment
  - bld_examples_customer_segment
  - n07_memory_industry_audit
  - p02_qg_customer_segment
  - bld_schema_customer_segment
  - p03_sp_customer_segment_builder
  - n06_kc_icp_frameworks
  - bld_instruction_customer_segment
  - p03_sp_discovery_questions_builder
  - p10_out_research_brief
---

```yaml
---
id: p02_cs_{{segment_name}}.md
kind: customer_segment
pillar: P02
title: "{{segment_title}}"
version: "1.0"
created: {{created_at}}
updated: {{updated_at}}
author: {{author}}
domain: "{{domain}}"
quality: null
tags: [{{tags}}]
tldr: "{{one_sentence_summary}}"
customer_type: "{{customer_type}}"
segmentation_criteria: [{{criteria_list}}]
---
```

<!-- id: Generated filename following p02_cs_[a-z][a-z0-9_]+.md pattern -->
<!-- segment_title: Human-readable name (e.g., "Mid-Market SaaS B2B") -->
<!-- customer_type: "B2B", "B2C", or "B2B2C" -->
<!-- criteria_list: e.g., "industry", "company_size", "revenue_range" -->
<!-- quality: Always null -- peer review assigns -->

## Overview
{{segment_overview}}

<!-- segment_overview: 2-3 sentences describing who this segment is and why they matter -->

## Firmographics

| Attribute | Value | Source |
|-----------|-------|--------|
| Industry vertical | {{industry}} | {{data_source}} |
| Company size | {{employee_range}} | {{data_source}} |
| Annual revenue | {{revenue_range}} | {{data_source}} |
| Geography | {{geography}} | {{data_source}} |
| Tech stack | {{tech_indicators}} | {{data_source}} |

<!-- industry: e.g., "SaaS", "Healthcare", "Manufacturing" -->
<!-- employee_range: e.g., "50-500 employees" -->
<!-- revenue_range: e.g., "$5M-$50M ARR" -->
<!-- geography: e.g., "North America, Western Europe" -->
<!-- tech_indicators: technographic signals (e.g., "Salesforce, Slack") -->

## Customer Needs (Jobs-to-be-Done)

| Job | Pain Point | Success Metric |
|-----|-----------|----------------|
| {{job_1}} | {{pain_1}} | {{metric_1}} |
| {{job_2}} | {{pain_2}} | {{metric_2}} |

## ICP Signals

| Signal Type | Indicator | Score Weight |
|-------------|-----------|-------------|
| BANT - Budget | {{budget_signal}} | {{weight}} |
| BANT - Authority | {{authority_signal}} | {{weight}} |
| BANT - Need | {{need_signal}} | {{weight}} |
| BANT - Timeline | {{timeline_signal}} | {{weight}} |
| PLG signal | {{product_led_signal}} | {{weight}} |

## Use Cases

1. {{use_case_1}}
2. {{use_case_2}}
3. {{use_case_3}}

## Key Metrics

| Metric | Target | Benchmark |
|--------|--------|-----------|
| CAC | {{cac_target}} | {{industry_benchmark}} |
| LTV | {{ltv_target}} | {{industry_benchmark}} |
| LTV:CAC ratio | {{ratio_target}} | 3:1 (industry standard) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_customer_segment]] | upstream | 0.24 |
| [[bld_examples_customer_segment]] | downstream | 0.22 |
| [[n07_memory_industry_audit]] | downstream | 0.18 |
| [[p02_qg_customer_segment]] | downstream | 0.18 |
| [[bld_schema_customer_segment]] | downstream | 0.18 |
| [[p03_sp_customer_segment_builder]] | upstream | 0.18 |
| [[n06_kc_icp_frameworks]] | upstream | 0.17 |
| [[bld_instruction_customer_segment]] | upstream | 0.16 |
| [[p03_sp_discovery_questions_builder]] | upstream | 0.15 |
| [[p10_out_research_brief]] | downstream | 0.15 |
