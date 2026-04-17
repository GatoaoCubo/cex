---
id: con_path_config_n03
kind: path_config
pillar: P09
nucleus: n03
title: Engineering Path Config
version: 1.0
quality: null
tags: [config, paths, engineering, filesystem, n03]
---


<!-- 8F: F1 constrain=P09/path_config F2 become=path-config-builder F3 inject=nucleus_def_n03, kc_path_config, P09_config, sibling config examples
     F4 reason=authoritative filesystem map for N03 build and validation surfaces F5 call=rg, Get-Content, apply_patch F6 produce=4770 bytes
     F7 govern=frontmatter+sections+tables+ascii+self-check F8 collaborate=save N03_engineering/P09_config/con_path_config_n03.md -->

# Engineering Path Config

## Purpose

| Field | Value |
|-------|-------|
| Mission fit | Canonical filesystem map for N03 source, compiled, runtime, and signal paths |
| Pride lens | Paths are named, bounded, and separated by ownership so no artifact wanders |
| Primary use | Guide builders, validators, and orchestration around where N03 reads and writes |
| Boundary | Filesystem locations only; access control lives in `permission` |
| Base anchor | `CEX_ROOT` |
| Failure prevented | User-specific hardcoding and accidental writes into shared sources |

## Values

| Alias | Relative path | Mode | Scope | Rule |
|-------|---------------|------|-------|------|
| `n03_root` | `N03_engineering/` | read_write | all | Home boundary for nucleus-owned artifacts |
| `n03_schemas` | `N03_engineering/P06_schema/` | read_write | schema builds | Source markdown for P06 outputs |
| `n03_config` | `N03_engineering/P09_config/` | read_write | config builds | Source markdown for P09 outputs |
| `n03_compiled` | `N03_engineering/compiled/` | read_write | compile stage | Generated YAML output only |
| `n03_quality` | `N03_engineering/quality/` | read_write | review | Quality artifacts and audits |
| `n03_output` | `N03_engineering/P05_output/` | read_write | reports | Human-oriented generated reports |
| `handoff_root` | `.cex/runtime/handoffs/` | read_only | mission | Upstream task source |
| `signal_root` | `.cex/runtime/signals/` | read_write | mission | Completion signaling |
| `builder_root` | `archetypes/builders/` | read_only | context load | Builder manifests and ISOs |
| `kind_kc_root` | `P01_knowledge/library/kind/` | read_only | context load | Kind knowledge cards |
| `pillar_schema_root` | `P06_schema/` and `P09_config/` | read_only | constrain | Pillar-level schema sources |
| `tool_root` | `_tools/` | read_only | compile, validate | Tooling invoked by N03 |

## Resolution Rules

| Rule ID | Statement | Why it matters |
|---------|-----------|----------------|
| `P01` | All writable aliases resolve under `CEX_ROOT` | Prevents off-repo drift |
| `P02` | Read-only aliases must never be used as output targets | Protects shared references |
| `P03` | `n03_compiled` is generated-only and should not host authored markdown | Clean source/output separation |
| `P04` | Mission execution reads handoffs from runtime paths but writes artifacts only inside N03-owned areas | N07 dispatch remains upstream |
| `P05` | Absolute paths may appear only after resolution, never as stored config values | Portability first |
| `P06` | Path aliases are referenced by name in docs and tooling whenever possible | Naming beats brittle string repetition |

## Rationale

| Design choice | Why it exists | Pride expression |
|---------------|---------------|------------------|
| Alias-based mapping | Names carry meaning and reduce path copy errors | Orderly systems leave clean trails |
| Separate source and compiled roots | Human-authored markdown and generated YAML should never blur | Craft respects materials |
| Read-only context roots | Shared knowledge and builder inputs are not casual scratch space | Respect upstream artifacts |
| Runtime paths included | Mission work uses real handoffs and signals | Theory stays connected to operations |
| No user-specific absolute defaults | The config should survive machine changes | Strong design travels well |
| Twelve aliases only | Enough coverage without turning path config into a map dump | Disciplined completeness |

## Example

```yaml
base_dir: ${CEX_ROOT}
paths:
  n03_root: N03_engineering/
  n03_schemas: N03_engineering/P06_schema/
  n03_config: N03_engineering/P09_config/
  n03_compiled: N03_engineering/compiled/
  handoff_root: .cex/runtime/handoffs/
  signal_root: .cex/runtime/signals/
readonly:
  - archetypes/builders/
  - P01_knowledge/library/kind/
  - P06_schema/
  - P09_config/
resolution:
  absolute_allowed_at_runtime_only: true
```

## Properties

| Property | Value |
|----------|-------|
| Nucleus | `n03` |
| Pillar | `P09` |
| Kind | `path_config` |
| Aliases | `12` |
| Writable aliases | `7` |
| Read-only roots | `5` |
| Base anchor | `${CEX_ROOT}` |
| Lens | `Inventive Pride` |
