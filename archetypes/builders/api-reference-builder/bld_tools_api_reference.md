---
kind: tools
id: bld_tools_api_reference
pillar: P04
llm_function: CALL
purpose: Tools available for api_reference production
quality: null
title: "Tools Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, tools]
tldr: "Tools available for api_reference production"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool              | Purpose                  | When                          |  
|-------------------|--------------------------|-------------------------------|  
| cex_compile.py    | Compiles API specs       | During reference generation   |  
| cex_score.py      | Scores API quality       | Post-validation               |  
| cex_retriever.py  | Fetches API endpoints    | Pre-processing                |  
| cex_doctor.py     | Diagnoses spec issues    | On error detection            |  
| cex_formatter.py  | Standardizes output      | Before final export           |  

## Validation Tools  
| Tool              | Purpose                  | When                          |  
|-------------------|--------------------------|-------------------------------|  
| val_checker.py    | Validates spec consistency | Post-compilation              |  
| val_linter.py     | Enforces style rules     | During development            |  
| val_tester.py     | Runs integration tests   | Pre-deployment                |  

## External References  
- Swagger UI (API visualization)  
- OpenAPI Generator (spec generation)  
- Pydantic (data validation)
