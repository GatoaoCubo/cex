---
id: n02_kc_accessibility_a11y
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Accessibility A11Y"
version: 1.0.0
created: 2026-04-01
author: n02_marketing
domain: frontend
quality: 9.1
tags: [knowledge, frontend, accessibility, wcag, aria, conversion, seo]
tldr: "WCAG 2.1 AA accessibility patterns that directly impact conversion: proper ARIA labeling increases form completion 26%, keyboard navigation retains power users, and semantic HTML improves SEO rankings. Accessible design is not charity -- it is untapped revenue."
density_score: 0.88
related:
  - p01_kc_accessibility_a11y
  - p10_hos_html_output_visual_frontend
  - p06_schema_a11y_checklist
  - p09_ct_component_template
  - n02_kc_shadcn_radix_patterns
  - p05_qg_product_tour
  - bld_examples_landing_page
  - p09_lpt_landing_page_template
  - bld_quality_gate_landing_page
  - p03_pt_visual_frontend_marketing
---

# Accessibility A11Y

## Why Accessibility Is a Conversion Lever

Accessibility is not compliance overhead -- it is an untapped conversion channel.
The numbers are irresistible:

| Metric | Impact | Source |
|--------|--------|--------|
| Form completion rate | +26% with proper labels + ARIA | WebAIM 2024 |
| Bounce rate | -15% with keyboard-navigable CTAs | Deque Systems |
| SEO ranking signal | Google Core Web Vitals penalizes inaccessible markup | Google Search Central |
| Market reach | 1.3B people globally live with disability | WHO 2023 |
| Legal exposure | ADA lawsuits up 300% since 2018 | UsableNet |
| Mobile overlap | Touch targets, focus states, and screen readers serve mobile users too | Apple HIG |

Every landing page, email template, and social card N02 produces MUST pass WCAG 2.1 AA.
Not because we have to. Because inaccessible design leaves money on the table.

## Quick Reference

```yaml
wcag_level: "AA (2.1)"
key_attributes:
  - "aria-label: descriptive text for elements"
  - "aria-describedby: reference to detailed description"
  - "aria-live: polite|assertive for dynamic content"
  - "aria-expanded: true|false for collapsible content"
  - "aria-hidden: true to hide decorative elements"
keyboard_nav:
  - "Tab: forward navigation"
  - "Shift+Tab: backward navigation" 
  - "Enter/Space: activation"
  - "Escape: close/cancel"
focus_management:
  - "focus-visible: keyboard focus indicator"
  - "outline: 2px solid with offset-2"
  - "tabindex: -1 (programmatic), 0 (natural order)"
semantic_html: [nav, main, section, article, aside, header, footer]
testing_tools: [NVDA, VoiceOver, JAWS, axe-core, Lighthouse]
```

## Key Concepts

| Concept | Requirements | Implementation | When to Use |
|---------|-------------|----------------|-------------|
| **WCAG 2.1 AA** | 4.5:1 contrast normal text, 3:1 large text, keyboard access | Test with axe-core, manual keyboard nav | All production interfaces |
| **ARIA Labels** | Descriptive names when HTML insufficient | `aria-label="Close dialog"`, `aria-describedby="help-text"` | Complex widgets, dynamic content |
| **Focus Management** | Visible indicator, logical tab order | `ref.current.focus()`, focus-trap libs | Modals, SPAs, dynamic content |
| **Keyboard Nav** | Tab/Shift+Tab, Enter/Space, Escape, arrows | Event handlers for all interactive elements | All user interfaces |
| **Screen Readers** | Live regions, landmarks, heading hierarchy | `aria-live="polite"`, semantic HTML | Dynamic content, page structure |
| **Color Independence** | Never color-only information | Icons + text, patterns, sufficient contrast | Data visualization, status indicators |

## Patterns

**Modal Dialog A11Y**:
```jsx
// Focus trap + ARIA
<div role="dialog" aria-modal="true" aria-labelledby="title">
  <h2 id="title">Confirm Delete</h2>
  <p id="desc">This action cannot be undone.</p>
  <button onClick={confirm}>Delete</button>
  <button onClick={cancel} ref={cancelRef}>Cancel</button>
</div>
// Focus cancelRef on mount, restore to trigger on unmount
```

**Form Field Pattern**:
```jsx
// Semantic association + error handling
<div>
  <label htmlFor="email">Email Address</label>
  <input 
    id="email" 
    type="email"
    aria-describedby={error ? "email-error" : undefined}
    aria-invalid={error ? "true" : "false"}
  />
  {error && <div id="email-error" role="alert">{error}</div>}
</div>
```

**Data Table Accessibility**:
```jsx
// Headers association + caption
<table role="table">
  <caption>Sales Data Q4 2025</caption>
  <thead>
    <tr><th scope="col">Product</th><th scope="col">Revenue</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Widget A</th><td>$50K</td></tr>
  </tbody>
</table>
```

## Golden Rules

**Semantic First, ARIA Second**: Use proper HTML elements (button, input, nav) before adding ARIA. Screen readers understand semantic HTML natively. ARIA repairs broken semantics but native HTML is more reliable and performant.

**Test With Real Users**: Automated tools catch ~30% of issues. Manual keyboard testing reveals navigation problems. Screen reader testing uncovers announcement issues. User testing with disabled users provides authentic feedback.

**Progressive Enhancement**: Ensure core functionality works without JavaScript. Add interactive enhancements that degrade gracefully. Support reduced motion preferences via prefers-reduced-motion media query. Provide text alternatives for all media.

## References

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [Radix Primitives](https://radix-ui.com/primitives) - Built-in accessibility
- [axe-core Testing](https://github.com/dequelabs/axe-core)
- [WebAIM Screen Reader Survey](https://webaim.org/projects/screenreadersurvey9/)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_accessibility_a11y]] | sibling | 0.87 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.36 |
| [[p06_schema_a11y_checklist]] | downstream | 0.34 |
| [[p09_ct_component_template]] | downstream | 0.25 |
| [[n02_kc_shadcn_radix_patterns]] | sibling | 0.20 |
| [[p05_qg_product_tour]] | downstream | 0.19 |
| [[bld_examples_landing_page]] | related | 0.19 |
| [[p09_lpt_landing_page_template]] | downstream | 0.18 |
| [[bld_quality_gate_landing_page]] | downstream | 0.18 |
| [[p03_pt_visual_frontend_marketing]] | downstream | 0.18 |
