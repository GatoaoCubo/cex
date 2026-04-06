---
kind: architecture
id: bld_architecture_reasoning_trace
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of reasoning_trace — inventory, dependencies, and architectural position
---

# Architecture: reasoning_trace in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata (id, kind, pillar, agent, intent, timestamp, quality) | reasoning-trace-builder | active |
| step_chain | Ordered list of step-evidence-confidence triplets | reasoning-trace-builder | active |
| conclusion | Final decision summary referencing strongest evidence | reasoning-trace-builder | active |
| alternatives_rejected | List of rejected paths with evidence-based rejection reasons | reasoning-trace-builder | active |
| confidence_score | Geometric mean of step confidences (0.0-1.0) | reasoning-trace-builder | active |
| duration_ms | Timing data for performance analysis | system | active |
| feedback_flag | Low-confidence marker triggering memory feedback loop | system | active |
## Dependency Graph
```
agent/agent_node  --reasons-->      reasoning_trace  --audited_by-->    human_reviewer
reasoning_trace   --feeds_back-->   memory_system    --improves-->      future_decisions
reasoning_trace   --consumed_by-->  quality_gate     --validates-->     confidence_calibration
8f_pipeline_F4    --produces-->     reasoning_trace  --archived_in-->   P03_prompt/compiled/
```
| From | To | Type | Data |
|------|----|------|------|
| agent/agent_node (P02) | reasoning_trace | produces | agent records its decision chain during F4 REASON |
| reasoning_trace | human_reviewer | consumes | auditor reviews trace to understand WHY a decision was made |
| reasoning_trace | memory_system (P10) | data_flow | low-confidence traces feed learning records for future improvement |
| reasoning_trace | quality_gate (P11) | validates | gate checks trace completeness, evidence density, confidence calibration |
| 8f_pipeline F4 REASON | reasoning_trace | produces | F4 state.reasoning generates the trace as a byproduct of planning |
| cex_sdk/reasoning/tracer.py | reasoning_trace | runtime | SDK tracer captures live reasoning into trace format |
| instruction (P03) | reasoning_trace | dependency | the instruction that triggered the decision being traced |
## Boundary Table
| reasoning_trace IS | reasoning_trace IS NOT |
|--------------------|------------------------|
| A structured decision record capturing WHY | An execution instruction telling WHAT to do (instruction P03) |
| Step-evidence-confidence chain with audit trail | A system prompt defining agent identity (system_prompt P03) |
| Immutable once emitted — corrections produce new traces | A mutable state that evolves during execution |
| Consumed by auditors and feedback loops | A workflow step graph (workflow_primitive P12) |
| YAML for human readability and auditability | JSON wire format (that belongs to signal P12) |
| Scoped to one decision chain from one agent | A multi-agent coordination artifact |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Capture | agent, intent, timestamp, duration_ms | Identify who reasoned, about what, and when |
| Reasoning | step_chain (thought + evidence + confidence) | Record the complete chain of reasoning |
| Decision | conclusion, alternatives_rejected | Document the final choice and rejected paths |
| Feedback | confidence_score, feedback_flag | Enable quality assessment and learning loops |
