---
kind: examples
id: bld_examples_preference_dataset
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of preference_dataset artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: null
title: "Examples Preference Dataset"
version: "1.0.0"
author: n03_builder
tags: [preference_dataset, builder, examples]
tldr: "Golden and anti-examples for preference_dataset construction."
domain: "preference dataset construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

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
