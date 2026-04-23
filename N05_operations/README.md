# N05 Operations -- Fractal Module

> Gating Wrath -- operations and deployment

Contains instances of all 12 pillars scoped to operations and deployment. Each pillar
subdir holds typed artifacts filtered through this nucleus's sin lens.

## Structure (mirrors 12 pillars)

| Subdir | Pillar | Function | Contents |
|--------|--------|----------|----------|
| knowledge/ | [[P01_knowledge]] | INJECT | Knowledge cards for operations and deployment |
| agents/ | [[P02_model]] | BECOME | Agents specialized in operations and deployment |
| prompts/ | [[P03_prompt]] | REASON | Prompt templates for operations and deployment |
| tools/ | [[P04_tools]] | CALL | Skills/tools for operations and deployment |
| output/ | [[P05_output]] | PRODUCE | Output formats for operations and deployment |
| schemas/ | [[P06_schema]] | CONSTRAIN | Validation rules for operations and deployment |
| quality/ | [[P07_evals]] | GOVERN | Quality gates for operations and deployment |
| architecture/ | [[P08_architecture]] | GOVERN | Component maps for operations and deployment |
| config/ | [[P09_config]] | GOVERN | Configs for operations and deployment |
| memory/ | [[P10_memory]] | INJECT | Learning records for operations and deployment |
| feedback/ | [[P11_feedback]] | GOVERN | User corrections for operations and deployment |
| orchestration/ | [[P12_orchestration]] | COLLABORATE | Routing rules for operations and deployment |

## Auxiliary

| Subdir | Purpose |
|--------|---------|
| rules/ | Nucleus-scoped rules (loaded at boot) |
| compiled/ | Auto-generated YAML from .md (do not edit) |

## Conventions

- Every file has YAML frontmatter (`id`, `kind`, `pillar`, `quality: null`).
- Kinds are variable; pillar subdirs are fixed.
- Reading any file's path reveals its pillar: `N05_*/{pillar}/{kind}_*.md`.
- Cross-nucleus siblings: same pillar in other nuclei lives at `../N0X_*/{pillar}/`.

## See also

- Nucleus definition: `architecture/nucleus_def_n05.md`
- Nucleus rules: `rules/` (or `.claude/rules/n07-*.md` for N07)
- Canonical pillar specs: `../P01_*/` through `../P12_*/`
