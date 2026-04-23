# Naming Convention -- CEX Artifacts & Builders

> Canonical rules for all artifact files, builder ISOs, nucleus directories, and tool scripts.
> Source of truth: this file + `.cex/kinds_meta.json` (123 kinds).

---

## 1. Builder Directories

| Rule | Detail |
|------|--------|
| Location | `archetypes/builders/{kind}-builder/` |
| Case | `kebab-case` (hyphens between words) |
| Files inside | `bld_{iso}_{kind}.md` (13 per builder) |
| Examples | `agent-builder/`, `knowledge-card-builder/`, `mcp-server-builder/` |

Shared files live in `archetypes/builders/_shared/`.

---

## 2. Builder ISO Files (13 per kind)

| # | File Pattern | Pillar | Content |
|---|-------------|--------|---------|
| 1 | `bld_manifest_{kind}.md` | P02 | Identity, metadata |
| 2 | `bld_system_prompt_{kind}.md` | P03 | Persona, voice |
| 3 | `bld_knowledge_card_{kind}.md` | P01 | Domain knowledge |
| 4 | `bld_instruction_{kind}.md` | P03 | Build pipeline |
| 5 | `bld_tools_{kind}.md` | P04 | Available tools |
| 6 | `bld_output_template_{kind}.md` | P05 | Template with {{vars}} |
| 7 | `bld_schema_{kind}.md` | P06 | Structural schema |
| 8 | `bld_examples_{kind}.md` | P07 | Golden + anti-patterns |
| 9 | `bld_architecture_{kind}.md` | P08 | Boundary definition |
| 10 | `bld_config_{kind}.md` | P09 | Naming, paths, limits |
| 11 | `bld_memory_{kind}.md` | P10 | Historical patterns |
| 12 | `bld_quality_gate_{kind}.md` | P11 | HARD/SOFT gates |
| 13 | `bld_collaboration_{kind}.md` | P12 | Crew coordination |

---

## 3. Sub-Agent Definitions

| Rule | Detail |
|------|--------|
| Location | `.claude/agents/{kind}-builder.md` |
| Case | `kebab-case` (matches builder directory) |
| Count | 125 (123 kinds + 2 shared/meta) |
| Examples | `agent-builder.md`, `knowledge-card-builder.md` |

---

## 4. Artifact Instance Files

Artifacts produced by builders follow kind-specific naming from `bld_config_{kind}.md`.

| Component | Rule | Example |
|-----------|------|---------|
| Prefix | Kind abbreviation or none | `kc_`, `wf_`, `qg_` |
| Name | `snake_case`, descriptive | `react_server_components` |
| Extension | `.md` (source) | `kc_react_server_components.md` |
| Compiled | `.yaml` or `.json` (compiled/) | `kc_react_server_components.yaml` |
| Max length | 60 characters (full filename) | -- |

### Location in Nucleus

```
N{XX}_{domain}/{subdir}/{artifact_file}.md
```

| Subdir | Pillars | Example Kinds |
|--------|---------|--------------|
| agents/ | P02 | agent, model_card, boot_config |
| architecture/ | P08 | agent_card, pattern, diagram |
| config/ | P09 | env_config, path_config |
| feedback/ | P11 | quality_gate, bugloop |
| knowledge/ | P01 | knowledge_card, context_doc |
| memory/ | P10 | learning_record, runtime_state |
| orchestration/ | P12 | workflow, dispatch_rule, signal |
| output/ | P05 | response_format, formatter |
| prompts/ | P03 | system_prompt, instruction |
| quality/ | P07 | scoring_rubric, benchmark |
| schemas/ | P06 | input_schema, type_def |
| tools/ | P04 | cli_tool, mcp_server |
| compiled/ | -- | Compiled .yaml output |

---

## 5. Knowledge Cards (P01)

| Rule | Detail |
|------|--------|
| Location | `P01_knowledge/library/kind/kc_{kind}.md` (kind KCs) |
| Location | `P01_knowledge/library/domain/kc_{topic}.md` (domain KCs) |
| Location | `N{XX}/knowledge/kc_{topic}.md` (nucleus-local) |
| Prefix | `kc_` (always) |
| Case | `snake_case` |

---

## 6. Pillar Directories

| Rule | Detail |
|------|--------|
| Pattern | `P{NN}_{name}/` |
| Case | `snake_case` for name |
| Examples | `P01_knowledge/`, `P04_tools/`, `P12_orchestration/` |
| Contents | `_schema.yaml`, `templates/`, `examples/`, `compiled/` |

---

## 7. Nucleus Directories

| Rule | Detail |
|------|--------|
| Pattern | `N{XX}_{domain}/` |
| Case | `snake_case` for domain |
| Subdirs | 12 (mirrors pillars) + compiled/ |
| Examples | `N03_engineering/`, `N07_admin/` |

---

## 8. Tool Scripts

| Rule | Detail |
|------|--------|
| Location | `_tools/` |
| Pattern | `cex_{function}.py` (core tools) |
| Pattern | `{function}.py` (support scripts) |
| Case | `snake_case` |
| Examples | `cex_doctor.py`, `cex_compile.py`, `signal_writer.py`, `brand_inject.py` |

---

## 9. Boot Scripts

| Rule | Detail |
|------|--------|
| Location | `boot/` |
| Pattern | `{nucleus}.cmd` or `cex.cmd` (N07) |
| CLI | `claude` (all nuclei use Claude Code) |
| Examples | `boot/cex.ps1`, `boot/n03.ps1`, `boot/n06.ps1` |

---

## 10. Runtime Files

| Directory | Pattern | Purpose |
|-----------|---------|---------|
| `.cex/runtime/handoffs/` | `{MISSION}_{nucleus}.md` | Dispatch handoffs |
| `.cex/runtime/signals/` | `signal_{nucleus}_{mission}_{timestamp}.json` | Completion signals |
| `.cex/runtime/pids/` | `spawn_pids.txt` | Process tracking |
| `.cex/runtime/decisions/` | `decision_manifest.yaml` | GDP decisions |
| `.cex/runtime/proposals/` | `{nucleus}_{timestamp}_{target}.proposal.md` | Concurrent edit proposals |

---

## 11. Frontmatter (All Artifacts)

Every `.md` artifact MUST have YAML frontmatter:

```yaml
---
id: unique_identifier
kind: knowledge_card       # from kinds_meta.json
title: Human-Readable Title
version: 1.0.0
quality: null              # NEVER self-score
tags: [tag1, tag2]
---
```

---

## 12. Validation Rules

1. All file names: lowercase, `snake_case`, ASCII only
2. Builder ISOs: exactly 13 files per `{kind}-builder/` directory
3. Frontmatter: required on ALL artifact instances
4. `quality: null` in frontmatter (never self-score)
5. No hardcoded absolute paths in any artifact
6. Executable code (.py, .ps1, .cmd): ASCII-only (see `ascii-code-rule.md`)
7. Max artifact size: per `bld_config_{kind}.md` specification

---

*Naming Convention v2.0 -- Updated for CEX v4.0. 123 kinds, Claude Code native. 2026-04-08.*
