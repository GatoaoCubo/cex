---
id: p11_qg_path_config
kind: quality_gate
pillar: P11
title: "Gate: path_config"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: path_config
quality: 9.0
tags: [quality-gate, path-config, P11, P09, governance, filesystem]
tldr: "Gates for path_config artifacts — portable paths catalog with platform spec, expandable variables, and creation order."
density_score: 0.85
llm_function: GOVERN
---
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
