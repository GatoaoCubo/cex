---
mission: SELFHEAL
wave: 1
nucleus: n01
role: semantic_inventory
auto_accept: true
deliverable: _reports/selfheal/w1_n01_inventory.md
timeout_s: 600
---

# Wave 1 -- Semantic Inventory (N01)

## Task
Scan the CEX repo and produce a structured inventory of SEMANTIC defects in artifacts.

## Scope
Walk these dirs (use Glob): `N01_intelligence/`, `N02_marketing/`, `N03_engineering/`, `N04_knowledge/`, `N05_operations/`, `N06_commercial/`, `N07_admin/`, `P01_knowledge/`, `P02_model/`, `P03_prompt/`, `P04_tools/`, `P05_output/`, `P06_schema/`, `P07_evaluation/`, `P08_architecture/`, `P09_config/`, `P10_memory/`, `P11_feedback/`, `P12_orchestration/`
Consider only `.md` files.

## Rules
1. BOUND the scan to max 500 files (stop once reached).
2. For each file detect ANY of:
   - `no_frontmatter`: file does not start with `---`
   - `missing_required`: frontmatter lacks `id` or `kind` or `pillar`
   - `wrong_pillar`: pillar in frontmatter differs from file's parent pillar dir
   - `stale_fact`: contains "2024" or "2025" as a date reference (easy false-positive, mark as low-conf)
3. Do NOT fix anything -- inventory only.
4. Emit exactly ONE output file at `_reports/selfheal/w1_n01_inventory.md`.

## Output shape
```markdown
---
mission: SELFHEAL
wave: 1
nucleus: n01
scanned: <N>
defects: <M>
---
# W1 Semantic Inventory
| path | defect | confidence |
|------|--------|------------|
| ... | ... | ... |

## Summary
- scanned: N
- defects: M
- top_pillars: ...
```

## Signal
After writing the file, run:
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n01', 'complete', 9.0, mission='SELFHEAL')"
```
