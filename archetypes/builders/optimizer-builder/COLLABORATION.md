---
pillar: P12
llm_function: COLLABORATE
purpose: How optimizer-builder works in crews
---

# Collaboration: optimizer-builder

## My Role
I define WHAT process is optimized, at WHAT metric threshold, with WHAT action.
I do not implement metric collection (validator-builder, P06).
I do not define evaluation criteria (scoring-rubric-builder, P07).
I do not cycle on artifact defects (bugloop-builder, P11).

## Crew: "Add Continuous Improvement to Pipeline"
```
  1. scoring-rubric-builder  -> defines quality dimensions and weights
  2. optimizer-builder        -> defines metric>action cycle with thresholds
  3. signal-builder           -> emits state-change signals on threshold crossings
  4. validator-builder        -> implements metric collection in code
```

## Crew: "Full Feedback Loop for New Process"
```
  1. quality-gate-builder     -> defines pass/fail barrier at publish time
  2. optimizer-builder        -> defines continuous improvement between publishes
  3. bugloop-builder          -> handles defect correction when metric signals failures
  4. lifecycle-rule-builder   -> handles freshness/archive when process output ages
```

## Handoff Protocol

### I Receive
- target: what process to optimize (string description)
- metric_name: what to measure (or enough context to derive it)
- domain: process domain for brain_query lookup
- severity: how aggressively to set thresholds (conservative / aggressive / slo-aligned)

### I Produce
- optimizer artifact in P11_feedback/examples/p11_opt_{slug}.md
- complete frontmatter + 5 body sections
- ready for signal-builder to wire state-change emissions

## Cross-Reference Obligations
optimizer-builder references signal-builder -> signal-builder MUST reference optimizer-builder.
optimizer-builder references knowledge-card-builder (improvement.history) -> knowledge-card-builder MUST reference optimizer-builder.

## Builders I Depend On
| Builder | Why |
|---------|-----|
| scoring-rubric-builder | Provides quality dimensions that become secondary metrics |
| quality-gate-builder | Gate thresholds inform optimizer trigger values |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| signal-builder | Optimizer threshold crossings are signal sources |
| validator-builder | Implements the metric collection this optimizer monitors |
| knowledge-card-builder | improvement.history entries become KC update triggers |
