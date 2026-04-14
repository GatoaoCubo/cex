---
kind: tools
id: bld_tools_contributor_guide
pillar: P04
llm_function: CALL
purpose: Tools available for contributor_guide production
quality: null
title: "Tools Contributor Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [contributor_guide, builder, tools]
tldr: "Tools available for contributor_guide production"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| cex_compile.py | Generates contributor guide from templates | On initial build |  
| cex_score.py | Evaluates guide quality via heuristic checks | During validation |  
| cex_retriever.py | Fetches external content (e.g., licenses) | When linking to external resources |  
| cex_doctor.py | Diagnoses common contributor guide issues | On demand or pre-commit |  
| cex_formatter.py | Enforces style consistency (e.g., headers, lists) | Pre-commit or manual runs |  
| cex_linter.py | Validates code examples and syntax | When adding code snippets |  

## Validation Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| validate_guide.py | Checks structure and required sections | Pre-release |  
| check_links.py | Verifies internal/external links | On build |  
| syntax_validator.py | Ensures Markdown/HTML syntax compliance | Pre-commit |  
| consistency_checker.py | Identifies duplicate or conflicting content | During updates |  

## External References  
- Markdownlint (https://github.com/DavidAnson/markdownlint)  
- Sphinx (https://www.sphinx-doc.org/)  
- Git (https://git-scm.com/)
