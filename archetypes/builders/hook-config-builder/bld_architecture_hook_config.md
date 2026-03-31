---
kind: architecture
id: bld_architecture_hook_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of hook_config — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| phases | 8F pipeline phases where hooks can bind | hook_config | required |
| events | Event types (pre-build, post-build, on-error, quality-fail) | hook_config | required |
| actions | What each hook triggers (script, signal, validator) | hook_config | required |
| conditions | When a hook fires (always, on-fail, on-score-below) | hook_config | required |
| priority | Execution order when multiple hooks bind same event | hook_config | optional |
| hook | Implementation code that runs when event fires | P04 | consumer |
| lifecycle_rule | Archive/promote policy triggered by hooks | P04 | consumer |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| phases | hook_config | produces | 8F pipeline phase declarations |
| events | hook_config | produces | Event type bindings |
| actions | hook_config | produces | Action declarations per hook |
| conditions | hook_config | produces | Conditional firing rules |
| priority | hook_config | produces | Execution order for same-event hooks |
| hook | P04 | depends | Implementation code bound to events |
| lifecycle_rule | P04 | depends | Policy triggered by hook events |
## Boundary Table
| hook_config IS | hook_config IS NOT |
|----------------|-------------------|
| Declaration of which hooks fire and when | hook (implementation code) |
| Event binding configuration per build phase | lifecycle_rule (archive/promote policy) |
| Conditional firing rules for pipeline events | plugin (extension module) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | phases, events, actions, conditions | Define the artifact's core declarations |
| optional | priority | Extend with execution ordering |
| external | hook, lifecycle_rule | Downstream consumers of declarations |
