---
kind: output_template
id: bld_output_template_govtech_vertical
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for govtech_vertical production
quality: null
title: "Output Template Govtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [govtech_vertical, builder, output_template]
tldr: "Template with vars for govtech_vertical production"
domain: "govtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
```yaml
---
id: p01_gv_{{name}}.md
pillar: P01
kind: govtech_vertical
title: {{title}}
description: {{description}}
stakeholders: {{stakeholders}}
quality: null
status: {{status}}
---
```

<!-- Replace {{name}} with lowercase alphanumeric identifier -->
<!-- Replace {{title}} with vertical name (e.g., "Digital Identity") -->
<!-- Replace {{description}} with 1-sentence purpose -->
<!-- Replace {{stakeholders}} with comma-separated agencies/organizations -->
<!-- Replace {{status}} with "draft" or "approved" -->

| Initiative       | Owner       | Status  |
|------------------|-------------|---------|
| eID System       | Ministry A  | Live    |
| Tax Automation   | Agency B    | Pilot   |
| Public Portal    | CTO Office  | Draft   |

```json
{
  "api": {
    "endpoint": "/govtech/{{name}}",
    "method": "GET",
    "response": {
      "data": "{{data}}",
      "error": null
    }
  }
}
```

<!-- Replace {{data}} with example JSON payload -->
```
