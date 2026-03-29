---
kind: architecture
id: bld_architecture_decision_record
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of decision_record — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| context | Circumstances and forces that made the decision necessary | decision_record | required |
| decision | The chosen option and primary rationale | decision_record | required |
| status | Lifecycle state of the ADR (proposed/accepted/deprecated/superseded) | decision_record | required |
| options | Alternatives considered with pros and cons | decision_record | required (>= 2) |
| consequences | Positive, negative, and neutral effects of the decision | decision_record | required |
| supersedes | Reference to older ADR this record replaces | decision_record | conditional |
| superseded_by | Reference to newer ADR that replaces this record | decision_record | conditional |
| related_to | References to architecturally related ADRs | decision_record | optional |
| deciders | Named individuals or roles who ratified the decision | decision_record | optional |
| date_decided | Date the decision was finalized | decision_record | optional |
| law | Inviolable system rule derived from accepted ADR | P08 | external consumer |
| pattern | Reusable prescriptive solution that may implement an ADR's choice | P08 | external consumer |
| agent | Runtime component subject to a decision's constraints | P02 | external consumer |
## Dependency Graph
```
context       --produces--> decision
options       --produces--> decision
decision      --produces--> consequences
status        --governs-->  decision
supersedes    --links-->    decision
superseded_by --links-->    decision
related_to    --links-->    decision
decision      --informs-->  law (if decision becomes inviolable)
decision      --informs-->  pattern (if decision becomes reusable prescription)
decision      --constrains--> agent (runtime behavior shaped by decision)
```
| From | To | Type | Data |
|------|----|------|------|
| context | decision | produces | forces and constraints that shaped the choice |
| options | decision | produces | evaluated alternatives proving deliberation |
| decision | consequences | produces | downstream effects of the chosen option |
| status | decision | governs | lifecycle state (proposed -> accepted -> deprecated/superseded) |
| supersedes | decision | links | backward reference to replaced ADR |
| superseded_by | decision | links | forward reference to replacing ADR |
| decision | law | informs | if the decision becomes a non-negotiable system constraint |
| decision | pattern | informs | if the chosen approach becomes a reusable prescription |
| decision | agent | constrains | runtime behavior shaped by the accepted decision |
## Boundary Table
| decision_record IS | decision_record IS NOT |
|-------------------|----------------------|
| A permanent record of a single significant architectural choice | A law (inviolable constraint that cannot be overridden — use law-builder) |
| Documents context, options, rationale, and consequences | A pattern (reusable prescriptive solution to recurring problems — use pattern-builder) |
| Has a status lifecycle: proposed -> accepted -> deprecated/superseded | A diagram (visual representation of structure — use diagram-builder) |
| Revisable: future teams can create superseding ADRs | A knowledge card (reference knowledge without a decision — use knowledge-card-builder) |
| Preserves history: deprecated/superseded ADRs are kept, never deleted | An implementation guide (how-to instructions — use instruction-builder) |
| Records a choice made at a specific point in time | A specification of how something works today |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| evidence | context, options | Supply the information needed to evaluate the decision |
| decision | decision, status, date_decided, deciders | Capture the choice, its timing, and who ratified it |
| effects | consequences | Document what changes as a result of the decision |
| links | supersedes, superseded_by, related_to | Maintain the traversable decision history chain |
| consumers | law, pattern, agent | Downstream artifacts shaped by accepted decisions |
