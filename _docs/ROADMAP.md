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
| 6 sub-agent definitions | .pi/agents/*.md | ✅ Built |
| Subagent extension | .pi/extensions/subagent/ | ✅ Installed |
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

## NEXT — Immediate (next session)

### H1: Doctor WARN cleanup (8 builders)

7 builders have ISOs slightly oversized (>6144B), 1 has low density (0.78).

| Builder | Issue | Fix |
|---------|-------|-----|
| agent-card-builder | bld_examples 6642B | Trim examples |
| compression-config-builder | bld_memory 6284B | Compress |
| guardrail-builder | bld_examples 6377B | Trim |
| session-backend-builder | bld_memory 6167B | Compress |
| system-prompt-builder | bld_examples 6350B | Trim |
| trace-config-builder | bld_memory 6343B | Compress |
| webhook-builder | bld_output_template density 0.78 | Restructure |
| workflow-primitive-builder | bld_examples 6424B | Trim |

Effort: 1 dispatch to N03. ~10 min.

### H2: Continuous batching mode

`cex_mission_runner.py --continuous` was specified but needs verification.
Test with a mini-mission (10 artifacts across 3 nuclei).

Effort: 1 dispatch to N05. ~15 min.

### H3: Fine-tune data export

Export training pairs from existing ISOs for fine-tuning:
- Input: kind name + schema definition
- Output: complete ISO artifact

This creates the dataset for the T3 fine-tuned model described in the spec.

Effort: 1 dispatch to N05. ~30 min.

---

## NEXT — Medium term (week)

### M1: Full from-zero bootstrap test

Use `boot/overnight_infinite.cmd` to rebuild CEX from a clean state.
Validates the entire infrastructure: mission_state, continuous batching,
sub-agents, multi-provider routing, quality gates.

Expected: ~3-4 hours with full grid + sub-agents.

### M2: capability_summary rename → capability_summary

141 files still use the non-standard term `capability_summary`.
Scheduled for overnight batch.

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

Release CEX as a distributable pi package. Users install via:
```bash
npm install @cex/brain
```
Gets: all archetypes, schemas, KCs, tools, rules. No brand (blank brain).

Blocker: `cex_release_check.py` must pass all 28 checks.

### L2: Fine-tuned CEX model

Train on 1,630 ISOs + 123 KCs + 377 templates/examples.
Deploy as custom provider in pi.
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
