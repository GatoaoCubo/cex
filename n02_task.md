---
mission: WAVE7
nucleus: n02
wave: lifecycle-consolidation
created: 2026-04-14
model: claude-opus-4-6
---

# N02 -- Exhaustive source regrouping into non-aging taxonomy lifecycle pipeline

## Mission

N04 built the scout + seed config + lifecycle spec. Your job: **harvest every source reference scattered across the repo** and merge them into ONE authoritative pipeline. Nothing must escape the scout's watch list.

## Deliverables

### 1. `_tools/cex_source_harvester.py` (~300 lines)

Scans the entire repo and extracts source references from:
- `N01_intelligence/research/**/*.md` -- all research KCs (URL citations, arXiv IDs, RFC numbers, GitHub links)
- `P01_knowledge/library/**/*.md` -- knowledge cards (standards references)
- `_docs/specs/**/*.md` -- spec documents (upstream citations)
- `archetypes/builders/**/bld_knowledge_card_*.md` -- builder KCs (253+ files)
- `.claude/rules/*.md` -- rule files (industry term references)
- `.cex/config/taxonomy_sources.yaml` -- N04's seed (starting point)
- `CLAUDE.md` -- root pointers

Extract patterns:
- URLs (http/https/ftp)
- arXiv IDs (`arXiv:\d{4}\.\d{4,5}`)
- RFC numbers (`RFC \d+`)
- GitHub slugs (`github\.com/[^/]+/[^/\s]+`)
- W3C TRs (`w3\.org/TR/\S+`)
- IETF drafts (`datatracker\.ietf\.org/doc/\S+`)
- ISO/IEEE/NIST standard codes (`ISO/IEC \d+`, `IEEE \d+`, `NIST AI \d+`)
- HuggingFace models (`huggingface\.co/[^/]+/[^/\s]+`)
- DOI references (`doi\.org/\S+`)

Dedupe via URL canonicalization + fuzzy match (levenshtein threshold).

Output: YAML merged into `.cex/config/taxonomy_sources.yaml` with new entries grouped by source_type. Preserve N04's existing entries. Tag harvest origin per entry (`harvested_from: <file-path>`).

Run: `python _tools/cex_source_harvester.py --dry-run | --apply`

### 2. `.cex/config/taxonomy_sources.yaml` (expanded to ~200+ entries)

Merge N04's 30 seeded sources with harvested ones. Target: complete, dedup, ordered by priority. Every entry has:
```yaml
- name: <canonical-name>
  type: github|arxiv|w3c|ietf|iso|ieee|nist|huggingface|doi|rfc|website
  url: <canonical-url>
  watch_paths: [<paths>]
  extract_patterns: [<regex>]
  cadence: daily|weekly|monthly
  priority: critical|high|medium|low
  harvested_from: <relative-path | seeded>
  last_checked: 2026-04-14
  status: active|deprecated|archived
```

### 3. `_tools/cex_source_harvester.py` hooks into `cex_taxonomy_scout.py`

Extend scout to read the full harvested YAML (not just seeded). Add CLI flag: `--harvest-first` (runs harvester then scout).

### 4. Taxonomy pipeline end-to-end test

Write `.cex/runtime/tests/test_taxonomy_pipeline.md` demonstrating:
1. Harvest runs -> N entries added
2. Scout reads all entries (with fake HTTP responses or `--offline` mode)
3. Candidate kinds extracted
4. Dedupe against kinds_meta.json works
5. Report: "Pipeline healthy, N sources active, M candidates pending"

### 5. `N04_knowledge/specs/spec_taxonomy_lifecycle.md` update

Add a "Source Harvest" section documenting the harvester tool + how to add new sources + cadence recommendations per source type.

## F3 INJECT

- Read: `_tools/cex_taxonomy_scout.py` (N04's scout)
- Read: `.cex/config/taxonomy_sources.yaml` (seed)
- Read: `N04_knowledge/specs/spec_taxonomy_lifecycle.md` (design)
- Read: `N01_intelligence/research/ai2ai_exhaustive_scan_20260414.md` (most source-dense file)
- Scan: `P01_knowledge/library/` (sample 10-20 KCs to understand URL density)

## ASCII rule

All Python code must be ASCII-only. YAML can have accented content in descriptions but keep names/urls ASCII. See `.claude/rules/ascii-code-rule.md`.

## Commit

```
git add _tools/cex_source_harvester.py .cex/config/taxonomy_sources.yaml N04_knowledge/ .cex/runtime/tests/
git commit -m "[N02] WAVE7: source harvester + 200+ entry taxonomy pipeline + e2e test"
```

## ON COMPLETION

```
python -c "from _tools.signal_writer import write_signal; write_signal('n02', 'complete', 9.0)"
```
