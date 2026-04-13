---
id: p01_gl_taxonomy
kind: glossary_entry
pillar: P01
title: "Taxonomy"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-management
quality: 8.8
tags: [glossary, taxonomy, classification, hierarchy]
tldr: "A hierarchical classification system organizing CEX's 123 kinds across 12 pillars with canonical tags, enforced by kind registry and schema contracts."
density_score: 0.96
updated: "2026-04-13"
---

# Taxonomy

**Term**: Taxonomy
**Abbreviation**: —
**Synonyms**: classification system, kind hierarchy, ontology (informal)

**Definition**: The hierarchical classification structure that organizes all CEX artifacts. Three levels: Pillar (12) → Kind (123) → Artifact (2,184+). Each artifact has exactly one `kind` and one `pillar`. Tags provide cross-cutting classification (3-10 per artifact, kebab-case). Maintained via `.cex/kinds_meta.json` (kind registry) and `P{01-12}_*/_schema.yaml` (pillar schemas). Not a true ontology — no formal inference rules, just strict hierarchical containment with tag-based cross-links.

**See**: `kinds_meta.json`, `taxonomy_builder_tool.md`, `agent_taxonomy_engineer.md`

## Boundary

Definicao curta de termo do dominio. NAO eh knowledge_card (sem densidade min) nem context_doc (sem escopo).


## 8F Pipeline Function

Primary function: **INJECT**
