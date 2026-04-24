---
id: p07_sr_visual_frontend_marketing
kind: scoring_rubric
8f: F7_govern
pillar: P07
title: "Rubric: Visual Frontend + Marketing Quality"
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n02_visual_frontend_marketing
framework: Dual-Role Evaluation (Visual Engineering + Conversion Copy)
target_kinds: [html_page, landing_page, component, email_template, ad_copy, social_post, visual_report]
dimensions_count: 10
total_weight: 100
threshold_golden: 9.5
threshold_publish_visual: 9.0
threshold_publish_copy: 8.0
threshold_publish_dual: 8.5
threshold_review: 7.0
automation_status: semi-automated
domain: visual_frontend_engineering_and_copywriting
quality: 9.2
tags: [scoring_rubric, visual-frontend, marketing, html, tailwind, copy, N02, P07]
tldr: 10-dimension dual rubric — 5 visual dimensions (performance, a11y, responsive, design tokens, UX) + 5 copy dimensions (hook, conversion, readability, brand, A/B)
density_score: 0.96
calibration_set: [golden_landing_page_dual_01, golden_component_visual_01, golden_ad_copy_01]
inter_rater_agreement: 0.88
appeals_process: Submit to N07 with competing score rationale and specific evidence.
linked_artifacts:
  primary: p11_qg_visual_frontend_marketing
  related: [p02_agent_visual_frontend_marketing, p03_sp_visual_frontend_marketing]
related:
  - p03_ap_visual_frontend_marketing
  - p08_ac_visual_frontend_marketing
  - p02_agent_visual_frontend_marketing
  - p11_qg_visual_frontend_marketing
  - p12_dr_visual_frontend_marketing
  - p12_wf_visual_frontend_marketing
  - p03_sp_visual_frontend_marketing
  - p03_pt_visual_frontend_marketing
  - n02_tool_copy_analyzer
  - p03_brand_audit_prompt
---

# Rubric: Visual Frontend + Marketing Quality

## Purpose

Evaluate dual-role N02 output across 10 dimensions (5 visual + 5 copy).
Different scoring applies based on mode:
- **VISUAL MODE**: Score visual dimensions only
- **COPY MODE**: Score copy dimensions only  
- **DUAL MODE**: Score all 10 dimensions

## Visual Dimensions (VISUAL and DUAL modes)

| Dimension | Weight | Scale | Score 10 | Score 5 | Score 0 |
|-----------|--------|-------|----------|---------|---------|
| **Performance & Technical** | 25% | 0–10 | Lighthouse 95+, W3C valid, 0 console errors, optimal loading | Lighthouse 90-94, minor validation issues | Lighthouse < 90, significant technical problems |
| **Accessibility & Usability** | 20% | 0–10 | WCAG AAA, perfect keyboard navigation, screen reader optimized | WCAG AA compliant, good usability | Poor a11y, non-accessible interactions |
| **Responsive Design** | 20% | 0–10 | Flawless across all devices, mobile-first, touch-optimized | Works on mobile/desktop, minor issues | Breaks on mobile or small screens |
| **Design Token Consistency** | 15% | 0–10 | Perfect token usage, zero hardcoded values, consistent spacing/colors | Mostly tokens, 1-2 hardcoded values | Multiple hardcoded colors, inconsistent spacing |
| **Visual Hierarchy & UX** | 20% | 0–10 | Clear F/Z-pattern, proper typography scale, intuitive navigation | Good hierarchy, minor flow issues | Confusing layout, poor visual flow |

## Copy Dimensions (COPY and DUAL modes)

| Dimension | Weight | Scale | Score 10 | Score 5 | Score 0 |
|-----------|--------|-------|----------|---------|---------|
| **Hook Strength** | 30% | 0–10 | First 10 words create irresistible curiosity, tension, or desire; reader cannot stop | Hook is present but predictable; mild interest only | No hook; copy starts with "We are..." or product name |
| **Conversion Clarity** | 25% | 0–10 | Single CTA is specific, benefit-first, zero friction; reader knows exactly what happens next | CTA present but generic ("Learn more"); benefit implied not stated | No CTA, or multiple conflicting CTAs that dilute focus |
| **Readability** | 20% | 0–10 | Flesch >= 65, avg sentence <= 15 words, zero passive voice, zero jargon without explanation | Flesch 50–64, occasional long sentences, 1–2 jargon terms | Flesch < 50, dense paragraphs, heavy jargon, no skimmability |
| **Brand Voice Fit** | 15% | 0–10 | Copy is indistinguishable from brand's own voice; correct tone, vocabulary, persona | Copy is neutral/generic; not wrong but not distinctly brand | Copy clashes with brand tone; too formal, too casual, or off-persona |
| **A/B Coverage** | 10% | 0–10 | >= 3 headline variants + >= 2 CTA variants; variants are meaningfully different (not just synonyms) | 2 variants present but barely differentiated | No variants; one version of everything |

## Scoring Examples

### VISUAL Mode Example
```
Performance & Technical:     9.2 × 0.25 = 2.30
Accessibility & Usability:   8.8 × 0.20 = 1.76
Responsive Design:           9.5 × 0.20 = 1.90
Design Token Consistency:    8.0 × 0.15 = 1.20
Visual Hierarchy & UX:       9.0 × 0.20 = 1.80
                                     -------
                           TOTAL =   8.96 → PUBLISH tier (>= 9.0)
```

### COPY Mode Example
```
Hook Strength:      8.5 × 0.30 = 2.55
Conversion Clarity: 9.0 × 0.25 = 2.25
Readability:        8.0 × 0.20 = 1.60
Brand Voice Fit:    7.5 × 0.15 = 1.13
A/B Coverage:       9.0 × 0.10 = 0.90
                              ------
                    TOTAL =   8.43 → PUBLISH tier (>= 8.0)
```

### DUAL Mode Example (all 10 dimensions)
```
VISUAL DIMENSIONS (50% weight):
  Performance: 9.0 × 0.125 = 1.13
  A11y: 8.8 × 0.10 = 0.88
  Responsive: 9.2 × 0.10 = 0.92
  Tokens: 8.5 × 0.075 = 0.64
  UX: 9.0 × 0.10 = 0.90
  
COPY DIMENSIONS (50% weight):
  Hook: 8.5 × 0.15 = 1.28
  Conversion: 9.0 × 0.125 = 1.13
  Readability: 8.0 × 0.10 = 0.80
  Brand Voice: 7.5 × 0.075 = 0.56
  A/B Coverage: 9.0 × 0.05 = 0.45
                        -------
              TOTAL =   8.69 → PUBLISH tier (>= 8.5)
```

## Tier Thresholds

### VISUAL Mode
| Tier | Score | Lighthouse | Action |
|------|-------|------------|--------|
| GOLDEN | >= 9.5 | >= 95 | Save as canonical example in `N02_marketing/P05_output/examples/` |
| PUBLISH | >= 9.0 | >= 90 | Deploy to production, approve for client delivery |
| REVIEW | >= 7.0 | >= 85 | Return with specific visual dimension feedback |
| REJECT | < 7.0 | < 85 | Full visual redesign required |

### COPY Mode  
| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Save as canonical copy example |
| PUBLISH | >= 8.0 | Deliver to client or deploy to campaign |
| REVIEW | >= 7.0 | Return with specific copy dimension feedback |
| REJECT | < 7.0 | Full rewrite — restart from audience research, change formula |

### DUAL Mode
| Tier | Score | Lighthouse | Action |
|------|-------|------------|--------|
| GOLDEN | >= 9.5 | >= 95 | Save as golden integrated example (copy + visual) |
| PUBLISH | >= 8.5 | >= 90 | Deploy integrated solution |
| REVIEW | >= 7.0 | >= 85 | Return with both visual AND copy feedback |
| REJECT | < 7.0 | < 85 | Restart integration from F4 (both dimensions) |

## Calibration

### VISUAL Mode Calibration
- **GOLDEN**: Lighthouse 95+, flawless accessibility, perfect responsive behavior, zero hardcoded values, intuitive UX that guides users effortlessly
- **PUBLISH**: Lighthouse 90+, WCAG AA compliant, mobile-responsive, consistent design tokens, clear visual hierarchy
- **REVIEW**: Lighthouse 85+, basic accessibility, mostly responsive, some hardcoded values, adequate UX
- **REJECT**: Poor performance, broken on mobile, accessibility issues, inconsistent styling, confusing layout

### COPY Mode Calibration  
- **GOLDEN**: Hook creates genuine tension; CTA so specific it answers "what exactly do I get?"; reads at 7th-grade level; sounds exactly like the brand; 3+ meaningfully different A/B variants
- **PUBLISH**: Strong hook; clear CTA with benefit; readable; brand voice mostly correct; 3 variants present
- **REVIEW**: Hook is generic; CTA is adequate; readable but some jargon; neutral voice; variants are near-duplicates
- **REJECT**: No hook; CTA is "click here"; hard to read; off-brand; single version with no variants

### DUAL Mode Calibration
- **GOLDEN**: Both visual and copy dimensions score GOLDEN; copy enhances visual flow, visual hierarchy supports persuasion perfectly
- **PUBLISH**: Both dimensions meet PUBLISH threshold; good integration between copy placement and visual design
- **REVIEW**: One dimension strong, other adequate; integration needs improvement
- **REJECT**: Both dimensions weak; copy and visual fight each other instead of working together

## Automation Status

### Visual Dimensions
| Dimension | Automation | Tool |
|-----------|-----------|------|
| Performance & Technical | Automated | Lighthouse CLI, W3C validator |
| Accessibility & Usability | Semi-auto | Lighthouse a11y, manual keyboard testing |
| Responsive Design | Semi-auto | Browser dev tools, manual testing |
| Design Token Consistency | Automated | Tailwind audit, hex color detection |
| Visual Hierarchy & UX | Manual | Human design review |

### Copy Dimensions  
| Dimension | Automation | Tool |
|-----------|-----------|------|
| Hook Strength | Manual | Human reviewer or LLM self-critique |
| Conversion Clarity | Semi-auto | CTA pattern checker in quality gate |
| Readability | Automated | `readability.py` (Flesch-Kincaid) |
| Brand Voice Fit | Manual (if card exists) | `sentiment_check.py` for tone proxy |
| A/B Coverage | Automated | Count variants in output file |

## Revision Instructions by Dimension

### Visual Revision Actions (scores < 7)
| Dimension | Revision Action |
|-----------|----------------|
| Performance & Technical | Optimize images, minify CSS, fix console errors, validate HTML |
| Accessibility & Usability | Add alt tags, improve contrast ratios, fix keyboard navigation, add ARIA labels |
| Responsive Design | Fix mobile breakpoints, optimize touch targets, test on real devices |
| Design Token Consistency | Replace hardcoded colors with Tailwind utilities, use consistent spacing scale |
| Visual Hierarchy & UX | Restructure layout for F/Z-pattern, improve heading hierarchy, clarify navigation |

### Copy Revision Actions (scores < 7)
| Dimension | Revision Action |
|-----------|----------------|
| Hook Strength | Rewrite opening with question, bold stat, or "If you..." opener. Apply 4U formula. |
| Conversion Clarity | Replace generic CTA. Template: "[Verb] my [specific benefit] [optional: in X minutes]" |
| Readability | Break sentences at 15 words. Replace jargon. Use active voice. |
| Brand Voice Fit | Re-read brand voice card. Replace 3 words that feel off-brand. |
| A/B Coverage | Generate 2 more headline variants using different formulas (AIDA vs PAS). |

### DUAL Mode Integration Issues
| Issue | Fix |
|-------|-----|
| Copy not in visual hierarchy | Place headlines in proper h1-h6 tags, not styled divs |
| CTAs not styled components | Convert text CTAs to button elements with hover states |
| Visual fights copy formula | Align layout flow with PAS/AIDA structure |

## Dimension Weight Rationale

### Visual Mode Weights
- **Performance & Technical (25%)**: Poor performance kills user experience; Lighthouse < 90 correlates with 53% bounce rate increase.
- **Accessibility & Usability (20%)**: Legal requirement + 15% of users need a11y features; WCAG violations block deployments.
- **Responsive Design (20%)**: 60%+ traffic is mobile; broken mobile = lost conversions.
- **Design Token Consistency (15%)**: Inconsistent styling looks unprofessional; hardcoded values break design systems.
- **Visual Hierarchy & UX (20%)**: Poor UX confuses users; clear hierarchy increases conversion 25%+.

### Copy Mode Weights  
- **Hook (30%)**: If the hook fails, no one reads the rest — highest weight.
- **Conversion Clarity (25%)**: The CTA is the conversion moment; vague CTAs lose 20–30% clicks.
- **Readability (20%)**: Dense copy loses mobile readers; Flesch < 50 correlates with 40% drop in scroll depth.
- **Brand Voice (15%)**: Voice mismatches erode trust; weight lower than conversion because neutral voice still converts.
- **A/B Coverage (10%)**: Variants enable testing; weight lowest because quality of variants matters more than count.

### DUAL Mode Weight Distribution
- **50% Visual** + **50% Copy** ensures both dimensions are equally critical for integrated success.

## Peer Review Protocol

### VISUAL Mode Review
1. Reviewer opens deliverable in browser (no context from requester)
2. Tests responsive behavior manually (resize window, mobile view)
3. Runs Lighthouse audit and notes scores
4. Checks accessibility with keyboard navigation
5. Validates HTML with W3C validator
6. Scores each visual dimension independently
7. Notes top 1 visual fix if score < 9.0

### COPY Mode Review
1. Scorer reads deliverable cold (no context from requester)
2. Scores each copy dimension independently
3. Writes 1-sentence rationale per dimension
4. Flags any [PROOF NEEDED] or [STAT NEEDED] placeholders found
5. Notes top 1 copy revision if score < 8.0

### DUAL Mode Review
1. Complete both visual and copy review protocols above
2. Additionally assess copy-visual integration quality
3. Check that headlines use proper semantic tags (not just styling)
4. Verify CTAs are button components, not text links
5. Confirm visual hierarchy supports copy formula flow
6. Apply final score: `quality: {score}` (NEVER self-applied by N02)

### Universal Rules
- **Quality field**: NEVER self-applied by N02, always peer-assigned
- **Evidence requirement**: Each dimension score needs specific evidence/rationale
- **Mode declaration**: Reviewer must identify mode (VISUAL/COPY/DUAL) before scoring

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ap_visual_frontend_marketing]] | upstream | 0.51 |
| [[p08_ac_visual_frontend_marketing]] | downstream | 0.50 |
| [[p02_agent_visual_frontend_marketing]] | upstream | 0.48 |
| [[p11_qg_visual_frontend_marketing]] | downstream | 0.47 |
| [[p12_dr_visual_frontend_marketing]] | downstream | 0.43 |
| [[p12_wf_visual_frontend_marketing]] | downstream | 0.43 |
| [[p03_sp_visual_frontend_marketing]] | upstream | 0.42 |
| [[p03_pt_visual_frontend_marketing]] | upstream | 0.36 |
| [[n02_tool_copy_analyzer]] | upstream | 0.33 |
| [[p03_brand_audit_prompt]] | upstream | 0.31 |
