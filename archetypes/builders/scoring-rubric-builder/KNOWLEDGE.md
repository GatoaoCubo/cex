---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for scoring_rubric production
sources: [AAC&U VALUE Rubrics, Bloom taxonomy, CEX validate_kc.py, Cooper 1990]
---

# Domain Knowledge: scoring_rubric

## Foundational Concepts
Scoring rubrics originate from education (Bloom 1956, AAC&U VALUE Rubrics).
In AI/LLM: evaluation frameworks for prompt quality, agent output, and artifact completeness.
In CEX: multi-dimensional weighted scoring with 4 tiers (GOLDEN/PUBLISH/REVIEW/REJECT).

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| AAC&U VALUE Rubrics | 16 rubrics for learning outcomes, 4 levels each | Multi-dimension, leveled criteria |
| Bloom Taxonomy | 6 cognitive levels (remember to create) | Hierarchical evaluation depth |
| LLM-as-Judge | LLM evaluates LLM output on dimensions | Automated scoring with rubric |
| SonarQube Quality Model | Reliability, Security, Maintainability dimensions | Weighted dimension scoring |
| DORA Metrics | 4 key metrics for DevOps performance | Concrete, measurable thresholds |

## Key Principles
- Dimensions must be ORTHOGONAL (no overlap — each measures one thing)
- Weights must be EXPLICIT and sum to exactly 100%
- Criteria must be CONCRETE (no "good" or "appropriate" — specify what counts)
- Scales must be CONSISTENT across dimensions (all 0-10 or all labeled)
- Calibration requires GOLDEN_TESTS as anchoring examples
- Inter-rater agreement measures rubric reliability (>= 0.80 is good)
- Automation status must be honest (manual if no validator exists)

## CEX Evaluation Frameworks (existing patterns)
| Framework | Dimensions | Used for |
|-----------|-----------|----------|
| 5D | Density, Completeness, Actionability, Boundary, References | Knowledge cards |
| 12LP | One dimension per pillar (P01-P12) | Cross-pillar artifacts |
| HARD/SOFT | Binary + weighted numeric | Quality gates |

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| target_kinds | Scopes rubric to artifact types | AAC&U: discipline-specific rubrics |
| automation_status | Tracks if dimensions are machine-checkable | SonarQube: automated vs manual review |
| calibration_set | Links golden_tests for anchoring | Education: benchmark papers |

## Boundary vs Nearby Types
| Type | What it does | NOT this |
|------|-------------|----------|
| quality_gate (P11) | Enforces PASS/FAIL with threshold | Does NOT define how to measure |
| golden_test (P07) | Provides reference EXAMPLE at 9.5+ | Does NOT define evaluation dimensions |
| benchmark (P07) | Measures PERFORMANCE (latency, cost) | Does NOT assess artifact quality |
| unit_eval (P07) | Tests specific agent/prompt behavior | Does NOT define multi-dimensional framework |

## References
- AAC&U VALUE Rubrics: https://www.aacu.org/initiatives/value-initiative
- Bloom Taxonomy (1956, revised Anderson & Krathwohl 2001)
- LLM-as-Judge: https://arxiv.org/abs/2306.05685
- validate_kc.py v2.0 (CEX HARD/SOFT pattern, 5D rubric reference)
