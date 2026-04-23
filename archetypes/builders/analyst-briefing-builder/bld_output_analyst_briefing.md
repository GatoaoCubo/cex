---
kind: output_template
id: bld_output_template_analyst_briefing
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for analyst_briefing production
quality: 9.1
title: "Output Template Analyst Briefing"
version: "1.0.0"
author: n01_wave6
tags: [analyst_briefing, builder, output_template]
tldr: "Template with vars for analyst_briefing production"
domain: "analyst_briefing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_analyst_briefing
  - bld_schema_analyst_briefing
  - bld_knowledge_card_analyst_briefing
  - p03_sp_analyst_briefing_builder
  - analyst-briefing-builder
  - bld_instruction_analyst_briefing
  - p05_qg_analyst_briefing
  - p10_mem_analyst_briefing_builder
  - bld_collaboration_analyst_briefing
  - bld_config_analyst_briefing
---

```markdown
---
id: p05_ab_{{vendor_slug}}_{{analyst_firm}}_{{year}}.md
kind: analyst_briefing
pillar: P05
analyst_firm: {{analyst_firm}}       <!-- gartner | forrester | idc -->
research_track: {{research_track}}   <!-- magic-quadrant | wave | marketscape | innovators -->
vendor: {{vendor_name}}
briefing_date: {{briefing_date}}     <!-- ISO date e.g. 2026-06-15 -->
embargo_flag: {{embargo_flag}}       <!-- true | false -->
quality: null
title: "Analyst Briefing: {{vendor_name}} for {{analyst_firm}} {{research_track}} {{year}}"
version: "1.0.0"
---

## Company Overview
{{vendor_name}} (founded {{founding_year}}, HQ: {{hq_city}}) provides {{product_category}} to {{target_market}}. ARR: ${{arr}}M. Employees: {{employee_count}}. YoY growth: {{growth_pct}}%.

## Market Position
Framework: {{analyst_firm}} {{research_track}}
Position claimed: {{claimed_position}}  <!-- e.g., Visionary (Gartner MQ), Strong Performer (Forrester Wave) -->

| Evaluation Axis | Our Score | Key Evidence |
|----------------|-----------|--------------|
| {{axis_1}}     | {{score_1}} | {{evidence_1}} |
| {{axis_2}}     | {{score_2}} | {{evidence_2}} |

## Product Strengths
1. **{{strength_1}}** -- {{proof_point_1}} (source: {{source_1}})
2. **{{strength_2}}** -- {{proof_point_2}} (source: {{source_2}})
3. **{{strength_3}}** -- {{proof_point_3}} (source: {{source_3}})

## Competitive Landscape
| Vendor | Our Advantage | Their Advantage |
|--------|---------------|-----------------|
| {{competitor_1}} | {{our_diff_1}} | {{their_diff_1}} |
| {{competitor_2}} | {{our_diff_2}} | {{their_diff_2}} |

Win rate vs {{competitor_1}}: {{win_rate_1}}%. Win rate vs {{competitor_2}}: {{win_rate_2}}%.

## Roadmap
> {{#if embargo_flag}}NDA/Embargo: Content below is confidential.{{/if}}

| Quarter | Milestone | Analyst Relevance |
|---------|-----------|-------------------|
| {{q1}}  | {{milestone_1}} | {{relevance_1}} |
| {{q2}}  | {{milestone_2}} | {{relevance_2}} |

## Anticipated Analyst Questions
**Q1: {{question_1}}**
{{answer_1}}

**Q2: {{question_2}}**
{{answer_2}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_analyst_briefing]] | downstream | 0.56 |
| [[bld_schema_analyst_briefing]] | downstream | 0.48 |
| [[bld_knowledge_card_analyst_briefing]] | upstream | 0.42 |
| [[p03_sp_analyst_briefing_builder]] | upstream | 0.38 |
| [[analyst-briefing-builder]] | related | 0.38 |
| [[bld_instruction_analyst_briefing]] | upstream | 0.37 |
| [[p05_qg_analyst_briefing]] | downstream | 0.36 |
| [[p10_mem_analyst_briefing_builder]] | downstream | 0.31 |
| [[bld_collaboration_analyst_briefing]] | downstream | 0.26 |
| [[bld_config_analyst_briefing]] | downstream | 0.25 |
