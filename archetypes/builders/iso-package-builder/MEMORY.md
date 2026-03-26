---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: iso-package-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any non-null value)
2. Using hyphens in id slug (must be underscores: p02_iso_my_agent not p02_iso_my-agent)
3. Declaring tier "standard" but including only 3 files (tier must match file count)
4. Hardcoded paths leaking into system_instruction.md from source agent (/home/, C:\, records/)
5. files_count not matching actual files in directory (manual count error)
6. system_instruction.md exceeding 4096 tokens (copy-paste from verbose system prompt)
7. Missing lp_mapping for files beyond the 3 required (standard tier needs all 7 mapped)
8. Naming files incorrectly (prompt.txt instead of system_instruction.md, readme instead of instructions)
9. Including files beyond declared tier (whitelabel files in a standard package)
10. File Inventory table missing or not listing all files with status column

### Packaging Patterns
- Manifest-first workflow: always start with manifest.yaml, then generate other files
- Tier escalation: start minimal for prototype, promote to standard when production-ready
- Token budgeting: count system_instruction tokens early (Phase 1) to avoid rework
- Path scanning: grep for /home/, /Users/, C:\, records/ before declaring portable: true
- LP mapping: derive from CONFIG.md LP Mapping Enum, never invent new mappings
- File inventory: use the exact table structure from OUTPUT_TEMPLATE for consistency

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | tier mismatch, token overflow, hardcoded paths |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing an iso_package, update:
- New common mistake (if encountered)
- New packaging pattern (if discovered)
- Production counter increment
