---
id: p11_qg_admin_orchestration
kind: quality_gate
pillar: P11
title: "Gate: N07 Orchestration Quality"
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: orchestration
quality: 8.8
tags: [quality-gate, orchestration, N07, validation]
tldr: "Quality gates for N07 orchestration — signal received, quality >= 8.0, doctor pass, compile success, git committed."
density_score: 1.0
---

# Quality Gate: N07 Orchestration

## Definition

| Property | Value |
|----------|-------|
| Metric | Orchestration output quality |
| Threshold | 8.0 / 10.0 |
| Operator | >= |
| Scope | All artifacts dispatched by N07 to builders |

## Checklist (HARD gates — ALL must pass)

- [ ] H01: Signal received — builder emitted completion signal to `.cex/runtime/signals/`
- [ ] H02: Quality score >= 8.0 — reported by builder in signal payload
- [ ] H03: Git committed — builder committed changes before signaling
- [ ] H04: Compile success — `python _tools/cex_compile.py {path}` produces valid YAML
- [ ] H05: Doctor pass — `python _tools/cex_doctor.py` reports no errors for artifact
- [ ] H06: Frontmatter valid — YAML parses, required fields present, kind matches
- [ ] H07: Scope respected — builder only modified files within handoff scope fence

## Scoring (SOFT gates — weighted dimensions)

| ID | Dimension | Weight | Criteria |
|----|-----------|--------|----------|
| S01 | Completeness | 25% | All handoff tasks completed, no partial deliverables |
| S02 | Density | 20% | density_score >= 0.85, no filler prose |
| S03 | Accuracy | 20% | Content matches domain reality, no placeholder data |
| S04 | Structure | 15% | Follows builder output template, correct sections |
| S05 | Integration | 10% | linked_artifacts correct, references valid paths |
| S06 | Freshness | 10% | updated date is current, version incremented if rebuild |

## Scoring Formula

```
aggregate_score = (S01 * 0.25) + (S02 * 0.20) + (S03 * 0.20) + (S04 * 0.15) + (S05 * 0.10) + (S06 * 0.10)
PASS = ALL(H01..H07) AND aggregate_score >= 0.80
```

## Actions

| Outcome | Consequence |
|---------|-------------|
| PASS (all HARD + soft >= 0.80) | Artifact accepted, handoff moved to `_done/` |
| HARD FAIL (any H01-H07 fails) | Block — builder must fix and re-signal |
| SOFT FAIL (aggregate < 0.80) | Return with feedback — builder revises |

## Quality Tiers

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Mark as reference example |
| PUBLISH | >= 8.0 | Standard acceptance |
| REVIEW | >= 7.0 | Revision required |
| REJECT | < 7.0 | Full rebuild |

## Bypass Policy

- **Who may override**: admin only (N07 operator)
- **Conditions**: documented justification required, logged to `.cex/runtime/signals/`
- **Audit**: bypass events recorded as signals with `status: bypass` and reason field

## Validation Commands

```bash
# Compile check
python _tools/cex_compile.py {artifact_path}

# Doctor check
python _tools/cex_doctor.py

# Quality check
grep -r "^quality: null" {path} --include="*.md"

# Signal check
ls .cex/runtime/signals/{nucleus}_*.json
```

## References

- Doctor tool: _tools/cex_doctor.py
- Compile tool: _tools/cex_compile.py
- Feedback tool: _tools/cex_feedback.py
