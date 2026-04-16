---
kind: output_template
id: bld_output_template_onboarding_flow
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for onboarding_flow production
quality: 8.9
title: "Output Template Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, output_template]
tldr: "Template with vars for onboarding_flow production"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
---
id: p05_of_{{name}}.md
name: {{onboarding_flow_name}}
pillar: P05
quality: null
description: {{flow_description}}
status: {{draft|review|approved}}
created_at: {{YYYY-MM-DD}}
updated_at: {{YYYY-MM-DD}}
---

## Onboarding Flow: {{flow_name}}

### Overview
| Step | Action | Description | Status |
|------|--------|-------------|--------|
| 1 | {{action_1}} | {{description_1}} | {{status_1}} |
| 2 | {{action_2}} | {{description_2}} | {{status_2}} |

### API Example
```yaml
endpoint: /api/v1/onboarding
method: POST
payload:
  user_id: {{user_id}}
  documents: 
    - type: {{doc_type}}
      file: {{file_hash}}
```

<!-- Replace {{name}} with lowercase alphanumeric identifier -->
<!-- Replace {{onboarding_flow_name}} with flow title -->
<!-- Replace {{flow_description}} with 1-2 sentence summary -->
<!-- Replace {{draft|review|approved}} with current status -->
<!-- Replace {{YYYY-MM-DD}} with date values -->
<!-- Replace {{action_1}}, {{description_1}}, etc. with step details -->
<!-- Replace {{user_id}}, {{doc_type}}, {{file_hash}} with sample data -->
```
