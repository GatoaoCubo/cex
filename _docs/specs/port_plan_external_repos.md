---
id: port_plan_external_repos
kind: spec
pillar: P08_architecture
title: "External Repo Port Plan -- ruflo + aiox-core vs CEX"
version: 1.0
quality: 9.1
tags: [spec, port_plan, architecture, comparative_analysis]
created: 2026-04-11
author: n07_orchestrator
domain: CEX architecture evolution
density_score: 1.0
---

# External Repo Port Plan -- ruflo + aiox-core vs CEX

> **Mission**: absorb reusable patterns from two peer projects that share CEX's
> "typed agent system" DNA. Keep CEX's unique strengths (typed taxonomy, 8F, GDP,
> brand bootstrap) intact. Import only what CEX lacks AND what demonstrably raises
> the quality ceiling.

## 1. CEX Baseline (what we already have)

| Capability | CEX implementation |
|------------|-------------------|
| Typed knowledge taxonomy | 123 kinds x 12 pillars x 125 builders x 12 ISOs |
| Reasoning protocol | 8F (F1 CONSTRAIN -> F8 COLLABORATE) mandatory on every task |
| Nuclei | 8 nuclei (N00-N07) with fractal subdirs mirroring pillars |
| Dispatch | 3-level CLI routing: L1 explicit / L2 YAML fallback_chain / L3 smart router |
| GDP | Guided Decision Protocol: user decides WHAT, CEX decides HOW |
| Brand | `brand_config.yaml` + propagation + validation + audit tools |
| Quality | 3-layer scoring (structural 30% + rubric 30% + semantic 40%), 9.0 target |
| Memory | 4-type taxonomy (correction/preference/convention/context) with age decay |
| Retrieval | TF-IDF over 2184 docs / 12K vocab (cex_retriever.py) |
| Session safety | Multi-N07 PID tracking, session-tagged stop commands |

## 2. ruvnet/ruflo -- analysis

**Framing**: SPARC 3.0 is a quality-gated, trust-tiered, MCP-driven agent runtime.
Its strongest ideas orbit around **hardening** -- gates, proofs, and cost control.

### Top 5 reusable ideas

| # | Pattern | What it is | CEX impact | Effort | Priority |
|---|---------|-----------|------------|--------|----------|
| R1 | **HNSW vector memory** | Hierarchical Navigable Small World index for semantic recall at scale | Replace TF-IDF cex_retriever with HNSW for >10k artifacts; keep TF-IDF as L1 fast path, HNSW as L2 semantic | Medium | HIGH |
| R2 | **Compiled policy gates** | Gates are compiled to a deterministic bytecode-like representation, not re-parsed per call | Compile quality_gate.yaml artifacts into a fast executor -- current gates are re-parsed by cex_score.py each run | Medium | MED |
| R3 | **Trust tiers** | Each capability has a trust level (sandboxed / audited / privileged); tasks require matching tier | Map to CEX agents: each agent_card declares required_trust; N07 rejects dispatch if handoff trust > nucleus capability | Low | HIGH |
| R4 | **3-tier cost router** | Cheap->mid->premium escalation based on task difficulty prediction | CEX already has fallback_chain but it's CLI-presence based, not difficulty based -- add a cost estimator that upgrades on regression detection | Medium | MED |
| R5 | **Cryptographic proof chain** | Every artifact signs its lineage (hash of inputs + outputs + model version) | Audit trail for "who built what with which model" -- fits CEX's `decision_record` kind; extends `cex_score.py` output with a proof blob | High | LOW |

## 3. SynkraAI/aiox-core -- analysis

**Framing**: aiox-core is an **IDE-native multi-agent orchestration** layer with a strong
focus on wave planning, star-command dispatch, and editor synchronization.

### Top 5 reusable ideas

| # | Pattern | What it is | CEX impact | Effort | Priority |
|---|---------|-----------|------------|--------|----------|
| A1 | **Synapse 8-layer stack** | 8 coordinated context layers (system/role/task/memory/tool/decision/trace/feedback) injected per call | Maps to CEX F3 INJECT but more structured -- adopt as the canonical F3 envelope; ensures nothing is forgotten | Low | HIGH |
| A2 | **star-command dispatch** | One central command ("/star") that reads manifest and spawns the right graph of sub-agents | CEX has /mission + /grid but not a single-entrypoint DAG runner; `cex_mission_runner.py` is close -- upgrade it to read a DAG manifest | Medium | MED |
| A3 | **Quality gate severity levels** | Gates have error/warn/info severities, not just pass/fail; warn doesn't block | CEX quality_gate is binary -- add severity field to score retries AND allow "publish with warnings" | Low | HIGH |
| A4 | **Wave analyzer** | Pre-dispatch tool that predicts which waves are independent and which need serialization | CEX cex_mission_runner chains waves but doesn't plan them -- a dependency analyzer over handoffs would catch missing blocks | Medium | MED |
| A5 | **IDE-sync parity** | Manifest format that works identically in VS Code + Cursor + JetBrains extensions | CEX is terminal-first; a manifest export for IDE consumption would open distribution; tie into cex_compile.py --target | High | LOW |

## 4. Combined priority matrix

| Priority | Pattern | Origin | Lands in | Blocking? |
|----------|---------|--------|----------|-----------|
| P0 HIGH | HNSW memory (R1) | ruflo | cex_retriever.py L2 layer | No -- side install |
| P0 HIGH | Trust tiers (R3) | ruflo | agent_card kind + N07 dispatch guard | No -- additive field |
| P0 HIGH | Synapse 8-layer F3 envelope (A1) | aiox | F3 INJECT canonical structure | No -- refactor |
| P0 HIGH | Quality gate severity (A3) | aiox | quality_gate kind schema | No -- schema extension |
| P1 MED | Compiled policy gates (R2) | ruflo | cex_score.py executor | No -- perf win |
| P1 MED | Cost router tier escalation (R4) | ruflo | cex_router.py | No -- extends L3 |
| P1 MED | Star-command DAG runner (A2) | aiox | cex_mission_runner.py | No -- extends |
| P1 MED | Wave analyzer (A4) | aiox | new _tools/cex_wave_plan.py | No -- additive |
| P2 LOW | Proof chain (R5) | ruflo | decision_record + cex_score.py | No -- audit |
| P2 LOW | IDE-sync manifest (A5) | aiox | cex_compile.py --target | No -- distro |

## 5. What NOT to port (CEX is already better)

| Peer feature | CEX equivalent (stronger) |
|--------------|--------------------------|
| Free-form prompt templates | 123-kind typed taxonomy -- enforces discipline |
| Ad-hoc builder scripts | 125 builders x 12 ISOs -- fractal, scorable, auditable |
| Generic "agent" concept | Nuclei (N01-N07) with sin lenses, pillars, fractal dirs |
| Unbounded autonomy | GDP -- user decides WHAT, CEX decides HOW |
| Brand-agnostic output | brand_config.yaml propagation -- every artifact speaks the brand |
| ad-hoc scoring | 3-layer (structural + rubric + semantic) with 8.0 floor / 9.0 target |

## 6. Risks & guardrails

| Risk | Mitigation |
|------|-----------|
| Import fatigue -- too many ports at once dilute focus | Execute P0 only in wave 1, P1 in wave 2, P2 deferred until P0+P1 stabilize |
| Schema drift -- new fields break existing artifacts | All extensions are additive; validate via cex_doctor.py before merging |
| Over-abstraction -- porting "elegant" code that doesn't fit | Each port must produce a CEX-native artifact (kind, builder, or tool); if it can't, it doesn't belong |
| Losing CEX identity -- becoming a clone | Keep 8F + GDP + fractal taxonomy immutable; these are non-negotiable |
| Attribution -- respect upstream licenses | Note each ported pattern in the relevant learning_record + commit message |

## 7. Wave plan

### Wave 1 (P0 -- HIGH, weeks 1-2)
1. R1 HNSW memory -- install `hnswlib` + write `cex_retriever_hnsw.py` side-by-side with TF-IDF
2. R3 Trust tiers -- extend `agent_card` schema with `trust_tier: [sandboxed|audited|privileged]`
3. A1 Synapse 8-layer -- document F3 INJECT canonical envelope in `.claude/rules/8f-reasoning.md`
4. A3 Gate severity -- extend `quality_gate` schema with `severity: [error|warn|info]` per rule

### Wave 2 (P1 -- MED, weeks 3-4)
5. R2 Compiled gates -- add a `cex_gate_compile.py` step that emits optimized executor bytecode
6. R4 Cost router -- add tier escalation to `cex_router.py` based on regression detection
7. A2 DAG runner -- extend `cex_mission_runner.py` to read a `mission.dag.yaml` manifest
8. A4 Wave analyzer -- new `_tools/cex_wave_plan.py` that reads handoffs and emits a DAG

### Wave 3 (P2 -- LOW, optional)
9. R5 Proof chain -- extend `decision_record` with cryptographic lineage
10. A5 IDE-sync -- `cex_compile.py --target vscode|cursor|jetbrains`

## 8. Success criteria

- **Absorption check**: each ported pattern maps to a CEX kind / rule / tool / builder -- no loose scripts.
- **Regression check**: `cex_doctor.py` + `cex_system_test.py` stay green after each port.
- **Identity check**: 8F + GDP + fractal taxonomy unchanged in structure.
- **Quality lift**: at least one port demonstrably raises measurable quality (retriever hit rate, gate false-positive rate, or dispatch success rate).

## 9. References

- ruvnet/ruflo: https://github.com/ruvnet/ruflo (SPARC 3.0 agent runtime)
- SynkraAI/aiox-core: https://github.com/SynkraAI/aiox-core (IDE-native multi-agent)
- CEX baseline: `CLAUDE.md` + `.claude/rules/8f-reasoning.md` + `.cex/kinds_meta.json`
- Multi-CLI learnings: `.cex/learning_records/lr_multi_cli_dispatch_20260411.json`
- Routing config: `.cex/config/nucleus_models.yaml` (fallback_chain per nucleus)
