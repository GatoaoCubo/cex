---
quality: 8.7
id: spec_structural_alignment_v1
kind: constraint_spec
pillar: P06
title: "Spec -- CEX Repo Structural Alignment v1"
version: 1.0.0
created: 2026-04-17
author: n07_orchestrator
domain: CEX system architecture
quality_target: 9.0
status: DONE
scope: N00-N07 + archetypes + tools + commands
depends_on: null
tags: [spec, structural, alignment, naming, refactor, mentor, pillars]
tldr: "Rename N00-N07 semantic subdirs to P-numbered pillars, build N00 canonical archetype, add /mentor command."
density_score: 0.95
---

<!-- 8F: F1=constraint_spec P06 F2=spec-builder F3=README+explore+kinds_meta F4=autonomous F5=dir_scan F6=write F7=9.0 F8=save -->

## Problem

CEX describes an architecture of 8 nuclei x 12 pillars x 300 kinds -- but the file system
does not reflect this structure. Each nucleus uses semantically-named subdirs (`knowledge/`,
`agents/`, `prompts/`) instead of pillar-numbered dirs (`P01_knowledge/`, `P02_model/`,
`P03_prompt/`). N00 lacks the canonical kind-template subfolders that make it a true archetype.
No `/mentor` entry point exists for the universal LLM vocabulary.

**3 consequences:**
1. LLM navigation requires opening files to understand context -- filenames don't encode pillar/kind
2. N00 is a skeleton, not a template -- no kind subfolders with open variables
3. No discoverable entry point for the 8F x 12P x 257K vocabulary

## Vision

```
N00_genesis/                         ARCHETYPE: 12 pillar dirs x kind subfolders
  P01_knowledge/
    kind_knowledge_card/              3 files: manifest + template + example
    kind_rag_source/
    kind_glossary_entry/
    ...  (28 P01 kinds)
  P02_model/
    kind_agent/
    kind_nucleus_def/
    ...  (22 P02 kinds)
  P03_prompt/ ... P12_orchestration/  (P03-P12 same pattern)
  rules/                              unchanged (meta, not a pillar)
  compiled/                           unchanged (build output)

N01_intelligence/                    INSTANCE: 12 P-numbered subdirs
  P01_knowledge/                      was: knowledge/
  P02_model/                          was: agents/
  P03_prompt/                         was: prompts/
  P04_tools/                          was: tools/
  P05_output/                         was: output/
  P06_schema/                         was: schemas/
  P07_evals/                          was: quality/
  P08_architecture/                   was: architecture/
  P09_config/                         was: config/
  P10_memory/                         was: memory/
  P11_feedback/                       was: feedback/
  P12_orchestration/                  was: orchestration/
  rules/                              unchanged
  compiled/                           unchanged

N02-N07: identical structure
```

### File Naming Convention (enforced going forward)

```
{pxx}_{kind}_{descriptor}_{nxx}.md
```

| Segment | Rule | Example |
|---------|------|---------|
| pxx | 3-char pillar code | p01, p02, p09 |
| kind | kind name snake_case | knowledge_card, agent, env_config |
| descriptor | short contextual name | competitor_analysis, intelligence |
| nxx | nucleus code | n01, n07, n00 (template) |

**Examples in context:**
- `N01/P01_knowledge/p01_knowledge_card_competitor_analysis_n01.md`
- `N01/P02_model/p02_agent_intelligence_n01.md`
- `N07/P06_schema/p06_validator_precommit_n07.md`
- `N07/P09_config/p09_env_config_n07.md`
- `N00/P02_model/kind_nucleus_def/p02_nucleus_def_template_n00.md`

**Legacy files** (kc_, age_, sch_, con_, mem_, pro_ prefixes): flag on validate, do not
break on build. Migrate gradually via `cex_naming_validator.py --fix`.

**Unchanged**: `bld_*` ISOs in `archetypes/builders/` (already correct, shared factory).

## Decisions (autonomous -- structural, not subjective)

| Decision | Choice | Reason |
|----------|--------|--------|
| archetypes/builders/ location | UNCHANGED | Shared factory; not nucleus-specific |
| Root P01-P12 dirs | UNCHANGED | Shared pillar schemas/templates; different layer |
| rules/ and compiled/ per nucleus | UNCHANGED | Meta dirs, not pillar artifacts |
| File rename strategy | GOING FORWARD + gradual migration | Mass rename breaks 500+ refs at once |
| N00 kind depth | kind_manifest.md only (not full template set) | 257 x 12 ISOs already in archetypes/ |
| /mentor implementation | New skill + N00 context loader | Reuses N00 knowledge, no duplication |
| Wave order | Tools first, then migration, then refs, then content | Dependency chain: tool before use |

## Pillar Mapping (current subdir -> new subdir)

| Current | Pillar | New | Kind count |
|---------|--------|-----|-----------|
| `knowledge/` | P01 | `P01_knowledge/` | 28 |
| `agents/` | P02 | `P02_model/` | 22 |
| `prompts/` | P03 | `P03_prompt/` | 20 |
| `tools/` | P04 | `P04_tools/` | 34 |
| `output/` | P05 | `P05_output/` | 23 |
| `schemas/` | P06 | `P06_schema/` | 8 |
| `quality/` | P07 | `P07_evals/` | 23 |
| `architecture/` | P08 | `P08_architecture/` | 12 |
| `config/` | P09 | `P09_config/` | 28 |
| `memory/` | P10 | `P10_memory/` | 18 |
| `feedback/` | P11 | `P11_feedback/` | 26 |
| `orchestration/` | P12 | `P12_orchestration/` | 15 |

Total: 8 nuclei x 12 renames = **96 git mv operations**

## Artifacts

### Wave 1: Migration Tooling (2 files -- N05)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | `_tools/cex_repo_align.py` | cli_tool | 6KB | Validates actual structure vs canonical; reports all gaps |
| CREATE | `_tools/cex_migrate_paths.py` | cli_tool | 8KB | Executes 96 git mv + updates refs in tools/CLAUDE.md/handoffs |

**cex_repo_align.py behavior:**
- Scans N00-N07 for semantic subdir names
- Reports: `[WRONG] N01/P01_knowledge/ should be P01_knowledge/`
- Reports: `[MISSING] N01/P04_tools/ not found`
- Exit 0 = clean, exit 1 = gaps found

**cex_migrate_paths.py behavior:**
- `--dry-run`: list all 96 git mv operations without executing
- `--execute`: run all git mv operations
- `--update-refs`: grep+sed pass on tools/, boot/, CLAUDE.md for old subdir names
- `--update-handoffs`: update paths in .cex/runtime/handoffs/*.md
- ASCII-only output (no emoji)

### Wave 2: Directory Migration (96 git mv -- N05 executes via script)

For each nucleus N00-N07:

```bash
# Pattern repeated for each of 8 nuclei x 12 dirs
git mv N0x_*/knowledge    N0x_*/P01_knowledge
git mv N0x_*/agents       N0x_*/P02_model
git mv N0x_*/prompts      N0x_*/P03_prompt
git mv N0x_*/tools        N0x_*/P04_tools
git mv N0x_*/output       N0x_*/P05_output
git mv N0x_*/schemas      N0x_*/P06_schema
git mv N0x_*/quality      N0x_*/P07_evals
git mv N0x_*/architecture N0x_*/P08_architecture
git mv N0x_*/config       N0x_*/P09_config
git mv N0x_*/memory       N0x_*/P10_memory
git mv N0x_*/feedback     N0x_*/P11_feedback
git mv N0x_*/orchestration N0x_*/P12_orchestration
```

**Note**: If a subdir doesn't exist in a nucleus (e.g. N07 has no `tools/`), skip silently.
`rules/` and `compiled/` are NOT renamed.

### Wave 3: Reference Updates (~40 files -- N05 + N07)

**Tools with hardcoded subdir names (N05 grep+sed pass):**

| Action | Path | Notes |
|--------|------|-------|
| REWRITE | `_tools/cex_doctor.py` | Update expected dir names in health check |
| REWRITE | `_tools/cex_flywheel_audit.py` | Update 109 check paths |
| REWRITE | `_tools/cex_hooks.py` | Update validation expected dirs |
| REWRITE | `_tools/cex_score.py` | Update artifact scan paths |
| REWRITE | `_tools/cex_materialize.py` | Update nucleus dir scanning |
| REWRITE | `_tools/cex_hygiene.py` | Update expected structure |
| REWRITE | `_tools/cex_retriever.py` | Update document scan paths |
| REWRITE | `_tools/cex_mission_runner.py` | Update nucleus dir refs |
| REWRITE | `_tools/cex_8f_runner.py` | Update output path resolution |
| REWRITE | `_tools/cex_crew_runner.py` | Update nucleus artifact discovery |
| REWRITE | `_tools/cex_query.py` | Update TF-IDF scan dirs |

**Boot scripts (N05):**

| Action | Path | Notes |
|--------|------|-------|
| REWRITE | `boot/n01.ps1` | Scan for hardcoded subdir refs |
| REWRITE | `boot/n02.ps1` | Same |
| REWRITE | `boot/n03.ps1` | Same |
| REWRITE | `boot/n04.ps1` | Same |
| REWRITE | `boot/n05.ps1` | Same |
| REWRITE | `boot/n06.ps1` | Same |
| REWRITE | `boot/n07.ps1` | Same |

**CLAUDE.md (N07):**

| Action | Path | Notes |
|--------|------|-------|
| REWRITE | `CLAUDE.md` | Update Pointers table + all path refs; add naming convention entry |

**FRACTAL_FILL handoffs (N07 -- must happen before W3 grid fires):**

| Action | Path | Notes |
|--------|------|-------|
| REWRITE (7) | `.cex/runtime/handoffs/FRACTAL_FILL_W3_n0*.md` | Update deliverable paths to P-numbered |
| REWRITE (8) | `.cex/runtime/handoffs/FRACTAL_FILL_W4_n0*.md` | Same |
| REWRITE (8) | `.cex/runtime/handoffs/FRACTAL_FILL_W5_n0*.md` | Same |
| REWRITE (8) | `.cex/runtime/handoffs/FRACTAL_FILL_W6_n0*.md` | Same |
| REWRITE | `.cex/runtime/handoffs/HANDOFF_FRACTAL_FILL_RESUME.md` | Update path table |

### Wave 4: N00 Canonical Structure (269 files -- N04)

**12 pillar kind_index files:**

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | `N00_genesis/P01_knowledge/kind_index.md` | knowledge_card | 3KB | Lists all 28 P01 kinds: name + purpose + builder link |
| CREATE | `N00_genesis/P02_model/kind_index.md` | knowledge_card | 3KB | Lists all 22 P02 kinds |
| CREATE | `N00_genesis/P03_prompt/kind_index.md` | knowledge_card | 3KB | Lists all 20 P03 kinds |
| CREATE | `N00_genesis/P04_tools/kind_index.md` | knowledge_card | 4KB | Lists all 34 P04 kinds |
| CREATE | `N00_genesis/P05_output/kind_index.md` | knowledge_card | 3KB | Lists all 23 P05 kinds |
| CREATE | `N00_genesis/P06_schema/kind_index.md` | knowledge_card | 2KB | Lists all 8 P06 kinds |
| CREATE | `N00_genesis/P07_evals/kind_index.md` | knowledge_card | 3KB | Lists all 23 P07 kinds |
| CREATE | `N00_genesis/P08_architecture/kind_index.md` | knowledge_card | 2KB | Lists all 12 P08 kinds |
| CREATE | `N00_genesis/P09_config/kind_index.md` | knowledge_card | 3KB | Lists all 28 P09 kinds |
| CREATE | `N00_genesis/P10_memory/kind_index.md` | knowledge_card | 2KB | Lists all 18 P10 kinds |
| CREATE | `N00_genesis/P11_feedback/kind_index.md` | knowledge_card | 3KB | Lists all 26 P11 kinds |
| CREATE | `N00_genesis/P12_orchestration/kind_index.md` | knowledge_card | 2KB | Lists all 15 P12 kinds |

**kind_index.md format (per file):**

```markdown
---
id: n00_p{xx}_kind_index
kind: knowledge_card
pillar: P{xx}
nucleus: n00
title: "P{xx} {Name} -- Kind Index"
version: 1.0
quality: 8.3
tags: [index, p{xx}, kinds, archetype]
---

## Purpose
Master index of all kinds in pillar P{xx}. Used by /mentor and by nucleus builders
to discover which kind to use for a given task.

## Kinds

| Kind | Purpose | Builder | Nucleus |
|------|---------|---------|---------|
| knowledge_card | ... | knowledge-card-builder | N01, N04 |
| ...

## Usage
To build any of these: `python _tools/cex_8f_runner.py "intent" --kind {kind} --execute`
```

**257 kind manifest files** (one per kind, organized in kind subfolders):

| Action | Path pattern | Kind | Est. Size | Notes |
|--------|--------------|------|-----------|-------|
| CREATE (257) | `N00_genesis/P{xx}_{name}/kind_{kind}/kind_manifest_n00.md` | knowledge_card | 1KB each | See format below |

**kind_manifest_n00.md format:**

```markdown
---
id: n00_{kind}_manifest
kind: knowledge_card
pillar: P{xx}
nucleus: n00
title: "{Kind} -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, {kind}, p{xx}, archetype, template]
---

## Purpose
{1 sentence description}

## Pillar
P{xx} -- {Pillar Name}

## Schema
{key fields from _schema.yaml}

## When to use
{3 bullet conditions}

## Builder
`archetypes/builders/{kind}-builder/`
Run: `python _tools/cex_8f_runner.py "intent" --kind {kind} --execute`

## Template variables (for nucleus instantiation)
{list of {{VARIABLE}} placeholders from the blank template}

## Example
{1 minimal filled example}

## Related kinds
{2-3 related kinds with why}
```

**2 N00 meta files:**

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | `N00_genesis/n00_README.md` | context_doc | 4KB | How to instantiate a new nucleus from N00 |
| CREATE | `N00_genesis/n00_nucleus_template.md` | nucleus_def | 5KB | Blank nucleus: sin=VARIABLE, role=VARIABLE |

### Wave 5: Naming Convention + /mentor (N03 + N07)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | `.claude/commands/mentor.md` | instruction | 2KB | /mentor skill: boots N00 universal vocabulary |
| CREATE | `.cex/skills/mentor.md` | instruction | 2KB | Cross-runtime mirror |
| CREATE | `N00_genesis/boot/mentor_context.md` | context_doc | 8KB | Pre-compiled: 8F + 12P descriptions + kind summaries |
| CREATE | `_tools/cex_naming_validator.py` | cli_tool | 4KB | Validates pxx_kind_desc_nxx.md convention |
| REWRITE | `CONTRIBUTING.md` | context_doc | +1KB | Add naming convention section |
| CREATE | `_docs/specs/spec_naming_convention_v1.md` | constraint_spec | 3KB | Formal naming spec document |

**mentor_context.md structure:**
- Section 1: 8F pipeline (all 8 functions, N07 examples)
- Section 2: 12 pillar descriptions (purpose + kinds + owners)
- Section 3: 257 kind summaries (name | pillar | 1-line purpose)
- Section 4: Builder structure (12 ISOs, what each does)
- Section 5: Nucleus roles (N00-N07, sin lens, pillar ownership)

**/mentor behavior:**
1. Load `N00_genesis/boot/mentor_context.md`
2. Activate encyclopedic mode: no sin lens, pure taxonomy
3. Answer: "What kind for X?", "Which pillar owns Y?", "Show all P07 kinds"

**cex_naming_validator.py behavior:**
```
python _tools/cex_naming_validator.py --check N01_intelligence/
  [OK]  P01_knowledge/p01_knowledge_card_competitor_n01.md
  [WARN] P02_model/agent_intelligence.md -- legacy name, should be p02_agent_intelligence_n01.md
  [WARN] P06_schema/sch_validator_n01.md -- legacy prefix 'sch_'

python _tools/cex_naming_validator.py --fix N01_intelligence/  # renames + updates refs
```

### Wave 6: Validation + Consolidation (N07)

| Action | Notes |
|--------|-------|
| `python _tools/cex_repo_align.py` | 0 gaps expected |
| `python _tools/cex_doctor.py` | 189+ builders PASS |
| `python _tools/cex_flywheel_audit.py audit` | 100+ of 109 PASS |
| Update `CLAUDE.md` Pointers table | Add /mentor, naming convention, N00 canonical paths |
| git add + commit consolidation | `[N07] spec_structural_alignment: 96 renames + N00 canonical + /mentor` |
| Set spec status: SPEC -> DONE | Edit this file |

## Wave Order and Dependencies

```
Wave 1 (Tools)
     |
     v
Wave 2 (Migration: 96 git mv)
     |
     v
Wave 3 (Ref Updates: tools + CLAUDE.md + handoffs)
     |            |
     v            v
Wave 4 (N00)  Wave 5 (Naming + /mentor)
                  |
                  v
              Wave 6 (Validation)
```

**Critical path**: W1 -> W2 -> W3 -> W6
Wave 3 MUST complete before FRACTAL_FILL W3 fires (handoffs need correct paths).
Wave 4 and 5 can run in parallel after Wave 3.

## Nucleus Assignments

| Wave | Nucleus | Task |
|------|---------|------|
| W1 -- Migration tools | N05 | Build cex_repo_align.py + cex_migrate_paths.py (2 tools) |
| W2 -- Directory migration | N05 | Execute 96 git mv via cex_migrate_paths.py --execute |
| W3 -- Ref updates (tools) | N05 | grep+sed pass on 11 tools + 7 boot scripts |
| W3 -- Ref updates (docs) | N07 | Update CLAUDE.md + 32 FRACTAL_FILL handoffs |
| W4 -- N00 canonical | N04 | 12 kind_index.md + 257 kind_manifest + 2 meta files |
| W5 -- Naming + /mentor | N03 | cex_naming_validator.py + spec_naming_convention.md |
| W5 -- /mentor command | N07 | mentor.md + mentor_context.md |
| W6 -- Validation | N07 | Run tools + consolidate + commit |

## Artifact Count Summary

| Wave | New Files | Modified Files | git mv |
|------|-----------|----------------|--------|
| W1 | 2 | 0 | 0 |
| W2 | 0 | 0 | ~96 |
| W3 | 0 | ~50 | 0 |
| W4 | 271 | 0 | 0 |
| W5 | 6 | 1 | 0 |
| W6 | 0 | 2 | 0 |
| **Total** | **279 new** | **~53 modified** | **~96 renames** |

## Done When

- [ ] `cex_repo_align.py` reports 0 structural gaps
- [ ] All 8 nuclei have P01-P12 subdirs (96 renames complete)
- [ ] `cex_doctor.py` passes 189+ builders
- [ ] `cex_flywheel_audit.py` passes 100+ / 109 checks
- [ ] FRACTAL_FILL W3-W6 handoffs updated with P-numbered paths
- [ ] N00 has 12 kind_index.md + 257 kind_manifest_n00.md + 2 meta files
- [ ] `/mentor` command responds correctly to vocabulary questions
- [ ] `cex_naming_validator.py` exists and validates correctly
- [ ] CLAUDE.md Pointers table updated (new paths + /mentor entry)
- [ ] spec_naming_convention_v1.md exists
- [ ] All tools reference P-numbered subdirs (no semantic names)
- [ ] spec status updated: SPEC -> DONE
