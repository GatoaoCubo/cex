---
id: ex_component_map_pipeline
kind: component_map
pillar: P08
title: Pipeline Engine Component Map
tags: [architecture, pipeline, components]
references:
  - tpl_component_map
  - ex_mental_model_pipeline
  - ex_dispatch_rule_research
---

# Pipeline Engine Component Map

> Skeleton: component_map kind

```
CAPTURE ──→ DECOMPOSE ──→ HYDRATE ──→ COMPILE ──→ ENVELOPE
 (Python)    (LLM micro)   (SQLite)    (Jinja2)    (Python)
```

## Links

- Design: [[ex_mental_model_pipeline]]
- Routing: [[ex_dispatch_rule_research]]
