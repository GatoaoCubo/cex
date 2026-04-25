---
kind: tools
id: bld_tools_roi_calculator
pillar: P04
llm_function: CALL
purpose: Tools available for roi_calculator production
quality: 8.9
title: "Tools Roi Calculator"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [roi_calculator, builder, tools]
tldr: "Tool registry for roi calculator builder: CEX pipeline tools (compile, score, retrieve), file system ops (Read/Write/Edit/Glob/Grep), and domain-specific automation for roi calculator spec with inputs, formulas, tco comparison for economic buyers."
domain: "roi_calculator construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_discovery_questions
  - bld_tools_sales_playbook
  - bld_tools_benchmark_suite
  - bld_tools_competitive_matrix
  - bld_tools_churn_prevention_playbook
  - bld_tools_pricing_page
  - bld_tools_eval_metric
  - bld_tools_legal_vertical
  - bld_tools_rbac_policy
  - bld_tools_api_reference
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile artifact after production | F8 COLLABORATE |
| cex_score.py | Score artifact quality (5D dimensions) | F7 GOVERN |
| cex_retriever.py | Retrieve similar ROI calculator artifacts for reuse | F3 INJECT |
| cex_doctor.py | Validate builder health, check ISO completeness | F7 GOVERN |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Structural YAML + frontmatter validation | Post-production |
| cex_hooks.py | Pre-commit ASCII and schema checks | Pre-commit |

## External References
- Forrester TEI (Total Economic Impact) methodology
- Gartner TCO framework
- IFRS/GAAP NPV calculation standards

## CEX Pipeline Tools

| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml | After Write (F8) |
| cex_score.py | Peer-review quality scoring | After production (F7) |
| cex_retriever.py | Discover similar artifacts by TF-IDF | During F3 INJECT |
| cex_doctor.py | Health check builder ISOs | Before dispatch |

## Data Sources

| Source | Content | When to use |
|--------|---------|-------------|
| SCHEMA.md | Field definitions, ID pattern, constraints | Every production run |
| OUTPUT_TEMPLATE.md | Exact frontmatter + body structure | Every production run |
| QUALITY_GATES.md | H01-H08 HARD gates | Every validation run |
| KNOWLEDGE.md | Domain concepts for roi calculator | When designing structure |
| MEMORY.md | Common mistakes, anti-patterns | When stuck or producing a variant |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Properties

| Property | Value |
|----------|-------|
| Kind | `tools` |
| Pillar | P04 |
| Domain | roi calculator construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_discovery_questions]] | sibling | 0.49 |
| [[bld_tools_sales_playbook]] | sibling | 0.47 |
| [[bld_tools_benchmark_suite]] | sibling | 0.41 |
| [[bld_tools_competitive_matrix]] | sibling | 0.40 |
| [[bld_tools_churn_prevention_playbook]] | sibling | 0.38 |
| [[bld_tools_pricing_page]] | sibling | 0.37 |
| [[bld_tools_eval_metric]] | sibling | 0.37 |
| [[bld_tools_legal_vertical]] | sibling | 0.36 |
| [[bld_tools_rbac_policy]] | sibling | 0.36 |
| [[bld_tools_api_reference]] | sibling | 0.36 |
