---
kind: tools
id: bld_tools_app_directory_entry
pillar: P04
llm_function: CALL
purpose: Tools available for app_directory_entry production
quality: null
title: "Tools App Directory Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [app_directory_entry, builder, tools]
tldr: "Tools available for app_directory_entry production"
domain: "app_directory_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| cex_compile.py | Compiles app directory entries | During entry creation |  
| cex_score.py | Scores entries based on quality metrics | During validation phase |  
| cex_retriever.py | Retrieves external data for entries | When populating metadata |  
| cex_doctor.py | Diagnoses entry inconsistencies | During pre-deployment checks |  
| cex_validator.py | Validates entry structure | On submission |  
| cex_analyzer.py | Analyzes entry performance | Post-deployment |  

## Validation Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| validator_check.py | Ensures compliance with app directory standards | During entry submission |  
| schema_validator.py | Validates JSON schema integrity | On metadata updates |  
| consistency_checker.py | Checks cross-entry data consistency | During bulk imports |  
| code_linter.py | Lints code snippets in entries | On code submission |  

## External References  
- JSON Schema (for metadata validation)  
- Pydantic (for data model validation)  
- Requests (for API data retrieval)
