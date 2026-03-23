---
# TEMPLATE: Few-Shot Example (P01 Knowledge)
# Valide contra P01_knowledge/_schema.yaml (types.few_shot_example)
# Max 1024 bytes

id: p01_fse_{{TOPIC_SLUG}}
type: few_shot_example
lp: P01
title: "{{EXAMPLE_TITLE}}"
input: {{INPUT_SUMMARY}}
output: {{OUTPUT_SUMMARY}}
quality: {{QUALITY_7_TO_10}}
---

# Few-Shot Example: {{EXAMPLE_TITLE}}

## Input
```text
{{REALISTIC_INPUT_EXAMPLE}}
```

## Output
```text
{{REALISTIC_OUTPUT_EXAMPLE}}
```

## Why It Works
- Signal preserved: {{WHY_OUTPUT_MATCHES_INPUT}}
- Constraint honored: {{WHAT_RULE_WAS_RESPECTED}}
- Reuse hint: {{WHEN_TO_REUSE_THIS_PATTERN}}
