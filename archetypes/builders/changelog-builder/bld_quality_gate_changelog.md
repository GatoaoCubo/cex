---
kind: quality_gate
id: p01_qg_changelog
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for changelog
quality: null
title: "Quality Gate Changelog"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for changelog"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(metric, threshold, operator, scope)  
Schema ID pattern, ^p01_ch_[a-z][a-z0-9_]+.md$, matches, all changelog files  

## HARD Gates  
(ID | Check | Fail Condition)  
H01 | YAML frontmatter valid | invalid YAML syntax  
H02 | ID matches pattern ^p01_ch_[a-z][a-z0-9_]+.md$ | invalid filename format  
H03 | kind field matches 'changelog' | kind ≠ 'changelog'  
H04 | semver version present | missing version field  
H05 | features section exists | missing 'features' list  
H06 | fixes section exists | missing 'fixes' list  
H07 | breaking changes section exists | missing 'breaking_changes' list  
H08 | no markdown in sections | markdown detected in features/fixes/breaking_changes  

## SOFT Scoring  
(Dim | Dimension | Weight | Scoring Guide)  
Clarity | Readability of entries | 0.15 | 1.0=clear, 0.0=ambiguous  
Completeness | All required sections filled | 0.20 | 1.0=all present, 0.0=missing  
Structure | Consistent formatting | 0.15 | 1.0=uniform, 0.0=disjointed  
Consistency | Semver alignment with code | 0.15 | 1.0=matches, 0.0=conflicting  
Semver Accuracy | Correct version bump | 0.10 | 1.0=correct, 0.0=incorrect  
Date Format | ISO 8601 date | 0.10 | 1.0=valid, 0.0=invalid  
Summary Quality | Concise summary present | 0.15 | 1.0=clear, 0.0=missing  

## Actions  
(Score | Action)  
GOLDEN | >=9.5 | Auto-publish  
PUBLISH | >=8.0 | Auto-publish  
REVIEW | >=7.0 | Require review  
REJECT | <7.0 | Block release  

## Bypass  
(conditions, approver, audit trail)  
Urgent hotfix with CTO approval, CTO, audit log entry with timestamp and reason
