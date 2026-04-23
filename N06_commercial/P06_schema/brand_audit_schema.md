---
id: n06_schema_brand_audit
kind: constraint_spec
pillar: P06
title: "Brand Audit Schema — 6-Dimension Consistency Scoring"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-audit-validation
quality: 9.1
updated: 2026-04-07
tags: [schema, brand, audit, scoring, consistency, n06]
tldr: "Defines 6 audit dimensions with weights: archetype (0.25), voice (0.20), visual (0.20), positioning (0.15), narrative (0.10), config (0.10). Pass = 0.85. Tool: brand_audit.py."
density_score: 0.93
axioms:
  - "Weights sum to 1.0 exactly. Pass threshold is 0.85. Below 0.70 = critical brand misalignment."
  - "ALWAYS run brand_audit.py after propagation — never trust manual assessment alone."
linked_artifacts:
  primary: p03_brand_audit_prompt
  related: [n06_schema_brand_voice_contract, n06_schema_brand_config, p07_qg_commercial]
related:
  - p03_brand_audit_prompt
  - p03_sp_brand_nucleus
  - p02_agent_brand_nucleus
  - p07_sr_commercial
  - spec_n06_brand_verticalization
  - spec_n06_part2
  - p07_sr_visual_frontend_marketing
  - p03_sp_commercial_nucleus
  - p02_agent_commercial_nucleus
  - p12_wf_commercial
---

# Brand Audit Schema

## Dimensions & Weights

| # | Dimension | Weight | What It Measures |
|---|-----------|--------|------------------|
| 1 | Archetype Alignment | 0.25 | Copy tone, visual style, narrative voice match archetype |
| 2 | Voice Consistency | 0.20 | 5D scores consistent across channels (±1 tolerance) |
| 3 | Visual Coherence | 0.20 | Colors, fonts, contrast consistent across all output |
| 4 | Positioning Clarity | 0.15 | UVP, category, differentiator consistent and unique |
| 5 | Narrative Integrity | 0.10 | Story, mission, vision, transformation arc coherent |
| 6 | Config Completeness | 0.10 | All 13 required fields filled with real values |

## Scoring Formula

```
overall = (archetype × 0.25) + (voice × 0.20) + (visual × 0.20)
        + (positioning × 0.15) + (narrative × 0.10) + (config × 0.10)
```

## Rating Scale

| Score | Rating | Action |
|-------|--------|--------|
| 0.95+ | Excellent | No action needed. Brand is coherent. |
| 0.85-0.94 | Healthy | Minor polish recommended. Review weak dimensions. |
| 0.70-0.84 | Needs Work | Revise weak dimensions. Re-calibrate voice or positioning. |
| < 0.70 | Critical | Re-run Brand Discovery interview. Fundamental gaps. |

## Audit Output Format

```yaml
brand_audit:
  brand: "{{BRAND_NAME}}"
  date: "YYYY-MM-DD"
  overall_score: 0.XXX
  rating: "Excellent|Healthy|Needs Work|Critical"
  dimensions:
    archetype_alignment:
      score: 0.XX
      weight: 0.25
      issues: []
    voice_consistency:
      score: 0.XX
      weight: 0.20
      issues: []
    visual_coherence:
      score: 0.XX
      weight: 0.20
      issues: []
    positioning_clarity:
      score: 0.XX
      weight: 0.15
      issues: []
    narrative_integrity:
      score: 0.XX
      weight: 0.10
      issues: []
    config_completeness:
      score: 0.XX
      weight: 0.10
      issues: []
  recommendations:
    - "Action item 1"
    - "Action item 2"
  files_scanned: 42
  brand_references_found: 156
```

## When to Run

| Trigger | Scope |
|---------|-------|
| After Brand Discovery complete | Full audit |
| After brand_config.yaml update | Config + affected dimensions |
| Before handoff to other nuclei | Full audit (must pass 0.85) |
| Weekly brand health check | Full audit |
| After major content batch | Voice + archetype dimensions |

## Tool

```bash
python _tools/brand_audit.py                    # full audit, human-readable
python _tools/brand_audit.py --json             # machine-readable
python _tools/brand_audit.py --verbose          # show all issues
python _tools/brand_audit.py --config path.yaml # custom config
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_brand_audit_prompt]] | upstream | 0.63 |
| [[p03_sp_brand_nucleus]] | upstream | 0.33 |
| [[p02_agent_brand_nucleus]] | upstream | 0.30 |
| [[p07_sr_commercial]] | downstream | 0.29 |
| [[spec_n06_brand_verticalization]] | sibling | 0.28 |
| [[spec_n06_part2]] | sibling | 0.27 |
| [[p07_sr_visual_frontend_marketing]] | downstream | 0.27 |
| [[p03_sp_commercial_nucleus]] | upstream | 0.27 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.26 |
| [[p12_wf_commercial]] | downstream | 0.26 |
