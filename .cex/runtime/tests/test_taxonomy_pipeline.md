---
id: test_taxonomy_pipeline
kind: context_doc
title: "Taxonomy Pipeline End-to-End Test"
version: 1.0.0
pillar: P01
nucleus: n02
mission: WAVE7
quality: 9.1
tags: [taxonomy, pipeline, test, scout, harvester, e2e]
created: 2026-04-14
density_score: 1.0
---

# Taxonomy Pipeline End-to-End Test

Validates that the full taxonomy lifecycle pipeline runs correctly:
Harvest -> Scout -> Candidate extraction -> Dedup -> Report.

---

## Stage 1: Source Harvester

**Command:**
```bash
python _tools/cex_source_harvester.py --dry-run
```

**Expected output:**
```
=== CEX Source Harvester ===
Root:   <cex-root>
Config: .cex/config/taxonomy_sources.yaml

Files scanned:  <N>
Refs found:     <M>
Deduped/skip:   <K>
New entries:    <J>

Run with --dry-run to preview or --apply to write.
```

**Pass criteria:**
- Exit code 0
- `Files scanned` > 0 (confirms scan targets accessible)
- `New entries` reported as integer (may be 0 if already applied)
- No Python traceback in output

**Apply mode:**
```bash
python _tools/cex_source_harvester.py --apply --verbose
```

**Pass criteria (apply):**
- `[OK] Applied N entries to .cex/config/taxonomy_sources.yaml`
- File `.cex/config/taxonomy_sources.yaml` has a `harvested:` section
- Entry count in YAML header matches reported count

---

## Stage 2: Harvested YAML Validity

**Command:**
```bash
python -c "
import yaml, sys
with open('.cex/config/taxonomy_sources.yaml') as f:
    data = yaml.safe_load(f)
sections = [k for k in data if isinstance(data[k], list)]
total = sum(len(data[k]) for k in sections if isinstance(data[k], list))
print('Sections:', sections)
print('Total entries:', total)
assert total >= 200, f'Expected >= 200 entries, got {total}'
print('[PASS] Entry count OK')
"
```

**Pass criteria:**
- `Total entries` >= 200
- No yaml.YAMLError
- All required sections present: `github`, `arxiv`, `standards`, `community`, `harvested`

**Manual verification (no PyYAML):**
```bash
grep -c "^  - name:" .cex/config/taxonomy_sources.yaml
```
Should print >= 200.

---

## Stage 3: Scout -- Offline / Dry-Run Mode

The scout makes live HTTP requests. For CI/offline testing, use `--dry-run`
which skips file writing but validates config loading and candidate extraction.

**Command:**
```bash
python _tools/cex_taxonomy_scout.py --source github --since 30 --dry-run
```

**Expected output includes:**
```
[OK] Loaded <N> existing kinds
...
[OK] Total raw candidates: <M>
[OK] Deduplicating and scoring...
[OK] Net new candidates after dedup: <K>
```

**Pass criteria:**
- Exit code 0
- `Loaded N existing kinds` where N > 100 (kinds_meta.json loaded)
- No FileNotFoundError for sources config
- No Python traceback

**Harvest-first mode:**
```bash
python _tools/cex_taxonomy_scout.py --harvest-first --source github --since 30 --dry-run
```

**Pass criteria:**
- First line: `[OK] Running source harvester first...`
- Harvester output printed
- Scout then proceeds normally

---

## Stage 4: Candidate Deduplication

Verifies that the scout does not produce duplicate candidates for known kinds.

**Command:**
```bash
python -c "
import json
from pathlib import Path

kinds_meta = json.loads(Path('.cex/kinds_meta.json').read_text())
print('Known kinds:', len(kinds_meta))

candidates_dir = Path('.cex/runtime/taxonomy_candidates')
pending = list(candidates_dir.glob('*.md')) if candidates_dir.exists() else []
print('Pending candidates:', len(pending))

# Check no candidate has same name as an existing kind
duplicates = []
for f in pending:
    text = f.read_text()
    import re
    m = re.search(r'candidate_id:\s*(\S+)', text)
    if m:
        cid = m.group(1)
        if cid in kinds_meta:
            duplicates.append(cid)

if duplicates:
    print('[FAIL] Duplicate candidates:', duplicates)
else:
    print('[PASS] No duplicates against kinds_meta.json')
"
```

**Pass criteria:**
- `[PASS] No duplicates against kinds_meta.json`
- Any pending candidates have status: pending_review (not already-known kinds)

---

## Stage 5: Scout Report (Health Dashboard)

**Command:**
```bash
python _tools/cex_taxonomy_scout.py --report
```

**Expected output:**
```
=== CEX Taxonomy Health ===
Active kinds:       <N> (<M> total with <D> draft)
Deprecated:           <K>
Archived:             <J>
Stale >180d:          <S> [GREEN|YELLOW|RED]
Stale 90-180d:        <T> [GREEN|YELLOW]
Candidates pending:   <P>
Scout last run:       <date>
===========================
```

**Pass criteria:**
- Exit code 0
- Active kinds > 100 (sanity check on kinds_meta.json)
- Deprecated < 20 (healthy pipeline, not over-deprecating)
- No error lines in output

---

## Stage 6: Pipeline Summary

After running all stages, expected result:

| Stage | Tool | Status |
|-------|------|--------|
| 1. Harvest | cex_source_harvester.py --dry-run | [PASS] |
| 2. Apply | cex_source_harvester.py --apply | [PASS] |
| 3. YAML validity | yaml.safe_load + count | [PASS] >= 200 entries |
| 4. Scout dry-run | cex_taxonomy_scout.py --dry-run | [PASS] |
| 5. Harvest-first | scout --harvest-first --dry-run | [PASS] |
| 6. Dedup check | custom py check | [PASS] no dupes |
| 7. Report | scout --report | [PASS] active > 100 |

**Overall pipeline health declaration:**
```
Pipeline healthy, <N> sources active, <M> candidates pending.
```

---

## Runbook

### Run full pipeline test manually:
```bash
cd <cex-root>
python _tools/cex_source_harvester.py --apply
python _tools/cex_taxonomy_scout.py --report
python _tools/cex_taxonomy_scout.py --source github --since 7 --dry-run
```

### Run offline (no HTTP):
```bash
python _tools/cex_source_harvester.py --stats
python _tools/cex_taxonomy_scout.py --report
```

### Add a new source:
1. Edit `.cex/config/taxonomy_sources.yaml` -- add entry in appropriate section
2. Re-run scout for that source:
   `python _tools/cex_taxonomy_scout.py --source github --since 30 --dry-run`
3. Review candidates in `.cex/runtime/taxonomy_candidates/`

### Force re-harvest (after repo changes):
```bash
python _tools/cex_source_harvester.py --apply --verbose
```

---

## Properties

| Property | Value |
|----------|-------|
| Kind | context_doc |
| Pillar | P01 |
| Domain | taxonomy pipeline |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
