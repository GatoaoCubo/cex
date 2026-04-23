---
kind: quality_gate
id: p11_qg_content_filter
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for content_filter
quality: 9.0
title: "Quality Gate Content Filter"
version: "1.0.0"
author: wave1_builder_gen
tags: [content_filter, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for content_filter"
domain: "content_filter construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_content_filter
  - p11_qg_function_def
  - p09_qg_marketplace_app_manifest
  - bld_collaboration_content_filter
  - p01_qg_reranker_config
  - p01_qg_graph_rag_config
  - p07_qg_eval_metric
  - bld_instruction_content_filter
  - p03_qg_prompt_technique
  - p05_output_validator
---

## Quality Gate

## Definition

This ISO defines a content filter -- the moderation rules that gate output or input.
| metric                | threshold | operator | scope              |
|-----------------------|-----------|----------|--------------------|
| Pipeline Config Validity | 100%      | equals   | All content filters |

## HARD Gates
| ID   | Check                  | Fail Condition                              |
|------|------------------------|---------------------------------------------|
| H01  | YAML valid             | Invalid YAML syntax                         |
| H02  | ID matches pattern     | ID does not match `^[a-z0-9]+_[a-z]+$`     |
| H03  | kind matches           | kind ≠ `content_filter`                    |
| H04  | Required fields present| Missing `input` or `output` field         |
| H05  | No duplicate IDs       | Duplicate ID detected                     |
| H06  | Allowed operators      | Operator not in `[allow,block,transform]` |
| H07  | Content type valid     | Unsupported content type specified        |

## SOFT Scoring
| Dim | Dimension             | Weight | Scoring Guide                                      |
|-----|------------------------|--------|----------------------------------------------------|
| D1  | YAML structure         | 0.10   | Valid syntax, proper nesting                      |
| D2  | ID uniqueness          | 0.10   | No duplicates                                     |
| D3  | Kind consistency       | 0.10   | All entries share same kind                       |
| D4  | Operator validity      | 0.10   | All operators valid                               |
| D5  | Content type coverage  | 0.15   | Covers 90%+ of required content types             |
| D6  | Performance            | 0.15   | Latency < 50ms, error rate < 1%                  |
| D7  | Error handling         | 0.10   | Defined fallback behavior                       |
| D8  | Documentation          | 0.10   | Clear comments and schema references            |

## Actions
| Score     | Action                          |
|-----------|----------------------------------|
| GOLDEN    | Auto-approve, deploy immediately |
| PUBLISH   | Manual review required          |
| REVIEW    | Escalate to senior engineer     |
| REJECT    | Block deployment, fix required  |

## Bypass
| conditions                  | approver | audit trail              |
|-----------------------------|----------|--------------------------|
| Urgent security fix required | CTO      | Requires written approval |

## Examples

## Golden Example

This ISO defines a content filter -- the moderation rules that gate output or input.
```yaml
---
kind: content_filter
name: example_filter
description: Filters input/output content for prohibited patterns
version: 1.0
---
stages:
  - name: input_sanitization
    type: regex_replacement
    parameters:
      patterns: ["<script>.*?</script>", "\$$.*?\$$"]
      replacement: "[REDACTED]"
  - name: output_validation
    type: keyword_filter
    parameters:
      prohibited_keywords: ["nsfw", "hate_speech"]
      action: drop
```

## Anti-Example 1: Missing essential parameters
```yaml
---
kind: content_filter
name: broken_filter
description: Incomplete filter config
version: 0.1
---
stages:
  - name: input_sanitization
    type: regex_replacement
    parameters:
      patterns: ["<script>.*?</script>"]
```
## Why it fails
Incomplete parameters - missing replacement value and no output validation stage, making the filter non-functional for complete content pipelines.

## Anti-Example 2: Mixing with guardrail checks
```yaml
---
kind: content_filter
name: mixed_filter
description: Combines filtering with safety checks
version: 1.0
---
stages:
  - name: input_sanitization
    type: regex_replacement
    parameters:
      patterns: ["<script>.*?</script>"]
      replacement: "[REDACTED]"
  - name: safety_check
    type: guardrail
    parameters:
      constraints: ["no_harmful_content", "no_personal_data"]
```
## Why it fails
Content_filter should handle structured filtering, not broad safety constraints. Guardrail checks belong to a different pipeline type and would cause configuration conflicts.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
