---
id: p04_browser_tool_NAME
kind: browser_tool
pillar: P04
version: 1.0.0
title: "Template — Browser Tool"
tags: [template, browser, scraping, web, automation]
tldr: "Configures a headless browser tool for web scraping, screenshot capture, or page interaction. Defines navigation rules, extraction patterns, and rate limits."
quality: 9.0
updated: "2026-04-07"
domain: "tool integration"
author: n03_builder
created: "2026-04-07"
density_score: 0.97
---

# Browser Tool: [NAME]

## Purpose
[WHAT web task — scraping, screenshot, form filling, monitoring]

## Configuration
```yaml
engine: [playwright | puppeteer | selenium]
headless: true
timeout_ms: [30000]
viewport: { width: 1280, height: 720 }
user_agent: "[custom or default]"
proxy: "[PROXY_URL or null]"
```

## Navigation Rules

| Action | Config | Example |
|--------|--------|---------|
| Go to URL | `navigate(url)` | `navigate("https://example.com")` |
| Wait for element | `wait_for(selector, timeout)` | `wait_for("#content", 5000)` |
| Click | `click(selector)` | `click("button.submit")` |
| Extract text | `text(selector)` | `text("h1.title")` |
| Screenshot | `screenshot(path, full_page)` | `screenshot("out.png", true)` |

## Extraction Pattern
```python
async def extract(page):
    return {
        "title": await page.text_content("h1"),
        "price": await page.text_content(".price"),
        "links": await page.eval_on_selector_all("a", "els => els.map(e => e.href)"),
    }
```

## Rate Limiting
- **Delay between requests**: [1000-3000]ms
- **Max concurrent pages**: [3]
- **Respect robots.txt**: [yes | no]
- **Max pages per session**: [100]

## Error Handling
- **Page not found (404)**: Log + skip + continue
- **Timeout**: Retry 1x, then mark as failed
- **CAPTCHA**: Abort + flag for manual review
- **Rate limited (429)**: Backoff [30s], retry [2x]

## Quality Gate
- [ ] Engine specified (playwright preferred)
- [ ] Rate limits defined (no accidental DDoS)
- [ ] Extraction selectors documented
- [ ] Error handling for 404/timeout/captcha
