---
kind: quality_gate
id: p11_qg_path_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of path_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: path_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, path-config, P11, P09, governance, filesystem]
tldr: "Gates for path_config artifacts — portable paths catalog with platform spec, expandable variables, and creation order."
domain: path_config
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.85
related:
  - p03_ins_path_config
  - bld_knowledge_card_path_config
  - bld_examples_path_config
  - bld_memory_path_config
  - bld_architecture_path_config
  - bld_schema_path_config
  - path-config-builder
  - bld_collaboration_path_config
  - p01_kc_path_config
  - p03_sp_path_config_builder
---

## Quality Gate

# Gate: path_config
## Definition
| Field     | Value                                                |
|-----------|------------------------------------------------------|
| metric    | path catalog completeness + portability compliance   |
| threshold | 8.0                                                  |
| operator  | >=                                                   |
| scope     | all path_config artifacts (P09)                      |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = all paths undefined at boot |
| H02 | id matches `^p09_path_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "path_config" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr | Completeness |
| H07 | paths catalog has >= 3 entries, each with name, default, and relative_or_absolute flag | Fewer than 3 paths does not justify a config artifact |
| H08 | platform field states target OS or list of supported OS values | Paths are platform-dependent; undeclared = silent breakage |
| H09 | No user-specific absolute paths (all absolute paths use expandable variables such as $HOME or `{{USER_DIR}}`) | Hardcoded user paths break on any other machine |
| H10 | default values are present for all paths (null is acceptable if no default exists, but must be explicit) | Missing defaults force manual config on every install |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "path-config" | 0.5 |
| S03 | density_score >= 0.80 | 0.5 |
| S04 | All path templates use forward slashes or explicit platform-conditional notation | 0.5 |
| S05 | relative_or_absolute is declared per path (not assumed) | 1.0 |
| S06 | expandable_vars block documents each variable used ($HOME, $XDG_DATA_HOME, etc.) with expansion example | 1.0 |
| S07 | validation_rules block states per-path check (must exist, must be writable, must be directory, etc.) | 1.0 |
| S08 | directory_hierarchy shows parent-child relationships for paths that depend on each other | 0.5 |
| S09 | creation_order list specifies which paths must be created first when initializing from scratch | 0.5 |
| S10 | permissions_note documents required read/write/execute access for each path where non-default | 0.5 |
| S11 | No filler phrases ("this config", "designed to manage", "various paths") | 1.0 |
Weights sum: 8.0. Normalize: divide each by 8.0 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference path catalog for this scope |
| >= 8.0 | PUBLISH — use in install scripts and boot configs |
| >= 7.0 | REVIEW — add missing variables, validation rules, or hierarchy |
| < 7.0  | REJECT — rework catalog with portable paths and platform spec |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Emergency hotfix requiring path override before full catalog review complete |
| approver | p09-chief |
| audit_trail | Log in records/audits/ with override path, platform, and timestamp |
| expiry | 48h — full catalog must pass gates before next deploy cycle |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
