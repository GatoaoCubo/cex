---
kind: tools
id: bld_tools_memory_type
pillar: P04
llm_function: CALL
---

# Tools: memory-type-builder

| Tool | Purpose | Status |
|------|---------|--------|
| cex_memory_types.py | MemoryType enum, should_save(), parse_memory_type() | ACTIVE |
| cex_memory_age.py | Age labels, freshness caveats, decay functions | ACTIVE |
| cex_memory_update.py | Append observations with type-aware decay | ACTIVE |
| cex_compile.py | Compile .md to .yaml in P10_memory/compiled/ | ACTIVE |
| cex_score.py | Score artifact quality (hybrid) | ACTIVE |

## Tool Permissions

| Tool | Read | Write | Execute | Scope |
|------|------|-------|---------|-------|
| cex_memory_types.py | ✅ | ❌ | ✅ | P10 |
| cex_memory_age.py | ✅ | ❌ | ✅ | P10 |
| cex_memory_update.py | ✅ | ✅ | ✅ | P10 |
| cex_compile.py | ✅ | ✅ | ✅ | pillar |
| cex_score.py | ✅ | ❌ | ✅ | pillar |
