---
id: p01_gl_knowledge_card
kind: glossary_entry
pillar: P01
title: "Knowledge Card (KC)"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-management
quality: 8.7
tags: [glossary, knowledge-card, kc, p01]
tldr: "A dense, structured document encoding a single concept with mandatory frontmatter, density ≥0.8, and machine-parseable format."
density_score: 0.97
updated: "2026-04-13"
---

# Knowledge Card (KC)

**Term**: Knowledge Card
**Abbreviation**: KC
**Synonyms**: knowledge doc, fact card

**Definition**: A structured Markdown document with YAML frontmatter that encodes a single domain concept at high density (≥0.8). The atomic knowledge unit in CEX. Every sentence must pass: "if I delete this, does the KC lose value?" Maximum 2KB (focused) or 4KB (comprehensive). Section order: H1 → Core → Tables → CEX Integration.

**See**: `kc_structure_contract.md`, `knowledge-card-builder`

## Boundary

Definicao curta de termo do dominio. NAO eh knowledge_card (sem densidade min) nem context_doc (sem escopo).


## 8F Pipeline Function

Primary function: **INJECT**
