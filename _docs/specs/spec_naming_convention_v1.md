---
id: spec_naming_convention_v1
kind: constraint_spec
pillar: P06
title: "Spec -- CEX Artifact Naming Convention v1"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: CEX naming system
quality: 9.2
status: ACTIVE
scope: "N00-N07 pillar artifacts (.md and .yaml inside P01-P12 subdirs)"
depends_on:
  - spec_structural_alignment_v1
  - _tools/cex_naming_validator.py
  - P08_architecture/examples/ex_naming_rule_cex_naming.md
tags: [spec, naming, convention, structural-alignment, P06, constraint]
tldr: "Every artifact in N0x/P{nn}_*/ must be named: p{nn}_{kind}_{descriptor}_{nxx}.{ext}"
density_score: 0.95
updated: "2026-04-17"
---

<!-- 8F: F1=constraint_spec P06 F2=naming-rule-builder F3=kc_naming_rule+ex_cex_naming+STRUCT_ALIGN_spec F4=autonomous F5=scan F6=write F7=quality_gate F8=save -->

## Problem

CEX describes 8 nuclei x 12 pillars x 300 kinds but artifact filenames inside nucleus
directories do not encode this structure. Files named `agent_intelligence.md`,
`kc_tool_shed.md`, or `LEVERAGE_MAP_V2.md` are opaque: pillar, kind, and nucleus
ownership cannot be determined without opening the file.

**3 consequences:**
1. Tool navigation requires file-open to determine context (token cost)
2. Automated cross-reference tooling breaks on inconsistent prefixes
3. New contributors cannot infer correct naming from examples alone

## Canonical Convention

```
p{nn}_{kind}_{descriptor}_{nxx}.{ext}
```

| Segment | Rule | Characters | Example |
|---------|------|-----------|---------|
| `p{nn}` | 2-digit zero-padded pillar number | `[p]\d{2}` | `p01`, `p09`, `p12` |
| `{kind}` | Kind name from kinds_meta.json (snake_case) | `[a-z][a-z0-9_]+` | `knowledge_card`, `agent`, `env_config` |
| `{descriptor}` | Short contextual identifier (snake_case) | `[a-z][a-z0-9_]*` | `competitor_analysis`, `intelligence`, `precommit` |
| `{nxx}` | Nucleus code | `[n]\d{2}` | `n01`, `n07`, `n00` |
| `{ext}` | Extension | `.md` or `.yaml` | `.md` for docs, `.yaml` for configs |

**Regex (canonical test):**
```
^p\d{2}_[a-z][a-z0-9_]+_[a-z][a-z0-9_]*_n\d{2}\.(md|yaml)$
```

### Examples

| File | Status | Notes |
|------|--------|-------|
| `p01_knowledge_card_competitor_analysis_n01.md` | [OK] | Full convention |
| `p02_agent_intelligence_n01.md` | [OK] | Single-word descriptor |
| `p06_validator_precommit_n07.md` | [OK] | P06 schema artifact |
| `p09_env_config_litellm_n05.md` | [OK] | P09 config artifact |
| `p12_workflow_content_publish_n02.md` | [OK] | P12 orchestration |
| `agent_intelligence.md` | [WARN] | Missing pillar prefix AND nucleus suffix |
| `kc_tool_shed.md` | [WARN] | Legacy `kc_` prefix |
| `sch_validator_n01.md` | [WARN] | Legacy `sch_` prefix |
| `p02_agent_n01.md` | [WARN] | No descriptor segment |
| `LEVERAGE_MAP_V2.md` | [FAIL] | No pillar or nucleus encoding |

## Scope

**Applies to:** `.md` and `.yaml` files inside `N{xx}_*/P{nn}_*/` directories.

**Excluded** (governed by separate conventions):

| Location | Convention | Notes |
|----------|-----------|-------|
| `archetypes/builders/{kind}-builder/*.md` | `bld_{iso}_{kind}.md` | Shared factory ISOs |
| `P{nn}_*/_schema.yaml` | `_schema.yaml` (fixed) | Root pillar schema |
| `P01_knowledge/library/kind/kc_*.md` | `kc_{kind}.md` | Canonical kind KCs |
| `N0x/rules/*.md` | Free-form | Meta docs, not artifacts |
| `N0x/compiled/*.yaml` | `{stem}.yaml` | Build outputs |
| `N00_genesis/P{nn}_*/kind_{kind}/*.md` | `kind_manifest_n00.md` | Archetype templates |
| `_docs/specs/*.md` | `spec_{name}_v{n}.md` | Spec documents |
| `_tools/*.py` | `cex_{name}.py` | Tool scripts |

## Pillar-to-Prefix Map

| Pillar | Directory | Prefix | Dominant kinds |
|--------|-----------|--------|---------------|
| P01 | P01_knowledge | `p01_` | knowledge_card, chunk_strategy, rag_source |
| P02 | P02_model | `p02_` | agent, nucleus_def, model_provider |
| P03 | P03_prompt | `p03_` | prompt_template, system_prompt, chain |
| P04 | P04_tools | `p04_` | cli_tool, browser_tool, mcp_server |
| P05 | P05_output | `p05_` | formatter, parser, naming_rule |
| P06 | P06_schema | `p06_` | input_schema, validator, interface |
| P07 | P07_evals | `p07_` | golden_test, scoring_rubric, benchmark |
| P08 | P08_architecture | `p08_` | diagram, decision_record, component_map |
| P09 | P09_config | `p09_` | env_config, feature_flag, path_config |
| P10 | P10_memory | `p10_` | entity_memory, knowledge_index, memory_scope |
| P11 | P11_feedback | `p11_` | quality_gate, guardrail, bugloop |
| P12 | P12_orchestration | `p12_` | workflow, schedule, dispatch_rule |

## Segment Rules

### Pillar prefix (`p{nn}`)
- Always 2-digit: `p01` not `p1`
- Matches the P-numbered directory containing the file
- Must agree with frontmatter `pillar:` field

### Kind segment (`{kind}`)
- Use the full kind name from `.cex/kinds_meta.json`
- Snake_case: `knowledge_card` not `KnowledgeCard` or `knowledge-card`
- Multi-word kinds keep their underscores: `env_config`, `quality_gate`

### Descriptor segment (`{descriptor}`)
- Short contextual label distinguishing this artifact from others of the same kind
- Snake_case, max 25 characters
- NOT a version number (version goes in frontmatter only)
- NOT redundant with the kind: prefer `intelligence` over `agent_intelligence`
  (kind already says `agent`, so `intelligence` is the descriptor, not `agent_intelligence`)
- Collision resolution: append `_2`, `_3` before adding a date segment

### Nucleus suffix (`{nxx}`)
- `n00` = genesis/template (N00_genesis only)
- `n01`-`n07` = operational nuclei
- Matches the N-numbered directory containing the file

### Extension
- `.md` for human-readable documents (knowledge cards, context docs, prompts)
- `.yaml` for machine-readable configs and schemas

## Legacy Prefix Catalog

Files with these prefixes are WARN-level violations. Migrate gradually:

| Legacy prefix | New convention | Example migration |
|--------------|----------------|------------------|
| `kc_` | `p{nn}_knowledge_card_{desc}_{nxx}.md` | `kc_tool_shed.md` -> `p04_knowledge_card_tool_shed_n01.md` |
| `sch_` | `p06_input_schema_{desc}_{nxx}.yaml` | `sch_quality_audit.yaml` -> `p06_input_schema_quality_audit_n05.yaml` |
| `age_` | `p02_agent_{desc}_{nxx}.md` | `age_scout.md` -> `p02_agent_scout_n01.md` |
| `con_` | `p{nn}_{kind}_{desc}_{nxx}.md` | context-dependent |
| `mem_` | `p10_{kind}_{desc}_{nxx}.md` | `mem_entity_scout.md` -> `p10_entity_memory_scout_n04.md` |
| `pro_` | `p03_{kind}_{desc}_{nxx}.md` | prompt-related |
| `tpl_` | `p{nn}_{kind}_{desc}_{nxx}.md` | template files |
| `ex_` | `p{nn}_{kind}_{desc}_{nxx}.md` | example files |
| `atom_` | `p01_knowledge_card_{desc}_{nxx}.md` | N01 atlas atoms |
| `bld_` | unchanged -- builder ISOs are exempt | `bld_manifest_agent.md` stays |

## Migration Strategy

**Phase 1 (NOW): Going forward** -- all NEW artifacts use the canonical convention.
**Phase 2 (GRADUAL): Existing files** -- migrate with `cex_naming_validator.py --fix`.
**Phase 3 (NEVER broken): Build tools** -- warn on WARN/FAIL, never block on legacy names.

### Migration checklist for each file

1. `git mv <old_name> <new_name>` (preserves git history)
2. Update `id:` in frontmatter to match new stem
3. Grep for old name references: `grep -r "<old_name>" . --include="*.md" -l`
4. Update all references in CLAUDE.md, handoffs, and other artifacts
5. Run `python _tools/cex_naming_validator.py --check <nucleus>/` to confirm

## Enforcement

| Layer | Tool | Mode |
|-------|------|------|
| Developer check | `cex_naming_validator.py --check` | Report [OK]/[WARN]/[FAIL] |
| CI gate | `cex_naming_validator.py --check --summary` | Exit 1 if FAIL count > 0 |
| Pre-commit hook | `cex_hooks.py pre-commit` | Warn only (non-blocking) |
| Build pipeline | 8F F7 GOVERN | Log but do not fail |
| Migration | `cex_naming_validator.py --fix` | Suggest; `--confirm` to apply |

## Relation to kinds_meta.json

`kinds_meta.json` defines the abbreviated naming patterns used by legacy builders
(e.g., `p11_abt_{{name}}.yaml` for `ab_test_config`). Those patterns coexist during
the migration period. The canonical convention uses the FULL kind name, not the
abbreviated code. When both exist, the full-kind-name form is preferred for new files.

| kinds_meta pattern | Full-kind-name pattern | Preferred |
|-------------------|----------------------|-----------|
| `p11_abt_{{name}}.yaml` | `p11_ab_test_config_{desc}_{nxx}.yaml` | Full (new files) |
| `p04_act_{{name}}.md` | `p04_action_paradigm_{desc}_{nxx}.md` | Full (new files) |
| `p02_agt_{{name}}.md` | `p02_agent_{desc}_{nxx}.md` | Full (new files) |

## Quality Gate

A `naming_rule` artifact is GOOD when:
- scope is explicit (which artifact type, which directory)
- pattern is machine-checkable (regex present)
- positive + negative examples both present
- validator tool linked

This spec satisfies all four criteria:
- Scope: N0x/P{nn}/ directories, .md and .yaml only
- Pattern: `^p\d{2}_[a-z][a-z0-9_]+_[a-z][a-z0-9_]*_n\d{2}\.(md|yaml)$`
- Positive examples: table above
- Validator: `_tools/cex_naming_validator.py`

## Done When

- [ ] `cex_naming_validator.py --check --summary` reports 0 [FAIL]
- [ ] All new N03 artifacts in this session use canonical names
- [ ] Frontmatter `id:` matches stem of filename for all new files
- [ ] CONTRIBUTING.md references this spec in naming section
