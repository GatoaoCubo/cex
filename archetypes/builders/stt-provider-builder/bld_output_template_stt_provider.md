---
kind: output_template
id: bld_output_template_stt_provider
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for stt_provider production
quality: null
title: "Output Template Stt Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [stt_provider, builder, output_template]
tldr: "Template with vars for stt_provider production"
domain: "stt_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
---
name: {{name}}
description: {{description}}
provider: {{provider}}
language: {{language}}
api_key: {{api_key}}
endpoint: {{endpoint}}
parameters: {{parameters}}
---
## Overview
{{overview_content}}

## Configuration
{{configuration_content}}

## Usage
{{usage_content}}

## Parameters
{{parameters_content}}

## Notes
{{notes_content}}
```
