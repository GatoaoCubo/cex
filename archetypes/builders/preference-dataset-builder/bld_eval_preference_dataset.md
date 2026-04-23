---
kind: quality_gate
id: p11_qg_preference_dataset
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of preference_dataset artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 8.8
title: "Gate: preference_dataset"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, preference-dataset, P11, rlhf, dpo]
tldr: "Pass/fail gate for preference_dataset: signal clarity, agreement_rate, rater_count, pair presence, training_objective."
domain: "preference_dataset -- curated preference pairs for RLHF/DPO/KTO alignment training"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - p11_qg_chunk_strategy
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - p11_qg_constraint_spec
  - p11_qg_function_def
  - p11_qg_handoff_protocol
  - p11_qg_output_validator
  - p11_qg_prompt_version
  - p11_qg_eval_dataset
  - p11_qg_effort_profile
---

## Quality Gate

# Gate: preference_dataset

## Definition
| Field | Value |
|---|---|
| metric | preference_dataset artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: preference_dataset` |

## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p11_pd_[a-z][a-z0-9_]+$` | ID has hyphens, uppercase, or missing prefix |
| H03 | training_objective is valid enum value | "better_training" or unrecognized value |
| H04 | Kind equals literal `preference_dataset` | `kind: dataset` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing preference_signal, annotation_method, rater_count, agreement_rate |
| H07 | preference_signal is non-empty string | `preference_signal: ""` or absent |
| H08 | agreement_rate in [0.0, 1.0] | `agreement_rate: 1.5` or negative value |
| H09 | Tags list has >= 3 items and includes "preference_dataset" | Only 2 tags or missing tag |
| H10 | pairs array present with >= 1 entry | Empty pairs or missing pairs key |

## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Signal clarity | 1.5 | preference_signal is specific, measurable criterion (not "better") |
| Agreement quality | 1.5 | agreement_rate >= 0.75; rater_count >= 2 |
| Annotation provenance | 1.0 | annotation_method declared and appropriate for domain |
| Pair schema compliance | 1.0 | Example pairs use prompt/chosen/rejected/metadata structure |
| Quality filter specification | 1.0 | quality_filters section with concrete thresholds |
| Split ratios | 0.5 | train/eval/test ratios declared and sum to 1.0 |
| Domain specificity | 0.5 | domain field set; task_type identifiable |
| Boundary clarity | 1.0 | Not eval_dataset (no evaluation metrics), not golden_test (no deterministic outputs) |
| tldr quality | 0.5 | <= 160 chars, includes objective and domain |

## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish as reference dataset spec |
| >= 8.0 | Publish | Ready for training pipeline config |
| >= 7.0 | Review | Improve signal clarity or add quality filters |
| < 7.0 | Reject | Return with specific gate failures |

## Never Bypass
- H01 (unparseable YAML breaks tooling)
- H05 (self-scored artifacts corrupt quality metrics)
- H07 (vague signal makes dataset unusable for training)

## Examples

# Examples: preference-dataset-builder

## Golden Example
INPUT: "Create preference dataset for instruction-following DPO training, human-rated, CEX nucleus tasks"
OUTPUT:
```yaml
id: p11_pd_cex_instruction_dpo
kind: preference_dataset
pillar: P11
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
training_objective: dpo
preference_signal: "Response follows all stated constraints and produces correct artifact with proper frontmatter"
annotation_method: human
rater_count: 3
agreement_rate: 0.85
domain: "instruction-following"
language: "en"
total_pairs: 500
split_ratios:
  train: 0.80
  eval: 0.10
  test: 0.10
source: "CEX nucleus task logs, human annotation by N07 team"
quality: null
tags: [preference_dataset, instruction_following, dpo, P11]
tldr: "500 DPO pairs for CEX instruction-following: chosen=correct artifact+frontmatter, rejected=incomplete/malformed response."
```
## Overview
DPO training dataset for CEX nucleus instruction-following tasks. Pairs drawn from real nucleus task logs, annotated by 3 raters with 85% agreement threshold.

## Annotation Protocol
Chosen when response: produces complete artifact with valid frontmatter, follows 8F pipeline, includes required sections.
Rejected when response: omits frontmatter, misses required sections, contradicts instructions.

| Chosen When | Rejected When |
|-------------|--------------|
| Complete frontmatter with all required fields | Missing or malformed frontmatter |
| All required sections present | Truncated output missing sections |
| Follows 8F pipeline trace | No 8F trace shown |

## Quality Filters
| Filter | Threshold | Action |
|--------|-----------|--------|
| agreement_rate | >= 0.85 | Exclude pairs with < 3 rater agreement |
| confidence | >= 0.80 | Flag and review borderline pairs |

## Pairs (excerpt)
```yaml
pairs:
  - id: "cex_dpo_001"
    prompt: "Build a knowledge_card for RAG chunking strategies"
    chosen: "---\nid: p01_kc_rag_chunking\nkind: knowledge_card\npillar: P01\nquality: null\n---\n## Overview\n..."
    rejected: "Here is a knowledge card about RAG chunking: RAG uses chunks to..."
    metadata:
      rater_count: 3
      agreement: 0.92
      confidence: 0.90
      tags: [instruction_following, frontmatter, knowledge_card]
```

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches `^p11_pd_` pattern (H02 pass)
- kind: preference_dataset (H04 pass)
- preference_signal declared (H06 pass)
- agreement_rate: 0.85 (H07 pass)
- rater_count: 3 (H08 pass)
- pairs array present with example (H09 pass)
- training_objective: dpo (H03 pass)

## Anti-Example
INPUT: "Create preference dataset for my chatbot"
BAD OUTPUT:
```yaml
id: my-chatbot-prefs
kind: preferences
quality: 9.2
signal: "better"
pairs:
  - good: "Hello! How can I help?"
    bad: "Hi"
```
FAILURES:
1. id: "my-chatbot-prefs" has hyphens and no `p11_pd_` prefix -> H02 FAIL
2. kind: "preferences" not "preference_dataset" -> H04 FAIL
3. quality: 9.2 (not null) -> H05 FAIL
4. preference_signal: "better" is too vague -> H06 SOFT FAIL
5. Missing required fields: training_objective, annotation_method, rater_count, agreement_rate -> H06 FAIL
6. Pairs use wrong schema: "good/bad" not "chosen/rejected" -> structure FAIL
7. No frontmatter pillar, version, created, updated, author, tags, tldr -> H06 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
