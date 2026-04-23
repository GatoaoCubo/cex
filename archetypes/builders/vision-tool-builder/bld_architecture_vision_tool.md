---
kind: architecture
id: bld_architecture_vision_tool
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of vision_tool — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Vision Tool"
version: "1.0.0"
author: n03_builder
tags: [vision_tool, builder, examples]
tldr: "Golden and anti-examples for vision tool construction, demonstrating ideal structure and common pitfalls."
domain: "vision tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_vision_tool_builder
  - p11_qg_vision_tool
  - p01_kc_vision_tool
  - bld_examples_vision_tool
  - bld_architecture_browser_tool
  - bld_architecture_computer_use
  - vision-tool-builder
  - bld_instruction_vision_tool
  - bld_output_template_vision_tool
  - bld_schema_vision_tool
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| input_type | Visual input format (base64, url, file_path) | vision_tool | required |
| capability | Named analysis operation | vision_tool | required |
| output_format | Result shape (json, text, table) | vision_tool | required |
| provider | Backing vision API or engine | vision_tool | required |
| confidence_threshold | Min confidence to include result | vision_tool | required |
| supported_formats | Accepted image formats (png, jpg) | vision_tool | recommended |
| max_resolution | Max input resolution | vision_tool | recommended |
| batch_support | Multi-image per call | vision_tool | recommended |
| guardrail | Rate caps, payload limits | P11 | external |
| agent | Invokes tool with image input | P02 | consumer |
| parser | Interprets JSON output | P04 | consumer |
## Dependency Graph
```
input_type          --feeds-->      capability
provider            --executes-->   capability
capability          --produces-->   output_format
confidence_threshold --filters-->   output_format
supported_formats   --constrains--> input_type
guardrail           --limits-->     capability
agent               --invokes-->    capability
parser              --consumes-->   output_format
```
| From | To | Type | Data |
|------|----|------|------|
| input_type | capability | feeds | image payload |
| provider | capability | executes | routes to API/engine |
| capability | output_format | produces | structured result |
| confidence_threshold | output_format | filters | drops low confidence |
| supported_formats | input_type | constrains | accepted file types |
| guardrail | capability | limits | rate/payload caps |
| agent | capability | invokes | runtime caller |
| parser | output_format | consumes | downstream consumer |
## Boundary Table
| vision_tool IS | vision_tool IS NOT |
|----------------|-------------------|
| Accepts image as input and returns structured data | A browser automation that reads DOM elements (browser_tool) |
| Processes static visual payload (base64, url, file) | A screen controller that moves cursor or clicks (computer_use) |
| Calls a vision API or local OCR engine | A document loader that ingests files without visual analysis |
| Returns json, text, or table from image content | A web search tool that finds images (search_tool) |
| Spec-only: no implementation code | A streaming video processr (different artifact kind) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| input | input_type, supported_formats, max_resolution | Define what visual data the tool accepts |
| processing | capability, provider, confidence_threshold | Execute analysis and filter results |
| output | output_format | Shape result data for downstream consumers |
| governance | guardrail, batch_support | Constrain execution (rate, payload, volume) |
| callers | agent, parser | Runtime consumers that invoke and interpret the tool |
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Screenshot and click button | vision_tool | computer_use | computer_use=see+act; vision_tool=see only |
| Extract text from web page | vision_tool | browser_tool | browser_tool=DOM; vision_tool=image pixels |
| Analyze video frames | vision_tool | audio_tool | audio_tool=sound; vision_tool=static images |
## Decision Tree
- Analyze image without control? → vision_tool
- See screen and interact? → computer_use
- Extract from DOM? → browser_tool
- Process audio signal? → audio_tool
## Neighbor Comparison
| Dimension | vision_tool | computer_use | Difference |
|---|---|---|---|
| Action | Read-only analysis | Read + act | vision_tool never controls |
| Input | Image file/URL | Live screen | Different input source |
| Output | Structured JSON | Next action | Different output purpose |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_vision_tool_builder]] | upstream | 0.45 |
| [[p11_qg_vision_tool]] | downstream | 0.43 |
| [[p01_kc_vision_tool]] | upstream | 0.42 |
| [[bld_examples_vision_tool]] | upstream | 0.38 |
| [[bld_architecture_browser_tool]] | sibling | 0.36 |
| [[bld_architecture_computer_use]] | sibling | 0.36 |
| [[vision-tool-builder]] | upstream | 0.36 |
| [[bld_instruction_vision_tool]] | upstream | 0.33 |
| [[bld_output_template_vision_tool]] | upstream | 0.33 |
| [[bld_schema_vision_tool]] | upstream | 0.32 |
