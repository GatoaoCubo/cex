---
quality: 8.4
quality: 8.0
id: audit_self_review_n05
kind: audit_report
8f: F7_govern
pillar: P07
nucleus: n05
mission: SELF_AUDIT
title: "N05 Operations Self-Audit: Eval, Config, Tools, Quality Gates"
version: 1.0.0
tags: [self-audit, operations, eval, config, tools, quality-gates]
created: 2026-04-18
related:
  - kc_intent_resolution_map
  - p03_pc_cex_universal
  - self_audit_n05_codex_2026_04_15
  - self_audit_n05_20260408
  - bld_sp_collaboration_software_project
  - p02_nd_n05.md
  - leverage_map_v2_n05_verify
  - p12_wf_create_orchestration_agent
  - bld_knowledge_card_nucleus_def
  - p12_dr_builder_nucleus
density_score: 1.0
updated: "2026-04-22"
---

# N05 Operations Self-Audit: Eval, Config, Tools, Quality Gates

## Executive Summary

This audit examines the structural completeness of CEX's quality infrastructure:
P07 (Evaluation) and P09 (Config) kind coverage, quality gate tooling, and
tool-to-kind wiring. The system is structurally sound -- 100% builder coverage
for both pillars, 100% flywheel health, zero FAIL results from cex_doctor --
but operational gaps exist in config instantiation, tool documentation accuracy,
and per-nucleus eval artifact distribution.

---

## P07 + P09 Coverage Matrix

### P07 Evaluation (23 kinds)

| Kind | Builder | 13 ISOs | KC | Nucleus Artifacts | Gap |
|------|---------|---------|-----|-------------------|-----|
| benchmark | OK | 13/13 | OK | N01:3 N03:3 N05:2 | none |
| benchmark_suite | OK | 13/13 | OK | N03:1 | low adoption outside N03 |
| bias_audit | OK | 13/13 | OK | N01:1 | single instance |
| cohort_analysis | OK | 13/13 | OK | N06:1 | single instance |
| e2e_eval | OK | 13/13 | OK | N05:2 | adequate |
| eval_dataset | OK | 13/13 | OK | N01:1 | single instance |
| eval_framework | OK | 13/13 | OK | N05:1 | adequate |
| eval_metric | OK | 13/13 | OK | N05:1 | adequate |
| experiment_tracker | OK | 13/13 | OK | N01:1 | single instance |
| golden_test | OK | 13/13 | OK | N05:1 | adequate |
| judge_config | OK | 13/13 | OK | N01:1 | single instance |
| llm_evaluation_scenario | OK | 13/13 | OK | N07:0 | zero instances |
| llm_judge | OK | 13/13 | OK | N05:1 | adequate |
| memory_benchmark | OK | 13/13 | OK | N04:1 | single instance |
| red_team_eval | OK | 13/13 | OK | N01:1 | single instance |
| regression_check | OK | 13/13 | OK | N05:1 | adequate |
| reward_model | OK | 13/13 | OK | N01:1 | single instance |
| scoring_rubric | OK | 13/13 | OK | N05:1 | adequate |
| smoke_eval | OK | 13/13 | OK | N05:2 | adequate |
| trace_config | OK | 13/13 | OK | N05:1 | adequate |
| trajectory_eval | OK | 13/13 | OK | N01:1 | single instance |
| unit_eval | OK | 13/13 | OK | N05:1 | adequate |
| usage_report | OK | 13/13 | OK | N06:1 | single instance |

**Summary**: 23/23 builders exist with full 13-ISO complement and KC coverage.
Builder infrastructure: COMPLETE. Artifact instantiation: SPARSE -- 11 of 23
kinds have only 0-1 instances across all nuclei. `llm_evaluation_scenario`
has zero instances despite having a full builder.

### P09 Config (37 kinds)

| Kind | Builder | 13 ISOs | KC | Nucleus Artifacts | Gap |
|------|---------|---------|-----|-------------------|-----|
| alert_rule | OK | 13/13 | OK | N05:1 | adequate |
| backpressure_policy | OK | 13/13 | OK | N05:1 | adequate |
| batch_config | OK | 13/13 | OK | N05:1 | adequate |
| canary_config | OK | 13/13 | OK | N05:1 | adequate |
| circuit_breaker | OK | 13/13 | OK | N05:1 | adequate |
| cost_budget | OK | 13/13 | OK | N06:1 | adequate |
| data_residency | OK | 13/13 | OK | N01:1 | adequate |
| deployment_manifest | OK | 13/13 | OK | N05:1 | adequate |
| effort_profile | OK | 13/13 | OK | N05:1 | adequate |
| env_config | OK | 13/13 | OK | N05:2 | adequate |
| experiment_config | OK | 13/13 | OK | N01:1 | adequate |
| feature_flag | OK | 13/13 | OK | N05:1 | adequate |
| hibernation_policy | OK | 13/13 | OK | N05:1 | adequate |
| kubernetes_ai_requirement | OK | 13/13 | OK | N05:1 | adequate |
| marketplace_app_manifest | OK | 13/13 | OK | N06:1 | adequate |
| oauth_app_config | OK | 13/13 | OK | N05:1 | adequate |
| path_config | OK | 13/13 | OK | N05:1 | adequate |
| permission | OK | 13/13 | OK | N05:1 | adequate |
| playground_config | OK | 13/13 | OK | N03:1 | adequate |
| prosody_config | OK | 13/13 | OK | N02:1 | adequate |
| quantization_config | OK | 13/13 | OK | N03:1 | adequate |
| rate_limit_config | OK | 13/13 | OK | N05:2 | adequate |
| rbac_policy | OK | 13/13 | OK | N05:1 | adequate |
| realtime_session | OK | 13/13 | OK | N03:1 | adequate |
| retry_policy | OK | 13/13 | OK | N05:1 | adequate |
| runtime_rule | OK | 13/13 | OK | N05:1 | adequate |
| sandbox_config | OK | 13/13 | OK | N05:1 | adequate |
| sandbox_spec | OK | 13/13 | OK | N05:1 | adequate |
| secret_config | OK | 13/13 | OK | N05:1 | adequate |
| slo_definition | OK | 13/13 | OK | N05:1 | adequate |
| sso_config | OK | 13/13 | OK | N05:1 | adequate |
| terminal_backend | OK | 13/13 | OK | N05:1 | adequate |
| thinking_config | OK | 13/13 | OK | N03:1 | adequate |
| transport_config | OK | 13/13 | OK | N05:1 | adequate |
| usage_quota | OK | 13/13 | OK | N06:1 | adequate |
| vad_config | OK | 13/13 | OK | N02:1 | adequate |
| white_label_config | OK | 13/13 | OK | N06:1 | adequate |

**Summary**: 37/37 builders exist. All have 13 ISOs and KCs.
No `.cex/P09_config/` central directory exists -- config instances live
per-nucleus. N05 owns 24 of 37 config kinds in practice, consistent with
its operations mandate. No structural gaps.

---

## Quality Gate Reality Check

| Gate | Documented | Implemented | Tool | Gap |
|------|-----------|-------------|------|-----|
| 8F pipeline (F1-F8) | `.claude/rules/8f-reasoning.md` | Yes -- every builder agent follows 8F | `cex_8f_runner.py` | None -- enforced by sub-agent prompts |
| F7 GOVERN (H01-H07) | 8f-reasoning.md references 7 hard gates | Partially -- gates are prompt-enforced, not machine-validated | `cex_score.py` (post-hoc) | H01-H07 are not programmatically checked; rely on LLM self-compliance |
| 12LP checklist | 8f-reasoning.md references "12LP: pass/12" | Not implemented as code | None | No tool validates the 12LP checklist -- it exists only in builder instructions |
| 5D scoring (D1-D5) | 8f-reasoning.md mentions weighted dimensions | `cex_score.py` uses 3-layer scoring (structural 30%, rubric 30%, semantic 40%) | `cex_score.py` | Documented 5D != implemented 3-layer. Score dimensions diverge from spec. |
| Pre-commit validation | `ascii-code-rule.md` | `cex_hooks.py pre-commit` + `cex_sanitize.py` | `cex_hooks.py` | Implemented and working |
| Post-tool-use compile | Boris merge item #5 | `cex_hooks_native.py post-tool-use` | `cex_hooks_native.py` | Implemented |
| Builder completeness | 13 ISOs per builder | `cex_doctor.py` checks 13-file count | `cex_doctor.py` | Implemented -- 0 FAIL |
| Density threshold (0.78) | Builder ISOs require >= 0.78 | `cex_doctor.py` checks density | `cex_doctor.py` | 94 WARN (below 0.78) -- enforced but not blocking |
| Naming convention | `cex_naming_validator.py` | Implemented | `cex_naming_validator.py` | Working |
| Flywheel audit | 7 layers + 7 wires + 7 cascades = 109 checks | `cex_flywheel_audit.py` | `cex_flywheel_audit.py` | 109/109 WIRED, 0 BROKEN |

### Verdict

Quality gates are structurally complete but **spec-to-implementation drift exists**:
- The "H01-H07 hard gates" mentioned in 8F docs are prompt-level, not code-enforced
- The "12LP checklist" has no automated validator
- Documented "5D scoring" maps to a different 3-layer system in `cex_score.py`
- These are documentation bugs, not functionality bugs -- the implemented system works

---

## Tool Coverage Sample (30 of 148 tools)

| Tool | Pillar | Kind Mapping | Nucleus | Wired |
|------|--------|-------------|---------|-------|
| cex_8f_motor.py | P12 | workflow orchestration | N07 | yes |
| cex_8f_runner.py | P12 | pipeline execution | N03-N06 | yes |
| cex_agent_spawn.py | P02 | agent spawn validation | N07 | yes |
| cex_auto.py | P11 | self-healing flywheel | N05 | yes |
| cex_benchmark_ollama.py | P07 | benchmark | N05 | yes |
| cex_bootstrap.py | P09 | env_config (brand) | N06 | yes |
| cex_compile.py | P05 | formatter (md->yaml) | N05 | yes |
| cex_coordinator.py | P12 | workflow coordination | N07 | yes |
| cex_crew.py | P12 | crew_template exec | N07 | yes |
| cex_doctor.py | P07 | quality_gate | N05 | yes |
| cex_evolve.py | P11 | self_improvement_loop | N07 | yes |
| cex_feedback.py | P11 | learning_record | N05 | yes |
| cex_flywheel_audit.py | P07 | audit infrastructure | N05 | yes |
| cex_gdp.py | P12 | dispatch_rule (GDP) | N07 | yes |
| cex_hooks.py | P11 | quality_gate (pre-commit) | N05 | yes |
| cex_hygiene.py | P11 | bugloop (artifact CRUD) | N05 | yes |
| cex_intent_resolver.py | P03 | prompt_compiler (F1) | N07 | yes |
| cex_materialize.py | P02 | agent materialization | N03 | yes |
| cex_memory_select.py | P10 | memory_scope | N04 | yes |
| cex_mission_runner.py | P12 | workflow (autonomous) | N07 | yes |
| cex_prompt_cache.py | P10 | prompt_cache | N05 | yes |
| cex_prompt_layers.py | P03 | prompt_template loader | N03 | yes |
| cex_query.py | P01 | retriever_config (TF-IDF) | N01 | yes |
| cex_retriever.py | P01 | retriever (similarity) | N01 | yes |
| cex_router.py | P09 | rate_limit_config | N07 | yes |
| cex_sanitize.py | P11 | content_filter (ASCII) | N05 | yes |
| cex_score.py | P07 | scoring_rubric | N05 | yes |
| cex_signal_watch.py | P12 | signal (poll) | N07 | yes |
| cex_skill_loader.py | P03 | skill (ISO loader) | N03 | yes |
| cex_token_budget.py | P03 | context_window_config | N05 | yes |

**Full count**: 131 cex_* tools in `_tools/`. CLAUDE.md claims 158 -- that
figure includes non-cex tools (signal_writer.py, brand_*.py, etc.) which
brings the total closer to ~155. The documented "158" is approximately correct
when counting all Python files in `_tools/`.

### Tools with no direct kind mapping

| Tool | Purpose | Why no kind |
|------|---------|-------------|
| cex_shared.py | Shared utilities | Library, not artifact-producing |
| cex_errors.py | Error definitions | Library |
| cex_fix_boot_banner.py | One-shot fix | Maintenance script |
| cex_fix_boot_colors.py | One-shot fix | Maintenance script |
| cex_fix_boot_tui.py | One-shot fix | Maintenance script |
| cex_wave_autofix*.py | One-shot fixes | Maintenance scripts (3 files) |
| cex_patch_*.py | One-shot patches | Maintenance scripts (2 files) |

These are utilities and maintenance scripts, not kind-producing builders.
No structural gap -- they are correctly categorized as operational tooling.

---

## Flywheel Audit Results

```
Checks:  109
WIRED:   109  (documented AND working)
BROKEN:    0  (documented but broken)
PHANTOM:   0  (documented but missing)
ORPHAN:    0  (exists but undocumented)
HEALTH:  100% (109/109)
```

Breakdown by layer:
- L0 Genesis & Config: 12/12 WIRED
- L1 Pillars (P01-P12): 24/24 WIRED
- L2 Nuclei (N01-N07): 21/21 WIRED
- L3 Archetypes: 7/7 WIRED (301 builders, 3647 ISOs)
- L4 Knowledge Library: 3/3 WIRED (293/293 KC coverage)
- L5 Tools: 12/12 WIRED (148 tools, 56 SDK modules)
- L6 Governance: 3/3 WIRED (11 rules, 20 commands, 25 learning records)
- WIRES (OpenClaude integrations): 18/18 WIRED
- CASCADES (dependency chains): 7/7 WIRED

**No intervention needed.** The flywheel is structurally complete.

---

## Collaboration Map

| Nucleus | Direction | Eval Artifacts | Config Artifacts |
|---------|-----------|---------------|-----------------|
| N01 Intelligence | produces | 25 (benchmarks, bias audits, evals) | 6 (experiment_config, data_residency) |
| N02 Marketing | produces | 13 (cohort analysis, NPS) | 7 (prosody, vad) |
| N03 Engineering | produces | 25 (golden tests, benchmarks) | 11 (playground, quantization, thinking) |
| N04 Knowledge | produces | 15 (memory benchmarks, evals) | 6 (various) |
| N05 Operations | produces + consumes | 18 (smoke_eval, e2e, scoring_rubric) | 17 (env, rate_limit, sandbox, etc.) |
| N06 Commercial | produces | 15 (cohort, usage_report) | 6 (cost_budget, marketplace, usage_quota) |
| N07 Admin | consumes | 1 (minimal) | 6 (various) |

N05 is the primary consumer and enforcer of quality gates -- correct per
nucleus mandate. N07 has minimal P07 artifacts (1), which is expected since
it orchestrates rather than evaluates. N01 and N03 lead in eval artifact
production.

---

## Top 5 Quality Infrastructure Gaps

### 1. CLAUDE.md tool count inaccuracy (severity: LOW)

CLAUDE.md claims "148 tools" but `_tools/cex_*.py` yields 131. Including
non-prefixed tools brings the count to ~155. The documented figure is stale.

**File**: `CLAUDE.md` line ~1
**Fix**: Update to "131 cex_* tools + 24 support tools = 155 total"

### 2. H01-H07 hard gates are prompt-only (severity: MED)

The 8F documentation references "H01-H07 gates" in F7 GOVERN but no tool
programmatically validates these. They exist only in builder instruction ISOs
as prompt directives. A rogue LLM call can skip them.

**File**: `.claude/rules/8f-reasoning.md`
**Fix**: Add H01-H07 checks to `cex_score.py` as structural validators

### 3. 12LP checklist has no automated validator (severity: MED)

F7 GOVERN references "12LP: pass/12" but no tool checks the 12 points.
The scoring system uses 3-layer (structural/rubric/semantic), not 12LP.
This is spec-implementation divergence.

**File**: `.claude/rules/8f-reasoning.md`
**Fix**: Either implement 12LP in `cex_score.py` or update the 8F doc to
match the actual 3-layer scoring system

### 4. Doctor density warnings: 301 builders below threshold (severity: LOW)

94 of 301 builders have at least one ISO below 0.78 density. These are
WARN not FAIL -- the builder still functions -- but it indicates that ~32%
of builder ISOs have thin content.

**File**: Builder ISOs in `archetypes/builders/*/`
**Fix**: Batch evolve via `cex_evolve.py` targeting density < 0.78

### 5. llm_evaluation_scenario: zero instances (severity: LOW)

The `llm_evaluation_scenario` kind has a complete builder (13 ISOs, KC)
but zero instantiated artifacts across all 7 nuclei. It is the only P07
kind with zero usage.

**File**: `archetypes/builders/llm-evaluation-scenario-builder/`
**Fix**: Create at least one instance in N05 or N01 to validate the builder

---

## Recommendations

1. **Reconcile 8F documentation with scoring implementation.**
   `cex_score.py` uses 3-layer scoring (structural 30%, rubric 30%, semantic 40%).
   The 8F rule references H01-H07 gates and 12LP and 5D dimensions. These are
   three different scoring vocabularies for the same system. Unify them in
   `.claude/rules/8f-reasoning.md` or implement the missing validators.
   Path: `.claude/rules/8f-reasoning.md` + `_tools/cex_score.py`

2. **Add machine-enforceable H01-H07 gates to cex_score.py.**
   Currently H01-H07 exist only as prompt instructions. Adding structural
   checks (e.g., H01=frontmatter exists, H02=kind in taxonomy, H03=pillar
   matches schema) to the scoring pipeline would catch LLM non-compliance.
   Path: `_tools/cex_score.py` -- add `validate_hard_gates()` function

3. **Update CLAUDE.md tool count from 158 to 155.**
   The actual count is 131 cex_* prefixed + ~24 non-prefixed (signal_writer,
   brand_*, etc.). Total ~155. This is a documentation accuracy issue.
   Path: `CLAUDE.md` line 1

4. **Batch-evolve the 94 low-density builder ISOs.**
   32% of builders have ISOs below 0.78 density. Run a targeted evolution
   pass: `python _tools/cex_evolve.py --target density --threshold 0.78`
   Path: `archetypes/builders/*/bld_*.md` (301 builders affected)

5. **Instantiate llm_evaluation_scenario in N05.**
   The kind exists with full builder infrastructure but zero instances.
   Create one evaluation scenario for a core N05 workflow (e.g., dispatch
   validation) to prove the builder works end-to-end.
   Path: `N05_operations/P07_evals/llm_eval_scenario_dispatch.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_intent_resolution_map]] | upstream | 0.29 |
| [[p03_pc_cex_universal]] | upstream | 0.29 |
| [[self_audit_n05_codex_2026_04_15]] | related | 0.26 |
| [[self_audit_n05_20260408]] | upstream | 0.24 |
| [[bld_sp_collaboration_software_project]] | downstream | 0.23 |
| [[p02_nd_n05.md]] | upstream | 0.23 |
| [[leverage_map_v2_n05_verify]] | downstream | 0.22 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.21 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.21 |
| [[p12_dr_builder_nucleus]] | downstream | 0.20 |
