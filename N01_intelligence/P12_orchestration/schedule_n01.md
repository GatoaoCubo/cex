---
id: schedule_n01
kind: schedule
8f: F8_collaborate
nucleus: n01
pillar: P12
mirrors: N00_genesis/P12_orchestration/kind_schedule/kind_manifest_n00.md
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
    - intel_sweep_targets   # N01 extension: what to monitor per cadence
  quality_threshold: 9.2
  density_target: 0.90
version: 1.0.0
quality: 8.1
tags: [mirror, n01, research, hermes_assimilation, schedule]
related:
  - p02_nd_n00.md
  - schedule-builder
  - n01_dr_research_pipeline
  - p02_agent_competitor_tracker
  - p02_nd_n01.md
  - n01_dr_intelligence
  - p02_card_intelligence
  - bld_collaboration_schedule
  - n01_intelligence
  - p12_wf_auto_research
density_score: 1.0
updated: "2026-04-22"
---

## Override Rationale

N01 schedules define **research cadences**, not generic task timers.
The Analytical Envy lens makes N01 schedule-driven: recurring sweeps ensure
competitors are never ahead of us for more than one cycle.

## Standard N01 Research Cadences

| Cadence | Cron | Scope | Output Kind |
|---------|------|-------|-------------|
| `daily_intel_sweep` | `0 7 * * *` | New papers, competitor updates, pricing changes | knowledge_card |
| `weekly_competitive_audit` | `0 9 * * 1` | Full competitor landscape refresh | knowledge_card + bias_audit |
| `monthly_benchmark_compare` | `0 8 1 * *` | Model/tool benchmark comparison update | benchmark |
| `quarterly_taxonomy_gap` | `0 8 1 */3 *` | CEX kind taxonomy vs. industry state-of-art | decision_record |

## Schedule Frontmatter Extensions

```yaml
intel_sweep_targets:
  - domain: competitive_intel
    sources: [crunchbase, linkedin, g2, product_hunt]
    staleness_threshold_days: 7
  - domain: research_papers
    sources: [arxiv, semantic_scholar, acl_anthology]
    staleness_threshold_days: 3
output_on_change_only: true   # suppress no-diff runs -- don't waste tokens
confidence_decay_per_day: 0.005  # facts lose 0.5%/day confidence until refreshed
```

## Deviation from N00

N00 schedule is generic recurrence. N01 schedule declares **what intelligence to harvest**,
**where to find it**, and **how fast knowledge decays** between runs.

## Links

- N00 archetype: [[N00_genesis/P12_orchestration/kind_schedule]]
- N00 KC: [[N00_genesis/P01_knowledge/library/kind/kc_schedule]]
- Related: [[N01_intelligence/P12_orchestration/dispatch_rule_intelligence]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_nd_n00.md]] | upstream | 0.30 |
| [[schedule-builder]] | related | 0.24 |
| [[n01_dr_research_pipeline]] | related | 0.24 |
| [[p02_agent_competitor_tracker]] | upstream | 0.24 |
| [[p02_nd_n01.md]] | upstream | 0.22 |
| [[n01_dr_intelligence]] | related | 0.21 |
| [[p02_card_intelligence]] | upstream | 0.21 |
| [[bld_collaboration_schedule]] | related | 0.21 |
| [[n01_intelligence]] | upstream | 0.20 |
| [[p12_wf_auto_research]] | related | 0.20 |
