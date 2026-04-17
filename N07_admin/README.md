# N07 Admin -- Fractal Module

> Orchestrating Sloth -- orchestration and dispatch

Contains instances of all 12 pillars scoped to orchestration and dispatch. Each pillar
subdir holds typed artifacts filtered through this nucleus's sin lens.

## Structure (mirrors 12 pillars)

| Subdir | Pillar | Function | Contents |
|--------|--------|----------|----------|
| knowledge/ | [[P01_knowledge]] | INJECT | Knowledge cards for orchestration and dispatch |
| agents/ | [[P02_model]] | BECOME | Agents specialized in orchestration and dispatch |
| prompts/ | [[P03_prompt]] | REASON | Prompt templates for orchestration and dispatch |
| tools/ | [[P04_tools]] | CALL | Skills/tools for orchestration and dispatch |
| output/ | [[P05_output]] | PRODUCE | Output formats for orchestration and dispatch |
| schemas/ | [[P06_schema]] | CONSTRAIN | Validation rules for orchestration and dispatch |
| quality/ | [[P07_evals]] | GOVERN | Quality gates for orchestration and dispatch |
| architecture/ | [[P08_architecture]] | GOVERN | Component maps for orchestration and dispatch |
| config/ | [[P09_config]] | GOVERN | Configs for orchestration and dispatch |
| memory/ | [[P10_memory]] | INJECT | Learning records for orchestration and dispatch |
| feedback/ | [[P11_feedback]] | GOVERN | User corrections for orchestration and dispatch |
| orchestration/ | [[P12_orchestration]] | COLLABORATE | Routing rules for orchestration and dispatch |

## Auxiliary

| Subdir | Purpose |
|--------|---------|
| rules/ | Nucleus-scoped rules (loaded at boot) |
| compiled/ | Auto-generated YAML from .md (do not edit) |

## Conventions

- Every file has YAML frontmatter (`id`, `kind`, `pillar`, `quality: null`).
- Kinds are variable; pillar subdirs are fixed.
- Reading any file's path reveals its pillar: `N07_*/{pillar}/{kind}_*.md`.
- Cross-nucleus siblings: same pillar in other nuclei lives at `../N0X_*/{pillar}/`.

## See also

- Nucleus definition: `architecture/nucleus_def_n07.md`
- Nucleus rules: `rules/` (or `.claude/rules/n07-*.md` for N07)
- Canonical pillar specs: `../P01_*/` through `../P12_*/`
