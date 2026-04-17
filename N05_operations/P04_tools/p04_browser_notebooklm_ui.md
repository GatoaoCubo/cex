---
id: p04_browser_notebooklm_ui
kind: browser_tool
pillar: P04
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "n05_operations"
name: "NotebookLM UI Automator"
engine: playwright
actions: [navigate, click, type, wait, extract, screenshot]
selectors: [aria, css, text, data_attr]
output_format: json
headless: true
viewport: "1280x720"
timeout: 60000
javascript: true
cookies: true
stealth: false
quality: null
tags: [browser_tool, notebooklm, google, playwright, P04, research]
tldr: "Playwright automator for NotebookLM: notebook select, source upload, prompt compose, Audio Overview submit, status poll, output retrieval"
description: "Automates NotebookLM UI for source management, prompt-driven research, Audio Overview generation, and output extraction"
credentials:
  source: secret_config
  keys: [GOOGLE_AUTH_TOKEN]
  injection: env_var
---

## Overview

Automates Google NotebookLM UI via Playwright. Covers notebook selection, source
document upload, prompt composition for research queries, Audio Overview generation
(submit + poll until complete), and output retrieval. Used by N01 research pipelines
and N04 knowledge workflows. Timeout set to 60s (Audio Overview generation is slow).
MCP fallback: `mcp__notebooklm__*` tools provide direct API access when available.

## Engine

Engine: Playwright (chromium). Headless: true. Viewport: 1280x720.
Timeout: 60000ms per action (Audio Overview generation requires extended wait).
JavaScript: enabled (Angular SPA). Cookies: true (Google auth session).
Auth: Google OAuth via `notebooklm.google.com` login flow.

## Actions

### navigate
Opens NotebookLM home or specific notebook URL.
Params: `url` (string, required): notebook URL or home page.
Wait: `networkidle` or selector `[aria-label="Notebook list"]`.

### click
Clicks notebook cards, source tabs, Audio Overview button, download links.
Params: `selector` (string, required): target element.
Selector: `[aria-label="Generate Audio Overview"]` (aria).
Fallback: `text="Audio Overview"` (text).

### type
Enters research prompts, notebook titles, source descriptions.
Params: `selector` (string, required), `text` (string, required).
Selector: `[aria-label="Ask a question"]` (aria).
Fallback: `textarea.prompt-input` (css).

### wait
Polls for Audio Overview completion, source processing, response generation.
Params: `selector` (string, optional), `timeout` (int, optional: 120000).
Wait: `[aria-label="Audio ready"]` or `.audio-player-controls`.
Poll strategy: check every 5000ms until selector appears or timeout.

### extract
Extracts generated text responses, audio URLs, source summaries, citations.
Params: `selector` (string, required), `format` (enum, optional).
Returns: JSON with content, citations array, and audio URL if applicable.

### screenshot
Captures notebook state, generation progress, or error for debugging.
Params: `fullPage` (bool, optional), `path` (string, optional).
Returns: PNG buffer or file path.

## Selectors

Priority order: aria > css > text > data_attr
1. aria (`[aria-label="..."]`): Google products use extensive ARIA labeling.
2. css (`.notebook-card`, `.source-panel`, `.audio-player`): structural containers.
3. text (`text="Add source"`, `text="Generate"`): button and link labels.
4. data_attr (`[data-notebook-id="..."]`): notebook identifiers when available.
Fallback rule: on null, try next priority; after all fail, screenshot + abort.

## Output Format

Primary: json
Schema:
```json
{
  "notebook_id": "string",
  "notebook_name": "string",
  "response_text": "string | null",
  "citations": ["string"],
  "audio_url": "string | null",
  "audio_status": "string",
  "sources_count": "number",
  "error": "string | null"
}
```
