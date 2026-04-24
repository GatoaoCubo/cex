---
# TEMPLATE: Context Doc (P01 Knowledge)
# Valide contra P01_knowledge/_schema.yaml (types.context_doc)
# Max 2048 bytes

id: p01_ctx_{{TOPIC_SLUG}}
kind: context_doc
8f: F3_inject
pillar: P01
title: "{{CONTEXT_TITLE}}"
domain: {{DOMAIN_NAME}}
scope: {{SYSTEM|CLIENT|WORKFLOW|REPO}}
quality: {{QUALITY_7_TO_10}}
---

# Context Doc: {{CONTEXT_TITLE}}

## Scope
- Domain: {{DOMAIN_NAME}}
- Boundary: {{WHAT_IS_INCLUDED}}
- Excluded: {{WHAT_IS_OUT_OF_SCOPE}}

## Current State
- {{FACT_1}}
- {{FACT_2}}
- {{FACT_3}}

## Operational Context
| Area | Detail |
|------|--------|
| Users | {{PRIMARY_USERS}} |
| Inputs | {{PRIMARY_INPUTS}} |
| Outputs | {{PRIMARY_OUTPUTS}} |
| Risks | {{MAIN_RISK}} |

## Decision Notes
1. {{DECISION_1}}
2. {{DECISION_2}}
3. {{DECISION_3}}
