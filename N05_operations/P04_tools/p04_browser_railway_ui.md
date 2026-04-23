---
id: p04_browser_railway_ui
kind: browser_tool
pillar: P04
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "n05_operations"
name: "Railway Dashboard Automator"
engine: playwright
actions: [navigate, click, type, wait, extract, screenshot]
selectors: [css, aria, text, data_attr]
output_format: json
headless: true
viewport: "1280x720"
timeout: 30000
javascript: true
cookies: true
stealth: false
quality: 9.0
tags: [browser_tool, railway, dashboard, playwright, P04, deploy]
tldr: "Playwright automator for Railway dashboard: service creation, env var config, domain assignment, deploy trigger, log tailing"
description: "Automates Railway UI for service lifecycle, environment config, custom domain setup, deploy management, and log access"
credentials:
  source: secret_config
  keys: [RAILWAY_TOKEN]
  injection: env_var
density_score: 0.92
related:
  - p04_browser_playwright
  - KC_N05_RAILWAY_CLI_PATTERNS
  - bld_schema_model_registry
  - n06_schema_brand_config
  - bld_knowledge_card_browser_tool
  - p02_agent_deploy_ops
  - bld_schema_browser_tool
  - p01_kc_railway_cli_patterns
  - bld_schema_tagline
  - bld_schema_experiment_tracker
---

## Overview

Automates Railway dashboard operations via Playwright. Covers service creation,
environment variable configuration, custom domain assignment, deploy triggering,
and log tailing. Used by N05 deploy pipelines when Railway CLI (`railway`) is
unavailable or when UI-only features (log viewer, metrics) are needed.

## Engine

Engine: Playwright (chromium). Headless: true. Viewport: 1280x720.
Timeout: 30000ms per action. JavaScript: enabled (Next.js SPA).
Cookies: true (session persistence for multi-step deploy workflows).
Auth: GitHub OAuth via `railway.com/dashboard` login redirect.

## Actions

### navigate
Opens Railway dashboard or project-specific URL.
Params: `url` (string, required): target path (e.g., `/project/{id}`).
Wait: `networkidle` or selector `.project-canvas`.

### click
Clicks buttons for new service, deploy, domain config, settings tabs.
Params: `selector` (string, required): target element.
Selector: `[aria-label="New Service"]` (aria).
Fallback: `text="New Service"` (text).

### type
Enters env var keys/values, domain names, service names.
Params: `selector` (string, required), `text` (string, required).
Selector: `input[name="key"]`, `input[name="value"]` (css).
Fallback: `[aria-label="Variable name"]` (aria).

### wait
Waits for deploy completion, service provisioning, domain verification.
Params: `selector` (string, optional), `timeout` (int, optional: 60000).
Wait: `.deploy-status-success` or `text="Active"`.

### extract
Extracts deploy status, service URL, build logs, resource usage.
Params: `selector` (string, required), `format` (enum, optional).
Returns: JSON with extracted values.

### screenshot
Captures deploy logs, metrics view, or error state for reporting.
Params: `fullPage` (bool, optional), `path` (string, optional).
Returns: PNG buffer or file path.

## Selectors

Priority order: aria > css > text > data_attr
1. aria (`[aria-label="..."]`): Railway uses ARIA labels on interactive elements.
2. css (`.service-card`, `.deploy-log`): structural selectors for containers.
3. text (`text="Deploy"`, `text="Variables"`): tab and button labels.
4. data_attr (`[data-testid="..."]`): limited use; fallback only.
Fallback rule: on null, try next priority; after all fail, screenshot + abort.

## Output Format

Primary: json
Schema:
```json
{
  "service_id": "string",
  "service_name": "string",
  "deploy_status": "string",
  "service_url": "string | null",
  "domain": "string | null",
  "env_vars_count": "number",
  "error": "string | null"
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_browser_playwright]] | sibling | 0.42 |
| [[KC_N05_RAILWAY_CLI_PATTERNS]] | upstream | 0.31 |
| [[bld_schema_model_registry]] | downstream | 0.31 |
| [[n06_schema_brand_config]] | downstream | 0.30 |
| [[bld_knowledge_card_browser_tool]] | upstream | 0.30 |
| [[p02_agent_deploy_ops]] | upstream | 0.29 |
| [[bld_schema_browser_tool]] | downstream | 0.28 |
| [[p01_kc_railway_cli_patterns]] | upstream | 0.28 |
| [[bld_schema_tagline]] | downstream | 0.27 |
| [[bld_schema_experiment_tracker]] | downstream | 0.27 |
