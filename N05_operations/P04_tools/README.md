# P04 Tools — N05 Operations

> Gating Wrath · CI/CD tools, deploy scripts, test runners

## Scope in N05
External capabilities operations uses: deploy CLIs, test harnesses,
CI hooks, rollback scripts, monitoring probes, webhook handlers.
Tools here are sharp and opinionated — wrath prefers tools that
fail loudly over tools that degrade silently.

## Kinds that live here
- `cli_tool` — deploy/ops CLI wrappers
- `webhook` — CI/CD notification endpoints
- `mcp_server` — MCP servers for ops (git, docker, k8s)
- `api_client` — clients for CI platforms (GitHub Actions, Vercel)

## Related
- `scripts/` — bare shell scripts (not full tool artifacts)
- `quality/` — gates that invoke these tools
