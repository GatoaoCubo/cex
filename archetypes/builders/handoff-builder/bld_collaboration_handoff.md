---
kind: collaboration
id: bld_collaboration_handoff
pillar: P12
llm_function: COLLABORATE
purpose: How handoff-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: handoff-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what should the target do, with what context, and how should it commit?"
I do not define routing rules. I do not model dependencies.
I package delegation instructions so remote executors have everything needed to complete a task.
## Crew Compositions
### Crew: "Full Dispatch Setup"
```
  1. dispatch-rule-builder -> "routing rules (who receives)"
  2. dag-builder -> "execution order (when to execute)"
  3. handoff-builder -> "delegation instructions (what to do)"
```
### Crew: "Task Delegation"
```
  1. context-doc-builder -> "domain context for the executor"
  2. instruction-builder -> "step-by-step recipe"
  3. handoff-builder -> "packaged delegation with scope fence and commit rules"
```
## Handoff Protocol
### I Receive
- seeds: target executor, task description, scope fence (allowed/forbidden paths)
- optional: context documents, seed keywords, commit template, quality threshold
### I Produce
- handoff artifact (.md with context, tasks, scope fence, commit, signal sections)
- committed to: `cex/P12/examples/p12_handoff_{mission}_{target}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- dispatch-rule-builder: provides routing decision that determines handoff target
- context-doc-builder: provides domain context embedded in the handoff
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| dag-builder | Models handoff dependencies in execution graphs |
| e2e-eval-builder | Tests that handoff execution produces correct results |
