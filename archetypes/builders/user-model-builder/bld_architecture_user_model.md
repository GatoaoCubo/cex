---
quality: 8.8
quality: 8.2
kind: architecture
id: bld_architecture_user_model
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of user_model -- inventory, dependencies, and architectural position
title: "Architecture: user_model"
version: "1.0.0"
author: n03_builder
tags: [user_model, builder, architecture, honcho, P10]
tldr: "Component inventory: Peer identity + dialectic loop + Collections + storage backend + API surface. Sits in P10 memory layer between session and knowledge."
domain: "user model construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
related:
  - p01_kc_session_state
  - bld_architecture_session_backend
  - bld_memory_session_state
  - p01_kc_session_backend
  - session-state-builder
  - bld_collaboration_session_state
  - p03_sp_session_state_builder
  - p01_kc_memory_scope
  - session-backend-builder
  - p10_rs_conversation
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| peer_id | Canonical identifier for this human peer | user_model | required |
| workspace | Tenant namespace for isolation | user_model | required |
| storage.primary | Backend for persistence (SQLite default) | user_model | required |
| storage.fallback_chain | Ordered fallback backends | user_model | required |
| dialectic.pre_response_insight | Query user model before generating | user_model | required |
| dialectic.post_response_derive | Write derived facts back after response | user_model | required |
| dialectic.compaction_cadence_turns | How often to compact collections | user_model | required |
| collections | Named groups of derived facts | user_model | required |
| retention | Message and derived fact TTLs | user_model | required |
| peer.chat | NL query interface against user model | P10 runtime | consumer |
| session.context | Bounded context extraction for prompt injection | P10 runtime | consumer |
| session.representation | Static insight string for pre-response injection | P10 runtime | consumer |
| session_state | Ephemeral session snapshot -- distinct from user_model | P10 | sibling |
| entity_memory | Factual record of any named entity -- distinct | P10 | sibling |
| memory_architecture | Whole memory stack definition | P10 | parent |

## Dependency Graph
```
conversation_turn     --triggers-->   session.add_messages
session.add_messages  --writes-->     session_store
pre_response_insight  --reads-->      collections
pre_response_insight  --produces-->   insight_string
insight_string        --injects-->    generation_context
generation_context    --produces-->   response
post_response_derive  --reads-->      response + session_store
post_response_derive  --writes-->     collections
collections           --compacts_to-> derived_facts
derived_facts         --answers-->    peer.chat
derived_facts         --injects-->    session.context
storage.primary       --persists-->   collections + derived_facts
storage.fallback_chain --enables-->   storage.primary resilience
```

## Boundary Table
| user_model IS | user_model IS NOT |
|--------------|-------------------|
| Cross-session derived model of a specific human | `entity_memory` (any entity -- org, product, tool) |
| Dialectic loop with pre/post-response derivation | `session_state` (ephemeral, resets each session) |
| Workspace-scoped multi-tenant peer record | `agent_profile` (describes the AI, not the human) |
| NL-queryable via peer.chat | `episodic_memory` (raw event/message log) |
| One layer in the memory architecture | `memory_architecture` (whole stack definition) |
| Compacted into derived facts across sessions | `session_backend` (storage infrastructure, not model) |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| identity | peer_id, workspace, title | Define which human peer this is |
| storage | storage.primary, fallback_chain, pgvector_enabled | Persist collections durably |
| dialectic | pre_response_insight, post_response_derive, compaction_cadence_turns | Configure insight loop |
| facts | collections, derived_facts | Store and compact per-turn derived insights |
| governance | retention.messages_ttl_days, derived_facts_ttl_days | Control growth and staleness |
| runtime | peer.chat, session.context, session.representation, search | Expose user model to agents |

## Honcho Data Flow (end-to-end)
```
User message (turn N)
  |
  +-> session.add_messages([user_msg])          # store turn
  |
  +-> pre_response: peer.chat(insight_query)    # query user model
  |     -> insight_string injected into context
  |
  +-> LLM generates response (with insight)
  |
  +-> post_response: peer.chat(derive_query)    # derive conclusions
        -> write to collections
        -> if turn % compaction_cadence == 0: compact collections
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_session_state]] | downstream | 0.29 |
| [[bld_architecture_session_backend]] | sibling | 0.27 |
| [[bld_memory_session_state]] | downstream | 0.27 |
| [[p01_kc_session_backend]] | downstream | 0.26 |
| [[session-state-builder]] | downstream | 0.23 |
| [[bld_collaboration_session_state]] | downstream | 0.23 |
| [[p03_sp_session_state_builder]] | upstream | 0.22 |
| [[p01_kc_memory_scope]] | upstream | 0.22 |
| [[session-backend-builder]] | downstream | 0.22 |
| [[p10_rs_conversation]] | downstream | 0.22 |
