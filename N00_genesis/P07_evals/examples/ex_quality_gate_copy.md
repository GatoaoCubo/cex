---
id: ex_quality_gate_copy
kind: quality_gate
8f: F7_govern
pillar: P07
title: Copywriting Quality Gate
tags: [quality, gate, copy, evaluation]
references:
  - tpl_quality_gate
  - ex_agent_copywriter
  - ex_response_format_ad_copy
  - ex_prompt_template_aida
quality: 9.1
updated: "2026-04-07"
domain: "evaluation and testing"
version: "1.0.0"
author: n03_builder
created: "2026-04-07"
density_score: 0.95
tldr: "Defines the quality gate specification for copywriting quality gate, with structural rules, validation gates, and integration points."
related:
  - quality-gate-builder
  - bld_examples_quality_gate
  - skill
  - bld_architecture_quality_gate
  - bld_tools_quality_gate
  - bld_collaboration_quality_gate
  - bld_config_quality_gate
  - p03_ins_quality_gate
  - bld_examples_eval_dataset
  - bld_memory_quality_gate
---
tldr: "Quality gate for copywriting: checks tone, CTA clarity, length, and brand voice compliance."
quality: 8.5
tldr: "Quality gate for copywriting: checks tone, CTA clarity, length, and brand voice compliance."
quality: 8.5
---

# Copywriting Quality Gate

> Skeleton: quality_gate kind (self-evaluation criteria)

| Criterion | Minimum | Weight |
|-----------|---------|--------|
| Clarity | >= 8 | 25% |
| Persuasion | >= 9 | 30% |
| Specificity | >= 8 | 20% |
| CTA strength | >= 9 | 25% |

Fail action: regenerate with feedback on weakest criterion.

## Links

- Evaluates: [[ex_agent_copywriter]]
- Checks format: [[ex_response_format_ad_copy]]
- Checks method: [[ex_prompt_template_aida]]
- Function: GOVERN (is it good enough?)

## Cross-References

- **Pillar**: P07 (Evals)
- **Kind**: `quality gate`
- **Artifact ID**: `ex_quality_gate_copy`
- **Tags**: [quality, gate, copy, evaluation]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P07 | Evals domain |
| Kind `quality gate` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P07 (Evals)
- **Kind**: `quality gate`
- **Artifact ID**: `ex_quality_gate_copy`
- **Tags**: [quality, gate, copy, evaluation]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P07 | Evals domain |
| Kind `quality gate` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Validation Command

```bash
# Score a single artifact against this gate
python _tools/cex_score.py --apply --verbose artifact.md
```

```bash
# Batch validation
python _tools/cex_score.py --apply N03_builder/*.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[quality-gate-builder]] | downstream | 0.33 |
| [[bld_examples_quality_gate]] | related | 0.25 |
| [[skill]] | downstream | 0.23 |
| [[bld_architecture_quality_gate]] | downstream | 0.23 |
| [[bld_tools_quality_gate]] | upstream | 0.21 |
| [[bld_collaboration_quality_gate]] | downstream | 0.21 |
| [[bld_config_quality_gate]] | downstream | 0.21 |
| [[p03_ins_quality_gate]] | downstream | 0.20 |
| [[bld_examples_eval_dataset]] | related | 0.20 |
| [[bld_memory_quality_gate]] | downstream | 0.20 |
