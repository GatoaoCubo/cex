---
kind: examples
id: bld_examples_content_filter
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of content_filter artifacts
quality: 8.9
title: "Examples Content Filter"
version: "1.0.0"
author: wave1_builder_gen
tags: [content_filter, builder, examples]
tldr: "Golden and anti-examples of content_filter artifacts"
domain: "content_filter construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example

This ISO defines a content filter -- the moderation rules that gate output or input.
```yaml
---
kind: content_filter
name: example_filter
description: Filters input/output content for prohibited patterns
version: 1.0
---
stages:
  - name: input_sanitization
    type: regex_replacement
    parameters:
      patterns: ["<script>.*?</script>", "\$$.*?\$$"]
      replacement: "[REDACTED]"
  - name: output_validation
    type: keyword_filter
    parameters:
      prohibited_keywords: ["nsfw", "hate_speech"]
      action: drop
```

## Anti-Example 1: Missing essential parameters
```yaml
---
kind: content_filter
name: broken_filter
description: Incomplete filter config
version: 0.1
---
stages:
  - name: input_sanitization
    type: regex_replacement
    parameters:
      patterns: ["<script>.*?</script>"]
```
## Why it fails
Incomplete parameters - missing replacement value and no output validation stage, making the filter non-functional for complete content pipelines.

## Anti-Example 2: Mixing with guardrail checks
```yaml
---
kind: content_filter
name: mixed_filter
description: Combines filtering with safety checks
version: 1.0
---
stages:
  - name: input_sanitization
    type: regex_replacement
    parameters:
      patterns: ["<script>.*?</script>"]
      replacement: "[REDACTED]"
  - name: safety_check
    type: guardrail
    parameters:
      constraints: ["no_harmful_content", "no_personal_data"]
```
## Why it fails
Content_filter should handle structured filtering, not broad safety constraints. Guardrail checks belong to a different pipeline type and would cause configuration conflicts.
