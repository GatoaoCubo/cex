# Changelog

All notable changes to CEX are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

---

## [10.1.0] - 2026-04-07 — G13 Terminology Unification

### Changed
- Renamed `satellite` and `agent_node` to `agent_group` across 648 files (2,078 insertions, 2,003 deletions)
- All case variants handled: lowercase, Capitalized, UPPER, plurals, compound identifiers
- Portuguese translation pairs in `translate_isos.py` updated
- G13 gap closed — zero residual old terms remain

---

## [10.0.0] - 2026-04-01 — Runtime Assimilation (Agno → CEX)

### Added — Phase 1: Runtime Foundation (v7.x)
- `cex_sdk/models/` — Model ABC + 6 providers (Claude, GPT, Gemini, Ollama, OpenRouter, LiteLLM)
- `cex_sdk/models/message.py` — Message dataclass for LLM conversations
- `cex_sdk/models/response.py` — ModelResponse + ToolExecution
- `cex_sdk/models/metrics.py` — Token/cost/timing metrics (RunMetrics, MessageMetrics)
- `cex_sdk/models/structured.py` — Pydantic structured output parsing (4 strategies)
- `cex_sdk/tools/` — Toolkit framework + Function auto-schema + @cex_tool decorator
- `cex_sdk/guardrails/` — PII detection (US+BR), prompt injection (EN+PT), BaseGuardrail ABC

### Added — Phase 2: Knowledge Pipeline (v8.x)
- `cex_sdk/knowledge/reader/` — 5 readers (markdown, PDF, CSV, JSON, web)
- `cex_sdk/knowledge/chunking/` — 4 strategies (fixed, recursive, markdown, base)
- `cex_sdk/knowledge/embedder/` — 2 providers (OpenAI, Ollama) + ABC
- `cex_sdk/vectordb/` — ChromaDB backend + VectorDb ABC
- `cex_sdk/knowledge/reranker/` — Cohere reranker + ABC

### Added — Phase 3: Execution Engine (v9.x)
- `cex_sdk/workflow/` — 5 primitives (Step, Parallel, Loop, Condition, Router) + Workflow orchestrator
- `cex_sdk/memory/manager.py` — LLM-powered memory extraction (6 memory types)
- `cex_sdk/memory/compression.py` — Context compression manager
- `cex_sdk/eval/base.py` — BaseEval (pre_check/post_check) + QualityGateEval
- `cex_sdk/reasoning/step.py` — ReasoningStep + ReasoningTrace with GDP integration

### Added — Phase 4: Integrations (v10.x)
- `cex_sdk/tools/mcp/client.py` — MCP bridge (MCPTools)
- `cex_sdk/tools/builtin/` — 4 tool kits (file, shell, python, web)
- `cex_sdk/tracing/exporter.py` — Trace/Span/TraceExporter for 8F observability
- `cex_sdk/session/base.py` — Per-user session state persistence

### Stats
- 78 Python files, 4504 lines absorbed from Agno patterns
- 46 integrity tests (100% passing)
- Source: https://github.com/agno-agi/agno (MPL-2.0)
- See: `_docs/ASSIMILATION_PLAN.md` for full roadmap
- See: `_docs/AGNO_vs_CEX_ANALYSIS.md` for competitive analysis

---

## [6.0.0] - 2026-03-27 — Governance

### Added
- `cex_doctor.py` v2: naming v2.0 validation + density checks + 13-file completeness
- `validate_builder` v2 + pre-commit hook with 7 automated checks
- Multi-LLM entry points: Cursor, Copilot, Windsurf, Claude rules generated
- `cex_pipeline.py`: 5-stage engine (CAPTURE > DECOMPOSE > HYDRATE > COMPILE > ENVELOPE)
- `cex_index.py`: SQLite index scanning 1642 files + wikilink graph
- `cex_feedback.py`: quality tracking + auto-archive + promotion engine
- `cex init` CLI: 5 interactive questions to functional repo
- Onboarding + quickstart + FAQ documentation suite
- README v2: public-facing with architecture diagram + quickstart

### Changed
- CODEX.md updated to v6.0.0
- Pre-commit hooks enforce naming v2.0 + density + 13-file structure
- CONTRIBUTING.md v2.0: builder guide with 13-file spec + `cex_doctor` workflow

---

## [5.0.0] - 2026-03-25 — Fractal Nuclei

### Added
- 7 departments (N01-N07) x 12 subdirs: fractal organizational structure
- Skeleton instances illustrating ideal CEX architecture per department
- Obsidian integration: graph colors by 8 functions + full repo audit map
- Whitepaper v3.0: 12 sections, 20KB, compiled from structured rascunho

### Changed
- Repository expanded from flat pillars to department-based fractal hierarchy
- Obsidian graph visualization enabled for cross-pillar navigation

---

## [4.0.0] - 2026-03-24 — Naming v2.0

### Added
- Naming convention v2.0: `bld_{kind}_{topic}.md` pattern enforced

### Changed
- 932 builder files renamed to comply with naming v2.0
- 158 legacy examples renamed (agent_group > director terminology)

### Removed
- Legacy naming patterns (mixed case, hyphens, non-standard prefixes)
- organization-specific jargon universalized across all files

---

## [3.0.0] - 2026-03-23 — Dual Output + Builders

### Added
- Dual output architecture: `.md` (human) + compiled `.yaml`/`.json` (machine)
- `machine_format` field in all 73 types across 12 LPs (64 yaml, 9 json)
- `archetypes/DECISION_MAP.md`: file category > LP > type > format routing
- `_tools/cex_compile.py`: compiles .md examples to machine-optimized format
- `_tools/validate_compiled.py`: validates compiled artifacts
- 35 builder archetypes (Waves 8-22): each with 13 ISO files
- Schema v2 refinement: evidence-calibrated across all 10 builder kinds
- Bootstrap regeneration: 7 docs x 35 builders (C01-C07 waves)
- P03 schema completed: meta_prompt + router_prompt types

### Changed
- All 12 `_schema.yaml` updated to v2.0/v3.0
- P03 user_prompt body_structure: context-first ordering (research-validated)
- P03 few_shot max_examples: 10 > 5 (diminishing returns)

---

## [2.0.0] - 2026-03-23 — Schemas + Generators

### Added
- 12 schemas (`_schema.yaml` per LP) with full field constraints
- 68 artifact types across all layers (CORE 27 + QUALITY 20 + SCALE 21)
- 12 generators (`_generator.md` per LP): step-by-step authoring + anti-patterns
- 7 templates across P01-P05
- 18 golden examples (density avg 88.6%, range 0.85-0.95)
- Meta-template v1 (`archetypes/META_TEMPLATE.md`)
- 3 validators: `validate_schema.py`, `validate_generators.py`, `validate_examples.py`
- Migration map: 9,916 files classified into 9 LP buckets
- 12 golden examples migrated + 22 candidates identified
- Density Report: Elite 6, High 12, mean 88.6%
- Versioning system: `VERSION.yaml`, `bump_version.py`, `changelog_gen.py`
- Pre-commit validation hooks wired to schemas

### Changed
- Max file size: 2KB > 4KB (golden avg ~3KB)
- Density floor: 0.75 > 0.80 (all examples exceeded 0.85)
- Elite tier: 0.95 > 0.90 (6 qualifying examples)

---

## [1.0.0] - 2026-03-22 — Initial Release

### Added
- CEX scaffold: 12 pillars (P01-P12) with CORE + QUALITY + SCALE layers
- 42KB distillation from 9,910 MD files + 783 golden in organization-core
- Pattern extraction: density tiers, naming conventions, frontmatter structure
- First golden example: `p01_kc_catalogo_proprio_mercado_livre` (density 0.92)
- Bootstrap CLI (`_tools/bootstrap.sh`): creates full LP structure in new repos
- Dogfood mode: CEX generates CEX artifacts (flywheel activated)
- CODEX v4, GLOSSARY, MANDAMENTOS documentation
- ARCHITECTURE.md, CONTRIBUTING.md, README v1.0
- MIT License

---

## Summary

| Metric | Value |
|--------|-------|
| Pillars | 12 (P01-P12) |
| Departments | 7 (N01-N07) |
| Artifact Types | 73 |
| Builder Archetypes | 35 |
| Schemas | 12/12 |
| Generators | 12/12 |
| Templates | 21 |
| Examples (golden) | 48 |
| Validators | 6 |
| Density avg | 88.6% |
| Files indexed | 1,642 (SQLite) |

---

*CEX v6.0.0 | 2026-03-27 | MIT License*
