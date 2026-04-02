---
id: p06_schema_a11y_checklist
kind: input_schema
pillar: P06
title: "WCAG 2.1 AA Accessibility Checklist"
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend
domain: frontend
quality: 9.1
tags: [schema, a11y, wcag, accessibility, frontend]
tldr: "WCAG 2.1 Level AA compliance checklist for all N02 HTML output."
density_score: 0.92
---

# WCAG 2.1 AA Accessibility Checklist

## Schema Purpose
Every HTML artifact produced by N02 MUST pass this checklist before publish.
Based on `kc_accessibility_a11y.md` — Radix primitives provide built-in a11y.

---

## 1. Perceivable

| Check | Rule | Threshold | Required |
|-------|------|-----------|----------|
| P1.1 | All `<img>` have `alt` attribute | 100% coverage | yes |
| P1.2 | Decorative images use `alt=""` | role="presentation" or empty alt | yes |
| P1.3 | Video/audio has captions or transcript | when media present | yes |
| P1.4 | Text contrast ratio (normal text) | >= 4.5:1 | yes |
| P1.5 | Text contrast ratio (large text >= 18px) | >= 3:1 | yes |
| P1.6 | No information conveyed by color alone | icon + text + color | yes |
| P1.7 | Content reflows at 320px without horizontal scroll | responsive | yes |

## 2. Operable

| Check | Rule | Threshold | Required |
|-------|------|-----------|----------|
| O2.1 | All interactive elements keyboard accessible | Tab/Shift+Tab/Enter/Escape | yes |
| O2.2 | Focus indicator visible | `focus-visible` outline >= 2px | yes |
| O2.3 | No keyboard traps | Escape always exits | yes |
| O2.4 | Skip-to-content link present | first focusable element | yes |
| O2.5 | Touch targets minimum size | >= 48x48px on mobile | yes |
| O2.6 | No auto-play media or animation > 5s | pause/stop control | yes |
| O2.7 | `prefers-reduced-motion` respected | disable animations when set | yes |

## 3. Understandable

| Check | Rule | Threshold | Required |
|-------|------|-----------|----------|
| U3.1 | `<html lang="xx">` attribute present | ISO 639-1 code | yes |
| U3.2 | Form inputs have visible `<label>` | associated via `for`/`id` | yes |
| U3.3 | Error messages descriptive | what went wrong + how to fix | yes |
| U3.4 | Consistent navigation across pages | same order, same location | yes |
| U3.5 | No unexpected context changes on input | no auto-submit on select | yes |

## 4. Robust

| Check | Rule | Threshold | Required |
|-------|------|-----------|----------|
| R4.1 | Valid HTML5 (W3C validator) | 0 errors | yes |
| R4.2 | ARIA roles used correctly | no redundant roles on semantic elements | yes |
| R4.3 | Heading hierarchy (h1→h6) no skips | h1 unique, sequential | yes |
| R4.4 | Semantic HTML elements used | nav/main/section/article/aside/header/footer | yes |
| R4.5 | Custom components have ARIA equivalents | Radix primitives preferred | yes |

---

## Validation Command

```yaml
validation:
  tool: lighthouse
  flags: "--only=accessibility"
  threshold: 95
  fallback_manual:
    - contrast_checker: "https://webaim.org/resources/contrastchecker/"
    - html_validator: "https://validator.w3.org/"
    - screen_reader: "NVDA or VoiceOver manual test"
```

## Pass Criteria

- **All "required: yes" checks** must pass
- Lighthouse Accessibility score >= 95
- Zero ARIA misuse warnings
- Heading hierarchy validated
