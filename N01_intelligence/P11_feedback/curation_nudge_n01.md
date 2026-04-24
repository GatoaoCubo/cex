---
id: curation_nudge_n01
kind: curation_nudge
8f: F6_produce
nucleus: n01
pillar: P11
mirrors: N00_genesis/P11_feedback/tpl_curation_nudge.md
mirror_version: 1.0.0
promoted_from: null
overrides:
  tone: analytical, source-citing, exhaustive
  voice: third-person academic
  sin_lens: Analytical Envy
  required_fields:
    - sources
    - confidence_score
    - last_verified
  quality_threshold: 9.2
  density_target: 0.90
  nudge_flavors:
    - new_source_detected     # a URL/paper not in KC -- add to corpus?
    - claim_without_citation  # claim made without source -- verify?
    - stale_fact_detected     # last_verified > 90 days -- refresh?
    - gap_vs_competitor       # competitor has data N01 lacks -- harvest?
version: 1.0.0
quality: 7.7
tags: [mirror, n01, research, hermes_assimilation, curation_nudge]
related:
  - p12_wf_auto_research
  - n01_dr_research_pipeline
  - p02_nd_n00.md
  - p02_nd_n01.md
  - p02_agent_competitor_tracker
  - n01_agent_intelligence
  - p12_dr_intelligence
  - n01_dr_intelligence
  - spec_n01_n04_verticalization
  - n01_intelligence
density_score: 1.0
updated: "2026-04-22"
---

## Override Rationale

N01 nudges are intelligence-oriented: they fire when the system detects an opportunity
to strengthen the knowledge base, not just to persist conversation state.
The `Analytical Envy` lens means every new source triggers an envy-fueled question:
"Do we have this? Is ours better? Do we need it?"

## N01 Nudge Flavors

| Flavor | Trigger | Prompt Template |
|--------|---------|----------------|
| `new_source_detected` | URL/DOI not in KC corpus | "New source found: {{source}}. Add to intelligence KC?" |
| `claim_without_citation` | Assertion lacking provenance | "Claim made: '{{claim}}'. Source needed -- add citation?" |
| `stale_fact_detected` | last_verified > 90 days | "Fact '{{fact}}' unverified since {{date}}. Refresh?" |
| `gap_vs_competitor` | Competitor KC has data N01 lacks | "Competitor intel gap: {{gap}}. Harvest and persist?" |

## Cadence Overrides

| Parameter | N00 Default | N01 Override | Reason |
|-----------|------------|--------------|--------|
| `min_interval_turns` | 5 | 3 | Research sessions are shorter, denser |
| `max_per_session` | 3 | 5 | More nudge types warrant higher cap |
| `threshold` | 10 | 7 | N01 fires earlier -- envy is impatient |

## Links

- N00 archetype: [[N00_genesis/P11_feedback/tpl_curation_nudge]]
- N00 KC: [[N00_genesis/P01_knowledge/library/kind/kc_curation_nudge]]
- Related: [[N01_intelligence/P11_feedback/quality_gate_advanced_n01]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_auto_research]] | downstream | 0.28 |
| [[n01_dr_research_pipeline]] | downstream | 0.25 |
| [[p02_nd_n00.md]] | upstream | 0.25 |
| [[p02_nd_n01.md]] | upstream | 0.24 |
| [[p02_agent_competitor_tracker]] | upstream | 0.23 |
| [[n01_agent_intelligence]] | upstream | 0.22 |
| [[p12_dr_intelligence]] | downstream | 0.22 |
| [[n01_dr_intelligence]] | downstream | 0.21 |
| [[spec_n01_n04_verticalization]] | upstream | 0.21 |
| [[n01_intelligence]] | upstream | 0.20 |
