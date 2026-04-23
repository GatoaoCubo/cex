---
id: spec_iso_12p
kind: decision_record
pillar: P08
nucleus: N07
status: accepted
date: "2026-04-19"
title: "ISO 12-Pillar Architecture: Builder ISOs mapped 1:1 to CEX Pillars"
quality: 8.3
density_score: 1.0
updated: "2026-04-22"
---

# ISO 12-Pillar Architecture

## Status

Accepted. Migration: in-progress.

## Context

CEX builders use 13 ISOs (Instruction Set Objects) per kind. The 13 ISOs do NOT
map to the 12 pillars — P03 has 2 ISOs (system_prompt + instruction), P07 has 2
(quality_gate + examples), and P11 has 0. This breaks the fractal CoC pattern
that governs every other layer of CEX.

| Layer | Structure | Fractal? |
|-------|-----------|----------|
| Repo | 12 pillar dirs per nucleus | Yes |
| Nucleus | 12 pillar subdirs | Yes |
| Builder | 13 ISOs | **No — mismatch** |

## Decision

Map builder ISOs 1:1 to pillars. 12 ISOs, function-named (not pillar-numbered),
with shared defaults and kind-specific overrides.

## Migration Map

| Pillar | Old ISO(s) | New ISO | Operation |
|--------|-----------|---------|-----------|
| P01 Knowledge | `bld_knowledge_card` | `bld_knowledge` | RENAME |
| P02 Model | `bld_manifest` + `bld_system_prompt` | `bld_model` | MERGE |
| P03 Prompt | `bld_instruction` | `bld_prompt` | RENAME |
| P04 Tools | `bld_tools` | `bld_tools` | UNCHANGED |
| P05 Output | `bld_output_template` | `bld_output` | RENAME |
| P06 Schema | `bld_schema` | `bld_schema` | UNCHANGED |
| P07 Eval | `bld_quality_gate` + `bld_examples` | `bld_eval` | MERGE |
| P08 Architecture | `bld_architecture` | `bld_architecture` | UNCHANGED |
| P09 Config | `bld_config` | `bld_config` | UNCHANGED |
| P10 Memory | `bld_memory` | `bld_memory` | UNCHANGED |
| P11 Feedback | *(missing)* | `bld_feedback` | NEW |
| P12 Orchestration | `bld_collaboration` | `bld_orchestration` | RENAME |

**Net: 4 renames, 2 merges, 1 new, 5 unchanged = 13 old -> 12 new.**

## Merge Rules

### P02: bld_manifest + bld_system_prompt -> bld_model

```
---
# frontmatter: union of both, manifest fields take priority
# body: manifest metadata section + system_prompt persona section
---

## Identity (from bld_manifest)
{manifest body}

## Persona (from bld_system_prompt)
{system_prompt body}
```

### P07: bld_quality_gate + bld_examples -> bld_eval

```
---
# frontmatter: union of both, quality_gate fields take priority
---

## Quality Gate (from bld_quality_gate)
{quality_gate body}

## Examples (from bld_examples)
{examples body}
```

## Shared Defaults (inheritance by convention)

```
archetypes/builders/_shared/
  bld_tools_default.md       # P04: Read,Write,Edit,Bash,Glob,Grep (universal)
  bld_eval_default.md        # P07: universal quality gates (H01-H07)
  bld_config_default.md      # P09: standard tunables
  bld_memory_default.md      # P10: default learning schema
  bld_feedback_default.md    # P11: common anti-patterns
  bld_orchestration_default.md # P12: standard signal protocol
  bld_architecture_default.md  # P08: default component map
```

**Load order** (cex_skill_loader.py source priority, unchanged):
1. `_shared/bld_{pillar}_default.md` (priority=1)
2. `{kind}-builder/bld_{pillar}_{kind}.md` (priority=2, overrides shared)
3. Nucleus override (priority=3)
4. Brand override (priority=4)

Simple builders override 4-5 ISOs. Complex builders override all 12.
Contributor writes ONLY the overrides — shared defaults cover the rest.

## Tooling Updates Required

| File | Change |
|------|--------|
| `_tools/cex_skill_loader.py` | Update ISO_PATTERNS (12 items), STAGE_ISO_MAP, F_STAGE_ALIASES |
| `_tools/cex_doctor.py` | Update ISO count check (13->12), instruction->prompt size limit |
| `cex_sdk/agent/context_loader.py` | Update bld_instruction -> bld_prompt, bld_examples -> bld_eval |
| `_tools/cex_materialize.py` | Update ISO name references in docs |
| `_tools/cex_prompt_cache.py` | Uses glob("bld_*.md") — no change needed |
| `_tools/cex_wave_validator.py` | Uses glob — no change needed |
| `CONTRIBUTING.md` | Update ISO table (13->12, new names) |
| `.claude/rules/8f-reasoning.md` | Update F2 BECOME references |
| `CLAUDE.md` | Update ISO count |

## File Count Impact

| Metric | Before | After |
|--------|--------|-------|
| ISOs per builder | 13 | 12 (or fewer with shared inheritance) |
| Total ISO files | 3,809 | ~3,500 (295 x 12 minus shared inheritance) |
| Shared defaults | 3 skills | 7 defaults + 3 skills |
| Min files for new builder | 13 | 4-5 (rest inherited from _shared) |
| Contributor friction | High (2-4h) | Low (30-60min for simple kinds) |

## CoC Fractal Proof

After migration, the same 12-pillar structure appears at every scale:

```
CEX repo         -> 12 pillar dirs (P01-P12)
  Nucleus N03    -> 12 pillar subdirs
    Builder      -> 12 ISOs (bld_knowledge..bld_orchestration)
      ISO        -> maps to 8F function (F1-F8)
        Artifact -> lands in pillar dir
```

A builder IS a nucleus compressed to 12 files.
A nucleus IS a builder expanded to a directory tree.
Same fractal. Same convention. Zero configuration.

## Consequences

- **Positive**: Perfect CoC alignment, lower contributor barrier, batch-editable shared defaults
- **Positive**: P11 gap filled — builders finally have formal anti-pattern documentation
- **Negative**: One-time migration of 3,800+ files (automated via script)
- **Negative**: Any external tooling referencing old ISO names breaks (migration script updates all known refs)
- **Risk**: Merge quality (manifest+system_prompt content may need manual review for top-10 builders)
