---
kind: collaboration
id: bld_collaboration_eval_framework
pillar: P12
llm_function: COLLABORATE
purpose: How eval_framework-builder works in crews with other builders
quality: 8.9
title: "Collaboration Eval Framework"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_framework, builder, collaboration]
tldr: "How eval_framework-builder works in crews with other builders"
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Designs and implements evaluation framework infrastructure, enabling modular integration of metrics, benchmarks, and execution pipelines. Acts as a central coordination layer for evaluation processes.  

## Receives From  
| Builder         | What                  | Format      |  
|------------------|-----------------------|-------------|  
| Config Manager   | Framework config specs| YAML        |  
| Benchmark Suite  | Integration requests  | API         |  
| Eval Metric      | Metric registration   | JSON        |  
| Data Engineer    | Data schema definitions| Avro        |  

## Produces For  
| Builder         | What                  | Format      |  
|------------------|-----------------------|-------------|  
| Benchmark Suite  | Framework API         | Python      |  
| Eval Metric      | Documentation spec    | Markdown    |  
| Test Engineer    | Validation test suite | pytest      |  
| UI/UX Team       | Framework UI spec     | Figma       |  

## Boundary  
Does NOT collect benchmarks (handled by benchmark_suite) or define individual metrics (handled by eval_metric). Does NOT curate datasets (handled by data_engineer). Does NOT handle deployment or CI/CD (handled by devops).
