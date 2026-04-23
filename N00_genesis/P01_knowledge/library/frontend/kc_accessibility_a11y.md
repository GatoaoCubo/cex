---
id: p01_kc_accessibility_a11y
kind: knowledge_card
pillar: P01
title: "Accessibility A11Y"
version: 1.0.0
created: 2026-04-01
author: builder
domain: frontend
quality: 9.0
tags: [knowledge, frontend]
tldr: "Accessibility A11Y patterns and best practices"
density_score: 0.88
related:
  - n02_kc_accessibility_a11y
  - p10_hos_html_output_visual_frontend
  - p06_schema_a11y_checklist
  - p09_ct_component_template
  - p03_pt_visual_frontend_marketing
  - n02_kc_shadcn_radix_patterns
  - p09_lpt_landing_page_template
  - p05_qg_product_tour
  - p03_sp_visual_frontend_marketing
  - p01_kc_tailwind_patterns
---

# Accessibility A11Y

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

**WCAG 2.1 Level AA Compliance**: Four principles (POUR) - Perceivable, Operable, Understandable, Robust. Level AA requires 1.4.3 contrast ratio 4.5:1 for normal text, 3:1 for large text, plus keyboard accessibility and time limits.

**ARIA Labeling Strategy**: aria-label provides accessible name when visible text insufficient. aria-describedby references additional description elements. aria-labelledby references multiple label sources. Use sparingly - semantic HTML preferred.

**Focus Management**: Programmatic focus control via ref.current.focus(). Focus trapping in modals using focus-trap or Radix Dialog. Skip-to-content link as first focusable element. Restore focus to trigger element on modal close.

**Keyboard Navigation Patterns**: Tab order follows visual layout. Enter activates buttons/links. Space toggles checkboxes, activates buttons. Arrow keys navigate menus/tabs/grids. Escape closes overlays. Home/End navigate to boundaries.

**Screen Reader Semantics**: Live regions (aria-live="polite") announce dynamic content. Landmark roles (banner, navigation, main, contentinfo) provide page structure. Heading hierarchy (h1-h6) creates outline. Lists (ul/ol) group related items.

**Color Independence**: Never rely solely on color to convey information. Add icons, patterns, or text indicators. Use sufficient contrast ratios. Support high contrast mode. Provide pattern/texture alternatives to color coding.

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
| [[n02_kc_accessibility_a11y]] | sibling | 0.83 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.38 |
| [[p06_schema_a11y_checklist]] | downstream | 0.32 |
| [[p09_ct_component_template]] | downstream | 0.27 |
| [[p03_pt_visual_frontend_marketing]] | downstream | 0.20 |
| [[n02_kc_shadcn_radix_patterns]] | sibling | 0.20 |
| [[p09_lpt_landing_page_template]] | downstream | 0.19 |
| [[p05_qg_product_tour]] | downstream | 0.19 |
| [[p03_sp_visual_frontend_marketing]] | downstream | 0.18 |
| [[p01_kc_tailwind_patterns]] | sibling | 0.18 |
