---
kind: architecture
id: bld_architecture_mcp_server
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of mcp_server — inventory, dependencies, and architectural position
---

# Architecture: mcp_server in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, transport, port, etc.) | mcp-server-builder | active |
| transport_config | Transport selection and configuration (stdio, SSE, HTTP) | author | active |
| tools_provided | Tool definitions with JSON-Schema parameters exposed to agents | author | active |
| resources_provided | Resource URI templates with read/subscribe capabilities | author | active |
| auth_strategy | Authentication and authorization mechanism per transport type | author | active |
| error_handling | Error response format and recovery behavior | author | active |
| health_endpoint | Liveness and readiness checks for monitoring | author | active |
## Dependency Graph
```
agent          --consumes-->   mcp_server  --depends-->     transport_layer
boot_config    --configures--> mcp_server  --produces-->    tool_results
mcp_server     --signals-->    health_status
```
| From | To | Type | Data |
|------|----|------|------|
| agent (P02) | mcp_server | consumes | agent invokes tools and reads resources via MCP protocol |
| boot_config (P02) | mcp_server | data_flow | server address, port, and auth config injected at boot |
| mcp_server | tool_results | produces | structured responses from tool invocations |
| mcp_server | transport_layer | dependency | requires stdio pipe, SSE stream, or HTTP endpoint |
| mcp_server | health_status (P12) | signals | periodic health and availability signals |
| spawn_config (P12) | mcp_server | data_flow | MCP profile path used during satellite spawn |
## Boundary Table
| mcp_server IS | mcp_server IS NOT |
|---------------|-------------------|
| A provider exposing tools and resources via MCP protocol | A bidirectional integration adapter (connector P04) |
| Configured with transport, auth, and endpoint details | A background process without protocol interface (daemon P04) |
| Consumed by agents at runtime through standardized calls | A reusable multi-phase capability (skill P04) |
| Defined by tools_provided and resources_provided schemas | An API consumer fetching external data (client P04) |
| Bound to a specific transport type (stdio/SSE/HTTP) | A pluggable extension with lifecycle hooks (plugin P04) |
| Stateless per request — no session memory across calls | A persistent state store or database |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Configuration | frontmatter, boot_config, spawn_config | Server identity, connection params, and launch profile |
| Transport | transport_config, auth_strategy | Protocol selection and authentication mechanism |
| Interface | tools_provided, resources_provided | Define what the server exposes to consuming agents |
| Runtime | error_handling, health_endpoint | Error recovery and availability monitoring |
| Consumers | agent, tool_results | Agents invoke tools and receive structured responses |
