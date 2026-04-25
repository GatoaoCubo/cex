---
id: bld_eval_default
kind: builder_default
pillar: P07
source: shared
title: "Eval Default: Universal Quality Gates + Examples"
llm_function: GOVERN
version: 1.1.0
quality: 7.3
tags: [eval, quality_gate, examples, P07, shared, default]
tldr: "_Shared evaluation: quality gate with scoring dimensions and pass/fail criteria"
related:
  - p03_sp_verification_agent
  - p11_qg_kind_builder
  - bld_instruction_kind
  - bld_knowledge_card_quality_gate
  - p11_qg_creation_artifacts
  - p01_kc_artifact_quality_evaluation_methods
  - p11_qg_builder_nucleus
  - p06_vs_frontmatter
  - bld_examples_validator
  - p01_kc_knowledge_best_practices
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-22"
---

# P07 Eval — Universal Quality Gates

## Hard Gates (H01-H07) — ALL must pass

| Gate | Check | Fail Action |
|------|-------|-------------|
| H01 | Frontmatter present and valid YAML | Return to F6, add frontmatter |
| H02 | `quality: null` in frontmatter (never self-score) | Remove score, set null |
| H03 | Required fields: id, kind, 8f, pillar, title | Add missing fields |
| H04 | Body density >= 0.85 (content lines / total lines) | Add structured data, remove filler |
| H05 | No hallucinated sources (cited paths must exist) | Remove or verify citations |
| H06 | ASCII-only in any generated code blocks | Replace non-ASCII per cex_sanitize rules |
| H07 | Output matches pillar schema constraints | Restructure to match schema |

## Scoring Dimensions (5D)

| Dimension | Weight | Criteria |
|-----------|--------|---------|
| D1 Structural | 30% | Frontmatter complete, naming correct, file in right pillar dir |
| D2 Content | 25% | Density >= 0.85, no filler, tables preferred over prose |
| D3 Accuracy | 20% | No hallucination, sources verified, constraints respected |
| D4 Usefulness | 15% | Actionable, implementable, unambiguous |
| D5 CEX fit | 10% | Kind/pillar/nucleus alignment, 8F stage correctness |

Quality floor: 8.0 (re-draft below this)
Quality target: 9.0+

## Retry Protocol

1. F7 fails -> identify which H gate failed -> return to F6
2. Fix the specific failure only (do not refactor unrelated sections)
3. Re-run F7 -> if pass, proceed to F8
4. Maximum 2 retries -> if still failing, flag to N07 with failure details

## Examples

Good artifacts share these properties:
- Frontmatter block: 8-12 fields, all snake_case keys
- Body: 60-80% tables and structured lists vs prose
- No "TODO", "TBD", or placeholder text in published output
- Cross-references use canonical paths (kind/pillar/nucleus names)

## When to Override This Default

Create `bld_eval_{kind}.md` to override this default when the kind has custom:
- Domain-specific H gates beyond H01-H07
- Non-standard quality floor (e.g., safety kinds require >= 9.5)
- Custom examples that replace the universal examples section

## Builder Checklist

- Verify all required frontmatter fields are present
- Validate body content against schema constraints
- Cross-reference with related artifacts for consistency
- Run quality gate before publishing

## Validation

```yaml
# Quality check
frontmatter: complete
schema: valid
references: checked
gate: passed
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_verification_agent]] | upstream | 0.28 |
| [[p11_qg_kind_builder]] | downstream | 0.27 |
| [[bld_instruction_kind]] | upstream | 0.27 |
| [[bld_knowledge_card_quality_gate]] | downstream | 0.27 |
| [[p11_qg_creation_artifacts]] | downstream | 0.26 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.26 |
| [[p11_qg_builder_nucleus]] | downstream | 0.26 |
| [[p06_vs_frontmatter]] | upstream | 0.25 |
| [[bld_examples_validator]] | related | 0.24 |
| [[p01_kc_knowledge_best_practices]] | upstream | 0.24 |
