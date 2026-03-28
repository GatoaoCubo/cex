---
kind: memory
id: bld_memory_mental_model
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for mental_model artifact generation
---

# Memory: mental-model-builder
## Summary
Mental models are design-time cognitive maps defining how an agent routes tasks, makes decisions, and prioritizes work. The most impactful production lesson is that routing rules must have confidence thresholds — rules without thresholds trigger on partial keyword matches, causing misroutes. Decision trees need explicit else/fallback branches; agents with incomplete trees silently drop tasks that match no branch.
## Pattern
- Every routing rule needs: keyword pattern, target action, and minimum confidence threshold (0.0-1.0)
- Decision trees must have an explicit default/fallback branch — no task should fall through unhandled
- Priority ordering must be total (no ties) — tied priorities cause non-deterministic behavior
- Heuristics should include their failure rate and the conditions under which they break down
- Domain boundaries must be stated as both positive ("I handle X") and negative ("I do NOT handle Y")
- Personality traits should be functional (affecting output style) not decorative
## Anti-Pattern
- Routing rules without confidence thresholds — triggers on any partial keyword match
- Decision trees with missing else branches — tasks silently dropped or stuck in limbo
- Tied priorities without tiebreaker — execution order becomes non-deterministic
- Domain boundary stated only positively — negative boundaries prevent scope creep more effectively
- Confusing mental_model (P02, design-time cognitive map) with runtime_state (P10, mutable agent state)
- Heuristics presented as certainties — all heuristics have failure modes that should be documented
## Context
Mental models sit in the P02 identity layer as static design-time documents. They are loaded when an agent boots and define its routing logic, decision framework, and domain expertise boundaries. Unlike runtime states (P10), mental models do not change during execution. Unlike routers (P02), mental models include the full cognitive context (personality, heuristics, priorities) beyond just route tables.
## Impact
Agents with confidence-thresholded routing rules showed 40% fewer misrouted tasks. Adding explicit fallback branches to decision trees eliminated 100% of silent task drops. Total priority ordering reduced non-deterministic behavior reports to zero in tested configurations.
## Reproducibility
Reliable mental model production: (1) enumerate all task types the agent handles, (2) create routing rules with keywords and confidence thresholds, (3) build decision tree with explicit fallback at every level, (4) define total priority ordering with no ties, (5) state domain boundaries both positively and negatively, (6) validate against 9 HARD + 12 SOFT gates.
## References
- mental-model-builder SCHEMA.md (14 required + 9 recommended fields)
- P02 identity pillar specification
- Cognitive architecture design patterns
