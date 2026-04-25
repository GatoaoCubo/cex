---
id: p11_fb_knowledge_graph
kind: builder_default
pillar: P11
title: "Feedback: Knowledge Graph"
domain: knowledge_graph
version: 1.1.0
quality: 8.4
tags: [feedback, anti-patterns, P11, knowledge_graph]
tldr: "Knowledge Graph feedback: anti-patterns, regression signals, and quality improvement triggers"
related:
  - bld_instruction_knowledge_card
  - p03_sp_n03_creation_nucleus
  - p03_sp_system-prompt-builder
  - p10_lr_golden_test_builder
  - p03_sp__builder_builder
  - p03_sp_golden_test_builder
  - bld_examples_axiom
  - p06_vs_frontmatter
  - bld_examples_response_format
  - bld_schema_kind
author: builder
llm_function: GOVERN
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-22"
---

# Feedback: Knowledge Graph

## Anti-Patterns (NEVER do)

- **No self-score**: never assign quality score to your own output
- **No hallucination**: cite sources; do not invent facts, metrics, or references
- **ASCII-only code**: no emoji, no accented chars in .py/.ps1/.sh output
- **No partial output**: produce complete artifact; no truncation, no "..." placeholders
- **No frontmatter omission**: every artifact must start with valid YAML frontmatter
- **No quality below 8.0**: re-draft before publishing if self-assessment < 8.0

## Common Failure Modes for Knowledge Graph

- Vague identity section (no concrete capabilities, tools, or constraints)
- Missing required frontmatter fields (id, kind, pillar, quality: null)
- Body prose only -- no tables, no structured data (density < 0.85)
- Output not matching the output template schema

## Correction Protocol

1. Identify which H01-H07 gate failed
2. Return to F6 PRODUCE with explicit fix instruction
3. Re-run F7 GOVERN
4. Maximum 2 retries before escalating to N07

## Key Behaviors

- Builder MUST load all 12 ISOs (1:1 with pillars) before producing any artifact
- Builder MUST run F7 GOVERN quality gate before saving output
- Builder MUST compile output via cex_compile.py after saving (F8 COLLABORATE)
- Builder MUST signal completion with quality score to N07 orchestrator
- Builder MUST NOT self-score: quality field is always null in own output
## Quality Thresholds

| Dimension | Weight | Target | Gate |
|-----------|--------|--------|------|
| Structural completeness | 30% | >= 8.0 | L1 |
| Rubric compliance | 30% | >= 8.0 | L2 |
| Semantic coherence | 40% | >= 8.5 | L3 |
| Density score | -- | >= 0.85 | S09 |
| Tables present | -- | >= 1 | S05 |

## Gate Check

```bash
python _tools/cex_score.py {FILE} --layer structural
python _tools/cex_score.py {FILE} --layer rubric
```

```yaml
# Expected output structure
structural: 8.5+
rubric: 7.5+
average: 8.0+
gates_passed: 7/7
density: 0.85+
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_knowledge_card]] | upstream | 0.22 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.21 |
| [[p03_sp_system-prompt-builder]] | upstream | 0.21 |
| [[p10_lr_golden_test_builder]] | upstream | 0.21 |
| [[p03_sp__builder_builder]] | upstream | 0.20 |
| [[p03_sp_golden_test_builder]] | upstream | 0.20 |
| [[bld_examples_axiom]] | upstream | 0.20 |
| [[p06_vs_frontmatter]] | upstream | 0.20 |
| [[bld_examples_response_format]] | upstream | 0.20 |
| [[bld_schema_kind]] | upstream | 0.19 |
