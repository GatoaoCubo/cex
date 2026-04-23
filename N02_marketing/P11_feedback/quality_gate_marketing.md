---
id: p11_qg_visual_frontend_marketing
kind: quality_gate
pillar: P11
title: "Gate: Visual Frontend + Marketing Quality"
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n02_visual_frontend_marketing
domain: visual_frontend_engineering_and_copywriting
quality: 8.8
tags: [quality_gate, visual-frontend, marketing, html, tailwind, copy, N02, P11]
tldr: 15 HARD gates (visual + copy + universal) + 8 SOFT dimensions for dual-role N02 — visual threshold Lighthouse 90+, copy threshold 8.0
density_score: 0.96
related:
  - p07_sr_visual_frontend_marketing
  - p03_ap_visual_frontend_marketing
  - p08_ac_visual_frontend_marketing
  - p02_agent_visual_frontend_marketing
  - p03_sp_visual_frontend_marketing
  - p12_wf_visual_frontend_marketing
  - p12_dr_visual_frontend_marketing
  - p03_pt_visual_frontend_marketing
  - spec_n02_visual_frontend_engineer
  - n02_tool_copy_analyzer
---

# Gate: Visual Frontend + Marketing Quality

## Purpose

Validates that dual-role N02 output meets production standards before delivery.
Applies to:
- **VISUAL MODE**: HTML/CSS components, landing pages, responsive designs
- **COPY MODE**: Ads, emails, headlines, campaign briefs  
- **DUAL MODE**: Integrated pages with copy embedded in visual hierarchy

## Hard Gates (BLOCK if fail)

### Visual Mode Hard Gates (applies to VISUAL and DUAL)

| gate_id | Description | Threshold | Validation Method |
|---------|-------------|-----------|------------------|
| V01 | Lighthouse Performance Score | >= 90 | `lighthouse --only=performance` |
| V02 | WCAG AA Accessibility Compliance | >= 95 score | `lighthouse --only=accessibility` |
| V03 | W3C HTML Validation | 0 errors | W3C HTML validator |
| V04 | Color Contrast Ratio | >= 4.5:1 | Color contrast analyzer |
| V05 | Zero Hardcoded Hex Colors | 0 #HEXCODE | Tailwind token audit |
| V06 | Responsive Design Functional | All breakpoints work | Browser dev tools test |
| V07 | F/Z-Pattern Layout | Visual hierarchy correct | Manual design review |
| V08 | Font Pairing Compliance | Max 3 font families | Typography system check |
| V09 | Semantic HTML5 Structure | Proper elements used | HTML5 semantic validation |

### Copy Mode Hard Gates (applies to COPY and DUAL)

| gate_id | Description | Threshold | Validation Method |
|---------|-------------|-----------|------------------|
| C01 | Funnel stage declared | present | Text search for "funnel_stage" |
| C02 | CTA present and specific | not "Click here" / "Learn more" | CTA pattern matching |
| C03 | A/B headline variants | min 3 variants | Count V1, V2, V3 labels |
| C04 | No unverified superlatives | [PROOF NEEDED] tagged | Superlative detection |
| C05 | Hook in first 10 words | curiosity/urgency present | First sentence analysis |

### Universal Hard Gates (all modes)

| gate_id | Description | Threshold | Validation Method |
|---------|-------------|-----------|------------------|
| U01 | Frontmatter parses without YAML error | N/A | YAML parser |
| U02 | ID matches pattern for artifact kind | kind-specific | Regex pattern match |
| U03 | Quality field is null (no self-score) | quality: null | Frontmatter check |
| U04 | Artifact size within limit | <= 16384 bytes | File size check |

## Soft Gates (SCORE penalties)

### Visual Mode Soft Gates (VISUAL and DUAL)

| gate_id | Description | Max Penalty | Weight |
|---------|-------------|-------------|--------|
| SV01 | Design Token Usage — consistent spacing, colors, typography | -1.5 | 15% |
| SV02 | Dark Mode Quality — proper contrast and readability | -1.0 | 10% |
| SV03 | Mobile-First Approach — optimized for mobile experience | -1.5 | 15% |
| SV04 | Component Reusability — follows shadcn/ui patterns | -1.0 | 10% |

### Copy Mode Soft Gates (COPY and DUAL)

| gate_id | Description | Max Penalty | Weight |
|---------|-------------|-------------|--------|
| SC01 | Hook Quality — first 10 words create curiosity or tension | -2.0 | 15% |
| SC02 | CTA Specificity — names benefit AND action | -1.5 | 15% |
| SC03 | Readability — Flesch-Kincaid >= 60 B2C, >= 40 B2B | -1.5 | 10% |
| SC04 | Brand Voice Alignment — matches provided voice card | -2.0 | 10% |

### DUAL Mode Integration Quality

| gate_id | Description | Max Penalty | Weight |
|---------|-------------|-------------|--------|
| SD01 | Copy-Visual Hierarchy — headlines in proper h1-h6 tags | -1.5 | 10% |
| SD02 | CTA Button Implementation — CTAs as styled components | -1.0 | 5% |
| SD03 | Visual Flow Supports Copy — F/Z-pattern enhances persuasion | -2.0 | 15% |

## Scoring Formula

### VISUAL Mode
```
hard_gates = V01-V09 + U01-U04 (13 gates total)
soft_score = SUM(SV01-SV04 * weight) (0–10 scale)
final_score = soft_score
PASS = all HARD gates pass AND final_score >= 9.0 AND Lighthouse >= 90
```

### COPY Mode  
```
hard_gates = C01-C05 + U01-U04 (9 gates total)
soft_score = SUM(SC01-SC04 * weight) (0–10 scale)
final_score = soft_score
PASS = all HARD gates pass AND final_score >= 8.0
```

### DUAL Mode
```
hard_gates = V01-V09 + C01-C05 + U01-U04 (17 gates total)
soft_score = SUM(SV01-SV04 + SC01-SC04 + SD01-SD03) * weight (0–10 scale)
final_score = soft_score
PASS = all HARD gates pass AND final_score >= 8.5 AND Lighthouse >= 90
```

## Tier Thresholds

### VISUAL Mode
| Tier | Score | Lighthouse | Action |
|------|-------|------------|--------|
| GOLDEN | >= 9.5 | >= 95 | Save as example in N02_marketing/P05_output/examples/ |
| PUBLISH | >= 9.0 | >= 90 | Approve for production deployment |
| REVIEW | >= 8.0 | >= 85 | Return to F6 with specific visual feedback |
| REJECT | < 8.0 | < 85 | Full visual redesign required |

### COPY Mode
| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Save as example in N02_marketing/P05_output/examples/ |
| PUBLISH | >= 8.0 | Approve for delivery to client/campaign |
| REVIEW | >= 7.0 | Return to F6 with specific copy feedback |
| REJECT | < 7.0 | Full rewrite — restart F4 with new formula |

### DUAL Mode
| Tier | Score | Lighthouse | Action |
|------|-------|------------|--------|
| GOLDEN | >= 9.5 | >= 95 | Save as golden example (copy + visual) |
| PUBLISH | >= 8.5 | >= 90 | Approve for integrated deployment |
| REVIEW | >= 7.5 | >= 85 | Return with dual feedback (copy AND visual) |
| REJECT | < 7.5 | < 85 | Restart integration from F4 |

## Bypass Policy

- **Who may override**: n07-orchestrator only
- **Conditions**: score between 7.5–8.0 AND explicit human approval AND urgent deadline
- **Audit requirement**: note bypass in commit message `[BYPASS score=7.x reason=...]`

## Quick Validation Scripts

### VISUAL Mode Validation
```python
def validate_n02_visual(html_content, frontmatter):
    import subprocess
    
    visual_gates = {
        "V01": lighthouse_performance_score(html_content) >= 90,
        "V02": lighthouse_accessibility_score(html_content) >= 95, 
        "V03": w3c_html_validate(html_content) == 0,  # 0 errors
        "V04": check_contrast_ratios(html_content) >= 4.5,
        "V05": count_hardcoded_hex(html_content) == 0,
        "V06": test_responsive_breakpoints(html_content),
        "V07": validate_visual_hierarchy(html_content),
        "V08": count_font_families(html_content) <= 3,
        "V09": validate_semantic_html5(html_content),
    }
    universal_gates = validate_universal(frontmatter, html_content)
    
    return all(visual_gates.values()) and all(universal_gates.values()), {**visual_gates, **universal_gates}
```

### COPY Mode Validation  
```python
def validate_n02_copy(copy_text, frontmatter):
    copy_gates = {
        "C01": funnel_stage_declared(copy_text),
        "C02": has_specific_cta(copy_text),
        "C03": count_headline_variants(copy_text) >= 3,
        "C04": no_unmarked_superlatives(copy_text),
        "C05": has_strong_hook(copy_text),
    }
    universal_gates = validate_universal(frontmatter, copy_text)
    
    return all(copy_gates.values()) and all(universal_gates.values()), {**copy_gates, **universal_gates}
```

### Universal Gates
```python
def validate_universal(frontmatter, content):
    return {
        "U01": is_valid_yaml(frontmatter),
        "U02": id_matches_kind_pattern(frontmatter),
        "U03": frontmatter.get("quality") is None,
        "U04": len(content.encode()) <= 16384,
    }
```

## Audit Trail

Each evaluation logs:
- Gate ID and result (pass/fail)
- Specific failing criterion
- Timestamp (UTC)
- Score by dimension
- Revision instructions for S-gate failures

Retention: logs kept in `N02_marketing/P05_output/` per mission.

## Common Failure Patterns

### Visual Mode Failures
| Failure | Gate | Most Common Cause | Fix |
|---------|------|------------------|-----|
| Lighthouse < 90 | V01 | Large images, no optimization | Optimize images, lazy loading |
| Accessibility < 95 | V02 | Missing alt tags, poor contrast | Add ARIA labels, check contrast |
| W3C validation errors | V03 | Invalid nesting, missing lang | Fix HTML structure, add required attributes |
| Poor contrast | V04 | Light text on light background | Use Tailwind contrast utilities |
| Hardcoded #colors | V05 | Direct hex codes used | Replace with Tailwind color tokens |
| Non-responsive | V06 | Fixed widths, no breakpoints | Add responsive utility classes |
| Poor visual hierarchy | V07 | No clear F/Z-pattern | Restructure layout, proper heading order |
| Too many fonts | V08 | > 3 font families | Stick to Geist + Inter + JetBrains Mono |
| Non-semantic HTML | V09 | Divs instead of proper elements | Use header, main, section, article tags |

### Copy Mode Failures
| Failure | Gate | Most Common Cause | Fix |
|---------|------|------------------|-----|
| No funnel stage | C01 | Stage not declared | Add funnel_stage line to output header |
| Generic CTA | C02 | "Click here" / "Learn more" used | Rewrite: "[Verb] my [benefit]" |
| Only 1 headline | C03 | Single variant produced | Generate 3 variants minimum (V1, V2, V3) |
| Superlative without proof | C04 | "Best" / "The only" used | Add [PROOF NEEDED] or specific claim |
| Weak hook | C05 | Boring opening | Create curiosity/urgency in first 10 words |

### Universal Failures
| Failure | Gate | Most Common Cause | Fix |
|---------|------|------------------|-----|
| quality: 8.x set | U03 | Self-scoring after generation | Set `quality: null` always |
| Invalid YAML | U01 | Syntax error in frontmatter | Fix YAML formatting |
| Wrong ID pattern | U02 | ID doesn't match kind | Follow kind naming convention |
| File too large | U04 | Excessive content | Break into smaller components |

### DUAL Mode Integration Failures
| Failure | Gate | Most Common Cause | Fix |
|---------|------|------------------|-----|
| Copy not in hierarchy | SD01 | Headlines as styled divs | Use h1-h6 tags with Tailwind styling |
| CTAs not components | SD02 | CTAs as plain text links | Convert to button elements |
| Visual fights copy | SD03 | Layout doesn't support persuasion | Align visual flow with copy formula |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_sr_visual_frontend_marketing]] | upstream | 0.55 |
| [[p03_ap_visual_frontend_marketing]] | upstream | 0.55 |
| [[p08_ac_visual_frontend_marketing]] | upstream | 0.55 |
| [[p02_agent_visual_frontend_marketing]] | upstream | 0.50 |
| [[p03_sp_visual_frontend_marketing]] | upstream | 0.48 |
| [[p12_wf_visual_frontend_marketing]] | downstream | 0.48 |
| [[p12_dr_visual_frontend_marketing]] | downstream | 0.46 |
| [[p03_pt_visual_frontend_marketing]] | upstream | 0.44 |
| [[spec_n02_visual_frontend_engineer]] | upstream | 0.29 |
| [[n02_tool_copy_analyzer]] | upstream | 0.26 |
