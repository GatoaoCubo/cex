---
id: content_filter_n02
kind: content_filter
pillar: P04
nucleus: n02
title: "Brand Voice Compliance Filter -- Content Safety and Quality Gate"
version: 1.0.0
quality: 8.9
tags: [content_filter, brand_voice, compliance, content_safety, P04, n02_marketing]
domain: content-governance
status: active
density_score: 1.0
---

# Brand Voice Compliance Filter

## Purpose

Not everything that can be published should be published.
This filter is N02's immune system: it catches copy that violates
brand standards, platform policies, and legal constraints before
it reaches the distribution layer. One viral mistake costs more
than a thousand great campaigns.

## Filter Architecture

```
COPY INPUT
    |
    v
L1: BRAND VOICE COMPLIANCE (fast, deterministic)
    |
    v
L2: PLATFORM POLICY CHECK (rule-based, platform-specific)
    |
    v
L3: LEGAL/SENSITIVITY CHECK (pattern matching + blocklist)
    |
    v
L4: COMPETITIVE INTELLIGENCE GUARD (protect brand positioning)
    |
    v
DECISION: PASS | WARN | FAIL
    |
    +-- PASS: proceed to social_publisher_n02.md
    +-- WARN: pass with flagged items (human review suggested)
    +-- FAIL: return to action_prompt_n02_copy.md for regeneration
```

## L1 Brand Voice Compliance

```yaml
brand_voice_rules:
  source: validation_schema_content_spec.md (tone_rule_matrix)

  universal_blocklist:
    - "game-changer"
    - "revolutionary"
    - "world-class"
    - "synergy"
    - "leverage" (as noun in "a key leverage")
    - "seamlessly"
    - "cutting-edge"
    - "innovative solution"
    - "empower" (overused; replace with specific action)
    - "ecosystem" (unless genuinely technical context)
    - "value-add"
    - "best-in-class"
    - "state-of-the-art"
    - "thought leader" (when self-applied)
    - "disruptive" (unless specific market context)

  readability_rules:
    flesch_kincaid_max: 10 (B2B) / 8 (B2C)
    avg_sentence_length_max: 25 words
    passive_voice_max_pct: 20

  action_per_voice:
    bold:
      require: verb-first-sentences
      block: qualifiers ("might", "could", "perhaps", "potentially")
    conversational:
      require: contractions-allowed
      block: corporate-jargon
    professional:
      block: exclamation_mark_count > 2
      block: emoji_count > 1
    empathetic:
      require: second-person-references
      block: prescriptive-commands
```

## L2 Platform Policy Check

```yaml
instagram:
  prohibited: [explicit_content, misleading_health_claims, firearms, tobacco]
  text_overlay_rule: max 20% image area (Meta policy)
  sponsored_label: required_if budget_usd > 0

linkedin:
  prohibited: [political_ads_without_disclosure, misleading_professional_claims]
  discrimination_free: age, gender, race cannot be targeting criterion in ads
  b2b_tone: required (no hyper-casual language in promoted content)

x_twitter:
  prohibited: [coordinated_inauthentic_behavior, synthetic_media_without_label]
  political_ads: require_authorization
  character_hard_limit: 280 (URLs = 23 chars each)

meta_ads:
  special_categories: [housing, credit, employment, social_issues]
  text_overlay_check: true (automated via Meta API)
  landing_page_required: true (for conversion objective)
```

## L3 Legal / Sensitivity Check

```yaml
legal_patterns:
  claim_guardrails:
    superlatives:
      detect: ["#1", "best", "only", "first", "exclusive", "guaranteed"]
      action: WARN -- requires substantiation
    health_claims:
      detect: ["cure", "treat", "prevent", "heal", "diagnose"]
      action: FAIL -- medical claims require compliance review
    financial_claims:
      detect: ["guaranteed return", "risk-free", "profit guaranteed"]
      action: FAIL -- financial disclaimer required

  sensitivity_blocklist:
    categories: [racial_slurs, gender_slurs, ableist_language, religious_mockery]
    action: FAIL (immediate, no regeneration)

  competitor_references:
    direct_comparison: WARN (legal review)
    disparagement: FAIL
    comparative_advertising: WARN (jurisdiction-specific rules)

  trademark_guard:
    detect: [registered_brand_names used incorrectly]
    action: WARN
```

## L4 Competitive Intelligence Guard

```yaml
competitive_guard:
  purpose: prevent accidental amplification of competitors
  rules:
    - no_competitor_mentions: unless explicit comparative campaign (requires approval)
    - no_competitor_hashtags: detect competitor branded hashtags
    - no_implicit_reference: detect dog-whistle competitor references
  source: campaign_brief.competitor_avoid field

  on_detection:
    action: WARN + flag specific mention + suggest neutral alternative
```

## Filter Output Schema

```yaml
filter_result:
  asset_id: string
  decision: PASS|WARN|FAIL
  score: float (0.0-1.0, where 1.0 = fully compliant)
  checks_passed: integer
  checks_total: integer
  violations:
    - layer: L1|L2|L3|L4
      rule: string
      severity: error|warning
      excerpt: string (the problematic text)
      suggestion: string
  override_allowed: boolean
  override_requires: human_review|legal_sign_off|auto
```

## Override Protocol

```yaml
override_rules:
  WARN_override:
    allowed: true
    requires: campaign_manager_acknowledgment
    log: true
  FAIL_override:
    L1_brand_voice: allowed (regenerate preferred)
    L2_platform_policy: not_allowed
    L3_legal: not_allowed (legal sign-off required externally)
    L4_competitive: allowed with legal_review flag
```

## Integration

- Reads: `validation_schema_content_spec.md` (brand voice rules source)
- Reads: `input_schema_campaign_brief.md` (competitor_avoid field)
- Called by: `workflow_campaign_pipeline.md` (F6 VALIDATE, after action_prompt)
- Blocks: `social_publisher_n02.md` (FAIL result prevents publish)
- Reports to: `self_improvement_loop_n02.md` (violation patterns as learning signals)
