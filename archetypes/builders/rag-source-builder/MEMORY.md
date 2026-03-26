---
pillar: P10
llm_function: INJECT
version: 1.0.0
artifacts_produced: 0
---

# Memory: rag-source-builder

## Common Mistakes (learned from production)

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Content body included | Body > 500 bytes with prose paragraphs | Remove content — pointer only |
| quality not null | quality: 8.5 or quality: "null" | Set quality: null (YAML null, not string) |
| Wrong id prefix | id: rs_source or id: rag_source_x | Must be p01_rs_{slug} |
| URL missing scheme | url: docs.anthropic.com | Must start with https:// or http:// |
| last_checked missing | H06 HARD gate fail | Always set to today YYYY-MM-DD |
| id != filename stem | H03 HARD gate fail | Check filename matches id exactly |
| Duplicate source | Two rag_sources for same URL | brain_query first, always |
| domain not in taxonomy | domain: "AI stuff" | Use established CEX domain values |
| Slug with hyphens | p01_rs_my-source | Use underscores only: p01_rs_my_source |

## Domain Patterns (observed)

| Source Reliability | Common Characteristics |
|-------------------|----------------------|
| high | docs.{vendor}.com, api.{vendor}.com, arxiv.org, official spec repos |
| medium | github.com wikis, curated blogs, stable third-party aggregators |
| low | social media, rapidly-changing landing pages, unofficial mirrors |

## Freshness Patterns

| Format | Typical Freshness | Reasoning |
|--------|------------------|-----------|
| html (docs) | 30 days | Docs update on releases |
| api | 7 days | APIs can change rapidly |
| pdf | 90 days | Papers rarely change post-publish |
| csv | 14 days | Dataset snapshots update often |

## Boundary Reminders
- If someone says "add knowledge about X" — that is a knowledge_card, not a rag_source
- If someone gives a URL to index — that is a rag_source
- If someone wants domain context for an agent — that is a context_doc

## Artifacts Produced Counter
0 (increment manually or via pipeline on each successful production)
