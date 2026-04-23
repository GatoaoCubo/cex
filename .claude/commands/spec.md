---
description: "Create a detailed spec from plan + decisions. Usage: /spec [plan_name]"
quality: 9.0
title: "Spec"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - ctx_cex_new_dev_guide
  - p12_wf_orchestration_pipeline
  - spec_n07_operational_intelligence
  - tpl_instruction
  - constraint-spec-builder
  - p12_wf_builder_8f_pipeline
  - output_grid_test_n02
  - bld_config_constraint_spec
  - bld_knowledge_card_context_doc
  - p12_wf_engineering_pipeline
---

# /spec — Blueprint from Plan + Decisions

> **Input**: A `/plan` + a `/guide` manifest (decisions)
> **Output**: A spec in `_docs/specs/` — the exact blueprint for execution
> **Next step**: `/grid` (execute the spec)

## What is a spec?

The CEX standard for "exactly what to build."
See `_docs/specs/` for 7 real examples that built this entire repo.

A spec contains:
- The PROBLEM (why)
- The VISION (what)
- The ARTIFACT LIST (every file, exact path, kind, size estimate)
- The WAVE ORDER (what builds first, second, third)
- The DEPENDENCIES (what needs what)
- The DECISION CONTEXT (from manifest — user's choices)
- The ACCEPTANCE CRITERIA (how we know it's done)

## Steps

### Step 1: Load context

```bash
# Read the plan
cat .cex/runtime/plans/plan_{slug}.md

# Read the decision manifest
cat .cex/runtime/decisions/decision_manifest.yaml

# Read brand config if it exists
cat .cex/brand/brand_config.yaml 2>/dev/null
```

### Step 2: Generate spec

Write to `_docs/specs/spec_{scope}_{slug}.md` with frontmatter:

```yaml
---
id: spec_{slug}
kind: constraint_spec
pillar: P06
title: "Spec — {title}"
version: 1.0.0
created: {date}
author: n07_orchestrator
domain: {domain}
quality_target: 9.0
status: SPEC
scope: {nucleus or scope}
depends_on: {list or null}
tags: [spec, ...]
tldr: "{1 sentence}"
density_score: 0.95
---
```

### Step 3: Artifact table

For EVERY artifact, specify:

```markdown
## Artifacts

### Wave 1: {name} ({count} artifacts)

| Action | Path | Kind | Est. Size | Notes |
|--------|------|------|-----------|-------|
| CREATE | N06_commercial/P03_prompt/brand_interview.md | prompt_template | 4KB | 15 questions |
| REWRITE | N06_commercial/P02_model/agent_commercial.md | agent | 3KB | Add brand caps |
```

Actions: CREATE (new file), REWRITE (existing file changes), MIGRATE (move+adapt)

### Step 4: Decision context

Include the relevant decisions from the manifest:

```markdown
## Decisions (from user)
- Archetype: Sage (DP 1)
- Voice: authoritative, warm (DP 2)
- Audience: career-switchers (DP 3)
- Layout: hero + features + testimonials (DP 4)
```

### Step 5: Acceptance criteria

```markdown
## Done When
- [ ] All {N} artifacts pass doctor
- [ ] All compile successfully
- [ ] Quality >= 9.0 on all scored artifacts
- [ ] E2E test passes (if applicable)
- [ ] Signal sent: n0X → complete → score
```

### Step 6: Present to user

Show the spec summary. Ask: "This is the blueprint. Ready to execute? Type `/grid` to start."

## Spec is NOT execution

`/spec` only SPECIFIES. It does not build, dispatch, or score.
The spec is a CONTRACT between the plan and the execution.

## Examples

See real specs that built this repo:
- `spec_n06_brand_verticalization.md` (348 lines, 32 artifacts)
- `spec_n02_visual_frontend.md` (159 lines, 14 artifacts)
- `spec_n05_railway_superintendent.md` (159 lines, 14 artifacts)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ctx_cex_new_dev_guide]] | related | 0.28 |
| [[p12_wf_orchestration_pipeline]] | related | 0.25 |
| [[spec_n07_operational_intelligence]] | related | 0.24 |
| [[tpl_instruction]] | related | 0.23 |
| [[constraint-spec-builder]] | related | 0.23 |
| [[p12_wf_builder_8f_pipeline]] | related | 0.23 |
| [[output_grid_test_n02]] | related | 0.23 |
| [[bld_config_constraint_spec]] | related | 0.20 |
| [[bld_knowledge_card_context_doc]] | related | 0.20 |
| [[p12_wf_engineering_pipeline]] | related | 0.19 |
