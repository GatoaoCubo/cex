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

## Source Reliability Scoring (N01 Domain-Specific)

N01 assesses every source a peer cites on 4 dimensions before trusting it:

| Dimension | Weight | Scoring Criteria |
|-----------|--------|-----------------|
| Recency | 0.30 | <30d = 1.0, 30-90d = 0.8, 90-180d = 0.6, 180-365d = 0.3, >365d = 0.1 |
| Verifiability | 0.25 | Primary (API/scrape) = 1.0, Official docs = 0.8, Blog/tweet = 0.5, Hearsay = 0.1 |
| Cross-confirmation | 0.25 | 3+ independent sources = 1.0, 2 sources = 0.7, single source = 0.3 |
| Domain authority | 0.20 | Core maintainer = 1.0, Contributor = 0.7, Industry analyst = 0.5, General media = 0.2 |

Composite reliability = weighted sum. Threshold for citation in KC: >= 0.55.

## Anti-Patterns (N01 User Modeling)

| Anti-Pattern | Why It Fails | Correction |
|-------------|-------------|-----------|
| Treating user claims as facts | Users report aspirational expertise, not verified competence | Cross-check against actual queries and tool usage patterns |
| Static expertise map | Domain competence shifts session-to-session | Decay factor: 0.95 per week without domain interaction |
| Ignoring blind spots | Peer may cite sources outside their competence | Flag when citation_depth_preference > domain_expertise_map score |
| Over-modeling from single session | Small sample size inflates confidence | Require >= 3 sessions before setting any score above 0.7 |

## Dialectic Loop (N01 flavor)

- `post_response_derive`: also extracts source mentions and logs to `sources` collection
- `compaction_cadence_turns`: 30 (tighter than N00 default 50 -- research sessions are denser)
- `expertise_decay_window`: 7 days (multiply domain_expertise_map values by 0.95 per week of inactivity)
- `blind_spot_detection`: if peer cites a source with reliability < 0.4 in a domain where their expertise > 0.6, flag as potential blind spot

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
