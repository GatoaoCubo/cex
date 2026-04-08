---
id: roadmap_cex
kind: context_doc
title: "CEX Roadmap — What Was Done, What's Next"
version: 4.0.0
quality: null
created: 2026-04-07
updated: 2026-04-08
purpose: Single source of truth for CEX progress and next steps
---

# CEX Roadmap

## Current State (2026-04-08)

| Metric | Value |
|--------|-------|
| Kinds | 123 |
| Builders | 123 PASS / 0 WARN / 0 FAIL |
| Builder dirs | 124 (123 kind-builders + _builder-builder) |
| Builder ISOs | 1,599 files (avg density 0.95) |
| Sub-agents | 125 (.claude/agents/) |
| Kind KCs | 123 (98/98 kinds covered) |
| Flywheel | 109/109 WIRED (100%) |
| Python tools | 92 total (64 cex_* tools) |
| Rules | 16 |
| N07 memory files | 6 permanent |
| Terminology KCs | 5 (Rosetta Stone + 4 providers) |
| Commits (2026-04-08) | 29 |

---

## DONE — Session 2026-04-07

### Phase 1: Terminology Standardization

| Task | Result |
|------|--------|
| Metaphor dictionary enriched | 40+ terms with Industry Term column |
| Rosetta Stone KC | Cross-provider mapping: Anthropic, OpenAI, Google, MCP |
| 4 provider KCs | Official vocabulary from each provider |
| 12 schemas PT→EN | All pillar descriptions translated to English |
| 139 builder ISOs PT→EN | "Especialista em" → "Specialist in" across all |
| 6 kind renames | deck→agent_card, vectordb_backend→vector_store, brain_index→knowledge_index, director→supervisor, law→invariant, content_monetization moved P04→P11 |
| 648 file rename | satellite/agent_node → agent_group |
| 4 llm_function nulls fixed | instruction=REASON, hook_config=GOVERN, supervisor=REASON, effort_profile=CONSTRAIN |

### Phase 2: New Capabilities

| Task | Result |
|------|--------|
| 4 new kinds added | prompt_cache, citation, context_window_config, multi_modal_config |
| 4 new builders (52 ISOs) | Full 13-ISO builders for each new kind |
| 4 kind KCs | Knowledge cards for each new kind |
| cex_handoff_composer.py | Auto-selects builders + KCs for handoffs |
| Brand template audit | 13 {{BRAND_*}} gaps closed |
| Context self-selection protocol | All nucleus boot prompts updated |

### Phase 3: Bug Fixes

| Task | Result |
|------|--------|
| F3 INJECT refactored | Pure Python, 14 context sources, zero LLM dependency |
| spawn_stop -Nucleus filter | Fixed: kills only target nucleus |
| CexRouter import | Wired in cex_crew_runner.py, flywheel → 100% |

### Phase 4: Quality Sweep

| Task | Result |
|------|--------|
| Heuristic sweep | 15 null artifacts scored |
| Full grid evolve (6 nuclei) | 735 artifacts evolved to 9.0+ |
| Final count | 3,049/3,050 at 9.0+ (100%) |

### Phase 5: Infinite Bootstrap Infrastructure

| Component | File | Status |
|-----------|------|--------|
| Mission state checkpoint | _tools/cex_mission_state.py | ✅ Built |
| File locking | _tools/cex_lock.py | ✅ Built |
| Overnight infinite loop | boot/overnight_infinite.cmd | ✅ Built |
| Shared-file proposal rule | .claude/rules/shared-file-proposal.md | ✅ Built |
| 125 sub-agent definitions | .claude/agents/*.md | ✅ Built |
| Agent tool (native) | Claude Code built-in sub-agent spawning | ✅ Native |
| Task queue spec | N04_knowledge/architecture/task_queue_spec.md | ✅ Spec written |
| Infinite bootstrap spec | _docs/specs/spec_infinite_bootstrap_loop.md | ✅ Full spec |
| Multi-provider strategy | In spec above | ✅ Documented |

### Phase 6: N07 Evolution

| Component | File | Status |
|-----------|------|--------|
| Technical authority rule | .claude/rules/n07-technical-authority.md | ✅ Active |
| Non-blocking lifecycle | .claude/rules/n07-autonomous-lifecycle.md | ✅ Updated |
| Input transmutation | .claude/rules/n07-input-transmutation.md | ✅ Enhanced |
| User directive memory | N07_admin/memory/user_directive_technical_authority.md | ✅ Permanent |
| Industry audit memory | N07_admin/memory/industry_terminology_audit.md | ✅ Permanent |
| Architecture audit memory | N07_admin/memory/deep_architecture_audit.md | ✅ Permanent |
| Terminology map memory | N07_admin/memory/terminology_standardization.md | ✅ Permanent |

---

## NEXT — Immediate

### H1: Doctor WARN cleanup (8 builders) — DONE (2026-04-08)

Resolved prior to this session. Doctor now: 123 PASS / 0 WARN / 0 FAIL.

### H2: Continuous batching mode — DONE (N05, grid ROADMAP_NEXT)

N05 delivered `cex_continuous.py` for continuous batching + fine-tune data export.
Commit: `0c3eda32`.

### H3: Fine-tune data export — DONE (N05, grid ROADMAP_NEXT)

Bundled with H2. N05 delivered fine-tune export tooling alongside continuous batching.
Commit: `0c3eda32`.

### H4: capabilities rename (147 files) — DONE (N03, grid ROADMAP_NEXT)

Renamed `capability_summary` to `capabilities` across all 146 files. Python tools, tests, templates, manifests updated.
Commit: `b905cffd`.

### H5: NotebookLM pipeline build — DONE (N01, grid ROADMAP_NEXT)

N01 built pipeline components, KC audit, 4 origin fixes, 5 new kind KCs.
Commit: `6b0a2c6d`.

### H6: Content Factory commercial layer — DONE (N06, grid ROADMAP_NEXT)

N06 delivered pricing model, monetization audit, product funnel.
Commit: `7a78dcdf`.

### H7: CANONICALIZATION grid (6 nuclei) — DONE (2026-04-08)

Full 6-nucleus grid for intent resolution canonicalization:
- N01: intent resolution patterns across 16 sources
- N02: value prop + seed words + didactic protocol
- N03: intent resolution map (123 kinds) + quality gate + audit
- N04: intent resolution KC + Rosetta Stone expansion + metaphor audit
- N05: e2e pipeline test + failure modes + performance audit
- N06: moat analysis + pricing tiers + value calculator
Consolidated commit: `c78621d8`.

### H8: INTENT_FIX grid (6 nuclei) — DONE (2026-04-08)

Follow-up grid fixing code + docs from CANONICALIZATION findings:
- N01: confidence scoring + clarification patterns + query decomposition + 50-case benchmark
- N02: onboarding + FAQ + 3 case studies for intent resolution
- N03: didactic protocol + seed words spec + metaphor expansion
- N05: EN verbs + AND split + 65 synonyms + fuzzy matching + confidence scoring
- N06: L0-L7 intent resolution depth spec + conversion triggers
- N07: consolidation + nucleus UX hardening
Consolidated commit: `f3dfc921`.

---

## NEXT — Medium term (week)

### M1: Full from-zero bootstrap test

Use `boot/overnight_infinite.cmd` to rebuild CEX from a clean state.
Validates the entire infrastructure: mission_state, continuous batching,
sub-agents, multi-provider routing, quality gates.

Expected: ~3-4 hours with full grid + sub-agents.

### M2: capabilities rename — DONE (completed in H4)

### M3: Content Factory v1 — PARTIALLY DONE

Spec exists: `spec_content_factory_v1.md`.
Pipeline: CEX artifacts -> multi-format content (blog, social, video scripts).
N06 delivered pricing + funnel (H6). N01 delivered NotebookLM pipeline (H5).
Remaining: integration layer connecting N01 pipeline output to N02/N06 endpoints.

### M4: NotebookLM Pipeline — DONE (completed in H5)

N01 built full pipeline: KC -> NotebookLM -> audio content.
KC audit completed. 4 origin fixes applied.

---

## NEXT — Long term (month)

### L1: CEX as npm package

Release CEX as a distributable package. Users clone or download, then run `/init`.
Gets: all archetypes, schemas, KCs, tools, rules. No brand (blank brain).

Blocker: `cex_release_check.py` must pass all 28 checks.

### L2: Fine-tuned CEX model

Train on 1,630 ISOs + 123 KCs + 377 templates/examples.
Deploy as custom model via API.
Target: 10x faster artifact generation at 90% cost reduction.

### L3: Multi-tenant CEX

Multiple brands running on same infrastructure.
Each brand = separate `.cex/brand/` config.
Nuclei route based on brand context.

### L4: CEX API

REST API exposing CEX capabilities:
- POST /build → 8F pipeline → artifact
- POST /evolve → improve artifact
- GET /query → find relevant artifacts
- POST /mission → decompose + execute

---

## Architecture Health Targets

| Metric | Current (2026-04-08) | Target |
|--------|----------------------|--------|
| Kinds | 123 | 130+ (as industry evolves) |
| Builders PASS | 123 (100%) | Maintain zero WARN/FAIL |
| Builder ISOs | 1,599 (density 0.95) | Maintain density >= 0.85 |
| Kind KCs | 123 (98/98 covered) | 100% coverage |
| Quality floor | 9.0 (100%) | Maintain |
| Flywheel | 109/109 (100%) | Maintain |
| Python tools | 92 (64 cex_*) | Consolidate overlaps |
| Sub-agents | 125 | Maintain 1:1 with builders |
| Rules | 16 | Add as patterns emerge |
| Portuguese remnants | ~0 | 0 (continuous audit) |
| Industry term alignment | 98% | 99% (quarterly review) |
| Intent resolution | 123 kinds mapped + confidence scoring | Full fuzzy matching |
| Overnight bootstrap time | Untested | < 4 hours |
