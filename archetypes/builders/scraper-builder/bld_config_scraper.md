---
kind: config
id: bld_config_scraper
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: scraper Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_scraper_{target_slug}.md` + `.yaml` | `p04_scraper_marketplace.md` |
| Builder directory | kebab-case | `scraper-builder/` |
| Frontmatter fields | snake_case | `output_format`, `rate_limit` |
| Target slug | snake_case, lowercase, no hyphens | `marketplace`, `news_feed` |
| Selector names | snake_case, noun pattern | `product_title`, `price`, `rating` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_scraper_{target_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_scraper_{target_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2000 bytes
- Density: >= 0.80 (no filler)
## Pagination Enum
| Value | When to use |
|-------|-------------|
| next_page | "Next" link or button to follow |
| infinite_scroll | JavaScript-rendered infinite scroll |
| numbered | Page number in URL (?page=2, /page/3) |
| none | Single page, no pagination needed |
## Anti-Bot Enum
| Value | Techniques needed |
|-------|------------------|
| none | Direct access, no protection |
| basic | Rotate User-Agent, respect robots.txt |
| cloudflare | JS challenge bypass, TLS fingerprint |
| captcha | CAPTCHA solving service required |
## Output Format Enum
| Value | When to use |
|-------|-------------|
| json | Structured data for downstream processing (default) |
| csv | Tabular data for spreadsheets or bulk import |
| yaml | Config-like hierarchical data |
