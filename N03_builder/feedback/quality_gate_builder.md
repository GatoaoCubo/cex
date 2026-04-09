---
id: p11_fb_builder_quality_feedback
kind: feedback
pillar: P11
title: "Feedback Template — N03 Builder Quality Reviews"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: null
tags: [feedback, builder, N03, quality, review, template]
tldr: "Feedback template for N03 builder output reviews — structured format for peer scoring and improvement notes."
density_score: 0.91
linked_artifacts:
  primary: "N03_builder/quality/quality_gate_builder.md"
  related:
    - N03_builder/agents/agent_builder.md
---

# Feedback Template — N03 Builder Quality Reviews

## Purpose

Structured template for peer review of N03 builder output. Used by N07 or
peer nuclei to score artifacts and provide actionable improvement feedback.
N03 never self-scores — this template is for external reviewers.

## Review Template

```yaml
# Quality Review
artifact: {path/to/artifact.md}
reviewer: {nucleus_id}
review_date: {YYYY-MM-DD}

# Gate Checklist (PASS/FAIL)
frontmatter_valid: PASS
required_fields: PASS
quality_null: PASS
schema_compliant: PASS
body_structure: PASS
pipeline_complete: PASS
compilation_sync: PASS
commit_convention: PASS

# Scoring (reviewer assigns)
quality_score: {8.0-10.0}
density_score: {0.0-1.0}

# Feedback
strengths:
  - {what was done well}
  - {specific section that excels}
improvements:
  - {specific actionable improvement}
  - {what to change and why}
verdict: PUBLISH | REVIEW | REJECT
```

## Scoring Rubric

| Dimension | Weight | 9.0+ | 8.0-8.9 | 7.0-7.9 | < 7.0 |
|-----------|--------|------|---------|---------|-------|
| Frontmatter | 20% | All fields perfect | Minor field issues | Missing optional fields | Missing required fields |
| Structure | 25% | Matches ISO template exactly | Minor deviations | Major deviations | No structure |
| Content | 30% | Dense, actionable, unique | Good coverage | Thin or generic | Filler content |
| References | 15% | All cross-refs valid | Most refs valid | Few refs | No refs |
| Density | 10% | 0.90+ density | 0.80-0.89 | 0.70-0.79 | < 0.70 |

## Feedback Flow

```
N03 builds artifact → commits with [N03] → signals complete
     ↓
N07 reads signal → runs cex_score.py → applies review
     ↓
If score >= 8.0: PUBLISH (move handoff to _done/)
If score 7.0-7.9: REVIEW (return to N03 with feedback)
If score < 7.0: REJECT (N03 rebuilds from scratch)
```

## References

- Quality gate: N03_builder/quality/quality_gate_builder.md
- Score tool: `_tools/cex_score.py`
- Feedback tool: `_tools/cex_feedback.py`
