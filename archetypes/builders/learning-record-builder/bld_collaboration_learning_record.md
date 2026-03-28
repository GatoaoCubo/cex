---
kind: collaboration
id: bld_collaboration_learning_record
pillar: P10
llm_function: COLLABORATE
purpose: How learning-record-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: learning-record-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what did we learn from this experience, and how reproducible is it?"
I capture success and failure patterns as scored, structured records with density >= 0.80. I do NOT handle external facts (knowledge-card-builder), ephemeral runtime state (session-state-builder), or abstract truths (axiom-builder).
## Crew Compositions
### Crew: "Post-Execution Review"
```
  1. signal-builder          -> "completion signal with execution status and metrics"
  2. learning-record-builder -> "distills durable patterns and anti-patterns from the run"
  3. quality-gate-builder    -> "validates the learning_record artifact itself"
```
### Crew: "Knowledge Upgrade"
```
  1. learning-record-builder -> "experience pattern captured with reproducibility score"
  2. knowledge-card-builder  -> "promotes high-impact learnings into stable external facts"
  3. axiom-builder           -> "crystallizes the pattern into an immutable truth if universal"
```
### Crew: "Agent Improvement Loop"
```
  1. learning-record-builder -> "records what routing decisions succeeded or failed"
  2. mental-model-builder    -> "updates agent routing rules based on captured patterns"
  3. instruction-builder     -> "revises execution steps when anti-patterns reveal failures"
```
## Handoff Protocol
### I Receive
- seeds: experience description, outcome (success or failure), domain/satellite context, impact assessment
- optional: signal data, session logs, execution metrics, prior learning records for deduplication
### I Produce
- learning_record artifact (Markdown, 22 frontmatter fields, patterns + anti-patterns, density >= 0.80, max 3KB)
- committed to: `cex/P10_memory/examples/p10_lr_{slug}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- signal-builder: signals trigger learning capture and provide execution context (optional, not blocking)
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| mental-model-builder   | updates agent heuristics and routing priorities based on captured patterns |
| axiom-builder          | repeated learnings may crystallize into universal immutable truths |
| knowledge-card-builder | promotes reproducible learnings into stable factual records |
| quality-gate-builder   | learning records validate whether gates are catching the right failures |
