---
id: con_permission_n03
kind: permission
pillar: P09
nucleus: n03
title: Engineering Permission Policy
version: 1.0
quality: null
tags: [config, permission, governance, access, n03]
---


<!-- 8F: F1 constrain=P09/permission F2 become=permission-builder F3 inject=nucleus_def_n03, kc_permission, P09_config, N03 runtime context
     F4 reason=minimum necessary read/write/execute rights for N03 artifact work F5 call=rg, Get-Content, apply_patch F6 produce=4798 bytes
     F7 govern=frontmatter+sections+tables+ascii+self-check F8 collaborate=save N03_engineering/config/con_permission_n03.md -->

# Engineering Permission Policy

## Purpose

| Field | Value |
|-------|-------|
| Mission fit | Access policy for N03 authoring, compilation, and signaling surfaces |
| Pride lens | Permissions are explicit and minimal because elegance without control is vanity |
| Primary use | Define who may read, write, execute, and signal within N03 scope |
| Boundary | Access control only; runtime paths and secret storage are configured elsewhere |
| Model | Whitelist with explicit deny-over-allow behavior |
| Failure prevented | Accidental writes to shared pillars and casual execution beyond builder scope |

## Values

| Subject | Resource | Read | Write | Execute | Notes |
|---------|----------|------|-------|---------|-------|
| `n03_builder` | `N03_engineering/schemas/**` | yes | yes | no | Owns schema markdown |
| `n03_builder` | `N03_engineering/config/**` | yes | yes | no | Owns config markdown |
| `n03_builder` | `N03_engineering/compiled/**` | yes | yes | no | Writes via compile flow |
| `n03_builder` | `archetypes/builders/**` | yes | no | no | Context only |
| `n03_builder` | `P01_knowledge/library/**` | yes | no | no | Context only |
| `n03_builder` | `_tools/cex_compile.py` | yes | no | yes | Compile is allowed |
| `n03_builder` | `_tools/cex_index.py` | yes | no | yes | Optional index pass |
| `n03_builder` | `_tools/signal_writer.py` | yes | no | yes | Completion signal only |
| `n03_builder` | `.cex/runtime/handoffs/**` | yes | no | no | Upstream instructions only |
| `n03_builder` | `.git/**` | no | no | no | Direct git internals are out of scope |
| `n03_builder` | `N0[0-7]_*/**` excluding own root | yes | no | no | Read for examples, never mutate |
| `n07_orchestrator` | `.cex/runtime/signals/**` | yes | yes | no | Reads and consolidates signals |

## Deny Rules

| Rule ID | Subject | Resource | Deny | Why it exists |
|---------|---------|----------|------|---------------|
| `D01` | `n03_builder` | `.git/**` | all | Internal git state is not an authoring surface |
| `D02` | `n03_builder` | `P01_knowledge/**` | write | Knowledge cards are inputs here |
| `D03` | `n03_builder` | `archetypes/builders/**` | write | Builder manifests are references, not scratchpad files |
| `D04` | `n03_builder` | `N00_genesis/**`, `N01_intelligence/**`, `N02_marketing/**`, `N04_knowledge/**`, `N05_operations/**`, `N06_commercial/**` | write | Example reading is allowed, mutation is not |
| `D05` | `n03_builder` | `_tools/**` | write | Tool changes require separate intent and review |
| `D06` | `n03_builder` | secrets by value | read/write | N03 may reference secrets, never expose or persist values |

## Rationale

| Design choice | Why it exists | Pride expression |
|---------------|---------------|------------------|
| Whitelist model | Default-deny keeps accidental power growth visible | Discipline is a design feature |
| Context roots are read-only | Reading examples should not turn into silent edits | Respect other nuclei |
| Execute limited to compile, index, signal | Tooling rights should match mission needs, nothing broader | Precision over convenience |
| Explicit git deny | Avoids unsafe low-level mutation patterns | Strong boundaries protect speed |
| Signal exception for N07 | Collaboration needs one narrow shared write surface | Cooperation without chaos |
| Secret-value deny | Config authorship must never become secret handling | Pride refuses sloppy leakage |

## Example

```yaml
policy_name: n03_engineering_permission_policy
mode: whitelist
subjects:
  - name: n03_builder
    allow:
      read:
        - N03_engineering/**
        - archetypes/builders/**
        - P01_knowledge/library/**
        - .cex/runtime/handoffs/**
      write:
        - N03_engineering/schemas/**
        - N03_engineering/config/**
        - N03_engineering/compiled/**
      execute:
        - _tools/cex_compile.py
        - _tools/cex_index.py
        - _tools/signal_writer.py
deny_overrides: true
```

## Properties

| Property | Value |
|----------|-------|
| Nucleus | `n03` |
| Pillar | `P09` |
| Kind | `permission` |
| Mode | `whitelist` |
| Allow rows | `12` |
| Deny rules | `6` |
| Deny precedence | `true` |
| Lens | `Inventive Pride` |
