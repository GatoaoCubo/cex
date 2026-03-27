---
id: p03_ins_path_config
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Path Config Builder Instructions
target: path-config-builder agent
phases_count: 3
prerequisites:
  - The system scope that requires filesystem paths is named (e.g., "logging subsystem", "plugin directory")
  - At least one target platform is identified (windows, linux, macos, or cross-platform)
  - The purpose of each directory or file path is known (what will be stored there)
validation_method: checklist
domain: path_config
quality: null
tags:
  - instruction
  - path-config
  - filesystem
  - P09
idempotent: true
atomic: false
rollback: "Delete the produced path_config artifact file; no system state changes occur"
dependencies: []
logging: true
tldr: "Identify scope and platforms, compose path catalog with platform variants and validation sequence, validate gates and write a path_config artifact."
density_score: 0.85
---

## Context

The path-config-builder receives a **system scope** and produces a `path_config` artifact that formally specifies all filesystem paths used within that scope, including platform variants, resolution rules, and startup validation.

**Input variables**:
- `{{scope}}` — name of the subsystem or feature that owns these paths (e.g., `logging`, `plugin_storage`, `artifact_cache`)
- `{{platforms}}` — list of target platforms: `[windows, linux, macos]` or `[cross-platform]`
- `{{path_purposes}}` — named paths with their purpose (e.g., `log_dir: stores runtime log files`)
- `{{base_dir}}` — optional root directory from which relative paths resolve (e.g., `~`, `$APPDATA`, `/var`)
- `{{constraints}}` — optional platform-specific rules (Windows max path 260 chars, Linux case-sensitivity, etc.)

**Output**: a single `path_config` artifact at `p09_path_{{scope}}.md` listing all paths with per-platform values, resolution type, and validation rules.

**Boundaries**: handles filesystem paths only. Does NOT define non-path environment variables (env_config), access control for directories (permission-builder), feature toggles (feature_flag), or timeout/retry settings (runtime_rule).

---

## Phases

### Phase 1: RESEARCH

**Goal**: Enumerate every path needed by the scope and classify each one before writing anything.

1. Identify the scope: confirm it is one of `global`, `satellite name`, or `service name`. Record as a snake_case lowercase slug with no hyphens.
2. List every filesystem path from `{{path_purposes}}`. For each, determine:
   - **Type**: `dir` (container) or `file` (specific file, include extension)
   - **Platform**: `windows`, `unix`, or `all`
   - **Necessity**: `required` (system fails without it) or `optional` (feature degrades gracefully)
   - **Creation policy**: `must_exist`, `create_if_absent`, or `warn_if_absent`
3. Identify parent-child relationships: which paths are subdirectories of another path in the list?
4. Build the directory hierarchy tree (ASCII art). Parent paths must appear before children.
5. Determine `{{base_dir}}`. If not provided, infer from platform defaults:
   - Windows: `%APPDATA%\{{scope}}` or `%LOCALAPPDATA%\{{scope}}`
   - Linux/macOS: `$HOME/.{{scope}}` or `$XDG_DATA_HOME/{{scope}}`
6. Flag any path that conflicts with OS-reserved directories (`C:\Windows`, `/etc`, `/proc`, `/sys`).
7. Confirm scope slug for `id`: must match `^p09_path_[a-z][a-z0-9_]+$`.
8. Search for existing path_config artifacts via brain_query [IF MCP]: `path_config {{scope}}`. Avoid duplicates.

**Exit**: every named path has type, platform, necessity, and creation policy assigned. Directory hierarchy is built. No OS-reserved conflicts unaddressed.

---

### Phase 2: COMPOSE

**Goal**: Produce all artifact fields, platform variants, resolution rules, and validation sequence.

9. Read SCHEMA.md — source of truth for all required fields.
10. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints exactly.
11. Fill frontmatter: all required fields. Set `quality: null` — never self-score.
12. Set `scope` to the concrete slug from Phase 1 step 1.
13. Write `paths` list with exact names matching the Path Catalog table (zero drift between frontmatter list and body table).
14. Write **Overview** section: 1–2 sentences on scope, purpose, and consumers.
15. Write **Path Catalog** section: table with columns `name | type | platform | default | required | notes`. Use expandable variables in default values (e.g., `%APPDATA%\logs`) — never hardcode user-specific absolute paths.
16. Write **Directory Hierarchy** section: ASCII tree showing parent-child relationships.
17. Write **Platform Notes** section: document separator differences (`\` Windows vs `/` Unix), environment variable expansion per platform, and the cross-platform resolution priority:
    - Priority 1: environment variable override (e.g., `APP_LOG_DIR`)
    - Priority 2: platform default
    - Priority 3: fallback relative path from executable directory
18. For dynamic paths, specify the resolution expression: `env("APP_{{PATH_NAME_UPPER}}") ?? platform_default("{{path_value}}")`.
19. Write **Startup Validation** sequence as an ordered list. Required paths with `must_exist` get `assert isdir/isfile`. Paths with `create_if_absent` get mkdir command. Parent paths appear before children.
20. Verify body <= 3072 bytes.

**Exit**: `paths` list in frontmatter matches path names in Path Catalog table exactly. Body within byte limit. No hardcoded user-specific absolute paths.

---

### Phase 3: VALIDATE

**Goal**: Verify all quality gates before writing the final artifact.

21. Check QUALITY_GATES.md — verify each HARD gate manually.
22. Confirm YAML frontmatter parses without errors.
23. Confirm `paths` list in frontmatter matches path names in Path Catalog (zero drift).
24. Confirm `quality == null`.
25. Confirm body has all 4 required sections: Overview, Path Catalog, Directory Hierarchy, Platform Notes.
26. Confirm no user-specific absolute paths — only expandable variables.
27. Confirm body <= 3072 bytes.
28. Verify no path value on Windows exceeds 260 characters.
29. Score SOFT gates against QUALITY_GATES.md.
30. If score < 8.0: revise in same pass before outputting. Do not output a failing artifact.
31. Write the final artifact using the Output Contract template below.

---

## Output Contract

```
---
id: p09_path_{{scope}}
kind: path_config
pillar: P09
domain: {{scope}}
version: 1.0.0
created: {{date}}
author: path-config-builder
scope: {{global|satellite|service}}
platforms: [{{platform_list}}]
base_dir: {{base_dir}}
paths: [{{path_name_1}}, {{path_name_2}}]
quality: null
tags: [path-config, {{scope}}, filesystem]
---

## Overview

{{scope_purpose_1_2_sentences}}

## Path Catalog

| Name | Type | Platform | Default | Required | Notes |
|------|------|----------|---------|----------|-------|
| {{path_name}} | {{dir|file}} | {{windows|unix|all}} | `{{expandable_default}}` | {{true|false}} | {{notes}} |

## Directory Hierarchy

```
{{base_dir}}/
├── {{path_name_1}}/    (dir, {{required|optional}})
│   └── {{path_name_2}}/ (dir, child)
└── {{path_name_3}}     (file)
```

## Platform Notes

- **Windows separator**: `\` — defaults under `%APPDATA%\{{scope}}`
- **Unix separator**: `/` — defaults under `$HOME/.{{scope}}`
- **Resolution order**: env override → platform default → relative fallback
- **Dynamic resolution**: `env("APP_{{PATH_NAME_UPPER}}") ?? "{{platform_default}}"`

## Startup Validation

1. `assert isdir("{{path_value}}")` — {{path_name}} (required, must_exist)
2. `mkdir -p "{{path_value}}"` if absent — {{path_name}} (create_if_absent)
3. log warning if absent — {{path_name}} (optional, warn_if_absent)
```

---

## Validation

| # | Gate | Type |
|---|------|------|
| 1 | Every path in `path_purposes` appears in the Path Catalog | HARD |
| 2 | `paths` list in frontmatter matches Path Catalog names exactly (zero drift) | HARD |
| 3 | Platform values use correct separator (`\` Windows, `/` Unix) | HARD |
| 4 | No user-specific absolute paths — only expandable variables | HARD |
| 5 | Every required path has an existence validation rule in startup sequence | HARD |
| 6 | Validation order places parent directories before children | HARD |
| 7 | Body <= 3072 bytes | HARD |
| 8 | `quality: null` is set | HARD |
| 9 | Directory hierarchy diagram present | SOFT |
| 10 | Dynamic paths specify env variable name and fallback | SOFT |
| 11 | Windows path values do not exceed 260 characters | SOFT |

---

## Metacognition

**Does**:
- Specifies all filesystem paths for a named system scope with per-platform variants
- Documents creation policy and startup validation sequence
- Uses expandable variables instead of hardcoded absolute paths

**Does NOT**:
- Define non-path environment variables (use env_config)
- Control who can access directories (use permission-builder)
- Toggle features on or off (use feature_flag)
- Define timeouts or retry counts (use runtime_rule)

**Chaining**: output feeds system startup validator (validation sequence), installer (creation policy), documentation (path catalog). Input from system design doc, deployment requirements, platform constraint catalog.
