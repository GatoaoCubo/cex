---
id: bld_context_sources_constitutional_rule
kind: knowledge_card
pillar: P11
title: "Constitutional Rule Builder -- Context Sources"
version: 1.0.0
quality: 7.6
tags: [builder, constitutional_rule, context]
llm_function: CONSTRAIN
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_architecture_kind
  - bld_tools_kind
  - bld_collaboration_kind
  - kind-builder
  - bld_instruction_kind
  - bld_examples_handoff
  - bld_collaboration_builder
  - bld_knowledge_card_kind
  - bld_output_template_builder
  - bld_collaboration_quality_gate
---
# Context Sources: constitutional_rule
## Mandatory Loads (F3 INJECT)
| Source | Path | Purpose |
|--------|------|---------|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_constitutional_rule.md | Primary definition |
| Schema | archetypes/builders/constitutional-rule-builder/bld_schema_constitutional_rule.md | Field constraints |
| Template | archetypes/builders/constitutional-rule-builder/bld_output_template_constitutional_rule.md | Structure |
| Examples | archetypes/builders/constitutional-rule-builder/bld_examples_constitutional_rule.md | Golden patterns |
| Guardrail builder | archetypes/builders/guardrail-builder/ | Contrast: soft vs absolute |
| Pillar schema | N00_genesis/P11_feedback/_schema.yaml | Pillar constraints |
## Related Kind KCs
| KC | Relationship |
|----|-------------|
| kc_guardrail.md | soft constraint with bypass (the adjacent kind; know the difference) |
| kc_quality_gate.md | output quality enforcement (not behavioral) |
## External References
| Source | Relevance |
|--------|----------|
| Bai et al. Constitutional AI (2022) | Original CAI paper defining constitutional principles |
| Anthropic Usage Policy | Hardcoded behaviors that cannot be unlocked by operators |
| NIST AI RMF | Trustworthiness dimensions including safety and explainability |
| EU AI Act Art. 5 | Prohibited AI practices (maps to harm_prevention basis) |

## Configuration Checklist

- Verify all required fields are present in frontmatter before saving
- Validate config values against schema constraints (type, range, enum)
- Cross-reference with related configs to avoid contradictions
- Test config loading in target runtime before committing

## Validation

```yaml
# Required config validation
fields_present: true
types_valid: true
ranges_checked: true
cross_refs_verified: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | upstream | 0.37 |
| [[bld_tools_kind]] | upstream | 0.34 |
| [[bld_collaboration_kind]] | downstream | 0.30 |
| [[kind-builder]] | upstream | 0.30 |
| [[bld_instruction_kind]] | upstream | 0.29 |
| [[bld_examples_handoff]] | upstream | 0.29 |
| [[bld_collaboration_builder]] | downstream | 0.27 |
| [[bld_knowledge_card_kind]] | sibling | 0.24 |
| [[bld_output_template_builder]] | upstream | 0.23 |
| [[bld_collaboration_quality_gate]] | related | 0.22 |
