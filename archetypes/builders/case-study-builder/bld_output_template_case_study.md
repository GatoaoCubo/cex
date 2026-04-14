---
kind: output_template
id: bld_output_template_case_study
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for case_study production
quality: null
title: "Output Template Case Study"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, output_template]
tldr: "Template with vars for case_study production"
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p05_cs_{{name}}.md <!-- Filename following p05_cs_[a-z][a-z0-9_]+.md -->
title: {{title}} <!-- Case study title -->
description: {{description}} <!-- Summary of the study's purpose -->
author: {{author}} <!-- Author name -->
date: {{date}} <!-- Publication date (YYYY-MM-DD) -->
quality: null <!-- Always null -->
keywords: {{keywords}} <!-- Comma-separated relevant terms -->
---
```

## Overview
{{overview}} <!-- Brief context and objectives -->

## Key Findings
| Metric       | Value   | Description              |
|--------------|---------|--------------------------|
| {{metric1}}  | {{val1}}| {{desc1}}                |
| {{metric2}}  | {{val2}}| {{desc2}}                |

## Recommendations
```python
# Sample code block
def {{function_name}}():
    {{code_logic}}  # Placeholder for implementation
```

## Conclusion
{{conclusion}} <!-- Summary of implications and next steps -->
