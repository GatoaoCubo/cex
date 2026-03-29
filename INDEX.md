# CEX Index

**Navigation map** | Updated: 2026-03-29 | 101 kinds, 99 builders, 244 examples, 12 pillars

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
| TAXONOMY_LAYERS.yaml | 98 kinds in layers |
| SEED_BANK.yaml | Seed words per kind |
| TYPE_TO_TEMPLATE.yaml | Kind → template mapping |
| META_TEMPLATE.md | Template that generates templates |
| VERSION.yaml | Version metadata |

## 12 Pillars

| Pillar | Name | Kinds | Templates | Examples | Compiled |
|--------|------|:-----:|:---------:|:--------:|:--------:|
| P01 | Knowledge | 8 | 8 | 87 | 87 |
| P02 | Model | 11 | 11 | 20 | 20 |
| P03 | Prompt | 10 | 7 | 20 | 20 |
| P04 | Tools | 18 | 18 | 38 | 38 |
| P05 | Output | 4 | 4 | 5 | 5 |
| P06 | Schema | 6 | 6 | 11 | 11 |
| P07 | Evals | 10 | 10 | 12 | 12 |
| P08 | Architecture | 7 | 7 | 9 | 9 |
| P09 | Config | 7 | 7 | 8 | 8 |
| P10 | Memory | 6 | 6 | 12 | 12 |
| P11 | Feedback | 6 | 6 | 9 | 9 |
| P12 | Orchestration | 8 | 8 | 13 | 13 |
| **Total** | | **101** | **98** | **244** | **244** |

Each pillar contains: `_schema.yaml` + `templates/` + `examples/` + `compiled/`

## Builders (99 + 1 meta)

All in `archetypes/builders/`. Each has 13 `bld_*.md` ISO files.
Total: 1,295 ISO files. Meta-builder: `_builder-builder/` (21 files).

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

## KC Library (79 Knowledge Cards across 17 domains)

All in `P01_knowledge/examples/ex_knowledge_card_*.md`. 100% compiled.

| Domain | KCs | Description |
|--------|:---:|-------------|
| cex_taxonomy | 36 | CEX concepts, functions, pillars, types |
| meta | 13 | Meta-construction, self-build, fractal architecture |
| llm_engineering | 5 | Model capabilities, benchmarks, prompt caching |
| research | 4 | RAG fundamentals, search, embedding |
| llm_memory | 3 | Persistence, compression, cross-IDE |
| execution | 3 | Pipeline execution, deployment patterns |
| knowledge_engineering | 2 | Distillation, structured data |
| architecture | 2 | Design tokens, component maps |
| Others (9 domains) | 11 | Debugging, hooks, plugins, content, dev tools |

**KC Sources**: distilled (from research), authored (manual), generated (from tools).
**Feeds**: KC-Domains → `feeds_kinds` wiring → Motor 8F INJECT function.

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
| cex_research.py | Research pipeline runner |

---

## Summary

| Metric | Count |
|--------|------:|
| Kinds | 101 |
| Templates | 98 |
| Builders | 99 + 1 meta |
| Builder ISOs | 1,295 |
| Examples | 244 |
| Compiled | 244 |
| KC Examples | 79 |
| KC Domains | 17 |
| Tools | 18 |
| Pillars | 12 |
| Nuclei | 7 |

---
*Run `python _tools/cex_doctor.py` to validate repo health.*
