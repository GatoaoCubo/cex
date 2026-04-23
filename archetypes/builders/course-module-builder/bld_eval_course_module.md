---
kind: quality_gate
id: p05_qg_course_module
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for course_module
quality: 9.1
title: "Quality Gate Course Module"
version: "1.0.0"
author: n03_builder
tags: [course_module, builder, quality_gate]
tldr: "Artifact-level quality gate: validates course_module structure, Bloom-alignment, assessment coverage, and accessibility (not learner runtime metrics)."
domain: "course_module construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_examples_course_module
  - bld_schema_course_module
  - bld_memory_course_module
  - p03_sp_course_module_builder
  - bld_knowledge_card_course_module
  - bld_instruction_course_module
  - course-module-builder
  - p05_kc_course_module
  - p11_qg_audit_log
  - p11_qg_ab_test_config
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| schema_fields_present | 100% | == | frontmatter |
| outcome_assessment_coverage | 100% | == | learning_outcomes |
| score_minimum | 8.0 | >= | artifact |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Missing or malformed YAML |
| H02 | ID matches `^p05_cm_[a-z][a-z0-9_]+\.md$` | ID does not conform |
| H03 | `kind` field == `course_module` | kind is wrong or missing |
| H04 | `learning_outcomes` non-empty AND every item starts with a Bloom verb | Verb absent or generic ("know", "learn", "understand" unqualified) |
| H05 | `bloom_levels` subset of {Remember, Understand, Apply, Analyze, Evaluate, Create} | Invalid level label |
| H06 | `assessment_items` non-empty; every item has `outcome_ref` matching a learning_outcome id | Missing coverage |
| H07 | Every `assessment_items[i].bloom_level` == its referenced outcome's bloom_level | Objective-assessment drift |
| H08 | `duration_minutes` present and > 0 | Missing or non-positive |
| H09 | `prerequisites[]` entries are course_module IDs (pattern `^p05_cm_`) or empty list | Free-text prerequisite |
| H10 | `quality: null` in frontmatter | Self-scored (must be null) |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | Outcome measurability | 0.15 | 1.0: Bloom verb + measurable artifact; 0.5: verb only; 0.0: aspirational |
| D2 | Assessment alignment | 0.15 | 1.0: 1:1 outcome->assessment, same Bloom level; 0.5: coverage with drift; 0.0: divergent |
| D3 | Cognitive load fit | 0.10 | 1.0: <= 4 new concepts per 10 min; 0.5: 5-6; 0.0: overload |
| D4 | Micro-learning chunking | 0.10 | 1.0: 5-10 min chunks with formative checks; 0.5: 15-20 min; 0.0: lecture-length |
| D5 | Accessibility (WCAG 2.2) | 0.12 | 1.0: AA confirmed + captions + alt-text; 0.5: partial; 0.0: unaddressed |
| D6 | Kirkpatrick measurement | 0.10 | 1.0: L1-L2 + L3/L4 plan; 0.5: L1-L2 only; 0.0: no evaluation plan |
| D7 | Interoperability | 0.08 | 1.0: SCORM 2004 or xAPI emission; 0.5: declares but no wrapper; 0.0: platform-locked |
| D8 | Prerequisite rigor | 0.08 | 1.0: module IDs + rationale; 0.5: IDs only; 0.0: free-text |
| D9 | Content diversity | 0.07 | 1.0: >= 3 formats (text+video+interactive); 0.5: 2 formats; 0.0: single format |
| D10 | Equity & inclusion | 0.05 | 1.0: diverse examples + inclusive language; 0.0: exclusionary framing |

Weights sum = 1.00.

## Actions
| Score | Action |
|---|---|
| >= 9.5 | GOLDEN: approve for publication |
| >= 8.0 | PUBLISH: ship to LMS |
| >= 7.0 | REVIEW: return to instructional designer |
| < 7.0 | REJECT: rebuild -- outcome/assessment misalignment |

## Bypass
| condition | approver | audit trail |
|---|---|---|
| Compliance-required content with fixed outline | Chief Learning Officer | Decision record required |
| Legacy module migration (SCORM 1.2 import) | Head of Learning Engineering | Migration plan attached |

## Examples

## Golden Example
---
title: "Introduction to Data Science"
vendor: "edX"
version: "2.1"
type: course_module
---
**Learning Objectives**
- Understand fundamental statistical concepts
- Apply Python for data analysis
- Interpret machine learning model outputs

**Content**
Week 1: Statistics basics (mean, median, variance)
Week 2: Python libraries (Pandas, NumPy)
Week 3: Supervised learning algorithms

**Assessments**
- Weekly quizzes via [Quizizz](https://quizizz.com)
- Final project: Analyze a public dataset using Jupyter Notebooks
- Peer reviews on [Moodle](https://moodle.org)

**References**
- "Python for Data Analysis" by Wes McKinney
- edX course materials

## Anti-Example 1: Missing Core Elements
---
title: "Quick Python Guide"
vendor: "Udemy"
version: "1.0"
type: course_module
---
**Content**
- Basics of syntax
- Loops and functions

**Assessments**
- No assessments listed

## Why it fails
Lacks learning objectives and assessments, making the module incomplete and unmeasurable.

## Anti-Example 2: Boundary Violation
---
title: "Prompt Engineering Basics"
vendor: "Coursera"
version: "0.5"
type: course_module
---
**Learning Objectives**
- Create effective prompts for AI models

**Content**
- Prompt templates for different tasks
- Example: "Act as a {role} and {task}"

**Assessments**
- Self-assessment checklist

## Why it fails
Includes prompt templates, which are explicitly excluded from the course_module boundary.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
