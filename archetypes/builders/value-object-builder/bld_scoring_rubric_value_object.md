---
id: bld_scoring_rubric_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Scoring Rubric"
version: 1.0.0
quality: null
tags: [builder, value_object, scoring]
llm_function: GOVERN
---
# Scoring Rubric: value_object
## 5D Dimensions
| Dim | Name | Weight | Description |
|-----|------|--------|-------------|
| D1 | Attribute Quality | 0.30 | Are attributes typed with precise constraints? |
| D2 | Immutability Guarantee | 0.25 | Are transformations side-effect-free (return new instances)? |
| D3 | Equality Contract | 0.15 | Is structural equality explicitly defined? |
| D4 | Validation Coverage | 0.20 | Are invalid state examples concrete and complete? |
| D5 | Domain Fit | 0.10 | Does this concept truly have no identity (not an entity)? |
## D1 Scoring Guide: Attribute Quality
| Score | Criteria |
|-------|----------|
| 1.0 | All attributes: typed, constrained, with valid and invalid examples |
| 0.7 | All typed, some constraints missing |
| 0.3 | Types present, no constraints |
| 0.0 | Attributes unnamed or untyped |
## D2 Scoring Guide: Immutability Guarantee
| Score | Criteria |
|-------|----------|
| 1.0 | All transformations explicitly return new instances, no mutators |
| 0.5 | Transformations present but mutation possible (ambiguous) |
| 0.0 | Setter methods or mutation implied |
