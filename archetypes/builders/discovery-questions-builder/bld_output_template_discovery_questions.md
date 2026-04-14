---
kind: output_template
id: bld_output_template_discovery_questions
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for discovery_questions production
quality: null
title: "Output Template Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, output_template]
tldr: "Template with vars for discovery_questions production"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p01_dq_{{name}}.md
name: {{name}}
pillar: P01
description: {{description}}
quality: null
related_entities: {{related_entities}}
discovery_type: discovery_questions
---
```

<!-- id: p01_dq_[a-z][a-z0-9_]+.md$ -->
<!-- name: Human-readable question name -->
<!-- description: Brief purpose of this discovery question -->
<!-- related_entities: List of entities this question applies to -->
<!-- discovery_type: Must be "discovery_questions" -->

| Question | Expected Answer Type |
|---------|---------------------|
| What data sources are available? | List of databases/APIs |
| How is data quality validated? | Process description |

```python
# Example validation code
def validate_data(source):
    if source not in APPROVED_SOURCES:
        raise ValueError("Invalid data source")
    return True
```
