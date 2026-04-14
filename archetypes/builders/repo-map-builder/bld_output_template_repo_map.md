---
kind: output_template
id: bld_output_template_repo_map
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for repo_map production
quality: null
title: "Output Template Repo Map"
version: "1.0.0"
author: wave1_builder_gen
tags: [repo_map, builder, output_template]
tldr: "Template with vars for repo_map production"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
---
name: {{name}}
description: {{description}}
owner: {{owner}}
date: {{date}}
status: {{status}}
---
```

# p01_rm_{{name}}.md

## Overview
{{overview_placeholder}}

## Repository Structure
{{structure_placeholder}}

## Mapping Rules
{{rules_placeholder}}

## Access Information
{{access_placeholder}}

## Notes
{{notes_placeholder}}
