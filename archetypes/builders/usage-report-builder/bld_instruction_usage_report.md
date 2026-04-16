---
kind: instruction
id: bld_instruction_usage_report
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for usage_report
quality: 8.9
title: "Instruction Usage Report"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_report, builder, instruction]
tldr: "Step-by-step production process for usage_report"
domain: "usage_report construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify stakeholders (billing, CFO, product teams) for requirement alignment.  
2. Map data sources (e.g., API logs, database queries, usage events).  
3. Define key metrics: active users, API calls, storage consumption, cost per feature.  
4. Audit existing reports to avoid duplication and ensure gaps are filled.  
5. Document compliance requirements (data privacy, retention policies).  
6. Create a preliminary report outline with sections: summary, trends, anomalies.  

## Phase 2: COMPOSE  
1. Set up environment with tools: Python (pandas), SQL, and report generation libraries.  
2. Reference SCHEMA.md to define fields: `report_id`, `metric`, `value`, `timestamp`.  
3. Use OUTPUT_TEMPLATE.md to structure tables, charts, and narrative sections.  
4. Aggregate data from sources, ensuring timestamps are normalized (UTC).  
5. Apply schema validation rules (e.g., `metric` must be in enum: "storage", "API").  
6. Generate visualizations (bar charts for monthly trends, heatmaps for anomalies).  
7. Write narrative analysis: highlight cost drivers, usage spikes, seasonal patterns.  
8. Embed metadata: author, report version, data source versions.  
9. Export artifact as PDF and CSV, adhering to OUTPUT_TEMPLATE.md formatting.  

## Phase 3: VALIDATE  
- [ ] Cross-check aggregated data against source systems (SQL queries, logs).  
- [ ] Ensure schema compliance using JSON schema validator (refer to SCHEMA.md).  
- [ ] Verify visualizations match data (e.g., bar chart axes, color coding).  
- [ ] Confirm all required fields in OUTPUT_TEMPLATE.md are populated.  
- [ ] Obtain stakeholder sign-off on accuracy and completeness.
