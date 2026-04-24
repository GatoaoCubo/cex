---
id: skill_n02
kind: skill
8f: F5_call
nucleus: n02
pillar: P04
mirrors: N00_genesis/P04_tools/kind_skill/kind_manifest_n00.md
overrides:
  tone: seductive, emotional, conversion-oriented
  voice: second-person direct / brand-first
  sin_lens: LUXURIA CRIATIVA
  required_fields:
    - brand_voice_anchor
    - emotional_tone
    - cta_intent
    - hook_structure
    - ab_variant_count
  quality_threshold: 9.0
  density_target: 0.85
  example_corpus: 3+ examples with brand voice samples
trigger: "copy request | hook needed | CTA pattern | A/B variant"
auto_generated_from: null
self_improves: true
agentskills_catalog_category: copywriting
version: 1.0.0
quality: 8.5
tags: [mirror, n02, marketing, creative, hermes_assimilation, copy, hooks, cta, P04]
tldr: "N02 copy skill: hook structures, CTA patterns, and A/B variant generation under LUXURIA CRIATIVA"
created: "2026-04-18"
updated: "2026-04-18"
author: n02_marketing
related:
  - p03_sp_marketing_nucleus
  - p08_ac_n02
  - n02_tool_copy_analyzer
  - p07_sr_5d_marketing
  - p03_ap_visual_frontend_marketing
  - ad_copy_template
  - p03_sp_visual_frontend_marketing
  - p07_sr_visual_frontend_marketing
  - p02_agent_visual_frontend_marketing
  - bld_collaboration_skill
density_score: 1.0
---

## N02 Override: Copy Skill

N00 defines skill as a reusable capability with trigger + phases. N02 specializes
this into **the art of conversion copy** -- structured seduction with measurable CTAs.

## Hook Structures

| Structure | Template | Trigger |
|-----------|----------|---------|
| Pain-first | "Still struggling with {{pain}}?" | Awareness stage |
| Desire-first | "What if {{aspiration}} was already yours?" | Consideration stage |
| Proof-first | "{{number}} {{peers}} already {{result}}." | Decision stage |
| Provocation | "{{common_belief}} is costing you {{loss}}." | Cold audience |

## CTA Patterns

| Pattern | Copy | Best For |
|---------|------|---------|
| Action | "Get {{outcome}} now" | High-intent page |
| Curiosity | "See what changes in 7 days" | Email subject |
| Belonging | "Join {{N}} people who already..." | Community CTAs |
| Urgency | "{{N}} spots left. You in?" | Launch / flash sale |

## A/B Variant Generation

When producing copy, always generate 2 variants minimum:
- **Variant A**: Desire-led (opens with aspiration)
- **Variant B**: Pain-led (opens with friction)

Both variants MUST share: same CTA intent, same word count range (+/-10%), same brand register.

## Skill Execution Phases

1. **Load** brand voice anchor + buyer stage from user_model_n02
2. **Select** hook structure matching buying stage
3. **Draft** Variant A + Variant B
4. **Check** anti-patterns from personality_n02
5. **Output** both variants with character counts

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_marketing_nucleus]] | upstream | 0.37 |
| [[p08_ac_n02]] | downstream | 0.28 |
| [[n02_tool_copy_analyzer]] | related | 0.26 |
| [[p07_sr_5d_marketing]] | downstream | 0.26 |
| [[p03_ap_visual_frontend_marketing]] | upstream | 0.26 |
| [[ad_copy_template]] | downstream | 0.25 |
| [[p03_sp_visual_frontend_marketing]] | upstream | 0.23 |
| [[p07_sr_visual_frontend_marketing]] | downstream | 0.22 |
| [[p02_agent_visual_frontend_marketing]] | upstream | 0.22 |
| [[bld_collaboration_skill]] | downstream | 0.22 |
