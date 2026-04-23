---
kind: output_template
id: bld_output_template_knowledge_graph
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a knowledge_graph artifact
pattern: every field here exists in bld_schema_knowledge_graph.md -- template derives, never invents
quality: 9.1
title: "Output Template: knowledge_graph"
version: "1.0.0"
author: n03_builder
tags: [knowledge_graph, builder, output_template, P01]
tldr: "Fill-in template for knowledge_graph artifacts with all required frontmatter fields and 6 body sections."
domain: "knowledge graph construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_instruction_knowledge_graph
  - bld_schema_knowledge_graph
  - p01_kc_knowledge_graph
  - bld_knowledge_card_knowledge_graph
  - p11_qg_knowledge_graph
  - bld_examples_knowledge_graph
  - p03_sp_knowledge_graph_builder
  - knowledge-graph-builder
  - p10_lr_knowledge_graph_builder
  - bld_config_knowledge_graph
---

# Output Template: knowledge_graph

```yaml
id: p01_kg_{{name}}
kind: knowledge_graph
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{knowledge_domain}}"
entity_types:
  - {{EntityType1}}
  - {{EntityType2}}
  - {{EntityType3}}
relation_types:
  - {{relation_type_1}}
  - {{relation_type_2}}
  - {{relation_type_3}}
storage_backend: {{neo4j|falkordb|in_memory|json}}
traversal_strategy: {{local|global|hybrid}}
quality: null
tags: [knowledge_graph, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_domain_and_relations_covered_max_200ch}}"
max_depth: {{1-10}}
embedding_integration: {{true|false}}
dedup_strategy: {{exact|fuzzy|llm}}
community_detection: {{leiden|louvain|none}}
extraction_prompt: "{{prompt_reference_or_short_description}}"
```

## Overview
`{{what_domain_this_graph_covers_1_sentence}}`
`{{why_graph_instead_of_flat_vector_1_sentence}}`
`{{what_questions_this_graph_answers_1_sentence}}`

## Entity Types

| Name | Description | Extraction Hint | Examples |
|------|-------------|----------------|----------|
| `{{EntityType1}}` | {{what_this_entity_represents}} | {{phrase_or_pattern_in_text}} | {{ex1}}, `{{ex2}}` |
| `{{EntityType2}}` | {{what_this_entity_represents}} | {{phrase_or_pattern_in_text}} | {{ex1}}, `{{ex2}}` |
| `{{EntityType3}}` | {{what_this_entity_represents}} | {{phrase_or_pattern_in_text}} | {{ex1}}, `{{ex2}}` |

## Relation Types

| Name | Source Type | Target Type | Description | Directionality |
|------|-------------|-------------|-------------|----------------|
| `{{relation_type_1}}` | {{EntityType}} | {{EntityType}} | `{{what_relation_means}}` | directed |
| `{{relation_type_2}}` | {{EntityType}} | {{EntityType}} | `{{what_relation_means}}` | directed |
| `{{relation_type_3}}` | {{EntityType}} | {{EntityType}} | `{{what_relation_means}}` | undirected |

## Extraction Config

| Parameter | Value |
|-----------|-------|
| Method | {{llm_triplet|ner|schema_constrained|pattern}} |
| LLM model | `{{model_name}}` |
| Temperature | {{0.0-0.3}} |
| Output format | {{json_triplets|yaml_structured}} |
| Extraction prompt | `{{prompt_reference_or_inline}}` |

Extraction prompt template:
```
Extract all entities and relations from the following text.
Entity types: {{EntityType1}}, {{EntityType2}}, {{EntityType3}}
Relation types: {{relation_type_1}}, {{relation_type_2}}
Output format: JSON list of {subject, predicate, object}
Text: {text}
```

## Storage and Traversal

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Storage backend | `{{backend}}` | `{{why_this_backend}}` |
| Traversal strategy | {{local/global/hybrid}} | `{{why_this_strategy}}` |
| Max depth | `{{N}}` | `{{why_this_depth}}` |
| Query language | {{cypher|gremlin|sparql|python}} | `{{why_this_query_lang}}` |
| Pruning rule | `{{relevance_threshold_or_none}}` | `{{pruning_rationale}}` |

## Integration

| Component | Value |
|-----------|-------|
| Embedding model | `{{model_name_or_artifact_ref}}` |
| Dedup strategy | {{exact/fuzzy/llm}} |
| Dedup threshold | `{{similarity_score_0_to_1}}` |
| Community detection | {{leiden/louvain/none}} |
| Community granularity | {{fine/medium/coarse}} |
| Downstream consumers | `{{agent_or_pipeline_names}}` |

## References
- `{{reference_1}}`
- `{{reference_2}}`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_knowledge_graph]] | upstream | 0.48 |
| [[bld_schema_knowledge_graph]] | downstream | 0.48 |
| [[p01_kc_knowledge_graph]] | upstream | 0.47 |
| [[bld_knowledge_card_knowledge_graph]] | upstream | 0.47 |
| [[p11_qg_knowledge_graph]] | downstream | 0.46 |
| [[bld_examples_knowledge_graph]] | downstream | 0.43 |
| [[p03_sp_knowledge_graph_builder]] | upstream | 0.43 |
| [[knowledge-graph-builder]] | upstream | 0.42 |
| [[p10_lr_knowledge_graph_builder]] | downstream | 0.40 |
| [[bld_config_knowledge_graph]] | downstream | 0.38 |
