---
glob: "**"
alwaysApply: true
description: "Shared-file proposal pattern — nuclei MUST NOT directly edit shared files during concurrent execution"
---

# Shared-File Proposal Rule

## The Problem

When multiple nuclei run concurrently (grid dispatch), two or more may need to modify the same file. Direct edits cause:
- Git merge conflicts (both nuclei commit different versions)
- Data loss (last-write-wins overwrites earlier nucleus output)
- Corrupt state (partial writes to JSON/YAML mid-read by another nucleus)

## The Rule

**During concurrent execution, nuclei MUST NOT directly edit protected shared files.**
Instead, write a `.proposal` file. N07 (or the merge coordinator) applies proposals after the wave completes.

## Protected Files (always use proposal pattern)

| File | Why |
|------|-----|
| `CLAUDE.md` | Global config — all nuclei read it |
| `.cex/kinds_meta.json` | Kind registry — N03/N04 both extend it |
| `.cex/runtime/grid_status.json` | Grid state — mission_runner + nuclei both touch it |
| `.cex/config/nucleus_models.yaml` | Model routing — N05/N07 both configure it |
| `.cex/runtime/decisions/decision_manifest.yaml` | GDP decisions — read-only during grid |
| `_tools/cex_*.py` | Shared tools — N05 builds, others import |
| `.claude/rules/*.md` | Rules — N04 writes, all nuclei read |
| `archetypes/builders/_shared/*` | Shared ISOs — cross-nucleus dependency |

## How Proposals Work

### 1. Nucleus writes a proposal file

```
.cex/runtime/proposals/{nucleus}_{timestamp}_{target_file_slug}.proposal.md
```

Example: `.cex/runtime/proposals/n04_20260407_153000_kinds_meta.proposal.md`

### 2. Proposal format

```yaml
---
nucleus: n04
target: .cex/kinds_meta.json
action: merge_keys          # merge_keys | append_lines | replace_section | patch_json
priority: normal             # critical | normal | low
created: 2026-04-07T15:30:00-03:00
depends_on: []               # other proposals that must apply first
idempotent: true             # safe to apply twice?
---

## Description
Add 3 new kinds discovered during taxonomy expansion.

## Payload
```json
{
  "task_queue_entry": {
    "pillar": "P09",
    "description": "Task queue entry for continuous dispatch",
    "naming": "p09_tqe_{{task}}.yaml",
    "max_bytes": 2048,
    "core": false,
    "llm_function": "CALL",
    "boundary": "Queue entry. NOT a handoff (P02) or signal (runtime)."
  }
}
```

## Rollback
Remove the 3 keys listed above from kinds_meta.json.
```

### 3. Proposal actions

| Action | Semantics | Conflict risk |
|--------|-----------|---------------|
| `merge_keys` | Deep-merge JSON/YAML keys (new keys added, existing untouched) | Low |
| `append_lines` | Append content to end of file (or after a marker) | None |
| `replace_section` | Replace content between `## Start` and `## End` markers | Medium |
| `patch_json` | JSON Patch (RFC 6902) operations array | Medium |
| `full_replace` | Replace entire file (DANGEROUS — requires `priority: critical`) | High |

### 4. N07 merge protocol (post-wave)

```
1. List all .proposal.md files in .cex/runtime/proposals/
2. Sort by: priority (critical first), then timestamp (oldest first)
3. For each proposal:
   a. Acquire CexLock on target file
   b. Validate: target exists? action supported? payload valid?
   c. Apply action (merge/append/replace/patch)
   d. Release lock
   e. Move proposal to .cex/runtime/proposals/applied/
4. If conflict detected (2 proposals touch same key):
   a. Apply higher-priority proposal
   b. Flag lower-priority for manual review
   c. Write conflict report to .cex/runtime/proposals/conflicts/
5. git add + git commit -m "[N07] apply {N} proposals from wave {W}"
```

## When Proposals Are NOT Required

- **Solo dispatch**: Only 1 nucleus running — direct edits are safe
- **Own namespace**: Files inside your nucleus directory (e.g., N04_knowledge/*) — you own these
- **New files**: Creating a file that doesn't exist yet — no conflict possible
- **Signals**: `.cex/runtime/signals/` — designed for concurrent writes (unique filenames)
- **Handoffs**: `.cex/runtime/handoffs/` — one file per nucleus, no overlap

## Quick Decision Tree

```
Is another nucleus running concurrently?
  NO  --> Edit directly (solo mode)
  YES --> Is the file in your own N0x_*/ directory?
            YES --> Edit directly (you own it)
            NO  --> Is the file in the Protected Files list?
                      YES --> Write .proposal.md
                      NO  --> Use CexLock, then edit directly
```

## Integration with cex_lock.py

For non-protected files that still need coordination, use the lock manager:

```python
from _tools.cex_lock import CexLock

with CexLock("path/to/shared/file.yaml", timeout=30):
    # Safe to read-modify-write
    data = load(path)
    data["new_key"] = value
    save(path, data)
```

The proposal pattern is STRONGER than locking — it defers the merge entirely,
eliminating even the possibility of conflict during the wave.

## Enforcement

- `cex_mission_runner.py` creates `.cex/runtime/proposals/` before each wave
- Post-wave consolidation step merges all proposals before the next wave starts
- `cex_doctor.py` flags direct edits to protected files during grid execution
