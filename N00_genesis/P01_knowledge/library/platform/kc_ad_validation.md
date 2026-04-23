---
id: kc_ad_validation
kind: knowledge_card
pillar: P01
quality: 9.1
tldr: "Patterns for validating LLM-generated content, including fabrication detection, confidence scoring, and retry-with-refinement logic."
tags: ["llm", "validation", "quality", "guardrails", "accuracy"]
updated: "2026-04-07"
domain: "knowledge management"
title: "Ad Validation"
version: "1.0.0"
author: n04_knowledge
created: "2026-04-07"
density_score: 0.75
related:
  - p05_output_validator
  - bld_knowledge_card_output_validator
  - p04_skill_verify
  - p01_kc_qa_validation
  - p01_kc_output_validator
  - p01_kc_universal_llm
  - p01_kc_schema_validation
  - bld_collaboration_validation_schema
  - kc_course_generation
  - p01_kc_output_formatting
---

# LLM Output Validation and Guardrails

After generating content with an LLM, a critical next step is validation. This card outlines several patterns for ensuring the quality, accuracy, and safety of LLM-generated text, such as advertisements or articles.

## 1. Fabrication and Refusal Detection

LLMs can sometimes "refuse" to complete a task or generate boilerplate, unhelpful text. A first-pass validator should scan the output for these patterns.

-   **Pattern**: Maintain a list of regular expressions (`FABRICATION_PATTERNS`) that match common refusal phrases (e.g., "As an AI language model...", "I cannot fulfill this request...", "I am not able to...").
-   **Action**: If a pattern is matched, the output is immediately flagged as invalid, preventing placeholder or refused content from moving forward.

## 2. Confidence Scoring

Rather than a simple binary (valid/invalid) assessment, a more nuanced approach is to assign a confidence score.

-   **Process**: The validator assesses multiple quality dimensions (e.g., fluency, factual accuracy, adherence to prompt) and combines them into a single numerical score, from 0.0 to 1.0.
-   **Tiers**: The score can be used to triage content:
    -   `> 0.9`: High confidence, suitable for auto-publishing.
    -   `0.7 - 0.9`: Medium confidence, flag for human review.
    -   `< 0.7`: Low confidence, automatically reject and trigger regeneration.
-   **Benefit**: This creates a flexible quality gate that balances automation with the need for human oversight.

## 3. Factual Accuracy Checks

For content containing factual claims (prices, specifications, statistics), a dedicated verification step is crucial.

-   **Pattern**:
    1.  Deconstruct the generated text into a list of individual claims.
    2.  For each claim, perform a verification check. This could involve:
        -   Comparing against a trusted internal database or knowledge base.
        -   Executing a targeted web search.
        -   Making a separate, focused LLM call specifically tasked with fact-checking that single claim.
-   **Action**: Claims that cannot be verified are flagged, and the confidence score is lowered.

## 4. Retry-with-Refinement Logic

When validation fails, simply regenerating the entire text can be inefficient. A smarter pattern is to retry the generation with more specific instructions.

-   **Process**:
    1.  The validator identifies the specific part of the text that is problematic (e.g., a factually incorrect paragraph, a fabricated sentence).
    2.  The system triggers another LLM call, but the prompt is modified to include the original text and instructions for targeted correction.
-   **Example Prompt**: "The following text was generated but has an error in the pricing section. Please regenerate *only the pricing section* with the correct price of `[PLACEHOLDER]`. Original text: [Original generated text]".
-   **Benefit**: This iterative refinement is faster and more resource-efficient than starting from scratch.

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `kc_ad_validation`
- **Tags**: ["llm", "validation", "quality", "guardrails", "accuracy"]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_output_validator]] | downstream | 0.23 |
| [[bld_knowledge_card_output_validator]] | sibling | 0.22 |
| [[p04_skill_verify]] | downstream | 0.21 |
| [[p01_kc_qa_validation]] | sibling | 0.20 |
| [[p01_kc_output_validator]] | sibling | 0.20 |
| [[p01_kc_universal_llm]] | sibling | 0.20 |
| [[p01_kc_schema_validation]] | sibling | 0.20 |
| [[bld_collaboration_validation_schema]] | downstream | 0.19 |
| [[kc_course_generation]] | sibling | 0.18 |
| [[p01_kc_output_formatting]] | sibling | 0.18 |
