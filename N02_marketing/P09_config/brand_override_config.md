---
id: brand_override_config
kind: env_config
pillar: P09
title: Brand Override Config for N02 Marketing
version: 1.0.0
created: 2026-04-02
author: n02_marketing
domain: brand_configuration
quality: 9.0
tags: [config, brand, marketing, tone, voice, N02]
tldr: Brand-specific overrides for marketing copy generation — tone, voice, terminology, and channel-specific adaptations.
density_score: 1.0
related:
  - brand_voice_templates
  - p06_schema_env_contract
  - bld_output_template_input_schema
  - p03_sp_brand_nucleus
  - ex_env_config_default
  - n06_input_schema_content_order
  - p01_kc_brand_voice_consistency_channels
  - ex_prompt_template_aida
  - n02_tool_copy_analyzer
  - p10_lr_input_schema_builder
---

# Brand Override Config — N02 Marketing

## Brand Voice Calibration

### Base Brand Settings
```yaml
brand:
  name: "{{BRAND_NAME}}"
  tone: "{{BRAND_TONE}}"  # professional | casual | technical | friendly
  voice: "{{BRAND_VOICE}}" # confident | humble | authoritative | conversational
  energy: "{{BRAND_ENERGY}}" # calm | energetic | bold | subtle
  person: "{{BRAND_PERSON}}" # 1st | 2nd | 3rd
```

### Copy Formula Preferences
```yaml
copy_preferences:
  primary_formula: "{{BRAND_COPY_FORMULA | default: 'AIDA'}}"  # AIDA | PAS | BAB | FAB
  headline_style: "{{BRAND_HEADLINE_STYLE | default: 'benefit-first'}}"  # benefit-first | curiosity-gap | specific-result
  cta_style: "{{BRAND_CTA_STYLE | default: 'action-specific'}}"  # action-specific | benefit-focused | urgency-driven
  audience_address: "{{BRAND_AUDIENCE_ADDRESS | default: 'you'}}"  # you | we | customer-name
```

### Channel Adaptations
```yaml
channels:
  email:
    tone_adjustment: "+5% formal"  # relative to base tone
    max_subject_length: 50
    preview_text_required: true
    
  social_media:
    tone_adjustment: "+10% casual"
    hashtag_strategy: "{{BRAND_HASHTAG_STRATEGY | default: 'minimal'}}"  # minimal | moderate | extensive
    emoji_usage: "{{BRAND_EMOJI_USAGE | default: 'occasional'}}"  # none | occasional | frequent
    
  ads:
    tone_adjustment: "0% (base)"
    hook_requirement: "curiosity-gap + benefit"
    character_limits:
      facebook: 125
      google: 90
      linkedin: 150
      
  landing_pages:
    tone_adjustment: "+5% confident"
    social_proof_requirement: true
    urgency_level: "{{BRAND_URGENCY_LEVEL | default: 'moderate'}}"  # low | moderate | high
```

### Terminology & Voice

#### Approved Terms
```yaml
preferred_words:
  - "{{BRAND_PREFERRED_WORDS | default: ['solution', 'results', 'growth', 'success']}}"
  
power_words:
  - "{{BRAND_POWER_WORDS | default: ['proven', 'effective', 'streamlined', 'optimized']}}"
  
industry_terms:
  - "{{BRAND_INDUSTRY_TERMS | default: []}}"  # Brand-specific terminology
```

#### Banned Terms
```yaml
avoid_words:
  - "{{BRAND_AVOID_WORDS | default: ['amazing', 'incredible', 'revolutionary', 'game-changer']}}"
  
overused_phrases:
  - "{{BRAND_OVERUSED_PHRASES | default: ['take your business to the next level', 'cutting-edge', 'world-class']}}"
```

### Quality Standards
```yaml
quality_gates:
  readability:
    flesch_kincaid_min: "{{BRAND_READABILITY_MIN | default: 60}}"  # B2C: 60-70, B2B: 40-60
    max_sentence_length: "{{BRAND_MAX_SENTENCE | default: 20}}"  # words
    
  specificity:
    stats_preference: "{{BRAND_STATS_PREFERENCE | default: 'specific-with-source'}}"  # vague | specific | specific-with-source
    claim_substantiation: "{{BRAND_CLAIM_SUBSTANTIATION | default: 'required'}}"  # required | optional
    
  legal:
    disclaimer_requirement: "{{BRAND_DISCLAIMER_REQUIRED | default: false}}"
    claim_approval_needed: "{{BRAND_CLAIM_APPROVAL | default: false}}"
```

## Integration Settings

### API Configurations
```yaml
integrations:
  headliner_scorer:
    enabled: true
    scoring_weights:
      curiosity: 0.3
      specificity: 0.4
      urgency: 0.2
      clarity: 0.1
      
  readability_analyzer:
    enabled: true
    target_score: "{{BRAND_READABILITY_TARGET | default: 65}}"
    
  sentiment_checker:
    enabled: true
    target_sentiment: "{{BRAND_TARGET_SENTIMENT | default: 'positive_confident'}}"
```

### Cross-Nucleus Handoffs
```yaml
handoffs:
  from_n01_research:
    format: "research_brief_to_marketing_angles"
    required_fields: ["audience_insights", "pain_points", "competitive_landscape"]
    
  to_n05_deployment:
    format: "copy_deployment_package" 
    deliverables: ["final_copy", "a_b_variants", "performance_expectations"]
    
  to_n06_commercial:
    format: "copy_commercial_alignment"
    coordination: ["pricing_messaging", "value_proposition", "objection_handling"]
```

## Environment Overrides

### Development
```yaml
development:
  ab_testing: false
  approval_workflow: false
  placeholder_content: true
  
### Staging  
staging:
  ab_testing: true
  approval_workflow: true
  real_content: true
  performance_tracking: false
  
### Production
production:
  ab_testing: true
  approval_workflow: true
  real_content: true
  performance_tracking: true
  legal_review: "{{BRAND_LEGAL_REVIEW_REQUIRED | default: false}}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[brand_voice_templates]] | upstream | 0.36 |
| [[p06_schema_env_contract]] | upstream | 0.29 |
| [[bld_output_template_input_schema]] | upstream | 0.21 |
| [[p03_sp_brand_nucleus]] | upstream | 0.21 |
| [[ex_env_config_default]] | sibling | 0.18 |
| [[n06_input_schema_content_order]] | upstream | 0.17 |
| [[p01_kc_brand_voice_consistency_channels]] | upstream | 0.17 |
| [[ex_prompt_template_aida]] | upstream | 0.17 |
| [[n02_tool_copy_analyzer]] | upstream | 0.16 |
| [[p10_lr_input_schema_builder]] | downstream | 0.16 |
