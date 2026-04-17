# N04 Knowledge -- Fractal Module

> Knowledge Gluttony -- knowledge management and RAG

Contains instances of all 12 pillars scoped to knowledge management and RAG. Each pillar
subdir holds typed artifacts filtered through this nucleus's sin lens.

## Structure (mirrors 12 pillars)

| Subdir | Pillar | Function | Contents |
|--------|--------|----------|----------|
| knowledge/ | [[P01_knowledge]] | INJECT | Knowledge cards for knowledge management and RAG |
| agents/ | [[P02_model]] | BECOME | Agents specialized in knowledge management and RAG |
| prompts/ | [[P03_prompt]] | REASON | Prompt templates for knowledge management and RAG |
| tools/ | [[P04_tools]] | CALL | Skills/tools for knowledge management and RAG |
| output/ | [[P05_output]] | PRODUCE | Output formats for knowledge management and RAG |
| schemas/ | [[P06_schema]] | CONSTRAIN | Validation rules for knowledge management and RAG |
| quality/ | [[P07_evals]] | GOVERN | Quality gates for knowledge management and RAG |
| architecture/ | [[P08_architecture]] | GOVERN | Component maps for knowledge management and RAG |
| config/ | [[P09_config]] | GOVERN | Configs for knowledge management and RAG |
| memory/ | [[P10_memory]] | INJECT | Learning records for knowledge management and RAG |
| feedback/ | [[P11_feedback]] | GOVERN | User corrections for knowledge management and RAG |
| orchestration/ | [[P12_orchestration]] | COLLABORATE | Routing rules for knowledge management and RAG |

## Auxiliary

| Subdir | Purpose |
|--------|---------|
| rules/ | Nucleus-scoped rules (loaded at boot) |
| compiled/ | Auto-generated YAML from .md (do not edit) |

## Conventions

- Every file has YAML frontmatter (`id`, `kind`, `pillar`, `quality: null`).
- Kinds are variable; pillar subdirs are fixed.
- Reading any file's path reveals its pillar: `N04_*/{pillar}/{kind}_*.md`.
- Cross-nucleus siblings: same pillar in other nuclei lives at `../N0X_*/{pillar}/`.

## See also

- Nucleus definition: `architecture/nucleus_def_n04.md`
- Nucleus rules: `rules/` (or `.claude/rules/n07-*.md` for N07)
- Canonical pillar specs: `../P01_*/` through `../P12_*/`
