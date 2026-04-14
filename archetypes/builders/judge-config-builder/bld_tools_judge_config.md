---
kind: tools
id: bld_tools_judge_config
pillar: P04
llm_function: CALL
purpose: Tools available for judge_config production
quality: null
title: "Tools Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, tools]
tldr: "Tools available for judge_config production"
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool              | Purpose                  | When                          |  
|-------------------|--------------------------|-------------------------------|  
| cex_compile.py    | Generate judge config    | Initial config creation       |  
| cex_score.py      | Evaluate config quality  | Post-validation scoring       |  
| cex_retriever.py  | Fetch external data      | When external references needed |  
| cex_doctor.py     | Debug config issues      | During troubleshooting        |  

## Validation Tools  
| Tool              | Purpose                  | When                          |  
|-------------------|--------------------------|-------------------------------|  
| val_check.py      | Validate syntax          | Pre-deployment checks         |  
| val_compare.py    | Compare config versions  | During updates                |  
| val_linter.py     | Enforce style guidelines | Code review phase             |  

## External References  
- JSON Schema (for config validation)  
- PyYAML (for config parsing)  
- pytest (for unit testing judge logic)
