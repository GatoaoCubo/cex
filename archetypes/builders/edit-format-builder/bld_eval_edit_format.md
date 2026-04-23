---
kind: quality_gate
id: p06_qg_edit_format
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for edit_format
quality: 9.0
title: "Quality Gate Edit Format"
version: "1.0.0"
author: wave1_builder_gen
tags: [edit_format, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for edit_format"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_edit_format
  - bld_output_template_edit_format
  - bld_knowledge_card_edit_format
  - p03_sp_edit_format_builder
  - bld_schema_edit_format
  - bld_architecture_edit_format
  - p10_lr_edit_format_builder
  - bld_collaboration_search_tool
  - edit-format-builder
  - p11_qg_content_filter
---

## Quality Gate

## Definition  

This ISO specifies an edit format: how diffs or patches are expressed and applied.
| metric | threshold | operator | scope |  
|---|---|---|---|  
| File Format Compliance | 100% | equals | All host files |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML Valid | Invalid YAML syntax |  
| H02 | ID matches pattern | ID does not match [a-zA-Z0-9_]+ |  
| H03 | kind matches | kind ≠ "edit_format" |  
| H04 | Required fields present | Missing 'action' or 'path' |  
| H05 | Syntax valid | Malformed JSON or YAML |  
| H06 | File size limit | Size > 10MB |  
| H07 | Metadata present | Missing 'author' or 'timestamp' |  
| H08 | Checksum valid | SHA-256 mismatch |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | YAML Structure | 0.15 | 1.0 for valid, 0.5 for minor issues |  
| D02 | ID Pattern | 0.15 | 1.0 for match, 0.0 for mismatch |  
| D03 | Kind Consistency | 0.10 | 1.0 for correct, 0.0 for incorrect |  
| D04 | Metadata Completeness | 0.15 | 1.0 for full, 0.5 for partial |  
| D05 | Syntax Quality | 0.15 | 1.0 for clean, 0.0 for errors |  
| D06 | File Size | 0.05 | 1.0 for ≤10MB, 0.0 for >10MB |  
| D07 | Checksum Validity | 0.10 | 1.0 for valid, 0.0 for invalid |  
| D08 | Documentation | 0.15 | 1.0 for clear, 0.5 for vague |  

## Actions  
| Score | Action |  
|---|---|  
| ≥9.5 | Automatically merge and notify |  
| ≥8.0 | Schedule for review |  
| ≥7.0 | Request changes |  
| <7.0 | Block and require fixes |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Critical hotfix with emergency approval | Senior Architect | Email confirmation, system log entry |

## Examples

## Golden Example 1: Search-Replace Format Spec

This ISO specifies an edit format: how diffs or patches are expressed and applied.

```markdown
---
id: p06_ef_search_replace
kind: edit_format
pillar: P06
title: "Search-Replace Block Edit Format"
version: "1.0.0"
format_type: search_replace
edit_scope: targeted_replace
created: "2026-04-13"
author: "n04"
domain: "code_agent"
quality: null
tags: [edit_format, search_replace, aider, cursor]
tldr: "Context-anchored SEARCH/REPLACE block pairs for LLM code edits -- no line numbers"
compatible_tools: [aider, cursor, claude-code]
---

## Overview

Search-replace block format enables LLMs to specify precise file edits by referencing
exact content rather than line numbers. Resilient to file drift between context loading
and edit application. Used by Aider (search/replace mode) and Cursor (apply format).

## Format Specification

Each edit is expressed as a block with SEARCH (exact content to find) and REPLACE
(new content to substitute). The host applies the edit by locating the SEARCH content
exactly in the target file and replacing it with REPLACE content.

```
path/to/target_file.py
<<<<<<< SEARCH
    old_function_call(param1, param2)
=======
    new_function_call(param1, param2, timeout=30)
>>>>>>> REPLACE
```

Multiple blocks apply sequentially. File path appears once before the first block
or before each block in multi-file edits.

## Application Rules

1. SEARCH block MUST match file content byte-for-byte (whitespace, indentation, CRLF/LF)
2. If SEARCH block not found: raise FileEditError, do NOT skip silently
3. Apply top-to-bottom; do NOT reorder blocks
4. Empty REPLACE = delete SEARCH content
5. Empty SEARCH = prepend REPLACE at file start

## Validation Rules

- Both SEARCH and REPLACE sections must be non-empty (except explicit delete/prepend)
- File path must be present and point to a valid path
- Delimiter lines must be exactly: `<<<<<<< SEARCH`, `=======`, `>>>>>>> REPLACE`
- SEARCH content must not contain the `=======` delimiter
```

## Golden Example 2: Unified Diff Format Spec

```markdown
---
id: p06_ef_unified_diff
kind: edit_format
pillar: P06
title: "Unified Diff Edit Format"
version: "1.0.0"
format_type: unified_diff
edit_scope: partial_hunk
created: "2026-04-13"
author: "n04"
domain: "git_workflow"
quality: null
tags: [edit_format, unified_diff, git]
tldr: "Standard unified diff for LLM code edits -- git-apply compatible"
compatible_tools: [git-apply, patch, aider]
---

## Overview

Standard POSIX unified diff (`diff -u` output). Git-compatible. Best for small targeted
changes in git-centric workflows where the output can be piped to `git apply` directly.

## Format Specification

```
--- a/src/utils.py
+++ b/src/utils.py
@@ -42,7 +42,7 @@
 def process(items):
-    for item in items:
+    for item in sorted(items):
         handle(item)
```

## Application Rules

1. Apply via `git apply` or `patch -p1 < file.diff`
2. Context lines anchor the hunk -- must match existing file content
3. Line number offsets in `@@ -n,m +n,m @@` are informational; `patch` recalculates if drift
```

## Anti-Example 1: Line Numbers as Anchors

```yaml
---
id: p06_ef_line_based
format_type: search_replace
---
# Edit specification
file: src/auth.py
line: 42
action: replace
old: "    pass"
new: "    return True"
```

**Why it fails:**
Line numbers are unstable -- any edit above line 42 shifts all subsequent line numbers.
By the time the agent applies the edit, line 42 may contain something entirely different.
Use SEARCH/REPLACE with actual content, not line numbers, for reliable application.

## Anti-Example 2: Placeholder Content in WHOLE Mode

```
src/models/user.py
```python
# ... existing imports ...

class User:
    # ... existing methods ...

    def new_method(self):
        return True
```
```

**Why it fails:**
`# ... existing imports ...` and `# ... existing methods ...` are placeholders, not real
content. Whole-file format MUST contain the complete file. A host applying this format
would overwrite all existing imports and methods with placeholder comments.

## Anti-Example 3: Mixing diff_strategy into edit_format

```yaml
---
id: p06_ef_hybrid
format_type: unified_diff
---
## Format
Uses unified diff with semantic matching enabled.

diff_strategy: semantic     # <-- WRONG: this is diff_strategy concern
fuzzy_threshold: 0.85       # <-- WRONG: matching algorithm, not wire format
edit: replace
from: "old code"
to: "new code"
```

**Why it fails:**
`diff_strategy`, `fuzzy_threshold`, and matching parameters belong to `diff_strategy` kind.
`edit_format` specifies the WIRE FORMAT (what the LLM emits), not how the host FINDS the
matching location in the file. These are separate CEX kinds with separate builders.

## Format Comparison
| Format | Patch Size | Apply Time | Error Rate | Best For |
|--------|-----------|-----------|-----------|----------|
| search_replace | small | fast | low | LLM outputs |
| unified_diff | small | fast | low | version control |
| whole_file | large | fast | none | complete rewrites |
| json_patch | tiny | fast | low | data files |
| semantic_diff | small | slow | medium | refactoring |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|-------------|------------------|
| Missing markers | Apply fails silently | Always include search + replace markers |
| Overlapping patches | Conflict on apply | Sequence patches or use atomic updates |
| No error handling | Silent corruption | Validate pre/post apply checksums |
| Ambiguous search | Wrong replacement | Ensure search pattern is unique |
| Large context | Token waste | Use minimal context window |
| No fallback | Hard failure | Provide whole-file fallback |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
