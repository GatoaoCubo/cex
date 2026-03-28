---
kind: architecture
id: bld_architecture_validator_builder_codex
pillar: P08
llm_function: DESIGN
purpose: Dependency map and architecture of validator-builder-codex
pattern: validator derives from schema and feeds governance/orchestration layers
---

# Architecture: validator-builder-codex
## Position In Taxonomy
- Layer: `governance`
- Pillar: `P06`
- Kind: `validator`
- Core: `true`
## Dependency Flow
1. `P06_schema/_schema.yaml` -> defines canonical validator boundary
2. `SEED_BANK.yaml` -> supplies validator seeds
3. `TAXONOMY_LAYERS.yaml` -> resolves overlap with P07/P11
4. Builder output -> `P06_schema/examples/` markdown validator
5. Compiled form -> `P06_schema/compiled/` YAML validator
## Upstream Inputs
- schema constraints
- domain law or template being enforced
- artifact family to validate
## Downstream Consumers [PLANNED]
- hook builders needing pre-commit enforcement
- workflow builders needing pass/fail guards
- quality-gate builders consuming validator outcomes as evidence
## Design Rule
Validator defines HOW to reject a concrete violation.
It does not decide publication policy or weighted scoring.
