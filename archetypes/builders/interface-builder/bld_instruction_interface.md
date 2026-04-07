---
kind: instruction
id: bld_instruction_interface
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for interface
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Interface"
version: "1.0.0"
author: n03_builder
tags: [interface, builder, examples]
tldr: "Golden and anti-examples for interface construction, demonstrating ideal structure and common pitfalls."
domain: "interface construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce an interface
## Phase 1: RESEARCH
1. Identify the two systems or agents being integrated — name both the provider and the consumer explicitly
2. List every method the provider exposes to the consumer
3. For each method, define the input schema (what the consumer sends) and the output schema (what the provider returns)
4. Determine the versioning strategy: semver (1.0.0) or date-based (2026-01-01)
5. Assess backward compatibility requirements: which changes are allowed without a version bump?
6. Plan the deprecation path: which methods may be removed, on what timeline, and what replaces them?
7. Check existing interfaces via brain_query [IF MCP] for the same provider-consumer pair — avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields and body constraints
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: all 20+ fields (null is acceptable for recommended fields)
4. Set quality: null — never self-score
5. Write the Methods section: one entry per method with name / direction / input schema / output schema / description
6. Write the Versioning section: strategy, current version, and the compatibility promise
7. Write the Backward Compatibility section: what changes are allowed without bumping the version
8. Write the Deprecation Policy section: timeline, migration path, and sunset date for any deprecated methods
9. Write the Mock Specification section: mock responses per method for use in testing
10. Write the Error Contracts section: error codes, messages, and retry guidance per method
11. Verify body is within 3072 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — apply each gate manually
2. HARD gates (all must pass):
   - YAML frontmatter parses without errors
   - id matches pattern `p06_iface_[a-z][a-z0-9_]+`
   - kind == interface
   - methods list has at least 2 entries
   - each method has name, input schema, output schema, and description
   - provider and consumer are both specified
   - versioning strategy is stated
   - quality == null
3. SOFT gates (score each against QUALITY_GATES.md):
   - backward compatibility policy is explicit
   - deprecation policy present (or null with a reason)
   - mock specification covers at least one method
   - error contracts cover failure cases per method
4. Cross-check scope boundaries:
   - bilateral contract (both sides documented), not a unilateral input_schema?
   - not a runtime event or signal (P12)?
   - not validation logic that belongs in a validator?
   - both provider and consumer sides fully documented?
5. If score < 8.0: revise in the same pass before outputting
