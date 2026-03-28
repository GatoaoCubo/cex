---
kind: tools
id: bld_tools_validator_builder_codex
pillar: P04
llm_function: EXECUTE
purpose: Tools and inputs used by validator-builder-codex
pattern: read constraints, compose validator, validate against gates
---

# Tools: validator-builder-codex
## Primary Inputs
- `P06_schema/_schema.yaml` -> canonical kind definition for `validator`
- `P06_schema/templates/tpl_validator.md` -> legacy production template
- `P06_schema/examples/*.md` -> style and density references
- `archetypes/SEED_BANK.yaml` -> canonical seeds
- `archetypes/TAXONOMY_LAYERS.yaml` -> boundary validation
## Working Methods
- Read schema before composing template text
- Prefer explicit enums, regexes, comparisons, and thresholds
- Reuse known trigger values: `pre_commit`, `post_generate`, `pre_pool`, `on_signal`
- Reuse known severity values: `block`, `warn`, `info`
## Validation Support
Primary: manual check against `QUALITY_GATES.md`
Interim compiled view: derive a YAML form from markdown sections
[PLANNED] validator CLI: `python _tools/validate_artifact.py --kind validator <file>`
