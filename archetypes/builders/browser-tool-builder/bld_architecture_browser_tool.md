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
| engine | Automation runtime (Playwright, Puppeteer, etc.) | browser_tool | required |
| action | Browser op (navigate, click, type, screenshot) | browser_tool | required |
| selector | Targeting (css, xpath, text, aria) + fallback | browser_tool | required |
| output_format | Result shape (json, html, screenshot, text) | browser_tool | required |
| headless_config | Headless, viewport, timeout, JS flag | browser_tool | required |
| stealth | Anti-detection measures | browser_tool | optional |
| cookies | Session persistence | browser_tool | optional |
| proxy | Network routing config | browser_tool | optional |
| guardrail | Timeouts, URL allow-list | P11 | external |
| agent | Runtime caller | P02 | consumer |
| workflow | Pipeline caller | P12 | consumer |
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
| engine | action | produces | browser context |
| headless_config | action | produces | viewport, timeout |
| stealth | action | produces | fingerprint evasion |
| cookies | action | produces | session state |
| proxy | action | produces | routed requests |
| selector | action | depends | targeting+fallback |
| action | output_format | produces | data/DOM/screenshot |
| guardrail | action | depends | timeout+URL policy |
| agent/workflow | action | depends | runtime callers |
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
| configuration | engine, headless_config, proxy, stealth, cookies | Browser runtime |
| interface | action, selector | Automation surface |
| execution | output_format | Result shape |
| governance | guardrail | Timeouts, URL restrictions |
| callers | agent, workflow | Runtime consumers |
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Click button on screen | browser_tool | computer_use | computer_use=pixels; browser_tool=DOM selectors |
| Search web for data | browser_tool | search_tool | search_tool=API query; browser_tool=navigate+scrape |
| Extract text from image | browser_tool | vision_tool | vision_tool=pixel analysis; browser_tool=DOM text |
## Decision Tree
- DOM-level web automation? → browser_tool
- Pixel-level GUI control? → computer_use
- Web search API? → search_tool
- Image analysis? → vision_tool
## Neighbor Comparison
| Dim | browser_tool | computer_use | Diff |
|---|---|---|---|
| Target | DOM elements | Screen pixels | Different abstraction |
| Scope | Web pages only | Any GUI | browser_tool is web-specific |
| Output | Structured JSON/HTML | Screenshots | browser_tool has richer data |
