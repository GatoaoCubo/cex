---
description: "Create a detailed spec (PSPEC) from plan + decisions. Usage: /spec [plan_name]"
---

# /spec — Blueprint from Plan + Decisions

> **Input**: A `/plan` + a `/guide` manifest (decisions)
> **Output**: A PSPEC in `_docs/pspecs/` — the exact blueprint for execution
> **Next step**: `/grid` (execute the spec)

## What is a PSPEC?

A **Production Specification** — the CEX standard for "exactly what to build."
See `_docs/pspecs/` for 7 real examples that built this entire repo.

A PSPEC contains:
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

### Step 2: Generate PSPEC

Write to `_docs/pspecs/PSPEC_{SCOPE}_{SLUG}.md` with frontmatter:

```yaml
---
id: pspec_{slug}
kind: constraint_spec
pillar: P06
title: "PSPEC — {title}"
version: 1.0.0
created: {date}
author: n07_orchestrator
domain: {domain}
quality_target: 9.0
status: SPEC
scope: {nucleus or scope}
depends_on: {list or null}
tags: [pspec, ...]
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
| CREATE | N06_commercial/prompts/brand_interview.md | prompt_template | 4KB | 15 questions |
| REWRITE | N06_commercial/agents/agent_commercial.md | agent | 3KB | Add brand caps |
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

Show the PSPEC summary. Ask: "This is the blueprint. Ready to execute? Type `/grid` to start."

## PSPEC is NOT execution

`/spec` only SPECIFIES. It does not build, dispatch, or score.
The PSPEC is a CONTRACT between the plan and the execution.

## Examples

See real PSPECs that built this repo:
- `PSPEC_N06_BRAND_VERTICALIZATION.md` (348 lines, 32 artifacts)
- `PSPEC_N02_VISUAL_FRONTEND_ENGINEER.md` (159 lines, 14 artifacts)
- `PSPEC_N05_RAILWAY_SUPERINTENDENT.md` (159 lines, 14 artifacts)
