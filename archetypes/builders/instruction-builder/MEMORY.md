---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: instruction-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p03_ins_my_task not p03_ins_my-task)
3. steps_count not matching actual numbered steps in body (S03 catches mismatch)
4. Compound steps with multiple actions ("deploy and verify and restart") — split them
5. Vague prerequisites ("environment ready") instead of verifiable ("Python 3.10+ installed")
6. Missing rollback when atomic: false (H08 rejects)
7. Including persona/identity text ("You are an expert...") — belongs in system_prompt
8. Forgetting validation section (common omission, S07 catches)

### Step Decomposition Patterns
- Command steps: "Run `{command}` — expect `{output}`"
- File operations: "Create/edit `{path}` — verify with `ls -la {path}`"
- Verification steps: "Confirm `{check}` — output should show `{expected}`"
- Conditional steps: split into separate numbered steps with IF noted
- Long-running steps: "Wait for completion (~{time}) — monitor via `{command}`"

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | compound steps, vague prerequisites, missing rollback |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing an instruction, update:
- New common mistake (if encountered)
- New step decomposition pattern (if discovered)
- Production counter increment
