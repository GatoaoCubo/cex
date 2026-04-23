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
related:
  - bld_output_template_playground_config
  - bld_output_template_multimodal_prompt
  - bld_output_template_integration_guide
  - bld_examples_edit_format
  - bld_output_template_api_reference
  - bld_output_template_user_journey
  - bld_knowledge_card_edit_format
  - bld_output_template_sales_playbook
  - bld_output_template_edit_format
  - bld_output_template_sdk_example
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_playground_config]] | sibling | 0.36 |
| [[bld_output_template_multimodal_prompt]] | sibling | 0.30 |
| [[bld_output_template_integration_guide]] | sibling | 0.24 |
| [[bld_examples_edit_format]] | downstream | 0.22 |
| [[bld_output_template_api_reference]] | sibling | 0.20 |
| [[bld_output_template_user_journey]] | sibling | 0.19 |
| [[bld_knowledge_card_edit_format]] | upstream | 0.18 |
| [[bld_output_template_sales_playbook]] | sibling | 0.17 |
| [[bld_output_template_edit_format]] | sibling | 0.17 |
| [[bld_output_template_sdk_example]] | sibling | 0.17 |
