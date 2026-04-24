---
id: p01_fse_n07_dispatch
kind: few_shot_example
8f: F3_inject
pillar: P01
nucleus: N07
title: "Few-Shot Example -- N07 Intent Resolution and Dispatch"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: few-shot-example-builder
domain: orchestration
difficulty: hard
edge_case: true
format: "intent resolution + handoff writing for N07 orchestrator"
quality: 9.1
tags: [few-shot, orchestration, intent-resolution, dispatch, n07]
tldr: "5 input/output pairs teaching N07 how to transmute vague user input into structured kind/pillar/nucleus/verb tuples and handoff snippets."
keywords: [intent-resolution, dispatch, handoff, n07, orchestrator, transmutation]
density_score: 1.0
related:
  - bld_collaboration_kind
  - agent_card_engineering_nucleus
  - p12_wf_admin_orchestration
  - p02_agent_creation_nucleus
  - p03_sp_orchestration_nucleus
  - p01_kc_orchestration_best_practices
  - p02_agent_admin_orchestrator
  - ctx_cex_new_dev_guide
  - report_intent_resolution_value_prop
  - quality_gate_intent_resolution
---
<!-- 8F TRACE
F1 CONSTRAIN: kind=few_shot_example, pillar=P01, max_bytes=5120, naming=p01_fse_{topic}.md
F2 BECOME: few-shot-example-builder (13 ISOs loaded: schema, system_prompt, instruction, output_template, examples, memory)
F3 INJECT: bld_examples + bld_memory + p01_fse_kc_creation.md (existing). Match: 78%
F4 REASON: 5 examples, easy->hard arc, N07 orchestrator domain: intent resolution + dispatch + grid
F5 CALL: Read+Write+compile ready. 1 similar artifact found.
F6 PRODUCE: 5 input/output pairs, each with resolved_intent tuple and handoff_snippet
F7 GOVERN: quality=null (H05 pass), id=p01_fse_n07_dispatch (H02 pass), input non-empty x5 (H06 pass), output non-empty x5 (H07 pass), tags>=3 (S02 pass), no scoring rubric (S07 pass)
F8 COLLABORATE: compiled to YAML via cex_compile.py
-->

## Explanation

N07's core skill is transmutation: convert vague user tokens into the canonical
`{kind, pillar, nucleus, verb}` tuple, then write a concrete handoff.
These 5 pairs calibrate easy (single kind) through hard (grid + wave plan).
Each output shows the exact structured form N07 must produce -- not prose, not
summary, but machine-readable dispatch that any nucleus can execute without
further clarification.

---

## Example 1 (easy) -- Single artifact, clear kind

**Input**
```
"make me a landing page"
```

**Resolved Intent**
```yaml
kind: landing_page
pillar: P05
nucleus: N03
verb: create
confidence: 0.92
```

**Handoff Snippet**
```markdown
## Task
Produce kind=landing_page, pillar=P05, using landing-page-builder ISOs.
Builder: archetypes/builders/landing-page-builder/
Output: N03_engineering/P05_output/landing_page_{{slug}}.md
Compile after save: python _tools/cex_compile.py {path}
Signal: write_signal("n03", "complete", null)
```

---

## Example 2 (easy) -- Research domain, nucleus routing

**Input**
```
"research competitors"
```

**Resolved Intent**
```yaml
kind: knowledge_card
pillar: P01
nucleus: N01
verb: analyze
domain: competitive-intelligence
confidence: 0.88
```

**Handoff Snippet**
```markdown
## Task
Produce kind=knowledge_card, pillar=P01, domain=competitive-intelligence.
Builder: archetypes/builders/knowledge-card-builder/
Scan: N01_intelligence/P01_knowledge/ for existing competitor KCs first.
Output: N01_intelligence/P01_knowledge/kc_competitor_{{slug}}.md
Signal: write_signal("n01", "complete", null)
```

---

## Example 3 (medium) -- Tool invocation, no kind

**Input**
```
"fix the tests"
```

**Resolved Intent**
```yaml
kind: null
pillar: P07
nucleus: N05
verb: validate
tool: cex_e2e_test.py
action: debug_and_repair
confidence: 0.85
```

**Handoff Snippet**
```markdown
## Task
No artifact to produce. Run: python _tools/cex_e2e_test.py --verbose
For each FAIL: diagnose root cause, apply fix, rerun until PASS.
Commit fixes: git commit -m "[N05] fix failing e2e tests"
Signal: write_signal("n05", "complete", null)
```

---

## Example 4 (hard) -- Grid dispatch, wave plan

**Input**
```
"launch all nuclei"
```

**Resolved Intent**
```yaml
kind: null
pillar: P12
nucleus: N07
verb: dispatch
mode: grid
wave_count: 1
targets: [n01, n02, n03, n04, n05, n06]
confidence: 0.79
gdp_required: true
```

**Handoff Snippet**
```markdown
## GDP Decision Required
Q1: What is the mission goal? (grid needs a task per nucleus)
Q2: Parallel or sequential waves?
-- After GDP --
Write 6 handoff files: .cex/runtime/handoffs/MISSION_{nucleus}.md
Run: bash _spawn/dispatch.sh grid MISSION
Monitor: git log --oneline --since="5 minutes ago"
Consolidate after all 6 signal complete.
```

---

## Example 5 (hard) -- Sweep tool, quality threshold

**Input**
```
"improve bad artifacts"
```

**Resolved Intent**
```yaml
kind: null
pillar: P11
nucleus: N07
verb: improve
tool: cex_evolve.py
threshold: 9.0
mode: heuristic_then_agent
confidence: 0.91
```

**Handoff Snippet**
```markdown
## Task
Run: python _tools/cex_evolve.py --sweep --threshold 9.0 --mode heuristic
Then: python _tools/cex_evolve.py --sweep --threshold 9.0 --mode agent --budget 50
Artifacts below quality 9.0 are retried up to 2 passes.
Commit: git commit -m "[N07] evolve: heuristic+agent sweep, threshold=9.0"
Signal: write_signal("n07", "complete", null)
```

---

## Edge Cases

- **Grid without goal**: input "launch all nuclei" triggers GDP (Example 4) --
  N07 must NOT dispatch without knowing the per-nucleus task.
- **Tool-only dispatch** (no kind): "fix tests" routes to N05 + tool, not a builder.
  `kind: null` is valid when the action is operational, not artifact-producing.
- **Confidence < 0.80**: present top-3 interpretations to user via GDP before
  dispatching. Do not guess silently.

---

## Variations

- "write a system prompt for N03" -> kind=system_prompt, pillar=P03, nucleus=N03, verb=create
- "schedule the overnight loop" -> kind=schedule, pillar=P12, nucleus=N07, tool=overnight.ps1
- "what agents do we have?" -> kind=null, verb=query, tool=cex_capability_index.py

---

## Properties

| Property | Value |
|----------|-------|
| Kind | `few_shot_example` |
| Pillar | P01 |
| Nucleus | N07 |
| Domain | orchestration |
| Difficulty | hard |
| Examples | 5 (easy x2, medium x1, hard x2) |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Quality target | null (never self-score) |
| Density target | 0.85+ |
| Max bytes | 5120 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_kind]] | downstream | 0.36 |
| [[agent_card_engineering_nucleus]] | downstream | 0.36 |
| [[p12_wf_admin_orchestration]] | downstream | 0.33 |
| [[p02_agent_creation_nucleus]] | downstream | 0.33 |
| [[p03_sp_orchestration_nucleus]] | downstream | 0.32 |
| [[p01_kc_orchestration_best_practices]] | related | 0.32 |
| [[p02_agent_admin_orchestrator]] | downstream | 0.31 |
| [[ctx_cex_new_dev_guide]] | related | 0.30 |
| [[report_intent_resolution_value_prop]] | related | 0.30 |
| [[quality_gate_intent_resolution]] | downstream | 0.30 |
