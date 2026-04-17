---
kind: output_template
id: bld_output_template_app_directory_entry
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for app_directory_entry production
quality: 8.7
title: "Output Template App Directory Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [app_directory_entry, builder, output_template]
tldr: "Template with vars for app_directory_entry production"
domain: "app_directory_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p05_ade_{{name}}.md
name: {{name}}
description: {{description}}
category: {{category}}
quality: null
created_at: {{created_at}}
updated_at: {{updated_at}}
---
```

<!-- id: p05_ade_[a-z][a-z0-9_]+.md -->
<!-- name: Application name -->
<!-- description: Brief app functionality summary -->
<!-- category: App classification (e.g., "wallet", "exchange") -->
<!-- created_at: ISO 8601 timestamp -->
<!-- updated_at: ISO 8601 timestamp -->

| Name       | Category | Quality |
|------------|----------|---------|
| example_app| utility  | null    |

```bash
# Example CLI command
cex-cli app show p05_ade_example_app
```
