---
kind: quality_gate
id: p11_qg_toolkit
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of toolkit artifacts
pattern: few-shot learning for permission bundles with confirmation tiers
quality: 9.0
title: 'Gate: Toolkit'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: Gates ensuring toolkits enforce least-privilege with correct confirmation tiers,
  deny lists override allow lists, tool count stays under 15, and no implementation
  code leaks into the permission bundle.
domain: toolkit
created: '2026-04-06'
updated: '2026-04-06'
density_score: 0.85
related:
  - bld_knowledge_card_toolkit
  - p03_ins_toolkit_builder
  - p03_sp_toolkit_builder
  - bld_schema_toolkit
  - bld_memory_toolkit
  - bld_examples_toolkit
  - toolkit-builder
  - bld_config_toolkit
  - bld_collaboration_toolkit
  - bld_output_template_toolkit
---

## Quality Gate

## Definition
A toolkit is a permission bundle defining which tools an agent can access and under what constraints. It passes this gate when every write tool requires confirmation, deny lists are explicit with reasons, the tool count stays under 15, no tool implementation code is present, and the least-privilege principle is demonstrably applied.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches pattern `p04_tk_{name}` | Mismatched IDs cause routing failures |
| H03 | `kind` is exactly `toolkit` (literal match) | Kind drives the loader; wrong literal silently misroutes |
| H04 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H05 | `name` field is non-empty snake_case string | Invalid names break lookup and indexing |
| H06 | `tools` is a non-empty list with 1-15 entries | Empty toolkits are useless; >15 indicates domain split needed |
| H07 | Each tool has `name`, `description`, and `confirmation` fields | Missing fields break runtime tool resolution |
| H08 | `confirmation` values are one of: auto, confirm, deny | Unknown tiers cause undefined runtime behavior |
| H09 | No write/delete tool has `confirmation: auto` | Write operations without confirmation are security violations |
| H10 | Total YAML size <= 4096 bytes | Oversized toolkits exceed token budget |
| H11 | No tool implementation code (functions, classes, scripts) in the toolkit | Toolkits define permissions, not implementations |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every line carries information |
| 2 | Least-privilege compliance (only tools the agent demonstrably needs) | 1.5 | Kitchen sink — every tool included | Most tools justified | Every tool has clear usage justification |
| 3 | Confirmation tier accuracy (tiers match risk: reads=auto, writes=confirm, dangerous=deny) | 1.5 | All tools on auto | Most tiers correct | Every tier accurately reflects operation risk |
| 4 | Deny lists are explicit with reasons (not just names) | 1.0 | No deny lists | Deny lists without reasons | Every denial has an evidence-based reason |
| 5 | Tool descriptions are precise (one-line purpose, not usage instructions) | 1.0 | Descriptions are paragraphs | Most are concise | Every description is under 80 chars and actionable |
| 6 | No cross-toolkit tool duplication | 0.5 | Many duplicates across toolkits | One or two overlaps | Zero duplicates; each tool in exactly one toolkit |
| 7 | MCP endpoints mapped where applicable | 0.5 | No MCP mapping despite remote tools | Some tools mapped | All remote tools have valid MCP endpoints |
| 8 | Category matches toolkit domain (file_ops toolkit has file tools) | 0.5 | Category mismatches tool domain | Category broadly correct | Category precisely matches all tool domains |

## Examples

# Examples: toolkit-builder
## Golden Example
INPUT: "Create a file operations toolkit for N03 build nucleus"
OUTPUT (`p04_tk_file_ops.yaml`):
```yaml
name: file_ops
category: file_ops
requires_confirmation: true
scope: nucleus
target_agent: n03
tools:
  - name: read_file
    description: Read file contents by absolute path
    confirmation: auto
    risk_level: read
  - name: glob_search
    description: Find files matching glob pattern in directory tree
    confirmation: auto
    risk_level: read
  - name: grep_search
    description: Search file contents with regex patterns
    confirmation: auto
    risk_level: read
  - name: write_file
    description: Create or overwrite file at specified path
    confirmation: confirm
    risk_level: write
  - name: edit_file
    description: Replace exact string in existing file
    confirmation: confirm
    risk_level: write
  - name: delete_file
    description: Permanently remove file from disk
    confirmation: deny
    denied_for: [n01, n02, n04, n06]
    risk_level: delete
```
WHY THIS IS GOLDEN:
- filename follows `p04_tk_{name}.yaml`
- read tools are `auto`, write tools are `confirm`, delete is `deny`
- least-privilege: only 6 tools, all demonstrably needed for file operations
- `denied_for` on delete restricts non-build nuclei
- descriptions are concise one-liners under 80 chars
- no implementation code, no agent identity, no workflow logic
## Golden MCP-Mapped Example
OUTPUT (`p04_tk_git_ops.yaml`):
```yaml
name: git_ops
category: git_ops
requires_confirmation: true
scope: nucleus
target_agent: n05
mcp_server: github-mcp
tools:
  - name: git_status
    description: Show working tree status and staged changes
    confirmation: auto
    mcp_endpoint: /repos/status
  - name: git_diff
    description: Show unstaged and staged diffs
    confirmation: auto
    mcp_endpoint: /repos/diff
  - name: git_log
    description: List recent commit messages and hashes
    confirmation: auto
    mcp_endpoint: /repos/log
  - name: git_add
    description: Stage specific files for commit
    confirmation: confirm
    mcp_endpoint: /repos/stage
  - name: git_commit
    description: Create commit with message from staged changes
    confirmation: confirm
    mcp_endpoint: /repos/commit
  - name: git_push
    description: Push commits to remote branch
    confirmation: confirm
    risk_level: write
    mcp_endpoint: /repos/push
  - name: git_force_push
    description: Force push to remote (destructive)
    confirmation: deny
    denied_for: [n01, n02, n03, n04, n06]
    risk_level: dangerous
```
WHY THIS PASSES:
- MCP endpoints mapped for all tools
- force_push correctly denied for all non-ops nuclei
- confirmation tiers match risk accurately
- tool count is 7, well within the 15-tool limit
## Anti-Example
BAD OUTPUT (`p04_tk_everything.yaml`):
```yaml
name: everything
category: general
requires_confirmation: false
tools:
  - name: read_file
    description: Reads a file
    confirmation: auto
  - name: write_file
    description: Writes a file
    confirmation: auto
  - name: delete_file
    description: Deletes a file
    confirmation: auto
  - name: execute_code
    description: Runs arbitrary code on the system
    confirmation: auto
  # ... 20 more tools
```
FAILURES:
1. name "everything" violates least-privilege — not domain-scoped
2. category "general" is not in the allowed enum
3. `requires_confirmation: false` when write/delete tools exist — security violation
4. write_file and delete_file have `confirmation: auto` — HARD gate H09 failure
5. execute_code with `confirmation: auto` — dangerous operation without restriction
6. 20+ tools exceeds 15-tool limit — HARD gate H06 failure
7. no `denied_for` on destructive tools
8. descriptions are vague ("Reads a file") — no actionable context
## Anti-Example: Implementation Drift
BAD OUTPUT (`p04_tk_search.yaml`):
```yaml
name: search_tools
tools:
  - name: semantic_search
    description: Search using embeddings
    confirmation: auto
    implementation: |
      def semantic_search(query, index):
          embeddings = model.encode(query)
          results = index.search(embeddings, k=10)
          return results
```
FAILURES:
1. contains implementation code — toolkits define permissions, not implementations
2. no `category` field — required top-level field missing
3. no `requires_confirmation` — required top-level field missing
4. implementation code belongs in N05 operations, not in a toolkit

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
