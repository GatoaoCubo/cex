---
id: n00_path_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Path Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, path_config, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_path_config
  - bld_collaboration_path_config
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_sandbox_config
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - path-config-builder
  - p03_ins_path_config
  - bld_architecture_path_config
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A path_config declares all filesystem paths that a nucleus or tool depends on: artifact directories, cache locations, signal directories, PID files, and log paths. It prevents hardcoded paths from breaking when the repo is moved, cloned, or deployed to a new machine, and enables cex_setup_validator.py to verify path existence before boot.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `path_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| scope | string | yes | Which nucleus or tool this path set covers |
| paths | list | yes | List of path definitions |
| paths[].name | string | yes | Logical name for this path |
| paths[].value | string | yes | Actual path (may use env var tokens like ${CEX_ROOT}) |
| paths[].must_exist | boolean | yes | If true, boot fails if path is absent |
| paths[].create_if_missing | boolean | no | Auto-create directory on first use |
| paths[].description | string | yes | What this path is used for |

## When to use
- Documenting all paths a new nucleus depends on during boot validation
- Centralizing path definitions so tools don't hardcode them independently
- Enabling cross-platform path resolution (Windows vs Linux vs macOS)

## Builder
`archetypes/builders/path_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind path_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: path_config_runtime
kind: path_config
pillar: P09
nucleus: n07
title: "CEX Runtime Path Config"
version: 1.0
quality: null
---
scope: runtime
paths:
  - name: signals_dir
    value: .cex/runtime/signals
    must_exist: true
    create_if_missing: true
    description: Directory for inter-nucleus signal files
  - name: handoffs_dir
    value: .cex/runtime/handoffs
    must_exist: true
    create_if_missing: true
    description: Handoff markdown files for dispatched nuclei
```

## Related kinds
- `env_config` (P09) -- environment variables that often contain path values
- `secret_config` (P09) -- secret file paths managed separately from data paths
- `sandbox_config` (P09) -- sandboxes define isolated path namespaces

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_path_config]] | upstream | 0.52 |
| [[bld_collaboration_path_config]] | related | 0.41 |
| [[bld_schema_reranker_config]] | upstream | 0.39 |
| [[bld_schema_usage_report]] | upstream | 0.39 |
| [[bld_schema_sandbox_config]] | upstream | 0.39 |
| [[bld_schema_benchmark_suite]] | upstream | 0.39 |
| [[bld_schema_dataset_card]] | upstream | 0.38 |
| [[path-config-builder]] | related | 0.38 |
| [[p03_ins_path_config]] | upstream | 0.38 |
| [[bld_architecture_path_config]] | upstream | 0.38 |
