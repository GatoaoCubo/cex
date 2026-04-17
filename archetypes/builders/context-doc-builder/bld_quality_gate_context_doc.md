---
id: p11_qg_context_doc
kind: quality_gate
pillar: P11
title: "Gate: context_doc"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "domain context documentation — background documents that hydrate prompts with scope, stakeholders, constraints, and assumptions"
quality: 9.0
tags: [quality-gate, context-doc, P01, prompt-hydration, domain-scope, constraints]
tldr: "Pass/fail gate for context_doc artifacts: domain scope precision, constraint completeness, assumption capture, and hydration readiness."
density_score: 0.91
llm_function: GOVERN
---
# Gate: context_doc
## Definition
| Field | Value |
|---|---|
| metric | context_doc artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: context_doc` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: my_ctx` but file is `other_ctx.md` |
| H04 | Kind equals literal `context_doc` | `kind: knowledge_card` or `kind: glossary_entry` or any other value |
| H05 | Quality field is null | `quality: 7.0` or any non-null value |
| H06 | All required fields present | Missing `domain`, `scope`, or `constraints` |
| H07 | Body size <= 2048 bytes | Body exceeds 2048 bytes — trim or split into knowledge_card |
| H08 | Scope section states what is OUT of scope | Scope only lists what is included; exclusions absent |
| H09 | At least one constraint documented | `constraints: []` or constraints section empty |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Scope precision | 1.0 | Domain boundary is specific enough to exclude adjacent domains unambiguously |
| Out-of-scope completeness | 1.0 | Adjacent domains that could be confused are explicitly excluded |
| Constraint actionability | 1.0 | Each constraint is a specific rule a prompt can apply, not a vague guideline |
| Assumption explicitness | 1.0 | Assumptions are stated as assumptions (not facts), with source noted |
| Stakeholder relevance | 0.5 | Stakeholders listed are those whose concerns affect prompt behavior |
| Dependency mapping | 0.5 | External dependencies that constrain the domain are identified |
| Hydration readiness | 1.0 | Document structured so key facts can be injected into a prompt without editing |
| Freshness | 0.5 | `updated` date is recent; stale context docs noted as requiring review |
| Terminology consistency | 0.5 | Key terms used consistently throughout; ambiguous terms defined inline |
| Density apownteness | 1.0 | Content is dense but readable; no padding or repeated constraints |
| Boundary from knowledge_card | 1.0 | Document is context or background, not a distilled atomic fact (that belongs in knowledge_card) |
| Domain specificity | 1.0 | Content specific to the declared domain; no generic boilerplate |
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
| conditions | Context doc for an emerging domain where constraints are still being discovered; used only in internal experiments |
| approver | Domain owner acknowledgment that constraints are provisional |
| audit_trail | Bypass reason and list of known-incomplete constraint areas in frontmatter comment |
| expiry | 7d — context docs for active domains must reach >= 7.0 within one week of first use |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |
