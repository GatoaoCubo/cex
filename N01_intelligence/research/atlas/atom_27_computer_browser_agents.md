---
id: n01_atom_27_computer_browser_agents
kind: knowledge_card
type: research_atom
pillar: P01
title: "Computer Use & Browser Agents -- Complete Vocabulary Atlas"
version: 1.0.0
created: 2026-04-13
updated: 2026-04-13
author: n01_intelligence
domain: computer_use_browser_agents
quality: 8.8
tags: [computer-use, browser-agent, gui-grounding, web-agent, benchmark, osworld, webarena, stagehand, playwright-mcp, set-of-mark, a11y-tree, dom-distillation]
tldr: "Exhaustive vocabulary extraction across computer use APIs (Anthropic, OpenAI CUA), browser agent SDKs (Stagehand, browser-use, Playwright MCP), visual grounding techniques (SoM, GUI-Actor, UGround), and agent benchmarks (OSWorld, WebArena, VisualWebArena, BrowserGym)"
when_to_use: "Building browser_tool or computer_use artifacts, designing vision_tool pipelines, evaluating agent performance on web/desktop tasks, selecting GUI grounding strategy"
keywords: [computer-use, browser-agent, cua, stagehand, browserbase, playwright-mcp, set-of-mark, osworld, webarena, browsergym, gui-grounding, a11y-tree, dom-distillation, action-space, observation-space]
density_score: null
---

# Computer Use & Browser Agents -- Complete Vocabulary Atlas

> **Scope**: Every technical term from Anthropic Computer Use, OpenAI CUA/Operator, Browserbase/Stagehand, browser-use, Playwright MCP, Microsoft SoM, GUI-Actor, and the OSWorld/WebArena/BrowserGym benchmark ecosystem.
> **Date**: April 2026 (reflects APIs and benchmarks current as of this date)

---

## 1. Foundational Concepts

### 1.1 Computer Use vs. Browser Agents

| Concept | Definition | Scope |
|---------|-----------|-------|
| **Computer use** | LLM-driven control of a full desktop environment via screenshot observation + mouse/keyboard actions | OS-level: any app, not just browsers |
| **Browser agent** | LLM-driven automation scoped to web browsers, using DOM/a11y tree or screenshots | Web-only: navigates pages, fills forms, extracts data |
| **GUI agent** | Umbrella term for any agent that interacts with graphical user interfaces | Superset of both computer use and browser agents |
| **Web agent** | Synonym for browser agent in academic literature | Used in benchmarks (WebArena, WebVoyager) |
| **Desktop agent** | Agent operating on full desktop OS (windows, menus, file system) | OSWorld scope |

### 1.2 Core Loop

Every computer/browser agent follows this cycle:

```
OBSERVE --> REASON --> ACT --> EVALUATE
   |                              |
   +--------- feedback -----------+
```

| Phase | Computer Use | Browser Agent |
|-------|-------------|---------------|
| **Observe** | Screenshot capture | DOM snapshot, a11y tree, screenshot, or hybrid |
| **Reason** | Vision model analyzes pixels, plans next action | LLM processes structured page representation |
| **Act** | Mouse/keyboard commands on desktop | Click, type, scroll, navigate on page |
| **Evaluate** | Next screenshot confirms result | Page state change confirms success |

---

## 2. Anthropic Computer Use

### 2.1 Tool Versions

| Tool Type | Version | Models | Key Addition |
|-----------|---------|--------|-------------|
| `computer_20250124` | Jan 2025 | Sonnet 3.7, Sonnet 4, Opus 4 | scroll, hold_key, triple_click, fine-grained mouse |
| `computer_20251124` | Nov 2025 | Opus 4.5, Sonnet 4.6, Opus 4.6 | zoom action (region inspection at full resolution) |
| `text_editor_20250124` | Jan 2025 | All above | str_replace_based_edit_tool |
| `text_editor_20250728` | Jul 2025 | Opus 4.5+ | Updated text editor |
| `bash_20250124` | Jan 2025 | All above | Shell command execution |

### 2.2 Action Space (Complete)

**Basic actions (all versions):**

| Action | Parameters | Description |
|--------|-----------|-------------|
| `screenshot` | (none) | Capture current display state |
| `left_click` | `coordinate: [x, y]`, optional `text` (modifier key) | Click at pixel coordinates |
| `type` | `text: string` | Type text string at cursor |
| `key` | `key: string` | Press key combo (e.g. "ctrl+s") |
| `mouse_move` | `coordinate: [x, y]` | Move cursor to position |

**Enhanced actions (computer_20250124+):**

| Action | Parameters | Description |
|--------|-----------|-------------|
| `scroll` | `coordinate`, `scroll_direction` (up/down/left/right), `scroll_amount`, optional `text` | Directional scroll with amount control |
| `left_click_drag` | `start_coordinate`, `coordinate` | Click and drag between points |
| `right_click` | `coordinate` | Right-click at position |
| `middle_click` | `coordinate` | Middle-click at position |
| `double_click` | `coordinate` | Double-click at position |
| `triple_click` | `coordinate` | Triple-click (select line/paragraph) |
| `left_mouse_down` | `coordinate` | Press and hold left button |
| `left_mouse_up` | `coordinate` | Release left button |
| `hold_key` | `key`, `duration` (seconds) | Hold key for duration |
| `wait` | `duration` | Pause between actions |

**Enhanced actions (computer_20251124+):**

| Action | Parameters | Description |
|--------|-----------|-------------|
| `zoom` | `region: [x1, y1, x2, y2]` | View screen region at full resolution (requires `enable_zoom: true`) |

**Modifier keys on click/scroll:** Pass modifier name via `text` parameter: `shift`, `ctrl`, `alt`, `super`.

### 2.3 Observation Space

| Term | Definition |
|------|-----------|
| **Screenshot** | Base64-encoded PNG/JPEG of current display state |
| **Display dimensions** | `display_width_px`, `display_height_px` -- configured at tool registration |
| **Display number** | X11 display ID for multi-display setups |
| **Coordinate space** | Pixel grid from (0,0) at top-left to (width-1, height-1) at bottom-right |
| **Coordinate scaling** | API resizes images to max 1568px long edge / ~1.15MP; coordinates returned in resized space must be scaled back to original |
| **Scale factor** | `min(1.0, 1568/long_edge, sqrt(1150000/total_pixels))` |
| **XGA resolution** | 1024x768 -- recommended for optimal model accuracy |

### 2.4 Environment Architecture

| Component | Description |
|-----------|-------------|
| **Virtual display** | Xvfb (X Virtual Framebuffer) renders headless desktop |
| **Desktop environment** | Lightweight Linux UI: Mutter (window manager) + Tint2 (panel) |
| **Docker container** | Sandboxed environment with Firefox, LibreOffice, file manager |
| **Agent loop** | Iterative cycle: send action -> execute in environment -> return screenshot -> repeat |
| **Tool result** | JSON with `tool_use_id`, `content` (screenshot or error), `is_error` flag |
| **Prompt injection classifier** | Auto-runs on screenshots; steers model to ask confirmation on suspicious content |

### 2.5 Safety & Isolation

| Term | Definition |
|------|-----------|
| **Desktop sandbox** | Isolated VM/container with minimal privileges |
| **Domain allowlist** | Restrict internet access to approved domains |
| **Human-in-the-loop** | Confirm before financial transactions, account creation, ToS acceptance |
| **Prompt injection** | Instructions embedded in screenshots/webpages that override user instructions |
| **Zero Data Retention (ZDR)** | Screenshots not retained after API response |

---

## 3. OpenAI CUA (Computer-Using Agent)

### 3.1 Core Architecture

| Term | Definition |
|------|-----------|
| **CUA (Computer-Using Agent)** | Model combining GPT-4o vision with reinforcement learning for GUI interaction |
| **Operator** | Consumer product powered by CUA; originally standalone, now integrated into ChatGPT as "agent mode" (Jul 2025) |
| **Agent mode** | ChatGPT dropdown option that activates CUA for autonomous web tasks |
| **Iterative loop** | Screenshot capture -> chain-of-thought reasoning -> action execution -> repeat |

### 3.2 Action Space

| Action | Description |
|--------|-------------|
| **click** | Click at screen coordinates |
| **type** | Enter text |
| **scroll** | Scroll page content |
| **key** | Press keyboard shortcut |
| **screenshot** | Capture current state |

### 3.3 Benchmark Performance

| Benchmark | CUA Score | Notes |
|-----------|-----------|-------|
| OSWorld | 38.1% | Full desktop tasks (human: 72.4%) |
| WebArena | 58.1% | Web navigation tasks |
| WebVoyager | 87% | Web task completion |

---

## 4. Google Project Mariner

| Term | Definition |
|------|-----------|
| **Project Mariner** | Google DeepMind browser agent, operates as Chrome extension |
| **Visual understanding** | Reads screen content including images, code, forms |
| **Task planning** | Decomposes goals into actionable steps |
| **Workflow learning** | Remembers workflows; replays with minimal prompting |
| **Multi-task juggling** | Handles concurrent tasks in same session |
| **Availability** | Google AI Ultra plan ($249.99/mo), US-first; Gemini API + Vertex AI integration (I/O 2025) |

---

## 5. Browserbase / Stagehand

### 5.1 Stagehand Primitives

| Primitive | Signature | Description |
|-----------|-----------|-------------|
| **act()** | `act("click the login button")` | Execute single action via natural language instruction |
| **extract()** | `extract("the price", { schema })` | Extract structured data from page using Zod schema |
| **observe()** | `observe("clickable buttons")` | Preview available actions without executing; returns candidate list |
| **agent()** | `agent("book a flight to NYC")` | Multi-step autonomous workflow executor |

### 5.2 Infrastructure Terms

| Term | Definition |
|------|-----------|
| **Browserbase** | Cloud headless browser platform; gives Stagehand production infrastructure |
| **Browser session** | Isolated browser instance with its own state, cookies, storage |
| **Agent Identity** | Browserbase feature that gives agents realistic browser fingerprints to avoid bot detection |
| **Action caching** | Store successful action sequences; skip LLM inference on repeat runs |
| **Self-healing** | Detect website changes (layout shifts, selector breaks) and re-engage AI |
| **Session replay** | CDP-based screencast recording of browser session (not DOM replay) |
| **Prompt observability** | Inspect what prompts Stagehand sends to the LLM during automation |
| **Captcha solving** | Built-in captcha bypass in Browserbase cloud |
| **CDP Engine** | Low-level Chrome DevTools Protocol interface for direct browser control |

### 5.3 Modes

| Mode | Description |
|------|-------------|
| **DOM mode** | Stagehand reads accessibility tree / DOM structure for element targeting |
| **Vision mode** | Stagehand uses screenshot analysis for visual element identification |
| **Hybrid** | Combine DOM + vision for robustness |

---

## 6. browser-use (Python)

| Term | Definition |
|------|-----------|
| **browser-use** | Open-source Python library (79k+ GitHub stars) for AI browser automation |
| **LLM Integration Layer** | Connects to OpenAI, Anthropic, Google, or local Ollama models |
| **Playwright backend** | Uses Playwright for actual browser control |
| **Dynamic feedback loop** | Observe page -> decide action -> handle failures -> adjust |
| **HTML structure extraction** | Parse page HTML for element identification |
| **Visual understanding** | Screenshot analysis for visual context |
| **Form filling** | Automated form interaction pipeline |
| **Login workflows** | Handle authentication flows |

---

## 7. Playwright MCP

### 7.1 Architecture

| Term | Definition |
|------|-----------|
| **Playwright MCP** | Model Context Protocol server exposing Playwright browser automation to LLMs (Microsoft, Mar 2025) |
| **Accessibility snapshot** | Structured text-based page representation from browser a11y tree; each element gets unique ref (`@e1`, `@e2`) |
| **Element ref** | Unique identifier (e.g. `@e15`) assigned to each interactive element in snapshot |

### 7.2 Tool Categories

| Category | Scope |
|----------|-------|
| **core** | Navigation, click, type, select, check -- via element refs |
| **pdf** | PDF generation and manipulation |
| **vision** | Coordinate-based interactions using screenshots |
| **devtools** | Developer tools features (console, network) |

### 7.3 Key Advantage

Playwright MCP uses the accessibility tree rather than screenshots for fast, deterministic control. No vision model required for basic interactions. Each element has a stable ref for unambiguous targeting.

---

## 8. Visual Grounding Techniques

### 8.1 Set-of-Mark (SoM) -- Microsoft

| Term | Definition |
|------|-----------|
| **Set-of-Mark (SoM)** | Visual prompting method: overlay numbered/labeled marks on UI elements in screenshot |
| **Interactive segmentation** | Use SAM/SEEM to partition image into regions at multiple granularity levels |
| **Mark types** | Alphanumerics, masks, bounding boxes overlaid on segmented regions |
| **Region index** | Numeric/alphabetic label on each marked region; model references by index |
| **Interleaved prompt** | Prompt mixing text instructions with visual references to marked regions |
| **Zero-shot grounding** | SoM + GPT-4V outperforms fine-tuned models on RefCOCOg without training |

### 8.2 GUI-Actor -- Microsoft (2025)

| Term | Definition |
|------|-----------|
| **GUI-Actor** | Coordinate-free visual grounding for GUI agents |
| **Dense spatial supervision** | Train on bounding boxes covering entire target regions, not just center points |
| **Spatial extent** | Full area of actionable element, not a single pixel |

### 8.3 UGround -- OSU NLP (ICLR 2025)

| Term | Definition |
|------|-----------|
| **UGround** | Universal visual grounding model for GUI agents |
| **Cross-platform grounding** | Works across web, desktop, and mobile GUIs |

### 8.4 Grounding Vocabulary (General)

| Term | Definition |
|------|-----------|
| **GUI grounding** | Identifying the correct pixel coordinate(s) to execute an action |
| **Visual grounding** | Mapping natural language references to visual regions in an image |
| **Screenshot grounding** | Using screenshot pixels as the sole observation for action targeting |
| **Pixel grounding** | Predicting exact (x,y) coordinates from visual input |
| **Bounding box prediction** | Predicting `[x_min, y_min, x_max, y_max]` for target element |
| **Granularity mismatch** | Vision Transformers operate at patch level; actions require pixel-level precision |
| **Coordinate-based interaction** | Actions specified by pixel coordinates (click at 500,300) |
| **Ref-based interaction** | Actions specified by element reference ID (click @e15) |
| **Cursor trajectory** | Sequence of (x,y) positions over time representing mouse movement path |

---

## 9. Observation Space -- Methods

### 9.1 Screenshot-Based (Vision)

| Term | Definition |
|------|-----------|
| **Raw screenshot** | Unprocessed pixel capture of screen/viewport |
| **Annotated screenshot** | Screenshot with SoM marks, bounding boxes, or element labels overlaid |
| **Resolution scaling** | Resize screenshots to fit model input constraints (Anthropic: 1568px max edge) |
| **Viewport screenshot** | Capture only visible browser viewport, not full page |
| **Full-page screenshot** | Stitch together entire scrollable page |

### 9.2 DOM-Based (Structured)

| Term | Definition |
|------|-----------|
| **DOM snapshot** | Full Document Object Model tree captured via CDP `DOMSnapshot.captureSnapshot` |
| **DOM distillation** | Strip raw HTML to essential interactive elements; remove noise (styles, scripts, hidden elements) |
| **Enriched DOM** | DOM nodes annotated with `bid` (browser ID), `coords`, `visible`, `clickable` attributes |
| **HTML structure extraction** | Parse HTML to identify form fields, links, buttons, headings |

### 9.3 Accessibility Tree (A11y)

| Term | Definition |
|------|-----------|
| **Accessibility tree (a11y tree)** | Browser-generated semantic tree: element roles, names, states, relationships |
| **AXTree** | Chrome's implementation of the accessibility tree (obtained via CDP) |
| **Element ref** | Unique identifier assigned to each a11y node (e.g. `@e1`, `@e2`) |
| **Structured accessibility snapshot** | Compact text representation: role + name + ref for each element |
| **A11y tree parsing** | Extract actionable elements from accessibility tree for agent consumption |
| **Role** | Semantic type: button, textbox, link, heading, combobox, checkbox, etc. |
| **Name** | Accessible label (from aria-label, text content, or alt text) |
| **State** | Current status: checked, expanded, selected, disabled, focused |

### 9.4 Hybrid Observation

| Term | Definition |
|------|-----------|
| **Multi-modal observation** | Combine screenshot + DOM + a11y tree in single observation |
| **Text DOM + visual** | Agent receives both structured text and rendered pixels |
| **Observation fusion** | Merge multiple observation modalities for robust understanding |

---

## 10. Action Space -- Unified Taxonomy

### 10.1 Navigation

| Action | Description |
|--------|-------------|
| **goto / navigate** | Load URL in browser |
| **go_back** | Browser back button |
| **go_forward** | Browser forward button |
| **refresh** | Reload current page |
| **new_tab** | Open new browser tab |
| **close_tab** | Close current tab |
| **switch_tab** | Switch to tab by index |

### 10.2 Mouse/Pointer

| Action | Description |
|--------|-------------|
| **click / left_click** | Single left click at coordinates or element ref |
| **right_click** | Context menu click |
| **double_click** | Double-click |
| **triple_click** | Select word/line/paragraph |
| **middle_click** | Middle button (often opens link in new tab) |
| **drag / click_drag** | Click-hold and move to destination |
| **mouse_move / hover** | Move cursor without clicking |
| **mouse_down / mouse_up** | Fine-grained press/release control |

### 10.3 Keyboard

| Action | Description |
|--------|-------------|
| **type / fill** | Enter text string |
| **key / press** | Press key or combo (Enter, Tab, Ctrl+A) |
| **hold_key** | Hold key for specified duration |

### 10.4 Scroll

| Action | Description |
|--------|-------------|
| **scroll** | Scroll in direction (up/down/left/right) by amount |
| **scroll_to_element** | Scroll until element is in viewport |

### 10.5 Observation

| Action | Description |
|--------|-------------|
| **screenshot** | Capture screen/viewport image |
| **snapshot** | Get structured a11y tree or DOM representation |
| **zoom** | Inspect subregion at full resolution (Anthropic) |
| **observe** | Preview available actions without executing (Stagehand) |

### 10.6 Data Extraction

| Action | Description |
|--------|-------------|
| **extract** | Pull structured data from page (Stagehand) |
| **get_text** | Get text content of element |
| **get_attribute** | Get element attribute value |

### 10.7 Form Interaction

| Action | Description |
|--------|-------------|
| **select_option** | Choose from dropdown/select element |
| **check / uncheck** | Toggle checkbox state |
| **upload_file** | Attach file to input |

---

## 11. Benchmarks

### 11.1 OSWorld

| Field | Value |
|-------|-------|
| **Full name** | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments |
| **Scope** | Full desktop OS (Ubuntu, Windows, macOS) |
| **Tasks** | 369 computer tasks across real web + desktop apps |
| **Task types** | OS file I/O, multi-app workflows, web tasks, office apps |
| **Evaluation** | Functional correctness (execution-based, not trajectory) |
| **Human baseline** | 72.4% |
| **Best agent (2025)** | CUA 38.1% |
| **Environment** | Real VMs with actual installed software |
| **URL** | https://os-world.github.io/ |

### 11.2 WebArena

| Field | Value |
|-------|-------|
| **Full name** | WebArena: A Realistic Web Environment for Building Autonomous Agents |
| **Scope** | Web browser tasks on self-hosted realistic websites |
| **Tasks** | 812 tasks from 241 templates |
| **Domains** | E-commerce (shopping), forums (Reddit), project management (GitLab), content editing (CMS), maps |
| **Evaluation** | Functional correctness against expected outcomes |
| **Best single-agent (2025)** | ~61.7% |
| **Key feature** | Self-hosted copies of real websites with injected data |
| **URL** | https://webarena.dev/ |

### 11.3 VisualWebArena

| Field | Value |
|-------|-------|
| **Full name** | VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks |
| **Scope** | Web tasks requiring visual understanding (image-text) |
| **Tasks** | 910 tasks across Classifieds, Shopping, Reddit |
| **Key difference** | Tasks require processing images embedded in web pages |
| **Multimodal** | Agents must interpret both text and visual content |
| **URL** | https://jykoh.com/vwa |

### 11.4 BrowserGym

| Field | Value |
|-------|-------|
| **Full name** | BrowserGym: A Gym Environment for Web Task Automation |
| **Scope** | Unified framework aggregating multiple web benchmarks |
| **Includes** | WebArena, VisualWebArena, WorkArena, WorkArena++, MiniWoB++ |
| **Observation space** | DOM snapshots, a11y trees (AXTree), viewport screenshots |
| **Action space** | Python code or high-level primitives (bid-based + coord-based) |
| **Developer** | ServiceNow Research |
| **URL** | https://github.com/ServiceNow/BrowserGym |

### 11.5 WorkArena

| Field | Value |
|-------|-------|
| **Tasks** | 33 tasks (base) / 682 tasks (WorkArena++) |
| **Platform** | ServiceNow enterprise platform |
| **Task types** | Knowledge work: form filling, list filtering, service catalog, dashboards |
| **Key feature** | Realistic enterprise SaaS environment |

### 11.6 MiniWoB++

| Field | Value |
|-------|-------|
| **Full name** | Mini World of Bits++ |
| **Tasks** | 100+ tasks on synthetic web pages |
| **Scope** | Simple web interactions (click button, fill form, navigate menu) |
| **Purpose** | Unit-test level evaluation; building block for complex benchmarks |

### 11.7 WebVoyager

| Field | Value |
|-------|-------|
| **Tasks** | 643 tasks across 15 real websites |
| **Websites** | Google, GitHub, Wikipedia, Booking.com, Amazon, Apple, etc. |
| **Task types** | Form submission, multi-page navigation, search, dropdown, date selection |
| **Best agent (2025)** | ~88% (CUA) |
| **Key method** | Three-phase: planner -> actor -> validator |

### 11.8 ST-WebAgentBench

| Field | Value |
|-------|-------|
| **Focus** | Safety and trustworthiness in web agents |
| **Evaluates** | Agent behavior under adversarial or ambiguous conditions |

---

## 12. Notable Browser Agent Frameworks

| Framework | Type | Key Innovation | Observation | Stars (Apr 2026) |
|-----------|------|---------------|-------------|-------------------|
| **Stagehand** | SDK (TS/Python) | act/extract/observe/agent primitives | DOM + vision | ~12k |
| **browser-use** | Python library | LLM + Playwright feedback loop | HTML + screenshot | ~79k |
| **Playwright MCP** | MCP server | A11y tree with element refs | A11y snapshot | ~14k |
| **Agent-E** | Multi-agent | DOM distillation + skill harvesting | Text-only DOM | N/A |
| **WebVoyager** | Research agent | SoM + 3-phase (plan/act/validate) | Screenshot + SoM | N/A |
| **SeeAct** | Research baseline | Simple vision-based web agent | Screenshot | N/A |
| **Project Mariner** | Product (Google) | Chrome extension + workflow learning | Visual + forms | N/A |
| **OpenAI CUA/Operator** | Product (OpenAI) | GPT-4o vision + RL | Screenshot | N/A |
| **AgentTrek** | Data synthesis | Generate trajectories from web tutorials | Replay-based | N/A |

---

## 13. Infrastructure & Environment Terms

| Term | Definition |
|------|-----------|
| **Desktop sandbox** | Isolated VM/container for safe agent execution (Docker, Firecracker, microVM) |
| **Headless browser** | Browser without visible UI; runs in background for automation |
| **Browser session** | Isolated browser context with own cookies, storage, history |
| **Session replay** | Recording of browser session for debugging/review (CDP screencast or DOM-based) |
| **CDP (Chrome DevTools Protocol)** | Low-level protocol for browser instrumentation (screenshot, DOM, network, console) |
| **Virtual display** | Xvfb or similar; renders desktop without physical monitor |
| **Ephemeral sandbox** | Short-lived VM/container destroyed after task completion |
| **Agent Identity / browser fingerprint** | Realistic browser fingerprint to avoid bot detection |
| **Captcha solving** | Automated bypass of CAPTCHA challenges |
| **Proxy rotation** | Cycle IP addresses to avoid rate limiting |
| **Human-in-the-loop (HITL)** | Require human confirmation for high-risk actions |
| **Cursor trajectory** | Path of mouse movements over time; used in trajectory analysis and training data |
| **AgentTrek trajectory synthesis** | Generate training trajectories by replaying web tutorials with VLM agent |

---

## 14. CEX Kind Mapping

### 14.1 Existing Kinds

| CEX Kind | Pillar | Boundary | Coverage |
|----------|--------|----------|----------|
| `computer_use` | P04 | GUI automation (screen, keyboard, mouse) -- NOT browser_tool, NOT cli_tool | Anthropic CU, OpenAI CUA, OSWorld agents |
| `browser_tool` | P04 | Web page interaction via DOM -- NOT computer_use, NOT search_tool | Stagehand, browser-use, Playwright MCP, WebArena agents |
| `vision_tool` | P04 | Visual analysis, OCR, screenshot interpretation -- NOT browser_tool, NOT computer_use | SoM overlay, GUI grounding, screenshot analysis |

### 14.2 Proposed New Kinds

| Proposed Kind | Pillar | Description | Boundary | Rationale |
|--------------|--------|-------------|----------|-----------|
| `gui_grounding_config` | P04 | Configuration for visual grounding strategy (SoM, coordinate, ref-based, bounding box) | Grounding strategy config. NOT vision_tool (runtime analysis) nor browser_tool (page interaction). | SoM, GUI-Actor, UGround each need different overlay/ref configs. No existing kind covers grounding strategy selection. |
| `agent_benchmark` | P07 | Benchmark definition for evaluating agent performance (tasks, metrics, environment spec) | Benchmark definition. NOT scoring_rubric (per-artifact quality) nor quality_gate (pass/fail threshold). | OSWorld, WebArena, BrowserGym etc. need a structured definition kind. Current P07 has scoring_rubric and benchmark but benchmark is underspecified for agent evaluation suites. |
| `session_recording` | P10 | Session replay configuration: what to capture, storage, playback format | Recording config. NOT trace_config (LLM call traces) nor entity_memory (remembered facts). | Browserbase, AgentTrek, and debug workflows need session capture specs. No existing kind covers browser/desktop session recording. |
| `sandbox_config` | P09 | Desktop/browser sandbox environment specification (VM type, isolation, display, pre-installed apps) | Environment isolation config. NOT env_config (runtime variables) nor boot_config (agent startup). | Docker containers, Firecracker microVMs, cloud sandboxes each need environment specs. env_config is too generic. |
| `dom_distillation_config` | P04 | DOM processing pipeline config: what to strip, what to enrich, output format (raw/distilled/a11y) | DOM processing config. NOT browser_tool (page interaction) nor parser (generic output parsing). | Agent-E, Playwright MCP, BrowserGym each use different DOM distillation strategies. Needs dedicated config kind. |

### 14.3 Kind Relationship Graph

```
                    gui_grounding_config
                          |
                    [grounding strategy]
                          |
        +---------+-------+-------+---------+
        |         |               |         |
  computer_use  browser_tool  vision_tool   |
   (P04)         (P04)        (P04)        |
     |             |             |          |
     |     dom_distillation_config         |
     |          (P04)                      |
     |                                     |
  sandbox_config              session_recording
     (P09)                       (P10)
                                   |
                            agent_benchmark
                               (P07)
```

---

## 15. Key Distinctions (Disambiguation)

| Pair | Difference |
|------|-----------|
| **computer_use vs. browser_tool** | computer_use controls full desktop (any app); browser_tool is scoped to web pages |
| **DOM observation vs. vision observation** | DOM uses structured text (a11y tree, HTML); vision uses screenshot pixels |
| **coordinate-based vs. ref-based actions** | Coordinates target pixels (click 500,300); refs target semantic elements (click @e15) |
| **SoM vs. a11y tree** | SoM overlays marks on screenshots for vision models; a11y tree is structured text for language models |
| **action caching vs. skill harvesting** | Action caching stores exact replay sequences; skill harvesting extracts reusable patterns |
| **session replay vs. trajectory** | Session replay is video/screencast for debugging; trajectory is structured action sequence for training |
| **agent loop vs. feedback loop** | Agent loop is the API-level observe-act cycle; feedback loop includes self-correction and retry |
| **OSWorld vs. WebArena** | OSWorld tests full desktop OS tasks; WebArena tests web-only browser tasks |
| **BrowserGym vs. WebArena** | BrowserGym is the unified framework/environment; WebArena is one benchmark within it |
| **Stagehand vs. browser-use** | Stagehand is TypeScript-first with 4 primitives; browser-use is Python-first with LLM feedback loop |

---

## 16. Sources

- [Anthropic Computer Use Tool Documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)
- [OpenAI Computer-Using Agent](https://openai.com/index/computer-using-agent/)
- [OpenAI Introducing Operator](https://openai.com/index/introducing-operator/)
- [Browserbase Stagehand](https://www.browserbase.com/stagehand)
- [Stagehand GitHub](https://github.com/browserbase/stagehand)
- [browser-use GitHub](https://github.com/browser-use/browser-use)
- [Playwright MCP GitHub](https://github.com/microsoft/playwright-mcp)
- [Microsoft Set-of-Mark (SoM)](https://github.com/microsoft/SoM) -- arXiv 2310.11441
- [GUI-Actor: Coordinate-Free Visual Grounding](https://microsoft.github.io/GUI-Actor/)
- [UGround: Universal GUI Visual Grounding](https://github.com/OSU-NLP-Group/UGround) -- ICLR 2025 Oral
- [OSWorld Benchmark](https://os-world.github.io/)
- [WebArena Benchmark](https://webarena.dev/)
- [VisualWebArena](https://jykoh.com/vwa)
- [BrowserGym GitHub](https://github.com/ServiceNow/BrowserGym)
- [WorkArena Benchmark](https://servicenow.github.io/WorkArena/)
- [Google Project Mariner](https://deepmind.google/models/project-mariner/)
- [AgentTrek: Trajectory Synthesis](https://openreview.net/forum?id=EEgYUccwsV) -- ICLR 2025
- [Anthropic vs OpenAI CUA Comparison (WorkOS)](https://workos.com/blog/anthropics-computer-use-versus-openais-computer-using-agent-cua)
- [Chrome DevTools Protocol DOMSnapshot](https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot/)
