---
# TEMPLATE: Knowledge Card (P01 Knowledge)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P01_knowledge/_schema.yaml (types.knowledge_card)
# Max 5120 bytes | density_min: 0.80 | quality_min: 7.0

id: p01_kc_{{TOPIC_SLUG}}
kind: knowledge_card
pillar: P01
title: "{{KNOWLEDGE_CARD_TITLE}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
domain: {{DOMAIN_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, knowledge]
tldr: "{{ONE_DENSE_SENTENCE}}"
when_to_use: "{{WHEN_THIS_CARD_SHOULD_BE_RETRIEVED}}"
keywords: [{{KEYWORD_1}}, {{KEYWORD_2}}, {{KEYWORD_3}}]
long_tails: [{{LONG_TAIL_QUERY_1}}, {{LONG_TAIL_QUERY_2}}]
axioms: [{{AXIOM_1}}]
linked_artifacts:
  adw: {{p12_wf_name_OR_null}}
  agent: {{p02_agent_name_OR_null}}
  hop: {{p03_pt_name_OR_null}}
density_score: {{0.80_TO_1.00}}
---

# Knowledge Card: {{KNOWLEDGE_CARD_TITLE}}

## Quick Reference
```yaml
topic: {{TOPIC_NAME}}
scope: {{SCOPE}}
owner: {{OWNER}}
criticality: {{low|medium|high}}
```

## Key Concepts
- {{CONCEPT_1_WITH_EXAMPLE}}
- {{CONCEPT_2_WITH_EXAMPLE}}
- {{CONCEPT_3_WITH_EXAMPLE}}

## Strategy Phases
1. {{PHASE_1_WITH_OUTCOME}}
2. {{PHASE_2_WITH_OUTCOME}}
3. {{PHASE_3_WITH_OUTCOME}}

## Golden Rules
- {{RULE_1}}
- {{RULE_2}}
- {{RULE_3}}

## Flow
```text
[{{INPUT}}] -> [{{ANALYZE}}] -> [{{DECIDE}}] -> [{{EXECUTE}}] -> [{{LEARN}}]
```

## References
- Related artifact: {{ARTIFACT_REF_1}}
- Related artifact: {{ARTIFACT_REF_2}}
