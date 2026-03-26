---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for golden_test production
sources: [ML golden datasets, SWE-bench, DeepEval, CEX validate_kc.py]
---

# Domain Knowledge: golden_test

## Foundational Concepts
Golden tests originate from ML evaluation (golden datasets, ground truth).
In NLP: human-annotated reference outputs for measuring model quality.
In CEX: curated artifacts scoring >= 9.5 that serve as calibration points for builders and validators.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| ML Golden Datasets | Labeled ground truth for training/eval | Reference artifacts for builder calibration |
| BLEU/ROUGE Reference | Human reference translations/summaries | Golden output as evaluation anchor |
| SWE-bench Verified | Verified test cases for code generation | Curated, reviewer-approved test cases |
| DeepEval Golden | Expected outputs for LLM evaluation | Input/golden_output pairs with rationale |

## Key Principles
- Golden means EXEMPLARY, not just correct — must demonstrate best practices
- Every golden_test needs a RATIONALE mapping to specific quality gates
- Reviewer approval is mandatory — producer cannot self-approve
- Edge cases need separate golden_tests (not mixed with standard)
- Golden output must be COMPLETE (no "..." or abbreviations)
- quality_threshold >= 9.5 distinguishes golden from unit_eval

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| target_kind | Scopes golden to specific artifact type | ML: dataset split by task |
| quality_threshold | 9.5+ floor for golden status | ML: confidence threshold |
| rationale | Maps to gate IDs for traceability | ML: annotation guidelines |

## Boundary vs Nearby Types
| Type | What it is | Why it is NOT golden_test |
|------|------------|--------------------------|
| few_shot_example (P01) | Input/output pair for prompt engineering | Teaches patterns; no quality threshold |
| unit_eval (P07) | Tests agent/prompt at any quality level | Any quality; not curated reference |
| scoring_rubric (P07) | Defines evaluation dimensions/weights | Criteria, not concrete examples |
| benchmark (P07) | Measures performance (latency, cost) | Quantitative metrics, not quality exemplars |

## References
- SWE-bench: https://www.swebench.com/
- DeepEval Golden Evaluation: https://docs.confident-ai.com/
- validate_kc.py v2.0 (CEX HARD/SOFT pattern, reference for gate mapping)
