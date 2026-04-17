---
kind: quality_gate
id: p01_qg_repo_map
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for repo_map
quality: 9.0
title: "Quality Gate Repo Map"
version: "1.0.0"
author: wave1_builder_gen
tags: [repo_map, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for repo_map"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Repo Map Completeness | 90% | ≥ | All repositories |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML valid | Invalid YAML syntax |  
| H02 | ID matches pattern | ID does not match `^p01_rm_[a-zA-Z0-9_]+$` (schema pattern) |
| H03 | kind matches | kind != `repo_map` |
| H04 | Token budget defined | Missing `token_budget` field |  
| H05 | Symbol table present | No function/class signatures in body |
| H06 | Token budget defined | Missing token_budget field |
| H07 | Tokens within budget | tokens_used > token_budget |
| H08 | Extraction method specified | Missing extraction_method field |
| H09 | File count matches body | file_count != actual files in symbol table |
| H10 | No flat file tree | Body contains only paths without signatures |  

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Symbol Extraction | 0.25 | tree-sitter signatures present=1.0; file paths only=0.3 |
| D02 | Token Budget Compliance | 0.20 | tokens_used <= budget=1.0; exceeded=0.0 |
| D03 | PageRank Ranking | 0.20 | scores shown, personalization applied=1.0; no ranking=0.3 |
| D04 | File Selection Heuristics | 0.15 | all 4 rules documented=1.0; none documented=0.4 |
| D05 | Structural Completeness | 0.20 | all template sections present=1.0; missing sections=0.5 |

**Weight sum: 0.25+0.20+0.20+0.15+0.20 = 1.00**  

## Actions  
| Score | Action |  
|---|---|  
| ≥9.5 | GOLDEN: Auto-approve and promote |  
| ≥8.0 | PUBLISH: Merge and notify stakeholders |  
| ≥7.0 | REVIEW: Flag for manual inspection |  
| <7.0 | REJECT: Block and require fixes |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Critical bug fix | Lead Architect | Change request #12345 |  
| Legacy system migration | CTO | Emergency ticket #67890 |  
| External dependency update | DevOps Manager | Dependency ticket #54321 |
