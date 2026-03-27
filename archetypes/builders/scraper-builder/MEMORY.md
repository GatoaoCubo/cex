---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: scraper-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Using hyphens in id slug (must be underscores: p04_scraper_marketplace not p04_scraper_e-commerce)
2. Setting quality to a number instead of null (H05 rejects any non-null value)
3. selectors list not matching ## Selectors section field names exactly (S03 drift)
4. Missing target field (required — cannot scrape without knowing where)
5. Omitting output_format (required — consumer needs to know data structure)
6. Including implementation code in body (this is a spec, not source)
7. Writing selector entries without CSS/XPath or extraction rule (S05 incomplete)
8. Exceeding 1024 bytes body limit (scraper is compact)
9. Confusing scraper with client (scraper extracts HTML, client consumes API)
10. Omitting rate_limit and pagination (## Pagination & Rate Limiting section required)

### Effective Patterns
- Selector naming: noun in snake_case — `product_title`, `price`, `seller_name`
- Target: full URL with path to searchable/listable page
- selectors mirror: write the list in frontmatter FIRST, then expand each in body
- Overview pattern: "Extracts {data} from {site}. Used by {consumer} for {purpose}."
- Body budget: Overview(80B) + Selectors(550B) + Pagination(200B) + Output(150B) = ~980B
- Always try JSON-LD selector first (structured data = more reliable)

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | id hyphens, selectors drift, missing target |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a scraper, update:
- New common mistake (if encountered)
- New effective pattern (if discovered)
- Production counter increment
