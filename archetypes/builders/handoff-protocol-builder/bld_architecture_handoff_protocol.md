---
kind: architecture
id: bld_architecture_handoff_protocol
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of handoff_protocol — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| trigger | Condition that initiates the handoff | handoff_protocol | required |
| context_passed | Data fields transferred from source to target | handoff_protocol | required |
| return_contract | Expected shape and fields of the response | handoff_protocol | required |
| timeout | Max wait time before escalation | handoff_protocol | optional |
| retry_policy | Retry count and backoff on failure | handoff_protocol | optional |
| source_agent | Agent initiating the handoff | P02 | upstream |
| target_agent | Agent receiving the handoff | P02 | downstream |
| dispatch_rule | Routing rule that selects the target | P12 | external |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| trigger | handoff_protocol | produces | Condition that initiates the handoff |
| context_passed | handoff_protocol | produces | Data fields transferred from source to target |
| return_contract | handoff_protocol | produces | Expected shape and fields of the response |
| timeout | handoff_protocol | produces | Max wait time before escalation |
| retry_policy | handoff_protocol | produces | Retry count and backoff on failure |
| source_agent | P02 | depends | Agent initiating the handoff |
| target_agent | P02 | depends | Agent receiving the handoff |
| dispatch_rule | P12 | depends | Routing rule that selects the target |
## Boundary Table
| handoff_protocol IS | handoff_protocol IS NOT |
|-------------|----------------|
| Handoff protocol — trigger conditions, context passed, return contract between agents | dispatch_rule (P12 |
| Not dispatch_rule | dispatch_rule (P12 |
| Not keyword routing) | keyword routing) |
| Not workflow | workflow (P12 |
| Not multi-step orchestration) | multi-step orchestration) |
| Not router | router (P02 |
| Not task routing) | task routing) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | trigger, context_passed, return_contract | Define the artifact's core parameters |
| optional | timeout, retry_policy | Extend with recommended fields |
| external | source_agent, target_agent, dispatch_rule | Upstream/downstream connections |
