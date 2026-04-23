---
kind: collaboration
id: bld_collaboration_red_team_eval
pillar: P12
llm_function: COLLABORATE
purpose: How red-team-eval-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Red Team Eval"
version: "1.0.0"
author: n03_builder
tags: [red_team_eval, builder, examples]
tldr: "Golden and anti-examples for red team eval construction, demonstrating ideal structure and common pitfalls."
domain: "red team eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - red-team-eval-builder
  - bld_collaboration_unit_eval
  - bld_collaboration_smoke_eval
  - bld_collaboration_regression_check
  - bld_collaboration_prompt_version
  - bld_collaboration_eval_dataset
  - p03_sp_red_team_eval_builder
  - bld_collaboration_system_prompt
  - bld_collaboration_golden_test
  - p01_kc_eval_testing
---

# Collaboration: red-team-eval-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what attack types target this agent, what is the target, and what criteria offine safe behavior?"
I do not build runtime enforcement. I do not define functional test suites.
I configure adversarial evaluations so security teams can probe LLM systems for safety vulnerabilities before deployment.
## Crew Compositions
### Crew: "LLM Safety Lifecycle"
```
  1. red-team-eval-builder  -> "adversarial eval config (attack_types, target, pass_criteria)"
  2. guardrail-builder       -> "runtime enforcement boundary (blocks attacks post-deploy)"
  3. learning-record-builder -> "captures vulnerability patterns found during red team run"
```
### Crew: "Pre-Deploy Security Review"
```
  1. system-prompt-builder   -> "system prompt being hardened"
  2. red-team-eval-builder   -> "adversarial eval against that prompt"
  3. e2e-eval-builder        -> "functional correctness test (parallel, not sequential)"
  4. quality-gate-builder    -> "final quality gate before deploy approval"
```
### Crew: "Eval Coverage Suite"
```
  1. red-team-eval-builder   -> "adversarial safety coverage"
  2. unit-eval-builder       -> "isolated logic correctness"
  3. smoke-eval-builder      -> "quick sanity check post-deploy"
  4. benchmark-builder       -> "comparative performance baseline"
```
## Handoff Protocol
### I Receive
- seeds: target agent/prompt name, threat model description, deployment context
- optional: framework preference, severity classification, OWASP categories of concern
- optional: existing system prompt or agent spec to scan for attack surface
### I Produce
- red_team_eval artifact (.md + .yaml frontmatter)
- committed to: `cex/P07_evals/examples/p07_rt_{eval_slug}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures
## Builders I Depend On
| Builder | Why | When |
|---------|-----|------|
| system-prompt-builder | I need the system prompt spec to identify attack surface | Before composing Attack Scenarios |
| agent-builder | I need the agent spec to understand what capabilities can be exploited | Before defining target field |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| guardrail-builder | Guardrail specs are informed by which attacks the red team eval found exploitable |
| learning-record-builder | Vulnerability patterns discovered during red team run become learning records |
| quality-gate-builder | Security gate for deploy approval requires passing red_team_eval as input |
## Boundary Declarations
| If the request is... | Route to... | Reason |
|---------------------|-------------|--------|
| Runtime blocking of attacks | guardrail-builder | Guardrail enforces at runtime; red team eval tests offline |
| Functional correctness testing | e2e-eval-builder | e2e_eval tests correct behavior; red team tests adversarial behavior |
| Isolated unit logic test | unit-eval-builder | unit_eval tests single functions; red team tests full attack surface |
| Quick post-deploy sanity check | smoke-eval-builder | smoke_eval checks liveness; red team checks exploitability |
| Performance comparison | benchmark-builder | benchmark compares scores; red team probes safety boundaries |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[red-team-eval-builder]] | upstream | 0.52 |
| [[bld_collaboration_unit_eval]] | sibling | 0.45 |
| [[bld_collaboration_smoke_eval]] | sibling | 0.42 |
| [[bld_collaboration_regression_check]] | sibling | 0.40 |
| [[bld_collaboration_prompt_version]] | sibling | 0.39 |
| [[bld_collaboration_eval_dataset]] | sibling | 0.39 |
| [[p03_sp_red_team_eval_builder]] | upstream | 0.38 |
| [[bld_collaboration_system_prompt]] | sibling | 0.38 |
| [[bld_collaboration_golden_test]] | sibling | 0.38 |
| [[p01_kc_eval_testing]] | upstream | 0.36 |
