---
quality: 8.9
quality: 8.2
id: spec_notebooklm_chrome_cdp
kind: spec
title: "NotebookLM Full Integration via Chrome CDP"
version: 1.0.0
status: SPEC
nucleus: N05
pillar: P04
created: 2026-04-19
author: N05
tags: [notebooklm, chrome, cdp, playwright, media, automation]
tldr: "Connect to any user's Chrome via CDP, automate NotebookLM end-to-end: create notebooks, upload sources, generate audio/video/slides/quizzes, download results."
density_score: 0.92
updated: "2026-04-22"
---

# NotebookLM Full Integration via Chrome CDP

## Problem

NotebookLM has no public API. The existing `notebooklm-mcp` server launches its
own Chromium instance with separate auth -- fragile, breaks on cookie expiry, and
requires re-authentication every session. Users already have Chrome open and logged
into Google. We should use THEIR browser, not fight a parallel one.

## Solution: Chrome CDP + Playwright MCP

```
User's Chrome (already logged into Google)
    |
    +-- launched with: --remote-debugging-port=9222
    |
    v
Playwright MCP server (connects via CDP endpoint)
    |
    v
Claude Code (browser_navigate, browser_click, browser_evaluate, etc.)
    |
    v
NotebookLM UI automation (create, upload, generate, download)
```

## Prerequisites

### 1. Chrome CDP Launch (one-time per session)

```powershell
# boot/chrome_cdp.ps1 handles this:
# - Detects Chrome install path from registry
# - Uses YOUR profile (cookies, sessions, extensions intact)
# - Launches with --remote-debugging-port=9222
.\boot\chrome_cdp.ps1
```

Cross-platform equivalent:

| OS | Command |
|----|---------|
| Windows | `boot\chrome_cdp.ps1` |
| macOS | `open -a "Google Chrome" --args --remote-debugging-port=9222` |
| Linux | `google-chrome --remote-debugging-port=9222 --user-data-dir=$HOME/.config/google-chrome` |

### 2. Playwright MCP Configuration

In `.mcp.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-playwright@latest"],
      "env": {
        "PLAYWRIGHT_CDP_URL": "http://localhost:9222"
      },
      "disabled": false
    }
  }
}
```

Key: `PLAYWRIGHT_CDP_URL` tells Playwright to CONNECT to existing Chrome
instead of launching a new browser. This inherits ALL user sessions.

### 3. Verify Connection

```bash
curl -s http://localhost:9222/json/version
# Should return: { "Browser": "Chrome/...", "webSocketDebuggerUrl": "ws://..." }
```

## NotebookLM Capabilities (Full Automation Map)

### Tier 1: Source Management

| Action | Method | UI Path |
|--------|--------|---------|
| Create notebook | Click "Criar novo" on homepage | `button "Criar novo notebook"` |
| Upload text source | "Texto copiado" in add-source dialog | Fill textbox + click "Inserir" |
| Upload file (PDF/doc) | "Enviar arquivos" button | File upload dialog |
| Add web source | "Sites" button + paste URL | URL input + submit |
| Add YouTube source | "Sites" button + paste YT URL | Same as web |
| Import from Drive | "Drive" button | Google Drive picker |
| Delete source | Source context menu > delete | `button "Mais"` on source card |

### Tier 2: Studio Outputs (the real value)

| Output | Button | Customization Options | Generation Time |
|--------|--------|-----------------------|-----------------|
| Resumo em Audio | `audio_magic_eraser` icon | Format (4 types), Language, Duration, Focus prompt | 2-5 min |
| Resumo em Video | `subscriptions` icon | Format (2 types), Language, Visual style, Focus prompt | 3-8 min |
| Apresentacao de slides | `tablet` icon | Direct generation | 1-2 min |
| Mapa mental | `flowchart` icon | Direct generation | 30s-1 min |
| Relatorios | `auto_tab_group` icon | Direct generation | 1-2 min |
| Cartoes didaticos | `cards_star` icon | Direct generation | 30s-1 min |
| Teste (Quiz) | `quiz` icon | Direct generation | 30s-1 min |
| Infografico | `stacked_bar_chart` icon | Direct generation | 1-2 min |
| Tabela de dados | `table_view` icon | Direct generation | 30s |

### Tier 3: Conversation

| Action | Method |
|--------|--------|
| Ask question about sources | Fill chat textbox + submit |
| Get citations | Responses include source references |
| Save to notes | "Salvar nas notas" button on responses |

## Audio Overview: Format Options

| Format | PT-BR Name | Description |
|--------|------------|-------------|
| Deep Dive | Analise detalhada | Animated conversation between 2 hosts explaining themes |
| Summary | Resumo | Brief overview of main ideas |
| Critique | Critica | Expert analysis with constructive feedback |
| Debate | Debate | Intelligent debate with different perspectives |

## Video Overview: Format Options

| Format | Description |
|--------|-------------|
| Standard | AI-generated video with visuals and narration |
| Custom focus | User-directed focus prompt |

Visual styles are selectable via radio buttons in the generation dialog.

## Automation Cookbook

### Recipe 1: Upload Text + Generate Audio + Video

```
1. browser_navigate -> https://notebooklm.google.com/
2. browser_click -> "Criar novo notebook"
3. browser_click -> "Texto copiado"
4. browser_evaluate -> inject text into textarea (el.value = content; dispatch input event)
5. browser_click -> "Inserir"
6. browser_click -> "Resumo em Audio" (Studio panel)
7. browser_click -> "Gerar" (accept defaults or customize)
8. browser_click -> "Resumo em Video" (Studio panel)
9. browser_click -> "Gerar"
```

### Recipe 2: Upload Multiple Sources to Existing Notebook

```
1. browser_navigate -> notebook URL
2. browser_click -> "Adicionar fontes"
3. For each source:
   a. browser_click -> "Texto copiado"
   b. browser_evaluate -> inject content
   c. browser_click -> "Inserir"
   d. browser_click -> "Adicionar fontes" (repeat)
```

### Recipe 3: Generate All Studio Outputs

```
For each output type in [Audio, Video, Slides, Mind Map, Report, Flashcards, Quiz, Infographic, Data Table]:
1. browser_click -> output button in Studio panel
2. If customization dialog appears: configure + click "Gerar"
3. Wait for generation (check for progress indicator)
```

## UI Selectors (PT-BR NotebookLM, April 2026)

NotebookLM uses Angular Material. Key patterns:

| Element | Reliable Selector Strategy |
|---------|---------------------------|
| Buttons | `button:has-text("Texto exato")` or aria role |
| Textboxes | `textbox` role + name/placeholder |
| Dialogs | `dialog` role -- always modal |
| Checkboxes | `checkbox` role inside source cards |
| Radio groups | `radiogroup` role for format/language selection |
| Comboboxes | `combobox` role for language dropdown |

### Content Injection Pattern (Critical)

Standard `browser_type` is too slow for large content. Use `browser_evaluate`:

```javascript
(el) => {
  el.focus();
  el.value = CONTENT_STRING;
  el.dispatchEvent(new Event('input', {bubbles: true}));
  el.dispatchEvent(new Event('change', {bubbles: true}));
  return el.value.length;
}
```

This bypasses character-by-character typing and triggers Angular's change detection.

### Overlay Trap (Known Issue)

Clicking a combobox (e.g., language selector) opens a Material overlay that
blocks clicks on other elements. Fix: press `Escape` to dismiss the overlay
before clicking the target button.

## Limits (NotebookLM, April 2026)

| Limit | Free | Pro |
|-------|------|-----|
| Notebooks | 100 | 500 |
| Sources per notebook | 50 | 300 |
| Words per source | 500K | 500K |
| Daily queries | 50 | 500 |
| Audio generation | Yes | Yes (priority) |
| Video generation | Yes (limited) | Yes (priority) |

## Security Considerations

- CDP exposes full browser control. Only bind to localhost (default).
- `--remote-allow-origins=*` is required for Playwright but scoped to localhost.
- Never expose port 9222 to network (firewall rule).
- User's Google session cookies are accessible -- treat with care.
- All automation runs in user's own browser context (no credential theft risk).

## Integration with CEX Media Pipeline

```
cex_media_produce.py --concept 8f --format audio --lang en
    |
    v
Produces: _output/mentor/8f/en/audio_source.md
    |
    v
N05 (this spec): Playwright MCP automation
    |
    +-- Create notebook (or reuse existing by ID)
    +-- Upload audio_source.md as "Texto copiado"
    +-- Trigger "Resumo em Audio" generation
    +-- Trigger "Resumo em Video" generation
    +-- Record notebook ID in media_config.yaml
    |
    v
Output: NotebookLM generates podcast + video asynchronously
User checks NotebookLM later to download/share
```

## Future: Full Programmatic Pipeline

When NotebookLM releases a public API (rumored for Google AI Pro):
1. Replace Playwright automation with API calls
2. Keep CDP path as fallback for free-tier users
3. Add download automation (currently manual -- no download button accessible via CDP)

## Artifacts to Create

| Action | Path | Kind |
|--------|------|------|
| UPDATE | `boot/chrome_cdp.ps1` | Add cross-platform instructions in header |
| UPDATE | `.mcp.json` | Ensure playwright CDP config is documented |
| UPDATE | `N05_operations/P09_config/media_config.yaml` | Add notebook ID tracking |
| CREATE | `_tools/cex_notebooklm_cdp.py` | CLI wrapper: concept -> CDP upload -> generate |

## Properties

| Property | Value |
|----------|-------|
| Kind | spec |
| Pillar | P04 (Tools) |
| Nucleus | N05 |
| Domain | media automation |
| Quality target | 9.0+ |
