---
id: p03_brand_audit_prompt
kind: prompt_template
pillar: P03
title: "Brand Audit — Consistency Scoring Across Artifacts"
version: 1.0.0
created: 2026-04-01
author: n06_commercial
domain: brand-audit
quality: 9.1
updated: 2026-04-07
tags: [prompt, brand, audit, consistency, n06]
tldr: "Scores brand consistency across 6 dimensions: archetype alignment (0.25), voice consistency (0.20), visual coherence (0.20), positioning clarity (0.15), narrative integrity (0.10), config completeness (0.10). Pass = 0.85."
density_score: 0.93
axioms:
  - "ALWAYS run after brand propagation — audit measures coherence AFTER distribution."
  - "Pass = 0.85. Below 0.70 requires full brand re-alignment."
linked_artifacts:
  primary: n06_schema_brand_audit
  related: [n06_output_brand_config, p01_kc_brand_voice_systems, p07_qg_commercial]
---

# Brand Audit Prompt

## Purpose
Score brand consistency across all CEX artifacts that reference brand_config.yaml.
Run after brand propagation to verify coherence.

## Audit Dimensions (weighted)

### 1. Archetype Alignment — Weight: 0.25
Check all artifacts that reference BRAND_ARCHETYPE:
- Does copy tone match archetype personality? (e.g., "sage" = educational, measured)
- Does visual style match archetype aesthetic? (e.g., "rebel" = bold, dark, angular)
- Does narrative voice match archetype voice? (e.g., "caregiver" = warm, supportive)
- Score: 0.0 (no alignment) to 1.0 (perfect alignment)

### 2. Voice Consistency — Weight: 0.20
Check all artifacts that use BRAND_VOICE_*:
- Are 5D scores (formality, enthusiasm, humor, warmth, authority) consistent?
- Is tone within ±1 tolerance across channels? (social = -1 formality, docs = +1 formality)
- Do Do's and Don'ts align with actual output?
- Score: 0.0 to 1.0

### 3. Visual Coherence — Weight: 0.20
Check all artifacts that reference BRAND_COLORS, BRAND_FONTS:
- Are colors consistent (same HEX values throughout)?
- Do font pairings match brand_config specification?
- Does contrast ratio meet WCAG 4.5:1?
- Is dark mode variant coherent with light mode?
- Score: 0.0 to 1.0

### 4. Positioning Clarity — Weight: 0.15
Check all artifacts that reference BRAND_UVP, BRAND_CATEGORY:
- Is UVP stated consistently (no contradictions)?
- Is category ownership clear and unique?
- Does differentiator hold up against BRAND_COMPETITORS?
- Score: 0.0 to 1.0

### 5. Narrative Integrity — Weight: 0.10
Check all artifacts that reference BRAND_STORY, BRAND_MISSION, BRAND_VISION:
- Is origin story consistent across mentions?
- Do mission and vision support each other (present vs. future)?
- Does transformation arc appear correctly (From/To/Through)?
- Score: 0.0 to 1.0

### 6. Config Completeness — Weight: 0.10
Check brand_config.yaml itself:
- Are all 13 required fields filled with non-placeholder values?
- Are optional fields populated where data exists?
- Are enum values valid (archetype, pricing_model)?
- Are format constraints met (HEX colors, language code)?
- Score: 0.0 to 1.0

## Scoring

```
final_score = (archetype * 0.25) + (voice * 0.20) + (visual * 0.20)
            + (positioning * 0.15) + (narrative * 0.10) + (config * 0.10)
```

| Range | Rating | Action |
|-------|--------|--------|
| 0.95+ | Excellent | No action needed |
| 0.85-0.94 | Healthy | Minor polish recommended |
| 0.70-0.84 | Needs Work | Revise weak dimensions |
| < 0.70 | Critical | Re-run Brand Discovery |

## Output Format
```yaml
brand_audit:
  brand: "{{BRAND_NAME}}"
  date: "{{DATE}}"
  overall_score: 0.XX
  rating: "Excellent|Healthy|Needs Work|Critical"
  dimensions:
    archetype_alignment: { score: 0.XX, issues: [] }
    voice_consistency: { score: 0.XX, issues: [] }
    visual_coherence: { score: 0.XX, issues: [] }
    positioning_clarity: { score: 0.XX, issues: [] }
    narrative_integrity: { score: 0.XX, issues: [] }
    config_completeness: { score: 0.XX, issues: [] }
  recommendations: []
```
