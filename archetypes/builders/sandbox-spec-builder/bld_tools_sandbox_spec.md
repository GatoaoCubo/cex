---
kind: tools
id: bld_tools_sandbox_spec
pillar: P04
llm_function: CALL
purpose: Tools available for sandbox_spec production
quality: null
title: "Tools Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, tools]
tldr: "Tools available for sandbox_spec production"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool | Purpose | When |  
|---|---|---|  
| cex_compile.py | Generate sandbox spec from source | Pre-deployment |  
| cex_score.py | Evaluate spec compliance | Post-validation |  
| cex_retriever.py | Fetch external data for spec | During spec building |  
| cex_doctor.py | Debug and repair spec issues | On error detection |  

## Validation Tools  
| Tool | Purpose | When |  
|---|---|---|  
| val_checker.py | Verify spec consistency | Pre-validation |  
| val_linter.py | Check syntax and formatting | During development |  
| val_comparator.py | Compare specs across versions | Post-update |  

## External References  
- CEX Framework (spec validation)  
- Sandbox Validator (compliance checks)  
- JSON Schema (data structure validation)
