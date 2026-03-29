---
kind: knowledge_card
id: bld_knowledge_card_handoff_protocol
pillar: P02
llm_function: INJECT
purpose: Domain knowledge for handoff_protocol production
sources: A2A protocol spec (Google), Swarm handoff patterns, multi-agent orchestration research, CODEXA satellite dispatch
---

# Domain Knowledge: handoff_protocol
## Executive Summary
Handoff protocol — trigger conditions, context passed, return contract between agents. Produced as P02 artifacts with concrete parameters and rationale.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 |
| llm_function | COLLABORATE |
| Max bytes | 2048 |
| Density min | 0.8 |
| Machine format | yaml |
## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Fire-and-forget | Source sends task, does not wait for result | Async logging, notifications, non-blocking side effects |
| Request-response | Source sends task and blocks until result returns | Sequential pipelines, dependent computations |
| Streaming | Target sends incremental results back to source | Long-running tasks with progress updates |
| Escalation | Target cannot complete, escalates back with partial context | Error recovery, human-in-the-loop |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No return contract | Caller cannot validate or use result — silent type mismatch |
| Passing full context | Token waste; pass only what target needs |
| No timeout | Hung handoff blocks entire pipeline indefinitely |
| Implicit trigger | Handoff fires on vague conditions, causing spurious delegations |
## Application
1. Identify the use case and constraints
2. Select appropriate pattern from the table above
3. Define concrete parameter values with rationale
4. Validate against SCHEMA.md required fields
5. Check body size <= 2048 bytes
6. Verify id matches `^p02_handoff_[a-z][a-z0-9_]+$`
## References
- Google A2A Task lifecycle, OpenAI Swarm Handoff, Anthropic tool_use handoff, CrewAI delegation, AutoGen handoff
- A2A protocol spec (Google), Swarm handoff patterns, multi-agent orchestration research, CODEXA satellite dispatch
