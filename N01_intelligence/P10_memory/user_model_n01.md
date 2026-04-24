---
id: user_model_n01
kind: user_model
8f: F2_become
nucleus: n01
pillar: P10
mirrors: N00_genesis/P10_memory/tpl_user_model.md
mirror_version: 1.0.0
promoted_from: null
overrides:
  tone: analytical, source-citing, exhaustive
  voice: third-person academic
  sin_lens: Analytical Envy
  required_fields:
    - sources          # min 3 per claim
    - confidence_score # 0.0-1.0 per known fact
    - last_verified    # YYYY-MM-DD freshness stamp
    - source_reliability_index  # domain extension
  quality_threshold: 9.2
  density_target: 0.90
  example_corpus: 3+ examples with cited sources
version: 1.0.0
quality: 7.9
tags: [mirror, n01, research, hermes_assimilation, user_model]
related:
  - p02_nd_n00.md
  - n01_dr_research_pipeline
  - p10_out_source_dossier
  - p11_qg_intelligence
  - p12_wf_auto_research
  - spec_n01_n04_verticalization
  - p02_nd_n01.md
  - leverage_map_v2_n01_tool_verification
  - ex_chain_research_pipeline
  - SPEC_05_skills_runtime
density_score: 1.0
updated: "2026-04-22"
---

## Override Rationale

N01 treats each peer as a **research subject**, not just a preference store.
The mirror adds source reliability tracking (who told us what, how trustworthy) and
raises confidence requirements: every derived fact needs a provenance chain.

## N01 Domain Extensions

| Field | Type | Description |
|-------|------|-------------|
| `source_reliability_index` | map<str,float> | Domain -> mean reliability score for sources peer cites |
| `citation_depth_preference` | int | How deep peer goes: 1=abstract, 3=full paper, 5=raw data |
| `domain_expertise_map` | map<str,float> | Domain -> assessed competence level (0.0-1.0) |
| `analytical_blind_spots` | list[str] | Domains where peer self-reports or shows consistent gaps |

## Collections (N01 Overlay)

### sources (N01 extra collection)
| Source | Domain | Reliability | Last Cited |
|--------|--------|-------------|------------|
| `{{source_id}}` | {{domain}} | {{0.0-1.0}} | {{YYYY-MM-DD}} |

All base collections from N00 tpl apply unchanged (preferences, working_style, context_history).

## Dialectic Loop (N01 flavor)

- `post_response_derive`: also extracts source mentions and logs to `sources` collection
- `compaction_cadence_turns`: 30 (tighter than N00 default 50 -- research sessions are denser)

## Links

- N00 archetype: [[N00_genesis/P10_memory/tpl_user_model]]
- N00 KC: [[N00_genesis/P01_knowledge/library/kind/kc_user_model]]
- Related: [[N01_intelligence/P10_memory/entity_memory_n01]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_nd_n00.md]] | upstream | 0.28 |
| [[n01_dr_research_pipeline]] | downstream | 0.23 |
| [[p10_out_source_dossier]] | related | 0.21 |
| [[p11_qg_intelligence]] | downstream | 0.20 |
| [[p12_wf_auto_research]] | downstream | 0.20 |
| [[spec_n01_n04_verticalization]] | upstream | 0.19 |
| [[p02_nd_n01.md]] | upstream | 0.17 |
| [[leverage_map_v2_n01_tool_verification]] | upstream | 0.17 |
| [[ex_chain_research_pipeline]] | upstream | 0.17 |
| [[SPEC_05_skills_runtime]] | upstream | 0.17 |
