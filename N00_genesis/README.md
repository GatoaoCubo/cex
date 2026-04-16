# N00 Genesis -- Fractal Module

> pre-sin archetype -- template for all nuclei

Contains instances of all 12 pillars scoped to template for all nuclei. Each pillar
subdir holds typed artifacts filtered through this nucleus's sin lens.

## Structure (mirrors 12 pillars)

| Subdir | Pillar | Function | Contents |
|--------|--------|----------|----------|
| knowledge/ | [[P01_knowledge]] | INJECT | Knowledge cards for template for all nuclei |
| agents/ | [[P02_model]] | BECOME | Agents specialized in template for all nuclei |
| prompts/ | [[P03_prompt]] | REASON | Prompt templates for template for all nuclei |
| tools/ | [[P04_tools]] | CALL | Skills/tools for template for all nuclei |
| output/ | [[P05_output]] | PRODUCE | Output formats for template for all nuclei |
| schemas/ | [[P06_schema]] | CONSTRAIN | Validation rules for template for all nuclei |
| quality/ | [[P07_evals]] | GOVERN | Quality gates for template for all nuclei |
| architecture/ | [[P08_architecture]] | GOVERN | Component maps for template for all nuclei |
| config/ | [[P09_config]] | GOVERN | Configs for template for all nuclei |
| memory/ | [[P10_memory]] | INJECT | Learning records for template for all nuclei |
| feedback/ | [[P11_feedback]] | GOVERN | User corrections for template for all nuclei |
| orchestration/ | [[P12_orchestration]] | COLLABORATE | Routing rules for template for all nuclei |

## Auxiliary

| Subdir | Purpose |
|--------|---------|
| rules/ | Nucleus-scoped rules (loaded at boot) |
| compiled/ | Auto-generated YAML from .md (do not edit) |

## Conventions

- Every file has YAML frontmatter (`id`, `kind`, `pillar`, `quality: null`).
- Kinds are variable; pillar subdirs are fixed.
- Reading any file's path reveals its pillar: `N00_*/{pillar}/{kind}_*.md`.
- Cross-nucleus siblings: same pillar in other nuclei lives at `../N0X_*/{pillar}/`.

## See also

- Nucleus definition: `architecture/nucleus_def_n00.md`
- Nucleus rules: `rules/` (or `.claude/rules/n07-*.md` for N07)
- Canonical pillar specs: `../P01_*/` through `../P12_*/`
