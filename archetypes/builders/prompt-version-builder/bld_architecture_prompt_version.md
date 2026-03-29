---
kind: architecture
id: bld_architecture_prompt_version
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of prompt_version — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| prompt_ref | Reference to the prompt_template being versioned | prompt_version | required |
| version | Semantic version of this snapshot | prompt_version | required |
| author | Who created this version | prompt_version | required |
| metrics | Performance metrics for this version | prompt_version | optional |
| ab_group | A/B test group assignment (control, variant_a, variant_b) | prompt_version | optional |
| parent_version | Previous version this evolved from | prompt_version | optional |
| prompt_template | The mutable template this snapshots | P03 | upstream |
| eval | Evaluation results validating this version | P07 | downstream |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| prompt_ref | prompt_version | produces | Reference to the prompt_template being versioned |
| version | prompt_version | produces | Semantic version of this snapshot |
| author | prompt_version | produces | Who created this version |
| metrics | prompt_version | produces | Performance metrics for this version |
| ab_group | prompt_version | produces | A/B test group assignment (control, variant_a, variant_b) |
| parent_version | prompt_version | produces | Previous version this evolved from |
| prompt_template | P03 | depends | The mutable template this snapshots |
| eval | P07 | depends | Evaluation results validating this version |
## Boundary Table
| prompt_version IS | prompt_version IS NOT |
|-------------|----------------|
| Prompt version — immutable snapshot of a prompt at a point in time with metrics and lineage | prompt_template (P03 |
| Not prompt_template | prompt_template (P03 |
| Not mutable template) | mutable template) |
| Not system_prompt | system_prompt (P03 |
| Not agent identity) | agent identity) |
| Not action_prompt | action_prompt (P03 |
| Not task prompt) | task prompt) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | prompt_ref, version, author | Define the artifact's core parameters |
| optional | metrics, ab_group, parent_version | Extend with recommended fields |
| external | prompt_template, eval | Upstream/downstream connections |
