# CEX Index

**Navigation map** | Updated: 2026-03-28 | 69 kinds, 69 builders, 12 pillars

---

## Root Documents

| File | Purpose |
|------|---------|
| CLAUDE.md | LLM entry point — architecture + navigation |
| README.md | Public README — what CEX is, quickstart |
| LLM_PIPELINE.md | 8 Functions (BECOME → COLLABORATE) |
| CEX_ARCHITECTURE_MAP.md | Visual architecture + color hierarchy |
| INDEX.md | This navigation map |
| CHANGELOG.md | Version history |
| CONTRIBUTING.md | Contributor guide |

## Architecture & Specs (_docs/)

| File | Purpose |
|------|---------|
| ARCHITECTURE.md | 5-layer structure, governance rules |
| WHITEPAPER_CEX.md | Full thesis — the SQL analogy |
| MOTOR_8F_SPEC.md | Intent decomposition engine spec |
| CREW_PATTERNS_RESEARCH.md | CrewAI/DSPy/LangGraph patterns |
| SELF_BUILD_PROTOCOL.md | Self-build test metrics + criteria |
| COMPARE_BUILDERS_SPEC.md | Builder comparison algorithm |
| NAMING_CONVENTION.md | File naming rules |
| ISO_PACKAGE_SPEC.md | 13-file builder specification |
| LLM_INSTRUCTIONS.md | System prompt for LLM operators |
| QUICKSTART.md | How to create artifacts |
| ONBOARDING.md | New contributor guide |
| ROADMAP_CONSOLIDATED.md | Waves 6-12 roadmap |

## Governance (archetypes/)

| File | Purpose |
|------|---------|
| CODEX.md | Construction bible — inviolable rules |
| MANDAMENTOS.md | 10 commandments |
| GLOSSARY.md | Term definitions |
| TAXONOMY_LAYERS.yaml | 69 kinds in layers |
| SEED_BANK.yaml | Seed words per kind |
| TYPE_TO_TEMPLATE.yaml | Kind → template mapping |
| META_TEMPLATE.md | Template that generates templates |
| VERSION.yaml | Version metadata |

## 12 Pillars

| Pillar | Name | Kinds | Templates | Examples | Compiled |
|--------|------|:-----:|:---------:|:--------:|:--------:|
| P01 | Knowledge | 6 | 6 | 85 | 84 |
| P02 | Model | 9 | 9 | 16 | 16 |
| P03 | Prompt | 5 | 5 | 17 | 16 |
| P04 | Tools | 9 | 9 | 16 | 16 |
| P05 | Output | 4 | 4 | 5 | 5 |
| P06 | Schema | 5 | 5 | 9 | 7 |
| P07 | Evals | 6 | 6 | 8 | 7 |
| P08 | Architecture | 5 | 5 | 6 | 5 |
| P09 | Config | 5 | 5 | 6 | 6 |
| P10 | Memory | 4 | 4 | 9 | 9 |
| P11 | Feedback | 5 | 5 | 8 | 7 |
| P12 | Orchestration | 6 | 6 | 9 | 9 |
| **Total** | | **69** | **69** | **194** | **187** |

Each pillar contains: `_schema.yaml` + `templates/` + `examples/` + `compiled/`

## Builders (69 + 1 meta)

All in `archetypes/builders/`. Each has 13 `bld_*.md` ISO files.
Total: 918 ISO files. Meta-builder: `_builder-builder/` (21 files).

## 7 Nuclei

| ID | Domain | Files |
|----|--------|:-----:|
| N01 | Intelligence | 6 |
| N02 | Marketing | 5 |
| N03 | Engineering | 3 |
| N04 | Knowledge | 2 |
| N05 | Operations | 2 |
| N06 | Commercial | 2 |
| N07 | Admin | 2 |

## Tools (_tools/)

| Tool | Purpose |
|------|---------|
| cex_forge.py | Forge v2 — builder-aware artifact generation |
| cex_8f_motor.py | Motor 8F — intent → builder execution plan |
| cex_crew_runner.py | Crew Runner — orchestrate builder pipeline |
| cex_pipeline.py | 5-stage build engine |
| cex_compile.py | .md → .yaml/.json compiler |
| cex_doctor.py | Repo health diagnostic |
| cex_feedback.py | Quality tracking + auto-archive |
| cex_index.py | Regenerate INDEX.md |
| cex_init.py | Scaffold new CEX project |
| compare_builders.py | Diff original vs rebuilt builders |
| validate_builder.py | Validate builder 13-file completeness |
| validate_schema.py | Validate _schema.yaml files |
| distill.py | .md → compiled sync |
| bootstrap.py | Initial repo setup |
| bump_version.py | Semantic version bumper |
| changelog_gen.py | CHANGELOG generator |
| fix_frontmatter.py | Batch frontmatter repair |

---
*Run `python _tools/cex_doctor.py` to validate repo health.*
