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
quality: 9.1
tags: [shared, skill, verification, adversarial, all-builders]
source_insight: "OpenClaude verificationAgent.ts -- adapted as shared builder skill"
tldr: "Every builder can invoke adversarial verification on its output before publishing"
density_score: 0.86
related:
  - p04_skill_verify
  - bld_collaboration_skill
  - p03_sp_verification_agent
  - skill
  - bld_instruction_kind
  - p07_qg_12_point_validation
  - bld_system_prompt_skill
  - bld_architecture_skill
  - bld_instruction_golden_test
  - p08_ac_verification
---

# Verification Protocol (Shared Skill)

After producing an artifact (F6 PRODUCE), invoke this protocol before F7 GOVERN.

## When to Verify
1. 3+ sections modified in the artifact
2. Artifact kind is core (system_prompt, skill, guardrail, agent, agent_card)
3. Quality target >= 8.5
4. Retry attempt (previous quality gate failure)

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

## Artifact Metadata

```yaml
kind: skill
pillar: P04
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `skill` |
| Pillar | P04 |
| Domain | verification |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_skill_verify]] | sibling | 0.31 |
| [[bld_collaboration_skill]] | downstream | 0.30 |
| [[p03_sp_verification_agent]] | upstream | 0.28 |
| [[skill]] | downstream | 0.27 |
| [[bld_instruction_kind]] | upstream | 0.26 |
| [[p07_qg_12_point_validation]] | downstream | 0.26 |
| [[bld_system_prompt_skill]] | upstream | 0.26 |
| [[bld_architecture_skill]] | downstream | 0.25 |
| [[bld_instruction_golden_test]] | upstream | 0.25 |
| [[p08_ac_verification]] | downstream | 0.25 |
