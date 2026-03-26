---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for plugin production
sources: CEX taxonomy, plugin architecture patterns, modular design, extension systems
---

# Domain Knowledge: plugin

## Foundational Concept
A plugin is a modular extension artifact that adds capabilities to a host system through a
defined interface contract. Unlike hooks (single-event) or skills (multi-phase workflows),
plugins provide a complete API surface with lifecycle management, configuration, dependency
resolution, and isolation. The CEX plugin (P04) defines interface contracts, API methods,
config schemas, and lifecycle hooks that enable extensibility without modifying core code.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| VS Code extensions | Extension API + activation events | interface + lifecycle pattern |
| WordPress plugins | Hook system + admin config | api_surface + config_schema |
| Webpack plugins | Compiler hooks + tap pattern | lifecycle + on_load/on_unload |
| Kubernetes operators | CRD + controller pattern | interface contract + API surface |
| Grafana plugins | Panel/datasource types + config | isolation + config_schema |
| ESLint plugins | Rule + processor interface | interface contract + API methods |

## Key Patterns
- Interface contract first: define what the plugin MUST implement before writing code
- Lifecycle is mandatory: on_load initializes, on_unload cleans up (resource leak prevention)
- Explicit dependencies: declare all requirements with version constraints
- Isolation levels: sandboxed (no host access), shared (read host), privileged (full access)
- Config over code: behavior changes via config_schema, not code modification
- Hot-reload: on_config_change enables live reconfiguration without restart
- API surface minimalism: expose only intentional methods, hide internals
- Priority ordering: lower priority loads first (infrastructure before features)
- Version constraints: semver ranges prevent incompatible plugin loading
- Testing in isolation: mock host interface for unit tests, real host for integration

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| api_surface_count | Integrity check: frontmatter matches body | No direct equivalent |
| isolation | CEX mandates explicit isolation declaration | Docker --privileged flag |
| lifecycle list | CEX requires explicit lifecycle event support declaration | VS Code activationEvents |
| config_schema | Inline schema definition for plugin configuration | JSON Schema for extension settings |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT plugin |
|------|------------|---------------------|
| hook (P04) | Single-event interception | INTERCEPTS one event, plugin EXTENDS with full API |
| skill (P04) | Multi-phase reusable capability | Has PHASES and workflow, plugin has INTERFACE and API |
| mcp_server (P04) | MCP protocol server | Implements MCP PROTOCOL, plugin implements custom interface |
| daemon (P04) | Persistent background process | RUNS continuously, plugin is LOADED on demand |
| connector (P04) | External service integration | CONNECTS to external service, plugin EXTENDS internal system |
| client (P04) | API consumer | CONSUMES external API, plugin PROVIDES internal API |
| cli_tool (P04) | Command-line tool | USER-INVOKED, plugin is SYSTEM-LOADED |
| scraper (P04) | Web data extractor | COLLECTS from web, plugin EXTENDS internal system |
| component (P04) | Atomic pipeline block | COMPOSABLE in pipeline, plugin is PLUGGABLE in host |

Regra: "como adicionar esta capacidade como extensao plugavel?" -> plugin.

## References
- CEX TAXONOMY_LAYERS.yaml — plugin in runtime layer
- CEX SEED_BANK.yaml — P04_plugin seeds
- Martin Fowler: Plugin Architecture pattern
- VS Code Extension API documentation
