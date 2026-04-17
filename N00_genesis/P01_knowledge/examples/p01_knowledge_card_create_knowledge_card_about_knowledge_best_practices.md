---
id: p01_kc_knowledge_best_practices
kind: knowledge_card
pillar: P01
title: "Knowledge Card Best Practices: Density, Structure, and Retrieval"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "knowledge-card-builder"
domain: knowledge_management
quality: 9.1
tags: [knowledge-card, density, best-practices, retrieval, meta_kc, frontmatter, axioms]
tldr: "KC quality hinges on density >= 0.80 (tables > bullets > prose), ALWAYS/NEVER axioms, 14 required frontmatter fields, and body 200-5120 bytes — all enforced by validate_kc.py v2.0"
when_to_use: "When authoring, reviewing, or improving knowledge cards; when density score falls below 0.80 or validator reports failures"
keywords: [knowledge_card, density, axiom, frontmatter, validate_kc, meta_kc, domain_kc]
long_tails:
  - How to achieve density >= 0.80 in a knowledge card
  - Difference between domain_kc and meta_kc body structure
  - Which frontmatter fields are required in a knowledge card
  - How to write axioms in ALWAYS NEVER format for knowledge cards
  - What causes knowledge card validator hard gate failures
axioms:
  - ALWAYS use tables over prose for comparisons — tables carry 3x info per line
  - NEVER set quality to a numeric value — scoring is always external (null required)
  - ALWAYS choose meta_kc for CEX-internal patterns, domain_kc for external tech
  - NEVER write bullets over 80 characters — split into two bullets or use a table
  - IF density < 0.80 THEN replace every prose paragraph with bullets or a table before resubmitting
linked_artifacts:
  primary: p01_kc_knowledge_card
  related: [p01_kc_prompt_caching, p01_kc_rag_fundamentals]
density_score: 0.87
data_source: "validate_kc.py v2.0 — 10 HARD + 20 SOFT gates; _schema.yaml v4.0"
---

# Knowledge Card Best Practices: Density, Structure, and Retrieval

## Executive Summary
Knowledge cards are the atomic retrieval unit in CEX. Quality is measured on five dimensions: D1 Frontmatter completeness, D2 Density (>= 0.80), D3 Axiom form, D4 Section structure, D5 Format compliance. The single most common failure mode is low density — prose paragraphs that dilute signal. The fix is always structural: tables replace descriptions, bullets replace sentences, axioms replace observations.

## Spec Table
| Property | Requirement | Gate |
|----------|-------------|------|
| Body size | 200–5120 bytes | H08 (HARD) |
| Density score | >= 0.80 | H08 (HARD) |
| quality field | null | H05 (HARD) |
| id pattern | `p01_kc_[a-z][a-z0-9_]+` | H03 (HARD) |
| Required fields | 14 frontmatter | H06 (HARD) |
| Sections | >= 4, each >= 3 lines | S06, S08 (SOFT) |
| Largest section | >= 30% of body | S07 (SOFT) |
| Tables | >= 1 | S11 (SOFT) |
| Code blocks | >= 1 | S12 (SOFT) |
| External URL | >= 1 | S13 (SOFT) |
| Bullets | <= 80 chars each | S10 (SOFT) |
| tldr | <= 160 chars, no self-ref | S01, S02 (SOFT) |
| Axioms | ALWAYS/NEVER/IF-THEN | S18 (SOFT) |

## Patterns

### Density Boosting (apply in order)
| Technique | Before | After | Density lift |
|-----------|--------|-------|-------------|
| Prose → bullets | `Caching improves performance in several ways. First, it reduces database load. Second, it speeds up response times. Finally, it enables offline functionality.` | `- Reduces database load`<br>`- Speeds up response times`<br>`- Enables offline functionality` | +0.15 |
| Description → table | `Redis is fast but memory-limited. PostgreSQL is reliable but slower. MongoDB is flexible but inconsistent.` | `\| DB \| Speed \| Reliability \|`<br>`\|----\|-------\|------------\|`<br>`\| Redis \| Fast \| Memory-limited \|`<br>`\| Postgres \| Slow \| High \|`<br>`\| Mongo \| Medium \| Variable \|` | +0.20 |
| Remove transitions | `As mentioned earlier, validation is important. Furthermore, we should note that error handling matters.` | `- Validation prevents bad data`<br>`- Error handling improves UX` | +0.05 |
| Compound → atomic | `- Configure timeouts, retries, and circuit breakers for resilience` | `- Set timeout: 5s max`<br>`- Configure retries: 3x with backoff` | +0.05 |
| Observation → axiom | `Validation helps prevent errors and improves data quality.` | `ALWAYS validate input at system boundaries` | +0.05 |
| Lists → categorized table | `Tools: Redis, PostgreSQL, MongoDB, Elasticsearch, Memcached, DynamoDB` | `\| Type \| Tool \| Use case \|`<br>`\|------\|------\|---------\|`<br>`\| Cache \| Redis \| Session data \|`<br>`\| DB \| Postgres \| Transactional \|` | +0.12 |
| Verbose → concise rule | `When you are working with large datasets, it's generally recommended that you implement proper indexing strategies to ensure optimal query performance.` | `ALWAYS index query columns in tables >100K rows` | +0.08 |
| Scattered examples → consolidated | Examples mixed throughout paragraphs | `## Examples`<br>`\| Pattern \| Code \|`<br>`\|-------\|-----\|`<br>`\| Auth \| req.user.id \|` | +0.06 |
| Remove hedging language | `Redis might be a good choice for caching, and it could potentially improve performance in most cases.` | `Redis: sub-1ms reads, 100K ops/sec capacity` | +0.04 |
| Questions → direct statements | `How do you handle errors? What about timeouts? When should you retry?` | `- Handle errors: catch + log + fallback`<br>`- Set timeouts: 5s max`<br>`- Retry: 3x with exponential backoff` | +0.07 |
| Workflow prose → steps | `The process involves first setting up the connection, then authenticating, and finally executing the query.` | `1. Connect: `client.connect(url)`<br>`2. Auth: `client.auth(token)`<br>`3. Query: `client.execute(sql)`` | +0.09 |

### Body Structure Selection
```
Topic is about external tech/API/protocol?
  YES → domain_kc body:
        Quick Ref | Key Concepts | Strategy Phases | Golden Rules | Flow | Compare | References
  NO (CEX-internal pattern/lesson)?
  YES → meta_kc body:
        Exec Summary | Spec Table | Patterns | Anti-Patterns | Application | References
```

### Frontmatter — 14 Required Fields
| Field | Format | Example | Validator rule |
|-------|--------|---------|---------------|
| id | `p01_kc_{topic_slug}` | `p01_kc_rag_fundamentals` | H03: regex match pillar_kc_pattern |
| kind | literal `knowledge_card` | `knowledge_card` | H04: exact string match |
| pillar | `P01` through `P12` | `P01` | H06: valid pillar code |
| title | 5-100 chars | `"RAG Pipeline Best Practices"` | S01: length constraint |
| version | semver format | `"1.0.0"` or `"2.1.3"` | H07: semver validation |
| created | ISO date | `"2026-04-02"` | H06: YYYY-MM-DD format |
| updated | ISO date | `"2026-04-02"` | H06: YYYY-MM-DD format |
| author | agent_group name | `"knowledge-card-builder"` | H10: not "orchestrator" |
| domain | snake_case label | `knowledge_management` | H06: no spaces/caps |
| quality | literal `null` | `null` | H05: HARD fail if numeric |
| tags | YAML list ≥3 items | `[rag, embedding, retrieval]` | H07: array format |
| tldr | ≤160 chars, no self-ref | `"Vector search + LLM for context"` | S01,S02: length + content |
| when_to_use | specific trigger | `"When building Q&A over docs"` | S03: actionable context |
| keywords | 2-5 search terms | `[rag, vector_search, embedding]` | S04: retrieval optimization |

### Retrieval Optimization by Field
| Field | Retrieval role | High-signal example |
|-------|---------------|-------------------|
| tldr | Primary BM25 + embedding match | "Execute CLI via subprocess, retry 3x on timeout" |
| keywords | Exact-match boost | `[subprocess, retry, cli_execution]` |
| long_tails | Semantic/vector search | "how to retry failed subprocess calls in Python" |
| when_to_use | Agent activation trigger | "When integrating CLI tools with 3+ retry requirement" |
| tags | Faceted filter | Mix domain (`python`) + technique (`retry`) + tier (`production`) |

## Anti-Patterns
| Anti-Pattern | Failure | Fix |
|-------------|---------|-----|
| `quality: 8.5` | H05 HARD fail | Set `quality: null` |
| `tags: "ai, ml"` as string | H07 HARD fail | Convert to YAML list `[ai, ml]` |
| Internal paths in body | H09 HARD fail | Remove all `.claude/`, `records/`, `C:\` |
| `author: orchestrator` | H10 HARD fail | Use agent_group/builder name |
| `id: prompt_caching` | H03 HARD fail | Prefix: `p01_kc_prompt_caching` |
| Body > 5120 bytes | H08 HARD fail | Split into 2 focused atomic cards |
| tldr: "This card describes…" | S01 SOFT fail | Start with the fact, not a description |
| Axiom: "Caching helps" | S18 SOFT fail | Rewrite as "ALWAYS declare cache TTL" |
| Density < 0.80 | H08 HARD fail | Replace prose with tables and bullets |
| Missing external URL | S13 SOFT fail | Add URL in References section |

## Application

### Step-by-Step Knowledge Card Creation
| Step | Action | Command/Example | Success criteria |
|------|--------|----------------|-----------------|
| 1. Type selection | Choose meta_kc (CEX internal) or domain_kc (external tech) | Check topic: CEX patterns → meta_kc, API/framework → domain_kc | Clear body structure template selected |
| 2. Frontmatter first | Draft all 14 required fields before writing body | `id: p01_kc_topic_name`<br>`quality: null`<br>`tags: [tag1, tag2, tag3]` | All fields present, passes `validate_kc.py --frontmatter` |
| 3. Dense formatting | Start with tables for comparisons, bullets for lists, avoid prose | Replace "X is good because Y" with `\| Tool \| Benefit \|`<br>`\|------\|--------\|`<br>`\| X \| Y \|` | Density estimate >= 0.85 |
| 4. Axiom writing | Review all statements, convert observations to rules | "Validation helps" → `ALWAYS validate input at boundaries` | ≥3 ALWAYS/NEVER/IF-THEN statements |
| 5. Density measurement | Count data lines / total non-empty lines | `grep -c '^\|' file.md` (tables) + `grep -c '^-' file.md` (bullets) | Calculated score >= 0.80 |
| 6. Validation cycle | Run validator, fix HARD gates first, then SOFT | `python _tools/validate_kc.py file.md`<br>Fix H-gates → rerun → fix S-gates | All H-gates PASS, ≥80% S-gates PASS |
| 7. Size check | Verify 200-5120 byte range | `wc -c file.md` | 200 ≤ bytes ≤ 5120 |
| 8. Final review | Check external URL, code block, table requirements | Ensure References section has ≥1 URL, ≥1 `code block`, ≥1 table | Meets S11, S12, S13 requirements |

## References
- Validator: `_tools/validate_kc.py` v2.0 — 10 HARD + 20 SOFT gates
- Schema: `P01_knowledge/_schema.yaml` v4.0 — canonical field definitions
- Golden example: `p01_kc_prompt_caching.md` — density 0.91, passes all gates
- Builder spec: `archetypes/builders/knowledge-card-builder/bld_instruction_knowledge_card.md`
- Source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching (density reference example)