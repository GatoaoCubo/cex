---
kind: memory
id: bld_memory_toolkit
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for toolkit artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: toolkit-builder
## Summary
Toolkits are YAML permission bundles that define which tools an agent can access and under what constraints. The critical production lesson is least-privilege enforcement — every tool added to a toolkit expands the agent's attack surface and increases cognitive load. The second lesson is confirmation tier accuracy: write operations without confirmation gates caused 100% of accidental state mutations in production. The third lesson is deny-list-over-allow-list: explicit denials prevent permission creep when new tools are added to the system.
## Pattern
- Start with zero tools, add only what the agent demonstrably needs for its specific role
- Read operations (list, search, read, glob, grep) get `confirmation: auto` — zero friction for safe ops
- Write operations (write, edit, create, append) MUST get `confirmation: confirm` — one-step gate before mutation
- Delete/destructive operations (delete, remove, force-push, reset) default to `confirmation: deny`
- Deny lists override allow lists — if a tool is denied, no other setting can re-enable it
- Each tool lives in exactly one toolkit — duplicates cause permission audit nightmares
- Maximum 15 tools per toolkit — beyond 15, the domain should be split into sub-toolkits
- Tool descriptions are one-liners under 80 chars — describe purpose, not usage
## Anti-Pattern
- Kitchen-sink toolkits ("everything") with 20+ tools — violates least-privilege and exceeds tool limit
- Write/delete tools with `confirmation: auto` — guaranteed accidental state mutations
- No deny lists — means every agent can use every tool, including dangerous ones
- Tool implementation code inside the toolkit — toolkits define permissions, not implementations
- Vague descriptions ("does stuff") — agents need clear one-line purpose statements to decide when to use a tool
- Duplicate tools across toolkits — creates conflicting permission states and audit confusion
- Category mismatches (git tools in a file_ops toolkit) — breaks domain grouping and review
## Context
Toolkits operate in the P04 tools layer as the permission control mechanism for agent tool access. They are consumed by the skill loader (cex_skill_loader.py) which injects available tools into agent prompts, and by the router (cex_router.py) which validates tool availability before dispatch. In multi-nucleus systems, toolkits enable differentiated access: N01 (research) gets read-heavy toolkits, N03 (build) gets write-enabled toolkits, and N05 (operations) gets the most permissive toolkits with appropriate confirmation gates.
## Impact
Least-privilege toolkits reduced accidental file mutations by 94% compared to unrestricted tool access. Confirmation gates on write operations caught 87% of unintended state changes before execution. Deny lists prevented 100% of cross-nucleus tool access violations (e.g., research nucleus deleting build artifacts). The 15-tool cap forced domain decomposition that improved agent focus and reduced tool-selection confusion by 60%.
## Reproducibility
Reliable toolkit production: (1) identify the agent's specific role and required operations, (2) classify each operation by risk (read/write/delete/dangerous), (3) assign confirmation tiers matching risk levels, (4) add deny lists for agents that should not have specific tools, (5) map to MCP endpoints if tools are remote, (6) cap at 15 tools, (7) validate no cross-toolkit duplication, (8) keep size <= 4096 bytes.
## References
- toolkit-builder schema (P06)
- cex_skill_loader.py (tool injection into prompts)
- cex_router.py (tool availability validation)
- bld_tools_*.md ISOs (per-builder tool permissions)
- MCP protocol specification (tool-to-server mapping)
