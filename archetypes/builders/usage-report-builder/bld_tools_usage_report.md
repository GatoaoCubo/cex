---
kind: tools
id: bld_tools_usage_report
pillar: P04
llm_function: CALL
purpose: Tools available for usage_report production
quality: null
title: "Tools Usage Report"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_report, builder, tools]
tldr: "Tools available for usage_report production"
domain: "usage_report construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| cex_compile.py | Aggregates raw usage data | Data collection phase |  
| cex_score.py | Calculates usage metrics | Post-processing |  
| cex_retriever.py | Fetches external data sources | Integration required |  
| cex_doctor.py | Diagnoses report inconsistencies | Validation stage |  
| cex_analyzer.py | Identifies usage patterns | Insight generation |  
| cex_formatter.py | Structures output for delivery | Finalization |  

## Validation Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| val_checker.py | Validates data integrity | Pre-processing |  
| val_validator.py | Ensures metric consistency | Post-scoring |  
| val_reporter.py | Logs validation results | QA phase |  

## External References  
- pandas (data manipulation)  
- Jupyter (interactive analysis)  
- Apache Airflow (orchestration)
