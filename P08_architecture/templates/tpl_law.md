---
# TEMPLATE: Law (P08 Architecture)
# Valide contra P08_architecture/_schema.yaml (types.law)
# Max 3072 bytes

id: p08_law_{{NUMBER}}
kind: law
pillar: P08
title: "LAW {{NUMBER}}: {{LAW_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# LAW {{NUMBER}}: {{LAW_NAME}}

## Statement
{{ONE_IMMUTABLE_OPERATIONAL_RULE}}

## Why It Exists
- Context: {{WHAT_PROBLEM_THIS_PREVENTS}}
- Risk: {{WHAT_BREAKS_IF_IGNORED}}

## Enforcement
1. {{ENFORCEMENT_MECHANISM_1}}
2. {{ENFORCEMENT_MECHANISM_2}}
3. {{ENFORCEMENT_MECHANISM_3}}

## Exceptions
- Allowed only when: {{STRICT_EXCEPTION_RULE}}
