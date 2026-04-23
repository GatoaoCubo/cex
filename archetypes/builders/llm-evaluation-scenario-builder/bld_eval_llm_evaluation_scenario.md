---
kind: quality_gate
id: p07_qg_llm_evaluation_scenario
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for llm_evaluation_scenario
quality: 9.0
title: "Quality Gate LLM Evaluation Scenario"
version: "1.0.0"
author: n06_wave7
tags: [llm_evaluation_scenario, builder, quality_gate, helm]
tldr: "Quality gate with HARD and SOFT scoring for llm_evaluation_scenario"
domain: "llm_evaluation_scenario construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_llm_evaluation_scenario
  - p03_sp_llm_evaluation_scenario_builder
  - bld_instruction_llm_evaluation_scenario
  - bld_schema_llm_evaluation_scenario
  - bld_output_template_llm_evaluation_scenario
  - bld_knowledge_card_llm_evaluation_scenario
  - llm-evaluation-scenario-builder
  - p10_lr_llm_evaluation_scenario_builder
  - p11_qg_audit_log
  - p08_qg_fhir_agent_capability
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Scenario reproducibility | 100% | equals | All HELM-compatible runners |

## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern `^p07_evs_[a-z][a-z0-9_]+\.md$` | Pattern mismatch |
| H03 | kind = "llm_evaluation_scenario" | Kind field incorrect or absent |
| H04 | subject_area in HELM taxonomy | Unrecognized or missing subject_area |
| H05 | capability is specific and falsifiable | Vague or missing capability description |
| H06 | task_format is homogeneous | Mixed MCQ + open-ended in same scenario |
| H07 | primary_metric maps to HELM family | Unknown or missing metric |
| H08 | canonicalization_fn referenced by name | Inline code or missing canonicalization |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Schema completeness (all required + recommended fields) | 0.25 | All present = 1.0, missing recommended = 0.7, missing required = 0 |
| D02 | Subject-area depth (IBM extension domains vs. generic) | 0.20 | Domain-specific with IBM extension = 1.0, standard HELM only = 0.7, vague = 0.3 |
| D03 | Adapter precision (concrete param values, prompt_template ref) | 0.20 | All concrete = 1.0, partial = 0.5, missing = 0 |
| D04 | Few-shot pool quality (size >= num_few_shot, diverse examples) | 0.15 | Sufficient + diverse = 1.0, sufficient only = 0.7, insufficient = 0 |
| D05 | Token cost estimate accuracy (within 20% of actual) | 0.20 | Documented + accurate = 1.0, documented only = 0.5, missing = 0 |

## Actions
| Label | Score | Action |
|-------|-------|--------|
| GOLDEN  | >= 9.5 | Auto-publish to HELM scenario registry |
| PUBLISH | >= 8.0 | Publish after peer validation |
| REVIEW  | >= 7.0 | Manual review required |
| REJECT  | < 7.0  | Return to builder with failure report |

## Bypass
| Condition | Approver | Audit Trail |
|-----------|----------|-------------|
| IBM Enterprise extension pilot | Head of Evaluation | Escalation log in N05_operations/ |

## Examples

## Golden Example

```markdown
---
id: p07_evs_medical_clinical_mcq.md
kind: llm_evaluation_scenario
pillar: P07
subject_area: knowledge
capability: clinical_diagnosis_mcq
task_format: mcq
primary_metric: exact_match
num_instances: 1089
num_few_shot: 5
adapter_ref: p03_pt_helm_mcq_standard.md
dataset_source: "MedQA-USMLE (MIT License)"
canonicalization_fn: "helm_normalize_mcq_letter"
token_cost_estimate: "~2.1M tokens for 1089 instances at 5-shot"
quality: null
---

## Scenario Overview
**Subject Area**: knowledge (HELM taxonomy)
**Capability Tested**: Clinical diagnosis from patient vignettes (USMLE Step 1-3 style)

| Field | Value |
|-------|-------|
| HELM Taxonomy | knowledge > medicine |
| IBM Extension | N/A |
| Upstream Dataset | MedQA-USMLE |
| License | MIT |

## Adapter Configuration
| Parameter | Value |
|-----------|-------|
| num_train_trials | 1 |
| num_test_instances | 1089 |
| max_tokens | 5 |
| temperature | 0.0 |
| stop_sequences | ["\n"] |

## Canonicalization Rules
1. Strip leading/trailing whitespace from model output.
2. Extract first letter character (A-E) from output string.
3. Uppercase extracted letter for comparison.

**Normalization Function**: `helm_normalize_mcq_letter`
```

## Anti-Example 1: Mixed Task Format

```markdown
---
id: p07_evs_reasoning_general.md
subject_area: reasoning
capability: general_reasoning
task_format: mixed  <!-- INVALID -->
primary_metric: accuracy
---
Some tasks are MCQ, others require a 3-sentence explanation.
```

**Why it fails**: Mixed task formats violate H06. Canonicalization becomes impossible -- MCQ needs letter extraction while open-ended needs ROUGE scoring. Single scenarios must be homogeneous.

## Anti-Example 2: Vague Capability

```markdown
---
id: p07_evs_knowledge_intelligence.md
subject_area: knowledge
capability: intelligence  <!-- INVALID: not falsifiable -->
task_format: open_ended
primary_metric: bleu
---
Tests how "intelligent" the model is at answering questions.
```

**Why it fails**: "Intelligence" is not a falsifiable cognitive function (H05). A valid capability must be specific: "factual_recall_world_events_2020_2024" or "multi_step_math_word_problems".

## Anti-Example 3: Missing Canonicalization

```markdown
---
id: p07_evs_code_python_generation.md
subject_area: code
capability: python_function_generation
task_format: generation
primary_metric: pass_at_k
---
Model generates Python functions. We check if they pass unit tests.
```

**Why it fails**: Missing canonicalization_fn (H08). Code evaluation requires explicit normalization: strip markdown code fences, normalize whitespace, specify execution sandbox. Without it, metric computation is nondeterministic across runners.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
