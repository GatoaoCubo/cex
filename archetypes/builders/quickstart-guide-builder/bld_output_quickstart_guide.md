---
kind: output_template
id: bld_output_template_quickstart_guide
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for quickstart_guide production
quality: 8.9
title: "Output Template Quickstart Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [quickstart_guide, builder, output_template]
tldr: "Template with vars for quickstart_guide production"
domain: "quickstart_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - e2e_gold_docs_marketing
  - bld_schema_quickstart_guide
  - bld_instruction_quickstart_guide
  - p03_ins_learning_record
  - quality_gate_intent_resolution
  - bld_output_template_integration_guide
  - bld_output_template_visual_workflow
  - bld_schema_integration_guide
  - p03_sp_quickstart_guide_builder
  - p11_qg_instruction
---

```markdown
---
id: p05_qs_{{name}}.md
kind: quickstart_guide
pillar: P05
title: {{title}}
version: "1.0.0"
created: {{date}}
updated: {{date}}
author: {{author}}
domain: {{domain}}
quality: null
tags: [quickstart, {{product}}, onboarding]
tldr: "{{one-sentence-goal}}"
prerequisites: [{{tool1}}, {{account_type}}, {{sdk_version}}]
---

## Overview

{{2-3 sentences: what will the user build, why it matters, time to complete (<5 min)}}

## Prerequisites

| Item | Version / Requirement |
|------|-----------------------|
| {{tool}} | {{version}} |
| API Key | Obtain at {{provider_console_url}} |

## Steps

1. **{{step_1_title}}**: {{action}} -- expected outcome: {{result}}
2. **{{step_2_title}}**: {{action}} -- expected outcome: {{result}}
3. **{{step_3_title}}**: {{action}} -- expected outcome: {{result}}

```{{language}}
{{minimal_working_code_snippet}}
```

## Verify

Success indicator: {{measurable_outcome}} (e.g., HTTP 200, console output, file created)

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| {{error_message}} | {{root_cause}} | {{resolution}} |

## Next Steps

- {{link_to_api_reference}} -- full endpoint docs
- {{link_to_sdk_example}} -- language-specific integration patterns
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[e2e_gold_docs_marketing]] | upstream | 0.22 |
| [[bld_schema_quickstart_guide]] | downstream | 0.19 |
| [[bld_instruction_quickstart_guide]] | upstream | 0.19 |
| [[p03_ins_learning_record]] | upstream | 0.18 |
| [[quality_gate_intent_resolution]] | downstream | 0.18 |
| [[bld_output_template_integration_guide]] | sibling | 0.18 |
| [[bld_output_template_visual_workflow]] | sibling | 0.17 |
| [[bld_schema_integration_guide]] | downstream | 0.17 |
| [[p03_sp_quickstart_guide_builder]] | upstream | 0.17 |
| [[p11_qg_instruction]] | downstream | 0.17 |
