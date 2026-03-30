---
id: p10_lr_entity_memory_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "Entity memory records without confidence scoring caused downstream agents to treat unverified attributes (scraped from secondary sources) with the same weight as primary-source facts, leading to incorrect grounding in 3 out of 5 test prompts. Records with confidence < 0.5 that lacked expiry dates were re-injected indefinitely, polluting context with stale data in 2 production runs."
pattern: "Assign confidence float to every entity_memory. Set expiry for all volatile entities (tools, services, APIs). Use update_policy: merge for general facts, overwrite for pricing/version data. Minimum 3 attributes — records with 1-2 attributes provided insufficient grounding to be useful."
evidence: "5 grounding test prompts: 3 failed with unscored attributes; 0 failures after confidence scoring added. 2 production runs with stale injection: root cause was missing expiry on versioned tool records."
confidence: 0.85
outcome: SUCCESS
domain: entity_memory
tags: [entity-memory, confidence-scoring, expiry, update-policy, grounding, attributes]
tldr: "Confidence scoring and expiry are load-bearing for entity memory quality. Min 3 attributes. update_policy must match entity volatility."
impact_score: 8.0
decay_rate: 0.03
agent_node: edison
keywords: [entity memory, confidence, expiry, attributes, update policy, grounding, staleness, relationships]
---

## Summary
Entity memory is only as useful as its worst attribute. A single unverified fact injected with the same weight as a primary-source fact degrades the entire grounding block. Three authoring decisions determine whether entity memory is useful or noise: confidence scoring, expiry declaration, and attribute count. Records with >= 3 specific, confidence-scored attributes consistently grounded LLM responses correctly.

## Pattern
**Confidence scoring + expiry + minimum attribute density.**
- 0.9-1.0: verified from primary source (official docs, direct API response)
- 0.7-0.89: reliable secondary source (internal MEMORY.md, team knowledge)
- 0.5-0.69: probable — inferred from multiple consistent mentions
- 0.0-0.49: uncertain — single mention; consider omitting

Expiry rules:
- tool/service with versioning: 6-12 months
- person with role: 12 months
- stable concept/organization: null
- API endpoint/pricing: 3-6 months

Update policy matching:
- pricing, versions, status → overwrite
- history, timeline, events → append
- general facts with mixed volatility → merge
- contracts, decisions → versioned

Attribute count: minimum 3 (identity + status + provenance); target 5-8; split at 12+.

## Anti-Pattern
- Single attribute — no grounding advantage over the entity name alone
- confidence: 1.0 for scraped web data — overconfidence poisons merge logic
- No expiry on versioned API service — stale endpoint causes silent failures after migration
- update_policy: append on pricing — accumulates outdated prices
- Attributes containing inferences ("best_tool: true") — opinions corrupt fact maps
- Mixing entity_memory with learning_record fields (impact_score, decay_rate) — breaks routing
