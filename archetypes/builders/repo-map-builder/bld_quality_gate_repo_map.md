---
kind: quality_gate
id: p01_qg_repo_map
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for repo_map
quality: null
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
| H02 | ID matches pattern | ID does not match `repo-[a-z0-9]{8}` |  
| H03 | kind matches | kind ≠ `repo_map` |  
| H04 | Required fields present | Missing `name`, `path`, or `language` |  
| H05 | Unique IDs | Duplicate ID detected |  
| H06 | URL valid | `url` field invalid or unreachable |  
| H07 | Versioning correct | Version format ≠ `vX.Y.Z` |  
| H08 | No duplicate repos | Multiple entries for same repo |  
| H09 | Language accurate | Language mismatch with code files |  
| H10 | License present | Missing SPDX license identifier |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | YAML Structure | 0.15 | 1.0 for valid, 0.5 for minor issues |  
| D02 | Completeness | 0.15 | 1.0 for ≥90% fields filled |  
| D03 | Consistency | 0.12 | 1.0 for uniform naming/structuring |  
| D04 | URL Validity | 0.10 | 1.0 for all URLs functional |  
| D05 | Versioning | 0.10 | 1.0 for semver compliance |  
| D06 | Language Accuracy | 0.12 | 1.0 for accurate language tags |  
| D07 | License Presence | 0.10 | 1.0 for valid SPDX license |  
| D08 | Documentation | 0.16 | 1.0 for clear repo descriptions |  

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
