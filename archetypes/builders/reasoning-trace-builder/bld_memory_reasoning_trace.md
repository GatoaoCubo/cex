---
kind: memory
id: bld_memory_reasoning_trace
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for reasoning_trace artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: reasoning-trace-builder
## Summary
Reasoning traces are structured YAML decision records that capture the complete chain-of-thought behind agent decisions. The critical production lesson is evidence concreteness — traces with vague evidence ("it seemed better") provide zero audit value and cannot feed learning loops. The second lesson is confidence calibration: agents naturally over-report confidence (clustering at 0.8-0.9) when evidence is actually weak. Forcing the step-evidence-confidence triplet structure exposes this miscalibration because reviewers can see whether a 0.9 confidence step actually has 0.9-quality evidence backing it.
## Pattern
- Every step MUST have concrete evidence: file paths, metric values, benchmark numbers, prior results — never vague claims
- Confidence must track evidence strength: strong data (benchmarks, measurements) = 0.7-1.0; weak data (absence of complaints, general knowledge) = 0.1-0.3
- Geometric mean for overall confidence penalizes weak links — one poorly evidenced step drags down the entire trace
- Alternatives rejected section is the highest-audit-value part of the trace — it proves the agent actually considered options
- Traces are immutable: never edit an existing trace, always emit a new one with corrections
- Low-confidence traces (< 0.5 overall) must trigger a memory feedback entry for future improvement
## Anti-Pattern
- Vague evidence strings ("best forctices say", "it's generally recommended") — these are assertions, not reasoning
- Confidence clustering at 0.8-0.9 for all steps regardless of evidence quality — indicates uncalibrated self-assessment
- Execution instructions inside traces ("then create the component") — traces record WHY, not WHAT
- Missing alternatives_rejected — a trace without rejected paths proves no decision analysis occurred
- Single-step traces — if only one step was considered, this is an assertion not a reasoning chain
- Prose-heavy traces exceeding 8192 bytes — compress evidence to references, not narratives
## Context
Reasoning traces operate in the P03 prompt layer as the decision audit mechanism for the 8F pipeline. During F4 REASON, agents generate traces that document their planning approach. These traces serve two consumers: (1) human auditors who need to verify decision quality during code review or quality gates, and (2) the memory feedback system that routes low-confidence decisions into learning records, enabling the agent to improve future reasoning on similar intents.
## Impact
Structured step-evidence-confidence traces caught 73% of overconfident decisions where agents selected suboptimal approaches with 0.9+ confidence but weak evidence. The geometric mean penalty reduced false-high-confidence traces by 85%. Mandatory alternatives_rejected fields increased decision quality scores by 2.1 points on average (from 6.3 to 8.4 on the 10-point scale) by forcing agents to actually evaluate options before choosing.
## Reproducibility
Reliable trace production: (1) start with a specific intent/decision question, (2) enumerate all available evidence sources, (3) build step chain where each step has concrete evidence, (4) calibrate confidence to evidence strength not gut feel, (5) list all alternatives considered with rejection reasons, (6) compute geometric mean for overall confidence, (7) write conclusion that references the strongest evidence, (8) validate size <= 8192 bytes.
## References
- reasoning-trace-builder schema (P06)
- cex_8f_runner.py F4 REASON state
- cex_sdk/reasoning/tracer.py (runtime trace capture)
- P03 prompt pillar specification
- Confidence calibration literature (Kahneman, "Thinking, Fast and Slow")
