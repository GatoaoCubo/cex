---
kind: collaboration
id: bld_collaboration_guardrail
pillar: P12
llm_function: COLLABORATE
purpose: How guardrail-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Guardrail"
version: "1.0.0"
author: n03_builder
tags: [guardrail, builder, examples]
tldr: "Golden and anti-examples for guardrail construction, demonstrating ideal structure and common pitfalls."
domain: "guardrail construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_agent
  - guardrail-builder
  - bld_collaboration_system_prompt
  - bld_collaboration_quality_gate
  - bld_collaboration_bugloop
  - bld_collaboration_builder
  - bld_collaboration_e2e_eval
  - bld_collaboration_axiom
  - bld_collaboration_agent_package
  - bld_collaboration_boot_config
---

# Collaboration: guardrail-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what must an agent NEVER do, and what happens if it tries?"
I do not define access permissions. I do not score quality.
I set safety boundaries so agents operate within safe limits with clear violation consequences.
## Crew Compositions
### Crew: "Agent Safety Stack"
```
  1. agent-builder -> "agent definition with capabilities"
  2. guardrail-builder -> "safety boundaries scoped to agent"
  3. bugloop-builder -> "correction cycle for guardrail violations"
```
### Crew: "Governance Foundation"
```
  1. axiom-builder -> "immutable rules (justification for guardrails)"
  2. guardrail-builder -> "enforceable safety restrictions"
  3. e2e-eval-builder -> "validation that guardrails hold under test"
```
## Handoff Protocol
### I Receive
- seeds: scope (agent, system, domain), restriction description, severity
- optional: enforcement mode (block/warn/log), bypass policy, violation examples
### I Produce
- guardrail artifact (.md + .yaml frontmatter)
- committed to: `cex/P11/examples/p11_guardrail_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- axiom-builder: provides immutable principles that justify guardrail restrictions
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agent definitions reference guardrails as constraints |
| bugloop-builder | Correction cycles enforce guardrail compliance |
| e2e-eval-builder | Tests verify guardrails are not bypassed |
| fallback-chain-builder | Degradation must respect guardrail boundaries |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent]] | sibling | 0.56 |
| [[guardrail-builder]] | upstream | 0.51 |
| [[bld_collaboration_system_prompt]] | sibling | 0.42 |
| [[bld_collaboration_quality_gate]] | sibling | 0.42 |
| [[bld_collaboration_bugloop]] | sibling | 0.42 |
| [[bld_collaboration_builder]] | sibling | 0.41 |
| [[bld_collaboration_e2e_eval]] | sibling | 0.40 |
| [[bld_collaboration_axiom]] | sibling | 0.39 |
| [[bld_collaboration_agent_package]] | sibling | 0.38 |
| [[bld_collaboration_boot_config]] | sibling | 0.38 |
