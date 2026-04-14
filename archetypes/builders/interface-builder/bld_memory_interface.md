---
id: p10_lr_interface_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Interface contracts that omit the deprecation path for old methods cause breaking changes when versions are incremented. Methods with input defined but no output (or vice versa) create implicit assumptions that differ between provider and consumer. Using backward_compatible as a string ('yes') instead of a boolean causes schema validation failure. Bilateral contract requirement (both provider and consumer fields) is the most commonly missed structural rule — 4 of 7 early productions had unilateral definitions."
pattern: "Every interface method requires both input schema and output schema. Every versioned interface must declare backward_compatible:bool and a deprecation_path for methods being removed. Both provider and consumer fields are required — an interface without both parties is an incomplete contract. Mock payloads must match method signatures exactly, not be illustrative approximations."
evidence: "7 interface productions reviewed: 4 missing consumer field (unilateral), 3 with output-only or input-only methods, 2 with backward_compatible as string. Mock payload mismatches found in 5 of 7 (payload showed extra or missing fields vs declared schema). Zero breaking changes in deployments using versioned interfaces with deprecation_path vs 3 breaking changes in deployments without."
confidence: 0.70
outcome: SUCCESS
domain: interface
tags: [interface, versioning, backward-compatibility, deprecation, bilateral-contract, methods]
tldr: "Both sides of the contract must be declared. Every method needs input AND output. Deprecation paths prevent breaking changes. backward_compatible is a boolean."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [interface, contract, provider, consumer, versioning, backward_compatible, deprecation, method, bilateral]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Interface"
density_score: 0.90
llm_function: INJECT
---
## Summary
Interfaces define bilateral contracts between a provider and a consumer. The most damaging failure is treating an interface as unilateral — defining only one party. The second most damaging failure is incrementing a version number without declaring what happens to old methods. Both failures cause breaking changes that are expensive to debug after deployment.
## Pattern
Bilateral contract checklist:
1. **Both parties declared** - `provider` and `consumer` fields both required. Name them as components, not roles.
2. **Method completeness** - Every method must have `input` schema and `output` schema. A method with only one side creates implicit assumptions.
3. **Version semantics** - Increment major version when removing or changing method signatures. Increment minor when adding methods. Patch for documentation only.
4. **Backward compatibility** - `backward_compatible: true` means old consumers work without changes. `false` means a migration is required. Declare `deprecation_path` for every method being removed: timeline, replacement method, migration notes.
5. **Mock payload fidelity** - Mock payloads in examples must contain exactly the fields declared in the method schema. No extra fields, no missing fields.
Do not add event handling or runtime state to an interface — those belong in signal and runtime_state artifacts respectively.
## Anti-Pattern
1. `provider` declared but no `consumer` — unilateral definition, incomplete contract.
2. Method with `input` but no `output` — consumer cannot know what to expect.
3. `backward_compatible: "yes"` — must be boolean `true`, string causes schema rejection.
4. Version increment without `deprecation_path` — old consumers break silently.
5. Mock payload with different fields than declared schema — misleads callers about actual behavior.
6. Adding event handling to interface — scope creep into signal territory.
## Context

## Builder Context

This ISO operates within the `interface-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Reference

```yaml
id: p10_lr_interface_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_interface_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | interface |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
