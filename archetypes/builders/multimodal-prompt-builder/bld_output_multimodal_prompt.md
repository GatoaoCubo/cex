---
kind: output_template
id: bld_output_template_multimodal_prompt
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for multimodal_prompt production
quality: 8.7
title: "Output Template Multimodal Prompt"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [multimodal_prompt, builder, output_template]
tldr: "Template with vars for multimodal_prompt production"
domain: "multimodal_prompt construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_workflow_node
  - bld_output_template_playground_config
  - kc_multimodal_prompt
  - bld_output_template_onboarding_flow
  - bld_examples_workflow_primitive
  - bld_knowledge_card_multi_modal_config
  - bld_examples_multimodal_prompt
  - p03_ch_kc_to_notebooklm
  - bld_output_template_input_schema
  - p03_react_web_research
---

```yaml
---
id: p03_mmp_{{name}}.md
name: {{name}}
kind: multimodal_prompt
pillar: P03
quality: null
description: {{description}}
content:
  - type: {{media_type}}
    data: {{data}}
---
```

<!-- Replace with prompt name -->
<!-- Replace with descriptive title -->
<!-- Replace with media type (text/image/audio) -->
<!-- Replace with raw data or reference -->

| Type   | Data                              |
|--------|-----------------------------------|
| text   | {{text_content}}                 |
| image  | {{image_url}}                    |
| code   | {{code_snippet}}                 |

```json
{
  "prompt": "{{name}}",
  "elements": [
    {"type": "text", "content": "{{text_content}}"},
    {"type": "image", "url": "{{image_url}}"}
  ]
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_workflow_node]] | downstream | 0.27 |
| [[bld_output_template_playground_config]] | sibling | 0.26 |
| [[kc_multimodal_prompt]] | upstream | 0.26 |
| [[bld_output_template_onboarding_flow]] | sibling | 0.23 |
| [[bld_examples_workflow_primitive]] | downstream | 0.20 |
| [[bld_knowledge_card_multi_modal_config]] | upstream | 0.19 |
| [[bld_examples_multimodal_prompt]] | downstream | 0.19 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.18 |
| [[bld_output_template_input_schema]] | sibling | 0.17 |
| [[p03_react_web_research]] | upstream | 0.17 |
