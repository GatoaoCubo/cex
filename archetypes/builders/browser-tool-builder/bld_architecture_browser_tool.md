---
kind: architecture
id: bld_architecture_browser_tool
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of browser_tool — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| engine | Browser automation runtime (Playwright, Puppeteer, Selenium, browser_use, Browserbase, Stagehand) | browser_tool | required |
| action | Named browser operation (navigate, click, type, scroll, wait, screenshot, extract, evaluate, hover, select) | browser_tool | required |
| selector | Element targeting strategy (css, xpath, text, aria, data_attr) with fallback chain | browser_tool | required |
| output_format | Shape of returned data (json, html, screenshot, text) | browser_tool | required |
| headless_config | Headless mode flag, viewport dimensions, timeout, javascript flag | browser_tool | required |
| stealth | Anti-detection measures: user_agent override, navigator.webdriver spoofing, request throttling | browser_tool | optional |
| cookies | Session persistence across actions within one tool invocation | browser_tool | optional |
| proxy | Network routing configuration for geo-restricted or rate-limited sites | browser_tool | optional |
| guardrail | Execution constraints — timeouts, URL allow-list, rate caps | P11 | external |
| agent | Runtime caller that invokes the tool via browser-use or orchestrator | P02 | consumer |
| workflow | Pipeline caller that chains browser_tools in multi-step sequences | P12 | consumer |
## Dependency Graph
```
engine          --produces--> action
headless_config --produces--> action
stealth         --produces--> action
cookies         --produces--> action
proxy           --produces--> action
selector        --depends-->  action
action          --produces--> output_format
guardrail       --depends-->  action
agent           --depends-->  action
workflow        --depends-->  action
```
| From | To | Type | Data |
|------|----|------|------|
| engine | action | produces | browser context, page object |
| headless_config | action | produces | viewport, timeout, javascript flag |
| stealth | action | produces | fingerprint evasion, user-agent header |
| cookies | action | produces | authenticated session state |
| proxy | action | produces | routed network requests |
| selector | action | depends | element targeting strategy and fallback chain |
| action | output_format | produces | extracted data, DOM snapshot, screenshot, text |
| guardrail | action | depends | timeout and URL constraint policy |
| agent | action | depends | LLM-driven or script invocation |
| workflow | action | depends | pipeline-orchestrated invocation |
## Boundary Table
| browser_tool IS | browser_tool IS NOT |
|-----------------|---------------------|
| Operates via DOM API — reads and mutates the document object model | computer_use: controls raw pixels on any screen surface |
| Targets specific web pages via URL navigation | search_tool: queries a search API without page navigation |
| Uses structured selectors (CSS, XPath, ARIA, data attrs) | vision_tool: analyzes image pixels without DOM access |
| Returns structured data, DOM snapshots, or screenshots | cli_tool: runs a command-line utility in a terminal |
| Bound to a declared browser engine | agent: autonomous decision-maker that may USE browser_tools |
| Stateless by default (cookies: false) | connector: bidirectional stateful API integration |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| configuration | engine, headless_config, proxy, stealth, cookies | Define browser runtime environment and session |
| interface | action, selector | Define the automation surface — what callers can trigger |
| execution | output_format | Shape result — how extracted data is returned |
| governance | guardrail | Apply timeouts, URL restrictions, and rate limits |
| callers | agent, workflow | Runtime consumers that invoke browser actions |
