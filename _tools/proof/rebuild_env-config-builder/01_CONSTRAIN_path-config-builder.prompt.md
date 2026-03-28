# CEX Crew Runner -- Builder Execution
**Builder**: `path-config-builder`
**Function**: CONSTRAIN
**Intent**: reconstroi env-config-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:18.497812

## Intent Context
- **Verb**: reconstroi
- **Object**: env-config-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_path_config.md
---
id: path-config-builder
kind: type_builder
pillar: P09
parent: null
domain: path_config
llm_function: GOVERN
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [kind-builder, path-config, P09, config, filesystem, paths]
---

# path-config-builder
## Identity
Especialista em construir path_config artifacts — especificacoes de caminhos do sistema de
arquivos. Domina platform-aware paths (Windows/Linux/Mac), directory hierarchies, path
resolution, relative vs absolute, path validation, e a boundary entre path_config (filesystem
paths) e env_config (P09, generic variables) ou permission (P09, access control). Produz
path_config artifacts com frontmatter completo e path catalog documentado.
## Capabilities
- Definir caminhos do sistema com scope, platform, tipo, e validation
- Especificar path resolution rules (relative, absolute, expandable)
- Documentar directory hierarchy com parent-child relationships
- Validar paths contra platform constraints (Windows vs Unix separators)
- Validar artifact contra quality gates (8 HARD + 10 SOFT)
- Distinguir path_config de env_config, permission, feature_flag, runtime_rule
## Routing
keywords: [path, directory, folder, filepath, filesystem, dir, base_dir, log_dir, config_dir, location]
triggers: "define filesystem paths", "create path config", "document directory structure", "specify system paths"
## Crew Role
In a crew, I handle FILESYSTEM PATH SPECIFICATION.
I answer: "what filesystem paths does this scope need, on which platforms, with what defaults?"
I do NOT handle: env_config (generic variables), permission (access control),
feature_flag (on/off toggle), runtime_rule (timeouts/retries).

### bld_instruction_path_config.md
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

### bld_knowledge_card_path_config.md
---
kind: knowledge_card
id: bld_knowledge_card_path_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for path_config production — atomic searchable facts
sources: path-config-builder MANIFEST.md + SCHEMA.md, XDG Base Directory, Windows Known Folders
---

# Domain Knowledge: path_config
## Executive Summary
Path configs are filesystem path catalogs that define every directory and file path a system scope needs — with platform support, default values, expandable variables, and creation order. Each config scopes paths to ONE system area with portable defaults using expandable variables instead of hardcoded absolutes. They differ from env configs (all environment variables), permissions (access control), feature flags (on/off toggles), and runtime rules (behavioral settings) by being the single source of truth for filesystem layout.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (configuration) |
| Kind | `path_config` (exact literal) |
| ID pattern | `p09_path_{slug}` |
| Required frontmatter | 14 fields |
| Quality gates | 8 HARD + 10 SOFT |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Min path entries | 3 |
| Path types | dir, file, glob |
| Platform field | required (target OS or list of supported OS) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Expandable variables | Use $HOME, {{USER_DIR}}, $XDG_DATA_HOME — never hardcoded user paths |
| Platform normalization | Define with forward slashes; resolve per-platform at runtime |
| Directory hierarchy | base_dir -> {data, config, cache, logs, temp} as tree |
| Required vs optional | Required paths block startup if missing; optional created on demand |
| Relative preference | Prefer relative to base_dir; absolute only for system-level paths |
| Explicit defaults | Every path has a default value (null acceptable if documented) |
| Creation order | Document which paths must exist before others |
### XDG Mapping Reference
| XDG Variable | Purpose | Windows Equivalent |
|-------------|---------|-------------------|
| $XDG_DATA_HOME | User data | %APPDATA% |
| $XDG_CONFIG_HOME | User config | %APPDATA% |
| $XDG_CACHE_HOME | Cache files | %LOCALAPPDATA%\cache |
| $XDG_STATE_HOME | State data | %LOCALAPPDATA% |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Hardcoded user paths (/home/john/) | Breaks on any other machine |
| No platform field | Paths are platform-dependent; undeclared = silent breakage |
| Missing defaults | Forces manual config on every installation |
| Fewer than 3 path entries | Doesn't justify a config artifact |
| Mixed separators (/ and \\) | Inconsistent; pick one and resolve at runtime |
| No creation order | Dependencies between paths cause race conditions |
## Application
1. Define scope: which system area does this path config govern?
2. List all paths with name, type (dir/file/glob), and default value
3. Set platform field (target OS or supported OS list)
4. Use expandable variables for all user-specific absolute paths
5. Mark each path as relative_or_absolute explicitly
6. Document directory hierarchy (parent-child relationships)
7. Specify creation_order for initialization from scratch
8. Validate: 8 HARD + 10 SOFT gates, body <= 3072 bytes
## References
- path-config-builder SCHEMA.md v1.0.0
- XDG Base Directory Specification
- Windows Known Folder IDs (MSDN)
- Python pathlib documentation

### bld_quality_gate_path_config.md
---
id: p11_qg_path_config
kind: quality_gate
pillar: P11
title: "Gate: path_config"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: path_config
quality: null
tags: [quality-gate, path-config, P11, P09, governance, filesystem]
tldr: "Gates for path_config artifacts — portable paths catalog with platform spec, expandable variables, and creation order."
density_score: 0.85
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
| H09 | No user-specific absolute paths (all absolute paths use expandable variables such as $HOME or {{USER_DIR}}) | Hardcoded user paths break on any other machine |
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
| conditions | Emergency hotfix requiring path override before full catalog review completes |
| approver | p09-chief |
| audit_trail | Log in records/audits/ with override path, platform, and timestamp |
| expiry | 48h — full catalog must pass gates before next deploy cycle |
| never_bypass | H01 (YAML), H05 (quality null) |

### bld_schema_path_config.md
---
kind: schema
id: bld_schema_path_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for path_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: path_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_path_{scope_slug}) | YES | - | Namespace compliance |
| kind | literal "path_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| scope | string | YES | - | Config scope: global, satellite, service |
| paths | list[string], len >= 1 | YES | - | Path names defined |
| platform | enum: windows, unix, all | YES | all | Target platform |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "path_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What these paths cover |
| base_dir | string | REC | - | Root directory for relative paths |
| dir_count | integer | REC | - | Number of directory paths |
| file_count | integer | REC | - | Number of file paths |
## ID Pattern
Regex: `^p09_path_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — scope, purpose, platform, base directory, consumers
2. `## Path Catalog` — table: name, type (dir/file), platform, default, required, notes
3. `## Directory Hierarchy` — ASCII tree showing parent-child path relationships
4. `## Platform Notes` — platform-specific path differences, resolution rules
## Constraints
- max_bytes: 3072 (body only)
- naming: p09_path_{scope_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- paths list MUST match path names in ## Path Catalog
- quality: null always
- NEVER include user-specific absolute paths (use expandable vars)
- Forward slashes in templates (normalize at runtime)

### bld_examples_path_config.md
---
kind: examples
id: bld_examples_path_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of path_config artifacts
pattern: few-shot learning — LLM reads these before producing
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
quality: null
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
| base_dir | dir | all | {{APP_ROOT}}/data_pipeline | yes | Root for all pipeline paths |
| input_dir | dir | all | {{base_dir}}/input | yes | Raw data ingestion directory |
| output_dir | dir | all | {{base_dir}}/output | yes | Processed output directory |
| staging_dir | dir | all | {{base_dir}}/staging | no | Temp staging area, auto-created |
| log_dir | dir | all | {{base_dir}}/logs | no | Pipeline execution logs |
| config_dir | dir | all | {{base_dir}}/config | yes | Pipeline configuration files |
| cache_dir | dir | all | {{base_dir}}/cache | no | Intermediate cache, purgeable |
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

### bld_architecture_path_config.md
---
kind: architecture
id: bld_architecture_path_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of path_config — inventory, dependencies, and architectural position
---

# Architecture: path_config in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, platform, scope, etc.) | path-config-builder | active |
| path_catalog | Master list of all paths with type, default, and description | author | active |
| platform_rules | Platform-specific separator and expansion rules (Windows/Linux/Mac) | author | active |
| resolution_strategy | How relative paths resolve to absolute paths at runtime | author | active |
| directory_hierarchy | Parent-child relationships between directories | author | active |
| validation_rules | Checks for path existence, permissions, and platform compliance | author | active |
## Dependency Graph
```
env_config      --produces-->  path_config  --consumed_by-->  agent
boot_config     --depends-->   path_config  --consumed_by-->  spawn_config
path_config     --signals-->   path_resolution_error
```
| From | To | Type | Data |
|------|----|------|------|
| env_config (P09) | path_config | data_flow | environment variables used in path expansion |
| path_config | agent (P02) | consumes | agent reads paths for file operations |
| path_config | spawn_config (P12) | consumes | spawn scripts use paths for working directories |
| boot_config (P02) | path_config | dependency | boot sequence needs paths for initialization |
| path_config | path_resolution_error (P12) | signals | emitted when a path fails validation |
| permission (P09) | path_config | dependency | access control may restrict certain paths |
## Boundary Table
| path_config IS | path_config IS NOT |
|----------------|-------------------|
| A specification of filesystem paths with platform awareness | A generic environment variable store (env_config P09) |
| Scoped to a domain with directory hierarchy documented | An access control rule for paths (permission P09) |
| Platform-aware with Windows/Linux/Mac resolution rules | A feature toggle (feature_flag P09) |
| Includes validation for existence and permissions | A runtime behavior parameter (runtime_rule P09) |
| Documents parent-child directory relationships | A naming convention for artifacts (naming_rule P05) |
| Resolves relative to absolute using defined strategy | A hardcoded absolute path without expansion |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Environment | env_config, platform_rules | Supply variables and platform constraints |
| Catalog | frontmatter, path_catalog, directory_hierarchy | List all paths with relationships |
| Resolution | resolution_strategy | Define how paths are expanded and resolved |
| Validation | validation_rules | Check paths exist and are accessible |
| Consumers | agent, spawn_config, boot_config | Systems that read and use the configured paths |

### bld_collaboration_path_config.md
---
kind: collaboration
id: bld_collaboration_path_config
pillar: P09
llm_function: COLLABORATE
purpose: How path-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: path-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what filesystem paths does this scope need, on which platforms, with what defaults?"
I define directories, file locations, path resolution rules, and platform-specific separators. I do NOT handle generic environment variables (env-config-builder), access control (permission-builder), or on/off toggles (feature-flag-builder).
## Crew Compositions
### Crew: "System Configuration Bootstrap"
```
  1. path-config-builder  -> "defines all filesystem paths the system needs"
  2. env-config-builder   -> "defines environment variables that reference those paths"
  3. permission-builder   -> "defines who can read/write each path"
```
### Crew: "Plugin Deployment Setup"
```
  1. plugin-builder       -> "defines the plugin and its required directories"
  2. path-config-builder  -> "specifies install path, config path, log path per platform"
  3. boot-config-builder  -> "wires path config into system startup sequence"
```
### Crew: "Data Pipeline Setup"
```
  1. path-config-builder  -> "input/output/staging/cache directory structure"
  2. env-config-builder   -> "env vars for pipeline configuration"
  3. runtime-rule-builder -> "timeout and retry rules for pipeline steps"
```
## Handoff Protocol
### I Receive
- seeds: scope name, target platforms (Windows/Linux/Mac), directory types needed (workspace/logs/config/cache)
- optional: existing directory structure to document, relative vs absolute preference
### I Produce
- path_config artifact (Markdown, max 4KB)
- committed to: `cex/P09/examples/p09_path_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- plugin-builder: declares what directories a plugin requires before I specify them
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| env-config-builder | references my paths as values for environment variables |
| permission-builder | applies access rules to paths I defined |
| boot-config-builder | uses my paths during system startup sequence |
| daemon-builder | needs log_dir, pid file, and working directory paths |

### bld_config_path_config.md
---
kind: config
id: bld_config_path_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: path_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_path_{scope_slug}.yaml` | `p09_path_data_pipeline.yaml` |
| Builder directory | kebab-case | `path-config-builder/` |
| Frontmatter fields | snake_case | `base_dir`, `dir_count` |
| Scope slug | snake_case, lowercase, no hyphens | `data_pipeline`, `global`, `shaka` |
| Path names | snake_case | `base_dir`, `log_dir`, `config_dir` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P09_config/examples/p09_path_{scope_slug}.yaml`
- Compiled: `cex/P09_config/compiled/p09_path_{scope_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total (frontmatter + body): ~4500 bytes
- Density: >= 0.80 (no filler)
## Path Template Conventions
| Pattern | Resolves to | Example |
|---------|------------|---------|
| {{HOME}} | User home directory | /home/user, C:\Users\user |
| {{APP_ROOT}} | Application root | /opt/app, C:\app |
| {{TEMP}} | System temp directory | /tmp, C:\Users\user\AppData\Local\Temp |
| {{base_dir}} | Scope base directory | Defined in artifact base_dir field |
## Platform Rules
| Platform | Separator | Long paths | Case |
|----------|-----------|------------|------|
| windows | \ (resolved at runtime) | \\?\ prefix for >260 chars | case-insensitive |
| unix | / | no limit (practical) | case-sensitive |
| all | / in templates | handle per-platform | follow platform default |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `path-config-builder` for pipeline function `CONSTRAIN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
