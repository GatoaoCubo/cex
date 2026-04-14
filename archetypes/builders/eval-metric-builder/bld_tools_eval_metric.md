---
kind: tools
id: bld_tools_eval_metric
pillar: P04
llm_function: CALL
purpose: Tools available for eval_metric production
quality: null
title: "Tools Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, tools]
tldr: "Tools available for eval_metric production"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| cex_compile.py | Compiles metric configurations into executable code | During metric setup |  
| cex_score.py | Applies scoring logic to evaluation data | After data processing |  
| cex_retriever.py | Fetches benchmark datasets for evaluation | When initializing metrics |  
| cex_doctor.py | Debugs inconsistencies in metric outputs | During validation phase |  
| cex_validator.py | Ensures metric compliance with spec standards | Before deployment |  
| cex_formatter.py | Converts raw scores into human-readable reports | For final output delivery |  

## Validation Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| metric_validator.py | Checks metric consistency across datasets | During testing |  
| benchmark_comparator.py | Compares results against reference benchmarks | For accuracy verification |  
| visualizer.py | Generates plots for metric performance trends | When analyzing results |  
| stress_tester.py | Tests edge cases in metric calculations | During robustness checks |  

## External References  
- Hugging Face Datasets: For benchmark data handling  
- MLflow: For experiment tracking and metric logging  
- SciPy: For statistical validation of scores
