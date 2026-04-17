---
id: mem_entity_memory_n01
kind: entity_memory
pillar: P10
nucleus: N01
title: "N01 Entity Memory"
version: "1.0.0"
quality: 9.1
tags: [entity_memory, n01, p10, analytical_envy, memory]
density_score: 1.0
---
<!-- 8F: F1=entity_memory/P10 F2=kc_entity_memory+tpl_entity_memory F3=nucleus_def_n01+kc_entity_memory+ex_entity_memory_user_preferences+knowledge_index_intelligence F4=stable entities for research continuity
     F5=rg+Get-Content+apply_patch F6=target dense markdown artifact F7=self-check properties+8F+ascii+80lines F8=N01_intelligence/P10_memory/mem_entity_memory_n01.md -->

# N01 Entity Memory

## Purpose
N01 entity memory stores stable facts about the entities that repeatedly shape research.
Analytical Envy means the memory should preserve what makes an entity strategically distinct, not every incidental mention.
If memory fills with trivia, future comparisons get weaker.

## Properties

| Property | Value |
|----------|-------|
| Kind | `entity_memory` |
| Pillar | `P10` |
| Nucleus | `N01` |
| Lens | `Analytical Envy` |
| Primary entities | vendor, product, source, analyst, market segment |
| Memory goal | durable comparative context |
| Update mode | merge with citation-aware revision |
| TTL stance | per attribute, not one blanket rule |
| Max fact density | prioritize decision-relevant attributes |
| Main risk | storing volatile observations as stable truth |

## Memory Thesis
N01 should remember the facts that reduce research startup cost:
- canonical vendor identity
- product aliases
- core positioning
- stable market segment
- recurring reliability patterns of important sources
- important entity relationships

It should not turn entity memory into a diary.

## Entity Types

| Type | Example | Why store |
|------|---------|-----------|
| vendor | company under analysis | recurring competitor work |
| product | named offering or plan | feature and pricing comparisons |
| source | recurring publication or database | trust calibration |
| analyst | repeated author or firm | bias and authority tracking |
| segment | buyer class or market slice | context for comparisons |

## Attribute Model
Each fact should include value, confidence, source, and update time.

| Attribute family | Example |
|------------------|---------|
| identity | official name, aliases, parent org |
| commercial | pricing model, target segment |
| technical | deployment model, core capability category |
| trust | source authority pattern, known bias |
| relational | competes_with, publishes_about, serves_segment |

## Update Rules
1. Stable identity facts can be long-lived.
2. Pricing model facts should be refreshed more often.
3. Weakly sourced claims should not overwrite stronger facts.
4. Conflicts should be recorded until resolved, not silently merged.
5. Attribute-level TTL beats entity-level TTL.

## Example Entity Shape
```yaml
entity: vendor_openai
entity_type: vendor
attributes:
  official_name: {value: "OpenAI", confidence: 0.98, source: "tier_1", updated: "2026-04-16"}
  pricing_model: {value: "subscription_and_usage", confidence: 0.82, source: "tier_2", updated: "2026-04-16"}
relationships:
  - relation: competes_with
    target: vendor_anthropic
    confidence: 0.95
```

## N01-Specific Memory Targets

| Target | Why it matters |
|--------|----------------|
| competitor alias maps | avoids duplicate rows in matrices |
| source trust profiles | speeds citation triage |
| recurring comparison axes per entity | improves retrieval focus |
| segment fit notes | better positioning synthesis |
| known contradiction zones | warns future analysts early |

## Memory Hygiene
Analytical Envy requires selective retention.

| Keep | Reject |
|------|--------|
| enduring identity | momentary chatter |
| repeated market role | one-off speculation |
| stable relationship | uncertain rumor |
| trust pattern | isolated emotional review |
| canonical naming | transient campaign slogan |

## Integration With Research Flow
Entity memory should be consulted during:
- query expansion
- alias normalization
- matrix row construction
- source reliability weighting
- synthesis conflict review

It should be updated after:
- repeated reuse across tasks
- confirmed source triangulation
- major vendor or product changes

## Anti-Patterns
- storing every article headline as an entity fact
- overwriting tier_1 facts with fresher but weaker gossip
- no distinction between product and vendor
- no alias memory, causing duplicate competitor rows
- no confidence scores

## N01 Decision
N01 entity memory exists to preserve structural advantage.
It keeps the durable facts that make each future comparison start from a stronger baseline than the last one.
