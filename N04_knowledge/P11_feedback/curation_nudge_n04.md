---
id: curation_nudge_n04
kind: curation_nudge
nucleus: n04
pillar: P11
mirrors: N00_genesis/compiled/tpl_curation_nudge.yaml
mirror_version: 1.0.0
promoted_from: null
overrides:
  tone: archival, dense, citation-thick
  voice: third-person encyclopedic
  sin_lens: GULA DO CONHECIMENTO
  required_fields:
    - sources
    - retrieval_method
    - freshness
  quality_threshold: 9.2
  density_target: 0.92
  example_corpus: 3+ examples with source manifest
ownership: canonical
trigger:
  type: density_threshold
  threshold: 10           # unconfirmed knowledge items triggers nudge
cadence:
  min_interval_turns: 5
  max_per_session: 3
version: 1.0.0
quality: 8.1
tags: [mirror, n04, knowledge, curation_nudge, hermes_assimilation, memory, canonical_owner]
related:
  - bld_collaboration_memory_type
  - agent_card_n04
  - bld_collaboration_memory_scope
  - p01_kc_memory_scope
  - n04_knowledge_memory_index
  - memory-scope-builder
  - bld_manifest_memory_type
  - bld_knowledge_card_memory_scope
  - p01_kc_memory_persistence
  - atom_22_memory_taxonomy
---

## Override Rationale

N04 **owns** the `curation_nudge` kind. Knowledge Gluttony means the system must
proactively prompt the user to persist any valuable insight surfaced during the session.
N04's nudge is specialised: it targets MEMORY.md persistence, taught-terms registry
updates, and knowledge corpus expansions -- the three N04-canonical memory destinations.

## Trigger Configuration (N04 canonical)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Trigger type | density_threshold | Fire when unconfirmed knowledge count >= threshold |
| Threshold | 10 | Items accumulated without explicit persistence decision |
| Min interval | 5 turns | Don't interrupt rapid-fire exchanges |
| Max per session | 3 | Avoid nudge fatigue; escalate to user after 3rd |
| Observation source | retrieval_history + taught_terms | What to surface for confirmation |

## Prompt Templates (N04)

### MEMORY.md persistence nudge
```
Detectei {{n}} insights nao persistidos nesta sessao (taught_terms: {{tt}}, KCs: {{kc}}).
Persistir em MEMORY.md? [S/N]
Confirmado -> escreve em {{destination}} e adiciona ponteiro ao indice.
```

### Taught-terms registry nudge
```
Ensinei {{n}} termos novos: {{term_list}}.
Registrar em taught_terms_registry.md? [S/N]
```

### Knowledge corpus expansion nudge
```
Corpus '{{corpus_id}}' cresceu {{n}} docs nesta sessao.
Atualizar user_model_n04.knowledge_corpus? [S/N]
```

## Target Memory Destinations

| Destination | Kind | Trigger Condition |
|-------------|------|-------------------|
| `MEMORY.md` | index | Any confirmed insight |
| `taught_terms_registry.md` | entity_memory | Term metaphor->industry mapping confirmed |
| `user_model_n04.knowledge_corpus` | user_model | Corpus ingestion confirmed |
| `N04_knowledge/P10_memory/entity_memory_n04.md` | entity_memory | Entity fact confirmed |

## Auto-write Behavior

When peer confirms a nudge:
1. N04 writes directly to the destination artifact (no extra confirmation)
2. Appends pointer to MEMORY.md index if not already present
3. Stamps `freshness: {{YYYY-MM-DD}}` on the new entry
4. Logs nudge result to `P11_feedback/iteration_history.md`

## Links

- N00 archetype: [[N00_genesis/compiled/tpl_curation_nudge.yaml]]
- N00 KC: [[N00_genesis/P01_knowledge/library/compiled/kc_curation_nudge.yaml]]
- Ownership sibling: [[N04_knowledge/P10_memory/user_model_n04]] (receives written facts)
- Memory index: [[.claude/projects/C--Users-CEX-Documents-GitHub-cex/memory/MEMORY.md]]
- Upstream: HERMES NousResearch/hermes-agent

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_type]] | downstream | 0.33 |
| [[agent_card_n04]] | upstream | 0.32 |
| [[bld_collaboration_memory_scope]] | downstream | 0.32 |
| [[p01_kc_memory_scope]] | upstream | 0.28 |
| [[n04_knowledge_memory_index]] | upstream | 0.28 |
| [[memory-scope-builder]] | upstream | 0.27 |
| [[bld_manifest_memory_type]] | upstream | 0.27 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.26 |
| [[p01_kc_memory_persistence]] | upstream | 0.25 |
| [[atom_22_memory_taxonomy]] | related | 0.24 |
