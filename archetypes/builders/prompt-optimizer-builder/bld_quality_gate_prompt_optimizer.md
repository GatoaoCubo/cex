---
kind: quality_gate
id: p03_qg_prompt_optimizer
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for prompt_optimizer
quality: 9.1
title: "Quality Gate Prompt Optimizer"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_optimizer, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for prompt_optimizer"
domain: "prompt_optimizer construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
(Table: metric, threshold, operator, scope)
| metric              | threshold | operator | scope           |
|---------------------|-----------|----------|-----------------|
| optimization_passes | 2         | >=       | each artifact   |
| industry_refs       | 1         | >=       | each artifact   |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID           | Check                                   | Fail Condition                                      |
|--------------|-----------------------------------------|-----------------------------------------------------|
| H01          | YAML frontmatter valid                  | Invalid YAML syntax or missing fields               |
| H02          | ID matches ^p03_po_[a-z][a-z0-9_]+.md$ | ID does not conform to schema pattern               |
| H03          | kind field = 'prompt_optimizer'         | kind field is incorrect or missing                  |
| H04          | At least 2 optimization passes defined  | No documented optimization steps                    |
| H05          | Input prompt and output prompt present  | Missing before/after comparison                     |
| H06          | Rationale documented for each pass      | No explanation of why each change improves quality  |
| H07          | At least 1 industry method cited        | No reference to DSPy, OPRO, APE, or PromptWizard    |

## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide)
| Dim | Dimension         | Weight | Scoring Guide                                            |
|-----|-------------------|--------|----------------------------------------------------------|
| D1  | Clarity gain      | 0.20   | 1.0: Unambiguous after optimization; 0.5: Minor gains    |
| D2  | Specificity       | 0.20   | 1.0: Task-specific, concrete; 0.5: Generic language      |
| D3  | Conciseness       | 0.15   | 1.0: No redundancy; 0.5: Some waste; 0.0: Bloated        |
| D4  | Constraint align  | 0.15   | 1.0: Meets all domain rules; 0.5: Partial; 0.0: Violates |
| D5  | Rationale quality | 0.15   | 1.0: Each change justified; 0.5: Partial; 0.0: None      |
| D6  | Method rigor      | 0.10   | 1.0: Named method applied; 0.5: Ad hoc; 0.0: None        |
| D7  | Reusability       | 0.05   | 1.0: Template extractable; 0.5: Partial; 0.0: One-off    |

## Actions
(Table: Score | Action)
| Score  | Action                          |
|--------|---------------------------------|
| >=9.5  | GOLDEN                          |
| >=8.0  | PUBLISH                         |
| >=7.0  | REVIEW                          |
| <7.0   | REJECT                          |

## Bypass
(Table: conditions, approver, audit trail)
| conditions                  | approver   | audit trail                          |
|-----------------------------|------------|--------------------------------------|
| Security exception approved | N07        | Bypass logged with reason + timestamp |
| Experimental method         | N07        | Bypass logged with reason + timestamp |
