---
quality: 7.6
quality: 7.3
id: handoff_n01
kind: handoff
8f: F8_collaborate
nucleus: n01
pillar: P12
mirrors: N00_genesis/P12_orchestration/kind_handoff/kind_manifest_n00.md
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
    - source_manifest    # N01 extension: full source list passed downstream
    - confidence_summary # N01 extension: aggregate confidence per output section
  quality_threshold: 9.2
  density_target: 0.90
version: 1.0.0
tags: [mirror, n01, research, hermes_assimilation, handoff]
related:
  - p02_nd_n00.md
  - bld_knowledge_card_nucleus_def
  - p12_wf_intelligence_pipeline
  - spec_n01_n04_verticalization
  - n01_dr_research_pipeline
  - p03_sp_orchestration_nucleus
  - n01_dr_intelligence
  - p03_sp_n01_intelligence
  - dispatch
  - p01_ctx_cex_project
density_score: 1.0
updated: "2026-04-22"
---

## Override Rationale

N01 handoffs carry **intelligence provenance**, not just task results.
When N01 passes findings to another nucleus (N04, N07, N03), the receiving nucleus
gets not only the conclusions but the source manifest and per-section confidence scores.
This prevents downstream nuclei from treating N01 output as ground truth when
confidence is low or sources are sparse.

## Source Manifest Format (N01 Extension)

Every N01 handoff includes:

```yaml
source_manifest:
  - id: src_001
    url_or_path: "{{source_url_or_path}}"
    type: peer_reviewed | primary_data | official_doc | reputable_press
    reliability: 0.0-1.0
    retrieved: "{{YYYY-MM-DD}}"
    used_for: ["{{claim_or_section_id}}"]
  - id: src_002
    ...
confidence_summary:
  overall: 0.0-1.0
  by_section:
    executive_summary: 0.0-1.0
    findings: 0.0-1.0
    recommendations: 0.0-1.0
low_confidence_flags:
  - section: "{{section_id}}"
    reason: "{{why_confidence_is_low}}"
    action: "verify before acting | accept with caveat | do not propagate"
```

## Deviation from N00

N00 handoff is a task-routing artifact. N01 handoff is an **intelligence transfer
protocol**: it packages findings WITH their epistemic status so downstream nuclei
can make trust-calibrated decisions.

## Links

- N00 archetype: [[N00_genesis/P12_orchestration/kind_handoff]]
- N00 KC: [[N00_genesis/P01_knowledge/library/kind/kc_handoff]]
- Related: [[N01_intelligence/P12_orchestration/dispatch_rule_intelligence]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_nd_n00.md]] | upstream | 0.34 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.29 |
| [[p12_wf_intelligence_pipeline]] | related | 0.29 |
| [[spec_n01_n04_verticalization]] | upstream | 0.28 |
| [[n01_dr_research_pipeline]] | related | 0.27 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.27 |
| [[n01_dr_intelligence]] | related | 0.27 |
| [[p03_sp_n01_intelligence]] | upstream | 0.25 |
| [[dispatch]] | upstream | 0.24 |
| [[p01_ctx_cex_project]] | upstream | 0.24 |
