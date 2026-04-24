---
# TEMPLATE: Golden Test
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P07_evals/_schema.yaml (types.golden_test)
# Max 2KB | density_min: 0.85 | quality_min: 9.5

id: p07_gt_{{CASE_SLUG}}
kind: golden_test
8f: F7_govern
pillar: P07
title: "Golden Test: {{REFERENCE_CASE_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
target: {{p02_ag_name|p03_pt_name|p04_sk_name}}
quality: {{QUALITY_9.5_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, golden, reference]
tldr: "{{ONE_SENTENCE_WHY_THIS_IS_GOLDEN}}"
source: {{FILE_PATH_OF_ORIGINAL}}
density_score: {{0.85_TO_1.00}}
linked_artifacts:
  target: {{ARTIFACT_ID}}
  eval: {{p07_ue_name_OR_null}}
---

# Golden Test: {{REFERENCE_CASE_NAME}}

## Why Golden

{{2_3_SENTENCES_WHY_THIS_EXEMPLIFIES_QUALITY_9.5}}

## Reference Input

```{{FORMAT}}
{{THE_EXACT_INPUT_THAT_PRODUCED_GOLDEN_OUTPUT}}
```

## Golden Output

```{{FORMAT}}
{{THE_EXACT_OUTPUT_SCORED_9.5_PLUS}}
```

## Quality Dimensions

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Completeness | {{9.0_TO_10}} | {{WHY_COMPLETE}} |
| Accuracy | {{9.0_TO_10}} | {{WHY_ACCURATE}} |
| Density | {{9.0_TO_10}} | {{WHY_DENSE}} |
| Actionability | {{9.0_TO_10}} | {{WHY_ACTIONABLE}} |
| Structure | {{9.0_TO_10}} | {{WHY_WELL_STRUCTURED}} |

## Assertions (for regression testing)

| # | Type | Expression |
|---|------|------------|
| 1 | contains | `{{KEY_PHRASE_THAT_MUST_EXIST}}` |
| 2 | contains | `{{KEY_PHRASE_THAT_MUST_EXIST}}` |
| 3 | score_gte | `quality >= 9.5` |
| 4 | {{regex|exact|contains}} | `{{ADDITIONAL_ASSERTION}}` |

## Derivation

- Source: `{{PATH_TO_ORIGINAL_IN_organization_CORE}}`
- Original score: {{ORIGINAL_QUALITY_SCORE}}
- Migrated: {{ISO_DATE}}
- Adapted: {{WHAT_CHANGED_DURING_MIGRATION_OR_none}}
