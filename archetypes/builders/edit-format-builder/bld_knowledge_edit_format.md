---
kind: knowledge_card
id: bld_knowledge_card_edit_format
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for edit_format production
quality: 9.2
title: "Knowledge Card Edit Format"
version: "1.1.0"
author: n04_hybrid_review2
tags: [edit_format, builder, knowledge_card, aider, cursor, diff, search-replace]
tldr: "LLM-to-host file edit formats: Aider WHOLE/DIFF/UDIFF, search-replace blocks, unified diff"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_examples_edit_format
  - p03_sp_edit_format_builder
  - bld_output_template_edit_format
  - atom_28_code_agents
  - bld_architecture_edit_format
  - bld_examples_diff_strategy
  - bld_tools_diff_strategy
  - bld_knowledge_card_diff_strategy
  - edit-format-builder
  - n06_hybrid_review2_final
---

## Domain Overview

This ISO specifies an edit format: how diffs or patches are expressed and applied.

Edit formats define the structured syntax LLMs use to communicate file modifications to
host systems (code editors, CI pipelines, auto-apply tools). The format must be: unambiguous
(the tool applies exactly what the LLM intended), resilient (handles whitespace drift, line
number changes), and parseable (simple regex/parser can extract and apply changes). Unlike
diff_strategy (which computes HOW differences are detected), edit_format defines the WIRE
FORMAT the LLM emits.

Four primary format families dominate production LLM coding tools:
1. **WHOLE file** (Aider WHOLE mode, Claude Projects file artifacts)
2. **Unified diff** (UDIFF, standard `diff -u` output)
3. **Search-replace blocks** (Aider search/replace, Cursor apply)
4. **Structured patch** (JSON Patch RFC 6902, language-server edits)

## Aider Edit Formats (Primary Reference)

Aider exposes four edit format modes. Understanding these is essential for edit_format artifacts.

### WHOLE Mode

LLM returns the entire file content. Host system replaces the file verbatim.

```
filename.py
```python
# entire file content here
def foo():
    return 42
```

- **Pros**: Simple, unambiguous, no hunk matching needed
- **Cons**: High token cost for large files; wastes tokens on unchanged lines
- **Use when**: File is small (<100 lines) or most content is changing

### DIFF Mode (Aider custom format)

LLM returns hunks using `<<<<<<< ORIGINAL` / `=======` / `>>>>>>> UPDATED` markers.

```
filename.py
<<<<<<< ORIGINAL
def old_function():
    return 1
=======
def new_function():
    return 42
>>>>>>> UPDATED
```

- **Pros**: Explicit before/after; easy for humans to review
- **Cons**: Requires fuzzy matching if file drifted from context
- **Use when**: Medium files, precise replacement of specific blocks

### UDIFF Mode (Unified Diff)

Standard Unix unified diff format (`diff -u`). LLM emits `---`/`+++`/`@@` headers with `+`/`-` lines.

```
--- a/filename.py
+++ b/filename.py
@@ -10,7 +10,7 @@
 def foo():
-    return 1
+    return 42
```

- **Pros**: Standard format (git-compatible), minimal tokens, industry-universal
- **Cons**: Line numbers can drift; requires context to anchor hunks
- **Use when**: Small targeted changes, git-workflow integration

### UDIFF-SIMPLE Mode

Simplified unified diff without context lines. Only the `+`/`-` lines, no `@@ -n,m @@` headers.

```
--- a/filename.py
+++ b/filename.py
-    return 1
+    return 42
```

- **Use when**: Simple single-hunk changes; reduces token output

## Search-Replace Block Format (Cursor Apply, Aider Search/Replace)

The most resilient format for LLM edits. No line numbers needed.

```
path/to/file.py
<<<<<<< SEARCH
    old code that must match exactly
    (including whitespace and indentation)
=======
    new code to replace it with
>>>>>>> REPLACE
```

**Properties:**
- SEARCH block must match file content EXACTLY (case, whitespace, indentation)
- If SEARCH block not found exactly, apply tool should raise error (not silently skip)
- Multiple SEARCH/REPLACE blocks in one response = sequential application
- Empty SEARCH = insert at start of file; empty REPLACE = delete the match

**Cursor apply format** uses the same pattern with slightly different markers:
```
```edit path/to/file.py
<<<<<<< SEARCH
old code
=======
new code
>>>>>>> REPLACE
```
```

## Structured Edit Formats

### JSON Patch (RFC 6902)

Structured operations for JSON/YAML config files.

```json
[
  { "op": "replace", "path": "/version", "value": "2.0.0" },
  { "op": "add", "path": "/dependencies/lodash", "value": "^4.17" },
  { "op": "remove", "path": "/scripts/test-old" }
]
```

Operations: `add`, `remove`, `replace`, `move`, `copy`, `test`
Reference: RFC 6902 (not 6943 -- 6943 does not exist)

### Language Server Protocol (LSP) TextEdit

Used by VS Code, Neovim, JetBrains for in-editor apply.

```json
{
  "range": {
    "start": { "line": 10, "character": 4 },
    "end": { "line": 10, "character": 15 }
  },
  "newText": "new_function_name"
}
```

## Key Concepts

| Concept | Definition | Source |
|---------|-----------|--------|
| Hunk | Contiguous block of changed lines with context | Git diff format |
| Search-replace block | SEARCH/REPLACE marker pair for context-anchored edits | Aider docs |
| Unified diff | Standard `-u` diff format: --- / +++ headers + @@ hunks | POSIX diff |
| WHOLE mode | Full file replacement -- highest token cost, lowest ambiguity | Aider docs |
| Fuzzy matching | Finding SEARCH block even with minor whitespace drift | Aider core |
| JSON Patch | RFC 6902 structured operations for JSON/YAML documents | RFC 6902 |
| LSP TextEdit | Range-based in-editor modification | LSP spec v3.17 |
| Context lines | Unchanged lines surrounding a hunk -- anchor for application | diff manual |
| Conflict marker | <<<<<< / ====== / >>>>>> merge conflict syntax | Git |

## Industry Standards

| Standard | Notes |
|----------|-------|
| RFC 6902 | JSON Patch -- `add`, `remove`, `replace`, `move`, `copy`, `test` |
| POSIX diff -u | Unified diff format -- `---`, `+++`, `@@ -n,m +n,m @@` |
| LSP spec v3.17 | TextEdit, WorkspaceEdit for editor-level changes |
| Aider edit formats | WHOLE / DIFF / UDIFF / SEARCH-REPLACE (see aider.chat/docs) |
| Cursor apply | Search-replace variant with triple-backtick fencing |
| RFC 5261 | XML Patch -- analogous to JSON Patch for XML |

## Common Patterns

1. **Default to search-replace** for LLM coding agents -- no line number drift, explicit context
2. **WHOLE for new files** -- nothing to match, full content is always correct
3. **Unified diff for git integration** -- output can be piped to `git apply` directly
4. **Multiple hunks per response** -- apply sequentially top-to-bottom to avoid offset shifts
5. **Include file path in every format** -- host tool needs path to locate file

## Pitfalls

- Using line numbers as anchors -- they change with every edit and cause misapplication
- SEARCH block with loose whitespace matching -- exact match is required for reliability
- Missing file path in WHOLE mode -- host cannot determine target file
- Applying hunks out of order -- later hunks have shifted line numbers after earlier ones apply
- Confusing edit_format (wire format) with diff_strategy (algorithm) -- they are separate concerns
- Citing RFC 6943 for JSON Patch -- that RFC does not exist; correct reference is RFC 6902
| search_replace | Most common LLM edit: `<<<` search `===` replace `>>>` markers |
| unified_diff | Standard git patch: `---` `+++` `@@` hunks |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_edit_format]] | downstream | 0.60 |
| [[p03_sp_edit_format_builder]] | downstream | 0.48 |
| [[bld_output_template_edit_format]] | downstream | 0.47 |
| [[atom_28_code_agents]] | sibling | 0.34 |
| [[bld_architecture_edit_format]] | downstream | 0.33 |
| [[bld_examples_diff_strategy]] | downstream | 0.32 |
| [[bld_tools_diff_strategy]] | downstream | 0.32 |
| [[bld_knowledge_card_diff_strategy]] | sibling | 0.28 |
| [[edit-format-builder]] | downstream | 0.27 |
| [[n06_hybrid_review2_final]] | downstream | 0.26 |
