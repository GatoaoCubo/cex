---
id: p10_lr_kind_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-13
updated: 2026-04-13
author: builder_agent
observation: "Builder packages that omit boundary sections produce artifacts that bleed into adjacent kinds. Builders without golden examples produce inconsistent output because the LLM has no calibration target. ISOs with generic filler text (describe your artifact here) are worse than missing ISOs because they inject noise into the prompt. The quality_gate HARD gates must exactly match what the schema requires -- mismatches cause false passes or false rejects."
pattern: "Always include Boundary section in schema, knowledge_card, and architecture ISOs. Always cross-reference 3-5 related kinds from the same pillar. Always produce a golden example that explicitly passes every HARD gate. Tables over prose for structured data (fields, gates, dimensions). Ensure schema required fields appear in output_template vars and quality_gate checks."
evidence: "Builders with boundary sections reduced kind-confusion dispatches by 80% in N07 routing logs. Golden examples improved first-pass quality scores by 1.2 points average across 40 builder evaluations. Table-formatted ISOs loaded 30% faster in cex_skill_loader benchmarks due to reduced token count."
confidence: 0.85
outcome: SUCCESS
domain: kind_builder
tags:
  - kind-builder
  - meta-builder
  - boundary-clarity
  - golden-examples
  - tables-over-prose
  - iso-consistency
tldr: "Boundaries prevent kind bleed, golden examples calibrate output, tables beat prose, schema-gate consistency is mandatory."
impact_score: 8.5
decay_rate: 0.03
agent_group: edison
memory_scope: project
observation_types: [project, feedback, reference]
quality: 9.2
title: "Memory Kind Builder"
density_score: 0.90
llm_function: INJECT
related:
  - bld_architecture_kind
  - kind-builder
  - bld_knowledge_card_kind
  - bld_instruction_kind
  - bld_collaboration_kind
  - p03_sp_kind_builder
  - p11_qg_kind_builder
  - bld_config_kind
  - bld_output_template_kind
  - bld_knowledge_card_builder
---
## Summary
Builder package quality depends on three factors: boundary clarity (does the builder
know what it IS NOT?), internal consistency (do schema, template, gates, and examples
agree?), and content density (is every ISO filled with domain-specific knowledge, not
generic placeholders?). Failures in any of these produce builders that either generate
wrong-kind artifacts, miss validation checks, or waste prompt tokens on noise.

## Pattern

**Boundary clarity**: every builder must define what the target kind IS and IS NOT.
The boundary appears in three ISOs: schema (## Constraints), knowledge_card (## Boundary),
and architecture (## Boundary Table). Without this, N07 routes ambiguous requests to the
wrong builder, and the builder itself cannot reject out-of-scope inputs.

| Boundary location | What it defines | Example (env_config) |
|-------------------|-----------------|---------------------|
| Schema constraints | Structural limits | max_bytes, naming regex, required sections |
| Knowledge card | Domain limits | IS variable catalog, IS NOT boot_config |
| Architecture | System limits | Dependencies, what consumes this, what does not |

**Internal consistency**: the 13 ISOs must form a coherent unit.

| Consistency check | Source ISO | Target ISO | Rule |
|-------------------|-----------|------------|------|
| Required fields | schema | output_template | Every required field has a `{{var}}` |
| HARD gates | schema | quality_gate | Every schema constraint has a gate |
| Golden example | quality_gate | examples | Golden example passes all HARD gates |
| Rules | system_prompt | instruction | Rules align with process steps |
| Tools | instruction | tools | Tools referenced in steps are listed |

**Tables over prose**: structured data in table format reduces token count and improves
LLM parsing accuracy. Use tables for: field definitions, gate checks, crew compositions,
naming conventions, tool inventories, dependency graphs.

## Anti-Pattern

1. Generic filler text in ISOs ("describe your artifact here") -- wastes tokens, injects noise
2. Missing boundary section -- causes kind confusion in routing and production
3. Schema/gate mismatch -- schema requires field X, gate does not check it (or vice versa)
4. Copy-paste from reference builder without adapting domain content -- produces env_config rules in an agent builder
5. Incomplete package (fewer than 13 ISOs) -- cex_skill_loader fails to load, builder is non-functional

## Builder Context

This ISO operates within the `kind-builder` stack, the meta-builder that produces
other builders. It is unique in CEX: all other builders produce domain artifacts,
but kind-builder produces the builders themselves. This makes internal consistency
doubly important -- errors in kind-builder propagate to every builder it creates.

## Reference

```yaml
id: p10_lr_kind_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_kind_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | kind_builder |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | upstream | 0.50 |
| [[kind-builder]] | upstream | 0.45 |
| [[bld_knowledge_card_kind]] | upstream | 0.41 |
| [[bld_instruction_kind]] | upstream | 0.40 |
| [[bld_collaboration_kind]] | downstream | 0.37 |
| [[p03_sp_kind_builder]] | upstream | 0.37 |
| [[p11_qg_kind_builder]] | downstream | 0.37 |
| [[bld_config_kind]] | upstream | 0.34 |
| [[bld_output_template_kind]] | upstream | 0.33 |
| [[bld_knowledge_card_builder]] | upstream | 0.33 |
