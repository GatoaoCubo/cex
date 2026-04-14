---
kind: output_template
id: bld_output_template_stt_provider
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for stt_provider production
quality: 8.9
title: "Output Template Stt Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [stt_provider, builder, output_template]
tldr: "Template with vars for stt_provider production"
domain: "stt_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
---
id: p04_stt_{{name}}
kind: stt_provider
title: "{{title}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [stt_provider, {{provider_name}}, asr]
tldr: "{{one_line_description}}"
language_support: ["{{primary_language}}", "{{secondary_language}}"]
accuracy_rating: {{wer_percent}}
---

## Overview
{{overview_content}}

## Technical Specifications
| Property | Value |
|---|---|
| Provider | {{provider_name}} |
| API Endpoint | {{endpoint_url}} |
| Auth Method | {{auth_method}} |
| Sample Rate | {{sample_rate_hz}} Hz |
| Audio Formats | {{supported_formats}} |
| Streaming Support | {{streaming_yes_no}} |
| Diarization | {{diarization_yes_no}} |
| WER Benchmark | ~{{wer_percent}}% ({{test_set}}) |
| P99 Latency | {{latency_ms}}ms |
| Pricing | {{pricing_usd_per_min}}/min |

## Configuration
```yaml
provider: `{{provider_name}}`
api_key: "${`{{PROVIDER_API_KEY}}`}"
endpoint: "`{{endpoint_url}}`"
language: "`{{language_code}}`"
sample_rate: `{{sample_rate_hz}}`
encoding: "`{{encoding_format}}`"
streaming: `{{streaming_bool}}`
diarization: `{{diarization_bool}}`
max_alternatives: `{{max_alternatives}}`
```

## Usage
{{usage_content}}

## Compliance
- Data retention: {{retention_policy}}
- Certifications: {{compliance_certs}}
- Region: {{data_region}}

## Notes
{{notes_content}}
```
