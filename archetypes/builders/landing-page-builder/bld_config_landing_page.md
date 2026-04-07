---
id: bld_config_landing_page
kind: config
pillar: P06
builder: landing-page-builder
version: 1.0.0
effort: high
max_turns: 30
disallowed_tools: []
permission_scope: nucleus
---
# Config: Landing Page Builder

output_format: html
quality_floor: 8.5

defaults:
  stack: html-tailwind    # html-tailwind | react | nextjs | astro
  sections: 12
  mobile_first: true
  dark_mode: true
  tailwind_version: "3.4"
  font_provider: google-fonts
  image_placeholders: picsum
  analytics: gtm
  a11y_level: AA          # WCAG AA minimum

brand_injection:
  required: false
  fields: [BRAND_NAME, BRAND_COLORS, BRAND_FONTS, BRAND_TONE, BRAND_TAGLINE]
  fallback: generate_defaults

design_tokens:
  colors:
    primary: "#2563eb"    # blue-600
    secondary: "#7c3aed"  # violet-600
    accent: "#f59e0b"     # amber-500
    bg: "#ffffff"
    text: "#111827"       # gray-900
    muted: "#6b7280"      # gray-500
  fonts:
    heading: "Inter"
    body: "Inter"
    mono: "JetBrains Mono"
  radius: "0.5rem"
  shadow: "0 4px 6px -1px rgb(0 0 0 / 0.1)"
