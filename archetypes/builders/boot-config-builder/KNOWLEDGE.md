---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for boot_config production
sources: CEX schema, provider documentation, runtime configuration patterns
---

# Domain Knowledge: boot_config

## Foundational Concept
A boot_config defines how an AI agent initializes on a specific provider runtime.
It captures the provider-specific parameters (model, flags, MCP servers, permissions)
that transform a generic agent definition into an executable instance. Analogous to
Dockerfile CMD/ENTRYPOINT or Kubernetes container spec — the bridge between
"what the agent is" (agent P02) and "how it runs" (spawn_config P12).

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Dockerfile CMD | Container entrypoint and args | flags + model + temperature |
| K8s container spec | Resources, env, command | constraints + tools + permissions |
| VS Code settings.json | Editor-specific config per extension | Provider-specific tool config |
| Claude .mcp.json | MCP server definitions per workspace | mcp_config object |
| Cursor .cursorrules | AI assistant behavior rules | identity + constraints |

## Key Patterns
- Provider isolation: one boot_config per provider — never combine providers
- Identity inheritance: identity block references the canonical agent definition
- Constraints rationalization: every limit has a documented reason (cost, safety, performance)
- Tool scoping: only tools available on the target provider runtime
- Flag minimalism: only flags necessary for correct operation — no defensive extras
- Temperature tuning: provider-specific defaults (creative tasks higher, code tasks lower)
- MCP conditional: mark MCP tools as conditional when not all providers support them

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| identity.satellite | Links boot to satellite grid | No direct equivalent |
| system_prompt_ref | Links to canonical system_prompt artifact | Claude system prompt |
| mcp_config | Structured MCP server references | .mcp.json |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT boot_config |
|------|------------|--------------------------|
| env_config (P09) | Generic environment variables | Platform-level, not provider-specific init |
| spawn_config (P12) | Runtime spawn orchestration | How to spawn satellites, not how agent boots |
| agent (P02) | Agent canonical definition | Who the agent IS, not how it starts |
| model_card (P02) | LLM spec (pricing, context) | Model capabilities, not initialization params |
| system_prompt (P03) | Agent persona and rules | How agent speaks, not how it initializes |

## References
- CEX P02_model/_schema.yaml — canonical boot_config fields
- Claude Code CLI: `claude --help` — flags and configuration
- MCP specification — tool server configuration
