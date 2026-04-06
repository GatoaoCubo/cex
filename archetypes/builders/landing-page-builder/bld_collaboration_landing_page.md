---
id: bld_collaboration_landing_page
kind: collaboration
pillar: P12
builder: landing-page-builder
version: 1.0.0
---
# Collaboration: Landing Page Builder

## Upstream (receives from)
- brand_config.yaml → colors, fonts, tone, logo URL
- tagline-builder → hero headline, sub-headline, CTA text
- content-monetization-builder → pricing tiers, feature lists
- N01 Research → competitor page analysis, market positioning
- N06 Commercial → pricing strategy, conversion goals

## Downstream (sends to)
- N05 Operations → deployment (Vercel, Netlify, S3, GitHub Pages)
- social-publisher-builder → Open Graph previews for social sharing
- N02 Marketing → campaign landing pages, A/B variants
- N04 Knowledge → page templates added to knowledge library

## Crew Behavior
- In a crew, landing-page-builder runs LATE (needs tagline, pricing, brand tokens first)
- Consumes outputs from tagline-builder and content-monetization-builder
- Produces a DEPLOYABLE artifact, not a design spec
- If A/B testing requested, produces 2 variants with clear differentiators
