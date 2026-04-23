---
id: p09_lpt_landing_page_template
kind: output_validator
pillar: P09
title: Landing Page Template — Production Ready
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend_marketing
template_type: landing_page
output_format: html_with_integrated_copy
copy_formulas: [AIDA, PAS, BAB]
layout_patterns: [f_pattern, z_pattern]
sections: [hero, features, testimonials, pricing, faq, cta]
responsive: mobile_first
accessibility: wcag_aa
performance: lighthouse_90_plus
domain: visual_frontend_engineering_and_copywriting
quality: 9.0
tags: [output_template, landing_page, dual_mode, html, tailwind, copy_integration, N02]
tldr: Complete landing page template with integrated copy — hero to CTA sections, responsive design, WCAG AA, persuasion formulas in visual hierarchy.
density_score: 0.96
related:
  - p09_ct_component_template
  - p10_hos_html_output_visual_frontend
  - p05_output_style_guide
  - p03_pt_visual_frontend_marketing
  - landing_page_petshop_crm
  - bld_examples_landing_page
  - p05_output_visual_report
  - p05_output_dashboard_ui
  - p01_kc_tailwind_patterns
  - kc_tailwind_patterns
---

# Landing Page Template — Production Ready

## Purpose

Complete template for generating conversion-focused landing pages that integrate persuasive copy with visual hierarchy. Follows F/Z-pattern layout supporting PAS/AIDA copy formulas.

## Template Structure

### Complete Landing Page Template

```html
---
component: landing_page_conversion
responsive: true
a11y_compliant: true
dark_mode: true
lighthouse_target: 90
page_type: landing_page
copy_formula: PAS
layout_pattern: f_pattern
breakpoints: [sm, md, lg, xl, 2xl]
color_scheme: codexa
---

<!DOCTYPE html>
<html lang="en" class="h-full scroll-smooth">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- SEO Meta -->
    <title>{{product_name}} — {{key_benefit}}</title>
    <meta name="description" content="{{seo_description}}">
    <meta property="og:title" content="{{product_name}} — {{key_benefit}}">
    <meta property="og:description" content="{{seo_description}}">
    <meta property="og:type" content="website">
    <meta name="robots" content="index, follow">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              primary: {
                DEFAULT: '#50C878',
                foreground: '#ffffff',
                hover: '#16a34a',
              },
              background: '#ffffff',
              foreground: '#111827',
              muted: {
                DEFAULT: '#f3f4f6',
                foreground: '#6b7280',
              },
              accent: {
                DEFAULT: '#50C878',
                foreground: '#ffffff',
              },
              border: '#e5e7eb',
            },
            fontFamily: {
              sans: ['Inter', 'system-ui', 'sans-serif'],
            },
          }
        },
        darkMode: 'class',
      }
    </script>
  </head>
  
  <body class="min-h-screen bg-background text-foreground font-sans antialiased">
    
    <!-- Navigation -->
    <nav class="border-b border-border bg-background/95 backdrop-blur sticky top-0 z-50">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <!-- Logo -->
          <div class="flex items-center">
            <a href="#" class="text-xl font-bold text-foreground">
              {{product_name}}
            </a>
          </div>
          
          <!-- Navigation Links -->
          <div class="hidden md:block">
            <div class="ml-10 flex items-baseline space-x-4">
              <a href="#features" class="text-muted-foreground hover:text-foreground px-3 py-2 text-sm font-medium transition-colors">
                Features
              </a>
              <a href="#pricing" class="text-muted-foreground hover:text-foreground px-3 py-2 text-sm font-medium transition-colors">
                Pricing
              </a>
              <a href="#testimonials" class="text-muted-foreground hover:text-foreground px-3 py-2 text-sm font-medium transition-colors">
                Reviews
              </a>
            </div>
          </div>
          
          <!-- CTA Button -->
          <div class="flex items-center space-x-4">
            <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-primary focus:ring-offset-2 px-4 py-2 rounded-md text-sm font-medium transition-colors">
              {{nav_cta_text}}
            </button>
          </div>
        </div>
      </div>
    </nav>

    <main>
      <!-- Hero Section — PROBLEM (PAS Formula) -->
      <section class="py-16 sm:py-24 lg:py-32">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid gap-8 lg:grid-cols-2 lg:gap-16 items-center">
            
            <!-- Content Column (F-pattern: starts top-left) -->
            <div class="space-y-6 lg:space-y-8">
              <!-- PROBLEM: Main headline -->
              <h1 class="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl">
                {{hero_headline_v1}}
                <span class="text-primary">{{hero_headline_emphasis}}</span>
              </h1>
              
              <!-- AGITATE: Subheadline -->
              <p class="text-xl text-muted-foreground sm:text-2xl leading-relaxed">
                {{hero_subheadline_agitate}}
              </p>
              
              <!-- Social Proof Hook -->
              <p class="text-sm text-muted-foreground font-medium">
                ✓ {{social_proof_stat}} ({{social_proof_qualifier}})
              </p>
              
              <!-- Primary CTA (F-pattern: left side focal point) -->
              <div class="flex flex-col gap-4 sm:flex-row">
                <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-primary focus:ring-offset-2 px-8 py-4 rounded-lg text-lg font-semibold transition-colors shadow-lg">
                  {{primary_cta_text}}
                </button>
                
                <button class="border border-border hover:bg-muted hover:text-muted-foreground focus:ring-2 focus:ring-ring focus:ring-offset-2 px-8 py-4 rounded-lg text-lg font-medium transition-colors">
                  {{secondary_cta_text}}
                </button>
              </div>
              
              <!-- Trust Indicators -->
              <div class="flex items-center space-x-6 text-sm text-muted-foreground">
                <div class="flex items-center space-x-2">
                  <svg class="w-4 h-4 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                  </svg>
                  <span>{{trust_indicator_1}}</span>
                </div>
                <div class="flex items-center space-x-2">
                  <svg class="w-4 h-4 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                  </svg>
                  <span>{{trust_indicator_2}}</span>
                </div>
              </div>
            </div>
            
            <!-- Visual Column (F-pattern: right side support) -->
            <div class="lg:order-last">
              <div class="aspect-video rounded-2xl bg-gradient-to-br from-primary/10 to-accent/10 border border-border flex items-center justify-center">
                <!-- Hero Image/Video Placeholder -->
                <div class="text-center p-8">
                  <div class="w-16 h-16 bg-primary/20 rounded-full mx-auto mb-4 flex items-center justify-center">
                    <svg class="w-8 h-8 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h1.5a1.5 1.5 0 001.5-1.5V7a1.5 1.5 0 00-1.5-1.5H9m12 0H9"></path>
                    </svg>
                  </div>
                  <p class="text-muted-foreground text-sm">{{visual_placeholder_text}}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Features Section — SOLUTION (PAS Formula) -->
      <section id="features" class="py-16 bg-muted">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
          
          <!-- Section Header -->
          <div class="text-center mb-16">
            <h2 class="text-3xl font-bold text-foreground sm:text-4xl mb-4">
              {{features_headline}}
            </h2>
            <p class="text-xl text-muted-foreground max-w-2xl mx-auto">
              {{features_subheadline}}
            </p>
          </div>
          
          <!-- Features Grid -->
          <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
            
            <!-- Feature 1 -->
            <div class="bg-background rounded-xl p-6 border border-border shadow-sm">
              <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-foreground mb-2">
                {{feature_1_title}}
              </h3>
              <p class="text-muted-foreground">
                {{feature_1_description}}
              </p>
            </div>
            
            <!-- Feature 2 -->
            <div class="bg-background rounded-xl p-6 border border-border shadow-sm">
              <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-foreground mb-2">
                {{feature_2_title}}
              </h3>
              <p class="text-muted-foreground">
                {{feature_2_description}}
              </p>
            </div>
            
            <!-- Feature 3 -->
            <div class="bg-background rounded-xl p-6 border border-border shadow-sm md:col-span-2 lg:col-span-1">
              <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"></path>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-foreground mb-2">
                {{feature_3_title}}
              </h3>
              <p class="text-muted-foreground">
                {{feature_3_description}}
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Testimonials Section — Social Proof -->
      <section id="testimonials" class="py-16">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
          
          <!-- Section Header -->
          <div class="text-center mb-16">
            <h2 class="text-3xl font-bold text-foreground sm:text-4xl mb-4">
              {{testimonials_headline}}
            </h2>
            <p class="text-xl text-muted-foreground">
              {{testimonials_subheadline}}
            </p>
          </div>
          
          <!-- Testimonials Grid -->
          <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
            
            <!-- Testimonial 1 -->
            <div class="bg-muted rounded-xl p-6 border border-border">
              <div class="flex items-center mb-4">
                <div class="flex text-yellow-400">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                  </svg>
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                  </svg>
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                  </svg>
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                  </svg>
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                  </svg>
                </div>
              </div>
              <p class="text-foreground mb-4">
                "{{testimonial_1_quote}}"
              </p>
              <div class="flex items-center">
                <div class="w-10 h-10 bg-gray-200 rounded-full mr-3"></div>
                <div>
                  <p class="font-medium text-foreground">{{testimonial_1_name}}</p>
                  <p class="text-sm text-muted-foreground">{{testimonial_1_title}}</p>
                </div>
              </div>
            </div>
            
            <!-- Additional testimonials follow same pattern -->
            <!-- ... -->
          </div>
        </div>
      </section>

      <!-- Final CTA Section — ACTION (PAS Formula) -->
      <section class="py-16 bg-primary text-primary-foreground">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center max-w-3xl mx-auto">
            <h2 class="text-3xl font-bold sm:text-4xl mb-4">
              {{final_cta_headline}}
            </h2>
            <p class="text-xl mb-8 text-primary-foreground/90">
              {{final_cta_subheadline}}
            </p>
            
            <!-- Large CTA Button -->
            <div class="space-y-4">
              <button class="bg-white text-primary hover:bg-gray-100 focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-primary px-8 py-4 rounded-lg text-xl font-semibold transition-colors shadow-lg">
                {{final_cta_button_text}}
              </button>
              
              <p class="text-sm text-primary-foreground/75">
                {{final_cta_disclaimer}}
              </p>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="bg-muted border-t border-border">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div>
            <h3 class="font-semibold text-foreground mb-4">{{product_name}}</h3>
            <p class="text-muted-foreground text-sm">
              {{footer_description}}
            </p>
          </div>
          <div>
            <h4 class="font-medium text-foreground mb-4">Product</h4>
            <ul class="space-y-2 text-sm text-muted-foreground">
              <li><a href="#" class="hover:text-foreground transition-colors">Features</a></li>
              <li><a href="#" class="hover:text-foreground transition-colors">Pricing</a></li>
              <li><a href="#" class="hover:text-foreground transition-colors">Demo</a></li>
            </ul>
          </div>
          <div>
            <h4 class="font-medium text-foreground mb-4">Company</h4>
            <ul class="space-y-2 text-sm text-muted-foreground">
              <li><a href="#" class="hover:text-foreground transition-colors">About</a></li>
              <li><a href="#" class="hover:text-foreground transition-colors">Blog</a></li>
              <li><a href="#" class="hover:text-foreground transition-colors">Contact</a></li>
            </ul>
          </div>
          <div>
            <h4 class="font-medium text-foreground mb-4">Support</h4>
            <ul class="space-y-2 text-sm text-muted-foreground">
              <li><a href="#" class="hover:text-foreground transition-colors">Help Center</a></li>
              <li><a href="#" class="hover:text-foreground transition-colors">Privacy</a></li>
              <li><a href="#" class="hover:text-foreground transition-colors">Terms</a></li>
            </ul>
          </div>
        </div>
        
        <div class="border-t border-border mt-12 pt-8">
          <p class="text-center text-sm text-muted-foreground">
            © 2026 {{product_name}}. All rights reserved.
          </p>
        </div>
      </div>
    </footer>

  </body>
</html>
```

## Variable Substitution Guide

### Required Variables for Template Completion

```yaml
# Product Information
product_name: "Your Product Name"
key_benefit: "Primary value proposition"
seo_description: "Meta description for SEO (155 chars max)"

# Navigation
nav_cta_text: "Get Started"

# Hero Section (PAS Formula - PROBLEM)
hero_headline_v1: "Stop Struggling with [Problem]"
hero_headline_emphasis: "That Changes Today"
hero_subheadline_agitate: "Every day you delay costs you [specific consequence]. Here's what that's really costing..."
social_proof_stat: "Join 10,000+ customers"
social_proof_qualifier: "already getting results"
primary_cta_text: "Start My Free Trial"
secondary_cta_text: "See How It Works"
trust_indicator_1: "No credit card required"
trust_indicator_2: "Setup in 5 minutes"
visual_placeholder_text: "Product demo or hero image"

# Features Section (PAS Formula - SOLUTION)
features_headline: "Everything You Need to [Achieve Outcome]"
features_subheadline: "Stop patching together multiple tools. Get everything in one powerful platform."
feature_1_title: "Feature Name"
feature_1_description: "Benefit-focused description of what this does for the user"
feature_2_title: "Feature Name"
feature_2_description: "Benefit-focused description"
feature_3_title: "Feature Name"
feature_3_description: "Benefit-focused description"

# Testimonials
testimonials_headline: "Don't Take Our Word for It"
testimonials_subheadline: "See what our customers say about their results"
testimonial_1_quote: "Specific result or transformation quote"
testimonial_1_name: "Customer Name"
testimonial_1_title: "Job Title, Company"

# Final CTA (PAS Formula - ACTION)
final_cta_headline: "Ready to [Get Specific Outcome]?"
final_cta_subheadline: "Join thousands who are already [achieving result]. Start your transformation today."
final_cta_button_text: "Start My [Specific Outcome] Now"
final_cta_disclaimer: "14-day free trial • No credit card required • Cancel anytime"

# Footer
footer_description: "Brief company description and mission statement"
```

## Copy Formula Integration Examples

### AIDA Structure Mapping

```html
<!-- ATTENTION: Hero headline -->
<h1 class="text-4xl font-bold">
  "10X Your Conversion Rate with One Simple Change"
</h1>

<!-- INTEREST: Problem development -->
<p class="text-xl text-muted-foreground">
  "Your landing page visitors are leaving without converting. Every bounce is money walking out the door..."
</p>

<!-- DESIRE: Benefit visualization -->
<div class="grid gap-8 lg:grid-cols-3">
  <!-- Features that create desire -->
</div>

<!-- ACTION: Clear next step -->
<button class="bg-primary text-primary-foreground px-8 py-4">
  "Get My Conversion Boost Now"
</button>
```

### PAS Structure Mapping

```html
<!-- PROBLEM: Name the pain -->
<h1 class="text-4xl font-bold">
  "Tired of Landing Pages That Don't Convert?"
</h1>

<!-- AGITATE: Make it worse -->
<p class="text-xl text-muted-foreground">
  "Every visitor that bounces is lost revenue. While your competition captures leads, you're watching potential customers slip away..."
</p>

<!-- SOLUTION: Present relief -->
<section class="features">
  <!-- How your product solves the problem -->
</section>
```

## Accessibility Compliance Checklist

### WCAG AA Requirements Built-In

- ✅ Semantic HTML5 structure (header, main, section, footer)
- ✅ Proper heading hierarchy (h1 → h2 → h3)
- ✅ Color contrast >= 4.5:1 (verified with CODEXA palette)
- ✅ Focus indicators on all interactive elements
- ✅ Alt text placeholders for images
- ✅ ARIA labels for complex interactions
- ✅ Keyboard navigation support
- ✅ Screen reader friendly markup
- ✅ Touch-friendly button sizes (44px minimum)

### Performance Optimization Built-In

- ✅ Preconnect to Google Fonts
- ✅ Font-display: swap for faster rendering
- ✅ Minimal CSS via Tailwind utilities
- ✅ Semantic markup for better Core Web Vitals
- ✅ Optimized asset loading strategy
- ✅ Mobile-first responsive approach

## Deployment Integration

### Handoff to N05 (Operations)

```bash
# Validation before handoff
lighthouse landing_page.html --only=performance,accessibility
w3c-validator landing_page.html
contrast-checker landing_page.html

# If all pass:
# → Hand off to N05 for Railway deployment
# → Include validation certificates
# → Provide mobile/desktop screenshots
# → Document any custom interactions
```

This template ensures every landing page generated by N02 meets production standards for performance, accessibility, and conversion optimization.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p09_ct_component_template]] | sibling | 0.62 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.60 |
| [[p05_output_style_guide]] | sibling | 0.56 |
| [[p03_pt_visual_frontend_marketing]] | upstream | 0.53 |
| [[landing_page_petshop_crm]] | upstream | 0.51 |
| [[bld_examples_landing_page]] | upstream | 0.47 |
| [[p05_output_visual_report]] | sibling | 0.47 |
| [[p05_output_dashboard_ui]] | sibling | 0.45 |
| [[p01_kc_tailwind_patterns]] | upstream | 0.40 |
| [[kc_tailwind_patterns]] | upstream | 0.39 |
