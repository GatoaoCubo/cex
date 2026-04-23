---
id: e2e_gold_quality_rubric
kind: golden_test
type: rubric
pillar: P01
title: "Quality Rubric — E2E Gold Standard Evaluation"
version: 1.0.0
created: 2026-04-06
author: n02_marketing
quality: 9.0
tags: [e2e, gold-standard, rubric, quality, marketing, stress-test]
density_score: 0.97
---

# Quality Rubric — E2E Gold Standards

> Machine-parseable evaluation criteria for all 3 stress test scenarios.
> Each criterion is PASS/FAIL — no partial credit. Gold standards are binary.

---

## S1: Pet Shop CRM (`petshop_marketing.md`)

### MUST-HAVE (all 5 = PASS, miss 1 = FAIL)

```yaml
s1_must_have:
  M1_headline_exists:
    check: "Landing page has a headline under 60 characters"
    grep: "### Headline"
    fail_if: "section missing or headline > 60 chars"

  M2_three_benefits:
    check: "Exactly 3 benefit blocks with title + body"
    grep: "### Benefit [1-3]"
    fail_if: "fewer than 3 or any benefit has no body text"

  M3_cta_present:
    check: "Primary CTA exists with action verb + friction remover"
    grep: "### CTA"
    fail_if: "no CTA or CTA lacks action verb (teste, comece, experimente)"

  M4_pricing_three_tiers:
    check: "Pricing table has exactly 3 tiers with different prices"
    grep: "Starter.*Pro.*Premium"
    fail_if: "fewer than 3 tiers or prices are identical"

  M5_five_taglines:
    check: "5 tagline variations, each targeting different angle"
    grep: "Tagline"
    fail_if: "fewer than 5 or angles repeat"
```

### NICE-TO-HAVE (bonus quality, not gate)

```yaml
s1_nice_to_have:
  N1_price_anchor:
    check: "Price anchor exists (reframes cost as daily/per-pet)"
    bonus: "Makes pricing feel cheap — conversion booster"

  N2_urgency_trigger:
    check: "Urgency element present (limited time, first N users)"
    bonus: "Creates FOMO — drives immediate action"

  N3_social_proof:
    check: "Testimonial, user count, or trust badge present"
    bonus: "Reduces risk perception"

  N4_competitor_differentiation:
    check: "At least 1 mention of why this > generic CRM"
    bonus: "Addresses 'why not just use Trello?' objection"

  N5_secondary_cta:
    check: "Secondary CTA for different buyer stage"
    bonus: "Catches leads not ready for primary action"
```

---

## S2: Instagram Content (`instagram_marketing.md`)

### MUST-HAVE (all 5 = PASS, miss 1 = FAIL)

```yaml
s2_must_have:
  M1_five_posts:
    check: "Exactly 5 post concepts present"
    grep: "### Post [1-5]"
    fail_if: "fewer than 5 posts"

  M2_format_mix:
    check: "At least 1 carousel + 1 reels + 1 static"
    grep: "Carousel|Reels|Static"
    fail_if: "missing any of the 3 formats"

  M3_every_post_has_cta:
    check: "Every post includes an explicit CTA"
    grep: "CTA"
    fail_if: "any post lacks CTA in caption or script"

  M4_calendar_seven_days:
    check: "Content calendar covers 7 days (Mon-Sun)"
    grep: "Segunda|Terca|Quarta|Quinta|Sexta|Sabado|Domingo"
    fail_if: "fewer than 7 days or gaps in schedule"

  M5_brand_voice_defined:
    check: "Brand voice guide exists with measurable dimensions"
    grep: "Tom de Voz|Formalidade|Autoridade"
    fail_if: "no voice guide or dimensions are vague (no numbers)"
```

### NICE-TO-HAVE (bonus quality, not gate)

```yaml
s2_nice_to_have:
  N1_hashtag_strategy:
    check: "Hashtag tiers defined (high/mid/niche volume)"
    bonus: "Strategic hashtags > random hashtags"

  N2_reels_timestamps:
    check: "Reels scripts include second-by-second timestamps"
    bonus: "Makes scripts actually producible"

  N3_hook_under_3s:
    check: "Every Reels hook happens in first 3 seconds"
    bonus: "Respects attention economy — hook or lose"

  N4_stories_included:
    check: "Stories appear in calendar (not just feed posts)"
    bonus: "Stories = daily touchpoint, feed = highlight reel"

  N5_vocabulary_guide:
    check: "Specific words to use and avoid are listed"
    bonus: "Actionable voice guide > abstract tone description"
```

---

## S3: Project Documentation (`docs_marketing.md`)

### MUST-HAVE (all 5 = PASS, miss 1 = FAIL)

```yaml
s3_must_have:
  M1_readme_structure:
    check: "README template has all core sections"
    grep: "Problem|Solution|Quickstart|Features|Install|Usage"
    fail_if: "missing any of the 6 core sections"

  M2_quickstart_max_5_steps:
    check: "Quickstart template has 5 or fewer steps"
    grep: "Step [1-5]"
    fail_if: "more than 5 steps"

  M3_quickstart_shows_output:
    check: "Quickstart includes expected output block"
    grep: "Expected Output"
    fail_if: "no expected output section"

  M4_kc_template_frontmatter:
    check: "KC template includes required frontmatter fields"
    grep: "id:|kind:|type:|pillar:|title:|version:|tldr:|when_to_use:"
    fail_if: "missing any of the 8 required fields"

  M5_benefits_not_specs:
    check: "Features guidance shows benefit framing with examples"
    grep: "benefit|BAD|GOOD"
    fail_if: "no concrete examples of benefit vs spec framing"
```

### NICE-TO-HAVE (bonus quality, not gate)

```yaml
s3_nice_to_have:
  N1_anti_patterns:
    check: "Anti-patterns section exists (what NOT to do)"
    bonus: "Learning from negatives is faster than positives"

  N2_tone_table:
    check: "Tone rules with concrete examples per section"
    bonus: "Actionable voice guidance for each doc section"

  N3_time_estimate:
    check: "Quickstart includes time estimate"
    bonus: "Sets expectations, builds confidence"

  N4_docs_as_marketing:
    check: "Explicit framing of docs-as-marketing with comparison table"
    bonus: "Changes mindset from 'docs are chore' to 'docs are growth'"

  N5_prerequisites_first:
    check: "Quickstart lists prerequisites before first command"
    bonus: "Prevents step-3 failure from missing dependency"
```

---

## Cross-Scenario Checks

```yaml
cross_scenario:
  X1_brand_voice_consistency:
    check: "All 3 gold standards use consistent quality language"
    method: "Compare tone across S1/S2/S3 — no jarring shifts"
    fail_if: "S1 is formal but S2 is slang, or S3 contradicts S1 guidelines"

  X2_cta_in_every_artifact:
    check: "Every marketing artifact includes at least 1 CTA"
    method: "Grep for CTA, 'action', imperative verbs across all 3 files"
    fail_if: "any file has zero calls to action"

  X3_pt_br_consistency:
    check: "All copy content is in pt-BR (matching original input language)"
    method: "No English-only sections in marketing copy (templates/structure in English OK)"
    fail_if: "marketing copy switches to English without reason"

  X4_measurable_criteria:
    check: "Every gold standard has validation criteria section"
    method: "Grep for 'Validation Criteria' in each file"
    fail_if: "any file missing its validation criteria block"

  X5_frontmatter_complete:
    check: "All 4 files have complete YAML frontmatter"
    method: "Parse frontmatter: id, kind, type, pillar, title, version, created, author, quality"
    fail_if: "any required field missing in any file"
```

---

## Scoring Summary

| Gate | Weight | Method |
|------|--------|--------|
| MUST-HAVE (per scenario) | 60% | 5/5 = PASS, <5 = FAIL |
| NICE-TO-HAVE (per scenario) | 20% | Each adds 0.4 to score |
| Cross-scenario checks | 20% | 5/5 = PASS, <3 = FAIL |

### Score Calculation

```
base = 6.0 (if all MUST-HAVEs pass across all scenarios)
+ nice_to_have_count * 0.4 (max 15 * 0.4 = 6.0, capped at 2.0)
+ cross_scenario_pass * 0.4 (max 5 * 0.4 = 2.0)
= max 10.0

FAIL conditions (override score to 0):
- ANY must-have fails in ANY scenario
- Fewer than 3 cross-scenario checks pass
- Any file missing frontmatter
```

### Pass Threshold

**>= 8.0** — Gold standard accepted for E2E test harness.
**< 8.0** — Revise and resubmit. Identify which MUST-HAVEs failed.
