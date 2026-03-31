---
kind: tools
id: bld_tools_browser_tool
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for browser_tool production
---

# Tools: browser-tool-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing browser_tool artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, browser_tool kind |
| CEX Examples | P04_tools/examples/ | Real browser_tool artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_browser_tool |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Engine Reference
| Engine | Language | Headless | JS | Use Case |
|--------|----------|----------|----|----------|
| playwright | Python/JS/TS | yes | yes | Default: cross-browser, modern sites |
| puppeteer | Node.js | yes | yes | Chrome/Chromium-specific automation |
| selenium | Python/Java/JS | yes | yes | Legacy/enterprise, cross-browser grid |
| browser_use | Python | yes | yes | LLM-driven autonomous navigation |
| browserbase | Python/JS | yes (cloud) | yes | Scalable cloud headless sessions |
| stagehand | TypeScript | yes | yes | AI-assisted, natural language actions |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, actions list matches body,
body <= 2048 bytes, quality == null, engine is recognized, selectors have fallback chain.
