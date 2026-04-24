---
id: skill_n01
kind: skill
8f: F5_call
nucleus: n01
pillar: P04
mirrors: N00_genesis/P04_tools/kind_skill/kind_manifest_n00.md
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
    - verification_steps   # N01 extension: explicit source-check protocol
  quality_threshold: 9.2
  density_target: 0.90
version: 1.0.0
quality: 7.8
tags: [mirror, n01, research, hermes_assimilation, skill]
related:
  - bld_collaboration_skill
  - bld_architecture_skill
  - procedural-memory-builder
  - bld_system_prompt_skill
  - bld_knowledge_card_procedural_memory
  - bld_memory_skill
  - skill-builder
  - p01_kc_skill
  - p03_ins_skill_builder
  - shared_skill_verification_protocol
density_score: 1.0
updated: "2026-04-22"
---

## Override Rationale

N01 skills emphasize **source verification** as a first-class step, not an afterthought.
Every skill that produces claims must declare how those claims are verified.
The sin lens (Analytical Envy) drives skills to go deeper than requested:
if 1 source exists, N01 finds 3; if 3, it finds the primary source.

## N01 Skill Signature Extensions

Every N01 skill manifest adds:

```yaml
verification_steps:
  - step: locate_primary_source     # find original paper/repo/doc
  - step: cross_reference_n_sources # min 3 independent confirmations
  - step: check_recency             # last_updated within acceptable window
  - step: flag_contradictions       # surface conflicting evidence explicitly
confidence_output:
  per_claim: true                   # confidence score attached to each claim
  overall: true                     # aggregate confidence for the skill run
```

## N01 Skill Categories

| Category | Examples | Verification Emphasis |
|----------|---------|----------------------|
| `competitive_intel` | competitor_scan, pricing_audit | Cross-ref 3+ public sources |
| `paper_review` | arxiv_digest, benchmark_compare | Original paper + 2 critiques |
| `market_research` | tam_estimate, segment_profile | Cite analyst report + primary data |
| `knowledge_harvest` | url_to_kc, pdf_to_kc | Source URL + extraction timestamp |
| `trend_detection` | signal_monitor, trend_spike | Time-series confidence interval |

## Deviation from N00

N00 skill is tool-agnostic. N01 skill hardwires `verification_steps` into every run.
A skill that cannot cite its sources is not a valid N01 skill.

## Links

- N00 archetype: [[N00_genesis/P04_tools/kind_skill]]
- N00 KC: [[N00_genesis/P01_knowledge/library/kind/kc_skill]]
- Related: [[N01_intelligence/P04_tools/search_strategy_n01]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_skill]] | downstream | 0.44 |
| [[bld_architecture_skill]] | downstream | 0.39 |
| [[procedural-memory-builder]] | downstream | 0.36 |
| [[bld_system_prompt_skill]] | upstream | 0.36 |
| [[bld_knowledge_card_procedural_memory]] | upstream | 0.36 |
| [[bld_memory_skill]] | downstream | 0.35 |
| [[skill-builder]] | related | 0.33 |
| [[p01_kc_skill]] | related | 0.32 |
| [[p03_ins_skill_builder]] | upstream | 0.30 |
| [[shared_skill_verification_protocol]] | sibling | 0.28 |
