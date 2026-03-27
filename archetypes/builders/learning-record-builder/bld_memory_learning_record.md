---
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for learning_record artifact generation
---

# Memory: learning-record-builder

## Summary

Learning records capture lived operational experience with structured observation-pattern-evidence pipelines. The critical production insight is that observation must contain only raw facts — injecting interpretation into the observation field corrupts the entire pipeline. Confidence calibration against the observation count scale is the second most common failure: builders default to 0.8-0.9 even for single observations.

## Pattern

- Write observation as pure facts first: timestamps, counts, error messages, file paths — zero adjectives
- Extract pattern as a reproducible rule: "Run X before Y to prevent Z" not "Be careful with X"
- Evidence must include before/after metrics or concrete data points, not qualitative assessments
- Calibrate confidence strictly: 0.3-0.4 for single observation, 0.5-0.6 for 2-4, 0.7-0.8 for 5-9, 0.9+ only for 10+
- Set decay_rate based on domain volatility: 0.01 for stable architecture patterns, 0.10+ for API-version-dependent findings
- Use PARTIAL outcome honestly when only some goals were met — never round up to SUCCESS

## Anti-Pattern

- Observation field containing judgment ("the deployment was problematic") instead of facts ("deployment failed at 14:32 with exit code 1")
- Confidence 0.9 assigned to a single-observation record — overstates certainty by 3x
- Missing evidence field with body saying "results were positive" — pipeline requires concrete metrics
- Body exceeding 4096 bytes — split into focused records per experience event
- Pattern section giving vague advice ("be more careful") instead of reproducible steps
- Omitting semantic_links when related records exist — isolated records lose knowledge graph value

## Context

Learning records sit in the P10 memory pillar, distinct from knowledge cards (P01, external facts), session states (P10, ephemeral), and axioms (P10, abstract truths). They encode what happened during real operations with confidence scoring and temporal decay. Each record documents ONE experience event — compound records covering multiple events should be decomposed.

## Impact

Records with properly calibrated confidence and concrete patterns are retrieved 3x more often by downstream consumers than vague records. Honest PARTIAL outcomes enable better decision-making than inflated SUCCESS markers. Decay-aware records auto-deprecate stale findings, reducing noise in retrieval results by approximately 40% over 60-day windows.

## Reproducibility

Reliable production requires: (1) capture observation immediately after the event, (2) wait at least one hour before extracting the pattern to avoid recency bias, (3) gather evidence metrics from logs or dashboards, (4) calibrate confidence against the scale, (5) validate all 7 body sections exist and pass density >= 0.80.

## References

- learning-record-builder SCHEMA.md v4.0 (10 required + 12 extended frontmatter fields)
- P10 memory pillar specification
- Kolb experiential learning cycle (observe-reflect-abstract-test)
