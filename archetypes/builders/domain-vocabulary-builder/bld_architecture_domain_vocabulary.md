---
id: bld_architecture_domain_vocabulary
kind: component_map
pillar: P08
llm_function: CONSTRAIN
version: 1.0.0
quality: 7.1
tags: [domain_vocabulary, architecture, ubiquitous-language]
title: "Architecture Domain Vocabulary"
density_score: 1.0
updated: "2026-04-17"
---
# Architecture: domain_vocabulary
## Position in CEX Kind Taxonomy
```
P01 Knowledge
  knowledge_card    (atomic facts)
  domain_vocabulary <-- THIS KIND (canonical term registry for a BC)
  glossary_entry    (single term definition)
  context_doc       (broad domain background)
```

## Relationships
| Relation | Kind | Direction | Notes |
|----------|------|-----------|-------|
| scoped to | bounded_context | many-to-one | One vocab per BC |
| references | glossary_entry | one-to-many | Terms may link to entries |
| loaded by | agent | many-to-many | All agents in BC load vocab |
| enforces | ubiquitous_language_rule | semantic | Prevents semantic drift |
| extends | domain_vocabulary (parent) | optional | Inheritance for sub-contexts |

## Hierarchy
```
N00_genesis core vocabulary (CEX universal terms: 257 kinds, 8F, 12 pillars)
    |
    +-- dv_{nucleus}_vocabulary (per-nucleus domain extension)
    |       +-- dv_n01_vocabulary (intelligence terms)
    |       +-- dv_n03_vocabulary (engineering terms)
    |
    +-- dv_{project}_vocabulary (project-specific terms)
```

## Loading Protocol (F2b SPEAK)
domain_vocabulary is the target artifact for the F2b SPEAK sub-step:
1. Agent loads its bounded_context's domain_vocabulary at F2b
2. All F3-F8 output uses only terms from loaded vocabulary
3. Unknown terms: flag for addition to vocabulary, don't invent

## When to Use
| Scenario | Use |
|----------|-----|
| Registry of terms for a whole BC | domain_vocabulary |
| Single term definition | glossary_entry |
| Formal term relationships (IS-A, PART-OF) | ontology |
| Cross-BC vocabulary bridge | translation_map (if exists) |
