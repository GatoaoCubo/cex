---
kind: quality_gate
id: p09_qg_marketplace_app_manifest
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for marketplace_app_manifest
quality: 9.0
title: "Quality Gate Marketplace App Manifest"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [marketplace_app_manifest, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for marketplace_app_manifest"
domain: "marketplace_app_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_marketplace_app_manifest
  - p01_qg_reranker_config
  - p05_qg_github_issue_template
  - p11_qg_audit_log
  - p01_qg_graph_rag_config
  - p07_qg_benchmark_suite
  - p06_qg_edit_format
  - bld_instruction_marketplace_app_manifest
  - p12_qg_visual_workflow
  - p05_qg_partner_listing
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| schema_id | ^p09_mam_[a-z][a-z0-9_]+.yaml$ | matches | H02 |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML syntax or missing frontmatter |
| H02 | ID matches pattern ^p09_mam_[a-z][a-z0-9_]+.yaml$ | ID does not conform to schema ID pattern |
| H03 | kind field matches 'marketplace_app_manifest' | kind field is incorrect or missing |
| H04 | metadata contains name, description, version | missing required metadata fields |
| H05 | permissions field defines valid access scopes | permissions missing or invalid |
| H06 | pricing field specifies cost model (free, tiered, etc.) | pricing missing or malformed |
| H07 | required fields (id, kind, metadata, perms) present | missing critical manifest fields |
| H08 | description length ≥ 50 characters | description too short or empty |
| H09 | id field is unique and lowercase alphanumeric | id contains invalid characters or duplicates |
| H10 | version follows semver (e.g., 1.0.0) | version format invalid |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Metadata completeness | 0.10 | 1.0 if all required fields present |
| D02 | Permissions clarity | 0.10 | 1.0 if scopes are well-defined |
| D03 | Pricing accuracy | 0.10 | 1.0 if cost model is explicit |
| D04 | Description quality | 0.10 | 1.0 if clear and ≥ 100 chars |
| D05 | Version validity | 0.10 | 1.0 if semver-compliant |
| D06 | Field consistency | 0.15 | 1.0 if all fields align with spec |
| D07 | Schema adherence | 0.10 | 1.0 if ID matches pattern |
| D08 | Error handling | 0.10 | 1.0 if no critical validation errors |
| D09 | Documentation links | 0.05 | 1.0 if URLs are valid and present |
| D10 | Compliance with TOS | 0.10 | 1.0 if terms are explicitly stated |

## Actions
| Score | Action |
|---|---|
| ≥9.5 | GOLDEN: Auto-approve and promote |
| ≥8.0 | PUBLISH: Directly list on marketplace |
| ≥7.0 | REVIEW: Require manual review by PM |
| <7.0 | REJECT: Reject and request fixes |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Emergency fix for critical bug | Senior Engineer | Documented in JIRA with approval |

## Examples

## Golden Example
```markdown
---
name: "Anthropic Claude Integration"
description: "Seamless integration with Anthropic's Claude API for advanced text generation and reasoning."
vendor: "Anthropic"
version: "1.2.0"
permissions:
  - "api_access:claude"
  - "data_usage:training"
pricing:
  - tier: "Free"
    limit: "1000 tokens/month"
  - tier: "Pro"
    price: "$0.0001/token"
    limit: "unlimited"
metadata:
  compatibility: ["Claude", "LangChain"]
  model: "Claude 3"
  license: "Apache 2.0"
```

## Anti-Example 1: Missing Required Fields
```markdown
---
name: "HuggingFace Model"
description: "A HuggingFace model for NLP tasks"
vendor: "HuggingFace"
version: "0.1.0"
metadata:
  model: "bert-base-uncased"
```
## Why it fails
Missing required `permissions` and `pricing` sections. All marketplace manifests must define access controls and monetization terms.

## Anti-Example 2: Invalid Permissions
```markdown
---
name: "LangChain Plugin"
description: "LangChain integration for RAG workflows"
vendor: "LangChain Inc"
version: "2.0.0"
permissions:
  - "full_system_access"
pricing:
  - tier: "Enterprise"
    price: "$5000/month"
```
## Why it fails
"full_system_access" is an invalid permission scope. Permissions must be specific and granular (e.g., "api_access:specific_endpoint"). The example also lacks metadata compatibility information required for marketplace listings.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
