---
id: bld_context_sources_constitutional_rule
kind: knowledge_card
pillar: P11
title: "Constitutional Rule Builder -- Context Sources"
version: 1.0.0
quality: null
tags: [builder, constitutional_rule, context]
llm_function: INJECT
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
