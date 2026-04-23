---
kind: quality_gate
id: p09_qg_usage_quota
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for usage_quota
quality: 9.1
title: "Quality Gate Usage Quota"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_quota, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for usage_quota"
domain: "usage_quota construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_usage_quota
  - p11_qg_audit_log
  - p07_qg_benchmark_suite
  - p09_qg_marketplace_app_manifest
  - p11_qg_white_label_config
  - p05_qg_github_issue_template
  - p01_qg_graph_rag_config
  - p07_qg_cohort_analysis
  - p01_qg_faq_entry
  - p11_qg_ai_rmf_profile
---

## Quality Gate

## Definition
| metric              | threshold | operator | scope              |
|---------------------|-----------|----------|--------------------|
| required fields     | 4         | >=       | per artifact       |
| quota_limit present | true      | ==       | frontmatter        |
| reset_interval set  | true      | ==       | frontmatter        |

## HARD Gates
| ID             | Check                          | Fail Condition                                      |
|----------------|--------------------------------|-----------------------------------------------------|
| H01            | YAML frontmatter valid         | Missing or invalid frontmatter                      |
| H02            | ID matches ^p09_uq_[a-z][a-z0-9_]+.yaml$ | ID does not match schema pattern                   |
| H03            | kind field matches 'usage_quota' | kind is not 'usage_quota'                          |
| H04            | Quota limits defined           | Missing or incomplete quota limits                 |
| H05            | enforcement_policy field present | enforcement_policy missing or not "hard"/"soft" |
| H06            | reset_interval is ISO 8601 duration | reset_interval format invalid (not P1D, PT1H, etc.) |
| H07            | quota_limit is positive number | quota_limit <= 0 or missing                      |
| H08            | usage_metric field present     | usage_metric field missing or empty              |

## SOFT Scoring
| Dim        | Dimension               | Weight | Scoring Guide                                      |
|------------|-------------------------|--------|----------------------------------------------------|
| D01        | Quota accuracy          | 0.20   | 1.0 if precise thresholds+units, 0.5 if approximate, 0.0 if missing |
| D02        | Fairness enforcement    | 0.20   | 1.0 if balanced+documented, 0.5 if partial, 0.0 if absent |
| D03        | Logging completeness    | 0.10   | 1.0 if full, 0.5 if partial, 0.0 if missing        |
| D04        | Scalability             | 0.10   | 1.0 if adaptive, 0.5 if static, 0.0 if non-functional |
| D05        | User notification       | 0.10   | 1.0 if clear, 0.5 if vague, 0.0 if absent          |
| D06        | Compliance with SLA     | 0.10   | 1.0 if aligned, 0.5 if partial, 0.0 if conflicting |
| D07        | Emergency override      | 0.10   | 1.0 if documented, 0.5 if implied, 0.0 if absent    |
| D08        | Documentation quality   | 0.10   | 1.0 if complete, 0.5 if partial, 0.0 if missing     |

## Actions
| Score     | Action                          |
|-----------|---------------------------------|
| GOLDEN    | >=9.5: Auto-approve             |
| PUBLISH   | >=8.0: Publish with review note |
| REVIEW    | >=7.0: Require manual review    |
| REJECT    | <7.0: Reject and rework         |

## Bypass
| conditions                  | approver         | audit trail                          |
|-----------------------------|------------------|--------------------------------------|
| Emergency system override   | CTO              | Requires written approval and log  |
| Regulatory compliance       | Legal team       | Documented in compliance audit     |
| Critical bug fix            | SRE lead         | Requires post-implementation review|

## Examples

## Golden Example
---
kind: usage_quota
spec:
  model: gpt-3.5-turbo
  max_tokens_per_month: 100000
  fair_use_policy: "Exceeding quota may result in throttling."
  reset_interval: "monthly"
  enforcement: "soft"
  description: "Token usage limit for OpenAI's GPT-3.5 Turbo model."
---

## Anti-Example 1: Missing quota specification
---
kind: usage_quota
spec:
  model: gpt-3.5-turbo
  description: "Token usage limit for OpenAI's GPT-3.5 Turbo model."
  enforcement: "soft"
---

## Why it fails
The example lacks a concrete quota value (e.g., `max_tokens_per_month`). Without a measurable limit, the configuration cannot enforce fair use or track consumption.

## Anti-Example 2: Confusing rate limits with quota
---
kind: usage_quota
spec:
  model: gpt-3.5-turbo
  max_requests_per_minute: 60
  max_tokens_per_month: 100000
---

## Why it fails
The configuration mixes rate limits (`max_requests_per_minute`) with usage quota. Rate limits (RPM) and usage quotas are distinct policies and should be managed in separate configurations.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
