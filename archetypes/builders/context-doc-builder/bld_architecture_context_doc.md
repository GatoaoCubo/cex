---
kind: architecture
id: bld_architecture_context_doc
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of context_doc — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Context Doc"
version: "1.0.0"
author: n03_builder
tags: [context_doc, builder, examples]
tldr: "Golden and anti-examples for context doc construction, demonstrating ideal structure and common pitfalls."
domain: "context doc construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - context-doc-builder
  - bld_schema_context_doc
  - p03_sp_context_doc_builder
  - p01_kc_context_doc
  - p11_qg_context_doc
  - bld_collaboration_context_doc
  - bld_architecture_glossary_entry
  - bld_knowledge_card_context_doc
  - bld_architecture_chain
  - p01_kc_glossary_entry
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| domain_scope | Explicit boundary — what the context covers and excludes | context_doc | required |
| background_narrative | Prose explanation of the domain — history, purpose, key facts | context_doc | required |
| stakeholder_map | Who is involved, their roles, and their concerns | context_doc | required |
| constraint_list | Hard limits, compliance requirements, non-negotiables | context_doc | required |
| assumption_list | Working assumptions the domain context depends on | context_doc | required |
| dependency_list | External systems, teams, or artifacts this domain relies on | context_doc | optional |
| system_prompt | Agent persona file that loads context_doc at boot | P03 | consumer |
| action_prompt | Task-level prompt that injects context_doc per invocation | P03 | consumer |
| knowledge_card | Sibling artifact — single atomic fact with density gate | P01 | sibling |
| glossary_entry | Sibling artifact — single controlled-vocabulary term definition | P01 | sibling |
## Dependency Graph
```
domain_scope        --produces-->  background_narrative
domain_scope        --produces-->  constraint_list
background_narrative --produces--> stakeholder_map
assumption_list     --depends-->   domain_scope
dependency_list     --depends-->   domain_scope
context_doc         --produces-->  system_prompt
context_doc         --produces-->  action_prompt
knowledge_card      --depends-->   context_doc
glossary_entry      --depends-->   context_doc
```
| From | To | Type | Data |
|------|----|------|------|
| domain_scope | background_narrative | produces | bounded domain as subject of narrative |
| domain_scope | constraint_list | produces | boundary that shapes what is constrained |
| background_narrative | stakeholder_map | produces | domain narrative that identifies actors |
| assumption_list | domain_scope | depends | assumptions derived from scope analysis |
| dependency_list | domain_scope | depends | external dependencies identified from scope |
| context_doc | system_prompt | produces | domain background injected into agent persona |
| context_doc | action_prompt | produces | situational context injected per task |
| knowledge_card | context_doc | depends | atomic facts scoped to same domain |
| glossary_entry | context_doc | depends | term definitions scoped to same domain |
## Boundary Table
| context_doc IS | context_doc IS NOT |
|---------------|-------------------|
| Multi-fact domain background for prompt hydration | A single atomic fact at high density (that is knowledge_card) |
| Narrative prose allowed — background, history, framing | A single controlled-vocabulary term definition (that is glossary_entry) |
| Loaded at agent boot or injected per task | A step-by-step execution protocol (that is instruction) |
| Covers stakeholders, constraints, assumptions, dependencies | An agent persona with operational rules (that is system_prompt) |
| Max 2048 bytes — concise enough for context injection | A full specification document or design artifact |
| P01 content layer — pure knowledge, no execution logic | A runtime tool or executable component |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| scoping | domain_scope | Define what the context covers and excludes |
| knowledge | background_narrative, stakeholder_map | Capture domain facts, history, and actors |
| constraints | constraint_list, assumption_list, dependency_list | Document limits, working assumptions, and external dependencies |
| injection | system_prompt, action_prompt | Downstream consumers that load context into prompts |
| siblings | knowledge_card, glossary_entry | Related P01 artifacts covering atomic facts and terms |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[context-doc-builder]] | upstream | 0.51 |
| [[bld_schema_context_doc]] | upstream | 0.45 |
| [[p03_sp_context_doc_builder]] | upstream | 0.45 |
| [[p01_kc_context_doc]] | upstream | 0.42 |
| [[p11_qg_context_doc]] | downstream | 0.38 |
| [[bld_collaboration_context_doc]] | downstream | 0.35 |
| [[bld_architecture_glossary_entry]] | sibling | 0.35 |
| [[bld_knowledge_card_context_doc]] | upstream | 0.30 |
| [[bld_architecture_chain]] | sibling | 0.29 |
| [[p01_kc_glossary_entry]] | upstream | 0.29 |
