---
id: roadmap_cex
kind: context_doc
title: "CEX Roadmap — What Was Done, What's Next"
version: 5.0.0
quality: 8.9
created: 2026-04-07
updated: 2026-04-08
purpose: Single source of truth for CEX progress and next steps
density_score: 1.0
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
| Python tools | 95 total (67 cex_* tools) |
| Rules | 16 |
| N07 memory files | 6 permanent |
| Terminology KCs | 5 (Rosetta Stone + 4 providers) |
| Ollama models | 2 (qwen3:8b, deepseek-r1:8b) |
| Distribution | install.cmd + release.cmd ready |
| Commits (2026-04-08) | 35+ |

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
| User directive memory | N07_admin/P10_memory/user_directive_technical_authority.md | ✅ Permanent |
| Industry audit memory | N07_admin/P10_memory/industry_terminology_audit.md | ✅ Permanent |
| Architecture audit memory | N07_admin/P10_memory/deep_architecture_audit.md | ✅ Permanent |
| Terminology map memory | N07_admin/P10_memory/terminology_standardization.md | ✅ Permanent |

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

### H9: Distribution Infrastructure — DONE (2026-04-08)

| Component | File | Status |
|-----------|------|--------|
| One-click installer | install.cmd | Built (8 steps: winget, Git, Python, Node, Claude, repo, deps, PS policy) |
| Release ZIP builder | release.cmd | Built (6 steps: doctor, compile, sanitize, git archive, verify, checksum) |
| Security fix | .gitignore | Added `**/*_token.json`, `**/*_credentials.json`, `_releases/` |
| Canva token leak | .cex/brand/canva_token.json | Removed from git tracking |
| Release check | cex_release_check.py | 25/28 PASS (3 cosmetic README fixes) |

### H10: Ollama Pipeline — DONE (2026-04-08)

Free local model support for CEX. Models run on user's hardware, zero API cost.

| Component | File | Status |
|-----------|------|--------|
| Ollama client | cex_ollama.py | Built (health, list, generate, artifact retry, /no_think) |
| Benchmark tool | cex_benchmark_ollama.py | Built (10 tasks, HTTP API, scoring) |
| Intent router | cex_intent.py | Updated (model_override, CEX_FORCE_OLLAMA, CEX_OLLAMA_MODEL) |
| 8F pipeline | cex_8f_runner.py | Updated (--model, F4 skip, ultra-lite F6: 15->5 sections) |
| Dispatch modes | dispatch.sh | Added `ollama` and `ollama-grid` modes |
| Router config | router_config.yaml | Updated (qwen3:8b, deepseek-r1:8b) |
| Nucleus fallbacks | nucleus_models.yaml | Updated (fallback_local -> qwen3:8b) |
| E2E proof | p01_kc_markdown_tables.md | Generated via Ollama, F7: 6/6 PASS |

Performance on GTX 1070 (4GB VRAM):
- Direct generation: ~4 min per artifact
- Full 8F pipeline (ultra-lite): ~7 min per artifact
- Speed: ~4.5 tok/s (CPU offload, 10x faster on RTX 3060+)

### H11: Token Optimization (4 tools) — DONE (2026-04-08)

| Tool | Change | Savings |
|------|--------|---------|
| cex_memory_select.py | LLM -> TF-IDF cosine similarity | ~1K tokens/call |
| cex_score.py | L3 cache inheritance gate | ~2K tokens/artifact |
| cex_8f_runner.py | Template-first F4 skip | ~5K tokens/build |
| cex_evolve.py | Heuristic add_updated, add_tags | ~1K tokens/artifact |

---

## NEXT SESSION — Start here

### S1: Fine-tune dataset preparation

Build QLoRA training dataset from CEX's own artifacts:
- Source: 1,630 ISOs + 123 KCs + 377 templates/examples
- Format: instruction/response pairs for Qwen 3 8B
- Tool: `cex_continuous.py` (built in H2) has export mode
- Target: 2,000+ training pairs covering all 123 kinds
- Validate: train/test split, dedup, format check

### S2: QLoRA fine-tune on Qwen 3 8B

Train custom model `cex-qwen3:8b` using prepared dataset:
- Framework: Unsloth or Axolotl (QLoRA, 4-bit)
- Hardware: GTX 1070 4GB (tight -- use gradient checkpointing)
- Epochs: 3-5 on full dataset
- Eval: re-run benchmark tool, compare base vs FT
- Deploy: `ollama create cex-qwen3 -f Modelfile`

### S3: Hybrid dispatch (Claude N07 + Ollama nuclei)

Wire the pipeline so `/mission` and `/grid` dispatch to Ollama:
- N07 stays Claude Opus (orchestration needs full agent)
- N01-N06 workers use Ollama/cex-qwen3 via `cex_8f_runner.py`
- Handoff format stays the same (model reads via pipeline, not CLI)
- F8 compiles + commits (pipeline handles, not model)
- Test: full 6-nucleus grid via Ollama

### S4: Benchmark re-run (valid comparison)

Re-run with fixed code (HTTP API, 300s timeout, /no_think):
- `python _tools/cex_benchmark_ollama.py --models qwen3:8b,deepseek-r1:8b --timeout 600`
- Compare: base Qwen 3 vs base DeepSeek R1 vs FT cex-qwen3
- Publish results to `.cex/benchmarks/`

### S5: Content Factory integration

Connect existing components into working pipeline:
- N01 NotebookLM pipeline (H5) -> input
- N02 content templates -> formatting
- N06 monetization layer (H6) -> distribution
- Remaining: integration workflow connecting the pieces

---

## NEXT — Medium term (week)

### M1: Full from-zero bootstrap test

Use `boot/overnight_infinite.cmd` to rebuild CEX from a clean state.
Validates: mission_state, continuous batching, sub-agents, quality gates.
Expected: ~3-4 hours with full grid + sub-agents.

### M2: Release v1.0 on Hotmart/Gumroad

Pre-requisites:
- `cex_release_check.py` passes 28/28 (3 README fixes remaining)
- Course outline or quickstart guide for buyers
- ZIP tested on clean Windows 10 VM
- Payment + download flow tested end-to-end

### M3: Ollama-only mode (zero Claude dependency)

Make CEX fully functional without any Claude subscription:
- Replace N07 orchestration with CLI wizard + cex_mission_runner.py
- All nuclei via Ollama/cex-qwen3
- install.cmd installs Ollama instead of Claude Code
- Target audience: users who can't afford $20/month

---

## NEXT — Long term (month)

### L1: CEX as distributable product

Release CEX as downloadable package:
- install.cmd (built, H9) handles dependencies
- release.cmd (built, H9) packages ZIP
- Channels: Hotmart ZIP, GitHub Releases, Gumroad

### L2: Fine-tuned CEX model (production)

Iterate on S2 prototype:
- Larger dataset (add user artifacts, session outputs)
- Multi-model: cex-qwen3:8b (free), cex-qwen3:32b (better GPU)
- Publish on Ollama registry or HuggingFace
- Potential revenue: sell fine-tuned model access

### L3: Multi-tenant CEX

Multiple brands running on same infrastructure.
Each brand = separate `.cex/brand/` config.
Nuclei route based on brand context.

### L4: CEX API (SaaS)

REST API exposing CEX capabilities:
- POST /build -> 8F pipeline -> artifact
- POST /evolve -> improve artifact
- GET /query -> find relevant artifacts
- POST /mission -> decompose + execute
- Revenue: usage-based pricing

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
| Python tools | 95 (67 cex_*) | Consolidate overlaps |
| Sub-agents | 125 | Maintain 1:1 with builders |
| Rules | 16 | Add as patterns emerge |
| Ollama models tested | 2 (qwen3:8b, deepseek-r1:8b) | FT model: cex-qwen3:8b |
| Ollama pipeline | Working (ultra-lite, 7 min/artifact) | < 2 min with FT + better GPU |
| Distribution | install.cmd + release.cmd ready | v1.0 on Hotmart |
| Overnight bootstrap time | Untested | < 4 hours |
