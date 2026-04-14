---
kind: tools
id: bld_tools_sdk_example
pillar: P04
llm_function: CALL
purpose: Tools available for sdk_example production
quality: null
title: "Tools Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, tools]
tldr: "Tools available for sdk_example production"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| cex_compile.py | Compiles SDK examples into executable formats | During build phase |  
| cex_score.py | Evaluates example quality using predefined metrics | Post-validation |  
| cex_retriever.py | Fetches external data required for example execution | Pre-runtime setup |  
| cex_doctor.py | Diagnoses and repairs common SDK configuration issues | On first run or deployment |  
| cex_deployer.py | Packages examples for distribution across environments | Release preparation |  
| cex_formatter.py | Standardizes code style and documentation in examples | Pre-commit checks |  

## Validation Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| val_check.py | Verifies example integrity and completeness | Pre-validation |  
| val_validator.py | Enforces SDK-specific rules and constraints | During testing |  
| val_comparer.py | Compares example outputs against expected results | Post-execution |  
| val_linter.py | Enforces code style and best practices | Pre-commit |  

## External References  
- ExampleML: Machine learning framework for SDK example generation  
- ExampleDB: Database schema for storing example metadata  
- ExampleTest: Unit testing framework for SDK validation scenarios
