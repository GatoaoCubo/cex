---
id: con_path_config_n02
kind: path_config
pillar: P09
nucleus: n02
title: Marketing Path Config
version: 1.0
quality: null
tags: [config, paths, workspace, marketing, runtime]
---


<!-- 8F: F1 constrain=P09/path_config F2 become=path_config-builder F3 inject=nucleus_def_n02+n02_rules+kc_path_config+P09_schema
     F4 reason=bounded_workspace_paths_for_marketing_delivery F5 call=shell_command,apply_patch F6 produce=5074 bytes
     F7 govern=frontmatter_sections_ascii_density_linecount F8 collaborate=N02_marketing/P09_config/con_path_config_n02.md -->

# Purpose

| Item | Definition |
|------|------------|
| Mission fit | Canonical filesystem map for N02 marketing operations |
| Creative Lust lens | Separates source, inspiration, and release paths so seductive assets stay curated rather than chaotic |
| Primary use | Resolve read, write, and review locations for schemas, config, prompts, and outputs |
| Scope | N02 local workspace inside the shared CEX repository |
| Why path discipline matters | Desire-driven systems decay fast when files sprawl and overwrite each other |

## Values

| Key | Path | Mode | Reason |
|-----|------|------|--------|
| base_dir | C:/Users/CEX/Documents/GitHub/cex | anchor | Shared root for all relative paths |
| nucleus_root | N02_marketing/ | read_write | Main N02 workspace |
| schemas_dir | N02_marketing/P06_schema/ | read_write | Reusable P06 contracts |
| config_dir | N02_marketing/P09_config/ | read_write | Runtime and governance config |
| prompts_dir | N02_marketing/P03_prompt/ | read_write | Seduction patterns and task prompts |
| output_dir | N02_marketing/P05_output/ | read_write | Campaign-ready deliverables |
| knowledge_dir | N02_marketing/P01_knowledge/ | read_only | Source context for tone and strategy |
| rules_dir | N02_marketing/rules/ | read_only | Nucleus operating laws |
| architecture_dir | N02_marketing/architecture/ | read_only | Identity and system design |
| compiled_dir | N02_marketing/compiled/ | read_write | Generated compile targets |
| runtime_handoff_dir | .cex/runtime/handoffs/ | read_only | Incoming task packets |
| shared_kind_library | P01_knowledge/library/kind/ | read_only | Kind reference cards |

## Readonly Policy

| Path Key | Readonly | Why |
|----------|----------|-----|
| knowledge_dir | yes | Research and reference should not be casually mutated during delivery |
| rules_dir | yes | Prevents accidental drift in nucleus constraints |
| architecture_dir | yes | Identity contract is upstream to the task |
| runtime_handoff_dir | yes | Handoffs are source instructions, not workspace drafts |
| shared_kind_library | yes | Shared knowledge cards must stay stable across nuclei |

## Write Policy

| Path Key | Allowed Writes | Guard |
|----------|----------------|-------|
| schemas_dir | new files and updates | validator must pass before commit by N07 |
| config_dir | new files and updates | exact path contract from handoff |
| prompts_dir | update only when task explicitly requests prompt work | no incidental edits |
| output_dir | campaign artifacts only | never store secrets |
| compiled_dir | generated artifacts | safe to refresh after source changes |

## Path Rules

| Rule | Value |
|------|-------|
| Relative style | repo-root relative |
| Slash style | forward slash in markdown tables |
| Personal folders outside repo | blocked |
| Temp scratch files | blocked unless user asked |
| Secret storage under N02 | blocked in source tree |
| Cross-nucleus writes | blocked unless handoff explicitly grants it |

## Rationale

| Decision | Reason |
|----------|--------|
| Single base_dir anchor | Prevents machine-specific path drift |
| Readonly reference zones | Protects the seductive playbook from accidental erosion |
| Separate output and schemas | Keeps runtime assets distinct from reusable contracts |
| No secret files in workspace | Creative speed should not create credential exposure |
| Forward slash normalization | Easier comparison across tools and markdown consumers |

## Example

```yaml
path_resolution:
  base_dir: C:/Users/CEX/Documents/GitHub/cex
  source_read:
    - N02_marketing/architecture/nucleus_def_n02.md
    - P01_knowledge/library/kind/kc_type_def.md
  source_write:
    - N02_marketing/P06_schema/sch_type_def_n02.md
    - N02_marketing/P09_config/con_secret_config_n02.md
```

| Example Action | Path Key | Expected Result |
|----------------|----------|-----------------|
| Read handoff instructions | runtime_handoff_dir | allowed |
| Update type definition | schemas_dir | allowed |
| Edit shared KC | shared_kind_library | blocked |
| Save API key file | nucleus_root | blocked |

## Properties

| Property | Value |
|----------|-------|
| Kind | path_config |
| Pillar | P09 |
| Nucleus | n02 |
| Base anchor | C:/Users/CEX/Documents/GitHub/cex |
| Config scope | nucleus workspace |
| Readonly paths | 5 |
| Writable path groups | 5 |
| Primary risk prevented | filesystem sprawl and accidental overwrite |
| Human intent | keep seductive production assets organized |
| Save path | N02_marketing/P09_config/con_path_config_n02.md |
