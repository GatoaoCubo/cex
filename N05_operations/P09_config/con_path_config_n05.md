---
id: con_path_config_n05
kind: path_config
pillar: P09
nucleus: n05
title: Ops Path Map
version: 1.0
quality: 9.0
tags: [config, path, operations, filesystem, boundaries]
density_score: 1.0
related:
  - p01_kc_path_config
  - self_audit_n05_codex_2026_04_15
  - p11_qg_path_config
  - bld_schema_path_config
  - p03_ins_path_config
  - bld_memory_path_config
  - bld_tools_path_config
  - bld_knowledge_card_path_config
  - p03_sp_path_config_builder
  - p12_ho_builder_nucleus
---
<!-- 8F: F1 constrain=P09/path_config F2 become=path-config-builder F3 inject=nucleus_def_n05+n05-operations+kc_path_config+P09_config+N05 path usage
     F4 reason=filesystem boundaries for ops artifacts with explicit readonly and write zones F5 call=apply_patch F6 produce=4634 bytes
     F7 govern=self-check headings+tables+gating_wrath+ascii+80_lines F8 collaborate=N05_operations/P09_config/con_path_config_n05.md -->

# Ops Path Map

## Purpose

| Field | Value |
|---|---|
| Intent | Define the path aliases and write boundaries used by N05 operations workflows. |
| Scope | Source review, compiled outputs, signals, runtime handoffs, reports, and logs. |
| Gating Wrath Lens | Separate readonly sources from writable output zones to prevent accidental corruption. |
| Default Posture | Deny writes outside named writable roots. |
| Platform Note | Use repo-relative anchors so CI and local runs resolve identically. |

## Values

| Alias | Relative Path | Mode | Writable | Validation | Why |
|---|---|---|---|---|---|
| repo_root | `.` | anchor | no | must exist | Stable base for all other paths. |
| n05_root | `N05_operations/` | source | no | must exist | Protects authored nucleus files. |
| n05_schemas | `N05_operations/P06_schema/` | source | controlled | must exist | Schema artifacts live here. |
| n05_config | `N05_operations/P09_config/` | source | controlled | must exist | Config artifacts live here. |
| compiled_root | `compiled/` | output | yes | create if missing | Compiled artifacts and indexes. |
| signal_root | `.cex_signals/` | output | yes | create if missing | Status and completion signaling. |
| handoff_root | `.cex/runtime/handoffs/` | input | no | must exist | Read-only task intake. |
| report_root | `_reports/` | output | yes | create if missing | Review and validation reports. |
| tool_root | `_tools/` | source | no | must exist | Operational scripts are protected. |
| temp_ops | `_spawn/` | ephemeral | yes | cleanup required | Worker scratch space only. |

## Boundary Rules

| Rule | Description | Enforcement |
|---|---|---|
| Read-only sources | `repo_root`, `n05_root`, `handoff_root`, `tool_root` are non-destructive by default. | Deny recursive delete and uncontrolled moves. |
| Controlled authoring | `n05_schemas` and `n05_config` allow edits only to declared deliverables. | Prevent collateral edits during missions. |
| Output isolation | `compiled_root`, `signal_root`, `report_root`, `temp_ops` absorb generated noise. | Keeps source tree reviewable. |
| Repo-relative resolution | Absolute user-specific paths are prohibited. | Ensures CI parity and portability. |
| Temp cleanup | `temp_ops` must be purged after execution window. | Avoids stale artifacts affecting later gates. |

## Rationale

| Design Choice | Why It Exists | Gating Wrath Effect |
|---|---|---|
| Writable roots are few | Fewer write targets mean fewer accidental blast zones. | Easier audit and rollback. |
| Read-only handoff path | Intake context must not be mutated mid-run. | Preserves mission integrity. |
| Separate compiled root | Generated files should never blur with source truth. | Keeps review signal sharp. |
| Explicit temp area | Scratch work is useful but dangerous if it lingers. | Forces cleanup discipline. |
| Repo-relative only | User-specific absolutes rot quickly. | Stops environment drift. |

## Example

| Use Case | Alias Path | Allowed Action |
|---|---|---|
| Save schema artifact | `n05_schemas/sch_enum_def_n05.md` | write |
| Read task handoff | `handoff_root/n05_task_codex.md` | read only |
| Compile markdown | `compiled_root/...` | write |
| Emit completion marker | `signal_root/...` | write |

```yaml
base_dir: .
paths:
  repo_root: .
  n05_root: N05_operations/
  n05_schemas: N05_operations/P06_schema/
  n05_config: N05_operations/P09_config/
  compiled_root: compiled/
  signal_root: .cex_signals/
  handoff_root: .cex/runtime/handoffs/
  report_root: _reports/
  tool_root: _tools/
  temp_ops: _spawn/
readonly:
  - repo_root
  - n05_root
  - handoff_root
  - tool_root
```

## Properties

| Property | Value |
|---|---|
| Kind | `path_config` |
| Pillar | `P09` |
| Nucleus | `n05` |
| Resolution Style | Repo-relative aliases |
| Write Policy | Allow only named writable roots |
| Portability | Windows and CI safe because no user-specific paths |
| Failure Mode | Unknown path alias resolves to denied |
| Sin Lens | Gating Wrath: path ambiguity is treated as a defect, not a convenience. |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_path_config]] | related | 0.27 |
| [[self_audit_n05_codex_2026_04_15]] | upstream | 0.25 |
| [[p11_qg_path_config]] | downstream | 0.23 |
| [[bld_schema_path_config]] | upstream | 0.23 |
| [[p03_ins_path_config]] | upstream | 0.23 |
| [[bld_memory_path_config]] | downstream | 0.23 |
| [[bld_tools_path_config]] | upstream | 0.22 |
| [[bld_knowledge_card_path_config]] | upstream | 0.21 |
| [[p03_sp_path_config_builder]] | upstream | 0.21 |
| [[p12_ho_builder_nucleus]] | downstream | 0.20 |
