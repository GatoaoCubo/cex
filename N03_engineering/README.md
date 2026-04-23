# N03 Engineering -- Fractal Module

> Inventive Pride -- artifact construction

Contains instances of all 12 pillars scoped to artifact construction. Each pillar
subdir holds typed artifacts filtered through this nucleus's sin lens.

## Structure (mirrors 12 pillars)

| Subdir | Pillar | Function | Contents |
|--------|--------|----------|----------|
| knowledge/ | [[P01_knowledge]] | INJECT | Knowledge cards for artifact construction |
| agents/ | [[P02_model]] | BECOME | Agents specialized in artifact construction |
| prompts/ | [[P03_prompt]] | REASON | Prompt templates for artifact construction |
| tools/ | [[P04_tools]] | CALL | Skills/tools for artifact construction |
| output/ | [[P05_output]] | PRODUCE | Output formats for artifact construction |
| schemas/ | [[P06_schema]] | CONSTRAIN | Validation rules for artifact construction |
| quality/ | [[P07_evals]] | GOVERN | Quality gates for artifact construction |
| architecture/ | [[P08_architecture]] | GOVERN | Component maps for artifact construction |
| config/ | [[P09_config]] | GOVERN | Configs for artifact construction |
| memory/ | [[P10_memory]] | INJECT | Learning records for artifact construction |
| feedback/ | [[P11_feedback]] | GOVERN | User corrections for artifact construction |
| orchestration/ | [[P12_orchestration]] | COLLABORATE | Routing rules for artifact construction |

## Auxiliary

| Subdir | Purpose |
|--------|---------|
| rules/ | Nucleus-scoped rules (loaded at boot) |
| compiled/ | Auto-generated YAML from .md (do not edit) |

## Conventions

- Every file has YAML frontmatter (`id`, `kind`, `pillar`, `quality: null`).
- Kinds are variable; pillar subdirs are fixed.
- Reading any file's path reveals its pillar: `N03_*/{pillar}/{kind}_*.md`.
- Cross-nucleus siblings: same pillar in other nuclei lives at `../N0X_*/{pillar}/`.

## See also

- Nucleus definition: `architecture/nucleus_def_n03.md`
- Nucleus rules: `rules/` (or `.claude/rules/n07-*.md` for N07)
- Canonical pillar specs: `../P01_*/` through `../P12_*/`
