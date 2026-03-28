---
kind: knowledge_card
id: bld_knowledge_card_browser_tool
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for browser_tool production — browser automation and DOM interaction specification
sources: Playwright docs, Puppeteer API, W3C WebDriver, ARIA spec, CSS selectors level 4
---

# Domain Knowledge: browser_tool
## Executive Summary
Browser tools are DOM-driven automation artifacts that control a browser engine to interact with web pages. They navigate URLs, interact with elements via selectors, extract structured data, and return output as JSON, HTML, screenshot, or text. Browser tools are NOT generic screen controllers (computer_use), NOT search API wrappers (search_tool), and NOT image analyzers (vision_tool). The key distinction: browser_tool operates via the DOM API — it reads and manipulates the document object model, not raw pixels.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Output formats | json, html, screenshot, text |
| Default engine | playwright |
| Default headless | true |
| Default timeout | 30000ms |
| Default viewport | 1280x720 |
| Selector priority | data_attr > aria > css > xpath |
## Engine Decision Matrix
| Need | Engine | Reason |
|------|--------|--------|
| Modern web, cross-browser, Python/JS | playwright | Best selector API, auto-wait, network interception |
| Chrome-only, Node.js team | puppeteer | Native Chrome DevTools Protocol, fast |
| Legacy apps, Java/Python, grid | selenium | Widest language support, remote grid |
| LLM-directed autonomous browsing | browser_use | Natural language to DOM actions |
| Cloud-scale, no infra | browserbase | Managed headless, built-in stealth |
| AI-assisted, TypeScript-native | stagehand | Semantic actions, vision+DOM hybrid |
## Action Reference
| Action | Purpose | Key Params |
|--------|---------|-----------|
| navigate | Load URL, wait for page state | url, waitUntil (load/networkidle/domcontentloaded) |
| click | Activate element | selector, button (left/right/middle), clickCount |
| type | Input text into field | selector, text, delay (ms between keystrokes) |
| scroll | Scroll page or element | direction (up/down/left/right), distance (px) |
| wait | Pause until condition | selector, timeout, state (visible/hidden/attached) |
| screenshot | Capture viewport or element | fullPage, path, clip (region), quality |
| extract | Read data from DOM | selector, attribute, multiple (boolean) |
| evaluate | Execute JavaScript in page context | script, args |
| hover | Move pointer to element | selector, position (top/center/bottom) |
| select | Choose option in select element | selector, value or label |
## Selector Strategy Guide
| Strategy | Syntax | Stability | Speed | When to use |
|----------|--------|-----------|-------|-------------|
| data_attr | `[data-testid="name"]` | High | Fast | QA-annotated elements, test-stable |
| aria | `[aria-label="Submit"]` | High | Fast | Accessible elements, form controls |
| css | `.product-price` | Medium | Fast | Well-maintained CSS classes |
| xpath | `//div[@class="price"]` | Low | Slower | Deep nesting, attribute conditions |
| text | `text=Add to Cart` | Medium | Medium | Buttons, links with stable text |
Fallback chain: attempt selectors in priority order; if primary returns null, try next before throwing.
## Wait Strategies
| Strategy | Playwright | When |
|----------|-----------|------|
| load | `waitUntil: 'load'` | Simple pages, no AJAX |
| networkidle | `waitUntil: 'networkidle'` | SPAs, dynamic content |
| domcontentloaded | `waitUntil: 'domcontentloaded'` | Fast initial render needed |
| selector visible | `waitForSelector(sel, {state:'visible'})` | Element-specific readiness |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No selector fallback | First fragile selector breaks entire extraction |
| Hardcoded absolute XPath | Breaks on any DOM restructure |
| Missing timeout config | Unbounded waits hang automation indefinitely |
| Omitting headless flag | Headed mode in CI/server environments fails |
| No wait before extract | Race condition: element not yet in DOM |
| Using computer_use for DOM data | Pixel-based reading is fragile vs DOM API |
| Self-scoring quality | Corrupts pool quality metrics |
## Application
1. Define target: what site, what data, what interaction is needed?
2. Choose engine: playwright for most cases; specialize if cloud/LLM/legacy needed
3. List actions in order of execution (navigate -> wait -> extract -> screenshot)
4. Specify selectors with fallback chain per element
5. Set output format: json for structured data, screenshot for visual verification
6. Configure headless, viewport, timeout, stealth as appropriate
7. Validate: actions match frontmatter list, selectors documented, output schema defined
