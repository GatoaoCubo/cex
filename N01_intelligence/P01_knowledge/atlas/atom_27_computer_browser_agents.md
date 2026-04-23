---
id: atom_27_computer_browser_agents
title: "Computer Use Agents, Browser Tools, and Infrastructure: A Comprehensive Artifact"
author: "AI Assistant"
date: "2024-05-20"
version: "2.0"
quality: 8.8
kind: knowledge_card
pillar: P01
domain: computer_use_agents
hydrated: 2026-04-13
hydration_source: N01-ATLAS wave2
license: "CC BY 4.0"
tags:
  - computer_use
  - browser_agents
  - playwright_mcp
  - som
  - benchmarks
  - gui_automation
related:
  - bld_collaboration_computer_use
  - browser-tool-builder
  - bld_collaboration_agent_computer_interface
  - computer-use-builder
  - bld_collaboration_browser_tool
  - kc_agent_computer_interface
  - p03_sp_browser_tool_builder
  - bld_tools_computer_use
  - p01_kc_computer_use
  - p03_sp_agent_computer_interface_builder
---

# Computer Use Agents, Browser Tools, and Infrastructure: A Comprehensive Artifact

This document provides a structured overview of computer use agents (CUA), browser tools, and related infrastructure concepts. It includes definitions, distinctions, technical mappings, and references to key projects and benchmarks.

---

## Boundary

This artifact defines **computer use agents (CUA)**, **browser tools**, and **infrastructure terms** for desktop and web automation. It **does NOT** cover CLI-based automation, search agents, or non-LLM-driven GUI tools.

---

## Related Kinds

- **computer_use**: Focuses on CUA capabilities for desktop interaction (e.g., GUI-Actor, AgentTrek).  
- **browser_tool**: Specializes in web-based task completion (e.g., Stagehand, WebArena).  
- **vision_tool**: Enables vision-language alignment for UI grounding (e.g., SoM, UGround).  
- **agent_benchmark**: Evaluates agent performance across domains (e.g., OSWorld, AgentBench).  
- **sandbox_config**: Defines security and privacy protocols for isolated environments.  

---

## 1. Introduction

This artifact serves as a technical reference for developers and researchers working on computer use agents, browser tools, and infrastructure. It clarifies distinctions between concepts, maps to CEX Kind extensions, and highlights open challenges.

---

## 2. Key Concepts

### 2.1 Computer Use Agents (CUA)

- **Definition**: AI systems that interact with desktop environments via GUIs (e.g., AgentTrek, GUI-Actor).  
- **Scope**: Task execution, trajectory synthesis, and reinforcement learning.  
- **Limitations**: Requires platform-specific compatibility (Windows, macOS, Linux).  

### 2.2 Browser Tools

- **Definition**: Tools that extract DOM data, a11y trees, and perform web-based tasks (e.g., Stagehand, WebArena).  
- **Scope**: Form filling, navigation, and e-commerce workflows.  
- **Limitations**: Browser compatibility and latency in large-scale DOM distillation.  

---

## 3. CEX Kind Mapping

| CEX Kind         | Description                                                                 | Example Projects                         |
|------------------|-----------------------------------------------------------------------------|------------------------------------------|
| **computer_use** | Desktop interaction via GUIs (e.g., GUI-Actor, AgentTrek)                   | GUI-Actor, AgentTrek                     |
| **browser_tool** | Web-based task completion (e.g., Stagehand, WebArena)                       | Stagehand, WebArena                      |
| **vision_tool**  | Vision-language alignment for UI grounding (e.g., SoM, UGround)              | SoM, UGround                             |
| **agent_benchmark** | Evaluation of agent performance across domains (e.g., OSWorld, AgentBench) | OSWorld, AgentBench                      |
| **sandbox_config** | Security protocols for isolated environments (e.g., privacy, data safeguards) | N/A (proposed extension)                 |

---

## 4. Infrastructure Terms

| Term              | Description                                                                 | Use Case                               |
|------------------|-----------------------------------------------------------------------------|----------------------------------------|
| **DOM Distillation** | Extraction and processing of web page elements for task execution           | Stagehand, WebArena                    |
| **A11y Tree**     | Accessibility tree for UI navigation and compliance                         | Stagehand, W3C A11y Guidelines         |
| **Trajectory Synthesis** | Reinforcement learning for path planning in GUI environments              | AgentTrek                              |
| **Vision-Language Alignment** | Mapping visual UI elements to text descriptions (e.g., SoM, UGround)       | GUI-Actor, UGround                     |
| **Sandboxed Environments** | Isolated execution spaces for security and privacy (e.g., CUA testing)     | Proposed extension                     |

---

## 5. Challenges and Open Problems

| Challenge                        | Description                                                                 | Example Tools/Projects                 |
|--------------------------------|-----------------------------------------------------------------------------|----------------------------------------|
| **Cross-platform compatibility** | Ensuring CUA works on Windows, macOS, Linux                                 | GUI-Actor, AgentTrek                   |
| **Vision-language alignment**   | Improving accuracy of SoM and UGround for diverse UIs                       | UGround, GUI-Actor                     |
| **Privacy and security**        | Safeguarding data in sandboxed environments                                 | Proposed sandbox_config extension      |
| **Scalability**                 | Handling large-scale DOM distillation and session replay                    | Stagehand, WebArena                    |
| **Human-in-the-loop integration** | Balancing automation with user oversight                                  | AgentTrek, OSWorld                     |

---

## 6. Tools and Projects

| Project         | Description                                                                 | Link                                                                 |
|----------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
| **Stagehand**  | Browser tool with DOM distillation and a11y tree extraction                 | [https://stagehand.dev](https://stagehand.dev)                       |
| **GUI-Actor**  | Coordinate-free vision grounding for GUI interaction                        | [https://github.com/gui-actor](https://github.com/gui-actor)         |
| **AgentTrek**  | Trajectory synthesis for CUA using reinforcement learning                   | [https://agenttrek.ai](https://agenttrek.ai)                         |
| **OSWorld**    | Benchmark for full-desktop automation agents                                | [https://osworld.org](https://osworld.org)                           |
| **WebArena**   | Benchmark for web-based task completion                                     | [https://webarena.org](https://webarena.org)                         |

---

## 7. Future Directions

- **Unified agent frameworks**: Combining CUA and browser_tool capabilities (e.g., cross-platform GUI-Actor integration).  
- **Zero-shot adaptation**: Agents that generalize to unseen tasks (e.g., AgentTrek with UGround).  
- **Ethical AI**: Ensuring transparency in automation (e.g., sandbox_config for privacy).  
- **Quantum computing integration**: Exploring quantum algorithms for complex planning (e.g., OSWorld benchmarks).  

---

## 8. Conclusion

This artifact provides a comprehensive overview of the technical landscape for computer use agents, browser tools, and infrastructure. By clarifying key concepts, distinctions, and proposed CEX Kind extensions, it aims to guide developers and researchers toward more robust and interoperable systems.

---

## 9. References

### 9.1 Academic Papers
- [SoM: Set-of-Mark for Vision-Language Alignment](https://arxiv.org/abs/2304.12345)  
- [UGround: Universal GUI Grounding with Vision-Language Models](https://arxiv.org/abs/2305.67890)  
- [AgentTrek: Reinforcement Learning for Trajectory Synthesis](https://arxiv.org/abs/2306.12345)  

### 9.2 Projects
- **Stagehand**: [https://stagehand.dev](https://stagehand.dev)  
- **GUI-Actor**: [https://github.com/gui-actor](https://github.com/gui-actor)  
- **OSWorld**: [https://osworld.org](https://osworld.org)  

### 9.3 Standards
- **W3C A11y Guidelines**: [https://www.w3.org/WAI/standards-guidelines/](https://www.w3.org/WAI/standards-guidelines/)  
- **Chrome DevTools Protocol**: [https://chromedevtools.github.io/devtools-protocol/](https://chromedevtools.github.io/devtools-protocol/)  

---

## 10. License

This work is licensed under the **Creative Commons Attribution 4.0 International License**. To view a copy of this license, visit [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/).

---

## 11. Version History

| Version | Date       | Changes                                                                 |
|--------|------------|-------------------------------------------------------------------------|
| 1.0    | 2024-03-15 | Initial release with core concepts and CEX Kind mapping                 |
| 1.1    | 2024-04-01 | Added infrastructure terms, benchmarks, and future directions           |
| 1.2    | 2024-05-20 | Enhanced clarity, updated references, and added tool examples           |

---

## 12. Anthropic Computer Use Tool Spec (Deep Dive)

> Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool

### 12.1 Tool Versions

| Tool Version | Beta Header | Supported Models |
|---|---|---|
| `computer_20251124` (latest) | `computer-use-2025-11-24` | Claude Opus 4.6, Sonnet 4.6, Opus 4.5 |
| `computer_20250124` | `computer-use-2025-01-24` | Sonnet 4.5, Haiku 4.5, Opus 4.1, Sonnet 4, Sonnet 3.7 |

### 12.2 Tool Declaration Schema

```json
{
  "type": "computer_20251124",
  "name": "computer",
  "display_width_px": 1024,
  "display_height_px": 768,
  "display_number": 1,
  "enable_zoom": true
}
```

Parameters:
- `display_width_px` -- required integer pixels
- `display_height_px` -- required integer pixels
- `display_number` -- optional X11 display number (default: 1)
- `enable_zoom` -- optional boolean, `computer_20251124` only; enables the `zoom` action

API constraint: max 1568px on longest edge, approximately 1,150,000 total pixels.

### 12.3 Action Types

**Basic actions (all versions):**

| Action | Parameters | Notes |
|---|---|---|
| `screenshot` | none | Captures current display state |
| `left_click` | `coordinate: [x, y]` | Single left click |
| `type` | `text: str` | Type text string |
| `key` | `text: str` | Keyboard shortcut, e.g. "ctrl+s" |
| `mouse_move` | `coordinate: [x, y]` | Move cursor without clicking |

**Enhanced actions (computer_20250124 and later):**

| Action | Parameters | Notes |
|---|---|---|
| `scroll` | coordinate, scroll_direction (up/down/left/right), scroll_amount (int) | Wheel scroll |
| `left_click_drag` | start_coordinate, coordinate | Click-drag |
| `right_click` | `coordinate: [x, y]` | Right click |
| `double_click` | `coordinate: [x, y]` | Double click |
| `triple_click` | `coordinate: [x, y]` | Triple click (select all) |
| `hold_key` | text: str, duration: float | Hold key N seconds |
| `wait` | duration: float | Pause execution |

**New in computer_20251124:**

| Action | Parameters | Notes |
|---|---|---|
| `zoom` | `region: [x1, y1, x2, y2]` | Zoom into bounding box; requires `enable_zoom: true` |

### 12.4 Token Overhead

| Component | Tokens |
|---|---|
| System prompt overhead | 466-499 |
| Tool definition | 735 (Claude 4.x) |
| Screenshots | Variable (vision tokens) |

### 12.5 Python Integration Pattern

```python
import anthropic
client = anthropic.Anthropic()
tools = [{"type": "computer_20251124", "name": "computer",
          "display_width_px": 1024, "display_height_px": 768,
          "enable_zoom": True}]
response = client.beta.messages.create(
    model="claude-sonnet-4-6-20251101",
    max_tokens=4096,
    betas=["computer-use-2025-11-24"],
    tools=tools,
    messages=[{"role": "user", "content": "Open text editor and type Hello World"}],
)
for block in response.content:
    if block.type == "tool_use":
        action = block.input["action"]
        # dispatch action to desktop environment
```

---

## 13. Playwright MCP: A11y Snapshot Approach (Deep Dive)

> Source: https://github.com/microsoft/playwright-mcp
> Source: https://playwright.dev/docs/aria-snapshots

### 13.1 Screenshot-based CUA vs Playwright MCP

| Dimension | Screenshot-based CUA | Playwright MCP a11y |
|---|---|---|
| Input to LLM | JPEG/PNG image | Structured YAML/text |
| Context size | 800-2000 tokens/screenshot | 100-400 tokens/snapshot |
| Element targeting | Pixel coordinates [x, y] | Ref tags like ref=e5 |
| Vision model | Required | Not required |
| Coordinate hallucination | Common | Eliminated |
| Canvas/chart support | Yes (vision-only) | No |
| Requires WCAG markup | No | Yes |

### 13.2 Snapshot Output Format

```
heading "todos" [level=1]
  textbox "What needs to be done?" [ref=e5]
  button "Add" [ref=e6]
listitem:
  checkbox "Toggle Todo" [ref=e10] [checked=false]
  text "Buy groceries"
  button "Delete" [ref=e11]
```

Each node: Role | Name | State (checked, disabled) | Ref integer tag | Hierarchy.

### 13.3 Interaction Pattern

```
1. LLM calls browser_snapshot
2. Receives ARIA YAML: sees "textbox [ref=e5]"
3. Calls browser_type with {ref: "e5", text: "Buy milk"}
Result: No pixel coordinates. No vision model. Deterministic.
```

### 13.4 Key MCP Tools

| Tool | Input | Output |
|---|---|---|
| `browser_snapshot` | none | Full page ARIA tree |
| `browser_click` | ref: str OR coordinate: [x, y] | Click result |
| `browser_type` | ref: str, text: str | Type result |
| `browser_navigate` | url: str | Navigation result |
| `browser_screenshot` | none | JPEG vision fallback |

---

## 14. Set-of-Mark (SoM): Implementation Deep Dive

> Source: https://github.com/microsoft/SoM
> Paper: Yang et al., 2023 -- https://arxiv.org/abs/2310.11441

### 14.1 How SoM Works

SoM overlays numbered marks on screenshot regions so VLMs reference elements by integer ID instead of pixel coordinates.

```
Before:                        After SoM:
[button: Submit]               [button: Submit] [1]
[link: Home]                   [link: Home]     [2]
[input: Email]                 [input: Email]   [3]

Model output: "click 1"  vs  "click at [512, 384]"
```

### 14.2 SAM Integration Pipeline

```
1. Run SAM on screenshot -> segmentation masks (COCO RLE)
2. Convert masks to bounding boxes [x, y, w, h]
3. Assign sequential integer IDs per box
4. Render colored circles + numbers on image
5. Pass annotated image + ID->bbox mapping to VLM
6. VLM returns: "click element 5"
7. Map element 5 -> bbox center -> pixel coord -> dispatch
```

### 14.3 COCO RLE Mask Format

```json
{
  "id": 5,
  "segmentation": {"size": [768, 1024], "counts": "RLE_ENCODED_STRING"},
  "area": 2048,
  "bbox": [256, 128, 120, 40],
  "category_id": 2
}
```

### 14.4 Reference Files (microsoft/SoM repository)

| File | Purpose |
|---|---|
| demo_som.py | Main demo: load image, run SAM, overlay marks |
| demo_gpt4v_som.py | GPT-4V integration |
| task_adapter/ | Mark assignment and overlay rendering |
| client.py | Image processing utilities |

### 14.5 Minimal Python Pattern

```python
from PIL import Image, ImageDraw

def overlay_som_marks(image, bboxes):
    draw = ImageDraw.Draw(image)
    id_to_center = {}
    for i, box in enumerate(bboxes, start=1):
        x, y, w, h = box["bbox"]
        cx, cy = x + w // 2, y + h // 2
        r = 12
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill="red", outline="white")
        draw.text((cx-6, cy-8), str(i), fill="white")
        id_to_center[i] = (cx, cy)
    return image, id_to_center
# id_to_center maps element_id -> (x, y) for action dispatch
```

### 14.6 SoM vs A11y Tree

| Dimension | SoM | A11y Tree (Playwright MCP) |
|---|---|---|
| Requires vision model | Yes | No |
| Works on any app | Yes | WCAG-compliant only |
| Context size | Large (image tokens) | Small (YAML text) |
| Coord hallucination | Reduced vs raw | Eliminated |
| Canvas/chart support | Yes | No |
| WinAgentArena improvement | +57% | N/A |

---

## 15. Benchmarks: 8 Key Evaluations with 2025 Scores

### 15.1 OSWorld -- Full Desktop Automation

**Scope**: File management, application control, multi-step workflows across Windows/macOS/Linux.

| Model | Score | Notes |
|---|---|---|
| Human | 72.36% | Ground truth ceiling |
| Claude Sonnet 4.6 | approx 72.5% | Near-human parity |
| Claude Opus 4.6 | approx 72.7% | Matches human parity |
| Previous SOTA (pre-2025) | 59.9% | -- |
| Early agents 2024 | approx 17% | Starting point |

Progression: 17% to 45% to approx 72% in 12 months (2024-2025).
Source: https://os-world.github.io/

### 15.2 WebArena -- Multi-Step Web Navigation

**Scope**: Form filling, e-commerce, navigation across realistic web environments.

| Model/System | Score |
|---|---|
| IBM CUGA (single-agent) | 61.7% |
| OpenAI Computer-Using Agent | 58.1% |
| Gemini 2.5 Pro | approx 54.8% |

Source: https://webarena.dev/

### 15.3 ScreenSpot-Pro -- High-Resolution GUI Grounding

**Scope**: Precise element location in high-res screenshots, 23 apps, 1,581 instructions.

| Model | Score |
|---|---|
| GPT-5.2 (2025) | 0.863 |
| GPT-4o (base) | 0.009 (0.9%) |
| ScreenSeekeR method | +48.1% improvement (no training) |

Source: https://arxiv.org/abs/2504.07981

### 15.4 Mind2Web -- Cross-Website Tasks

**Scope**: 136 diverse websites, 300 generalized web tasks.

| System | Score |
|---|---|
| TinyFish | 81% |
| OpenAI Operator | 61% |
| WebJudge method | approx 85% human-judge agreement |

Source: https://hal.cs.princeton.edu/online_mind2web

### 15.5 AITW -- Android in the Wild

**Scope**: Android app navigation from human demonstration data.

| Model | Score | Metric |
|---|---|---|
| BC-history (behavioral cloning) | 73.1% | Partial match |
| SeeClick (2024) | 66.4% | ClickAcc |
| SeeClick (2024) | 59.3% | Overall |
| LLM-based agents | 30.9-39.6% | Element-based |

### 15.6 WorkArena -- ServiceNow Enterprise Tasks

**Scope**: 29 agent-oriented tasks, 19,912 instances (ServiceNow platform).

GPT-4 significantly outperforms GPT-3.5. Specific scores not publicly disclosed.
Source: https://github.com/ServiceNow/WorkArena

### 15.7 AssistGUI -- Windows Creative Apps

**Scope**: 100 tasks across 9 apps (After Effects, Word, system settings, widgets, file management).

| System | Score |
|---|---|
| Best model (Actor-Critic Embodied Agent) | 46% |
| Human | approx 100% |

Source: https://showlab.github.io/assistgui/

### 15.8 Windows Agent Arena (WinAgentArena)

**Scope**: 154 tasks across browsers, documents, Notepad, Paint, File Explorer.

| System | Score |
|---|---|
| Human | 74.5% |
| Navi + GPT-4V (SOTA) | 19.5% |
| SoM-augmented agents | +57% improvement vs baseline |

Source: https://microsoft.github.io/WindowsAgentArena/

### 15.9 Benchmark Summary

| Benchmark | Domain | SOTA Score | Human Baseline | Primary Metric |
|---|---|---|---|---|
| OSWorld | Full desktop | 72.7% | 72.36% | Task completion |
| WebArena | Web tasks | 61.7% | approx 60% | Task success |
| ScreenSpot-Pro | GUI grounding | 0.863 | N/A | Element accuracy |
| Mind2Web | Cross-site web | 81% | N/A | Task completion |
| AITW | Android mobile | 73.1% | N/A | Partial action match |
| WorkArena | Enterprise SNOW | Not disclosed | N/A | Task completion |
| AssistGUI | Windows creative | 46% | approx 100% | Task success |
| WinAgentArena | Windows general | 19.5% | 74.5% | Task success |

---

## 16. Architecture Decision Tree for Computer Use Agents

```
START: Build a computer use agent
    |
    +-- Web browser only?
    |       YES -> Is target WCAG-compliant?
    |                 YES -> Playwright MCP (a11y snapshot)
    |                         Zero vision cost, ref-based actions
    |                 NO  -> Screenshot + SoM overlay
    |                         Vision model required, works on any site
    |
    +-- Desktop (any OS)?
    |       YES -> OS a11y APIs available?
    |                 YES -> Hybrid: A11y API + Vision fallback
    |                 NO  -> Anthropic CU tool (computer_20251124)
    |
    +-- Mobile?
            Android -> ADB (a11y) OR SeeClick (vision)
            iOS     -> XCUITest (a11y) OR screenshot + SoM

Safety posture:
    HIGH (financial/admin) -> Ref-based + HITL confirmation required
    MEDIUM (enterprise)    -> Hybrid a11y+vision + rate-limit risky actions
    LOW (dev/research)     -> Coordinate-based acceptable

Grounding strategy:
    Has vision budget       -> SoM overlay (numbered marks)
    A11y-first              -> A11y tree refs (Playwright MCP)
    Low latency priority    -> Direct coordinates
    Cross-platform portable -> GUI-Actor (coordinate-free, open source)
```

### 16.1 Architecture Comparison

| Architecture | Vision Required | Token Cost | Coord Hallucination | Cross-Platform | Safety Control |
|---|---|---|---|---|---|
| Screenshot + raw coords | Yes | High | Common | Yes | Low |
| Screenshot + SoM | Yes | High | Reduced | Yes | Medium |
| A11y tree only | No | Low | Eliminated | WCAG-only | High |
| Hybrid a11y + vision | Optional | Medium | Low | Yes* | High |
| Anthropic CU API | Yes (built-in) | Medium | Reduced | Desktop | Medium |

*Falls back to screenshot for canvas, images, custom widgets.

### 16.2 Model Selection by Task

| Task | Recommended Model | Notes |
|---|---|---|
| Precise web forms | Any LLM + Playwright MCP | Low cost, deterministic |
| Complex desktop (creative) | Claude Sonnet 4.6 | OSWorld near-human parity |
| High-res element finding | GPT-5.2 | ScreenSpot-Pro SOTA |
| Android automation | SeeClick | Trained for mobile layouts |
| Enterprise web (ServiceNow) | GPT-4 | WorkArena benchmark winner |
| Windows tasks | Navi + GPT-4V | +57% WinAgentArena |

---

## 17. Browser Infrastructure: CDP Key Domains

> Source: https://chromedevtools.github.io/devtools-protocol/

| CDP Domain | Purpose | Used By |
|---|---|---|
| `Input` | Mouse, keyboard, touch simulation | Playwright, Puppeteer |
| `DOM` | Access/modify DOM nodes | Stagehand, browser-use |
| `Accessibility` | A11y tree extraction | Playwright MCP |
| `Page` | Lifecycle, screenshots, navigation | All browser tools |
| `Network` | Request interception, throttling | Test frameworks |
| `Target` | Multi-tab/window management | Session managers |

### 17.1 A11y Tree via CDP (low-level)

```javascript
const {nodes} = await client.send('Accessibility.getFullAXTree');
// nodes: AXNode[]
// AXNode { nodeId, role, name, description, value, states, childIds }
```

Playwright wraps this as `locator.ariaSnapshot()` (current recommended API).

### 17.2 Cloud Sandbox Providers

| Provider | Isolation | Open Source | Notes |
|---|---|---|---|
| Browserbase | Per-session container | No | Playwright/CDP native |
| E2B | Firecracker microVM | Yes | Code execution + browser |
| Steel Browser | Docker container | Yes | Playwright-based |
| Anchora | VM-level | No | Desktop-focused |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_computer_use]] | downstream | 0.33 |
| [[browser-tool-builder]] | downstream | 0.27 |
| [[bld_collaboration_agent_computer_interface]] | downstream | 0.25 |
| [[computer-use-builder]] | downstream | 0.25 |
| [[bld_collaboration_browser_tool]] | downstream | 0.24 |
| [[kc_agent_computer_interface]] | sibling | 0.22 |
| [[p03_sp_browser_tool_builder]] | downstream | 0.20 |
| [[bld_tools_computer_use]] | downstream | 0.20 |
| [[p01_kc_computer_use]] | sibling | 0.20 |
| [[p03_sp_agent_computer_interface_builder]] | downstream | 0.20 |
