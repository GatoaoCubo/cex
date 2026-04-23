---
kind: config
id: bld_config_prompt_optimizer
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for prompt_optimizer production
quality: 8.7
title: "Config Prompt Optimizer"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_optimizer, builder, config]
tldr: "Naming, paths, limits for prompt_optimizer production"
domain: "prompt_optimizer construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_workflow_node
  - bld_config_visual_workflow
  - bld_config_graph_rag_config
  - bld_config_prompt_technique
  - bld_config_search_strategy
  - bld_config_customer_segment
  - bld_config_sales_playbook
  - bld_config_pricing_page
  - bld_config_diff_strategy
  - bld_config_usage_quota
---

## Naming Convention  
Pattern: p03_po_{{name}}.md  
Examples: p03_po_chatbot.md, p03_po_summarizer.md  

## Paths  
Artifacts: /opt/cex/prompt_optimizers/artifacts/{{name}}  
Logs: /var/log/cex/po/{{name}}  

## Limits  
max_bytes: 5120  
max_turns: 20  
effort_level: 3  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null  

```
   __  __           _       _           
  |  \/  |         | |     | |          
  | \  / | __ _  __| | __ _| |_ ___ _ __
  | |\/| |/ _` |/ _` |/ _` | __/ _ \ '__|
  | |  | | (_| | (_| | (_| | ||  __/ |   
  |_|  |_|\__,_|\__,_|\__,_|\__\___|_|   
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_workflow_node]] | sibling | 0.59 |
| [[bld_config_visual_workflow]] | sibling | 0.58 |
| [[bld_config_graph_rag_config]] | sibling | 0.57 |
| [[bld_config_prompt_technique]] | sibling | 0.57 |
| [[bld_config_search_strategy]] | sibling | 0.57 |
| [[bld_config_customer_segment]] | sibling | 0.56 |
| [[bld_config_sales_playbook]] | sibling | 0.56 |
| [[bld_config_pricing_page]] | sibling | 0.55 |
| [[bld_config_diff_strategy]] | sibling | 0.55 |
| [[bld_config_usage_quota]] | sibling | 0.55 |
