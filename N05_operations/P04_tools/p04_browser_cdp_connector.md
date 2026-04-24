---
id: p04_browser_cdp_connector
kind: browser_tool
8f: F5_call
pillar: P04
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "n05_operations"
name: "Chrome CDP Connector"
engine: playwright
actions: [navigate, click, type, wait, extract, screenshot, evaluate]
selectors: [css, aria, text, data_attr]
output_format: json
headless: false
viewport: "1280x720"
timeout: 30000
javascript: true
cookies: true
stealth: false
quality: 9.1
tags: [browser_tool, cdp, chrome, connector, playwright, P04, automation]
tldr: "Generic CDP connector for user Chrome: setup, connect, navigate, interact. Base layer for all browser_tool specs."
description: "Connects to user Chrome via CDP WebSocket on localhost:9222. Provides navigate/click/type/read/screenshot primitives."
density_score: 1.0
related:
  - p04_browser_playwright
  - bld_knowledge_card_browser_tool
  - bld_config_browser_tool
  - p04_tk_browser_tools
  - p10_lr_browser_tool_builder
  - bld_output_template_browser_tool
  - spec_notebooklm_pipeline
  - bld_schema_browser_tool
  - bld_examples_browser_tool
  - bld_instruction_browser_tool
---

## Overview

Generic CDP connector that bridges Claude Code (CLI) to the user's real Chrome browser.
All target-specific browser_tools (Supabase, Railway, NotebookLM) depend on this connector.
Uses Chrome DevTools Protocol over WebSocket. User's logged-in sessions are preserved.

## Engine

Engine: Playwright MCP (`@playwright/mcp --cdp-endpoint http://localhost:9222`) OR direct
WebSocket via `_tools/cex_cdp.py`. Headless: false (user's real Chrome). Viewport: user's
actual viewport. Timeout: 30000ms default. JavaScript: enabled. Cookies: user's real cookies.

Prerequisites:
1. Chrome launched with `--remote-debugging-port=9222 --remote-allow-origins=*`
2. User logged into target accounts
3. Either: Playwright MCP enabled in `.mcp.json` OR `cex_cdp.py` for direct CDP

## Actions

### navigate

Opens URL in specified tab. Uses Page.navigate CDP method.
Params: `url` (string, required), `tab` (int, optional: 0).
Wait: networkidle or 5s timeout.
CLI: `python _tools/cex_cdp.py navigate https://example.com`

### click

Clicks element using multi-strategy selector resolution.
Params: `selector` (string, required), `tab` (int, optional).
Strategies (auto-detected):
- `text:Label` -- innerText match (default if no prefix)
- `aria:label` -- aria-label attribute
- `css:.class` or `css:[attr]` -- CSS selector
- `coord:x,y` -- pixel coordinates via Input.dispatchMouseEvent
CLI: `python _tools/cex_cdp.py click "text:Criar novo notebook"`

### type

Types text into input/textarea with React/Angular compatibility.
Uses native value setter + input/change event dispatch.
Params: `selector` (string, required), `text` (string, required).
CLI: `python _tools/cex_cdp.py type "css:textarea" "Hello world"`

### wait

Polls for element appearance or page state change.
Params: `selector` (string, optional), `timeout` (int, optional).
CLI: `python _tools/cex_cdp.py eval "document.querySelector('.done') !== null"`

### extract

Reads page content: full text, element text, or structured data via JS eval.
Params: `expression` (string, optional: defaults to document.body.innerText).
CLI: `python _tools/cex_cdp.py read` or `python _tools/cex_cdp.py eval "document.title"`

### screenshot

Captures viewport as PNG via Page.captureScreenshot CDP method.
Params: `output` (string, optional: file path).
CLI: `python _tools/cex_cdp.py screenshot --output /tmp/screen.png`

### evaluate

Runs arbitrary JavaScript in page context. Returns result value.
Params: `expression` (string, required).
CLI: `python _tools/cex_cdp.py eval "document.querySelectorAll('button').length"`

## Selectors

Priority order: text > aria > css > coord

1. **text** (`text:Label`): Most reliable for modern SPAs. Matches innerText.
2. **aria** (`aria:Label`): Google products use extensive ARIA labeling.
3. **css** (`css:.class`, `css:[data-testid]`): Structural, may break on redesign.
4. **coord** (`coord:x,y`): Pixel-level click. Last resort. Viewport-dependent.

Fallback rule: if no prefix given, auto-detect (starts with `.` `#` `[` = css, else = text).

## Output Format

Primary: json (for programmatic use) or plain text (for CLI).
Status check: `python _tools/cex_cdp.py status` returns JSON:

```json
{
  "active": true,
  "browser": "Chrome/147.0.7727.56",
  "tabs": 5,
  "port": 9222
}
```

## Connection Lifecycle

### 1. Launch Chrome with CDP

```powershell
# Windows (PowerShell)
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
    --remote-debugging-port=9222 `
    --remote-allow-origins=* `
    --user-data-dir="$env:LOCALAPPDATA\Google\Chrome\User Data"
```

If Chrome is already running without `--remote-debugging-port`, it must be restarted
with the flag. Existing tabs and sessions are preserved when using the same
`--user-data-dir`.

### 2. Verify CDP endpoint

```bash
python _tools/cex_cdp.py status
# Expected: {"active": true, "browser": "Chrome/...", "tabs": N, "port": 9222}
```

If status returns `{"active": false}`, Chrome is not listening on port 9222.

### 3. Connect via Playwright MCP

The `.mcp.json` config connects Playwright to the running Chrome:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--cdp-endpoint", "http://localhost:9222"]
    }
  }
}
```

### 4. Connect via direct WebSocket

For non-MCP usage (scripts, CI, other runtimes):

```python
import websocket, json

ws = websocket.create_connection("ws://localhost:9222/json/version")
info = json.loads(ws.recv())
ws_url = info["webSocketDebuggerUrl"]
# Now connect to ws_url for CDP commands
```

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| Connection refused :9222 | Chrome not launched with CDP flag | Restart Chrome with `--remote-debugging-port=9222` |
| No tab found | All tabs closed or navigated away | Open a new tab or navigate to target URL |
| Element not found | Selector mismatch or page not loaded | Wait for page load, try alternative selector strategy |
| Timeout (30s) | Page or element load too slow | Increase timeout or check network connectivity |
| Stale element | SPA re-rendered DOM after selector resolved | Re-query the selector before interacting |
| Permission denied | Chrome profile locked by another process | Close other Chrome instances using same profile |

## Dependency Graph

This connector is the base layer. All target-specific browser_tools depend on it:

```
p04_browser_cdp_connector (this file)
    |
    +-- p04_browser_supabase_ui.md    (Supabase dashboard automation)
    +-- p04_browser_railway_ui.md     (Railway deploy automation)
    +-- p04_browser_notebooklm_ui.md  (NotebookLM content automation)
    +-- (future browser_tool specs)
```

Each target spec inherits the CDP connection, selector strategies, and action primitives
defined here. Target specs add domain-specific flows (e.g., Supabase SQL editor sequences,
Railway deploy triggers) built on top of these primitives.

## Security Notes

- CDP exposes full browser control. Only bind to localhost (default).
- `--remote-allow-origins=*` is required for MCP but limits to local connections.
- User cookies and sessions are live -- any CDP command runs as the logged-in user.
- Never expose port 9222 to network. No `--remote-debugging-address=0.0.0.0`.
- Treat CDP access as equivalent to full browser session hijacking.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_browser_playwright]] | sibling | 0.37 |
| [[bld_knowledge_card_browser_tool]] | upstream | 0.30 |
| [[bld_config_browser_tool]] | downstream | 0.27 |
| [[p04_tk_browser_tools]] | related | 0.25 |
| [[p10_lr_browser_tool_builder]] | downstream | 0.23 |
| [[bld_output_template_browser_tool]] | downstream | 0.23 |
| [[spec_notebooklm_pipeline]] | downstream | 0.22 |
| [[bld_schema_browser_tool]] | downstream | 0.22 |
| [[bld_examples_browser_tool]] | downstream | 0.22 |
| [[bld_instruction_browser_tool]] | upstream | 0.21 |
