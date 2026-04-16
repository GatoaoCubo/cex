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
