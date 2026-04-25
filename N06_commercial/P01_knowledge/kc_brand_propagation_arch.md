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

## 1. Design Tokens: Conceito e Especificacao W3C

### O que sao Design Tokens
Design Tokens sao as decisoes de design codificadas como variaveis — a **fonte unica de verdade** que conecta decisoes de marca a codigo executavel em qualquer plataforma.

Ao inves de hardcodar `color: #E87C3E` em cada componente, voce declara:
```json
"color-brand-primary": { "$value": "#E87C3E", "$type": "color" }
```
...e todos os sistemas consomem essa variavel. Mudar o token muda tudo.

### Especificacao DTCG (W3C Community Group)
O DTCG (Design Tokens Community Group) lancou a primeira versao estavel do spec em outubro de 2025.

**Formato DTCG (tokens.json):**
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

**Tipos suportados pelo DTCG:**
- `color` — cores hex, RGB, HSL
- `dimension` — px, rem, em
- `fontFamily`, `fontWeight`, `fontSize`, `lineHeight`
- `duration` — para animacoes (ms)
- `cubicBezier` — easing functions
- `number`, `string`, `boolean`

**Alias (referencia entre tokens):**
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

## 2. Arquitetura de 3 Camadas

```
PRIMITIVO (Global)        →    SEMANTICO (Role)         →    COMPONENTE (Application)
─────────────────────────────────────────────────────────────────────────────────────
Valores brutos             Significado contextual         Uso especifico por componente

blue-400: #4A90E2          color-interactive: blue-400    button-bg-primary: color-interactive
space-4: 4px               spacing-tight: space-4         card-padding: spacing-tight
font-bold: 700             font-emphasis: font-bold       heading-weight: font-emphasis
```

### Layer 1: Primitive Tokens (Paleta)
- Todos os valores possiveis do design system
- Sem contexto semantico — apenas valores
- Nao usados diretamente em componentes
- Exemplo: `red-100` thru `red-900`, `space-1` thru `space-64`

### Layer 2: Semantic Tokens (Papeis)
- Dao significado contextual aos primitivos
- Sao o que muda entre temas (light/dark)
- Exemplo: `color-background-primary`, `color-text-muted`, `color-border-subtle`

### Layer 3: Component Tokens (Aplicacoes)
- Mapeiam semantico para componente especifico
- Permitem override por componente sem quebrar outros
- Exemplo: `button-background-hover`, `card-border-radius`, `input-focus-ring`

---

## 3. Pipeline de Propagacao de Marca

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

### brand_config.yaml (arquivo mestre)
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

## 5. Convencao de Nomenclatura de Tokens

### Padrao: categoria-tipo-item-subitem-estado
```
color  - background - primary  - [null]   - [null]    → color-background-primary
color  - text       - body      - [null]   - disabled  → color-text-body-disabled
space  - [null]     - stack     - tight    - [null]    → space-stack-tight
font   - size       - heading   - xl       - [null]    → font-size-heading-xl
border - radius     - button    - [null]   - [null]    → border-radius-button
```

### Regras
1. Sempre kebab-case
2. Comece com categoria (color, space, font, border, shadow, motion)
3. Nao use valores no nome (`blue-400` e primitivo, nunca semantico)
4. Estado no final: `hover`, `focus`, `disabled`, `active`, `selected`
5. Temas como prefixo opcional: `dark-color-background-primary`

---

## 6. Prompt Injection de Marca

### Conceito
Extrair identidade de marca do `brand_config.yaml` e injetar automaticamente em prompts de LLM — garante consistencia de voz sem redefinir manualmente.

### Template de Injeccao (Mustache)
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

### Pipeline de Build
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

### Mapa de Uso por Plataforma
| Plataforma | Formato de Token | Mecanismo |
|------------|-----------------|-----------|
| **Web** | CSS Custom Properties | `var(--color-brand-primary)` |
| **React Native** | JS/TS object | `StyleSheet.create({ bg: tokens.colorBrandPrimary })` |
| **iOS** | Swift UIColor/CGFloat | `StyleDictionary.colorBrandPrimary` |
| **Android** | XML resources / Kotlin | `@color/color_brand_primary` |
| **Email** | Inline CSS | Tokens compilados como strings hex diretos |
| **Figma** | Tokens Plugin / Variables | Sincronizado via Tokens Studio |
| **Docs** | Markdown/MDX | Tokens renderizados como swatches |

### Email (caso especial)
Email clients nao suportam CSS vars. Usar Style Dictionary com formatter customizado:
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

### Como Funcionar com 1 brand_config.yaml
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

**Output CSS com suporte a temas:**
```css
:root { --color-background-primary: #FAF8F5; }
[data-theme="dark"] { --color-background-primary: #1A1A1A; }
[data-theme="brand"] { --color-background-primary: #4A9B8E; }
```

---

## 9. Brand Consistency Automation (Linting)

### Stylelint Rule para Tokens
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

**O que isso garante**: nenhum desenvolvedor hardcoda `color: #E87C3E` — obrigado a usar `var(--color-brand-primary)`.

### ESLint Plugin para Design Tokens
```js
// Bloqueia valores magicos de cor em componentes React
"no-restricted-syntax": ["error", {
  "selector": "Property[key.name='color'][value.type='Literal']",
  "message": "Use design tokens: import { tokens } from '@/tokens'"
}]
```

---

## 10. Mustache Variable Pattern (Build-Time Brand Injection)

### Estrutura de Templates
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

### Exemplo de Template
```mustache
# Bem-vindo a {{brand.name}}

{{brand.tagline}}

Nossos valores: {{#brand.values}}{{.}}, {{/brand.values}}

Cor principal: {{brand.colors.primary}}
```

### Script de Build
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

## 11. Atomic Design (Contexto de Aplicacao)

Brad Frost define 5 niveis de componentes — tokens permeiam todos os niveis:

| Nivel | Descricao | Usa Tokens? |
|-------|-----------|-------------|
| **Atoms** | Elementos basicos (botao, input, icone) | Diretamente (layer 3: component) |
| **Molecules** | Combinacao de atoms (form field = label + input + error) | Via atoms |
| **Organisms** | Secoes complexas (header, product card grid) | Via molecules |
| **Templates** | Layout sem conteudo real | Estrutural |
| **Pages** | Templates com conteudo real | Conteudo |

---

## Referencias
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
