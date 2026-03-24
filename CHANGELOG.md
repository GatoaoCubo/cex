# CHANGELOG

All notable changes to CEX are documented here.
Format: Wave-based (chronological order).

---

## [3.0.0] - 2026-03-23

### Added
- Dual output architecture: .md (human) + compiled .yaml/.json (machine)
- `machine_format` field in all 73 types across 12 LPs (64 yaml, 9 json)
- `_meta/DECISION_MAP.md`: file category -> LP -> type -> format routing table
- `_tools/cex_compile.py`: compiles .md examples to machine-optimized format
- `_tools/validate_compiled.py`: validates compiled artifacts
- `compiled/` directory in each LP
- P03 schema completed: meta_prompt + router_prompt types (were missing)
- source_map field in P03 types: maps existing codexa-core artifacts to CEX types

### Changed
- All 12 `_schema.yaml` updated to v2.0/v3.0
- P03 `_schema.yaml` user_prompt body_structure: context-first ordering (research-validated)
- P03 few_shot max_examples: 10 -> 5 (diminishing returns research)

### Research Basis
- KC_SHAKA_ANTHROPIC_PROMPT_ENGINEERING (9.0): XML for Claude, caching patterns
- KC_SHAKA_097_META_PROMPT_ENGINEERING_2025 (8.7): knowledge-first +0.91, MIPRO +13%
- KC_SHAKA_DSPY_PROGRAMMATIC_PROMPTING (9.0): Signatures, BootstrapFewShot
- KC_EDISON_024_CHAIN_OF_THOUGHT (9.5): Metacognitive +26.9%

---

## [1.1.0] - 2026-03-23

### Versioning System (EDISON)
- `_meta/VERSION.yaml` — formal version manifest with real counts per LP (12 LPs, 69 types, 21 templates, 48 examples)
- `_tools/bump_version.py` — version bumper with `--lp` and `--level` args, auto-updates CHANGELOG
- `_tools/changelog_gen.py` — git log parser, groups commits by LP, generates formatted entries
- Post-v1.0 additions: ISO package spec, compile/decompile/validate tools, deck system, GDrive integration
- Pipeline: distill.py (template-as-prompt), audio feedback (Edge TTS), contributor ingestion pipeline
- Packages: 7 golden agents normalized to ISO Package Spec format
- ML Algorithm Map: first universal KC (dual: CEX framework + instance pool)

---

## [1.0.0] - 2026-03-22

### Wave 6: Product Release (PYTHA + STELLA)
- Bootstrap CLI (`_tools/bootstrap.sh`) — creates full LP structure in new repos
- Dogfood mode — CEX used to generate CEX artifacts (flywheel activated)
- Full documentation suite: ARCHITECTURE.md, CONTRIBUTING.md, CHANGELOG.md
- README v1.0 finalized with badge, tree, 3-step getting started, MIT license
- CODEX v4: final metrics + all wave decisions consolidated

### Wave 5: Anti-Fragility (PYTHA)
- Meta-docs v3: CODEX + ROADMAP + README updated with real data from execution
- Density Report: 18 examples analyzed — Elite:6 / High:12 / Standard:0 / mean:88.6%
- 3 validators: `validate_schema.py`, `validate_generators.py`, `validate_examples.py`
- QUALITY+SCALE templates: P05 output_schema template added
- GOLDEN_CANDIDATES.md updated with priority queue

### Wave 4: Golden Migration (PYTHA + STELLA)
- Migration map: 9,916 files from codexa-core classified into 9 LP buckets
  - KC: 638 | HOP: 701 | AGT: 570 | SKL: 412 | FAT: 89 | ADW: 312 | others
- 12 golden examples migrated (4 KC + 3 agent + 3 prompt + 2 skill)
- GOLDEN_CANDIDATES.md: 22 candidates identified with priority queue

### Wave 3: Generators + Examples (PYTHA + EDISON)
- 12 generators (P01-P12): step-by-step authoring + anti-patterns per LP
- 18 golden examples across P01-P04 (density avg 88.6%, range 0.85-0.95)
- 7 templates: P01(3) + P02(1) + P03(1) + P04(1) + P05(1)
- Meta-template v1 (`_meta/META_TEMPLATE.md`) — the template that generates templates
- Validation chain test PASS: META_TEMPLATE > schema > template > instance pipeline
- GLOSSARY.md and MANDAMENTOS.md consolidated

### Wave 2: Schemas 12LP (EDISON + PYTHA)
- 12 schemas (`_schema.yaml` per LP) with full field constraints
- 68 artifact types across all layers:
  - CORE (P01-P04): 27 types
  - QUALITY (P05-P08): 20 types
  - SCALE (P09-P12): 21 types
- Pre-commit validation hooks wired to schemas

### Wave 1: Destilar (SHAKA x3 grid)
- 42KB distillation from 9,910 MD files + 783 golden in codexa-core
- Pattern extraction: density tiers, naming conventions, frontmatter structure
- P01/_schema.yaml v0 — first schema derived from real data
- First golden example: `p01_kc_catalogo_proprio_mercado_livre` (density 0.92)
- CEX scaffold (`P01-P12/` + `_meta/`) created

---

## Summary

| Metric | Value |
|--------|-------|
| Leverage Points | 12 (P01-P12) |
| Artifact Types | 69 |
| Schemas | 12/12 |
| Generators | 12/12 |
| Templates | 21 |
| Examples (golden) | 48 |
| Validators | 3 |
| Density avg | 88.6% |
| Elite examples | 6 (density >= 0.90) |
| Files indexed | 9,916 (migration map) |
| Total commits | 30+ |
| Repo size | ~65KB |

---

## Credits

| Satellite | Role | Waves |
|-----------|------|-------|
| STELLA | Orchestration, handoffs, mission control | 1-6 |
| SHAKA | codexa-core distillation, pattern extraction | 1, 4 |
| PYTHA | Knowledge, generators, examples, templates, docs | 3-6 |
| EDISON | Schemas (P05-P12), validators, bootstrap CLI | 2-3, 6 |
| ATLAS | Chain validation, VALIDATION_REPORT.md | 3 |

---

*CEX v1.1.0 | 2026-03-23 | MIT License*
