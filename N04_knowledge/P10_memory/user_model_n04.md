---
id: user_model_n04
kind: user_model
8f: F2_become
nucleus: n04
pillar: P10
mirrors: N00_genesis/P10_memory/tpl_user_model.md
mirror_version: 1.0.0
promoted_from: null
overrides:
  tone: archival, dense, citation-thick
  voice: third-person encyclopedic
  sin_lens: Knowledge Gluttony
  required_fields:
    - sources           # 3+ minimum per derived fact
    - retrieval_method  # how the fact was surfaced
    - freshness         # YYYY-MM-DD last-verified stamp
    - taught_terms      # domain extension: terms successfully taught to this peer
    - knowledge_corpus  # domain extension: what corpora the peer has ingested
  quality_threshold: 9.2
  density_target: 0.92
  example_corpus: 3+ examples with source manifest
version: 1.0.0
quality: 7.9
tags: [mirror, n04, knowledge, user_model, hermes_assimilation, canonical_owner]
ownership: canonical
related:
  - agent_card_n04
  - n04_dr_knowledge
  - self_audit_n04_codex_2026_04_15
  - bld_architecture_supabase_data_layer
  - p02_nd_n04.md
  - p01_kc_supabase_data_layer_n04
  - n04_knowledge
  - p02_card_knowledge
  - bld_collaboration_supabase_data_layer
  - n04_knowledge_memory_index
---

## Override Rationale

N04 **owns** the `user_model` kind. Knowledge Gluttony means the peer model is not a thin
preference cache -- it is an encyclopedic record of every knowledge interaction: what the peer
knows, how they prefer to consume knowledge, which terms have been taught, and what corpora
they have already ingested. N04 enriches the base model with knowledge-domain fields that
no other nucleus tracks.

## N04 Domain Extensions (Canonical)

| Field | Type | Description |
|-------|------|-------------|
| `taught_terms` | map<str,{industry_term,date}> | Terms taught to peer: metaphor -> industry mapping + date |
| `knowledge_corpus` | list[{corpus_id, ingested_at, size_docs}] | Corpora the peer has consumed via RAG or read |
| `retrieval_preference` | enum | dense \| sparse \| hybrid \| graph -- peer's preferred retrieval mode |
| `citation_appetite` | int | How many sources peer expects per claim (1=none, 5=exhaustive) |
| `taxonomy_familiarity` | map<str,float> | Pillar -> familiarity score (0.0-1.0) for CEX taxonomy |
| `memory_density_preference` | float | Preferred knowledge density per response (0.0=concise, 1.0=maximal) |

## Collections (N04 Overlay)

### preferences
| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| `retrieval_preference` | hybrid | 0.9 | {{YYYY-MM-DD}} |
| `citation_appetite` | 3 | 0.85 | {{YYYY-MM-DD}} |
| `memory_density_preference` | 0.85 | 0.8 | {{YYYY-MM-DD}} |

### working_style
| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| `taxonomy_mode` | guided | 0.9 | {{YYYY-MM-DD}} |
| `knowledge_depth` | domain_expert | 0.85 | {{YYYY-MM-DD}} |

### taught_terms (N04 extra collection)
| Metaphor | Industry Term | Taught At | Source |
|----------|---------------|-----------|--------|
| `{{metaphor}}` | {{industry_term}} | {{YYYY-MM-DD}} | {{session_id}} |

### knowledge_corpus (N04 extra collection)
| Corpus ID | Ingested At | Size (docs) | Retrieval Score |
|-----------|-------------|-------------|-----------------|
| `{{corpus_id}}` | {{YYYY-MM-DD}} | {{n}} | {{0.0-1.0}} |

All base collections from N00 tpl apply unchanged (context_history).

## Dialectic Loop (N04 flavor)

- `post_response_derive`: extracts new knowledge claims, logs taught_terms, appends to knowledge_corpus
- `compaction_cadence_turns`: 40 (tighter than N00 default 50 -- knowledge sessions accumulate fast)
- `freshness_check`: on every pre_response_insight, flag any derived fact older than 90 days

## MEMORY.md Integration (canonical behavior)

N04 is the canonical writer to `.claude/projects/*/memory/MEMORY.md`.
On session end, the curation_nudge fires if any unconfirmed knowledge exists.
Confirmed knowledge writes directly to the corresponding memory file; a pointer
is appended to MEMORY.md index.

## Links

- N00 archetype: [[N00_genesis/P10_memory/tpl_user_model]]
- N00 KC: [[N00_genesis/P01_knowledge/library/kind/kc_user_model]]
- Ownership sibling: [[N04_knowledge/P11_feedback/curation_nudge_n04]] (memory persistence trigger)
- Related: [[N04_knowledge/P10_memory/entity_memory_n04]]
- Taught-terms registry: [[N07_admin/P10_memory/taught_terms_registry.md]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n04]] | upstream | 0.32 |
| [[n04_dr_knowledge]] | related | 0.26 |
| [[self_audit_n04_codex_2026_04_15]] | upstream | 0.26 |
| [[bld_architecture_supabase_data_layer]] | upstream | 0.25 |
| [[p02_nd_n04.md]] | upstream | 0.24 |
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.23 |
| [[n04_knowledge]] | upstream | 0.23 |
| [[p02_card_knowledge]] | upstream | 0.23 |
| [[bld_collaboration_supabase_data_layer]] | downstream | 0.23 |
| [[n04_knowledge_memory_index]] | related | 0.22 |
