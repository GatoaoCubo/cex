---
kind: tools
id: bld_tools_edit_format
pillar: P04
llm_function: CALL
purpose: Tools available for edit_format production
quality: 8.9
title: "Tools Edit Format"
version: "1.0.0"
author: wave1_builder_gen
tags: [edit_format, builder, tools]
tldr: "Tools available for edit_format production"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Production Tools  

This ISO specifies an edit format: how diffs or patches are expressed and applied.
| Tool | Purpose | When |  
|------|---------|------|  
| cex_compile.py | Compiles format definitions into executable rules | During format deployment |  
| cex_score.py | Scores data against format rules for compliance | During validation phases |  
| cex_retriever.py | Retrieves format templates from external repositories | When initializing new formats |  
| cex_doctor.py | Diagnoses format rule conflicts and suggests fixes | During rule editing |  
| cex_formatter.py | Applies format rules to transform raw data | During data preprocessing |  
| cex_validator.py | Validates format rule syntax and semantics | Before rule deployment |  

## Validation Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| val_checker.py | Ensures format rules meet quality standards | During rule review |  
| val_analyzer.py | Analyzes rule coverage across data types | During format design |  
| val_comparator.py | Compares format outputs against golden standards | During testing |  
| val_profiler.py | Profiles rule performance on large datasets | During optimization |  

## External References  
- LintTools (static analysis framework)  
- FormatX (cross-format compatibility library)  
- JSON Schema (standard for data structure validation)
