---
id: ex_response_format_ad_copy
kind: response_format
pillar: P05
title: "Example — Ad Copy Output Format"
tags: [output, format, ad, copy, social-media]
tldr: "Structured output format for ad copy generation. Enforces character limits, emoji caps, and hashtag counts for platform compliance."
references:
  - tpl_response_format
  - ex_agent_copywriter
  - ex_quality_gate_copy
quality: 9.0
updated: "2026-04-07"
domain: "output formatting"
version: "1.0.0"
author: n03_builder
created: "2026-04-07"
density_score: 0.96
---

# Ad Copy Output Format

## Schema
```yaml
headline: string    # max 60 chars — grabs attention
body: string        # max 2200 chars — Instagram limit
cta: string         # max 30 chars — clear action
hashtags: list      # max 5 — focused, not spammy
emoji_count: int    # max 3 — emphasis without noise
platform: enum      # instagram | linkedin | twitter | facebook
tone: enum          # casual | professional | urgent | playful
```

## Platform Constraints

| Platform | Headline | Body | Hashtags | Emoji |
|----------|----------|------|----------|-------|
| Instagram | 60 chars | 2200 chars | 5-30 | 1-5 |
| LinkedIn | 70 chars | 3000 chars | 3-5 | 0-2 |
| Twitter/X | N/A | 280 chars | 1-3 | 0-2 |
| Facebook | 80 chars | 500 chars | 0-3 | 0-3 |

## Example Output
```json
{
  "headline": "Your competitors post 5x more than you.",
  "body": "73% of SaaS founders say content is their #1 growth channel. But most post once a week — if that.\n\nOur clients automated their content pipeline and went from 3 random posts to 20 strategic ones per month.\n\nResult? 4x engagement. 2x qualified leads.",
  "cta": "Start your free audit →",
  "hashtags": ["#SaaS", "#ContentStrategy", "#Growth", "#Marketing", "#Automation"],
  "emoji_count": 0,
  "platform": "linkedin",
  "tone": "professional"
}
```

## Validation Rules
- Headline ≤ platform limit (reject if over)
- Body ≤ platform limit (truncate + warn if close)
- No `{{placeholders}}` in output
- CTA contains exactly 1 action verb

## Quality Gate
- [ ] All fields populated (no nulls)
- [ ] Character limits respected per platform
- [ ] Tone matches requested tone
- [ ] CTA is actionable (verb + direction)
