---
kind: quality_gate
id: p11_qg_white_label_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for white_label_config
quality: 9.1
title: "Quality Gate White Label Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [white_label_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for white_label_config"
domain: "white_label_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_white_label_config
  - p01_qg_graph_rag_config
  - p11_qg_audit_log
  - p07_qg_benchmark_suite
  - p09_qg_marketplace_app_manifest
  - p05_qg_github_issue_template
  - white-label-config-builder
  - p07_qg_cohort_analysis
  - p09_qg_usage_quota
  - p03_sp_white_label_config_builder
---

## Quality Gate

## Definition
| metric         | threshold                              | operator | scope         |
|----------------|----------------------------------------|----------|---------------|
| schema_id      | ^p09_wl_[a-z][a-z0-9_]+.yaml$         | matches  | all YAML files|

## HARD Gates
| ID  | Check                          | Fail Condition                                      |
|-----|--------------------------------|-----------------------------------------------------|
| H01 | YAML frontmatter valid       | Missing or invalid YAML frontmatter                 |
| H02 | ID matches pattern           | ID does not match ^p09_wl_[a-z][a-z0-9_]+.yaml$    |
| H03 | kind field matches           | kind ≠ 'white_label_config'                       |
| H04 | brand_name field present     | brand_name missing or empty                       |
| H05 | reseller_id field present    | reseller_id missing or invalid                    |
| H06 | custom_logo_url valid        | URL invalid or unreachable                        |
| H07 | allowed_domains field valid  | allowed_domains missing or not a list             |

## SOFT Scoring
| Dim | Dimension                  | Weight | Scoring Guide                                                          |
|-----|----------------------------|--------|------------------------------------------------------------------------|
| D01 | Branding completeness      | 0.15   | 1.0=logo+colors+favicon+custom domain all defined; 0.5=partial; 0.0=none |
| D02 | Reseller model accuracy    | 0.15   | 1.0=sub-account+margins+OEM licensing defined; 0.5=partial; 0.0=absent  |
| D03 | Customization depth        | 0.15   | 1.0=theming API+custom emails+co-branded UI; 0.5=one element; 0.0=none  |
| D04 | Compliance settings        | 0.15   | 1.0=GDPR+regional flags defined; 0.5=one standard; 0.0=absent           |
| D05 | Schema validation          | 0.15   | 1.0=SemVer+strict types+backward compat; 0.5=partial; 0.0=absent        |
| D06 | Security posture           | 0.10   | 1.0=encrypted secrets+RBAC+audit trail; 0.5=partial; 0.0=plaintext      |
| D07 | Documentation quality      | 0.15   | 1.0=all fields documented+changelog; 0.5=partial; 0.0=absent            |

## Actions
| Score   | Action                          |
|---------|---------------------------------|
| ≥9.5    | GOLDEN: Auto-approve            |
| ≥8.0    | PUBLISH: Deploy with review     |
| ≥7.0    | REVIEW: Manual QA required      |
| <7.0    | REJECT: Fix and resubmit        |

## Bypass
| conditions                          | approver | audit trail         |
|-----------------------------------|----------|---------------------|
| Urgent deployment with CTO approval | CTO      | Ticket #WL-XXXX     |

## Examples

## Golden Example
```yaml
name: white_label_config
kind: white_label_config
description: Configuration for Acme Corp's white-label deployment on Stripe and AWS
tags:
  - reseller
  - branding
branding:
  reseller_name: "Acme Corp"
  reseller_logo_url: "https://acme.com/logo.png"
  custom_domain: "acme.stripe.com"
api_keys:
  stripe_publishable_key: "pk_live_1234567890"
  stripe_secret_key: "sk_live_0987654321"
  aws_access_key_id: "AKIAXXXXXXXXXXXXXXXX"
  aws_secret_access_key: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
reseller_settings:
  allowed_brands: ["Acme Corp", "Beta Inc"]
  support_email: "support@acme.com"
```

## Anti-Example 1: Brand identity confusion
```yaml
name: white_label_config
kind: white_label_config
branding:
  company_logo: "logo.svg"
  primary_color: "#007BFF"
  secondary_color: "#6C757D"
```
## Why it fails
Mixes brand identity configuration (colors, logos) with white-label reseller settings. White-label config should focus on reseller-specific deployment parameters, not core brand identity elements which belong in brand_config.

## Anti-Example 2: Runtime environment mixing
```yaml
name: white_label_config
kind: white_label_config
env_vars:
  DATABASE_URL: "postgres://user:pass@localhost:5432/dbname"
  API_ENDPOINT: "https://api.prod.example.com"
```
## Why it fails
Includes runtime environment variables that belong in env_config, not white-label configuration. White-label config should handle reseller branding and deployment parameters, not runtime infrastructure settings.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
