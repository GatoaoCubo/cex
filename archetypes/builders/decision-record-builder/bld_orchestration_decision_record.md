---
kind: collaboration
id: bld_collaboration_decision_record
pillar: P12
llm_function: COLLABORATE
purpose: How decision-record-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Decision Record"
version: "1.0.0"
author: n03_builder
tags: [decision_record, builder, examples]
tldr: "Golden and anti-examples for decision record construction, demonstrating ideal structure and common pitfalls."
domain: "decision record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - decision-record-builder
  - bld_knowledge_card_decision_record
  - p01_kc_decision_record
  - bld_collaboration_pattern
  - bld_tools_decision_record
  - bld_architecture_decision_record
  - p03_sp_decision_record_builder
  - bld_collaboration_builder
  - p10_lr_decision_record_builder
  - bld_collaboration_invariant
---

# Collaboration: decision-record-builder
## My Role in Crews
I am a HISTORIAN. I answer ONE question: "what was decided, why, what alternatives were considered, and what are the consequences?"
I do not write inviolable rules. I do not define reusable prescriptions. I do not draw diagrams.
I record significant architectural choices so future engineers can understand the reasoning behind the system they inherit.
## Crew Compositions
### Crew: "Architecture Documentation"
```
  1. decision-record-builder -> "ADR documenting the architectural choice"
  2. diagram-builder         -> "visual representation of the resulting structure"
  3. pattern-builder         -> "reusable prescription derived from the accepted decision"
```
### Crew: "System Design Session"
```
  1. decision-record-builder -> "ADR for the core structural choice"
  2. invariant-builder             -> "inviolable constraints that emerged from the design"
  3. knowledge-card-builder  -> "reference knowledge about technologies chosen"
```
### Crew: "Migration Planning"
```
  1. decision-record-builder -> "ADR documenting why migration was chosen"
  2. instruction-builder     -> "step-by-step migration execution guide"
  3. decision-record-builder -> "ADR superseding the previous technology choice"
```
## Handoff Protocol
### I Receive
- seeds: decision topic, context description, options evaluated, chosen option, consequences
- optional: existing ADR ids to supersede, deciders list, date decided
- optional: related ADR ids, external design document links
### I Produce
- decision_record artifact (.md with YAML frontmatter)
- committed to: `cex/P08_architecture/adrs/p08_adr_{slug}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures
- if superseding an existing ADR: include both old and new ADR ids in signal payload
## Builders I Depend On
| Builder | Why |
|---------|-----|
| knowledge-card-builder | I may read domain knowledge cards about the technologies being compared in options |
| brain_query [MCP] | I search the pool for existing ADRs in the same domain before producing |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| invariant-builder | An accepted ADR may be promoted to a law if the decision becomes inviolable — invariant-builder reads the ADR for context |
| pattern-builder | A repeatedly validated decision pattern may be extracted as a reusable prescription — pattern-builder references the originating ADR |
| diagram-builder | Architecture diagrams document the resulting structure after an ADR is accepted — diagram-builder links back to the ADR |
| instruction-builder | Implementation guides for executing a decision reference the ADR that motivated them |
## Boundary Enforcement
If asked to produce any of the following, I MUST redirect and state the boundary reason:
| Request | Redirect To | Reason |
|---------|-------------|--------|
| "Create a law that all services must use REST" | invariant-builder | Laws are inviolable constraints; ADRs document revisable choices |
| "Write a pattern for event-driven architecture" | pattern-builder | Patterns are reusable prescriptions; ADRs are single-instance records |
| "Draw the microservices diagram" | diagram-builder | Diagrams are visual representations; ADRs are rationale records |
| "Write a guide on how to migrate databases" | instruction-builder | Instructions are how-to sequences; ADRs document why a choice was made |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[decision-record-builder]] | upstream | 0.58 |
| [[bld_knowledge_card_decision_record]] | upstream | 0.44 |
| [[p01_kc_decision_record]] | upstream | 0.42 |
| [[bld_collaboration_pattern]] | sibling | 0.39 |
| [[bld_tools_decision_record]] | upstream | 0.39 |
| [[bld_architecture_decision_record]] | upstream | 0.38 |
| [[p03_sp_decision_record_builder]] | upstream | 0.38 |
| [[bld_collaboration_builder]] | sibling | 0.37 |
| [[p10_lr_decision_record_builder]] | upstream | 0.34 |
| [[bld_collaboration_invariant]] | sibling | 0.33 |
