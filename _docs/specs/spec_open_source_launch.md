---
id: spec_open_source_launch
kind: constraint_spec
pillar: P06
title: "Spec -- Open Source Launch: Security + Hygiene + 300 Kinds + EN Sweep"
version: 1.0.0
created: 2026-04-23
author: n07_orchestrator
domain: launch_readiness
quality_target: 9.0
status: SPEC
scope: N07 + N03 + N04 + N05
depends_on: [plan_300_kinds]
tags: [launch, security, hygiene, kinds, i18n, open-source]
tldr: "5-wave mission: secure, clean, expand to 300 kinds, translate to EN, validate"
density_score: 0.95
updated: "2026-04-23"
---

# Open Source Launch

## Problem

CEXAI is going public. The repo has:
- 580MB+ of runtime artifacts from 11 days of development (handoffs, signals, logs)
- 109/293 kind boundary fields in Portuguese (global repo = EN only)
- 300 kinds (marketing wants 300 — 7 Karpathy-aligned gaps identified)
- Example fake emails in template artifacts (sarah.johnson@springfieldenergy.com etc.)
- No .cursorrules for Cursor/Codex users
- .playwright-mcp/ console logs: 216MB

The code is clean (.env never committed, .gitignore correct). But the repo is not
presentation-ready for the global developer community.

## Vision

A repo that is:
1. **Secure** — zero secrets in history, zero real names
2. **Clean** — zero runtime artifacts, zero logs, zero stale handoffs
3. **Complete** — 300 typed kinds (Karpathy-aligned ML infrastructure)
4. **Global** — all metadata in English, cross-runtime docs generated
5. **Verified** — doctor passes, system test passes, counts match

## Current State

| Metric | Current | Target |
|--------|---------|--------|
| Kinds | 293 | 300 |
| Builders | 298 | 305 |
| Sub-agents | 294 | 301 |
| KCs | 302 | 309 |
| PT-BR boundary fields | 109 | 0 |
| Runtime artifact files | ~1,900 | 0 |
| Runtime artifact size | ~580MB | 0 |
| Fake example emails | 5 files | 0 |
| .cursorrules | missing | generated |

## The 7 New Kinds (Karpathy-Aligned)

| # | Kind | Pillar | Description | llm_function | depends_on |
|---|------|--------|-------------|-------------|------------|
| 1 | `retrieval_evaluator` | P07 | RAG-specific IR eval metrics (MRR, NDCG, precision@k) | GOVERN | [eval_metric, benchmark, retriever_config] |
| 2 | `synthetic_data_config` | P01 | Synthetic training data generation pipeline config | CONSTRAIN | [dataset_card, eval_dataset] |
| 3 | `tokenizer_config` | P09 | BPE/sentencepiece/tiktoken tokenizer parameters | CONSTRAIN | [embedding_config, model_provider] |
| 4 | `distillation_config` | P02 | Teacher-student model compression setup | CONSTRAIN | [finetune_config, quantization_config, model_card] |
| 5 | `inference_config` | P09 | Temperature, top_p, sampling, stop sequences, penalties | CONSTRAIN | [model_provider, thinking_config, streaming_config] |
| 6 | `query_optimizer` | P01 | Query rewriting, expansion, multi-hop decomposition for RAG | CALL | [search_strategy, retriever_config, rag_source] |
| 7 | `curriculum_config` | P07 | Training data ordering, difficulty scheduling, adaptive pacing | CONSTRAIN | [dataset_card, training_method, eval_metric] |

## Decisions (from user + manifest)

- Language: EN only across all new and edited artifacts
- No real names or third-party brand names in any artifact
- Kinds selection: Karpathy-aligned (ML infrastructure focus)
- Verticalization: out of scope (base kinds only)
- Continuous batching: not needed (5 sequential waves in 1 mission)
- .cursorrules: generate via cex_compile.py --target cursorrules
- Runtime purge: full delete (not archive)
- Learning records: review then purge
- Cache: keep (pre-compiled builders, needed for runtime)

## Artifacts

### Wave 1: SECURITY_GATE (N07, 0 new artifacts)

Pre-flight security verification. No new files — audit only.

| Action | Target | Check | Pass Criteria |
|--------|--------|-------|---------------|
| VERIFY | `.env` | Never committed to git history | `git log --all -- .env` returns empty |
| VERIFY | `.gitignore` | Contains `.env`, `.playwright-mcp/`, `.venv*/` | All 3 present |
| SCAN | `**/*.py` `**/*.ps1` `**/*.md` | No hardcoded API keys (sk-ant-, sk-proj-, gsk_, github_pat_) | 0 matches outside .env |
| SCAN | `**/*.md` `**/*.yaml` | No real person emails (exclude example.com, placeholder) | 0 real email domains |
| VERIFY | `.aider.chat.history.md` | Contains session history — must delete | File removed |

Command:
```bash
git log --all -- .env
grep -rn "sk-ant-\|sk-proj-\|gsk_\|github_pat_\|csk-" --include="*.py" --include="*.ps1" --include="*.yaml" .
```

### Wave 2: REPO_HYGIENE (N07, 0 new artifacts — deletions only)

| Action | Path | Files | Size | Notes |
|--------|------|-------|------|-------|
| DELETE | `.playwright-mcp/` | 100+ | 216MB | Console logs from CDP sessions |
| DELETE | `.cex/runtime/handoffs/*.md` | 14 | 40KB | Old dispatch handoffs |
| DELETE | `.cex/runtime/signals/*.json` | 13 | 26KB | Completion signals |
| DELETE | `.cex/runtime/pids/*.txt` | 9 | 6KB | Spawn PID tracking |
| DELETE | `.cex/runtime/logs/` | ~50 | 90KB | Wave/overnight logs |
| DELETE | `.cex/runtime/out/` | ~30 | 283KB | Test run outputs |
| DELETE | `.cex/runtime/traces/` | ~60 | 257KB | Execution traces |
| DELETE | `.cex/runtime/crews/` | ~70 | 300KB | Crew execution records |
| DELETE | `.cex/archive/` | 7+ | 639KB | Archived handoffs |
| DELETE | `.cex/overnight/` | ~20 | 4.7MB | Overnight job logs |
| DELETE | `.cex/experiments/` | 2 | <1KB | Experiment tracking |
| DELETE | `.cex/system_test_results.json` | 1 | <1KB | Stale test snapshot |
| DELETE | `.aider.chat.history.md` | 1 | 13KB | Aider session history |
| REVIEW+DELETE | `.cex/learning_records/` | 39 | ~1MB | Check for PII, then purge |
| KEEP | `.cex/cache/` | 125 | 8.5MB | Pre-compiled builders (needed) |
| KEEP | `.cex/runtime/decisions/` | 3 | 16KB | Decision manifests (reusable) |
| GITIGNORE | `.cex/runtime/handoffs/` | -- | -- | Add to .gitignore |
| GITIGNORE | `.cex/runtime/signals/` | -- | -- | Add to .gitignore |
| GITIGNORE | `.cex/runtime/pids/` | -- | -- | Add to .gitignore |
| GITIGNORE | `.cex/runtime/logs/` | -- | -- | Add to .gitignore |
| GITIGNORE | `.cex/runtime/out/` | -- | -- | Add to .gitignore |
| GITIGNORE | `.cex/runtime/traces/` | -- | -- | Add to .gitignore |
| GITIGNORE | `.cex/runtime/crews/` | -- | -- | Add to .gitignore |
| GITIGNORE | `.playwright-mcp/` | -- | -- | Add to .gitignore |
| GITIGNORE | `.cex/overnight/` | -- | -- | Add to .gitignore |

Post-purge commit: `[N07] repo hygiene: purge 580MB runtime artifacts for open-source launch`

### Wave 3: KINDS_300 (N07 → N03 + N04, 112 new artifacts)

#### W3.1: Registration (N07, 7 edits)

| Action | Path | Kind | Notes |
|--------|------|------|-------|
| EDIT | `.cex/kinds_meta.json` | -- | Add 7 entries with EN boundaries |
| EDIT | `N00_genesis/P01_knowledge/_schema.yaml` | -- | Add synthetic_data_config, query_optimizer |
| EDIT | `N00_genesis/P02_model/_schema.yaml` | -- | Add distillation_config |
| EDIT | `N00_genesis/P07_evals/_schema.yaml` | -- | Add retrieval_evaluator, curriculum_config |
| EDIT | `N00_genesis/P09_config/_schema.yaml` | -- | Add tokenizer_config, inference_config |
| EDIT | `N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md` | -- | Add 7 kind entries (PT+EN patterns) |

#### W3.2: Knowledge Cards (N04, 7 new files)

| Action | Path | Kind | Est. Size |
|--------|------|------|-----------|
| CREATE | `N00_genesis/P01_knowledge/library/kind/kc_retrieval_evaluator.md` | knowledge_card | 3KB |
| CREATE | `N00_genesis/P01_knowledge/library/kind/kc_synthetic_data_config.md` | knowledge_card | 3KB |
| CREATE | `N00_genesis/P01_knowledge/library/kind/kc_tokenizer_config.md` | knowledge_card | 3KB |
| CREATE | `N00_genesis/P01_knowledge/library/kind/kc_distillation_config.md` | knowledge_card | 3KB |
| CREATE | `N00_genesis/P01_knowledge/library/kind/kc_inference_config.md` | knowledge_card | 3KB |
| CREATE | `N00_genesis/P01_knowledge/library/kind/kc_query_optimizer.md` | knowledge_card | 3KB |
| CREATE | `N00_genesis/P01_knowledge/library/kind/kc_curriculum_config.md` | knowledge_card | 3KB |

#### W3.3: Builder ISOs (N03, 84 new files)

For each of the 7 kinds, create 12 ISOs (1:1 with pillars):

| ISO | Pillar | Naming |
|-----|--------|--------|
| `bld_knowledge_{kind}.md` | P01 | Knowledge context |
| `bld_model_{kind}.md` | P02 | Builder identity |
| `bld_prompt_{kind}.md` | P03 | Prompt instructions |
| `bld_tools_{kind}.md` | P04 | Available tools |
| `bld_output_{kind}.md` | P05 | Output format |
| `bld_schema_{kind}.md` | P06 | Schema constraints |
| `bld_eval_{kind}.md` | P07 | Evaluation criteria |
| `bld_architecture_{kind}.md` | P08 | Architecture context |
| `bld_config_{kind}.md` | P09 | Config patterns |
| `bld_memory_{kind}.md` | P10 | Memory patterns |
| `bld_feedback_{kind}.md` | P11 | Feedback loops |
| `bld_orchestration_{kind}.md` | P12 | Orchestration rules |

Paths: `archetypes/builders/{kind}-builder/bld_{pillar}_{kind}.md`

Total: 7 kinds x 12 ISOs = 84 files

Template source: use existing kind with same llm_function as reference
- GOVERN kinds: copy structure from `eval_metric-builder/`
- CONSTRAIN kinds: copy structure from `embedding_config-builder/`
- CALL kinds: copy structure from `search_strategy-builder/`

#### W3.4: Sub-agent Definitions (N03, 7 new files)

| Action | Path | Est. Size |
|--------|------|-----------|
| CREATE | `.claude/agents/retrieval-evaluator-builder.md` | 1KB |
| CREATE | `.claude/agents/synthetic-data-config-builder.md` | 1KB |
| CREATE | `.claude/agents/tokenizer-config-builder.md` | 1KB |
| CREATE | `.claude/agents/distillation-config-builder.md` | 1KB |
| CREATE | `.claude/agents/inference-config-builder.md` | 1KB |
| CREATE | `.claude/agents/query-optimizer-builder.md` | 1KB |
| CREATE | `.claude/agents/curriculum-config-builder.md` | 1KB |

Template: use `archetypes/builders/_shared/agent_template.md` or copy from existing.

### Wave 4: EN_SWEEP (N07 + N04, edits only)

#### W4.1: kinds_meta.json EN translation (N07, 1 file edit)

Translate all 109 PT-BR `boundary` fields to English.
Source: `.cex/kinds_meta.json`

Example transform:
```
BEFORE: "boundary": "Definicao completa de agente (persona + capabilities). NAO eh skill..."
AFTER:  "boundary": "Complete agent definition (persona + capabilities). NOT a skill..."
```

Rules:
- "NAO eh" → "NOT a"
- "Definicao" → "Definition"
- "Tarefa especifica" → "Specific task"
- Keep technical terms (pillar IDs, kind names) unchanged
- All new text must be ASCII-only (per ascii-code-rule.md)

#### W4.2: Fake names cleanup (N07, 4 file edits)

| Action | Path | Change |
|--------|------|--------|
| EDIT | `archetypes/builders/agent-profile-builder/bld_config_agent_profile.md` | Replace sarah.johnson@ etc. with generic user@example.com |
| EDIT | `archetypes/builders/compiled/bld_config_agent_profile.yaml` | Same |
| EDIT | `N00_genesis/P01_knowledge/library/kind/kc_press_release.md` | Replace real-sounding names with generic |
| EDIT | `N00_genesis/P01_knowledge/library/compiled/kc_press_release.yaml` | Same |

#### W4.3: Generate .cursorrules (N05, 1 new file)

```bash
python _tools/cex_compile.py --target cursorrules --output .cursorrules
```

If compiler target not ready, manually create `.cursorrules` from CLAUDE.md subset
(core rules: 8F, dispatch, quality gates — without Claude-specific commands).

#### W4.4: Counter updates (N07, 2 file edits)

| Action | Path | Changes |
|--------|------|---------|
| EDIT | `README.md` | 293→300 (6 occurrences), builder count update |
| EDIT | `CLAUDE.md` | 293→300 (4 occurrences), 298→301 builders, 3563→3647 ISOs, 294→301 sub-agents |

### Wave 5: VALIDATE (N05, 0 new artifacts)

| Action | Command | Pass Criteria |
|--------|---------|---------------|
| RUN | `python _tools/cex_doctor.py` | All checks PASS |
| RUN | `python _tools/cex_system_test.py` | 54+ tests PASS |
| RUN | `python _tools/cex_sanitize.py --check --scope _tools/` | 0 non-ASCII in code |
| VERIFY | `python -c "import json; print(len(json.load(open('.cex/kinds_meta.json'))))"` | Output: 300 |
| VERIFY | `ls archetypes/builders/ \| wc -l` | Output: 305 |
| VERIFY | `ls .claude/agents/*-builder.md \| wc -l` | Output: 301 |
| VERIFY | `ls N00_genesis/P01_knowledge/library/kind/kc_*.md \| wc -l` | Output: 309 |
| VERIFY | `grep -c "293" README.md CLAUDE.md` | Output: 0 (no stale references) |
| VERIFY | PT-BR scan on kinds_meta.json | 0 Portuguese boundary fields |
| COMPILE | `python _tools/cex_compile.py --all` | All new artifacts compiled |
| COMMIT | Final validation commit | `[N07] open source launch: 300 kinds, EN-only, clean` |

## Dependencies

```
W1: SECURITY_GATE (N07 solo)
 |
 v
W2: REPO_HYGIENE (N07 solo)
 |
 v
W3: KINDS_300
 |-- W3.1: Registration (N07 solo, sequential)
 |-- W3.2: Knowledge Cards (N04, after W3.1)  ---|
 |-- W3.3: Builder ISOs (N03, after W3.1)     ---|- PARALLEL
 |-- W3.4: Sub-agents (N03, after W3.3)       ---|
 |
 v
W4: EN_SWEEP
 |-- W4.1: kinds_meta EN translation (N07)
 |-- W4.2: Fake names cleanup (N07)
 |-- W4.3: Generate .cursorrules (N05)  --- PARALLEL with W4.1-W4.2
 |-- W4.4: Counter updates (N07, after W3 + W4.1)
 |
 v
W5: VALIDATE (N05 solo)
```

## Estimated Effort

| Wave | Nucleus | New Files | Edits | Deletions | Est. Time |
|------|---------|-----------|-------|-----------|-----------|
| W1 | N07 | 0 | 0 | 1 | 5 min |
| W2 | N07 | 0 | 1 (.gitignore) | ~1,900 | 15 min |
| W3 | N07+N03+N04 | 98 | 6 | 0 | 60 min |
| W4 | N07+N05 | 1 | 7 | 0 | 30 min |
| W5 | N05 | 0 | 0 | 0 | 15 min |
| **Total** | **4 nuclei** | **99** | **14** | **~1,900** | **~2 hrs** |

## Risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Git contention in W3 (N03 + N04 parallel) | LOW | Different directories, no overlap |
| ISO quality variance (84 files) | MED | N03 uses template from same llm_function kind |
| Counter drift if other work lands between waves | LOW | W4.4 reads actual count, never hardcodes |
| .cursorrules compiler target not implemented | LOW | Manual creation fallback from CLAUDE.md |
| PT-BR missed in non-boundary fields | MED | W5 validation grep catches remaining |
| 109 boundary translations introduce errors | MED | Batch translate with consistent glossary |

## Done When

- [ ] `.env` verified never committed
- [ ] Zero hardcoded secrets in source
- [ ] Zero runtime artifacts in tracked files
- [ ] .gitignore updated for runtime dirs
- [ ] 300 kinds in kinds_meta.json
- [ ] 305 builder directories
- [ ] 301 sub-agent definitions
- [ ] 309 knowledge cards
- [ ] 84 new builder ISOs (7 x 12)
- [ ] Prompt compiler has all 300 kind patterns
- [ ] 4 pillar schemas updated
- [ ] 0 PT-BR boundary fields in kinds_meta.json
- [ ] 0 fake person emails in artifacts
- [ ] .cursorrules exists
- [ ] README.md shows 300 kinds everywhere
- [ ] CLAUDE.md shows 300 kinds, 301 builders, 3647 ISOs
- [ ] cex_doctor passes
- [ ] cex_system_test passes
- [ ] cex_sanitize passes
- [ ] All new artifacts compiled
- [ ] Final commit tagged
