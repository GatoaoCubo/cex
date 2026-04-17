---
id: ex_dag_content_factory
kind: dag
pillar: P12
title: "Example DAG: Content Factory"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: content_factory_pipeline
quality: 8.7
brand_placeholders:
  - BRAND_VOICE
  - BRAND_AUDIENCE
  - BRAND_CONTENT_THEMES
tags: [dag, content-factory, orchestration, n02]
tldr: "Directed graph for parallelizable content operations across research, copy, media, QA, and publishing."
density_score: 0.91
---

# Node Graph

```yaml
nodes:
  - intake_brief
  - select_angle
  - draft_copy
  - draft_media
  - validate_copy
  - validate_html
  - schedule_publish
  - publish
  - capture_feedback
edges:
  - intake_brief -> select_angle
  - select_angle -> draft_copy
  - select_angle -> draft_media
  - draft_copy -> validate_copy
  - draft_media -> validate_html
  - validate_copy -> schedule_publish
  - validate_html -> schedule_publish
  - schedule_publish -> publish
  - publish -> capture_feedback
```

## Routing Notes

- `select_angle` chooses the strongest audience/content-theme fit.
- `draft_copy` and `draft_media` can run in parallel.
- Publishing is blocked until both validation branches pass.

