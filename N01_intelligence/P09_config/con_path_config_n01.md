---
id: con_path_config_n01
kind: path_config
pillar: P09
nucleus: n01
title: N01 Path Config
version: 1.0
quality: 9.0
tags: [path_config, filesystem, research, runtime]
density_score: 1.0
---

<!-- 8F: F1 constrain=P09/path_config F2 become=path-config-builder F3 inject=nucleus_def_n01+n01-intelligence+kc_path_config+P09_schema+path examples F4 reason=bounded path map for research inputs outputs and scratch work F5 call=apply_patch+cex_compile F6 produce=4013 bytes F7 govern=frontmatter+ascii+80-line+self-check F8 collaborate=N01_intelligence/P09_config/con_path_config_n01.md -->

## Purpose

| Item | Decision |
|------|----------|
| Scope | Named filesystem paths for N01 evidence work and outputs |
| Base dir | `N01_intelligence` |
| Platform | all |
| Lens | Analytical Envy separates raw inputs, comparative workspaces, and final intelligence so weak evidence does not contaminate stronger artifacts |
| Readonly policy | source rules and architecture paths stay readonly |

## Values

| Path Alias | Type | Default | Required | Readonly | Notes |
|-----------|------|---------|----------|----------|-------|
| `base_dir` | dir | `N01_intelligence/` | yes | no | root anchor |
| `architecture_dir` | dir | `N01_intelligence/architecture/` | yes | yes | identity reference |
| `rules_dir` | dir | `N01_intelligence/rules/` | yes | yes | nucleus governance |
| `knowledge_dir` | dir | `N01_intelligence/P01_knowledge/` | yes | no | reusable research notes |
| `schemas_dir` | dir | `N01_intelligence/P06_schema/` | yes | no | typed contracts |
| `config_dir` | dir | `N01_intelligence/P09_config/` | yes | no | runtime settings |
| `compiled_dir` | dir | `N01_intelligence/compiled/` | no | no | compiler outputs |
| `output_dir` | dir | `N01_intelligence/P05_output/` | no | no | finished reports |
| `scratch_dir` | dir | `N01_intelligence/_scratch/` | no | no | disposable comparison work |
| `source_cache_dir` | dir | `N01_intelligence/_cache/sources/` | no | no | fetched material cache |
| `benchmark_dir` | dir | `N01_intelligence/_benchmarks/` | no | no | side-by-side evidence tables |
| `agent_card_file` | file | `N01_intelligence/agent_card_n01.md` | yes | yes | runtime identity file |

## Directory Hierarchy

```text
N01_intelligence/
  architecture/
  rules/
  knowledge/
  schemas/
  config/
  compiled/
  output/
  _scratch/
  _cache/
    sources/
  _benchmarks/
  agent_card_n01.md
```

## Path Resolution

| Rule | Behavior |
|------|----------|
| relative first | resolve against repo root, then `N01_intelligence/` |
| slash style | store forward slashes in docs; runtime can normalize |
| creation | writable optional dirs may be created on demand |
| cleanup | only `_scratch` and `_cache` are purge-safe |

## Rationale

| Design Choice | Why | Analytical Envy Interpretation |
|--------------|-----|--------------------------------|
| separate `_benchmarks` dir | keeps comparative tables durable and inspectable | rivalry data deserves its own lane |
| separate `_scratch` dir | early envy experiments should be disposable | do not let half-proved claims look canonical |
| readonly architecture and rules | identity and governance should not drift during execution | discipline preserves analytical consistency |
| compiled and output split | machine derivatives should not mix with final briefs | quality improves when artifact status is visible |
| source cache isolated | fetched evidence needs bounded lifecycle | better to expire stale proof than trust it forever |

## Example

```yaml
base_dir: N01_intelligence/
benchmark_dir: N01_intelligence/_benchmarks/
scratch_dir: N01_intelligence/_scratch/
source_cache_dir: N01_intelligence/_cache/sources/
readonly:
  - N01_intelligence/architecture/
  - N01_intelligence/rules/
  - N01_intelligence/agent_card_n01.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `path_config` |
| Pillar | `P09` |
| Nucleus | `n01` |
| Platform | `all` |
| Dir Count | `11` |
| File Count | `1` |
| Readonly Count | `3` |
| Quality Field | `null` |
