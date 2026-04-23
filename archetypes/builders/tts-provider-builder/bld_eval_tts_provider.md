---
kind: quality_gate
id: p04_qg_tts_provider
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for tts_provider
quality: 9.1
title: "Quality Gate Tts Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [tts_provider, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for tts_provider"
domain: "tts_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_tts_provider
  - bld_instruction_tts_provider
  - p04_qg_stt_provider
  - p03_sp_tts_provider_builder
  - bld_examples_stt_provider
  - p11_qg_function_def
  - bld_config_tts_provider
  - bld_output_template_playground_config
  - p09_qg_prosody_config
  - bld_schema_tts_provider
---

## Quality Gate

## Definition  
| Metric                | Threshold | Operator | Scope      |  
|-----------------------|-----------|----------|------------|  
| Latency               | <500ms    | <=       | Per-call   |  
| Accuracy              | >95%      | >=       | Per-provider |  
| Supported Languages   | >=5       | >=       | Per-provider |  
| Error Rate            | <1%       | <=       | Per-hour   |  

## HARD Gates  
| ID   | Check               | Fail Condition                          |  
|------|---------------------|-----------------------------------------|  
| H01  | YAML valid          | Invalid YAML syntax                     |  
| H02  | ID matches pattern  | ID does not match `^p04_tts_[a-zA-Z0-9_-]+$` |  
| H03  | Kind matches        | Kind != `tts_provider`                  |  
| H04  | Provider registered | Provider not in approved list           |  
| H05  | API key present     | Missing or invalid API key              |  
| H06  | Endpoint reachable  | API endpoint unreachable                |  
| H07  | Language codes valid| Language codes not ISO 639-1 compliant  |  

## SOFT Scoring  
| Dim | Dimension         | Weight | Scoring Guide                          |  
|-----|-------------------|--------|----------------------------------------|  
| D1  | Latency           | 0.15   | 1.0 (<=200ms), 0.5 (<=500ms)           |  
| D2  | Accuracy          | 0.15   | 1.0 (>98%), 0.5 (>95%)                 |  
| D3  | Language support  | 0.10   | 1.0 (>=10), 0.5 (>=5)                  |  
| D4  | Error handling    | 0.10   | 1.0 (0% errors), 0.5 (<1%)             |  
| D5  | Documentation     | 0.10   | 1.0 (complete), 0.5 (partial)          |  
| D6  | API stability     | 0.10   | 1.0 (no downtime), 0.5 (<1h/month)     |  
| D7  | Scalability       | 0.10   | 1.0 (10k+ RPS), 0.5 (1k+ RPS)          |  
| D8  | Security          | 0.10   | 1.0 (TLS 1.2+), 0.5 (no TLS)           |  

## Actions  
| Score     | Action                          |  
|-----------|---------------------------------|  
| GOLDEN    | >=9.5: No action required       |  
| PUBLISH   | >=8.0: Deploy to production     |  
| REVIEW    | >=7.0: Require QA review        |  
| REJECT    | <7.0: Rework and resubmit       |  

## Bypass  
| Conditions                          | Approver   | Audit Trail                   |  
|-------------------------------------|------------|-------------------------------|  
| Critical bug fix (SLA violation)    | CTO        | Note: "Urgent SLA fix approved" |  
| New provider onboarding (first time)| Architect  | Note: "Initial provider setup"  |  
| Temporary demo environment          | Manager    | Note: "Demo bypass approved"    |

## Examples

## Golden Example
```yaml
name: tts_provider
description: Integrates with Azure Cognitive Services Text-to-Speech
version: 1.2.0
parameters:
  - name: api_key
    type: string
    description: Azure API key for TTS service
  - name: endpoint
    type: string
    format: uri
    description: Azure TTS endpoint URL
  - name: voice
    type: string
    enum: ["en-US-JennyNeural", "fr-FR-DeniseNeural"]
    description: Voice model to use
```

## Anti-Example 1: Missing Critical Parameters
```yaml
name: tts_provider
description: Incomplete TTS integration
version: 0.1.0
parameters:
  - name: voice
    type: string
    enum: ["en-US-JennyNeural"]
```
## Why it fails
Lacks authentication parameters (api_key) and endpoint URL, making the integration non-functional. No way to connect to any TTS service.

## Anti-Example 2: Mixing Responsibilities
```yaml
name: tts_provider
description: Overloaded TTS configuration
version: 1.0.0
parameters:
  - name: prosody_config
    type: object
    properties:
      pitch: number
      rate: number
```
## Why it fails
Violates boundary constraints by including prosody_config parameters which belong to voice_pipeline, not tts_provider. Mixes integration configuration with voice personality settings.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
