---
kind: output_template
id: bld_output_template_path_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a path_config artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: path_config
```yaml
id: p09_path_{{scope_slug}}
kind: path_config
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{global_or_satellite_or_service}}"
paths:
  - {{path_name_1}}
  - {{path_name_2}}
  - {{path_name_3}}
platform: {{windows|unix|all}}
quality: null
tags: [path_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_paths_cover_max_200ch}}"
base_dir: "{{base_directory_path}}"
dir_count: {{N}}
file_count: {{N}}
```
## Overview
{{what_scope_and_purpose_1_to_2_sentences}}
{{who_consumes_these_paths}}
## Path Catalog
| Path | Type | Platform | Default | Required | Notes |
|------|------|----------|---------|----------|-------|
| {{path_name_1}} | {{dir|file}} | {{windows|unix|all}} | {{default_path}} | {{yes|no}} | {{notes}} |
| {{path_name_2}} | {{type}} | {{platform}} | {{default}} | {{yes|no}} | {{notes}} |
| {{path_name_3}} | {{type}} | {{platform}} | {{default}} | {{yes|no}} | {{notes}} |
## Directory Hierarchy
```text
{{base_dir}}/
  {{subdir_1}}/
  {{subdir_2}}/
    {{nested_dir}}/
  {{subdir_3}}/
```
## Platform Notes
{{platform_specific_differences_and_resolution_rules}}
## References
- {{reference_1}}
- {{reference_2}}
