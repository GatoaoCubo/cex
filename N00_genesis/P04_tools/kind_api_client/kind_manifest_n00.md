---
id: n00_api_client_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "API Client -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, api_client, p04, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An api_client is a typed REST, GraphQL, or gRPC API client that gives agents structured access to external services. It encapsulates authentication, request/response schemas, retry logic, and rate limit handling so the agent never makes raw HTTP calls. The output is a production-ready client module with typed method signatures, error handling, and observable logging.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `api_client` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| protocol | string | yes | REST, GraphQL, gRPC, or WebSocket |
| base_url | string | yes | Base URL of the target API |
| auth_scheme | string | yes | none, api_key, oauth2, bearer, basic |
| endpoints | list | yes | List of supported operations with method, path, params |

## When to use
- When an agent needs structured access to an external API (Stripe, GitHub, Slack, etc.)
- When N05 Operations is building tool integrations for the agent toolkit
- When a webhook or notifier needs a typed client for outbound delivery

## Builder
`archetypes/builders/api_client-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind api_client --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: apic_github_rest_v4
kind: api_client
pillar: P04
nucleus: n05
title: "GitHub REST API Client"
version: 1.0
quality: null
---
protocol: REST
base_url: "https://api.github.com"
auth_scheme: bearer
endpoints:
  - name: list_repos
    method: GET
    path: "/user/repos"
  - name: create_pr
    method: POST
    path: "/repos/{owner}/{repo}/pulls"
```

## Related kinds
- `webhook` (P04) -- inbound event handler that complements the outbound api_client
- `toolkit` (P04) -- collection that bundles multiple api_clients for an agent
- `function_def` (P04) -- LLM-callable wrapper that exposes api_client methods as tools
- `sdk_example` (P04) -- example showing canonical api_client usage patterns
