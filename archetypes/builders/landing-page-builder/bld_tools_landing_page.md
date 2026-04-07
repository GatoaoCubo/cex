---
id: bld_tools_landing_page
kind: tools
pillar: P04
builder: landing-page-builder
version: 1.0.0
---
# Tools: Landing Page Builder

## Required Tools
- `brand_config_reader`: Read design tokens from .cex/brand/brand_config.yaml
- `cex_query.py`: Find tagline-builder output, pricing data, brand artifacts
- `cex_retriever.py`: Search existing page templates and design patterns

## Construction Tools (available in stack)
- `browser_playwright`: Preview generated page, take screenshots, test responsive
- `browser_design_extractor`: Extract design tokens from reference URLs
- `computer_use`: Visual validation of rendered page (optional)

## Reference Tools
- `browser_web_scraping`: Analyze competitor landing pages for inspiration
- `browser_awesome_list`: Find design resources, icon sets, font pairings

## No Build Dependencies for HTML Output
Default HTML+Tailwind CDN output requires ZERO build tools. User saves file and deploys.
React/Next.js outputs require user's existing project setup.

## Tool Permissions
- READ: brand config, existing artifacts, competitor pages, design resources
- WRITE: output files only (landing page HTML/JSX + compiled YAML)
- EXECUTE: preview tools (browser_playwright, browser_design_extractor)
- DENY: no database writes, no deployment, no external API mutations
