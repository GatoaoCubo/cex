---
id: n01_qg_intelligence
kind: quality_gate
pillar: P11
title: "Quality Gate: N01 Research & Intelligence Output"
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "N01_rebuild_8F"
quality: 9.1
tags: [quality, validation, gate, n01, research, intelligence]
tldr: "Defines the rigorous, two-stage (pass/fail and scored) quality gates for all analytical outputs produced by the N01 Research & Intelligence Nucleus."
target_artifact_type: "IntelligenceBrief"
pass_threshold: 8.0
density_score: 0.94
domain: intelligence
---

## 1. PURPOSE
This document specifies the quality assurance gates that all analytical outputs from the N01 agent must pass before being considered complete. The primary goal is to guarantee that every `IntelligenceBrief` is rigorous, evidence-based, structured, and actionable.

---

## 2. STAGE 1: HARD GATES (AUTOMATED PASS/FAIL CHECKS)
A failure in any Hard Gate results in an immediate `REJECT` status and a mandatory correction loop. These are checked automatically.

| Gate ID | Criterion                 | Validation Logic                                                                                                                              |
|---------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `H01`   | **Schema Conformance**    | The output document MUST contain the mandatory markdown sections: `## Executive Summary`, `## Detailed Analysis`, and `## Source Appendix`.       |
| `H02`   | **Universal Citation**    | Every paragraph or bullet point within `## Detailed Analysis` that makes a factual claim MUST end with a valid citation, e.g., `[source, id]`. |
| `H03`   | **Appendix Integrity**    | Every citation in the text MUST have a corresponding, non-empty entry in the `## Source Appendix`.                                           |
| `H04`   | **No Information Gaps**   | The document MUST NOT contain placeholder text (e.g., "Planned", "Pending finalization", "[add analysis here]"). If information is unknown, it must be in `## Information Gaps`. |
| `H05`   | **Confidence Declaration**| If the brief contains predictive statements or forecasts, a `Confidence Level` (High, Medium, Low) and its rationale MUST be present.     |
| `H06`   | **Bounded by Sources**    | A random sample of 3 claims will be checked to ensure they are directly supported by the content of their cited source.                        |

---

## 3. STAGE 2: SOFT GATES (AUTOMATED SCORING)
After passing all Hard Gates, the artifact is scored. A score below the `pass_threshold` of **8.0** is flagged for human review.

| Gate ID | Criterion                  | Weight | Scoring Rubric (0-10)                                                                                                                            |
|---------|----------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `S01`   | **Depth of Synthesis**     | 35%    | **0-4**: Simple summary. **5-7**: Connects some facts. **8-10**: Creates novel, non-obvious insights by synthesizing multiple disparate sources.      |
| `S02`   | **Evidence Quality**       | 25%    | **0-4**: Relies on low-tier sources. **5-7**: Mix of sources. **8-10**: Over 75% of sources are Tier 1-2 (Peer-reviewed, SEC filings, etc.).   |
| `S03`   | **Actionability & "So What?"** | 20%    | **0-4**: Purely descriptive. **5-7**: Implies some consequences. **8-10**: Executive Summary clearly states strategic implications & "so what". |
| `S04`   | **Clarity and Precision**  | 10%    | **0-4**: Vague, jargon-filled. **5-7**: Clear but verbose. **8-10**: Precise, unambiguous, and concise language.                                  |
| `S05`   | **Objectivity**            | 10%    | **0-4**: Uses biased language. **5-7**: Mostly neutral. **8-10**: Completely objective and dispassionate tone.                                      |

---

## 4. OUTCOMES
- **`REJECT` (Hard Gate Fail)**: Artifact is returned to N01 with the failed Gate ID and a directive to fix it.
- **`FLAG_FOR_REVIEW` (Soft Gate Score < 8.0)**: Artifact is accepted but flagged in the system for human oversight.
- **`ACCEPT` (Soft Gate Score >= 8.0)**: Artifact is accepted and a `validation_complete` signal is propagated.

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental intelligence artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |
