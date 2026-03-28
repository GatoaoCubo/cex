---
kind: architecture
id: bld_architecture_function_def
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of function_def — inventory, dependencies, and architectural position
---

# Architecture: function_def
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| name | Function identifier — snake_case verb_noun | function_def | required |
| description | LLM-facing purpose statement — when to call | function_def | required |
| parameters | JSON Schema object defining input structure | function_def | required |
| returns | Return type and structure specification | function_def | required |
| provider_compat | Tested provider compatibility list | function_def | recommended |
| strict | Strict schema enforcement flag | function_def | optional |
| examples | Concrete input/output pairs | function_def | recommended |
| error_types | Possible error conditions | function_def | recommended |
| agent | Runtime caller that selects and invokes the function | P02 | consumer |
| mcp_server | Protocol server that exposes the function | P04 | consumer |
## Dependency Graph
```
description  --informs-->  agent (routing decision)
parameters   --constrains--> agent (input construction)
returns      --constrains--> agent (output parsing)
function_def --consumed-by-> mcp_server
function_def --consumed-by-> agent
provider_compat --informs-> deployment (which providers support it)
```
| From | To | Type | Data |
|------|----|------|------|
| description | agent | informs | LLM reads to decide whether to call |
| parameters | agent | constrains | LLM constructs input matching schema |
| returns | agent | constrains | LLM parses output expecting this shape |
| function_def | mcp_server | consumed-by | Server exposes function as a tool |
| provider_compat | deployment | informs | Which providers can use this definition |
## Boundary Table
| function_def IS | function_def IS NOT |
|----------------|-------------------|
| A JSON Schema describing callable function parameters | A protocol server with transport (that is mcp_server) |
| A provider-agnostic interface contract | An HTTP client implementation (that is api_client) |
| Read by LLMs to decide when and how to call | A sandboxed runtime for code execution (that is code_executor) |
| Defines input types, constraints, and return shape | A terminal command with flags (that is cli_tool) |
| Portable across OpenAI, Anthropic, Gemini, Bedrock | A DOM interaction tool (that is browser_tool) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| identity | name, description | Define what the function is and when to call it |
| interface | parameters, returns | Specify input/output contract |
| compatibility | provider_compat, strict | Provider-specific considerations |
| documentation | examples, error_types | Usage guidance and error handling |
| consumers | agent, mcp_server | Runtime callers that use the definition |
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Server exposes tools via protocol | function_def | mcp_server | mcp_server=transport+protocol; function_def=schema only |
| Client calls external API | function_def | api_client | api_client=implementation; function_def=interface contract |
| Agent executes code via tool | function_def | code_executor | code_executor=runtime; function_def=parameter schema |
## Decision Tree
- JSON Schema for LLM tool_use? → function_def
- Protocol server exposing tools? → mcp_server
- HTTP client implementation? → api_client
- Sandboxed code execution? → code_executor
## Neighbor Comparison
| Dimension | function_def | mcp_server | Difference |
|---|---|---|---|
| Scope | Single function schema | Multi-tool server | mcp_server bundles multiple functions |
| Transport | None (pure schema) | stdio/SSE/HTTP | function_def has no runtime |
| Portability | OpenAI/Anthropic/Gemini | MCP protocol only | function_def is provider-agnostic |
