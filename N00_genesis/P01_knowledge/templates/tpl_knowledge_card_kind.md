---
# TEMPLATE: Kind Knowledge Card (P01 Knowledge — per-kind deep injection)
# 1 per kind. Primary F3 INJECT source. Optimized for LLM consumption.
# Valide contra P01_knowledge/_schema.yaml (types.knowledge_card, body_structure.kind_kc)
# Max 5120 bytes | density_min: 0.85 | quality_min: 8.0

id: p01_kc_{{KIND_SLUG}}
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P01
title: "{{KIND_TITLE}} — Deep Knowledge for {{KIND_SLUG}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AUTHOR}}
domain: {{KIND_SLUG}}
quality: 9.1
tags: [{{KIND_SLUG}}, {{PILLAR_CODE}}, {{LLM_FUNCTION}}, kind-kc]
tldr: "{{ONE_DENSE_SENTENCE_ABOUT_THIS_KIND}}"
when_to_use: "Building, reviewing, or reasoning about {{KIND_SLUG}} artifacts"
keywords: [{{KEYWORD_1}}, {{KEYWORD_2}}, {{KEYWORD_3}}]
feeds_kinds: [{{KIND_SLUG}}]
density_score: null
---

# {{KIND_TITLE}}

## Spec
```yaml
kind: {{KIND_SLUG}}
pillar: {{PILLAR_CODE}}
llm_function: {{LLM_FUNCTION}}
max_bytes: {{MAX_BYTES}}
naming: {{NAMING_PATTERN}}
core: {{true|false}}
```

## What It Is
{{2-3 sentences: what this kind represents, its atomic boundary, what it is NOT.}}

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | {{CLASS_OR_NA}} | {{HOW_IT_MAPS}} |
| LlamaIndex | {{CLASS_OR_NA}} | {{HOW_IT_MAPS}} |
| CrewAI | {{CLASS_OR_NA}} | {{HOW_IT_MAPS}} |
| DSPy | {{CLASS_OR_NA}} | {{HOW_IT_MAPS}} |
| Haystack | {{CLASS_OR_NA}} | {{HOW_IT_MAPS}} |
| OpenAI | {{CLASS_OR_NA}} | {{HOW_IT_MAPS}} |
| Anthropic | {{CLASS_OR_NA}} | {{HOW_IT_MAPS}} |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| {{PARAM_1}} | {{TYPE}} | {{DEFAULT}} | {{HIGHER_VS_LOWER}} |
| {{PARAM_2}} | {{TYPE}} | {{DEFAULT}} | {{HIGHER_VS_LOWER}} |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| {{PATTERN_1}} | {{TRIGGER}} | {{CONCRETE_EXAMPLE}} |
| {{PATTERN_2}} | {{TRIGGER}} | {{CONCRETE_EXAMPLE}} |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| {{ANTI_1}} | {{ROOT_CAUSE}} | {{CORRECTION}} |
| {{ANTI_2}} | {{ROOT_CAUSE}} | {{CORRECTION}} |

## Integration Graph
```
{{INPUT_KINDS}} --> [{{KIND_SLUG}}] --> {{OUTPUT_KINDS}}
                         |
                    {{RELATED_KINDS}}
```

## Decision Tree
- IF {{CONDITION_1}} THEN {{VARIANT_A}}
- IF {{CONDITION_2}} THEN {{VARIANT_B}}
- DEFAULT: {{SAFE_DEFAULT}}

## Quality Criteria
- GOOD: {{WHAT_MAKES_A_GOOD_INSTANCE}}
- GREAT: {{WHAT_MAKES_AN_EXCELLENT_INSTANCE}}
- FAIL: {{WHAT_MAKES_IT_REJECTED}}
