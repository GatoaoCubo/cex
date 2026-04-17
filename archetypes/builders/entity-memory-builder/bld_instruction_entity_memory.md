---
kind: instruction
id: bld_instruction_entity_memory
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for entity_memory
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Entity Memory"
version: "1.0.0"
author: n03_builder
tags: [entity_memory, builder, examples]
tldr: "Golden and anti-examples for entity memory construction, demonstrating ideal structure and common pitfalls."
domain: "entity memory construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce an entity_memory
## Phase 1: RESEARCH
1. Identify the entity: what named thing (person, tool, concept, org, project, service) is being recorded
2. Determine entity_type from enum — tool for software, service for APIs/SaaS, person for humans, concept for abstract ideas
3. Gather attributes: collect >= 3 specific, verifiable facts from primary sources (docs, official pages, direct observation)
4. Assess confidence per attribute: primary source = 0.9+, secondary/inferred = 0.5-0.69
5. Identify relationships: which other entities does this one use, own, depend on, or belong to
6. Determine update_policy: volatile entity (API, versioned tool) -> overwrite or merge; stable concept -> append
7. Set expiry: versioned services need a review date; stable concepts get null
8. Check for existing entity_memory artifacts to avoid duplicates — search by entity name and slug
9. Confirm entity slug for id: snake_case, lowercase, no hyphens, <= 30 chars
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write attributes map: snake_case keys, string values, specific facts only — no inferences
5. Write relationships list: [{entity: slug, relation: verb_noun}] — at least 1 if any links exist
6. Write Overview section: 2 sentences — what entity this is and why it is tracked
7. Write Attributes section: table with Key | Value | Type | Source columns
8. Write Relationships section: table with Entity | Relation | Direction | Notes columns
9. Write Update Policy section: policy name + conflict resolution rule + staleness handling rule
10. Verify body <= 2048 bytes
11. Verify id matches `^p10_em_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p10_em_` prefix
4. Confirm kind == entity_memory
5. Confirm entity_type is one of: person, tool, concept, organization, project, service
6. Confirm attributes map is non-empty (>= 1 key-value pair; ideally >= 3)
7. Confirm no PII in attributes (no emails, phone numbers, home addresses)
8. HARD gates: frontmatter valid, id pattern matches, attributes non-empty, entity_type in enum
9. SOFT gates: score against QUALITY_GATES.md — target >= 8.0 before outputting
10. Cross-check kind boundaries: no outcome/lesson fields (that is learning_record)? No ephemeral runtime flags (that is session_state)? Not a reusable phase sequence (that is skill)?
11. Revise if score < 8.0 — most common fix is adding more attributes or missing relationship links
