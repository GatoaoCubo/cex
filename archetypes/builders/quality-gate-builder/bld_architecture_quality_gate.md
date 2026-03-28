---
kind: architecture
id: bld_architecture_quality_gate
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of quality_gate — inventory, dependencies, and architectural position
---

# Architecture: quality_gate in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target_kind, pass_threshold, etc.) | quality-gate-builder | active |
| hard_gates | Blocking checks that must pass — artifact rejected on failure | author | active |
| soft_gates | Score-contributing checks that degrade quality score but do not block | author | active |
| scoring_formula | Weighted combination of soft gate scores into final quality number | author | active |
| pass_threshold | Minimum score required to pass the gate | author | active |
| bypass_policy | Conditions and audit requirements for overriding a failed gate | author | active |
## Dependency Graph
```
artifact (any)  --evaluated_by-->  quality_gate  --produces-->    pass_fail_result
scoring_rubric  --depends-->       quality_gate  --signals-->     gate_event
validator       --depends-->       quality_gate
```
| From | To | Type | Data |
|------|----|------|------|
| artifact (any) | quality_gate | data_flow | artifact submitted for quality evaluation |
| quality_gate | pass_fail_result | produces | boolean pass/fail plus numeric score |
| scoring_rubric (P07) | quality_gate | dependency | rubric dimensions inform gate criteria |
| validator (P06) | quality_gate | dependency | validators implement individual hard gate checks |
| quality_gate | gate_event (P12) | signals | emitted on pass, fail, or bypass |
| quality_gate | lifecycle_rule (P11) | data_flow | gate scores may trigger lifecycle transitions |
## Boundary Table
| quality_gate IS | quality_gate IS NOT |
|-----------------|---------------------|
| A barrier with HARD (block) and SOFT (score) checks | A technical pass/fail validation rule (validator P06) |
| Produces a numeric quality score from weighted formula | An evaluation criteria framework (scoring_rubric P07) |
| Applied before artifact is accepted into a pool or promoted | A fix-verify cycle for broken artifacts (bugloop P11) |
| Includes bypass policy with audit trail | A safety restriction on agent behavior (guardrail P11) |
| Targets a specific artifact kind with kind-aware criteria | A continuous optimization loop (optimizer P11) |
| Binary outcome (pass/fail) plus score for ranking | A subjective review without numeric scoring |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Input | artifact, scoring_rubric | Artifact under evaluation and criteria reference |
| Hard Checks | hard_gates, validator | Blocking checks that must pass |
| Soft Checks | soft_gates, scoring_formula | Score-contributing checks with weighted combination |
| Decision | pass_threshold, bypass_policy | Pass/fail determination and override rules |
| Output | pass_fail_result, gate_event | Result delivered and event signaled downstream |
