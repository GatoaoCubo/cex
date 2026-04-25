---
quality: 8.3
id: spec_opensource_release_v1
kind: constraint_spec
pillar: P06
title: "Spec -- CEX Open-Source Release v1.0.0"
version: 1.0.0
created: "2026-04-19"
author: n07_orchestrator
domain: release_engineering
quality_target: 9.0
status: SPEC
scope: full_repo
depends_on:
  - spec_iso_12p_refactor
  - spec_hermes_assimilation
tags: [spec, release, open-source, pre-release, audit]
tldr: "42-finding audit fix + repo hygiene + SDK docs + examples + CI hardening = v1.0.0"
density_score: 0.95
updated: "2026-04-22"
---

# CEX Open-Source Release v1.0.0

## Problem

CEX has 300 kinds, 3,647 ISOs, 301 builders, 148 tools, 4 runtimes, and a
proven 30/30 multi-runtime showoff. But the repo is not shippable:

1. **Security**: 2 critical vulns fixed (C1 exec, C2 shell), 2 remain (C3 done prior, C4 manual key rotation)
2. **Language**: 12 docs files still contain PT-BR; open-source mandate is EN-only
3. **Hygiene**: 154 tracked files are ephemeral (cache, benchmarks, compiled skills, task stubs, binary media)
4. **Documentation**: CLAUDE.md is for the AI, not humans. No SDK docs, no quickstart, no examples/
5. **CI**: quality.yml swallows failures with `|| true`; no cross-platform test matrix
6. **Skills**: /consolidate doesn't manage GPU VRAM; no orchestrator skill organization
7. **Competitive gap**: CrewAI has `pip install` + 20-line hello world; CEX SDK exists but is undocumented

## Vision

Ship a repo where a stranger can:
1. `pip install cex-sdk` and run a 5-line agent in 2 minutes
2. Read a human-readable quickstart (not CLAUDE.md)
3. See 5 end-to-end examples that prove CEX's unique value
4. Trust that CI gates quality (no `|| true`)
5. Know that no secrets, PT-BR noise, or machine-specific data leaked

## Decision Context (from prior sessions + today's audit)

- Language: EN-only for all public docs (PT-BR only in bilingual intent tables)
- License: MIT (already in pyproject.toml)
- Audience: solo operators building enterprise AI, not quick-bot builders
- Positioning: typed knowledge infrastructure, NOT "CrewAI killer"
- SDK API: CEXAgent + cex_build() + cex_dispatch()
- All nuclei: Opus tier (no downgrade)
- Boot scripts: Windows-only acknowledged, documented in README

---

## Artifacts

### Wave 1: Security + Audit Commit (N07 direct -- no dispatch)

Already done in this session. Commit the 29 changed files.

| Action | Path | Kind | Status | Notes |
|--------|------|------|--------|-------|
| FIXED | cex_sdk/tools/builtin/python_tools.py | security | done | C1: exec() stubbed |
| VERIFIED | cex_sdk/tools/builtin/shell_tools.py | security | already clean | C2: shlex + shell=False |
| FIXED | _tools/cex_hooks.py:391 | security | done | H7: path via $args[0] |
| FIXED | cex_sdk/models/providers/anthropic.py:137 | bugfix | done | H8: stream ctx manager |
| FIXED | _tools/cex_agent_spawn.py:489 | bugfix | done | H9: atomic PID write |
| FIXED | boot/n07.ps1:89 | bugfix | done | H13: N07_admin not N07_commercial |
| FIXED | cex_sdk/models/base.py:18 | bugfix | done | H14: lazy pydantic import |
| FIXED | install.cmd:114 | bugfix | done | H11: GatoaoCubo/cex URL |
| FIXED | README.md + CLAUDE.md | docs | done | H4: stale counts updated |
| FIXED | _tools/cex_translate.py:476 | deprecation | done | M2: datetime.now(timezone.utc) |
| FIXED | _tools/cex_taxonomy_scout.py:357 | deprecation | done | M2: same |
| FIXED | _tools/cex_mission_runner.py:632 | hygiene | done | M9: removed --no-verify |
| FIXED | _tools/cex_orchestrate.py:100 | hygiene | done | M9: removed --no-verify |
| FIXED | _tools/cex_hooks_native.py | feature | done | M5: hook log rotation 500KB |
| FIXED | .mcp.json | compat | done | M6: npx direct (9 entries) |
| HARDENED | _tools/brand_ingest.py | security | done | M1: SSRF localhost/::1 |
| HARDENED | _tools/cex_auto_research.py | security | done | M1: SSRF validation order |
| HARDENED | _tools/cex_model_updater.py | security | done | M1: SSRF localhost/::1 |

**Commit message**: `[N07] pre-release audit: 28 fixes (C1-C2, H4-H14, M1-M9)`

### Wave 2: Repo Hygiene (N07 direct -- gitignore + git rm)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| GITIGNORE | n0[1-7]_task.md | ephemeral | -- | 6 stale handoff stubs at root |
| GITIGNORE | .cex/cache/ | generated | -- | 125 pre-compiled builder cache files |
| GITIGNORE | .cex/benchmarks/ | machine-specific | -- | RTX 5070 Ti benchmark data |
| GITIGNORE | .cex/auto_cycle_results.json | ephemeral | -- | stale auto-cycle result |
| GITIGNORE | .cex/skills/autocreated/ | noise | -- | 13 hash-named auto-generated skills |
| GITIGNORE | .cex/skills/compiled/ | noise | -- | 9 hash-named compiled YAML |
| GITIGNORE | .cex/nudges/ | runtime | -- | nudge_state.db is ephemeral |
| GIT-RM | .cex/cache/*.json | untrack | -- | `git rm -r --cached .cex/cache/` |
| GIT-RM | .cex/benchmarks/ | untrack | -- | `git rm -r --cached .cex/benchmarks/` |
| GIT-RM | .cex/skills/compiled/ | untrack | -- | `git rm -r --cached .cex/skills/compiled/` |
| GIT-RM | n0[1-6]_task.md | untrack | -- | `git rm --cached n0?_task.md` |
| MOVE | _docs/cex_overview.mp4 | binary | 3.7MB | move to external host, replace with link |
| MOVE | _docs/cex_overview_audio.mp3 | binary | 1.2MB | move to external host, replace with link |
| GITIGNORE | _docs/*.mp4, _docs/*.mp3 | binary | -- | prevent future media commits |

**Commit message**: `[N07] repo hygiene: untrack 154 ephemeral files, gitignore cache/benchmarks/tasks`

### Wave 3: EN Translation (N04 dispatch -- Knowledge nucleus)

12 files with PT-BR content that must be EN-only for open source.

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| TRANSLATE | _docs/SCRIPT_CEX_OVERVIEW.md | docs | 4KB | 100% PT-BR presentation script |
| TRANSLATE | _docs/MOTOR_8F_SPEC.md | spec | 8KB | heavy PT-BR field descriptions |
| TRANSLATE | _docs/8F_BUILDER_MAP.yaml | data | 6KB | PT-BR descriptions in values |
| TRANSLATE | _docs/specs/spec_content_factory_v1.md | spec | 3KB | scattered PT-BR lines |
| TRANSLATE | _docs/specs/spec_n02_part2_schemas_output_quality.md | spec | 3KB | scattered PT-BR lines |
| TRANSLATE | _docs/specs/spec_n05_part2_schemas_output_quality.md | spec | 3KB | scattered PT-BR lines |
| TRANSLATE | _docs/specs/spec_seed_words.md | spec | 2KB | PT-BR fragments |
| GITIGNORE | _docs/archive/ | archive | -- | 13 internal planning docs, not public |
| GIT-RM | _docs/archive/*.md | untrack | -- | `git rm -r --cached _docs/archive/` |

**Commit message**: `[N04] EN translation: 7 docs files translated, archive/ untracked`

### Wave 4: SDK Documentation (N04 dispatch)

Human-readable docs that a stranger can follow. NOT CLAUDE.md rewrites.

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | docs/README.md | docs | 1KB | Docs index with navigation |
| CREATE | docs/quickstart.md | quickstart_guide | 4KB | pip install + 5-line agent + first build |
| CREATE | docs/concepts.md | knowledge_card | 6KB | 8F, 12P, nuclei, kinds explained for humans |
| CREATE | docs/cli-reference.md | api_reference | 5KB | /build, /mission, /grid, /validate, /dispatch |
| CREATE | docs/sdk-reference.md | api_reference | 6KB | CEXAgent, cex_build(), cex_dispatch() API |
| CREATE | docs/architecture.md | knowledge_card | 5KB | How CEX thinks (8F), how it organizes (12P), how it scales (nuclei) |
| CREATE | docs/glossary.md | glossary_entry | 3KB | nucleus, pillar, kind, ISO, 8F, GDP -- plain English |
| CREATE | docs/faq.md | faq_entry | 3KB | "How is this different from CrewAI?" etc. |
| REWRITE | README.md | docs | -- | Add "Documentation" section linking to docs/ |

**Commit message**: `[N04] SDK documentation: quickstart, concepts, CLI/SDK reference, glossary, FAQ`

### Wave 5: Runnable Examples (N03 dispatch)

5 end-to-end examples that prove CEX's unique value. Each must be self-contained.

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | examples/README.md | docs | 2KB | Index of examples with difficulty levels |
| CREATE | examples/01_hello_agent/main.py | code | 1KB | 5-line CEXAgent, produce 1 knowledge_card |
| CREATE | examples/01_hello_agent/README.md | docs | 1KB | What it does, how to run, expected output |
| CREATE | examples/02_build_cli/README.md | docs | 1KB | Using /build from CLI to produce an artifact |
| CREATE | examples/02_build_cli/expected_output.md | docs | 2KB | What the artifact looks like |
| CREATE | examples/03_multi_nucleus_crew/main.py | code | 2KB | 3-nucleus crew: N01 research -> N04 document -> N06 price |
| CREATE | examples/03_multi_nucleus_crew/crew_template.md | crew_template | 2KB | The crew definition |
| CREATE | examples/03_multi_nucleus_crew/README.md | docs | 1KB | Explains crew pattern |
| CREATE | examples/04_knowledge_rag/main.py | code | 2KB | Build KC + retrieve + answer question |
| CREATE | examples/04_knowledge_rag/README.md | docs | 1KB | Knowledge pipeline explanation |
| CREATE | examples/05_grid_mission/main.py | code | 2KB | 6-nucleus grid dispatch on a mission |
| CREATE | examples/05_grid_mission/README.md | docs | 1KB | Grid dispatch explanation |

**Commit message**: `[N03] examples: 5 end-to-end patterns (agent, CLI, crew, RAG, grid)`

### Wave 6: CI Hardening + /consolidate Skill (N05 dispatch)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| REWRITE | .github/workflows/quality.yml:43 | ci | -- | Remove `\|\| true`, handle failure properly |
| CREATE | .github/workflows/test.yml | ci | 3KB | pytest on Python 3.10+ (Windows + Ubuntu) |
| REWRITE | .github/workflows/ci.yml | ci | -- | Add cex_doctor.py + example smoke tests |
| CREATE | .claude/skills/n07/consolidate.md | skill | 4KB | Full resource manager: processes + GPU + signals + verify |
| CREATE | .claude/skills/n07/dispatch_monitor.md | skill | 3KB | Non-blocking poll pattern: git log + status + VRAM check |
| REWRITE | .claude/commands/consolidate.md | command | 2KB | Wire to new consolidate skill |

**Commit message**: `[N05] CI hardening + /consolidate skill with GPU memory management`

### Wave 7: Final Polish (N07 direct)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| REWRITE | README.md | docs | -- | Final numbers, docs link, examples link, honest positioning |
| REWRITE | CLAUDE.md | docs | -- | Update counts to match reality |
| REWRITE | CONTRIBUTING.md | docs | -- | Verify accuracy, add "how to add a kind" section |
| CREATE | CHANGELOG.md | changelog | 3KB | v1.0.0 release notes |
| RUN | python _tools/cex_doctor.py | validation | -- | Full health check, must pass 100% |
| RUN | python _tools/cex_system_test.py | validation | -- | 54 tests, must pass |
| RUN | python _tools/cex_release_check.py | validation | -- | Release gate |
| TAG | git tag v1.0.0 | release | -- | Only after all gates pass |

**Commit message**: `[N07] v1.0.0 release: changelog, final README, doctor + system test pass`

---

## Wave Dependency Graph

```
W1 (audit commit)     -- no deps, do NOW
  |
W2 (repo hygiene)     -- depends on W1 committed
  |
  +-- W3 (EN translation)     -- independent, N04
  |
  +-- W4 (SDK docs)           -- independent, N04
  |
  +-- W5 (examples)           -- needs SDK API stable, N03
  |
  +-- W6 (CI + consolidate)   -- independent, N05
  |
  v
W7 (final polish)     -- depends on W3-W6 all complete
  |
  v
TAG v1.0.0
```

W3, W4, W5, W6 can run in parallel after W2.
W7 is the consolidation wave.

---

## Nucleus Assignment

| Wave | Nucleus | Why | Dispatch Mode |
|------|---------|-----|---------------|
| W1 | N07 (direct) | Commit existing changes, no build needed | manual |
| W2 | N07 (direct) | gitignore + git rm, orchestrator work | manual |
| W3 | N04 Knowledge | Translation is knowledge domain | solo |
| W4 | N04 Knowledge | Documentation is knowledge domain | solo |
| W5 | N03 Engineering | Code examples need builder expertise | solo |
| W6 | N05 Operations | CI/CD + skills are ops domain | solo |
| W7 | N07 (direct) | Final validation, tag, release | manual |

**Note**: W3+W4 both target N04. Run sequentially (W3 first, then W4) or
split into N04 (W3 translation) + N01 (W4 docs, research-oriented).

---

## Remaining Audit Findings NOT in This Spec

These are post-v1.0 items (LOW priority, tech debt):

| # | Finding | Why deferred |
|---|---------|-------------|
| C4 | Rotate API keys | Manual action by user, not automatable |
| L1 | 78% test coverage gap | Track, don't block release |
| L2 | 407 silent except patterns | Incremental, not blocking |
| L3 | Boot scripts Windows-only | Document in README, don't block |
| L4 | asyncio.get_event_loop() deprecated | 3 files, low risk |
| L5 | Bare except: in 2 files | Low risk |
| L6 | requirements.txt dev/prod split | Cosmetic |
| L7 | sdk-all missing sdk-litellm | Minor packaging gap |
| L8 | Stale handoff files accumulate | Add to /consolidate skill (W6) |
| L9 | 43 unlisted tools | Document post-launch |
| M8 | 3 duplicate write_signal() | Consolidate post-launch |
| M10 | Task file race in spawn_grid | Low frequency |
| M11 | CLAUDE.md sub-agent counts | Fixed in W1 |
| M12 | ISO count stale in 10+ files | Grep-and-replace post-W7 |
| M14 | CI || true (quality.yml) | Fixed in W6 |

---

## Resource Budget

| Wave | Est. Time | Token Cost | GPU Impact |
|------|-----------|-----------|------------|
| W1 | 5 min | 0 (commit only) | none |
| W2 | 15 min | 0 (git ops only) | none |
| W3 | 30 min | ~50K tokens (N04 solo) | none |
| W4 | 45 min | ~80K tokens (N04 solo) | none |
| W5 | 45 min | ~80K tokens (N03 solo) | none |
| W6 | 30 min | ~50K tokens (N05 solo) | none |
| W7 | 15 min | ~20K tokens (validation) | none |
| **Total** | **~3 hours** | **~280K tokens** | **zero GPU** |

All waves use Claude (no Ollama needed). No grid dispatch -- solo sequential
is more token-efficient for this scope (7 waves, no parallelism needed within waves).

---

## Acceptance Criteria

### Per-Wave Gates

- [ ] W1: `git diff --stat HEAD` shows 0 uncommitted audit changes
- [ ] W2: `git ls-files .cex/cache/ .cex/benchmarks/ .cex/skills/compiled/ n0?_task.md _docs/archive/` returns empty
- [ ] W3: `grep -rl 'missao\|visao\|Acao principal\|Valida todo\|orquestracao de alto' _docs/ --include='*.md' --include='*.yaml'` returns empty
- [ ] W4: `ls docs/{quickstart,concepts,cli-reference,sdk-reference,glossary,faq}.md` all exist
- [ ] W5: `ls examples/0{1,2,3,4,5}_*/README.md` all exist; `python examples/01_hello_agent/main.py` runs without error
- [ ] W6: `grep -r '|| true' .github/workflows/` returns only intentional cases; `.claude/skills/n07/consolidate.md` exists
- [ ] W7: `python _tools/cex_doctor.py` passes; `python _tools/cex_release_check.py` passes

### Final Gate (v1.0.0 tag)

- [ ] All 7 wave gates pass
- [ ] `git status` is clean (no uncommitted changes)
- [ ] README.md accurately reflects: 300 kinds, 301 builders, 3,647 ISOs, 148 tools, 4 runtimes
- [ ] No PT-BR in executable code or public docs (except bilingual intent tables)
- [ ] No tracked secrets, binary media, or machine-specific data
- [ ] CHANGELOG.md exists with v1.0.0 entry
- [ ] `git tag v1.0.0` applied

---

## Competitive Positioning (embedded in docs)

CEX is NOT "CrewAI but better." Different category:

| If you need... | Use |
|----------------|-----|
| Quick multi-agent prototype (20 lines) | CrewAI |
| Production state machine for agents | LangGraph |
| Minimal OpenAI wrapper | OpenAI Agents SDK |
| **Typed knowledge infrastructure that scales to 300 kinds, learns from every execution, and runs on 4 LLM runtimes** | **CEX** |

This positioning must appear in: README.md, docs/faq.md, examples/README.md.

---

## Post-v1.0 Roadmap (NOT in this spec)

1. Documentation site (Docusaurus or MkDocs)
2. TypeScript SDK
3. Cross-platform boot scripts (bash equivalents)
4. Durable checkpoints with mission resume
5. Tool marketplace / discovery UI
6. Community Discord
7. Video walkthrough (10 min)
8. Model benchmarking command (`/bench`)
9. 78% test coverage gap closure (L1)
