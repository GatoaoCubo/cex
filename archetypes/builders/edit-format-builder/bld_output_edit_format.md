---
kind: output_template
id: bld_output_template_edit_format
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for edit_format production
quality: 9.1
title: "Output Template Edit Format"
version: "1.1.0"
author: n04_hybrid_review2
tags: [edit_format, builder, output_template]
tldr: "Template with vars for edit_format production -- whole_file, unified_diff, search_replace, json_patch variants"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_examples_edit_format
  - bld_knowledge_card_edit_format
  - p03_sp_edit_format_builder
  - bld_schema_edit_format
  - bld_architecture_edit_format
  - kc_edit_format
  - edit-format-builder
  - p08_ac_explore
  - hybrid_review2_n04
  - p06_vs_frontmatter
---

## Variant A: Whole File Format
This ISO specifies an edit format: how diffs or patches are expressed and applied.

```markdown
---
id: p06_ef_{{name}}
kind: edit_format
pillar: P06
title: "{{title}}"
version: "1.0.0"
format_type: whole_file
edit_scope: whole_file
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [edit_format, whole_file]
tldr: "{{tldr}}"
compatible_tools: [aider, claude-projects, cursor]
---

## Overview
{{description}}. LLM returns the complete file content. Host replaces the file verbatim.
Best for: new files, small files (<100 lines), or large-scale rewrites.

## Format Specification
The LLM MUST output the target file path on a line by itself, followed immediately by
a fenced code block containing the entire new file content:

```
`{{file_path}}`
``{{language}}`
{{entire_file_content}}
```
```

No diff markers. No partial content. The entire file, start to finish.

## Application Rules
1. Host receives the file path and complete content.
2. If file exists: overwrite entirely.
3. If file does not exist: create with full content.
4. No matching required -- zero ambiguity.

## Validation Rules
- File path MUST be present and non-empty
- Content block MUST be non-empty
- Language tag MUST match file extension
- No partial content or placeholder comments allowed

## Examples
**Valid:**
```
src/utils/helper.py
```python
def greet(name):
    return f"Hello, {name}"
```
```

**Invalid (partial content):**
```
src/utils/helper.py
```python
# ... existing code ...
def greet(name):
    return f"Hello, {name}"
```
```
Reason: `# ... existing code ...` is a placeholder -- the host cannot apply this as-is.
```

---

## Variant B: Search-Replace Block Format
```markdown
---
id: p06_ef_{{name}}
kind: edit_format
pillar: P06
title: "{{title}}"
version: "1.0.0"
format_type: search_replace
edit_scope: {{edit_scope}}
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [edit_format, search_replace]
tldr: "{{tldr}}"
compatible_tools: [aider, cursor]
---

## Overview
{{description}}. Context-anchored replacement using SEARCH/REPLACE block pairs.
Best for: targeted edits without line numbers, multi-file changes, resilient application.

## Format Specification
```
`{{file_path}}`
<<<<<<< SEARCH
`{{exact_content_to_find}}`
=======
`{{new_content_to_replace_with}}`
>>>>>>> REPLACE
```

Multiple blocks per response are applied sequentially top-to-bottom.

## Application Rules
1. SEARCH block MUST match file content EXACTLY (whitespace, indentation, line endings).
2. If SEARCH not found: raise error, do NOT silently skip.
3. Apply blocks in order -- do not re-sort.
4. Empty REPLACE = delete the matched content.
5. Empty SEARCH = insert REPLACE content at beginning of file.

## Validation Rules
- Each block MUST have both SEARCH and REPLACE sections
- SEARCH content MUST not contain the `=======` delimiter unescaped
- File path MUST precede the first block

## Examples
**Valid:**
```
src/auth/login.py
<<<<<<< SEARCH
    password_hash = md5(password)
=======
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
>>>>>>> REPLACE
```

**Invalid (line numbers instead of content):**
```
src/auth/login.py
<<<<<<< SEARCH
line 42
=======
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
>>>>>>> REPLACE
```
Reason: SEARCH must contain actual file content, not line number references.
```

---

## Variant C: Unified Diff Format
```markdown
---
id: p06_ef_{{name}}
kind: edit_format
pillar: P06
title: "{{title}}"
version: "1.0.0"
format_type: unified_diff
edit_scope: {{edit_scope}}
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [edit_format, unified_diff]
tldr: "{{tldr}}"
compatible_tools: [git-apply, patch, aider]
---

## Overview
{{description}}. Standard unified diff (`diff -u` output). Git-compatible.
Best for: git workflows, code review tools, standard patch application.

## Format Specification
```
--- a/`{{file_path}}`
+++ b/`{{file_path}}`
@@ -`{{start_line}}`,{{original_lines}} +{{start_line}},`{{new_lines}}` @@
 `{{context_line}}`
-`{{removed_line}}`
+`{{added_line}}`
 `{{context_line}}`
```

## Application Rules
1. Apply via `git apply` or `patch -p1`.
2. Context lines (no prefix) MUST match existing file for hunk anchoring.
3. Multiple hunks applied top-to-bottom; line offsets adjust automatically.

## Validation Rules
- `---` and `+++` headers MUST be present
- Each hunk MUST start with `@@ -n,m +n,m @@`
- At least 3 context lines around each change (unless at file start/end)
```

## Template Validation
| Field | Required | Constraint |
|-------|---------|------------|
| format_type | Y | From allowed enum |
| encoding | Y | Must specify encoding method |
| apply_example | Y | Show input + output |
| reversible | Y | Boolean |
| granularity | Y | token/line/block/file |
| error_handling | Recommended | What happens on failure |
| performance | Recommended | Typical apply time/cost |
| size_impact | Recommended | Patch vs file size ratio |
| tooling | Recommended | Which tools support this format |
| limitations | Recommended | Known edge cases |
| streaming_safe | Optional | Can apply while streaming |
| parallel_safe | Optional | Can apply concurrently |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_edit_format]] | downstream | 0.60 |
| [[bld_knowledge_card_edit_format]] | upstream | 0.42 |
| [[p03_sp_edit_format_builder]] | upstream | 0.36 |
| [[bld_schema_edit_format]] | downstream | 0.34 |
| [[bld_architecture_edit_format]] | downstream | 0.28 |
| [[kc_edit_format]] | upstream | 0.27 |
| [[edit-format-builder]] | downstream | 0.24 |
| [[p08_ac_explore]] | downstream | 0.22 |
| [[hybrid_review2_n04]] | upstream | 0.22 |
| [[p06_vs_frontmatter]] | downstream | 0.21 |
