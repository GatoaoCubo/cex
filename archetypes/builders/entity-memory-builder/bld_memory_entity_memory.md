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
satellite: edison
keywords: [entity memory, confidence, expiry, attributes, update policy, grounding, staleness, relationships]
---

## Summary
Entity memory records are only as useful as their worst attribute. A single unverified fact injected into LLM context with the same weight as a primary-source fact degrades the entire grounding block. The difference between useful entity memory and noise comes down to three decisions made at authoring time: confidence scoring, expiry declaration, and attribute count.
Records with >= 3 specific, confidence-scored attributes consistently grounded LLM responses correctly. Records with 1-2 vague attributes without confidence scores caused agents to either over-rely on uncertain facts or ignore the grounding block entirely.
## Pattern
**Confidence scoring + expiry + minimum attribute density.**
Confidence scale:
- 0.9-1.0: verified from primary source (official docs, direct API response)
- 0.7-0.89: reliable from trusted secondary source (internal MEMORY.md, team knowledge)
- 0.5-0.69: probable — inferred from multiple consistent mentions
- 0.0-0.49: uncertain — single mention, unverified; consider omitting or flagging
Expiry rules:
- tool / service with versioning: set expiry 6-12 months from created date
- person with role: set expiry 12 months (roles change)
- stable concept / organization: expiry null (facts do not stale quickly)
- API endpoint / pricing: set expiry 3-6 months (changes frequently)
Update policy matching:
- pricing, versions, status -> overwrite (latest value replaces)
- history, timeline, events -> append (accumulates)
- general facts with mixed volatility -> merge (new keys added, existing updated if confidence improves)
- contracts, decisions, agreements -> versioned (all versions preserved)
Attribute count budget:
- Minimum useful: 3 attributes (identity + status + provenance)
- Target: 5-8 attributes (covers identity, capabilities, integration, status)
- Maximum before split: 12 attributes (beyond this, consider splitting into sub-entities)
## Anti-Pattern
- Storing a single attribute ("purpose: web scraping") — provides no grounding advantage over the entity name alone.
- Confidence: 1.0 for scraped web data — overconfidence poisons merge logic.
- No expiry on a versioned API service — stale endpoint injected after migration causes silent failures.
- update_policy: append on pricing data — accumulates outdated prices; consumer sees all historical values.
- Attributes containing inferences ("best_tool: true") — opinions corrupt fact maps.
- Mixing entity_memory with learning_record fields (impact_score, decay_rate in entity_memory) — wrong kind, breaks routing.
## Context
The 2048-byte body limit for entity_memory is generous enough for 8-10 attributes plus a relationship table. Allocate bytes: Overview (100) + Attributes table (800) + Relationships (400) + Update Policy (200) = ~1500. Reserve 548 bytes for dense attribute values. Frontmatter carries the machine-readable payload; body carries the human-readable structured view — both must be consistent.
