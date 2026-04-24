---
id: p12_dr_visual_frontend_marketing
title: "Dispatch Rule Marketing"
kind: dispatch_rule
8f: F8_collaborate
pillar: P12
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n02_visual_frontend_marketing
domain: visual_frontend_engineering_and_copywriting
quality: 9.1
tags: [dispatch_rule, visual-frontend, marketing, N02, html, tailwind, routing]
tldr: Route to N02 for HTML/CSS generation with Tailwind + shadcn/ui AND copywriting tasks — dual-role visual frontend engineer + copywriter.
scope: visual_frontend_and_marketing_creative
keywords: [html, frontend, landing, visual, design, tailwind, component, css, responsive, a11y, dark_mode, typography, copy, copywriting, ad, ads, headline, CTA, campaign, email, brand_voice, social_media, anuncio, campanha, redacao]
agent_group: n02-visual-marketing-hub
model: claude-sonnet-4-6
model_fallback: claude-opus-4-6
cli: claude
priority: 8
confidence_threshold: 0.70
fallback: n07-orchestrator
density_score: 1.0
related:
  - p08_ac_visual_frontend_marketing
  - p02_agent_visual_frontend_marketing
  - p12_wf_visual_frontend_marketing
  - p03_ap_visual_frontend_marketing
  - p03_sp_visual_frontend_marketing
  - p07_sr_visual_frontend_marketing
  - p03_pt_visual_frontend_marketing
  - p11_qg_visual_frontend_marketing
  - spec_n02_visual_frontend_engineer
  - spec_n02_part2
---

# Visual Frontend + Marketing Dispatch Rule

## Purpose

Routes dual-role tasks to N02 (Visual Frontend Engineer + Marketing Nucleus).
N02 handles both:
- **VISUAL MODE**: HTML/CSS generation with Tailwind CSS, shadcn/ui components, responsive design, accessibility
- **COPY MODE**: Persuasive content — ads, emails, headlines, brand voice, social media
- **DUAL MODE**: Integrated pages where copy and visual work together

## Trigger Conditions

### VISUAL MODE Triggers - Route to N02 when request contains:

| Category | English Keywords | Portuguese Keywords |
|----------|-----------------|---------------------|
| HTML Generation | html, build page, create page, web page | html, página web, criar página |
| Frontend Development | frontend, front-end, css, styling | frontend, front-end, estilização |
| Tailwind CSS | tailwind, utility classes, css framework | tailwind, classes utilitárias |
| Components | component, button, form, card, navbar | componente, botão, formulário |
| Layout & Design | layout, design, visual, grid, flexbox | layout, design, visual, grid |
| Responsive Design | responsive, mobile, breakpoints, mobile-first | responsivo, mobile, dispositivos |
| Accessibility | accessibility, a11y, wcag, screen reader | acessibilidade, a11y |
| Landing Pages | landing page, hero section, above the fold | página de destino, LP, hero |
| Dark Mode | dark mode, light mode, theme toggle | modo escuro, modo claro |
| Typography | typography, fonts, text styling, hierarchy | tipografia, fontes, hierarquia |

### COPY MODE Triggers - Route to N02 when request contains:

| Category | English Keywords | Portuguese Keywords |
|----------|-----------------|---------------------|
| Copy writing | copy, copywriting, ad copy, write ad | copy, redação, texto publicitário |
| Advertising | ad, ads, advertisement, banner ad | anuncio, anúncio, publicidade |
| Headlines | headline, subject line, title, hook | titulo, manchete, assunto de email |
| CTAs | CTA, call to action, button text | botão, chamada para ação |
| Campaigns | campaign, campaign brief, creative brief | campanha, briefing |
| Email | email sequence, nurture, cold email | sequência de email, email marketing |
| Brand | brand voice, tone of voice, messaging | voz da marca, tom de voz |
| Social | social media post, caption, Instagram | post, legenda, redes sociais |

### DUAL MODE Triggers - Route to N02 when request contains BOTH visual AND copy keywords

### Do NOT route to N02:

| Task | Route To | Reason |
|------|----------|--------|
| Backend development, APIs, databases | N05 | Server-side code and deployment |
| Statistical analysis, A/B test results | N01 | Research and data analysis |
| Market research with large doc sets | N01 | Document analysis and intelligence |
| Sales pricing strategy, monetization | N06 | Commercial strategy |
| Build tools, webpack, bundlers | N05 | Development infrastructure |
| Legal review of copy claims | Human | Compliance and legal validation |

## Mode Detection Logic

```python
def detect_mode(task_text):
    visual_keywords = ["html", "frontend", "tailwind", "component", "responsive", 
                       "design", "css", "layout", "visual", "a11y", "dark_mode"]
    copy_keywords = ["copy", "ad", "headline", "CTA", "email", "campaign", 
                     "brand_voice", "social", "copywriting"]
    
    has_visual = any(kw in task_text.lower() for kw in visual_keywords)
    has_copy = any(kw in task_text.lower() for kw in copy_keywords)
    
    if has_visual and has_copy:
        return "DUAL"
    elif has_visual:
        return "VISUAL"
    elif has_copy:
        return "COPY"
    else:
        return "UNCLEAR"
```

## Routing Logic

```
mode = detect_mode(task.text)

IF mode in ["VISUAL", "COPY", "DUAL"] AND confidence >= 0.70:
    route → n02-visual-marketing-hub (claude, sonnet+opus, anthropic_max)
    handoff_note: mode={mode}
ELIF mode == "UNCLEAR" AND confidence < 0.70:
    request clarification → ask "is this a visual/frontend task, copy task, or both?"
ELIF n02-visual-marketing-hub unavailable:
    escalate → n07-orchestrator
```

## Keyword Rationale

Keywords cover:
- **Visual**: HTML generation, Tailwind CSS, component creation, responsive design, accessibility
- **Copy**: Direct copy requests, channel-specific writing (email/social/ads), structural elements (headline/CTA/hook)
- **Dual**: Tasks requiring both visual implementation and persuasive copy
- **Multilingual**: Portuguese variants for bilingual CEX operation

## Confidence Calibration

### Visual Mode Signals
| Signal | Confidence Boost |
|--------|----------------|
| User says "build/create HTML page/component" | +0.35 |
| Mentions Tailwind CSS or utility classes | +0.30 |
| Requests responsive design or mobile-first | +0.25 |
| Mentions accessibility (a11y, WCAG) | +0.20 |
| Asks for dark mode implementation | +0.20 |
| References shadcn/ui or specific components | +0.25 |

### Copy Mode Signals  
| Signal | Confidence Boost |
|--------|----------------|
| User says "write copy for..." | +0.30 |
| Task contains product name + audience + benefit | +0.20 |
| Channel mentioned (email, ad, landing page) | +0.15 |
| Portuguese copy keywords (anuncio, campanha, redação) | +0.25 |
| Requests A/B variants or headlines | +0.20 |

### DUAL Mode Signals
| Signal | Confidence Boost |
|--------|----------------|
| "Build landing page with copy" or "integrated page" | +0.40 |
| Mentions both design AND copy elements | +0.35 |
| Requests "visual + persuasive" or "designed copy" | +0.30 |

### Negative Signals (route elsewhere)
| Signal | Confidence Penalty | Route To |
|--------|-------------------|----------|
| Task is statistical/analytical | −0.50 | N01/N04 |
| Mentions backend, API, database | −0.60 | N05 |
| Requests pricing strategy or monetization | −0.40 | N06 |
| Legal compliance or claim review | −0.70 | Human |

## Fallback Policy

If `n02-visual-marketing-hub` is unavailable: escalate to `n07-orchestrator` with task description.
N07 will either retry N02 or provide manual handoff instructions.

For Opus fallback (HTML-heavy tasks): N02 automatically escalates to claude-opus-4-6 when task complexity exceeds Sonnet capabilities.

## Dispatch Command

```bash
# Solo dispatch with mode detection
bash _spawn/dispatch.sh solo n02 "build responsive landing page with persuasive copy"

# Grid batch processing
bash _spawn/dispatch.sh grid MISSION_NAME

# Mode-specific examples:
# VISUAL: "create tailwind component with dark mode"
# COPY: "write email sequence for new product launch"  
# DUAL: "build landing page with integrated AIDA copy structure"
```

## Handoff Template

```markdown
# N02 Task — [MODE] [Brief Description]
**Mode**: [VISUAL | COPY | DUAL]
**Detected keywords**: [list matched keywords]
**Confidence**: [0.70-1.00]

## Task Description
[Original user request]

## Mode Context
[For VISUAL: component requirements, responsive needs, accessibility level]
[For COPY: audience, funnel stage, copy formula preference]
[For DUAL: integration requirements, visual hierarchy needs]
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_ac_visual_frontend_marketing]] | upstream | 0.67 |
| [[p02_agent_visual_frontend_marketing]] | upstream | 0.62 |
| [[p12_wf_visual_frontend_marketing]] | related | 0.59 |
| [[p03_ap_visual_frontend_marketing]] | upstream | 0.59 |
| [[p03_sp_visual_frontend_marketing]] | upstream | 0.54 |
| [[p07_sr_visual_frontend_marketing]] | upstream | 0.50 |
| [[p03_pt_visual_frontend_marketing]] | upstream | 0.45 |
| [[p11_qg_visual_frontend_marketing]] | upstream | 0.44 |
| [[spec_n02_visual_frontend_engineer]] | upstream | 0.40 |
| [[spec_n02_part2]] | upstream | 0.35 |
