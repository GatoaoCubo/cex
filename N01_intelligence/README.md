# N01 Intelligence -- Fractal Module

> Analytical Envy -- research and analysis

Contains instances of all 12 pillars scoped to research and analysis. Each pillar
subdir holds typed artifacts filtered through this nucleus's sin lens.

## Structure (mirrors 12 pillars)

| Subdir | Pillar | Function | Contents |
|--------|--------|----------|----------|
| knowledge/ | [[P01_knowledge]] | INJECT | Knowledge cards for research and analysis |
| agents/ | [[P02_model]] | BECOME | Agents specialized in research and analysis |
| prompts/ | [[P03_prompt]] | REASON | Prompt templates for research and analysis |
| tools/ | [[P04_tools]] | CALL | Skills/tools for research and analysis |
| output/ | [[P05_output]] | PRODUCE | Output formats for research and analysis |
| schemas/ | [[P06_schema]] | CONSTRAIN | Validation rules for research and analysis |
| quality/ | [[P07_evals]] | GOVERN | Quality gates for research and analysis |
| architecture/ | [[P08_architecture]] | GOVERN | Component maps for research and analysis |
| config/ | [[P09_config]] | GOVERN | Configs for research and analysis |
| memory/ | [[P10_memory]] | INJECT | Learning records for research and analysis |
| feedback/ | [[P11_feedback]] | GOVERN | User corrections for research and analysis |
| orchestration/ | [[P12_orchestration]] | COLLABORATE | Routing rules for research and analysis |

## Auxiliary

| Subdir | Purpose |
|--------|---------|
| rules/ | Nucleus-scoped rules (loaded at boot) |
| compiled/ | Auto-generated YAML from .md (do not edit) |

## Conventions

- Every file has YAML frontmatter (`id`, `kind`, `pillar`, `quality: null`).
- Kinds are variable; pillar subdirs are fixed.
- Reading any file's path reveals its pillar: `N01_*/{pillar}/{kind}_*.md`.
- Cross-nucleus siblings: same pillar in other nuclei lives at `../N0X_*/{pillar}/`.

## See also

- Nucleus definition: `architecture/nucleus_def_n01.md`
- Nucleus rules: `rules/` (or `.claude/rules/n07-*.md` for N07)
- Canonical pillar specs: `../P01_*/` through `../P12_*/`
