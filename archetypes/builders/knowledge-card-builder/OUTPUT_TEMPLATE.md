---
lp: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a knowledge_card
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: knowledge_card

## domain_kc variant (subject-matter knowledge)
```yaml
---
id: p01_kc_{{topic_slug}}
type: knowledge_card
lp: P01
title: "{{Knowledge Card Title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{satellite_name}}"
domain: "{{domain_name}}"
quality: null
tags: [{{tag1}}, {{tag2}}, {{tag3}}]
tldr: "{{one_dense_sentence_under_160_chars}}"
when_to_use: "{{when_this_card_should_be_retrieved}}"
keywords: [{{keyword1}}, {{keyword2}}, {{keyword3}}]
long_tails:
  - "{{natural_language_query_1}}"
  - "{{natural_language_query_2}}"
axioms:
  - "{{SEMPRE_or_NUNCA_actionable_rule}}"
linked_artifacts:
  primary: {{p0X_type_name_OR_null}}
  related: [{{p0X_type_name_OR_null}}]
density_score: {{0.80_to_1.00}}
data_source: "{{source_url_or_description}}"
---

# {{Knowledge Card Title}}

## Quick Reference
```yaml
topic: {{topic_name}}
scope: {{scope}}
owner: {{owner}}
criticality: {{low|medium|high}}
```

## Key Concepts
- {{concept_1_concise_max_80_chars}}
- {{concept_2_concise_max_80_chars}}
- {{concept_3_concise_max_80_chars}}

## Strategy Phases
1. {{phase_1_with_outcome}}
2. {{phase_2_with_outcome}}
3. {{phase_3_with_outcome}}

## Golden Rules
- {{SEMPRE_or_NUNCA_rule_1}}
- {{SEMPRE_or_NUNCA_rule_2}}
- {{SEMPRE_or_NUNCA_rule_3}}

## Flow
```text
[{{input}}] -> [{{process_1}}] -> [{{process_2}}] -> [{{output}}]
```

## Comparativo
| Abordagem | Vantagem | Desvantagem |
|-----------|----------|-------------|
| {{approach_1}} | {{pro}} | {{con}} |
| {{approach_2}} | {{pro}} | {{con}} |

## References
- {{source_url_or_artifact_ref}}
```

## meta_kc variant (system/spec knowledge)
```yaml
# Same frontmatter as above, then body:

# {{Knowledge Card Title}}

## Executive Summary
- {{key_fact_1}}
- {{key_fact_2}}
- {{key_fact_3}}

## Spec Table
| Spec | Value | Notes |
|------|-------|-------|
| {{field}} | {{value}} | {{note}} |

## Patterns
- {{confirmed_pattern_1}}
- {{confirmed_pattern_2}}

## Anti-Patterns
- {{anti_pattern_1_with_consequence}}

## Application
1. {{how_to_apply_step_1}}
2. {{how_to_apply_step_2}}

## References
- {{source_url_or_artifact_ref}}
```
