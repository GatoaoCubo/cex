---
kind: knowledge_card
id: bld_knowledge_card_boot_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for boot_config production — agent initialization per provider
sources: Claude Code CLI, Cursor rules, Codex runtime, Kubernetes container spec patterns
---

# Domain Knowledge: boot_config
## Executive Summary
Boot configs define how an agent initializes on a specific provider runtime (Claude Code, Cursor, Codex). They bridge "what the agent is" (identity) with "how it runs" (constraints, flags, MCP servers, permissions). Analogous to Dockerfile CMD/ENTRYPOINT or Kubernetes container spec. One agent may have multiple boot configs — one per target provider.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (identity/model) |
| Frontmatter fields | 15 required + 7 recommended |
| Quality gates | 9 HARD + 10 SOFT |
| Key sections | identity_block, constraints, tools, permissions, mcp_config |
| Constraint types | max_tokens, context_window, timeout_ms, max_retries |
| Providers | claude, cursor, codex, openai-assistants |
## Patterns
- **Provider isolation**: one boot_config per provider — never combine multiple providers in a single config
- **Identity inheritance**: identity block references the canonical agent definition, not duplicates it
- **Constraint rationalization**: every limit documents WHY it is set — "timeout: 120s because P95 task < 90s"
- **Tool scoping**: only tools available on the target provider runtime — over-listing causes boot errors
- **Flag minimalism**: only flags necessary for correct operation — no defensive extras
| Source | Concept | Application |
|--------|---------|-------------|
| Dockerfile CMD | Container entrypoint and args | flags + model + temperature |
| K8s container spec | Resources, env, command | constraints + tools + permissions |
| Claude .mcp.json | MCP server definitions | mcp_config object |
| Cursor .cursorrules | AI assistant behavior rules | identity + constraints |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Provider-agnostic config | Runtimes have different capabilities; one-size breaks |
| Hardcoded absolute paths | Not portable across machines or environments |
| Missing timeout | Agent hangs indefinitely on slow provider |
| Over-permissioned tools | Security risk; agent accesses tools it never uses |
| No MCP specification | Agent boots without required integrations |
| Unrationalized constraints | Arbitrary limits nobody understands or maintains |
## Application
1. Identify target provider and its runtime capabilities
2. Define identity block: name, role, domain (reference canonical agent)
3. Set constraints with rationale: tokens, context window, timeout, retries
4. Configure MCP servers: which ones, permissions, load order
5. Map CLI flags: translate constraints to provider-specific syntax
6. Validate: config boots on target provider without errors
## References
- Claude Code: CLI flags and configuration (`claude --help`)
- Cursor: .cursorrules and AI configuration patterns
- MCP specification: Model Context Protocol server configuration
- Kubernetes: container spec and resource limits patterns
