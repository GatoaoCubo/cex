---
kind: output_template
id: bld_output_template_episodic_memory
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an episodic_memory artifact
quality: null
title: "Output Template Episodic Memory"
version: "1.0.0"
author: n03_builder
tags: [episodic_memory, builder, output_template]
tldr: "Fill {{vars}} to produce an episodic_memory artifact with episode schema, retrieval config, and decay."
domain: "episodic memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Output Template: episodic_memory
```yaml
id: p10_ep_{{agent_slug}}
kind: episodic_memory
pillar: P10
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
owner: "{{agent_or_nucleus_id}}"
episode_schema:
  timestamp: "datetime"
  context: "string"
  task: "string"
  outcome: "string"
  {{field_4}}: "{{type}}"
  retrieval_keys: "list[string]"
  confidence: "float"
retrieval_method: {{recency|relevance|hybrid}}
episode_count: {{int_max_episodes}}
decay_policy:
  method: {{time|count|relevance|hybrid}}
  rate: "{{e.g._30_days_or_relevance_threshold}}"
retrieval_keys: [{{key_1}}, {{key_2}}, {{key_3}}]
index_method: {{embedding|keyword|hybrid}}
promotion_sources: [{{working_memory_id_1}}]
quality: null
tags: [episodic_memory, {{owner_tag}}, {{domain_tag}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_agent_and_purpose_max_200ch}}"
```
## Overview
`{{what_agent_this_serves_1_to_2_sentences}}`
`{{why_episodic_memory_is_needed}}`

## Episode Schema
| Field | Type | Purpose |
|-------|------|---------|
| timestamp | datetime | Temporal indexing for decay and retrieval |
| context | string | Situational context when episode occurred |
| task | string | Task being performed |
| outcome | string | Result or conclusion |
| retrieval_keys | list[string] | Topics/entities enabling future retrieval |
| confidence | float | Reliability of stored episode |

## Retrieval Config
Method: `{{retrieval_method}}`
Index: `{{index_method}}`
Retrieval keys: `{{key_list}}`

## Decay Policy
Method: `{{decay_method}}`
Rate: `{{decay_rate}}`
Pruning: `{{what_happens_to_pruned_episodes}}`

## Example Episodes
```yaml
- timestamp: "{{YYYY-MM-DDTHH:MM:SSZ}}"
  context: "{{what_was_happening}}"
  task: "{{what_agent_was_doing}}"
  outcome: "{{what_happened}}"
  retrieval_keys: [{{topic_1}}, {{topic_2}}]
  confidence: {{float}}
```
