---
id: p03_ins_toolkit_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: instruction-builder
title: Toolkit Builder Instructions
target: toolkit-builder agent
phases_count: 3
prerequisites:
  - Target agent or nucleus is identified
  - Required operations are known (what the agent needs to do)
  - Risk assessment of operations is available (read vs write vs delete)
  - MCP server availability is confirmed (if MCP tools are included)
validation_method: checklist
domain: toolkit
quality: 9.0
tags: [instruction, toolkit, permissions, P04]
idempotent: true
atomic: true
rollback: "Revert to previous toolkit version — toolkits are versioned permission documents"
dependencies: []
logging: true
tldr: Produce a YAML toolkit bundle with tool definitions, confirmation tiers, and deny lists — under 4096 bytes, least-privilege enforced, no tool implementation code included.
density_score: 0.86
llm_function: REASON
related:
  - bld_knowledge_card_toolkit
  - p03_sp_toolkit_builder
  - bld_collaboration_toolkit
  - toolkit-builder
  - bld_config_toolkit
  - bld_schema_toolkit
  - bld_tools_toolkit
  - bld_architecture_toolkit
  - bld_memory_toolkit
  - p01_kc_toolkit
---
## Context
The toolkit-builder produces `toolkit` artifacts — YAML bundles defining which tools an agent
or nucleus can access and under what permission constraints. A toolkit answers exactly: what
tools are available, what confirmation level each requires, and which agents are denied specific
tools. Toolkits are consumed by the agent runtime and skill loader; they are not tool
implementations, agent identities, or workflow definitions.
**Input contract**:
- `{{name}}`: toolkit name (e.g. `file_ops`, `git_ops`, `research_tools`)
- `{{target_agent}}`: agent or nucleus that will use this toolkit
- `{{operations}}`: list of operations the agent needs to perform
- `{{risk_profile}}`: read/write/delete classification per operation
- `{{mcp_endpoints}}`: optional MCP server mappings for tool execution
**Output contract**: A single `toolkit` YAML file named `p04_tk_{{name}}.yaml`,
under 4096 bytes, with tool definitions, confirmation tiers, and deny lists. No tool
implementation code, no agent identity, no workflow logic.
**Boundaries**:
- A toolkit is a permission bundle — one bundle per agent role or domain.
- Tool implementation code belongs in N05 operations.
- Agent identity and persona belong in a system_prompt artifact.
- Routing policy belongs in a dispatch_rule artifact.
- Maximum 15 tools per toolkit — split if more are needed.
## Phases
### Phase 1: Classify
**Primary action**: Confirm this is a tool permission bundle and determine the minimum
required toolkit structure before writing any YAML.
```
INPUT: name, target_agent, operations, risk_profile, mcp_endpoints
1. Confirm this is a permission bundle, not a tool implementation or agent config:
   Is it defining WHICH tools an agent can use?              -> toolkit
   Is it implementing HOW a tool works?                      -> NOT a toolkit
   Is it defining WHO the agent is?                          -> NOT a toolkit
2. Validate toolkit name:
   Must match pattern: ^[a-z][a-z0-9_]+$
   Must be descriptive of the domain: file_ops, git_ops, search, web
   Examples: "file_ops", "git_ops", "research_tools", "build_tools"
3. Classify each operation by risk:
   READ operations (list, search, read, glob, grep)   -> confirmation: auto
   WRITE operations (write, edit, create, append)      -> confirmation: confirm
   DELETE operations (delete, remove, clean, reset)    -> confirmation: confirm
   DANGEROUS operations (force push, drop, format)     -> confirmation: deny (default)
4. Check for overlapping tools:
   Scan existing toolkits for the same tools
   Flag overlaps — each tool should live in exactly one toolkit
   If overlap found: decide which toolkit owns it, deny in the other
5. Map to MCP endpoints (if applicable):
   Match each tool to its MCP server endpoint
   Validate endpoint availability
   Flag tools without MCP backing as "local-only"
OUTPUT: validated_name, risk_classified_ops, overlap_flags, mcp_mappings
```
Verification: `validated_name` matches naming pattern. Each operation has a risk
classification. No unresolved overlaps. MCP endpoints validated if present.
### Phase 2: Compose
**Primary action**: Assemble the YAML toolkit with tool definitions, confirmation
tiers, deny lists, and MCP mapping.
```
INPUT: validated_name, target_agent, risk_classified_ops, overlap_flags, mcp_mappings
1. Set filename: p04_tk_{{name}}.yaml
2. Assemble frontmatter:
   id: p04_tk_{{name}}
   kind: toolkit
   pillar: P04
   name: {{name}}
   category: {{domain_category}}
   quality: null
3. Compose tool definitions (ordered by risk: auto first, confirm second):
   For each tool:
     name: tool identifier (snake_case)
     description: one-line purpose statement
     requires_confirmation: auto | confirm | deny
     mcp_endpoint: MCP server path (if applicable)
     denied_for: list of agents/nuclei denied this tool (if any)
   Rules:
     - Read tools: requires_confirmation = auto
     - Write tools: requires_confirmation = confirm
     - Dangerous tools: requires_confirmation = deny (or omit from toolkit)
     - Maximum 15 tools per toolkit
4. Compose deny list:
   For each denied tool-agent pair:
     tool: tool name
     denied_for: [list of agents/nuclei]
     reason: why denied (one line)
5. Compose category metadata:
   category: domain grouping (file_ops, git_ops, search, web, system)
   scope: nucleus | global | agent-specific
6. Size check:
   Estimate YAML byte count
   If > 4096 bytes: split into sub-toolkits by category
   until each sub-toolkit <= 4096 bytes
OUTPUT: toolkit YAML content (assembled, not yet validated)
```
Verification: all required fields present. Tool count <= 15. Each tool has
confirmation tier. Deny lists are explicit. Size <= 4096 bytes.
### Phase 3: Validate
**Primary action**: Run all quality gates against the assembled YAML and output the
final file only if all HARD gates pass.
```
INPUT: toolkit YAML content
1. HARD quality gates (all must pass):
   HARD_1: id matches pattern ^p04_tk_[a-z][a-z0-9_]+$
   HARD_2: kind == "toolkit"
   HARD_3: name is non-empty string
   HARD_4: tools is non-empty list with >= 1 entry
   HARD_5: each tool has name, description, requires_confirmation
   HARD_6: requires_confirmation is one of: auto, confirm, deny
   HARD_7: no write/delete tool has requires_confirmation = auto
   HARD_8: tool count <= 15
   HARD_9: quality == null
   HARD_10: YAML parses without syntax errors
   HARD_11: total YAML size <= 4096 bytes
   HARD_12: no tool implementation code in the toolkit
2. Scope check:
   Verify toolkit contains NO tool implementation code
   Verify toolkit contains NO agent identity or persona
   Verify toolkit contains NO workflow or routing logic
3. If all HARD gates pass: emit file
   If any HARD gate fails: return to Phase 2 with failure reasons
OUTPUT: validated toolkit YAML file
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_toolkit]] | upstream | 0.67 |
| [[p03_sp_toolkit_builder]] | related | 0.65 |
| [[bld_collaboration_toolkit]] | upstream | 0.64 |
| [[toolkit-builder]] | downstream | 0.61 |
| [[bld_config_toolkit]] | downstream | 0.61 |
| [[bld_schema_toolkit]] | downstream | 0.59 |
| [[bld_tools_toolkit]] | downstream | 0.57 |
| [[bld_architecture_toolkit]] | downstream | 0.57 |
| [[bld_memory_toolkit]] | downstream | 0.56 |
| [[p01_kc_toolkit]] | downstream | 0.55 |
