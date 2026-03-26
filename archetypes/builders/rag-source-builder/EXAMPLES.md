---
pillar: P07
llm_function: GOVERN
version: 1.0.0
---

# Examples: rag_source

## Golden Example

**Artifact**: p01_rs_anthropic_claude_api_docs

```yaml
---
id: p01_rs_anthropic_claude_api_docs
kind: rag_source
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
url: "https://docs.anthropic.com/en/api/getting-started"
domain: llm_providers
last_checked: "2026-03-26"
quality: null
tags: [rag-source, llm_providers, html]
tldr: "Official Anthropic Claude API reference covering authentication, models, messages API, and rate limits."
keywords: [anthropic, claude, api, llm, documentation]
reliability: high
format: html
extraction_method: crawl
---

## Source Description
Official Anthropic developer documentation covering the Claude API. Maintained by Anthropic engineering. Includes authentication patterns, model capabilities, messages endpoint reference, tool use, and rate limit policies.

## Freshness Policy
- Re-check interval: 30 days
- Staleness threshold: 60 days
- Trigger: on Claude model release or API version bump
- Last verified: 2026-03-26

## Extraction Notes
- Method: crawl
- Format: html
- Auth required: no (public docs)
- Known quirks: versioned paths change on major releases — track /en/api/ root

## References
- Parent domain: llm_providers
- Related sources: none
```

### Why This Is Golden

| Gate | Status | Reason |
|------|--------|--------|
| H01 | PASS | YAML parses cleanly |
| H02 | PASS | id matches ^p01_rs_[a-z][a-z0-9_]+$ |
| H03 | PASS | id == filename stem |
| H04 | PASS | kind == rag_source |
| H05 | PASS | quality == null |
| H06 | PASS | all 5 required fields present |
| H07 | PASS | body <= 1024 bytes |
| S01 | PASS | tldr <= 160 chars |
| S03 | PASS | URL is valid https:// |
| S06 | PASS | no content body — pointer only |

---

## Anti-Example

**Artifact**: p01_rs_bad_source (DO NOT PRODUCE THIS)

```yaml
---
id: rs_anthropic_docs
kind: rag_source
pillar: P01
url: docs.anthropic.com
last_checked: today
quality: 8.5
tags: [source]
---

## Content
The Anthropic API uses bearer token authentication. You pass the API key as a header:
Authorization: Bearer sk-ant-...
The messages endpoint accepts a JSON body with model, max_tokens, and messages array.
Each message has role (user or assistant) and content (string or array)...
[continues for 800 more bytes of extracted API documentation]
```

### Why This Fails

| Gate | Status | Failure |
|------|--------|---------|
| H01 | FAIL | Missing required fields — YAML incomplete |
| H02 | FAIL | id "rs_anthropic_docs" missing p01_ prefix |
| H04 | PASS | kind correct |
| H05 | FAIL | quality == 8.5 — never self-score |
| H06 | FAIL | domain field missing |
| H07 | FAIL | body > 1024 bytes |
| S03 | FAIL | URL missing https:// scheme |
| S06 | FAIL | body contains extracted content — this is a knowledge_card, not a rag_source |

**Root cause**: Author confused rag_source (pointer) with knowledge_card (content). The extracted API documentation belongs in a knowledge_card, not in a rag_source body.
