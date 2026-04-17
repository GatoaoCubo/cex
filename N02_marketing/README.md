# N02 Marketing -- Fractal Module

> Creative Lust -- marketing and copywriting

Contains instances of all 12 pillars scoped to marketing and copywriting. Each pillar
subdir holds typed artifacts filtered through this nucleus's sin lens.

## Structure (mirrors 12 pillars)

| Subdir | Pillar | Function | Contents |
|--------|--------|----------|----------|
| knowledge/ | [[P01_knowledge]] | INJECT | Knowledge cards for marketing and copywriting |
| agents/ | [[P02_model]] | BECOME | Agents specialized in marketing and copywriting |
| prompts/ | [[P03_prompt]] | REASON | Prompt templates for marketing and copywriting |
| tools/ | [[P04_tools]] | CALL | Skills/tools for marketing and copywriting |
| output/ | [[P05_output]] | PRODUCE | Output formats for marketing and copywriting |
| schemas/ | [[P06_schema]] | CONSTRAIN | Validation rules for marketing and copywriting |
| quality/ | [[P07_evals]] | GOVERN | Quality gates for marketing and copywriting |
| architecture/ | [[P08_architecture]] | GOVERN | Component maps for marketing and copywriting |
| config/ | [[P09_config]] | GOVERN | Configs for marketing and copywriting |
| memory/ | [[P10_memory]] | INJECT | Learning records for marketing and copywriting |
| feedback/ | [[P11_feedback]] | GOVERN | User corrections for marketing and copywriting |
| orchestration/ | [[P12_orchestration]] | COLLABORATE | Routing rules for marketing and copywriting |

## Auxiliary

| Subdir | Purpose |
|--------|---------|
| rules/ | Nucleus-scoped rules (loaded at boot) |
| compiled/ | Auto-generated YAML from .md (do not edit) |

## Conventions

- Every file has YAML frontmatter (`id`, `kind`, `pillar`, `quality: null`).
- Kinds are variable; pillar subdirs are fixed.
- Reading any file's path reveals its pillar: `N02_*/{pillar}/{kind}_*.md`.
- Cross-nucleus siblings: same pillar in other nuclei lives at `../N0X_*/{pillar}/`.

## See also

- Nucleus definition: `architecture/nucleus_def_n02.md`
- Nucleus rules: `rules/` (or `.claude/rules/n07-*.md` for N07)
- Canonical pillar specs: `../P01_*/` through `../P12_*/`
