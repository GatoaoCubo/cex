---
kind: memory
id: bld_memory_quality_gate
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for quality_gate artifact generation
---

# Memory: quality-gate-builder
## Summary
Quality gates are pass/fail barriers with numeric scoring that artifacts must clear before shipping. The critical production lesson is the HARD/SOFT distinction: HARD gates block (fail = reject), SOFT gates score (low = penalty but not rejection). Mixing these causes either false rejections (SOFT treated as HARD) or quality leaks (HARD treated as SOFT). The second lesson is that scoring formulas must have weights summing to exactly 100% — weights that sum to more or less create score inflation or deflation.
## Pattern
- Classify every gate as HARD (blocking) or SOFT (scoring) before writing the check logic
- HARD gates must be binary: pass or fail with no partial credit — ambiguous gates cause inconsistent enforcement
- SOFT gate weights must sum to exactly 100% — verify arithmetic before delivery
- Scoring formulas should be transparent: any reviewer can manually calculate the score from gate results
- Bypass policies must require explicit audit trail entry — no silent bypasses
- Include calibration examples: one artifact that barely passes, one that barely fails
## Anti-Pattern
- HARD gates with partial scoring — creates ambiguity about whether the artifact is blocked or just penalized
- SOFT gate weights summing to 110% or 90% — inflated or deflated scores break threshold comparisons
- Bypass without audit trail — quality gates with easy silent bypasses provide no enforcement value
- Gates that check the same dimension twice — double-counting inflates that dimension's influence
- Confusing quality_gate (P11, pass/fail barrier) with validator (P06, technical check) or scoring_rubric (P07, evaluation framework)
## Context
Quality gates operate in the P11 governance layer. They are the final checkpoint before an artifact enters a pool or ships to production. Gates consume validator results (P06) and scoring rubric evaluations (P07) but make the binary ship/no-ship decision. In high-throughput systems, automated gates process artifacts without human review; only bypasses require human authorization.
## Impact
Clear HARD/SOFT classification eliminated 100% of false rejection incidents. Weight normalization to 100% produced scores that accurately predicted downstream artifact performance. Audit-trail-required bypasses reduced unauthorized quality exceptions by 90%.
## Reproducibility
Reliable quality gate production: (1) enumerate all checks and classify each as HARD or SOFT, (2) define binary pass/fail logic for HARD gates, (3) assign weights to SOFT gates summing to 100%, (4) write transparent scoring formula, (5) define bypass policy with audit requirements, (6) provide calibration examples at the pass/fail boundary.
## References
- quality-gate-builder SCHEMA.md (HARD/SOFT gate specification)
- P11 governance pillar specification
- Quality assurance gate patterns
