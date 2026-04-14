---
id: p11_qg_vision_tool
kind: quality_gate
pillar: P11
title: "Gate: vision_tool"
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
domain: "visual analysis tool definition — image processrs with declared input types, capabilities, providers, and structured output"
quality: 9.0
tags: [quality-gate, vision-tool, P04, image, ocr, confidence-threshold]
tldr: "Pass/fail gate for vision_tool artifacts: input type coverage, capability documentation, provider mapping, confidence thresholds, and output schema."
density_score: 0.90
llm_function: GOVERN
---
# Gate: vision_tool
## Definition
| Field | Value |
|---|---|
| metric | vision_tool artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: vision_tool` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_vision_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, missing prefix, or spaces |
| H03 | ID equals filename stem | `id: p04_vision_ocr` but file is `p04_vision_document.md` |
| H04 | Kind equals literal `vision_tool` | `kind: tool` or `kind: image_tool` or any other value |
| H05 | Quality field is null | `quality: 8.5` or any non-null value |
| H06 | All required fields present | Missing any of: input_types, capabilities, output_format, providers |
| H07 | Body has all 4 required sections | Missing ## Overview, ## Input Types, ## Capabilities, or ## Output Format |
| H08 | input_types contains only valid enum values | `input_types: [file]` — "file" is not valid (must be "file_path") |
| H09 | output_format is one of: json, text, table | `output_format: xml` or unrecognized value |
| H10 | capabilities list non-empty and matches body section names | `capabilities: []` or capability in list has no matching ## Capabilities section |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Input type coverage | 1.0 | All meaningful input formats documented with encoding details and size limits |
| Capability documentation | 1.5 | Each capability has description, confidence range, and output schema |
| Provider mapping | 1.0 | Each provider listed; capabilities mapped to providers that support them |
| Confidence threshold declared | 1.0 | confidence_threshold present and justified; not left as implicit default |
| Supported formats declared | 1.0 | supported_formats list present; provider-specific format limitations noted |
| Output schema completeness | 1.5 | Output format section shows JSON envelope with field names and types |
| Boundary clarity | 1.0 | Explicitly distinguishes from browser_tool, computer_use, document_loader |
| Domain specificity | 1.0 | Capabilities and output schemas are specific to the declared visual domain |
| Batch support declared | 0.5 | batch_support field present with behavioral description if true |
| Resolution constraints | 0.5 | max_resolution and max_bytes_per_image declared for payload planning |
| Testability | 1.0 | Each capability has a concrete output example a caller can validate against |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Internal prototype used only during provider evaluation, never shipped to production |
| approver | Author self-certification with comment explaining prototype-only scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — prototypes must be promoted to >= 7.0 or removed from repo |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics), H10 (unmatched capabilities break validation pipeline) |
