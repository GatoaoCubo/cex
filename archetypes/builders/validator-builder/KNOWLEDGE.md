---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for validator production
sources: [JSON Schema validation, pre-commit framework, CEX governance layer]
---

# Domain Knowledge: validator

## Foundational Concept
Validators are technical gatekeepers: deterministic, binary (pass/fail) checks
applied to artifacts before acceptance. Rooted in design-by-contract (Meyer 1992)
and schema validation (JSON Schema, XML Schema). In CEX, validators sit in the
governance layer of P06 — they enforce contracts, not measure quality.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| JSON Schema (draft-07+) | Field type, format, pattern constraints | conditions structure (field/operator/value) |
| pre-commit framework | Git hook validators (lint, format, security) | pre_commit boolean, auto_fix capability |
| OpenAPI 3.x validators | Request/response validation rules | Structural validation of artifact fields |
| ESLint/Ruff rules | Code quality rules with severity + auto-fix | severity enum, auto_fix boolean |
| Terraform validate | HCL config validation before apply | Pre-commit artifact validation pattern |

## Key Patterns
- Validators are DETERMINISTIC: same input = same result, always
- Validators are BINARY: pass or fail, never "score 7.5"
- Validators are COMPOSABLE: multiple validators chain (all must pass)
- Validators have SEVERITY: error (blocks), warning (flags), info (logs)
- Validators can AUTO-FIX: simple issues (formatting, casing) can self-repair
- Conditions use TRIPLES: (field, operator, expected_value)
- Error messages are ACTIONABLE: tell the user what to fix, not just what failed
- Bypass requires AUDIT: who bypassed, when, why

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| pre_commit | CEX artifacts validate before git commit | pre-commit hooks |
| auto_fix | Some validators can self-repair (casing, formatting) | ESLint --fix |
| domain | Scopes validator to specific artifact kind | JSON Schema $ref |
| bypass.approver | Governance trail for exceptions | RBAC override |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT validator |
|------|------------|----------------------|
| quality_gate (P11) | Weighted scoring barrier (0-10 score) | Validators are binary pass/fail, no scoring |
| scoring_rubric (P07) | Subjective evaluation criteria | Validators are objective and deterministic |
| input_schema (P06) | Entry contract for data shape | Input schemas define shape; validators check rules |
| validation_schema (P06) | Post-generation system contract | Applied by system silently; validators are explicit |
| guardrail (P11) | Safety boundary enforcement | Guardrails are behavioral limits; validators check data |

## References
- Meyer, B. (1992) "Design by Contract" — preconditions/postconditions
- JSON Schema: https://json-schema.org/
- pre-commit: https://pre-commit.com/
- ESLint rule anatomy: https://eslint.org/docs/latest/extend/custom-rules
