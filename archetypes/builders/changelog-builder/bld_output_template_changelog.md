---
kind: output_template
id: bld_output_template_changelog
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for changelog production
quality: null
title: "Output Template Changelog"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, output_template]
tldr: "Template with vars for changelog production"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
```yaml
---
id: p01_ch_{{name}}.md
title: {{changelog_title}}
version: {{version_number}}
date: {{release_date}}
author: {{maintainer_name}}
quality: null
description: {{summary_of_changes}}
---
```

<!-- changelog_title: Title of the changelog entry -->
<!-- version_number: Semantic version (e.g., 1.2.3) -->
<!-- release_date: YYYY-MM-DD -->
<!-- maintainer_name: Name of the maintainer -->
<!-- summary_of_changes: Brief description of updates -->

### Changes
| Version | Date       | Description                  |
|---------|------------|------------------------------|
| {{version}} | {{date}} | {{change_description}}       |

<!-- change_description: Summary of key updates -->

### Example Config
```yaml
# Configuration snippet
{{config_key}}: {{config_value}}
```

<!-- config_key: Key name in config file -->
<!-- config_value: Value for the config key -->
```
