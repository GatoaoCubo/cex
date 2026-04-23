---
id: con_path_config_n04
kind: path_config
pillar: P09
nucleus: n04
title: Knowledge Path Config
version: 1.0
quality: 9.0
tags: [config, path, knowledge, storage, index]
density_score: 1.0
related:
  - p09_path_{{SCOPE_SLUG}}
  - p02_bc_builder_nucleus
  - bld_memory_path_config
  - path-config-builder
  - p03_sp_path_config_builder
  - bld_collaboration_path_config
  - bld_schema_path_config
  - p01_kc_path_config
  - bld_tools_path_config
  - bld_knowledge_card_path_config
---
<!-- 8F: F1 constrain=P09/path_config F2 become=path-config-builder F3 inject=n04-knowledge+kc_path_config+P09 examples+repo layout F4 reason=bounded filesystem map for hungry but disciplined knowledge storage F5 call=shell,apply_patch F6 produce=4879 bytes F7 govern=frontmatter+ascii+density+80-line self-check F8 collaborate=N04_knowledge/P09_config/con_path_config_n04.md -->
# Knowledge Path Config
## Purpose
N04 accumulates source material, compiled artifacts, embeddings, and audit outputs quickly.
The Knowledge Gluttony lens therefore needs a bounded path map: gather many files, but place each class of knowledge in a named location so the nucleus can hoard without becoming unreadable.
This path config defines the authoritative directory aliases for N04 work.
## Values
| Alias | Path | Type | Writable | Purpose |
|-------|------|------|----------|---------|
| root | `${CEX_ROOT}` | absolute | no | repository anchor |
| n04_home | `${CEX_ROOT}/N04_knowledge` | absolute | limited | nucleus root |
| schemas_dir | `${CEX_ROOT}/N04_knowledge/schemas` | absolute | yes | schema artifacts |
| config_dir | `${CEX_ROOT}/N04_knowledge/config` | absolute | yes | config artifacts |
| prompts_dir | `${CEX_ROOT}/N04_knowledge/prompts` | absolute | no | prompt references |
| tools_dir | `${CEX_ROOT}/N04_knowledge/tools` | absolute | limited | tool docs and specs |
| compiled_dir | `${CEX_ROOT}/compiled/N04_knowledge` | absolute | yes | compiled outputs |
| runtime_handoffs | `${CEX_ROOT}/.cex/runtime/handoffs` | absolute | read_mostly | task intake |
| runtime_signals | `${CEX_ROOT}/.cex/runtime/signals` | absolute | limited | completion and status signals |
| cache_dir | `${CEX_ROOT}/_data/n04_cache` | absolute | yes | transient retrieval caches |
| export_dir | `${CEX_ROOT}/_reports/n04_exports` | absolute | yes | audit and export bundles |
## Resolution Rules
| Input form | Resolution rule |
|-----------|-----------------|
| absolute path | use as-is after normalization |
| `${CEX_ROOT}` token | expand from runtime env |
| relative path | resolve from `root` |
| Windows separator | normalize to forward slashes for docs |
| missing writable dir | create lazily with explicit owner check |
## Readonly Registry
| Path alias | Readonly reason |
|------------|-----------------|
| root | avoids accidental repo-wide writes |
| prompts_dir | prompt references should change intentionally |
| runtime_handoffs | intake files are historical evidence |
## Writable Registry
| Path alias | Write policy |
|------------|-------------|
| schemas_dir | artifact generation and revision allowed |
| config_dir | artifact generation and revision allowed |
| compiled_dir | compiler output only |
| cache_dir | transient and purgeable |
| export_dir | generated reports and snapshots |
## Example
```yaml
base_dir: ${CEX_ROOT}
paths:
  n04_home: ${CEX_ROOT}/N04_knowledge
  compiled_dir: ${CEX_ROOT}/compiled/N04_knowledge
  cache_dir: ${CEX_ROOT}/_data/n04_cache
readonly:
  - ${CEX_ROOT}
  - ${CEX_ROOT}/N04_knowledge/prompts
  - ${CEX_ROOT}/.cex/runtime/handoffs
```
## Rationale
| Decision | Knowledge Gluttony angle | Benefit |
|----------|--------------------------|---------|
| separate cache and export dirs | N04 gathers both transient and durable knowledge products | easy purge without losing evidence |
| compiled output isolated | hungry schema work generates many derivatives | prevents pollution of authoring dirs |
| handoffs read-mostly | intake tasks are evidence and should not be rewritten casually | auditability |
| root readonly | gluttony must be scoped to owned zones | avoids cross-nucleus damage |
| forward-slash normalization | many tools read markdown path specs | less platform drift |
## Path Safety Checks
| Check | Rule |
|-------|------|
| root escape | no writable alias may resolve outside `${CEX_ROOT}` |
| user path hardcode | reject `C:/Users/<name>` literals in committed config |
| alias collision | each alias resolves to unique normalized path |
| missing anchor | every alias must descend from `root` unless explicitly external |
## Consumers
| Consumer | Usage |
|----------|-------|
| compiler | writes compiled outputs |
| retrieval cache | stores transient lookup state |
| export jobs | emits audit bundles |
| permission rules | map resource scopes to read/write rights |
## Properties
| Property | Value |
|----------|-------|
| Base dir | `${CEX_ROOT}` |
| Alias count | 11 |
| Readonly aliases | 3 |
| Writable aliases | 5 |
| Normalization style | forward slash |
| External paths allowed | no by default |
| Cache path present | yes |
| Export path present | yes |
| Scope | N04 knowledge |
| Enforcement | permission plus validator |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p09_path_{{SCOPE_SLUG}}]] | sibling | 0.48 |
| [[p02_bc_builder_nucleus]] | upstream | 0.28 |
| [[bld_memory_path_config]] | downstream | 0.25 |
| [[path-config-builder]] | related | 0.25 |
| [[p03_sp_path_config_builder]] | upstream | 0.24 |
| [[bld_collaboration_path_config]] | related | 0.24 |
| [[bld_schema_path_config]] | upstream | 0.23 |
| [[p01_kc_path_config]] | related | 0.22 |
| [[bld_tools_path_config]] | upstream | 0.22 |
| [[bld_knowledge_card_path_config]] | upstream | 0.22 |
