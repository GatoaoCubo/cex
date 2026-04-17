---
# TEMPLATE: Architecture Pattern
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P08_architecture/_schema.yaml (types.pattern)
# Max 2KB | density_min: 0.80 | quality_min: 8.0

id: p08_pat_{{NAME_SLUG}}
kind: pattern
pillar: P08
title: "Pattern: {{PATTERN_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, pattern, architecture]
tldr: "{{ONE_SENTENCE_PROBLEM_SOLUTION}}"
density_score: {{0.80_TO_1.00}}
linked_artifacts:
  law: {{p08_law_N_OR_null}}
  diagram: {{p08_diag_name_OR_null}}
---

# Pattern: {{PATTERN_NAME}}

## Problem

{{2_3_SENTENCES_DESCRIBING_THE_RECURRING_PROBLEM}}

## Context

- When: {{CONDITION_WHERE_PATTERN_APPLIES}}
- Scale: {{SINGLE_AGENT|MULTI_AGENT_GROUP|SYSTEM_WIDE}}
- Frequency: {{HOW_OFTEN_THIS_OCCURS}}

## Solution

{{3_5_SENTENCES_DESCRIBING_THE_SOLUTION_APPROACH}}

## Flow

```
[{{TRIGGER}}] --> [{{STEP_1}}] --> [{{STEP_2}}] --> [{{OUTCOME}}]
                       |                |
                  [{{GUARD}}]      [{{FALLBACK}}]
```

## Implementation

| Step | Action | Component | Notes |
|------|--------|-----------|-------|
| 1 | {{ACTION_1}} | {{COMPONENT}} | {{NOTE}} |
| 2 | {{ACTION_2}} | {{COMPONENT}} | {{NOTE}} |
| 3 | {{ACTION_3}} | {{COMPONENT}} | {{NOTE}} |

## Consequences

| Aspect | Positive | Negative |
|--------|----------|----------|
| {{ASPECT_1}} | {{BENEFIT}} | {{TRADEOFF}} |
| {{ASPECT_2}} | {{BENEFIT}} | {{TRADEOFF}} |

## Known Uses

1. {{REAL_USAGE_1_WITH_CONTEXT}}
2. {{REAL_USAGE_2_WITH_CONTEXT}}

## Anti-Pattern

{{WHAT_HAPPENS_IF_YOU_DO_THE_OPPOSITE_OR_MISAPPLY}}

## Related

- {{p08_pat_related_OR_null}}
- {{p08_law_related_OR_null}}
