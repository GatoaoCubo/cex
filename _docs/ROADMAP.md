---
id: roadmap_cex
kind: context_doc
title: "CEX Roadmap — What Was Done, What's Next"
version: 3.0.0
quality: null
created: 2026-04-07
updated: 2026-04-07
purpose: Single source of truth for CEX progress and next steps
---

# CEX Roadmap

## Current State (2026-04-07)

| Metric | Value |
|--------|-------|
| Kinds | 123 |
| Builders | 124 (115 PASS, 8 WARN, 0 FAIL) |
| Artifacts scored | 3,050 |
| At 9.0+ | 3,049 (100%) |
| Below 9.0 | 0 |
| Flywheel | 109/109 WIRED (100%) |
| Tools | 59 Python tools |
| Rules | 16 |
| N07 memory files | 5 permanent |
| Terminology KCs | 5 (Rosetta Stone + 4 providers) |
| Commits today | 111 |

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

### H2: Continuous batching mode — IN PROGRESS (N05, grid ROADMAP_NEXT)

`cex_mission_runner.py --continuous` verification + fine-tune data export.
Dispatched to N05 on 2026-04-08.

### H3: Fine-tune data export — IN PROGRESS (N05, grid ROADMAP_NEXT)

Export training pairs from existing ISOs for fine-tuning.
Bundled with H2 dispatch to N05.

### H4: capabilities rename (147 files) — DONE (N03, grid ROADMAP_NEXT)

Renamed `capability_summary` to `capabilities` across all 146 files. Python tools, tests, templates, manifests updated.

### H5: NotebookLM pipeline build — IN PROGRESS (N01, grid ROADMAP_NEXT)

Build pipeline components from spec. KC audit + 5 new kind KCs. Dispatched to N01.

### H6: Content Factory commercial layer — IN PROGRESS (N06, grid ROADMAP_NEXT)

Pricing model + monetization audit + product funnel. Dispatched to N06.

---

## NEXT — Medium term (week)

### M1: Full from-zero bootstrap test

Use `boot/overnight_infinite.cmd` to rebuild CEX from a clean state.
Validates the entire infrastructure: mission_state, continuous batching,
sub-agents, multi-provider routing, quality gates.

Expected: ~3-4 hours with full grid + sub-agents.

### M2: capabilities rename — DONE

Completed in H4. All 146 files renamed `capability_summary` → `capabilities`.

### M3: Content Factory v1

Spec exists: `spec_content_factory_v1.md`.
Pipeline: CEX artifacts → multi-format content (blog, social, video scripts).
Uses N02 (marketing) + N06 (commercial) + NotebookLM integration.

### M4: NotebookLM Pipeline

Spec exists: `spec_notebooklm_pipeline.md`.
Pipeline: KCs → Google NotebookLM → audio content.
N01 has MCP server for this (`notebooklm-mcp`).

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

| Metric | Current | Target |
|--------|---------|--------|
| Kinds | 123 | 130+ (as industry evolves) |
| Builders PASS | 115 | 124 (zero WARN) |
| Quality floor | 9.0 (100%) | Maintain |
| Flywheel | 100% | Maintain |
| Portuguese remnants | ~0 | 0 (continuous audit) |
| Industry term alignment | 95% | 99% (quarterly review vs provider docs) |
| Sub-agent coverage | 6 agents | 10+ (specialized per task type) |
| Overnight bootstrap time | Untested | < 4 hours |
