---
mission: SELFHEAL
wave: 1
nucleus: n04
role: quality_inventory
auto_accept: true
deliverable: _reports/selfheal/w1_n04_inventory.md
timeout_s: 600
---

# Wave 1 -- Quality Inventory (N04)

## Task
Scan CEX artifacts and list those with `quality: null` or `quality < 8.0`.

## Scope
Same dirs as N01 (see plan). Use Glob `**/*.md` under Nxx_* and Pxx_* dirs.

## Rules
1. BOUND the scan to max 500 files.
2. Read frontmatter of each .md (first 30 lines).
3. For each file extract:
   - `quality` value (null, number, or missing)
   - `kind` if present
   - `pillar` if present
4. Classify:
   - `quality_null`: frontmatter has `quality: null`
   - `quality_low`: numeric quality and value < 8.0
   - `quality_missing`: no `quality` key at all
5. Do NOT rescore. Inventory only.
6. Emit exactly ONE output file at `_reports/selfheal/w1_n04_inventory.md`.

## Output shape
```markdown
---
mission: SELFHEAL
wave: 1
nucleus: n04
scanned: <N>
quality_null: <A>
quality_low: <B>
quality_missing: <C>
---
# W1 Quality Inventory
| path | kind | pillar | quality | classification |
|------|------|--------|---------|----------------|
| ... | ... | ... | ... | ... |

## Summary
- total scanned: N
- quality_null: A
- quality_low: B
- quality_missing: C
- bottom 10: (paths sorted ascending by quality)
```

## Signal
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', 9.0, mission='SELFHEAL')"
```
