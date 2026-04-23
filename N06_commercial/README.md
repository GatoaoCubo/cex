# N06 Commercial -- Fractal Module

> Strategic Greed -- commercial and monetization

Contains instances of all 12 pillars scoped to commercial and monetization. Each pillar
subdir holds typed artifacts filtered through this nucleus's sin lens.

## Structure (mirrors 12 pillars)

| Subdir | Pillar | Function | Contents |
|--------|--------|----------|----------|
| knowledge/ | [[P01_knowledge]] | INJECT | Knowledge cards for commercial and monetization |
| agents/ | [[P02_model]] | BECOME | Agents specialized in commercial and monetization |
| prompts/ | [[P03_prompt]] | REASON | Prompt templates for commercial and monetization |
| tools/ | [[P04_tools]] | CALL | Skills/tools for commercial and monetization |
| output/ | [[P05_output]] | PRODUCE | Output formats for commercial and monetization |
| schemas/ | [[P06_schema]] | CONSTRAIN | Validation rules for commercial and monetization |
| quality/ | [[P07_evals]] | GOVERN | Quality gates for commercial and monetization |
| architecture/ | [[P08_architecture]] | GOVERN | Component maps for commercial and monetization |
| config/ | [[P09_config]] | GOVERN | Configs for commercial and monetization |
| memory/ | [[P10_memory]] | INJECT | Learning records for commercial and monetization |
| feedback/ | [[P11_feedback]] | GOVERN | User corrections for commercial and monetization |
| orchestration/ | [[P12_orchestration]] | COLLABORATE | Routing rules for commercial and monetization |

## Auxiliary

| Subdir | Purpose |
|--------|---------|
| rules/ | Nucleus-scoped rules (loaded at boot) |
| compiled/ | Auto-generated YAML from .md (do not edit) |

## Conventions

- Every file has YAML frontmatter (`id`, `kind`, `pillar`, `quality: null`).
- Kinds are variable; pillar subdirs are fixed.
- Reading any file's path reveals its pillar: `N06_*/{pillar}/{kind}_*.md`.
- Cross-nucleus siblings: same pillar in other nuclei lives at `../N0X_*/{pillar}/`.

## See also

- Nucleus definition: `architecture/nucleus_def_n06.md`
- Nucleus rules: `rules/` (or `.claude/rules/n07-*.md` for N07)
- Canonical pillar specs: `../P01_*/` through `../P12_*/`
