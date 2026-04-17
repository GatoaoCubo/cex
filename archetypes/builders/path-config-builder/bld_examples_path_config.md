---
kind: examples
id: bld_examples_path_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of path_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Path Config"
version: "1.0.0"
author: n03_builder
tags: [path_config, builder, examples]
tldr: "Golden and anti-examples for path config construction, demonstrating ideal structure and common pitfalls."
domain: "path config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: path-config-builder
## Golden Example
INPUT: "Define filesystem paths for the data pipeline service"
OUTPUT:
```yaml
id: p09_path_data_pipeline
kind: path_config
pillar: P09
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
scope: "data_pipeline"
paths:
  - base_dir
  - input_dir
  - output_dir
  - staging_dir
  - log_dir
  - config_dir
  - cache_dir
platform: all
quality: 8.9
tags: [path_config, data_pipeline, P09, filesystem, directories]
tldr: "Data pipeline paths: 7 dirs, all platform, base-relative, auto-create optional"
description: "Filesystem paths for data pipeline service covering input, output, staging, logs, config, cache"
base_dir: "{{APP_ROOT}}/data_pipeline"
dir_count: 7
file_count: 0
```
## Overview
Filesystem paths for the data pipeline service. All paths relative to base_dir.
Consumed by pipeline orchestrator at startup; missing required dirs block execution.
## Path Catalog
| Path | Type | Platform | Default | Required | Notes |
|------|------|----------|---------|----------|-------|
| base_dir | dir | all | `{{APP_ROOT}}`/data_pipeline | yes | Root for all pipeline paths |
| input_dir | dir | all | `{{base_dir}}`/input | yes | Raw data ingestion directory |
| output_dir | dir | all | `{{base_dir}}`/output | yes | Processed output directory |
| staging_dir | dir | all | `{{base_dir}}`/staging | no | Temp staging area, auto-created |
| log_dir | dir | all | `{{base_dir}}`/logs | no | Pipeline execution logs |
| config_dir | dir | all | `{{base_dir}}`/config | yes | Pipeline configuration files |
| cache_dir | dir | all | `{{base_dir}}`/cache | no | Intermediate cache, purgeable |
## Directory Hierarchy
```text
{{APP_ROOT}}/data_pipeline/
  input/
  output/
  staging/
  logs/
  config/
  cache/
```
## Platform Notes
All paths use forward slashes in templates. Runtime resolves per platform.
Windows: backslash substitution, long path support (>260 chars via \\?\ prefix).
Unix: no special handling needed, forward slashes native.
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_path_ pattern (H02 pass)
- kind: path_config (H04 pass)
- 19 required+recommended fields present (H06 pass)
- body has all 4 sections: Overview, Path Catalog, Directory Hierarchy, Platform Notes (H07 pass)
- paths list matches catalog names exactly (S03 pass)
- No user-specific absolute paths (H08 pass)
- tldr: 72 chars <= 160 (S01 pass)
- tags: 5 items, includes "path_config" (S02 pass)
- Forward slashes in all path templates (S07 pass)
## Anti-Example
INPUT: "Create path config for logs"
BAD OUTPUT:
```yaml
id: log-paths
kind: paths
pillar: config
scope: logging
paths: /var/log/myapp/app.log
quality: 8.0
tags: [logs]
```
Log paths for the application.
Put your logs in /var/log/myapp.
FAILURES:
1. id: "log-paths" uses hyphens and no `p09_path_` prefix -> H02 FAIL
2. kind: "paths" not "path_config" -> H04 FAIL
3. pillar: "config" not "P09" -> H06 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. paths is string, not list of names -> H06 FAIL
6. User-specific absolute path /var/log/myapp -> H08 FAIL
7. Missing fields: version, created, updated, author, platform, tldr -> H06 FAIL
8. tags: only 1 item, missing "path_config" -> S02 FAIL
9. Body missing ## Path Catalog, ## Directory Hierarchy, ## Platform Notes -> H07 FAIL
10. No directory hierarchy shown -> S05 FAIL
11. No platform compatibility specified -> S06 FAIL
