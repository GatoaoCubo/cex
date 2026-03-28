---
kind: architecture
id: bld_architecture_vision_tool
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of vision_tool — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| input_type | Accepted visual input format (base64, url, file_path, buffer, screenshot) | vision_tool | required |
| capability | Named visual analysis operation the tool performs | vision_tool | required |
| output_format | Shape of result data (json, text, table) | vision_tool | required |
| provider | Backing vision API or local engine | vision_tool | required |
| confidence_threshold | Minimum confidence score to include a result | vision_tool | required |
| supported_formats | Accepted image file format list (png, jpg, etc.) | vision_tool | recommended |
| max_resolution | Maximum input resolution constraint | vision_tool | recommended |
| batch_support | Whether multiple images can be processed per call | vision_tool | recommended |
| guardrail | Execution constraints — rate caps, payload limits | P11 | external |
| agent | Runtime caller that invokes the tool with image input | P02 | consumer |
| parser | Downstream consumer that interprets the tool's JSON output | P04 | consumer |
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
| input_type | capability | feeds | raw image payload for analysis |
| provider | capability | executes | routes image to API or local engine |
| capability | output_format | produces | structured result (json/text/table) |
| confidence_threshold | output_format | filters | drops results below minimum confidence |
| supported_formats | input_type | constrains | restricts accepted file types |
| guardrail | capability | limits | rate caps, max payload bytes |
| agent | capability | invokes | calls tool with image input at runtime |
| parser | output_format | consumes | downstream structure interpretation |
## Boundary Table
| vision_tool IS | vision_tool IS NOT |
|----------------|-------------------|
| Accepts image as input and returns structured data | A browser automation that reads DOM elements (browser_tool) |
| Processes static visual payload (base64, url, file) | A screen controller that moves cursor or clicks (computer_use) |
| Calls a vision API or local OCR engine | A document loader that ingests files without visual analysis |
| Returns json, text, or table from image content | A web search tool that finds images (search_tool) |
| Spec-only: no implementation code | A streaming video processor (different artifact kind) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| input | input_type, supported_formats, max_resolution | Define what visual data the tool accepts |
| processing | capability, provider, confidence_threshold | Execute analysis and filter results |
| output | output_format | Shape result data for downstream consumers |
| governance | guardrail, batch_support | Constrain execution (rate, payload, volume) |
| callers | agent, parser | Runtime consumers that invoke and interpret the tool |
