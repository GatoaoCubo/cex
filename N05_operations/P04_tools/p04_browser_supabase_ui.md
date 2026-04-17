---
id: p04_browser_supabase_ui
kind: browser_tool
pillar: P04
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "n05_operations"
name: "Supabase Dashboard Automator"
engine: playwright
actions: [navigate, click, type, wait, extract, screenshot]
selectors: [css, aria, data_attr, text]
output_format: json
headless: true
viewport: "1280x720"
timeout: 30000
javascript: true
cookies: true
stealth: false
quality: 9.0
tags: [browser_tool, supabase, dashboard, playwright, P04, devops]
tldr: "Playwright automator for Supabase dashboard: project CRUD, env vars, schema setup, RLS policies, edge functions deploy"
description: "Automates Supabase Studio UI for project lifecycle, database config, RLS policy management, and edge function deployment"
credentials:
  source: secret_config
  keys: [SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY]
  injection: env_var
density_score: 0.91
---

## Overview

Automates Supabase Studio dashboard operations via Playwright. Covers the full project
lifecycle: creation, environment variable injection, schema setup via SQL editor,
RLS policy configuration, and edge function deployment. Triggered by N05 deploy
pipelines or N03 scaffold workflows when Supabase CLI is unavailable.

## Engine

Engine: Playwright (chromium). Headless: true. Viewport: 1280x720.
Timeout: 30000ms per action. JavaScript: enabled (React SPA requires it).
Cookies: true (session persistence across multi-step workflows).
Auth: GitHub OAuth or email/password via `/dashboard/sign-in`.

## Actions

### navigate
Opens Supabase dashboard URL. Waits for `networkidle`.
Params: `url` (string, required): target dashboard path.
Wait: `networkidle` or selector `[data-testid="project-list"]`.

### click
Clicks UI elements for project selection, tab navigation, policy toggles.
Params: `selector` (string, required): target element.
Selector: `[data-testid="project-{slug}"]` (data_attr).
Fallback: `text="{project_name}"` (text).

### type
Enters text into SQL editor, env var fields, function code editor.
Params: `selector` (string, required), `text` (string, required).
Selector: `.monaco-editor textarea` (css) for SQL editor.
Fallback: `[aria-label="SQL Editor"]` (aria).

### wait
Waits for async operations: project provisioning, migration runs, deploy.
Params: `selector` (string, optional), `timeout` (int, optional).
Wait: `[data-testid="project-status-active"]` or `.toast-success`.

### extract
Extracts project metadata, connection strings, deploy status.
Params: `selector` (string, required), `format` (enum, optional).
Returns: JSON with extracted field values.

### screenshot
Captures viewport for verification or error reporting.
Params: `fullPage` (bool, optional), `path` (string, optional).
Returns: PNG buffer or file path.

## Selectors

Priority order: data_attr > aria > css > text
1. data_attr (`[data-testid="..."]`): Supabase uses data-testid extensively; most stable.
2. aria (`[aria-label="..."]`): accessible labels on buttons and inputs.
3. css (`.project-card`, `.sql-editor`): structural fallback for unlabeled elements.
4. text (`text="Run query"`): last resort for dynamic or unlabeled controls.
Fallback rule: on null result, try next priority strategy; after all fail, screenshot + abort.

## Output Format

Primary: json
Schema:
```json
{
  "project_id": "string",
  "project_name": "string",
  "status": "string",
  "connection_string": "string | null",
  "rls_policies": "number",
  "edge_functions": "number",
  "error": "string | null"
}
```
