---
kind: output_template
id: bld_output_template_quality_gate
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for quality_gate production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.0
title: "Output Template Quality Gate"
version: "1.0.0"
author: n03_builder
tags: [quality_gate, builder, examples]
tldr: "Golden and anti-examples for quality gate construction, demonstrating ideal structure and common pitfalls."
domain: "quality gate construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - quality-gate-builder
  - bld_examples_quality_gate
  - bld_knowledge_card_quality_gate
  - bld_output_template_scoring_rubric
  - bld_schema_quality_gate
  - bld_config_quality_gate
  - p03_ins_quality_gate
  - bld_memory_quality_gate
  - p11_qg_quality_gate
  - bld_output_template_experiment_config
---

# Output Template: quality_gate
```yaml
id: p11_qg_{{gate_slug}}
kind: quality_gate
pillar: P11
title: "Gate: {{gate_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{what_domain_this_protects}}"
quality: null
tags: [quality-gate, {{domain}}, {{scope}}]
tldr: "{{one_sentence_what_gate_enforces}}"
density_score: {{0.80_to_1.00}}
## Definition
| Property | Value |
|----------|-------|
| Metric | {{metric_name}} |
| Threshold | {{numeric_value}} |
| Operator | {{>= / <= / == / !=}} |
| Scope | {{where_gate_applies}} |
## Checklist (HARD gates — ALL must pass)
1. [ ] {{check_1}}: {{description}}
2. [ ] {{check_2}}: {{description}}
3. [ ] {{check_3}}: {{description}}
## Scoring (SOFT gates — weighted dimensions)
| Dimension | Weight | Criteria |
|-----------|--------|----------|
| {{dim_1}} | {{pct}}% | {{what_to_check}} |
| {{dim_2}} | {{pct}}% | {{what_to_check}} |
| {{dim_3}} | {{pct}}% | {{wha

## Metadata

```yaml
id: bld_output_template_quality_gate
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-output-template-quality-gate.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[quality-gate-builder]] | downstream | 0.36 |
| [[bld_examples_quality_gate]] | downstream | 0.32 |
| [[bld_knowledge_card_quality_gate]] | downstream | 0.31 |
| [[bld_output_template_scoring_rubric]] | sibling | 0.30 |
| [[bld_schema_quality_gate]] | downstream | 0.29 |
| [[bld_config_quality_gate]] | downstream | 0.28 |
| [[p03_ins_quality_gate]] | downstream | 0.27 |
| [[bld_memory_quality_gate]] | downstream | 0.27 |
| [[p11_qg_quality_gate]] | downstream | 0.26 |
| [[bld_output_template_experiment_config]] | sibling | 0.25 |
