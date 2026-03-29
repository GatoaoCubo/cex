---
id: "p12_dr_{{AGENT_ID}}"
kind: dispatch_rule
pillar: P12
version: "1.0.0"
created: "{{DATE}}"
updated: "{{DATE}}"
author: "{{AUTHOR}}"
domain: "{{DOMAIN}}"
quality: null
tags: [{{TAGS}}]
tldr: "Route {{DOMAIN}} tasks to this nucleus"
scope: "{{DOMAIN}}"
keywords: [{{KEYWORDS}}]
target: "{{AGENT_ID}}"
model: "{{MODEL}}"
priority: "{{PRIORITY}}"
confidence_threshold: 0.75
fallback: "{{FALLBACK}}"
---
## Purpose
Routes tasks related to {{DOMAIN}} to the {{AGENT_NAME}} nucleus.

## Keywords
{{KEYWORD_RATIONALE}}

## Fallback
When confidence < threshold, route to {{FALLBACK}}.
