---
kind: examples
id: bld_examples_app_directory_entry
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of app_directory_entry artifacts
quality: 8.8
title: "Examples App Directory Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [app_directory_entry, builder, examples]
tldr: "Golden and anti-examples of app_directory_entry artifacts"
domain: "app_directory_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
kind: app_directory_entry
name: Supabase
tagline: "Open source backend for modern apps, free tier included"
screenshots:
  - https://supabase.io/static/images/hero.png
  - https://supabase.io/static/images/dashboard.png
install_steps:
  - "Visit https://supabase.io"
  - "Sign up for a free account"
  - "Use CLI: `npm install -g supabase`"
demo_link: https://supabase.io/demo
description: "Supabase provides a free tier with PostgreSQL, Auth, and Realtime features. Ideal for startups and developers."
```

## Anti-Example 1: Missing Key Sections
```yaml
kind: app_directory_entry
name: ExampleApp
tagline: "A great app for everything"
screenshots: []
install_steps: []
demo_link: https://example.com
```
## Why it fails
Omits critical sections like `description` and lacks screenshots/install steps, making it incomplete for discovery.

## Anti-Example 2: Placeholder Names
```yaml
kind: app_directory_entry
name: ProviderA's App
tagline: "Example solution for hypothetical use cases"
screenshots:
  - https://providera.com/placeholder.png
install_steps:
  - "Download from ProviderA's site"
demo_link: https://providera.com
description: "This is a placeholder example for demonstration purposes only."
```
## Why it fails
Uses generic names like "ProviderA" and "ExampleApp" instead of real tools/vendors, reducing credibility and discoverability.
