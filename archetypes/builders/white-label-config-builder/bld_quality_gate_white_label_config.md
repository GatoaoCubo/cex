---
kind: quality_gate
id: p09_qg_white_label_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for white_label_config
quality: null
title: "Quality Gate White Label Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [white_label_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for white_label_config"
domain: "white_label_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric         | threshold                              | operator | scope         |  
|----------------|----------------------------------------|----------|---------------|  
| schema_id      | ^p09_wl_[a-z][a-z0-9_]+.yaml$         | matches  | all YAML files|  

## HARD Gates  
| ID  | Check                          | Fail Condition                                      |  
|-----|--------------------------------|-----------------------------------------------------|  
| H01 | YAML frontmatter valid       | Missing or invalid YAML frontmatter                 |  
| H02 | ID matches pattern           | ID does not match ^p09_wl_[a-z][a-z0-9_]+.yaml$    |  
| H03 | kind field matches           | kind ≠ 'white_label_config'                       |  
| H04 | brand_name field present     | brand_name missing or empty                       |  
| H05 | reseller_id field present    | reseller_id missing or invalid                    |  
| H06 | custom_logo_url valid        | URL invalid or unreachable                        |  
| H07 | allowed_domains field valid  | allowed_domains missing or not a list             |  

## SOFT Scoring  
| Dim | Dimension                  | Weight | Scoring Guide                                      |  
|-----|----------------------------|--------|----------------------------------------------------|  
| D01 | Branding completeness      | 0.15   | 100% complete = 1.0; missing fields = 0.5          |  
| D02 | API key security           | 0.15   | Encrypted keys = 1.0; plaintext = 0.2              |  
| D03 | Customization options      | 0.10   | 5+ custom fields = 1.0; <3 = 0.5                   |  
| D04 | Branding guideline compliance | 0.10 | 100% compliant = 1.0; 1 error = 0.7                |  
| D05 | Performance metrics        | 0.10   | Latency < 200ms = 1.0; >500ms = 0.3                |  
| D06 | Error handling             | 0.10   | 100% covered = 1.0; 50% covered = 0.5              |  
| D07 | Documentation quality      | 0.10   | Complete = 1.0; partial = 0.6                      |  
| D08 | User experience            | 0.10   | 5+ UX checks passed = 1.0; <3 = 0.4                |  

## Actions  
| Score   | Action                          |  
|---------|---------------------------------|  
| ≥9.5    | GOLDEN: Auto-approve            |  
| ≥8.0    | PUBLISH: Deploy with review     |  
| ≥7.0    | REVIEW: Manual QA required      |  
| <7.0    | REJECT: Fix and resubmit        |  

## Bypass  
| conditions                          | approver | audit trail         |  
|-----------------------------------|----------|---------------------|  
| Urgent deployment with CTO approval | CTO      | Ticket #WL-XXXX     |
