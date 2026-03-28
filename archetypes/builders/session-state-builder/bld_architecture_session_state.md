---
kind: architecture
id: bld_architecture_session_state
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of session_state — inventory, dependencies, and architectural position
---

# Architecture: session_state in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, session_id, agent, timestamp, etc.) | session-state-builder | active |
| context_snapshot | Current context window contents and token usage | agent | active |
| checkpoint_data | Resumable state for crash recovery or context overflow | agent | active |
| active_tasks | List of in-progress tasks with status and progress | agent | active |
| tool_state | Current tool invocations and pending results | agent | active |
| token_budget | Remaining token allocation and compression status | agent | active |
## Dependency Graph
```
agent           --produces-->   session_state  --consumed_by-->  recovery_system
session_state   --feeds-->      learning_record  --signals-->    checkpoint_event
session_state   --consumed_by-->  context_manager
```
| From | To | Type | Data |
|------|----|------|------|
| agent (P02) | session_state | produces | agent dumps current state as ephemeral snapshot |
| session_state | recovery_system | consumes | checkpoint data used for crash recovery |
| session_state | learning_record (P10) | data_flow | session data distilled into persistent learning |
| session_state | context_manager | consumes | context manager reads token budget and usage |
| session_state | checkpoint_event (P12) | signals | emitted when checkpoint is saved |
| runtime_state (P10) | session_state | dependency | runtime state provides initial values for session |
## Boundary Table
| session_state IS | session_state IS NOT |
|------------------|----------------------|
| An ephemeral snapshot of current session context | A persistent record of accumulated experience (learning_record P10) |
| Discarded when session ends — not cross-session | A variable state that persists across sessions (runtime_state P10) |
| Contains token usage, active tasks, and checkpoints | A design-time cognitive map (mental_model P02) |
| Used for crash recovery and context overflow management | A search index or knowledge base (brain_index P01) |
| Scoped to one session of one agent | A shared state across multiple agents |
| Lightweight snapshot with minimal overhead | A comprehensive audit log of all actions |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | agent, runtime_state | Agent execution produces session data |
| Snapshot | frontmatter, context_snapshot, token_budget | Capture current context and resource usage |
| Tasks | active_tasks, tool_state | Track in-progress work and pending tool results |
| Recovery | checkpoint_data, recovery_system | Enable crash recovery and context overflow handling |
| Downstream | learning_record, checkpoint_event | Distill persistent learning and signal checkpoints |
