---
id: kc_chrome_cdp_automation
kind: knowledge_card
pillar: P01
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "n05_operations"
domain: "browser automation"
tags: [knowledge_card, chrome, cdp, browser, automation, playwright, P01]
quality: null
title: "Chrome CDP Browser Automation"
tldr: "Control user Chrome via CDP WebSocket: setup, gotchas, session cookies, click strategies, and NotebookLM integration"
---

# Chrome CDP Browser Automation

## Overview

Chrome DevTools Protocol (CDP) allows programmatic control of Chrome via WebSocket. By launching Chrome with `--remote-debugging-port=9222`, any tool can navigate, click, type, read, and screenshot. CDP is the foundation for Playwright, Puppeteer, and any custom browser automation that needs to operate on the user's actual browser session (with existing logins, cookies, and extensions).

Key advantage over headless: the user's real Chrome profile means all session cookies, OAuth tokens, and logged-in states are available without re-authentication.

## Setup Flow

### Option A: Manual Shortcut Modification

1. Right-click Chrome shortcut -> Properties
2. In "Target", append: `--remote-debugging-port=9222 --remote-allow-origins=*`
3. Close ALL Chrome processes (`taskkill /F /IM chrome.exe /T` or via Task Manager)
4. Open Chrome via the modified shortcut
5. User logs into accounts as usual
6. Tools connect to `http://localhost:9222/json` to discover tabs
7. WebSocket connection to each tab's `webSocketDebuggerUrl`

### Option B: Automated Setup

Run `boot/chrome_cdp.ps1` for guided setup. The script:
- Detects Chrome install path via Windows Registry
- Validates no existing Chrome processes are running
- Launches Chrome with the correct flags
- Confirms CDP is listening on port 9222

### Verifying CDP is Active

```bash
curl http://localhost:9222/json
```

Returns a JSON array of open tabs with `webSocketDebuggerUrl` for each.

## Critical Gotchas (learned 2026-04-17)

### Session Cookies Die on Restart

| Shutdown method | Persistent cookies | Session cookies |
|----------------|-------------------|-----------------|
| `Stop-Process -Force` | LOST | LOST |
| `CloseMainWindow()` (graceful) | Survive | LOST |
| User clicks X | Survive | LOST |
| Never restart | Survive | Survive |

**SOLUTION:** Never restart Chrome for CDP purposes. Modify the shortcut permanently so every user launch includes CDP flags. User opens Chrome once, stays open. All automation connects to the running instance.

Impact: Supabase auth, Google OAuth sessions, and any service using session cookies will require re-login after ANY Chrome restart. This is a Chrome behavior, not a CDP limitation.

### CDP Port Not Binding

- If Chrome is already running WITHOUT the CDP flag, launching a new instance with `--remote-debugging-port=9222` delegates to the existing process (Chrome single-instance behavior). The CDP flag is silently ignored.
- **MUST close ALL Chrome processes** before the first CDP-enabled launch.
- `--remote-allow-origins=*` is REQUIRED. Without it, CDP refuses WebSocket connections from localhost tools with a CORS-like rejection.
- If port 9222 is already in use by another process, Chrome silently falls back to no CDP. Check with: `netstat -ano | findstr :9222`

### Click Strategies (priority order)

| Priority | Selector | Example | When to use |
|----------|----------|---------|-------------|
| 1 | `text:Label` | Find by innerText | Most reliable for Material UI / Angular apps |
| 2 | `aria:label` | aria-label attribute | Google apps use extensively (Gmail, Drive, NotebookLM) |
| 3 | `css:.class` | `css:[data-testid="submit"]` | Structural selectors, stable test IDs |
| 4 | XPath | `//button[contains(text(),'Save')]` | Complex DOM traversal, fallback |
| 5 | `coord:x,y` | Pixel coordinates via `Input.dispatchMouseEvent` | Last resort, viewport-dependent |

**Important:** `.click()` via JavaScript execution often fails on Angular/React/Material UI components because these frameworks intercept and re-dispatch events. Use CDP's `Input.dispatchMouseEvent` (native click simulation) instead.

### Typing into React/Angular Fields

Standard `element.value = 'text'` does NOT trigger React/Angular state updates. The framework's synthetic event system never fires. Must use the prototype setter hack:

```javascript
// For input elements:
var setter = Object.getOwnPropertyDescriptor(
    HTMLInputElement.prototype, 'value'
).set;
setter.call(element, 'your text here');
element.dispatchEvent(new Event('input', { bubbles: true }));

// For textarea elements:
var setter = Object.getOwnPropertyDescriptor(
    HTMLTextAreaElement.prototype, 'value'
).set;
setter.call(element, 'your text here');
element.dispatchEvent(new Event('input', { bubbles: true }));
```

This triggers React's `onChange` handler and Angular's `ngModel` binding correctly.

### Windows Terminal Encoding

All CDP responses (page titles, element text) may contain non-ASCII characters (e.g., PT-BR accented text from Brazilian sites). When printing to Windows terminal:

- Default Windows terminal codec is cp1252, NOT UTF-8
- `print(title)` with accented chars -> `UnicodeEncodeError`
- **Fix:** Always encode output as ASCII with replace: `text.encode('ascii', 'replace').decode('ascii')`
- Or set `PYTHONIOENCODING=utf-8` before running Python scripts

## Tool Stack

| Tool | Purpose | Path |
|------|---------|------|
| `boot/chrome_cdp.ps1` | Launch Chrome with CDP flags | `boot/` |
| `_tools/cex_cdp.py` | CLI helper: navigate, click, type, read, screenshot | `_tools/` |
| `.mcp.json` playwright | MCP server for Playwright (disabled by default) | root |
| `p04_browser_*.md` | browser_tool specs per target site | `N05_operations/P04_tools/` |

### cex_cdp.py Quick Reference

```bash
# Navigate
python _tools/cex_cdp.py navigate "https://example.com"

# Click by text
python _tools/cex_cdp.py click "text:Submit"

# Type into focused element
python _tools/cex_cdp.py type "Hello world"

# Read page text
python _tools/cex_cdp.py read

# Screenshot
python _tools/cex_cdp.py screenshot output.png
```

## NotebookLM Integration (proven 2026-04-17)

End-to-end flow for creating a notebook and generating Audio Overview:

### Step-by-step

1. Navigate to `notebooklm.google.com` (user must be logged into Google)
2. Click "Criar novo notebook" (or "Create new notebook" in EN locale)
3. Click "Texto copiado" ("Copied text") to add a text source
4. Fill the textarea using the React setter hack (see above) + click "Inserir" ("Insert")
5. Click "Estudio" ("Studio") tab in the right panel
6. Click "Resumo em Audio" ("Audio Overview")
7. Configure generation parameters:
   - **Format:** Analise detalhada | Resumo | Critica | Debate
   - **Language:** Selectable dropdown (default follows Google account locale)
   - **Duration:** Curto (Short) | Padrao (Standard)
   - **Focus prompt:** Free text field for guiding the audio generation
8. Click "Gerar" ("Generate")
9. Poll for completion (typically 2-10 minutes depending on source length)

### Gotchas Specific to NotebookLM

- Google apps use `aria-label` extensively -- prefer `aria:` selectors
- The "Estudio" tab may not appear until at least one source is added
- Audio generation is async and server-side -- no local progress indicator
- Generated audio is tied to the notebook and cannot be downloaded via CDP (use the UI download button)

## Open Source Safety

This KC documents tools that interact with the user's local browser. Safety considerations for the public repo:

| Artifact | Safety measure |
|----------|---------------|
| `.mcp.json` | Playwright entry has `disabled: true` with `_setup` hint comment |
| `boot/chrome_cdp.ps1` | Auto-detects Chrome path via Windows Registry, no hardcoded paths |
| `_tools/cex_cdp.py` | Connects to `localhost` only, no credentials stored in code |
| Chrome shortcuts | Modified locally by user/script, NOT tracked in git |
| CDP port | Bound to `127.0.0.1:9222` only (not exposed to network) |

## CDP Protocol Reference

Key CDP domains used by CEX tools:

| Domain | Methods | Purpose |
|--------|---------|---------|
| `Page` | `navigate`, `captureScreenshot`, `getFrameTree` | Page lifecycle |
| `Runtime` | `evaluate`, `callFunctionOn` | JavaScript execution |
| `Input` | `dispatchMouseEvent`, `dispatchKeyEvent` | Native input simulation |
| `DOM` | `getDocument`, `querySelector`, `getOuterHTML` | DOM inspection |
| `Network` | `enable`, `getResponseBody` | Request/response capture |
| `Target` | `getTargets`, `attachToTarget` | Tab/window management |

Full protocol docs: https://chromedevtools.github.io/devtools-protocol/

## Related Artifacts

- `N05_operations/P04_tools/p04_browser_*.md` -- per-site browser tool specs
- `N00_genesis/P04_tools/` -- tool archetype schemas
- `.cex/kinds_meta.json` -- `browser_tool` kind definition
- `archetypes/builders/browser-tool-builder/` -- builder ISOs for browser tools
