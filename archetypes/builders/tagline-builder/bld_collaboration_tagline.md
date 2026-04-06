---
id: bld_collaboration_tagline
kind: collaboration
pillar: P12
builder: tagline-builder
version: 1.0.0
---
# Collaboration: Tagline Builder

## Upstream (receives from)
- brand_config.yaml → brand identity, tone, audience
- N01 Research → competitor taglines, market positioning data
- N06 Commercial → pricing tier names, product positioning

## Downstream (sends to)
- landing-page-builder → hero headline, sub-headline
- social-publisher-builder → bio lines, post captions
- content-monetization-builder → course taglines, product names
- N02 Marketing → campaign headlines, ad copy
- N06 Commercial → pitch deck one-liners, brand book messaging

## Crew Behavior
- In a crew, tagline-builder runs EARLY (provides messaging foundation)
- Other builders reference tagline output for consistency
- If brand_config changes, tagline should be regenerated first
