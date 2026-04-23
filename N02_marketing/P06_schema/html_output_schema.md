---
id: p10_hos_html_output_visual_frontend
kind: input_schema
pillar: P10
title: HTML Output Schema for Visual Frontend Engineering
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend_marketing
target_artifact: html_component
output_format: html_with_frontmatter
validation_rules: [w3c_valid, lighthouse_90_plus, wcag_aa, responsive_mobile_first]
required_frontmatter: [component, responsive, a11y_compliant, dark_mode, lighthouse_target]
domain: visual_frontend_engineering
quality: 9.1
tags: [input_schema, html, output, visual-frontend, tailwind, N02, P10]
tldr: Schema definition for N02 HTML output — frontmatter + semantic HTML with Tailwind classes, WCAG AA compliance, Lighthouse 90+ target.
density_score: 0.96
related:
  - p03_pt_visual_frontend_marketing
  - p03_sp_visual_frontend_marketing
  - bld_examples_landing_page
  - p09_ct_component_template
  - p02_agent_visual_frontend_marketing
  - spec_n02_part2
  - p01_kc_tailwind_patterns
  - p03_ap_visual_frontend_marketing
  - p05_output_email_template
  - p08_ac_visual_frontend_marketing
---

# HTML Output Schema for Visual Frontend Engineering

## Purpose

Defines the required structure for all HTML output from N02 Visual Frontend Engineer.
Ensures consistency, validation, and quality across all generated components, pages, and layouts.

## Schema Structure

### Frontmatter (Required YAML)

```yaml
---
component: string # Component name or page type (required)
responsive: boolean # Must be true (required)
a11y_compliant: boolean # Must be true for WCAG AA (required) 
dark_mode: boolean # Dark mode support included (required)
lighthouse_target: number # Performance target, minimum 90 (required)
page_type: string # landing_page | component | email | form (optional)
breakpoints: array # [sm, md, lg, xl, 2xl] used (optional)
color_scheme: string # codexa | neutral | brand (optional)
animation_level: string # none | subtle | moderate | rich (optional)
font_stack: array # [geist, inter, jetbrains-mono] (optional)
tailwind_version: string # Version compatibility (optional)
browser_support: array # Minimum browser versions (optional)
---
```

### HTML Structure (Required Elements)

```html
<!DOCTYPE html>
<html lang="en" class="h-full">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><!-- Descriptive title --></title>
    <meta name="description" content="<!-- SEO description -->">
    <!-- Tailwind CSS CDN or custom build -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Custom Tailwind config if needed -->
  </head>
  <body class="min-h-screen bg-background text-foreground">
    <!-- Semantic HTML5 structure required -->
    <main>
      <!-- Component/page content -->
    </main>
  </body>
</html>
```

## Validation Rules

### Hard Requirements (Must Pass)

| Rule | Description | Validation Method |
|------|-------------|------------------|
| **W3C Valid** | Zero HTML validation errors | W3C HTML validator |
| **Lighthouse >= 90** | Performance score minimum | `lighthouse --only=performance` |
| **WCAG AA** | Accessibility compliance | `lighthouse --only=accessibility` |
| **Mobile Responsive** | Works on all device sizes | Browser dev tools testing |
| **Semantic HTML5** | Proper element usage | HTML5 semantic validation |
| **Zero Hardcoded Hex** | No #HEXCODE colors | Automated hex color scan |
| **Dark Mode Ready** | Dark variants present | Visual dark mode test |

### Tailwind Class Requirements

```html
<!-- Background and text colors -->
✅ class="bg-background text-foreground"
❌ style="background: white; color: black;"

<!-- Dark mode variants -->
✅ class="bg-white dark:bg-gray-900"
❌ class="bg-white" (no dark variant)

<!-- Responsive classes -->
✅ class="grid gap-4 sm:gap-6 lg:grid-cols-2"
❌ class="grid gap-4" (not responsive)

<!-- Accessibility focus states -->
✅ class="focus:ring-2 focus:ring-primary focus:ring-offset-2"
❌ class="focus:outline-none" (no alternative focus indicator)
```

## Accessibility Requirements

### ARIA Labels (Required)

```html
<!-- Interactive elements need labels -->
<button aria-label="Close dialog">×</button>

<!-- Form inputs need proper association -->
<label for="email">Email Address</label>
<input id="email" type="email" aria-describedby="email-error">
<div id="email-error" role="alert" aria-live="polite">
  <!-- Error messages -->
</div>

<!-- Navigation landmarks -->
<nav aria-label="Main navigation">
  <!-- Navigation items -->
</nav>
```

### Color Contrast (4.5:1 Minimum)

```css
/* Compliant examples */
.text-gray-900 { color: #111827; } /* on white: 16.9:1 ratio */
.text-blue-600 { color: #2563eb; } /* on white: 8.6:1 ratio */

/* Non-compliant (avoid) */
.text-gray-400 { color: #9ca3af; } /* on white: 2.8:1 ratio */
```

## Component Output Templates

### Basic Component Template

```html
---
component: button_primary
responsive: true
a11y_compliant: true
dark_mode: true
lighthouse_target: 90
---

<!DOCTYPE html>
<html lang="en" class="h-full">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Primary Button Component</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body class="min-h-screen bg-background p-8">
    
    <div class="space-y-4">
      <!-- Component variants -->
      <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-primary focus:ring-offset-2 px-4 py-2 rounded-md font-medium transition-colors">
        Primary Button
      </button>
      
      <button class="bg-secondary text-secondary-foreground hover:bg-secondary/90 focus:ring-2 focus:ring-secondary focus:ring-offset-2 px-4 py-2 rounded-md font-medium transition-colors">
        Secondary Button
      </button>
      
      <button class="bg-destructive text-destructive-foreground hover:bg-destructive/90 focus:ring-2 focus:ring-destructive focus:ring-offset-2 px-4 py-2 rounded-md font-medium transition-colors">
        Destructive Button
      </button>
    </div>
    
  </body>
</html>
```

### Landing Page Template

```html
---
component: landing_page_hero
responsive: true
a11y_compliant: true
dark_mode: true
lighthouse_target: 90
page_type: landing_page
breakpoints: [sm, md, lg, xl]
---

<!DOCTYPE html>
<html lang="en" class="h-full">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Landing Page</title>
    <meta name="description" content="Convert more visitors with our proven solution">
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body class="min-h-screen bg-background text-foreground">
    
    <!-- Hero Section -->
    <main>
      <section class="container mx-auto px-4 py-16 sm:px-6 lg:px-8">
        <div class="grid gap-8 lg:grid-cols-2 lg:gap-16">
          
          <!-- Content Column -->
          <div class="space-y-6 lg:space-y-8">
            <h1 class="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl">
              <!-- Headline goes here -->
            </h1>
            
            <p class="text-xl text-muted-foreground sm:text-2xl">
              <!-- Subheadline goes here -->
            </p>
            
            <div class="flex flex-col gap-4 sm:flex-row">
              <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-primary focus:ring-offset-2 px-6 py-3 rounded-lg text-lg font-medium transition-colors">
                Get Started Today
              </button>
              
              <button class="border border-input hover:bg-accent hover:text-accent-foreground focus:ring-2 focus:ring-ring focus:ring-offset-2 px-6 py-3 rounded-lg text-lg font-medium transition-colors">
                Learn More
              </button>
            </div>
          </div>
          
          <!-- Visual Column -->
          <div class="lg:order-first">
            <!-- Hero image or visual element -->
            <div class="aspect-video rounded-lg bg-muted"></div>
          </div>
          
        </div>
      </section>
    </main>
    
  </body>
</html>
```

## Error Prevention

### Common Mistakes to Avoid

| Mistake | Problem | Correct Approach |
|---------|---------|-----------------|
| Missing semantic tags | Poor accessibility | Use header, main, section, article |
| Hardcoded colors | Design system breaks | Use Tailwind color tokens |
| No dark mode | Poor UX | Include dark: variants |
| Fixed pixel widths | Not responsive | Use responsive units (rem, %, vw) |
| Missing focus states | Keyboard users excluded | Add focus:ring-* classes |
| No alt attributes | Screen readers blocked | Add descriptive alt text |
| Generic button text | Poor accessibility | Use descriptive aria-label |

### Quality Assurance Checklist

```markdown
Before Output Delivery:
- [ ] Frontmatter complete with all required fields
- [ ] W3C HTML validation passes (0 errors)
- [ ] Lighthouse performance >= 90
- [ ] Lighthouse accessibility >= 95
- [ ] Color contrast >= 4.5:1 for all text
- [ ] Mobile responsive behavior tested
- [ ] Dark mode variants working
- [ ] Keyboard navigation functional
- [ ] Zero hardcoded hex colors
- [ ] Semantic HTML5 structure used
- [ ] All interactive elements have focus states
- [ ] Images have descriptive alt attributes
```

## Integration with CEX System

### Compilation

```bash
# After HTML generation, compile to YAML for CEX system
python _tools/cex_compile.py N02_marketing/P05_output/component_name.md

# Validation pipeline
python _tools/cex_doctor.py  # Health check
lighthouse component_name.html --only=performance,accessibility
```

### Handoff to N05

For deployment, N02 hands off validated HTML to N05 (Operations) with:
- Lighthouse audit results
- Browser compatibility notes  
- Responsive breakpoint validation
- Accessibility compliance certificate

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_pt_visual_frontend_marketing]] | upstream | 0.44 |
| [[p03_sp_visual_frontend_marketing]] | upstream | 0.40 |
| [[bld_examples_landing_page]] | upstream | 0.37 |
| [[p09_ct_component_template]] | upstream | 0.35 |
| [[p02_agent_visual_frontend_marketing]] | upstream | 0.34 |
| [[spec_n02_part2]] | upstream | 0.33 |
| [[p01_kc_tailwind_patterns]] | upstream | 0.33 |
| [[p03_ap_visual_frontend_marketing]] | upstream | 0.32 |
| [[p05_output_email_template]] | upstream | 0.30 |
| [[p08_ac_visual_frontend_marketing]] | upstream | 0.30 |
