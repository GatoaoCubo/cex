---
kind: examples
id: bld_examples_toolkit
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of toolkit artifacts
pattern: few-shot learning for permission bundles with confirmation tiers
---

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
