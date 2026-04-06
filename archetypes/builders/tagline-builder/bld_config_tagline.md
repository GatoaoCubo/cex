---
id: bld_config_tagline
kind: config
pillar: P06
builder: tagline-builder
version: 1.0.0
---
# Config: Tagline Builder

effort: medium
max_turns: 15
permission_scope: nucleus
output_format: yaml
quality_floor: 8.5

defaults:
  variants_per_round: 10
  approaches: [emotional, functional, aspirational, provocative, minimal]
  lengths: [short, medium, long]
  contexts: [site-hero, social-bio, ad-headline, email-subject, pitch-deck]
  language: auto  # detect from user input

brand_injection:
  required: false
  fields: [BRAND_NAME, BRAND_TAGLINE, BRAND_TONE, BRAND_AUDIENCE, BRAND_INDUSTRY]
  fallback: ask_user
