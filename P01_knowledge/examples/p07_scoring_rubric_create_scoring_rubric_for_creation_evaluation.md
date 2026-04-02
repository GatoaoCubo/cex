---
id: p07_sr_creation_eval
kind: scoring_rubric
pillar: P07
title: "Rubric: Creation Evaluation"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "scoring-rubric-builder"
framework: "5D Creation"
target_kinds: [agent, prompt_template, knowledge_card, workflow, system_prompt]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "creation"
quality: 9.1
tags: [scoring-rubric, creation, evaluation, 5d]
tldr: "5-dimension rubric for creation tasks: correctness 30%, completeness 25%, clarity 20%, originality 15%, usability 10%"
density_score: 0.88
calibration_set: []
inter_rater_agreement: 0.82
appeals_process: "Submit to N07 orchestrator with rationale and evidence for re-evaluation"
linked_artifacts:
  primary: "quality-gate-builder"
  related: [p11_qg_creation, p07_gt_creation_examples]
---
## Framework Overview
5D Creation evaluates newly generated artifacts across 5 orthogonal quality dimensions. Designed for creation tasks where technical accuracy, structural completeness, and user value must be balanced. Applies to agents, prompts, workflows, knowledge cards, and system prompts produced by builders or humans.

## Dimensions
| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Correctness | 30% | 0-10 | Technical accuracy, no factual errors, valid syntax | Zero errors, all facts verified, perfect syntax | 1-2 minor errors, mostly accurate, valid structure |
| Completeness | 25% | 0-10 | All required sections present, adequate detail level | All frontmatter fields, all body sections, rich detail | Most sections present, some missing fields, adequate detail |
| Clarity | 20% | 0-10 | Well-organized structure, readable prose, logical flow | Perfect structure, clear prose, intuitive navigation | Good organization, readable text, minor flow issues |
| Originality | 15% | 0-10 | Novel insights, creative approach, unique value-add | Innovative approach, new patterns, significant novelty | Some new elements, partially creative, modest innovation |
| Usability | 10% | 0-10 | Target audience can apply immediately, actionable | Ready-to-use, zero learning curve, immediate value | Mostly usable, minor setup needed, clear value |

## Thresholds
| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Promote to exemplar set, use as reference template |
| PUBLISH | >= 8.0 | Merge to production pool, deploy immediately |
| REVIEW | >= 7.0 | Return with dimension-specific feedback for improvement |
| REJECT | < 7.0 | Rebuild from requirements with fresh research |

## Calibration
- **GOLDEN (9.7)**: agent with perfect frontmatter, comprehensive capabilities, novel architecture, production-ready
- **PUBLISH (8.2)**: prompt_template with complete sections, clear instructions, good examples, minor polish needed
- **REVIEW (7.3)**: knowledge_card with most sections, some gaps in references, adequate but improvable
- **REJECT (5.8)**: workflow with structural issues, missing steps, unclear purpose, requires major revision

## Automation
| Dimension | Status | Tool |
|-----------|--------|------|
| Correctness | semi-automated | Schema validation + manual fact-check |
| Completeness | automated | Section counting + required field validation |
| Clarity | manual | Human review for readability and structure |
| Originality | manual | Human assessment vs existing artifact pool |
| Usability | semi-automated | Template validation + manual user journey review |

## References
- CEX 8F Pipeline validation framework
- AAC&U VALUE Rubrics for Creative Thinking
- Schema validation tools: cex_compile.py, cex_doctor.py