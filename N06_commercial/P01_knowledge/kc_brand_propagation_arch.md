---
id: p01_kc_brand_propagation_arch
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Brand Propagation Architecture"
version: 1.0.0
created: 2026-04-01
author: shaka_research
domain: brand-identity
quality: 9.2
updated: 2026-04-07
tags: [brand, design-tokens, style-dictionary, css-variables, propagation, theming, prompt-injection, atomic-design]
tldr: "3-layer architecture (primitive > semantic > component), brand-to-code pipeline, Style Dictionary, multi-platform, and prompt injection"
when_to_use: "When implementing brand_config.yaml → design tokens → CSS variables pipeline, or configuring brand propagation across nuclei."
keywords: [design-tokens, style-dictionary, brand-propagation, css-variables, atomic-design, prompt-injection]
density_score: 0.93
axioms:
  - "ALWAYS propagate from brand_config.yaml outward -- never hardcode brand values in components."
  - "NEVER edit tokens directly -- edit brand-guidelines.md first, then compile."
  - "ALWAYS use semantic token layer between primitives and components."
linked_artifacts:
  primary: p01_kc_brand_tokens_pipeline
  related: [n06_output_visual_identity, n06_schema_brand_config, n06_output_brand_config]
related:
  - p01_kc_design_token_arch
  - p12_wf_brand_propagation
  - p01_kc_color_theory_applied
  - n02_kc_color_theory_applied
  - p01_kc_brand_tokens_pipeline
  - p01_kc_brand_skill
  - n06_output_visual_identity
  - p05_output_email_template
  - p04_browser_design_extractor
  - n02_kc_email_html_responsive
---

# Brand Propagation Architecture

## 1. Design Tokens: W3C Concept and Specification

### What Are Design Tokens
Design Tokens are design decisions encoded as variables — the **single source of truth** connecting brand decisions to executable code on any platform. ROI: one token change propagates to every component, every platform, every theme — zero manual per-file updates.

Instead of hardcoding `color: #E87C3E` in each component, you declare:
```json
"color-brand-primary": { "$value": "#E87C3E", "$type": "color" }
```
...e todos os sistemas consomem essa variavel. Mudar o token muda tudo.

### DTCG Specification (W3C Community Group)
The DTCG (Design Tokens Community Group) released the first stable spec version in October 2025. This is the industry standard — any token tooling investment should target DTCG format for maximum interoperability.

**DTCG format (tokens.json):**
```json
{
  "color": {
    "brand": {
      "primary": {
        "$value": "#E87C3E",
        "$type": "color",
        "$description": "Cor principal da marca, usada em CTAs e highlights"
      },
      "secondary": {
        "$value": "#2D4A8A",
        "$type": "color"
      }
    }
  },
  "spacing": {
    "base": {
      "$value": "8px",
      "$type": "dimension"
    }
  }
}
```

**Types supported by DTCG:**
- `color` — hex, RGB, HSL values
- `dimension` — px, rem, em
- `fontFamily`, `fontWeight`, `fontSize`, `lineHeight`
- `duration` — for animations (ms)
- `cubicBezier` — easing functions
- `number`, `string`, `boolean`

**Alias (cross-token references):**
```json
{
  "button": {
    "background": {
      "$value": "{color.brand.primary}",
      "$type": "color"
    }
  }
}
```

---

## 2. Three-Layer Token Architecture

```
PRIMITIVE (Global)        ->    SEMANTIC (Role)          ->    COMPONENT (Application)
-------------------------------------------------------------------------------------
Raw values                 Contextual meaning             Component-specific binding

blue-400: #4A90E2          color-interactive: blue-400    button-bg-primary: color-interactive
space-4: 4px               spacing-tight: space-4         card-padding: spacing-tight
font-bold: 700             font-emphasis: font-bold       heading-weight: font-emphasis
```

### Layer 1: Primitive Tokens (Palette)
- All possible values in the design system
- No semantic context — raw values only
- Never used directly in components
- Example: `red-100` through `red-900`, `space-1` through `space-64`

### Layer 2: Semantic Tokens (Roles)
- Give contextual meaning to primitives
- These are what changes between themes (light/dark) — the ROI layer for white-labeling
- Example: `color-background-primary`, `color-text-muted`, `color-border-subtle`

### Layer 3: Component Tokens (Applications)
- Map semantic to specific component usage
- Allow per-component override without breaking others — the customization layer
- Example: `button-background-hover`, `card-border-radius`, `input-focus-ring`

---

## 3. Brand Propagation Pipeline

```
brand_config.yaml
      │
      ▼
guidelines.md (documento humano de identidade)
      │
      ▼
tokens.json (DTCG format — fonte de verdade maquina)
      │
      ├─────────────────────┬──────────────────────┬────────────────────
      ▼                     ▼                       ▼
CSS Custom Properties    Swift Constants         Kotlin Constants
(web)                   (iOS)                   (Android)
      │                     │                       │
      ▼                     ▼                       ▼
React components        SwiftUI views           Compose composables
      │
      ▼
LLM Prompt Templates (brand voice injection)
```

### brand_config.yaml (master file — single source of truth)
```yaml
brand:
  name: "Agua Marinha"
  tagline: "Sua casa, sua historia"
  
  colors:
    primary: "#4A9B8E"      # Agua marinha
    secondary: "#F4C669"    # Dourado areia
    neutral_100: "#FAF8F5"
    neutral_900: "#1A1A1A"
  
  typography:
    heading: "Playfair Display"
    body: "Inter"
    base_size: "16px"
  
  voice:
    tone: ["acolhedor", "sofisticado", "acessivel"]
    avoid: ["corporativo", "tecnico", "distante"]
    persona: "Consultora de decoracao que e tambem amiga"
  
  spacing:
    unit: 8
    scale: [4, 8, 16, 24, 32, 48, 64, 96, 128]
```

---

## 4. Style Dictionary

Style Dictionary (Amazon) e o sistema de build que transforma `tokens.json` em codigo especifico por plataforma.

### Config Basica (config.json)
```json
{
  "source": ["tokens/**/*.json"],
  "platforms": {
    "css": {
      "transformGroup": "css",
      "buildPath": "build/css/",
      "files": [{
        "destination": "variables.css",
        "format": "css/variables"
      }]
    },
    "ios": {
      "transformGroup": "ios-swift",
      "buildPath": "build/ios/",
      "files": [{
        "destination": "StyleDictionary.swift",
        "format": "ios-swift/class.swift"
      }]
    },
    "android": {
      "transformGroup": "android",
      "buildPath": "build/android/",
      "files": [{
        "destination": "tokens.xml",
        "format": "android/resources"
      }]
    }
  }
}
```

### Output por Plataforma
**CSS (web):**
```css
:root {
  --color-brand-primary: #4A9B8E;
  --color-brand-secondary: #F4C669;
  --spacing-base: 8px;
  --font-heading: 'Playfair Display', serif;
}
```

**Swift (iOS):**
```swift
public class StyleDictionary {
  public static let colorBrandPrimary = UIColor(red: 74/255, green: 155/255, blue: 142/255, alpha: 1)
  public static let spacingBase = CGFloat(8)
}
```

**Kotlin (Android):**
```kotlin
object StyleDictionary {
  val colorBrandPrimary = Color.parseColor("#4A9B8E")
  val spacingBase = 8.dp
}
```

---

## 5. Token Naming Convention

### Pattern: category-type-item-subitem-state
```
color  - background - primary  - [null]   - [null]    → color-background-primary
color  - text       - body      - [null]   - disabled  → color-text-body-disabled
space  - [null]     - stack     - tight    - [null]    → space-stack-tight
font   - size       - heading   - xl       - [null]    → font-size-heading-xl
border - radius     - button    - [null]   - [null]    → border-radius-button
```

### Rules
1. Always kebab-case
2. Start with category (color, space, font, border, shadow, motion)
3. Never use raw values in semantic names (`blue-400` is primitive, never semantic)
4. State suffix at the end: `hover`, `focus`, `disabled`, `active`, `selected`
5. Theme as optional prefix: `dark-color-background-primary`

---

## 6. Brand Prompt Injection

### Concept
Extract brand identity from `brand_config.yaml` and automatically inject into LLM prompts — ensures voice consistency without manual redefinition. ROI: eliminates "make it sound more like us" revision cycles. One system prompt block, consistent across every AI-generated output.

### Injection Template (Mustache)
```
{{#brand}}
Voce e um assistente de {{name}}.

IDENTIDADE DE MARCA:
- Tom: {{voice.tone}}
- Evite: {{voice.avoid}}
- Persona: {{voice.persona}}
- Tagline: {{tagline}}

PALETA VISUAL (para descricoes de imagem):
- Cor principal: {{colors.primary}}
- Estilo: elegante, acolhedor, harmonioso

ALWAYS respond in the tone defined above.
{{/brand}}
```

### Build Pipeline
```bash
# 1. Ler brand_config.yaml
# 2. Renderizar templates Mustache com variaveis da marca
# 3. Output: system_prompt_{sat}.md, image_prompt_template.md, etc.

python scripts/inject_brand.py \
  --config brand_config.yaml \
  --template templates/llm_system_prompt.mustache \
  --output .claude/prompts/system_brand.md
```

---

## 7. Multi-Platform Propagation

### Platform Usage Map
| Platform | Token Format | Mechanism |
|------------|-----------------|-----------|
| **Web** | CSS Custom Properties | `var(--color-brand-primary)` |
| **React Native** | JS/TS object | `StyleSheet.create({ bg: tokens.colorBrandPrimary })` |
| **iOS** | Swift UIColor/CGFloat | `StyleDictionary.colorBrandPrimary` |
| **Android** | XML resources / Kotlin | `@color/color_brand_primary` |
| **Email** | Inline CSS | Tokens compilados como strings hex diretos |
| **Figma** | Tokens Plugin / Variables | Sincronizado via Tokens Studio |
| **Docs** | Markdown/MDX | Tokens renderizados como swatches |

### Email (special case — highest conversion-impact surface)
Email clients do not support CSS variables. Use Style Dictionary with a custom formatter:
```json
{
  "platforms": {
    "email": {
      "transformGroup": "js",
      "files": [{
        "format": "javascript/es6",
        "destination": "emailTokens.js"
      }]
    }
  }
}
```

---

## 8. Theming: Light / Dark / Custom

### How to Support Multiple Themes from 1 brand_config.yaml
```yaml
themes:
  light:
    color-background-primary: "{color.neutral.100}"
    color-text-primary: "{color.neutral.900}"
  dark:
    color-background-primary: "{color.neutral.900}"
    color-text-primary: "{color.neutral.100}"
  brand-custom:
    color-background-primary: "{color.brand.primary}"
    color-text-primary: "#FFFFFF"
```

**CSS output with theme support:**
```css
:root { --color-background-primary: #FAF8F5; }
[data-theme="dark"] { --color-background-primary: #1A1A1A; }
[data-theme="brand"] { --color-background-primary: #4A9B8E; }
```

---

## 9. Brand Consistency Automation (Linting)

### Stylelint Rules for Tokens
```json
{
  "rules": {
    "custom-property-pattern": "^(color|space|font|border|shadow|motion)-",
    "color-no-invalid-hex": true,
    "declaration-property-value-allowed-list": {
      "color": ["/^var\\(--color-/"]
    }
  }
}
```

**What this enforces**: no developer hardcodes `color: #E87C3E` — forced to use `var(--color-brand-primary)`. Brand consistency is automated, not policed. Cost of drift: zero.

### ESLint Plugin for Design Tokens
```js
// Bloqueia valores magicos de cor em componentes React
"no-restricted-syntax": ["error", {
  "selector": "Property[key.name='color'][value.type='Literal']",
  "message": "Use design tokens: import { tokens } from '@/tokens'"
}]
```

---

## 10. Mustache Variable Pattern (Build-Time Brand Injection)

### Template Structure
```
brand_config.yaml          (fonte de verdade)
      │
      ├── templates/
      │   ├── README.mustache        → README.md (com nome da marca)
      │   ├── system_prompt.mustache → prompts/system.md
      │   ├── email_header.mustache  → email/header.html
      │   └── landing_hero.mustache  → landing/hero.tsx
      │
      └── scripts/
          └── build_brand.py         (renderiza todos os templates)
```

### Template Example
```mustache
# Bem-vindo a {{brand.name}}

{{brand.tagline}}

Nossos valores: {{#brand.values}}{{.}}, {{/brand.values}}

Cor principal: {{brand.colors.primary}}
```

### Build Script
```python
import yaml, chevron, glob, os

with open("brand_config.yaml") as f:
    config = yaml.safe_load(f)

for tmpl in glob.glob("templates/**/*.mustache"):
    with open(tmpl) as f:
        rendered = chevron.render(f, config)
    out = tmpl.replace("templates/", "build/").replace(".mustache", "")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(rendered)
```

---

## 11. Atomic Design (Application Context)

Brad Frost defines 5 component levels — tokens permeate all levels:

| Level | Description | Uses Tokens? |
|-------|-------------|-------------|
| **Atoms** | Basic elements (button, input, icon) | Directly (layer 3: component) |
| **Molecules** | Atom combinations (form field = label + input + error) | Via atoms |
| **Organisms** | Complex sections (header, product card grid) | Via molecules |
| **Templates** | Layout without real content | Structural |
| **Pages** | Templates with real content | Content |

---

## References
- [Design Tokens W3C Spec v2025.10](https://www.designtokens.org/tr/2025.10/format/)
- [DTCG Community Group](https://www.w3.org/community/design-tokens/)
- [Style Dictionary — GitHub](https://github.com/style-dictionary/style-dictionary)
- [Style Dictionary + DTCG](https://styledictionary.com/info/dtcg/)
- [Atomic Web Design — Brad Frost](https://bradfrost.com/blog/post/atomic-web-design/)
- [Naming Tokens in Design Systems — EightShapes](https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676)
- [Design Tokens Technical Guide — Product Rocket](https://productrocket.ro/articles/design-tokens-guide/)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_design_token_arch]] | sibling | 0.48 |
| [[p12_wf_brand_propagation]] | downstream | 0.37 |
| [[p01_kc_color_theory_applied]] | sibling | 0.36 |
| [[n02_kc_color_theory_applied]] | sibling | 0.36 |
| [[p01_kc_brand_tokens_pipeline]] | sibling | 0.35 |
| [[p01_kc_brand_skill]] | sibling | 0.34 |
| [[n06_output_visual_identity]] | downstream | 0.31 |
| [[p05_output_email_template]] | downstream | 0.25 |
| [[p04_browser_design_extractor]] | downstream | 0.24 |
| [[n02_kc_email_html_responsive]] | sibling | 0.23 |
