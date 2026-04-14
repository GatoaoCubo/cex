---
kind: quality_gate
id: p06_qg_edit_format
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for edit_format
quality: 9.0
title: "Quality Gate Edit Format"
version: "1.0.0"
author: wave1_builder_gen
tags: [edit_format, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for edit_format"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  

This ISO specifies an edit format: how diffs or patches are expressed and applied.
| metric | threshold | operator | scope |  
|---|---|---|---|  
| File Format Compliance | 100% | equals | All host files |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML Valid | Invalid YAML syntax |  
| H02 | ID matches pattern | ID does not match [a-zA-Z0-9_]+ |  
| H03 | kind matches | kind ≠ "edit_format" |  
| H04 | Required fields present | Missing 'action' or 'path' |  
| H05 | Syntax valid | Malformed JSON or YAML |  
| H06 | File size limit | Size > 10MB |  
| H07 | Metadata present | Missing 'author' or 'timestamp' |  
| H08 | Checksum valid | SHA-256 mismatch |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | YAML Structure | 0.15 | 1.0 for valid, 0.5 for minor issues |  
| D02 | ID Pattern | 0.15 | 1.0 for match, 0.0 for mismatch |  
| D03 | Kind Consistency | 0.10 | 1.0 for correct, 0.0 for incorrect |  
| D04 | Metadata Completeness | 0.15 | 1.0 for full, 0.5 for partial |  
| D05 | Syntax Quality | 0.15 | 1.0 for clean, 0.0 for errors |  
| D06 | File Size | 0.05 | 1.0 for ≤10MB, 0.0 for >10MB |  
| D07 | Checksum Validity | 0.10 | 1.0 for valid, 0.0 for invalid |  
| D08 | Documentation | 0.15 | 1.0 for clear, 0.5 for vague |  

## Actions  
| Score | Action |  
|---|---|  
| ≥9.5 | Automatically merge and notify |  
| ≥8.0 | Schedule for review |  
| ≥7.0 | Request changes |  
| <7.0 | Block and require fixes |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Critical hotfix with emergency approval | Senior Architect | Email confirmation, system log entry |
