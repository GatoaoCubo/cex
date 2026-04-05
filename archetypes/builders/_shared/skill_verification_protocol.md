---
id: shared_skill_verification_protocol
kind: skill
pillar: P04
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
title: "Shared Skill: Verification Protocol for All Builders"
domain: verification
quality: null
tags: [shared, skill, verification, adversarial, all-builders]
source_insight: "OpenClaude verificationAgent.ts -- adapted as shared builder skill"
tldr: "Every builder can invoke adversarial verification on its output before publishing"
---

# Verification Protocol (Shared Skill)

After producing an artifact (F6 PRODUCE), invoke this protocol before F7 GOVERN.

## When to Verify
- 3+ sections modified in the artifact
- Artifact kind is core (system_prompt, skill, guardrail, agent, agent_card)
- Quality target >= 8.5
- Retry attempt (previous quality gate failure)

## Verification Steps

1. **Schema compliance**: Does the artifact match its kind's SCHEMA.md?
   Check: every required frontmatter field present and correctly typed.

2. **Boundary compliance**: Does the artifact stay within its kind's boundary?
   Check: no system_prompt content in a skill, no task instructions in identity.

3. **Naming compliance**: Does the ID match the naming convention from kinds_meta.json?
   Check: `p{NN}_{prefix}_{slug}` format.

4. **Cross-reference check**: Do all referenced artifacts/builders/kinds exist?
   Check: grep for references, verify targets are real paths.

5. **Adversarial probe**: Try to break the artifact:
   - Feed it an edge-case input (empty, malformed, contradictory)
   - Check if the rules are enforceable or aspirational
   - Verify the output format is machine-parseable

## Output
For each check: PASS with evidence or FAIL with Expected vs Actual.
Final: VERDICT: PASS | FAIL | PARTIAL
