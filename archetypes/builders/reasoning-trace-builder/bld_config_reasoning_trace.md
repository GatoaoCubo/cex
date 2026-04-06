---
kind: config
id: bld_config_reasoning_trace
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
---
# Config: reasoning_trace Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p03_rt_{agent}_{timestamp}.yaml` | `p03_rt_research_agent_20260406T143000.yaml` |
| Builder directory | kebab-case | `reasoning-trace-builder/` |
| Trace fields | snake_case | `alternatives_rejected`, `duration_ms` |
| Step labels | sequential integers | `1`, `2`, `3` |
| Agent values | lowercase slug | `research-agent`, `build-sat` |
Rule: use `.yaml` only for this builder — traces are human-readable audit records.
## File Paths
- Output: `cex/P03_prompt/compiled/p03_rt_{agent}_{timestamp}.yaml`
- Human reference: `cex/P03_prompt/examples/p03_rt_{agent}_{timestamp}.md`
## Size Limits
- Preferred trace size: <= 4096 bytes
- Absolute max: 8192 bytes
- Steps should be concise: thought + evidence in 1-2 sentences each
- Cap step count at 10 — more than 10 steps indicates the decision should be decomposed
## Trace Restrictions
- Required fields must appear exactly as defined in schema
- Omit optional null/unknown fields instead of writing placeholders
- `duration_ms` allowed only when timing data is genuinely available
- Each step MUST have non-empty `thought`, `evidence`, and `confidence`
- Confidence values must be numeric 0.0-1.0, not strings or percentages
- Overall confidence is geometric mean of step confidences, not arithmetic mean
## Boundary Restrictions
- No execution instructions, tool calls, or action items inside the trace
- No workflow step definitions, DAGs, or sequencing logic
- No system prompt content, persona definitions, or agent identity
- No routing tables, dispatch rules, or agent selection logic
## Feedback Loop Rules
- Traces with overall confidence < 0.5 trigger memory feedback: write learning record
- Traces with any single step confidence < 0.2 flag that step for human review
- Traces are immutable once emitted — corrections produce a new trace, never mutate
