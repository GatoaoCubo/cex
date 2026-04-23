---
id: hybrid_review4_n01
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW4 N01 Audit: trajectory_eval + self_improvement_loop + prompt_technique"
version: "1.0.0"
quality: 8.9
tags: [audit, hybrid_review4, wave3, trajectory_eval, self_improvement_loop, prompt_technique]
domain: "generator quality assurance"
created: "2026-04-14"
updated: "2026-04-14"
author: n01_intelligence
tldr: "39 ISOs audited (3 Wave 3 kinds). 16 defects found and fixed: 1 CRITICAL domain hallucination (trajectory_eval robotics contamination), 3 D02 memory kind errors, 2 D03 runtime quality gates, 5 D07 hallucinated tools, 3 D10 file reference drift, 2 citation errors. All 39/39 ISOs pass validator post-fix."
source_model: "qwen3:14b (Wave 3 via gen_v2)"
related:
  - n01_hybrid_review_wave1
  - n02_audit_action_paradigm_builder
  - hybrid_review4_n04
  - n01_audit_voice_pipeline_builder
  - hybrid_review7_n04
  - hybrid_review5_n01
  - n01_audit_realtime_session_builder
  - n02_audit_collaboration_pattern_builder
  - hybrid_review6_n02
  - hybrid_review6_n01
---

## Scope

| Builder | Risk | ISOs | Validator Pre | Validator Post |
|---------|------|------|--------------|----------------|
| trajectory_eval | HIGH | 13 | 12/13 FAIL | 13/13 PASS |
| self_improvement_loop | HIGH | 13 | 13/13 PASS | 13/13 PASS |
| prompt_technique | LOW | 13 | 13/13 PASS | 13/13 PASS |
| **TOTAL** | | **39** | **38/39** | **39/39** |

---

## Defects Found and Fixed

### trajectory_eval (CRITICAL -- 9 ISOs modified)

**Score pre-fix: ~4.5/10. Score post-fix: ~8.5/10.**

**D04 CRITICAL -- Domain hallucination (entire builder)**
- Root cause: qwen3:14b confused `trajectory_eval` (LLM agent step-level evaluation) with
  robotics/autonomous vehicle trajectory evaluation.
- Contaminated ISOs: knowledge_card, schema, quality_gate, output_template, tools
- Evidence: ISO 17380:2017 (Autonomous Vehicles), ROS 2, CARLA, Gazebo, jerk measurements,
  collision avoidance, start_point/end_point coordinate fields.
- Fix: Rebuilt 5 ISOs with correct domain: AgentBench, WebArena, SWE-bench, OSWorld,
  tau-bench; agent_id/task_id/step_count fields; step-log structure; failure root cause taxonomy.

**D02 -- Memory ISO kind=learning_record**
- bld_memory: kind=learning_record (id=p10_lr_*) -> kind=memory (id=p10_mem_*)
- Fix: Updated frontmatter kind + id + tags.

**D03+D06 -- Quality gate runtime metrics + wrong HARD gate IDs**
- HARD gate IDs were `.md` file paths (e.g. `p07_te_trajectory_coverage.md`) instead of H01-H07 pattern.
- Metrics: jerk, collision, smoothness (robotics runtime, not artifact structure).
- Fix: Rebuilt with H01-H07 artifact-structural checks; 5D soft scoring aligned to step-log completeness.

**D07 -- Hallucinated tools**
- Fake: cex_visualizer.py, cex_linter.py, cex_consistency_checker.py, cex_performance_analyzer.py
- Wrong domain: TrajectoryEval Framework, Waymo Open Dataset, CARLA Simulation
- Fix: Replaced with real CEX tools (cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py,
  cex_wave_validator.py, cex_hygiene.py) + correct benchmark references.

**D09 -- Architecture wrong pillars**
- bld_architecture listed ALL 13 ISOs as pillar=P07. Correct pillars vary (P03, P04, P05, P06, P08, P09, P10, P11).
- Fix: Rebuilt architecture with correct pillar per ISO and correct dependency graph.

**D10 -- File reference drift**
- bld_instruction: `SCHEMA.md` -> `bld_schema_trajectory_eval.md`, `OUTPUT_TEMPLATE.md` -> `bld_output_template_trajectory_eval.md`

**Validator FAIL (pre-fix)**
- bld_config: Missing domain keyword ('trajectory', 'sequence', 'step').
- Fix: Added "LLM agent step-level path analysis" to naming section.

---

### self_improvement_loop (HIGH -- 4 ISOs modified)

**Score pre-fix: ~6.5/10. Score post-fix: ~8.5/10.**

**D02 -- Memory ISO kind=learning_record**
- bld_memory: kind=learning_record -> kind=memory, id=p10_mem_*

**D03 -- Quality gate H04-H08 tests runtime system metrics**
- H04: learning_rate_stability >= 0.95 (runtime ML training metric, not artifact field)
- H05: feedback_loop_integrity == 100% (system operational metric)
- H06: model_drift_detection <= 0.1 (training metric)
- H07: training data freshness >= 90% (operational metric)
- H08: error recovery rate >= 99% (runtime metric)
- Fix: Rebuilt H04-H07 as artifact-structural checks (loop_stages count, metrics field,
  feedback_sources reference, safety guard documentation).

**D07 -- Hallucinated tools**
- Fake: cex_analyzer.py, cex_optimizer.py, cex_monitor.py, cex_stress_test.py
- Wrong expansion: "CEX Framework (Core Execution eXchange)" -- CEX is "Typed Knowledge System for LLM Agents"
- Fix: Replaced with real CEX tools + accurate external references (DSPy, STaR, Self-Refine, Constitutional AI).

**D10 -- File reference drift**
- bld_instruction: `SCHEMA.md` -> `bld_schema_self_improvement_loop.md`, `OUTPUT_TEMPLATE.md` -> `bld_output_template_self_improvement_loop.md`

**Citation issues fixed**
- RFC 8611 is a YANG data modeling RFC, NOT an ML metrics standard -- removed.
- "ML-Kits Framework (Google)" does not exist as a Google product -- removed.
- Added: STaR (Zelikman 2022), DSPy (Khattab 2023), Self-Refine (Madaan 2023), AlphaCode 2,
  Constitutional AI (Anthropic 2022).

---

### prompt_technique (LOW -- 4 ISOs modified)

**Score pre-fix: ~7.5/10. Score post-fix: ~8.8/10.**

**D02 -- Memory ISO kind=learning_record**
- bld_memory: kind=learning_record -> kind=memory, id=p10_mem_*

**D12 -- ASCII violations**
- bld_instruction: checkmark emojis in Phase 3 VALIDATE section (unicode U+2705)
- Fix: Replaced `- [ ] [checkmark]` -> `- [ ]`

**D07 -- Hallucinated tools**
- Fake: cex_optimizer.py, cex_analyzer.py, val_tester.py, val_benchmark.py, val_debugger.py, val_checker.py
- Fix: Replaced with real CEX tools (cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py,
  cex_prompt_optimizer.py, cex_wave_validator.py) + real paper references.

**D10 -- File reference drift**
- bld_instruction: `SCHEMA.md` -> `bld_schema_prompt_technique.md`, `OUTPUT_TEMPLATE.md` -> `bld_output_template_prompt_technique.md`
- Also corrected wrong function reference: `INJECT` -> `PRODUCE`

**Citation errors fixed**
- "Chain-of-Thought = Brown et al. 2020 (GPT-3 paper)" is WRONG. CoT is Wei et al. 2022.
- "Prompt Engineering Manifesto (OpenAI, 2023)" does not exist -- replaced with real reference.
- Added: ReAct (Yao 2022), Tree of Thoughts (Yao 2023), Self-Consistency (Wang 2022), Chain-of-Verification (Dhuliawala 2023).

---

## Defect Frequency vs. Master Systemic Defects

| Defect | Expected (master_systemic_defects.md) | Found in Wave 3 | Status |
|--------|--------------------------------------|-----------------|--------|
| D01 system_prompt llm_function=INJECT | CRITICAL (10/11 audits) | NOT FOUND (all 3 BECOME) | gen_v2 fixed this |
| D02 memory kind=learning_record | CRITICAL | ALL 3 builders | Still active in gen_v2 |
| D03 quality_gate runtime metrics | CRITICAL | 2/3 builders | Still active in gen_v2 |
| D04 domain hallucination | CRITICAL | 1/3 builders (trajectory_eval) | Still active |
| D05 quality non-null defaults | HIGH | NOT FOUND (all null) | gen_v2 fixed this |
| D06 quality_gate ID pattern drift | HIGH | 1 (trajectory_eval) | Still active |
| D07 hallucinated tools | HIGH | ALL 3 builders | Still active in gen_v2 |
| D08 output_template bare placeholders | HIGH | 1 (trajectory_eval pre-fix) | Fixed |
| D09 architecture wrong pillars | HIGH | 1 (trajectory_eval) | Still active |
| D10 file reference drift | HIGH | ALL 3 builders | Still active in gen_v2 |
| D12 ASCII violations | MEDIUM | 1 (prompt_technique) | Still active |

## Key Finding: gen_v2 Progress

gen_v2 (qwen3:14b) FIXED D01 and D05 versus gen_v1 (qwen3:8b).
D02, D07, D10 persist across ALL Wave 3 kinds -- systematic generator gaps still open.
D04 (domain hallucination) appears in HIGH-risk cutting-edge kinds; LOW-risk kinds are clean.

## Validator Results (post-fix)

| Builder | Score |
|---------|-------|
| trajectory_eval | 13/13 PASS |
| self_improvement_loop | 13/13 PASS |
| prompt_technique | 13/13 PASS |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_hybrid_review_wave1]] | related | 0.39 |
| [[n02_audit_action_paradigm_builder]] | downstream | 0.33 |
| [[hybrid_review4_n04]] | sibling | 0.33 |
| [[n01_audit_voice_pipeline_builder]] | downstream | 0.33 |
| [[hybrid_review7_n04]] | sibling | 0.33 |
| [[hybrid_review5_n01]] | sibling | 0.32 |
| [[n01_audit_realtime_session_builder]] | downstream | 0.32 |
| [[n02_audit_collaboration_pattern_builder]] | downstream | 0.31 |
| [[hybrid_review6_n02]] | sibling | 0.30 |
| [[hybrid_review6_n01]] | sibling | 0.30 |
