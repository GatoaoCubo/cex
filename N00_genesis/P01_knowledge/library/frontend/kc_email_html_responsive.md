---
id: p01_kc_email_html_responsive
kind: knowledge_card
pillar: P01
title: Email HTML & Responsive Design
version: 1.0.0
created: 2026-04-01
author: builder
domain: frontend
quality: 9.1
tags: [email, html, responsive, outlook, gmail, dark-mode, templating, deliverability]
tldr: Rock-solid email HTML with table layouts, inline CSS, client compatibility, and dark mode support for maximum deliverability
density_score: 1.0
when_to_use: "Apply when rock-solid email html with table layouts, inline css, client compatibility, and dark mode support..."
keywords: [knowledge-card, reference, frontend, email, html]
linked_artifacts:
  primary: null
  related: []
related:
  - p05_output_email_template
  - n02_kc_email_html_responsive
  - p01_kc_brand_propagation_arch
  - p01_kc_color_theory_applied
  - p05_output_social_card
  - p01_kc_design_token_arch
  - n02_kc_color_theory_applied
  - spec_n02_part2
  - p10_hos_html_output_visual_frontend
  - p03_sp_visual_frontend_marketing
---

# Email HTML & Responsive Design

## Quick Reference

```yaml
email_constraints:
  max_width: 600px
  layout: table-based
  css: inline-only
  images: alt-text-required
  
client_support:
  outlook: mso-conditionals, table-layout, no-flexbox
  gmail: limited-css, no-external-styles, image-blocking
  apple_mail: best-support, webkit-features
  
dark_mode:
  media_query: "@media (prefers-color-scheme: dark)"
  meta_tag: '<meta name="color-scheme" content="light dark">'
  
templating:
  engine: jinja2
  api: resend
  variables: "{{ user.name }}, {{ product.price }}"
```

## Key Concepts

### Table-Based Layout Foundation
- **Nested tables**: Use table>tr>td structure for reliable cross-client layout, avoid div-based layouts
- **Cellpadding/cellspacing**: Always set to 0, use CSS padding for spacing control
- **Width constraints**: Max-width 600px with width="100%" for mobile responsiveness
- **Alignment**: Use align="center" on tables and valign="top" on cells for consistent positioning
- **Border collapse**: Set border-collapse: collapse; border-spacing: 0; on all tables

### Inline CSS Requirements
- **No external stylesheets**: Gmail strips <link> tags, inline all CSS using style attributes
- **CSS support matrix**: Stick to basic properties - margin, padding, color, font-family, background
- **Font fallbacks**: Always specify web-safe font stacks: Arial, Helvetica, sans-serif
- **Background images**: Use background-color fallback, many clients block background-image
- **Reset styles**: Inline margin: 0; padding: 0; on body and table elements

### Client Compatibility Patterns
- **MSO conditionals**: <!--[if mso]> for Outlook-specific fixes and VML fallbacks
- **Image blocking**: Provide meaningful alt text, design works without images loaded
- **Link styling**: Inline color and text-decoration on <a> tags, Outlook ignores inherited styles
- **Line height**: Use unitless line-height values (1.4) for better cross-client rendering
- **Margin/padding**: Prefer padding over margin for more predictable spacing

### Dark Mode Implementation
- **Color scheme meta**: Include meta tag for system dark mode detection
- **Media query wrapper**: Wrap dark mode styles in @media (prefers-color-scheme: dark)
- **Color variables**: Define light/dark color pairs, swap in media query
- **Image alternatives**: Provide dark mode image variants or ensure images work on dark backgrounds
- **Border visibility**: Light borders disappear in dark mode, use contrasting colors

## Patterns

### Responsive Container
```html
<table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td align="center">
      <table width="600" style="max-width: 600px;" cellpadding="0" cellspacing="0">
```

### Dark Mode Colors
```html
<style>
  @media (prefers-color-scheme: dark) {
    .content { background-color: #1a1a1a !important; color: #ffffff !important; }
    .border { border-color: #333333 !important; }
  }
</style>
```

### MSO Conditionals
```html
<!--[if mso]>
<table width="600" cellpadding="0" cellspacing="0"><tr><td>
<![endif]-->
  <div style="max-width: 600px;">
<!--[if mso]>
</td></tr></table>
<![endif]-->
```

### Jinja2 Template
```html
<h1 style="color: #333;">Hello {{ user.name }}!</h1>
<p>Your order #{{ order.id }} for {{ product.name }} is ready.</p>
{% if user.premium %}
<div style="background: gold;">Premium Member Benefits</div>
{% endif %}
```

## Golden Rules

1. **Tables Everywhere**: Use table layout for structure, never rely on div+CSS for email layout
2. **Inline All CSS**: No external stylesheets, no <style> in <head>, inline everything
3. **600px Max Width**: Industry standard, works across all clients and devices
4. **Alt Text Always**: Every image needs descriptive alt text for accessibility and blocking
5. **Test Dark Mode**: Use @media (prefers-color-scheme: dark) and test in real clients
6. **MSO Fallbacks**: Outlook needs special treatment, use conditionals liberally
7. **Font Stack Defense**: Always specify fallback fonts, don't rely on web fonts alone
8. **Preview Text**: Include preheader text to control inbox preview, hide with CSS

## References

- HTML Email Standards: Table layout, inline CSS, client compatibility matrix
- Dark Mode: Color scheme meta tag, media queries, image alternatives
- Outlook MSO: Conditional comments, VML fallbacks, table-based layouts
- Accessibility: Alt text, semantic HTML, screen reader optimization
- Templating: Jinja2 syntax, variable interpolation, conditional blocks
- Resend API: Send transactional emails, template management, deliverability tracking

## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_output_email_template]] | downstream | 0.66 |
| [[n02_kc_email_html_responsive]] | sibling | 0.65 |
| [[p01_kc_brand_propagation_arch]] | sibling | 0.34 |
| [[p01_kc_color_theory_applied]] | sibling | 0.32 |
| [[p05_output_social_card]] | downstream | 0.31 |
| [[p01_kc_design_token_arch]] | sibling | 0.30 |
| [[n02_kc_color_theory_applied]] | sibling | 0.30 |
| [[spec_n02_part2]] | downstream | 0.30 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.28 |
| [[p03_sp_visual_frontend_marketing]] | downstream | 0.25 |
