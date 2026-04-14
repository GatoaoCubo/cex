---
id: p11_qg_diagram
kind: quality_gate
pillar: P11
title: "Gate: diagram"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "diagram — visual architecture representations in ASCII or Mermaid notation"
quality: 9.0
tags: [quality-gate, diagram, architecture-visualization, mermaid, ascii, P11]
tldr: "Gates for diagram artifacts: validates notation correctness, layer boundaries, legend presence, and structural accuracy of architecture visuals."
density_score: 0.90
llm_function: GOVERN
---
# Gate: diagram
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: diagram` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p08_diag_[a-z][a-z0-9_]+$` | "ID fails diagram namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"diagram"` | "Kind is not 'diagram'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, notation, subject, layers, version, created, author, tags | "Missing required field(s)" |
| H07 | `notation` is one of: `ascii`, `mermaid` | "Notation must be 'ascii' or 'mermaid'" |
| H08 | Diagram body is non-empty (>= 5 lines of visual content) | "Diagram has no visual content" |
| H09 | If `notation: mermaid`, diagram block opens with valid Mermaid graph type directive | "Mermaid diagram type directive missing or invalid" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Layer boundaries | 1.0 | Distinct system layers are visually separated and labeled |
| Legend present | 1.0 | Symbol/notation key included (especially for ASCII) |
| Component completeness | 1.0 | All major system components visible in diagram |
| Data flow direction | 1.0 | Arrows or connections show clear data/control flow |
| Annotation quality | 0.5 | Key components have short inline annotations |
| Boundary clarity | 0.5 | Explicitly not component_map (data) or pattern (prescription) |
| External systems marked | 1.0 | Third-party or external dependencies visually distinct |
| Readability | 1.0 | Diagram renders cleanly without overlapping elements |
| Subject specificity | 1.0 | Diagram represents the stated subject accurately |
| Documentation | 1.0 | tldr and body intro explain what architecture this depicts |
Weight sum: 1.0+1.0+1.0+1.0+0.5+0.5+1.0+1.0+1.0+1.0 = 9.0 -> normalize to 100%
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Work-in-progress diagram during active system design iteration |
| approver | Architecture lead sign-off required |
| audit_trail | Bypass event logged to `records/audits/diagram_bypass_{date}.md` |
| expiry | 48h; must reach >= 7.0 before being referenced in documentation |
| never_bypass | H01 (YAML parse failure), H05 (quality null invariant), H08 (empty diagram has no value) |
