---
kind: tools
id: bld_tools_skill
pillar: P04
llm_function: CALL
purpose: Tools available to skill-builder during construction
pattern: what external tools this builder can invoke
---

# Tools: skill-builder

## Available Tools

| Tool | Purpose | When |
|------|---------|------|
| `cex_query.py` | Find existing skills and patterns | F3 INJECT — discover similar skills |
| `cex_compile.py` | Validate frontmatter + compile to YAML | F8 COLLABORATE — after writing |
| `cex_doctor.py` | Check builder spec completeness | F7 GOVERN — verify all 13 specs |
| `cex_index.py` | Update search index | F8 COLLABORATE — after compile |
| `signal_writer.py` | Signal completion | F8 COLLABORATE — after commit |

## Tool Usage Pattern
```
F3: cex_query.py --kind skill → find similar skills
F5: List tools above → ready for use
F7: cex_compile.py {path} → validate
F8: cex_compile.py + cex_doctor.py + signal_writer.py → ship
```

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |
