---
id: p07_gt_n03
kind: golden_test
pillar: P07
title: "Golden Tests -- N03 Builder Outputs"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 8.8
tags: [golden-test, N03, builder, expected-output, regression, 8F]
tldr: "Golden output tests for N03's primary builders. Each test case defines: input intent, expected kind, expected frontmatter fields, structural assertions, and forbidden patterns. Run before any builder ISO update."
density_score: 0.91
updated: "2026-04-17"
---

# Golden Tests: N03 Builder Outputs

## Purpose

Golden tests capture the EXPECTED output of N03's builders.
When a builder ISO is updated, golden tests detect unintended regressions.
These are NOT unit tests -- they test end-to-end builder output shape, not logic.

## Test Execution

```bash
python _tools/cex_system_test.py --golden --nucleus n03
# Or specific kind:
python _tools/cex_system_test.py --golden --kind input_schema
```

**Pass condition:** all assertions match for every test case.
**Fail condition:** any assertion fails OR frontmatter field missing.
**Regression:** test that previously passed now fails.

## Golden Test Format

Each test case:
```yaml
test_id: gt_n03_{kind}_{variant}
kind: string                    # target kind
intent: string                  # input to builder
expected:
  frontmatter:
    kind: string                # must match exactly
    pillar: string              # must match exactly
    quality: null               # always null
    density_score: ">= 0.85"    # numeric assertion
  body:
    min_sections: integer       # H2 count minimum
    must_contain: string[]      # required strings in body
    must_not_contain: string[]  # forbidden patterns
    density_floor: 0.80
  compile:
    exit_code: 0                # cex_compile.py must succeed
```

## Test Cases

### GT-N03-001: input_schema basic

```yaml
test_id: gt_n03_input_schema_basic
kind: input_schema
intent: "create an input schema for a build task"
expected:
  frontmatter:
    kind: input_schema
    pillar: P06
    quality: null
    density_score: ">= 0.85"
  body:
    min_sections: 3
    must_contain:
      - "## Fields"
      - "| Field |"
      - "| Type |"
      - "## Validation Rules"
      - "## Examples"
    must_not_contain:
      - "TODO"
      - "TBD"
      - "{{placeholder}}"
      - quality: 9  # self-scoring
    density_floor: 0.82
  compile:
    exit_code: 0
```

### GT-N03-002: knowledge_card with domain

```yaml
test_id: gt_n03_knowledge_card_domain
kind: knowledge_card
intent: "create a knowledge card about embedding strategies"
expected:
  frontmatter:
    kind: knowledge_card
    pillar: P01
    quality: null
  body:
    min_sections: 4
    must_contain:
      - "## Definition"
      - "## Application"
    must_not_contain:
      - "I don't know"
      - "Not applicable"
    density_floor: 0.80
  compile:
    exit_code: 0
```

### GT-N03-003: workflow with steps

```yaml
test_id: gt_n03_workflow_steps
kind: workflow
intent: "create a workflow for artifact build pipeline"
expected:
  frontmatter:
    kind: workflow
    pillar: P12
    quality: null
  body:
    min_sections: 3
    must_contain:
      - "## Steps"
      - "## Trigger"
    density_floor: 0.80
  compile:
    exit_code: 0
```

### GT-N03-004: scoring_rubric weight sum

```yaml
test_id: gt_n03_scoring_rubric_weights
kind: scoring_rubric
intent: "create a scoring rubric for artifact quality"
expected:
  frontmatter:
    kind: scoring_rubric
    pillar: P07
    quality: null
  body:
    min_sections: 3
    must_contain:
      - "| Weight |"
      - "100%"      # weights must sum to 100
    density_floor: 0.82
  assertions:
    - type: weight_sum
      target: 100
      tolerance: 0
  compile:
    exit_code: 0
```

### GT-N03-005: agent frontmatter completeness

```yaml
test_id: gt_n03_agent_completeness
kind: agent
intent: "create an agent for research tasks"
expected:
  frontmatter:
    kind: agent
    pillar: P02
    quality: null
  body:
    min_sections: 4
    must_contain:
      - "## Capabilities"
      - "## Tools"
      - "## Sin Lens"
    density_floor: 0.80
  compile:
    exit_code: 0
```

## Forbidden Pattern Library

These patterns, if found in any N03 output, fail the golden test:

| Pattern | Reason |
|---------|--------|
| `quality: [0-9]` | Self-scoring violation |
| `TODO` / `TBD` / `FIXME` | Placeholder in production output |
| `{{[a-zA-Z_]+}}` | Unresolved template variable |
| `research card` | Vocabulary drift (should be knowledge_card) |
| `brain query` | Vocabulary drift (should be cex_retriever.py) |
| `N/A` as only content of a section | Empty section placeholder |
| Non-ASCII chars in .py/.ps1 code blocks | ASCII rule violation |

## Test Maintenance

- Run golden tests before ANY change to builder ISOs
- If output legitimately changes (spec update): update golden test first, then update ISO
- Golden tests are the CONTRACT between spec writers and builders
- Never delete a golden test without a spec change justifying the removal
