---
kind: examples
id: bld_examples_validator_builder_codex
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of validator artifacts
pattern: teach objective pass/fail validator authoring
---

# Examples: validator-builder-codex
## Golden Example
OUTPUT (`p06_val_frontmatter_required.md`):
```yaml
id: p06_val_frontmatter_required
kind: validator
pillar: P06
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "CODEX"
title: "Validator: Required Frontmatter Fields"
trigger: pre_commit
severity: block
quality: null
tags: [validator, frontmatter, compliance]
tldr: "Rejects artifacts missing required frontmatter fields."
target: "P*/**/*.md"
action_on_fail: reject
threshold: null
```
```text
## Rule
condition: all required fields are present
## Checks
1. id exists
2. kind exists
3. pillar exists
```
WHY THIS IS GOLDEN:
- correct P06 naming and identity
- trigger/severity use valid enums
- rule is objective and testable
- no scoring, weights, or rubric drift
## Anti-Example
BAD OUTPUT (`validator_quality.md`):
```yaml
id: validator_quality
kind: quality_gate
score_weights:
  clarity: 40
  usefulness: 60
rule: "should feel complete"
```
FAILURES:
1. wrong id namespace; missing `p06_val_`
2. wrong kind; drifted to `quality_gate`
3. weighted scoring belongs to P11/P07, not validator
4. condition is subjective and not machine-checkable
5. required P06 fields are missing
