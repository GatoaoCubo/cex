# Changelog

All notable changes to CEX are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

---

## [10.4.0] - 2026-04-21 — CEXAI Rebrand + OSS Wiring Final

### Added
- **CEXAI rebrand**: "Cognitive Enterprise X" renamed to "Cognitive Exchange AI" across all public-facing files
- **`kc_artificial_sins.md`** — canonical 7-sin narrative knowledge card (N02 marketing)
- **`spec_exchange_protocol.md`** — architectural spec for typed cognition exchange (P06)
- **`kc_contributor_nucleus_standard.md`** — technical standard for community N08+ nuclei
- **`kc_admin_vocabulary.md`** — N07 orchestration domain controlled vocabulary
- **`spec_oss_wiring_final.md`** — 12-gap remediation spec from 4 parallel audit agents
- **`pull_request_template.md`** — standard PR template with CEX quality checklist
- **`docs/glossary.md`** — 6 new terms: Artificial Sin, CEXAI, Exchange, Exchange Protocol, Vertical Nucleus
- **`docs/vocabulary.md`** — 8 exchange terms added, entry count 90 to 98
- **`cex_deprecated_terms.txt`** — pre-commit blocklist for old terminology

### Security
- Placeholder emails replaced in SECURITY.md and CODE_OF_CONDUCT.md
- Export script now strips N01-N07 P10_memory/ (80 instance-specific files)
- `brand_config.yaml` added to .gitignore (preventive)
- Export script commit message updated to v10.4.0

### Changed
- README, CLAUDE.md, CONTRIBUTING.md, FAQ, concepts updated with Exchange framing
- "The Artificial Sins" section in README (renamed from "The seven sins")
- `kc_cex_as_digital_asset.md` rewritten as "Knowledge Asset" (avoid crypto connotation)
- Version bumped to 10.4.0 across README badge, pyproject.toml, export script
- `spec_metaphor_dictionary.md` +7 exchange-related term mappings
- Marketing outputs updated: webinar_script, product_tour, interactive_demo

### Stats
- 293 kinds x 298 builders x 12 ISOs = 3,576 artifact constructors
- 4 parallel audit agents: infrastructure 98%, toolchain 95%, nuclei 70%, OSS 85%
- 12 gaps identified, 12 closed in 3 waves
- Tag: v10.4.0-cexai

---

## [10.3.0] - 2026-04-19 — Public Release Preparation

### Added
- **`docs/`** — 7 human-readable docs for newcomers: quickstart, concepts, CLI reference, SDK reference, glossary, FAQ, index
- **`examples/`** — 5 end-to-end patterns: hello_agent, build_artifact, multi_nucleus_crew, knowledge_rag, grid_mission
- **`/consolidate` skill** — full resource manager: processes + GPU VRAM + signals + verify + git state
- **`/dispatch_monitor` skill** — non-blocking poll pattern (git log + status + nvidia-smi at 60-90s intervals)
- **Documentation section in README** — links to docs/ and examples/

### Security
- Removed exec()-based PythonTools (C1: sandbox not secure)
- Fixed shell=True command injection in cex_hooks.py (H7: path injection via crafted filenames)
- SSRF hardening in brand_ingest, cex_auto_research, cex_model_updater (M1: localhost/private IP rejection)
- Atomic PID file writes with tempfile + os.replace (H9: race condition fix)
- Anthropic stream bug fix: get_final_message() moved inside context manager (H8)

### Fixed
- N07 boot agent card path: N07_commercial -> N07_admin (H13)
- Pydantic import made optional with lazy fallback (H14)
- README clone URL corrected to GatoaoCubo/cex (H11)
- Hook log rotation added (500KB cap, keeps last 200 lines) (M5)
- Removed --no-verify from automated git commits in mission_runner and orchestrate (M9)
- MCP config cross-platform: npx direct instead of cmd /c npx (M6)
- datetime.utcnow() replaced with timezone-aware calls in translate, taxonomy_scout (M2)
- CI quality.yml: removed `|| true` that swallowed scoring failures (M14)
- PS parse hook: fixed PowerShell 5.1 argument passing via stdin pipe
- 154 ephemeral .cex/runtime/ files untracked from git history (H10)

### Changed
- Kind count: 257 -> 293 (HERMES assimilation + taxonomy expansion)
- Builder count: 259 -> 295
- ISO count: 13 -> 12 per builder (1:1 pillar mapping)
- All docs translated to English for open-source release
- README updated with Documentation section linking docs/ and examples/
- .gitignore expanded with 8 new patterns for runtime ephemeral files

### Stats
- 293 kinds x 295 builders x 12 ISOs = 3,540 artifact constructors
- 135 Python CLI tools
- 12 pillars x 8 nuclei x 8F pipeline
- 109 flywheel checks (100% WIRED)
- 42 audit findings addressed (28 fixed, 14 already resolved)

---

## [10.2.0] - 2026-04-16 — Open-Source Hardening + Multi-Runtime Grid

### Added
- **Four-runtime grid dispatch** — `dispatch.sh grid-{claude,codex,gemini,ollama,haiku,litellm}` plus mixed-runtime swarms
- **`/showoff` skill** (`_tools/cex_showoff.py`) — 5-wave smoke validation across all 4 runtimes with auto-consolidate + signal safety-net
- **21 Boris-isms** (BORIS_MERGE) — native skills (`/commit`, `/simplify`, `/loop`, `/schedule`, `/batch`, `/btw`, `/verify`, `/dream`), `isolation: worktree` frontmatter on heavy builders, `settings.json` hooks, `--bare` startup, `swarm N kind`, `-w` worktree dispatch, `@.claude learn` PR-comment learning loop
- **Composable crews (WAVE8)** — 5 new primitives (`crew_template` P12, `role_assignment` P02, `capability_registry` P08, `nucleus_def` P02, `team_charter` P12) + `cex_crew.py` list/show/run CLI + grid-of-crews composition
- **LiteLLM dispatch layer** — 7 boot wrappers + JSONL fine-tune logging on every call; proven free-tier grid on Ollama-only (6/6 clean, zero crashes)
- **Hybrid routing** — `cex_router_v2.py` picks Claude vs Ollama per task signature based on 7-nucleus benchmarks (llama3.1:8b wins 5/7, qwen3:14b wins N03+N04, gemma2:9b wins structural synthesis sweep)
- **`cex_release_check.py`** — public-release gate (README, deps, CI, versions)
- **`cex_flywheel_audit.py`** — 109-check doc-vs-practice audit across 7 layers × 7 wires × 7 cascades
- **Reverse compiler** — `cex_compile.py --target {claude-md,cursorrules,customgpt,mcp-server}` makes CEX the single source of truth for any LLM
- **Gitleaks gate** — `.github/gitleaks.toml` + pre-commit scan; audit dumps untracked
- **`.gemini/settings.json`** — `respectGitIgnore: false` so Gemini nuclei can see `.cex/runtime/handoffs/`

### Changed
- **Kind count**: 202 → 257 (REPO_AUDIT_OPENSOURCE 9 waves + OPENSOURCE_FIX follow-ups + TOKEN_TRIM_V1 A/B/C + VERTICAL_DISTILLATION waves 1–4 landed 58 new templates)
- **Builder count**: 207 → 259 (builder-per-kind invariant restored across all new kinds)
- **Builder ISOs**: 2666 → 3381 (13-per-builder pattern enforced)
- **MCP + boot consolidation** — consolidated root `.mcp.json` with per-nucleus overlays (still win)
- **N07_SPAWN_PROBE** — session-aware PID tracking with wrapper → worker resolution via `Win32_Process` BFS; tree-kill is the only reliable stop
- **Codex on ChatGPT-plus auth** — omit `--model` entirely (any explicit model returns HTTP 400); fix landed in `cex_boot_gen.py:build_codex_ps1`
- **Gemini on oauth-personal** — locked to `gemini-2.5-flash-lite` across all 7 nuclei; pro hangs, 2.0-flash 404s
- **`boot_gen` SELF_AUDIT hardcode removed** — codex/gemini `initialMsg` now defers to handoff frontmatter
- **README rewritten** — new positioning ("Cognitive Exchange AI · Seven Artificial Sins, twelve pillars, one typed brain"); maturity-gap table contrasting basic agents vs 12-pillar nuclei; sin-lens table sourced verbatim from `nucleus_def_n0X.md`
- **100% English repo** — open-source pass translates README / CHANGELOG / CONTRIBUTING / CLAUDE.md / 8 nucleus_defs / 38 rules+skills+commands

### Fixed
- **OPENSOURCE_FIX** — 2/5 blockers clean, 2/5 partial, 1/5 skipped (commits `72edab54e`, `7109cde29`, `722238e05`)
- **Showoff runtime fixes (2026-04-16)** — codex model flag, gemini gitignore scope, boot_gen mission names, `--skip` flag for exhausted runtimes
- **Window title truncation** — switched from `MainWindowTitle` to `Win32_Process.CommandLine` for nucleus wrapper identification
- **`$pid` PowerShell reserved-variable bug** — replaced with `$procId` across spawn scripts
- **Gemini kill target** — there is no `gemini.exe`; orphan cleanup now targets `node.exe` by parent-dead
- **Doc drift** — builder count (259 not 260), tool count (152 not 113), pillar count corrected across README/CLAUDE.md

### Removed
- Legacy Portuguese-only operational docs (migrated to English for open-source); brand configs and personal memory remain in user's native language by design

### Stats
- 257 kinds × 259 builders × 13 ISOs = 3,381 artifact constructors
- 152 Python CLI tools (up from 113)
- 12 pillars × 8 nuclei (N00 archetype + N01–N07 operational) × 8F pipeline
- 109 flywheel checks (100% WIRED)
- 4 supported runtimes: Claude (Anthropic), Codex (OpenAI), Gemini (Google), Ollama (local)

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

## Summary (current)

| Metric | Value |
|--------|------:|
| Artifact kinds | 293 |
| Builder factories | 295 |
| Builder ISOs (12 per kind) | 3,540 |
| Sub-agents | 295 |
| Python CLI tools | 135 |
| Pillars | 12 |
| Nuclei | 8 (1 archetype + 7 operational) |
| 8F functions | 8 |
| Flywheel checks | 109 |
| Supported runtimes | 4 (Claude, Codex, Gemini, Ollama) |

---

*CEX v10.3.0 | 2026-04-19 | MIT License*
