---
kind: output_template
id: bld_output_template_course_module
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for course_module production
quality: 8.9
title: "Output Template Course Module"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [course_module, builder, output_template]
tldr: "Template with vars for course_module production"
domain: "course_module construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
```yaml
---
id: {{id}} <!-- Unique module ID following p05_cm_[a-z][a-z0-9_]+.md pattern -->
title: {{title}} <!-- Module title -->
pillar: P05 <!-- Always P05 -->
quality: null <!-- Must be null -->
description: {{description}} <!-- Brief module overview -->
---
```

## Learning Objectives

| Objective | Description |
|----------|-------------|
| {{objective1}} <!-- e.g., "Understand CEX principles" --> | {{desc1}} <!-- e.g., "Cover core concepts and use cases" --> |
| {{objective2}} <!-- e.g., "Implement basic workflows" --> | {{desc2}} <!-- e.g., "Walkthrough code examples" --> |

## Sample Code

```python
# {{code_example}} <!-- e.g., "Basic CEX integration" -->
def example_function():
    {{code_logic}} <!-- e.g., "print('Hello, CEX!')" -->
```
```
