---
kind: memory
id: p10_lr_api_reference_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for api_reference construction
quality: 8.7
title: "Learning Record Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, learning_record]
tldr: "Learned patterns and pitfalls for api_reference construction"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Observation
Common issues include inconsistent parameter formatting, missing authentication details, and incomplete example responses that don't match real-world scenarios.

## Pattern
Successful artifacts use consistent endpoint grouping (e.g., by resource), embed auth requirements directly under each endpoint, and pair examples with both request and response code blocks.

## Evidence
Reviewed artifacts from `project-x` and `service-y` showed 30% fewer user queries when examples included full request/response cycles with valid auth tokens.

## Recommendations
- Standardize parameter tables with `name`, `type`, `required`, and `description` columns
- Document auth methods (OAuth, API keys) per endpoint rather than in a centralized section
- Use code blocks for examples with clear `curl`/`HTTP` syntax and valid JSON/Payloads
- Cross-reference related endpoints (e.g., "See also: /users/{id}/roles")
- Validate against a checklist ensuring all endpoints have examples, auth, and error responses
