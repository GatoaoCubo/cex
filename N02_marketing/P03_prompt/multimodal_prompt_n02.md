---
id: multimodal_prompt_n02
kind: multimodal_prompt
8f: F6_produce
pillar: P03
nucleus: n02
title: "Visual + Copy Coordination Prompt -- Image Brief + Caption Combo"
version: 1.0.0
quality: 9.0
tags: [multimodal_prompt, visual_brief, image_copy, creative_direction, P03, n02_marketing]
domain: creative-production
status: active
density_score: 1.0
related:
  - p07_sr_visual_frontend_marketing
  - p02_agent_visual_frontend_marketing
  - p03_ap_visual_frontend_marketing
  - p12_wf_visual_frontend_marketing
  - p08_ac_visual_frontend_marketing
  - p12_dr_visual_frontend_marketing
  - n02_leverage_map_v2_verification
  - p03_pt_visual_frontend_marketing
  - n02_leverage_map_v2_iteration2
  - p03_sp_visual_frontend_marketing
---

# Multimodal Prompt -- Visual + Copy Coordination

## Purpose

Copy without visual context produces orphaned text.
Visual without copy direction produces generic imagery.
This prompt bridges both: a unified creative brief that makes the
image and the caption inseparable. Two inputs. One impact.

## Creative Direction Schema

```yaml
creative_brief:
  campaign_id: string
  asset_id: string
  platform: instagram|linkedin|x|meta|tiktok|youtube
  format: post|story|reel|carousel|email_hero|ad_creative

  visual_direction:
    primary_subject: string          # "founder at desk, working late, honest environment"
    mood: string                     # "focused intensity, not corporate polish"
    color_palette: array[hex]        # from brand_config.yaml or brief
    avoid: array[string]             # "stock photo smiles, white backgrounds, posed groups"
    text_overlay: string (nullable)  # text embedded in image (if applicable)
    dimensions:
      width: integer
      height: integer
      aspect_ratio: string           # "4:5" "9:16" "1:1" "16:9"

  copy_direction:
    hook: string                     # from action_prompt_n02_copy.md (headline)
    body: string                     # from action_prompt_n02_copy.md (body)
    cta: string                      # from action_prompt_n02_copy.md (CTA)
    hashtags: array[string]          # max per platform (validation_schema)

  visual_copy_relationship:
    type: contrast|complement|reinforce|subvert
    rationale: string
```

## Visual-Copy Relationship Types

| Type | Definition | When to Use | Example |
|------|-----------|------------|--------|
| `contrast` | Visual says the opposite of copy | Pattern interrupt, curiosity hook | Image: chaotic desk. Copy: "The most organized campaign of your year." |
| `complement` | Visual illustrates what copy states | Data or authority hooks | Image: graph rising. Copy: "40% more conversions. Here's how." |
| `reinforce` | Visual amplifies the emotion of copy | Pain or empathy hooks | Image: exhausted person. Copy: "We've been there too." |
| `subvert` | Visual undermines the expected | Playful, bold brand voices | Image: polished product. Copy: "It's not magic. It just looks like it." |

## System Prompt Template (Creative Direction)

```
You are the Creative Director for N02 Marketing. Your job is to brief
a visual artist OR an image generation system on EXACTLY what to create
to make this copy land with maximum impact.

COPY (LOCKED -- do not change):
Headline: {{headline}}
Body: {{body}}
CTA: {{cta}}

PLATFORM: {{platform}} | FORMAT: {{format}} | DIMENSIONS: {{dimensions}}
BRAND VOICE: {{brand_voice}} | ICP: {{icp_label}}

Create a VISUAL BRIEF with these exact sections:

PRIMARY SUBJECT: [what is in the image, described in 15 words or fewer]
MOOD: [emotional atmosphere -- not abstract adjectives, but sensory descriptors]
COMPOSITION: [where the subject sits, negative space, text safe zones]
LIGHTING: [quality and direction of light -- natural/studio/dramatic/soft]
COLOR STRATEGY: [palette, dominant color, accent, what to avoid]
TEXT OVERLAY: [exact text to embed in image, or "none"]
AVOID: [3-5 specific visual clichés to exclude]
RELATIONSHIP TO COPY: [contrast|complement|reinforce|subvert -- one sentence explanation]
```

## Platform-Specific Visual Specs

| Platform | Format | Dimensions | Safe Zone | Notes |
|----------|--------|-----------|---------|-------|
| Instagram | Post (portrait) | 1080x1350 | 1080x1215 center | Bottom 135px often cropped |
| Instagram | Story | 1080x1920 | 1080x1420 center | Top/bottom 250px for UI |
| Instagram | Reel | 1080x1920 | 1080x1420 center | Same as Story |
| Instagram | Carousel | 1080x1080 | Full | Square; left edge continues |
| LinkedIn | Post | 1200x628 | 1200x542 center | Wide landscape format |
| LinkedIn | Vertical | 1080x1350 | 1080x1215 | Same as IG portrait |
| Meta Ads | Feed | 1080x1080 | Full | Text max 20% of image |
| Meta Ads | Story | 1080x1920 | 1080x1420 | UI zones at top/bottom |
| X | Post | 1200x675 | Full | 16:9 wide format |
| Email Hero | Desktop | 600x338 | Full | 2:1 ratio standard |

## Carousel Sequence Schema

For carousel format, coordinate visual narrative across cards:

```yaml
carousel_sequence:
  card_count: integer (2-10)
  narrative_arc: teaser|serial|list|comparison|tutorial
  cards:
    - position: 1
      role: hook (stop the scroll)
      visual: string
      copy: string (short -- this gets read)
    - position: 2
      role: body (build desire)
      visual: string
      copy: string
    # ...
    - position: last
      role: cta (convert)
      visual: string
      copy: string (CTA prominent)
  visual_continuity: true   # bleeding image across card edges
```

## Quality Self-Check

Before delivering creative brief:
- [ ] Visual brief is platform-correct dimensions
- [ ] Text overlay is within character limits for embedded text
- [ ] Visual-copy relationship type is declared and justified
- [ ] No generic/stock-photo visual direction (specific, ownable)
- [ ] Carousel has narrative arc (not random sequence)
- [ ] Brand color palette referenced (from brand_config.yaml)

## Integration

- Called by: `workflow_campaign_pipeline.md` (F5 CREATE, if visual assets required)
- Extends: `action_prompt_n02_copy.md` (adds visual layer to copy outputs)
- Feeds: `social_publisher_n02.md` (image brief -> image -> publish)
- Validated by: `validation_schema_content_spec.md` (text overlay limits)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_sr_visual_frontend_marketing]] | downstream | 0.36 |
| [[p02_agent_visual_frontend_marketing]] | upstream | 0.35 |
| [[p03_ap_visual_frontend_marketing]] | related | 0.34 |
| [[p12_wf_visual_frontend_marketing]] | downstream | 0.33 |
| [[p08_ac_visual_frontend_marketing]] | downstream | 0.32 |
| [[p12_dr_visual_frontend_marketing]] | downstream | 0.31 |
| [[n02_leverage_map_v2_verification]] | upstream | 0.30 |
| [[p03_pt_visual_frontend_marketing]] | related | 0.30 |
| [[n02_leverage_map_v2_iteration2]] | downstream | 0.29 |
| [[p03_sp_visual_frontend_marketing]] | related | 0.29 |
