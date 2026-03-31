---
description: "Build a CEX artifact via 8F pipeline. Usage: /build <intent>"
---

# /build — Create CEX Artifact

Execute the full 8F pipeline to produce a new artifact.

## Steps

1. Parse the intent: `$ARGUMENTS`
2. Run the 8F Motor to resolve kind:
   ```bash
   python _tools/cex_8f_runner.py "$ARGUMENTS" --execute --verbose
   ```
3. If the runner produces a valid artifact (PASS verdict):
   - Compile: `python _tools/cex_compile.py {output_path}`
   - Validate: `python _tools/cex_hooks.py post-save {output_path}`
   - Commit: `git add {output_path} && git commit -m "[N03] build {kind} via 8F"`
4. If FAIL after retries:
   - Show the issues from F7
   - Suggest manual fixes

## Examples
```
/build create a knowledge card about RAG chunking strategies
/build create an agent for code review automation
/build create a workflow for sales funnel optimization
```
