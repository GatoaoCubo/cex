---
kind: config
id: bld_config_browser_tool
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: browser_tool Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_browser_{target_slug}.md` | `p04_browser_marketplace_scraper.md` |
| Builder directory | kebab-case | `browser-tool-builder/` |
| Frontmatter fields | snake_case | `output_format`, `headless`, `user_agent` |
| Target slug | snake_case, lowercase, no hyphens | `marketplace_scraper`, `checkout_flow` |
| Action names | lowercase verb | `navigate`, `click`, `extract`, `screenshot` |
| Selector values | lowercase | `css`, `xpath`, `aria`, `data_attr`, `text` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_browser_{target_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_browser_{target_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~3500 bytes
- Density: >= 0.80 (no filler)
## Engine Enum
| Value | Notes |
|-------|-------|
| playwright | Default. Python/JS/TS, cross-browser, auto-wait |
| puppeteer | Node.js only, Chrome/Chromium |
| selenium | Legacy/enterprise, remote grid |
| browser_use | LLM-driven, Python |
| browserbase | Cloud headless, managed |
| stagehand | TypeScript, AI-assisted |
## Output Format Enum
| Value | When to use |
|-------|-------------|
| json | Structured data extraction, machine-readable |
| html | Raw DOM snapshot for downstream parsing |
| screenshot | Visual capture, debugging, verification |
| text | Plain text extraction, readable content |
## Action Enum
| Value | Description |
|-------|-------------|
| navigate | Load a URL and wait for page state |
| click | Activate an element |
| type | Input text into a form field |
| scroll | Scroll page or element in a direction |
| wait | Pause until selector or condition is met |
| screenshot | Capture viewport or full page |
| extract | Read structured data from DOM elements |
| evaluate | Execute arbitrary JavaScript in page context |
| hover | Move pointer to element without clicking |
| select | Choose an option in a select/dropdown element |
## Timeout Conventions
| Scenario | Recommended timeout |
|----------|---------------------|
| Simple static page | 10000ms |
| SPA / dynamic content | 30000ms (default) |
| Slow e-commerce | 45000ms |
| Network-intercepted mock | 5000ms |
Rule: every browser_tool MUST define timeout (implicit default 30000ms is acceptable if not overridden, but explicit is preferred).
