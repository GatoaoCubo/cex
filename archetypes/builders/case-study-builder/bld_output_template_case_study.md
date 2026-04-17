---
kind: output_template
id: bld_output_template_case_study
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for case_study production
quality: 9.1
title: "Output Template Case Study"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, output_template]
tldr: "Challenge-Solution-Outcome template with pullquote, ROI call-out, and KPI table"
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p05_cs_{{slug}}.md
kind: case_study
pillar: P05
title: "{{customer_name}}: {{outcome_headline}}"
version: "1.0.0"
author: "{{content_author}}"
domain: "{{industry}}"
quality: null
tags: [{{industry_tag}}, {{product_tag}}, case_study]
tldr: "{{one_sentence_result}} -- {{customer_name}}, {{champion_title}}"
context: "{{challenge_summary_50_words}}"
outcome: "{{primary_kpi_result}}"
---
```

<!-- slug: lowercase_underscores (e.g., healthtech_aws_2024) -->
<!-- outcome_headline: "Reduced Downtime 85% with X" -->

## Company Snapshot
| Field | Value |
|-------|-------|
| Company | {{customer_name}} |
| Industry | {{industry}} |
| Size | {{employee_count}} employees |
| Region | {{region}} |
| Champion | {{champion_name}}, {{champion_title}} |
| Product Used | {{cex_product}} |

## The Challenge
<!-- 150-200 words. Before-state, pain context, business stakes. -->
{{challenge_narrative}}

**Key pain points:**
- {{pain_point_1}}
- {{pain_point_2}}
- {{pain_point_3}}

## The Solution
<!-- Named features, deployment timeline, integrations. -->
{{solution_narrative}}

**Implementation:**
- Timeline: {{deployment_weeks}} weeks
- Key features: {{feature_list}}
- Integrations: {{integration_list}}

## The Outcome
<!-- 3+ KPIs with before/after comparison. -->
{{outcome_narrative}}

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| {{kpi_1_name}} | {{kpi_1_before}} | {{kpi_1_after}} | {{kpi_1_delta}} |
| {{kpi_2_name}} | {{kpi_2_before}} | {{kpi_2_after}} | {{kpi_2_delta}} |
| {{kpi_3_name}} | {{kpi_3_before}} | {{kpi_3_after}} | {{kpi_3_delta}} |

## ROI Call-Out
> **{{roi_headline_metric}}** in {{roi_timeframe}}
> Source: {{roi_source}} ({{roi_date}})

## Customer Pullquote
> "{{pullquote_text_50_80_words}}"
>
> -- {{champion_name}}, {{champion_title}}, {{customer_name}}

## Lessons Learned
<!-- 50-100 words. Transferable insight for similar customers. -->
{{lessons_learned}}
