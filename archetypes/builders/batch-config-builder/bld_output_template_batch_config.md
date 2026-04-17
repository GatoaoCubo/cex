---
kind: output_template
id: bld_output_template_batch_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a batch_config artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 9.1
title: "Output Template Batch Config"
version: "1.0.0"
author: n03_builder
tags: [batch_config, builder, template, P09]
tldr: "Fill-in-the-blank template for batch_config artifacts: frontmatter + 5 required body sections."
domain: "batch config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Output Template: batch_config

```yaml
id: p09_bc_{{name_slug}}
kind: batch_config
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
provider: "{{openai|anthropic|azure_openai|custom}}"
model: "{{model_id}}"
endpoint: "{{/v1/chat/completions_or_provider_path}}"
max_requests: {{integer}}
completion_window: "{{24h|12h|etc}}"
cost_cap_usd: {{float}}
concurrency: {{integer}}
retry_policy: "{{max_N_retries_exponential_backoff}}"
input_format: "{{jsonl|csv|json}}"
output_format: "{{jsonl|csv|json}}"
quality: null
tags: [batch_config, {{provider_tag}}, {{use_case_tag}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_batch_job_covers_max_200ch}}"
```

## Overview
`{{purpose_of_this_batch_job_1_to_2_sentences}}`
Triggered by: `{{who_or_what_triggers_this_batch}}`
Credential env var: `{{PROVIDER_API_KEY_ENV_VAR_NAME}}`

## Job Parameters
| Parameter | Value | Description |
|-----------|-------|-------------|
| provider | {{openai|anthropic|azure_openai|custom}} | API provider for batch inference |
| model | `{{model_id}}` | Model to use for all requests in batch |
| endpoint | {{/v1/endpoint}} | API endpoint path for batch submission |
| max_requests | `{{N}}` | Maximum requests per batch file submission |
| completion_window | `{{Nh}}` | Provider SLA for batch completion |
| concurrency | `{{N}}` | Max in-flight requests at one time |

## Cost Controls
| Control | Value | Notes |
|---------|-------|-------|
| cost_cap_usd | $`{{N}}` | Job halts if projected spend exceeds cap |
| sync_api_discount | ~50% | Batch pricing vs synchronous equivalent |
| token_budget | `{{N}}` tokens | Max tokens per request (input + output) |
| alert_threshold_usd | $`{{N}}` | Alert if cumulative cost exceeds this |

## Retry and Error Policy
| Setting | Value | Description |
|---------|-------|-------------|
| max_retries | `{{N}}` | Retries per failed request |
| backoff | {{exponential|fixed}} | Retry backoff strategy |
| backoff_base_s | `{{N}}` | Base wait in seconds before first retry |
| partial_failure | {{continue|halt}} | Behavior when some requests in batch fail |
| dead_letter | `{{path_or_null}}` | Storage for permanently failed requests |

## Input/Output Format
- Input format: `{{JSONL}}` -- one JSON object per line, each with `custom_id`, `method`, `url`, `body`
- Output format: `{{JSONL}}` -- one result per line with `id`, `custom_id`, `response`, `error`
- Input path: `{{storage_path_or_bucket}}`
- Output path: `{{storage_path_or_bucket}}`

## References
- `{{provider_batch_api_docs_url}}`
- `{{related_artifact_or_env_config}}`
