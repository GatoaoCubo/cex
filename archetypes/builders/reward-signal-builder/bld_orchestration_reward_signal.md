---
kind: collaboration
id: bld_collaboration_reward_signal
pillar: P12
llm_function: COLLABORATE
purpose: How reward-signal-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Reward Signal"
version: "1.0.0"
author: n03_builder
tags: [reward_signal, builder, examples]
tldr: "Golden and anti-examples for reward signal construction, demonstrating ideal structure and common pitfalls."
domain: "reward signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - reward-signal-builder
  - bld_knowledge_card_reward_signal
  - bld_collaboration_quality_gate
  - p03_sp_reward_signal_builder
  - bld_collaboration_builder
  - bld_collaboration_scoring_rubric
  - bld_collaboration_signal
  - bld_architecture_reward_signal
  - bld_examples_reward_signal
  - bld_instruction_reward_signal
---

# Collaboration: reward-signal-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what dimensions does this reward signal measure, at what scale, and how does it drive learning?"
I do not make binary pass/fail decisions. I do not define criteria taxonomies.
I design continuous quality scores so training pipelines and monitoring systems can improve agent behavior over time.
## Crew Compositions
### Crew: "Agent Improvement Pipeline"
```
  1. scoring-rubric-builder  -> "criteria taxonomy — what dimensions matter for this domain"
  2. reward-signal-builder   -> "continuous reward signal — scalar/preference/critique with calibrated baseline"
  3. quality-gate-builder    -> "binary gate consuming reward scores for serving-time enforcement"
```
### Crew: "RLHF Dataset Construction"
```
  1. reward-signal-builder   -> "preference signal design — how to collect A>B pairs"
  2. dataset-builder         -> "preference dataset schema and storage format"
  3. training-config-builder -> "RLHF/DPO training configuration consuming the dataset"
```
### Crew: "Production Quality Monitoring"
```
  1. reward-signal-builder   -> "per-turn scalar signal with baseline"
  2. metric-builder          -> "rolling average KPI derived from reward scores"
  3. alert-builder           -> "alert firing when rolling metric falls below baseline"
```
### Crew: "Constitutional AI Pipeline"
```
  1. principle-builder       -> "constitutional principles for critique"
  2. reward-signal-builder   -> "critique signal — LLM produces critique + revision + score"
  3. instruction-builder     -> "critique-revise loop recipe referencing the signal"
```
## Handoff Protocol
### I Receive
- seeds: domain, quality dimensions to measure, intended improvement loop (RLHF/DPO/filtering/monitoring)
- optional: existing scoring_rubric artifact (informs criteria), model preference, scale preference
- optional: human rating data (for baseline calibration)
### I Produce
- reward_signal artifact (.md with YAML frontmatter)
- committed to: `cex/P11_feedback/examples/p11_reward_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons and specific gate IDs
## Builders I Depend On
| Builder | Why | When |
|---------|-----|------|
| scoring-rubric-builder | Criteria definitions inform reward dimensions | Optional upstream — if rubric exists, read it before designing criteria |
| system-prompt-builder | LLM-judge prompts implement the reward signal | After signal design, for implementation |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | Gates consume reward scores as input thresholds |
| metric-builder | Rolling averages derived from per-turn reward scores |
| training-config-builder | RLHF/DPO configs reference reward signal spec for dataset construction |
| instruction-builder | Multi-step recipes reference reward signal as evaluation step |
| alert-builder | Alerts fire when rolling reward score falls below baseline |
## Boundary Enforcement
If asked to produce any of the following, REDIRECT with reason:
| Request type | Redirect to | Reason |
|-------------|-------------|--------|
| Binary pass/fail threshold | quality-gate-builder | quality_gate makes pass/fail decisions; reward_signal produces continuous scores |
| Criteria taxonomy definition | scoring-rubric-builder | scoring_rubric defines what dimensions exist; reward_signal measures them with a score |
| Business KPI | metric-builder or kpi-builder | KPIs track business outcomes; reward_signals track learning-loop quality |
| Training loop implementation | training-config-builder | Implementation code out of scope; reward_signal is a spec |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[reward-signal-builder]] | upstream | 0.53 |
| [[bld_knowledge_card_reward_signal]] | upstream | 0.42 |
| [[bld_collaboration_quality_gate]] | sibling | 0.42 |
| [[p03_sp_reward_signal_builder]] | upstream | 0.41 |
| [[bld_collaboration_builder]] | sibling | 0.37 |
| [[bld_collaboration_scoring_rubric]] | sibling | 0.37 |
| [[bld_collaboration_signal]] | sibling | 0.36 |
| [[bld_architecture_reward_signal]] | upstream | 0.35 |
| [[bld_examples_reward_signal]] | upstream | 0.34 |
| [[bld_instruction_reward_signal]] | upstream | 0.34 |
