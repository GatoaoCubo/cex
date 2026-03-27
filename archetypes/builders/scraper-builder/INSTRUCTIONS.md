---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for scraper
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a scraper

## Phase 1: RESEARCH
1. Identify the target site/domain and primary data to extract
2. Determine selector strategy: CSS selectors, XPath, or structured data (JSON-LD)
3. List every data field the scraper extracts (concrete field names)
4. Determine pagination strategy: next_page, infinite_scroll, numbered, or none
5. Identify rate_limit constraints (requests per unit time, politeness delay)
6. Assess anti_bot measures on target (Cloudflare, CAPTCHA, fingerprinting)
7. Check for existing scraper artifacts via brain_query [IF MCP] (avoid duplicates)
8. Confirm target slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write selectors list with exact names matching ## Selectors body section
5. Write ## Overview: 1-2 sentences on target site and extracted data
6. Write ## Selectors: for each field, define selector, type, extraction rule
7. Write ## Pagination & Rate Limiting: pagination strategy, rate limits, delays
8. Write ## Output: output format, validation rules, freshness policy
9. Verify body <= 1024 bytes
10. Verify id matches `^p04_scraper_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm selectors list matches field names in ## Selectors section (zero drift)
4. Confirm quality == null
5. Confirm body has all 4 required sections
6. Confirm body <= 1024 bytes
7. Score SOFT gates against QUALITY_GATES.md
8. Revise if score < 8.0 before outputting
