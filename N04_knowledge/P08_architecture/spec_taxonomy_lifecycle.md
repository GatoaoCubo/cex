---
id: spec_taxonomy_lifecycle
kind: context_doc
8f: F3_inject
title: "CEX Taxonomy Non-Aging Lifecycle System"
version: 1.0.0
pillar: P01
nucleus: n04
mission: AI2AI_DEEP
quality: 9.1
tags: [taxonomy, lifecycle, RAG, discovery, scout, deprecation, versioning]
created: 2026-04-14
related:
  - atom_23_multiagent_protocols
  - kc_llm_vocabulary_atlas
  - taxonomy_completeness_audit
  - cex_llm_vocabulary_whitepaper
  - ai2ai_coverage_matrix_20260414
  - p01_kc_terminology_rosetta_stone
  - bld_collaboration_handoff_protocol
  - bld_tools_model_card
  - n07_memory_industry_audit
  - ai2ai_exhaustive_scan_20260414
---

# CEX Taxonomy Non-Aging Lifecycle System

## Problem Statement

CEX has 238 kinds across 12 pillars. The AI2AI protocol landscape evolves at
20-30 new specs/year. Without a lifecycle system, CEX taxonomy stales in 12-18
months: kinds reference dead specs, builders miss emerging protocols, and the
knowledge graph diverges from industry reality.

**This spec defines the auto-assimilation loop** that keeps CEX taxonomy current
without manual intervention beyond a weekly N07 review gate.

---

## Architecture Overview

```
[Sources]          [Scout]              [Review Gate]       [Assimilation]
GitHub  ----+      cex_taxonomy_        N07 weekly          N03 build
arXiv   ----+----> scout.py    ------>  review of       --> handoff
IETF    ----+      (weekly cron)        candidates          (auto-generated)
W3C     ----+          |
IEEE    ----+      .cex/runtime/
HN/PH   ----+      taxonomy_candidates/
Conf    ----+
```

Signal flow:
1. Scout runs weekly (cron or manual)
2. Candidates written to `.cex/runtime/taxonomy_candidates/`
3. N07 reviews: build / wait / merge / reject
4. N03 builds approved kinds via standard 8F pipeline
5. kinds_meta.json updated with new lifecycle fields
6. Deprecated kinds flagged via `deprecated_by` + migration hints

---

## A. Sources Feed (Auto-Watchers)

### A.1 GitHub Repositories

| Name | Repo | Watch Paths | Priority | Cadence |
|------|------|-------------|----------|---------|
| google-a2a | google-a2a/A2A | spec/, drafts/ | critical | weekly |
| mcp | modelcontextprotocol/modelcontextprotocol | spec/, schema/ | critical | weekly |
| opentelemetry-semconv | open-telemetry/semantic-conventions | model/ | high | weekly |
| w3c-vc | w3c/verifiable-credentials | drafts/ | high | biweekly |
| sigstore | sigstore/sigstore | docs/, spec/ | medium | monthly |
| c2pa | c2pa-org/c2pa-spec | docs/ | medium | monthly |
| lf-ai | lfai-data projects | docs/ | medium | monthly |
| openai-agents | openai/openai-agents-python | docs/, examples/ | high | weekly |
| anthropic-sdk | anthropic/anthropic-sdk-python | src/, docs/ | critical | weekly |
| langchain | langchain-ai/langchain | docs/concepts/ | medium | biweekly |
| llama-index | run-llama/llama_index | docs/ | medium | biweekly |
| autogen | microsoft/autogen | docs/, python/packages/ | high | weekly |
| crew-ai | crewAIInc/crewAI | docs/ | medium | biweekly |
| dspy | stanfordnlp/dspy | docs/ | medium | biweekly |
| smolagents | huggingface/smolagents | docs/ | medium | weekly |
| openapi | OAI/OpenAPI-Specification | versions/ | high | monthly |
| json-schema | json-schema-org/json-schema-spec | drafts/ | high | monthly |

### A.2 arXiv Daily Feed

Query: `(cs.AI OR cs.MA OR cs.CL) AND (protocol OR schema OR interoperability OR agent-to-agent OR multi-agent)`

Tracked keywords for candidate extraction:
- "novel protocol", "propose a schema", "new standard", "interoperability framework"
- "agent communication", "tool use protocol", "context protocol", "memory protocol"
- Venue filters: NeurIPS Systems, ICML Systems, EMNLP System Demos, ACL System Papers

### A.3 Standards Bodies

| Body | Source | Watch Target | Cadence |
|------|--------|-------------|---------|
| IETF | datatracker.ietf.org/drafts/active | AI-tagged working groups | monthly |
| W3C | w3.org/groups/wg/ | AI-adjacent charters (DCAT, VC, DID, WebNN) | monthly |
| ISO/IEC JTC 1/SC 42 | iso.org/committee/6794475 | Published work items | quarterly |
| IEEE SA | standards.ieee.org/ieee/P* | P3119 (synthetic data), P3119, P2933 | monthly |
| NIST AI | csrc.nist.gov/projects/ai | AI RMF profile updates | monthly |

### A.4 Vendor / Community Signals

| Source | Type | Signal | Cadence |
|--------|------|--------|---------|
| HackerNews | community | "Show HN" with 100+ points + AI+protocol tags | daily |
| Product Hunt | community | AI tool launches with API/protocol component | weekly |
| dev.to / Substack | blogs | Posts mentioning new AI schema/protocol | weekly |
| GitHub Trending | community | New repos: agent*, mcp-*, a2a-*, protocol* | weekly |

### A.5 Conference System Papers

Track submission deadlines + proceedings for system papers at:
- NeurIPS (Datasets & Benchmarks, Systems)
- ICML (Systems)
- EMNLP (System Demonstrations)
- ACL (System Demonstrations)
- ICLR (TinyPapers + main)

---

## B. Discovery Protocol

### B.1 Scout Schedule

```
Weekly: Monday 02:00 UTC
  python _tools/cex_taxonomy_scout.py --source all --since 7
```

Daily (lightweight, GitHub only):
```
  python _tools/cex_taxonomy_scout.py --source github --since 1 --dry-run
```

### B.2 Extraction Heuristics

Scout uses layered extraction to find candidate kind names:

**Layer 1 — Structural patterns (high precision):**
```
TypeScript interfaces:    interface\s+[A-Z][a-zA-Z]+
JSON Schema definitions:  "\$defs":\s*\{[^}]+\}
OpenAPI components:       components/schemas/[A-Z][a-zA-Z]+
Protobuf messages:        message\s+[A-Z][a-zA-Z]+
```

**Layer 2 — Keyword extraction (medium precision):**
```
"X protocol"   -> candidate: x_protocol
"X schema"     -> candidate: x_schema
"X format"     -> candidate: x_format
"X message"    -> candidate: x_message
"X contract"   -> candidate: x_contract
```

**Layer 3 — NER patterns (lower precision, needs scoring):**
```
Repeated PascalCase nouns appearing 3+ times in spec documents
```

### B.3 Deduplication

Before writing a candidate, scout checks against existing kinds:

1. **Exact match**: kind name already in kinds_meta.json -> skip
2. **Alias match**: known synonym mapping (e.g., "tool_call" == "function_def") -> skip
3. **Semantic similarity**: TF-IDF cosine against kind descriptions (threshold 0.85) -> flag as potential merge
4. **Boundary overlap**: if candidate description overlaps with existing boundary -> flag

Candidates passing all 4 checks are written to `.cex/runtime/taxonomy_candidates/`.

### B.4 Candidate Scoring

Each candidate gets a composite score (0-10):

| Dimension | Weight | Signal |
|-----------|--------|--------|
| adoption_signal | 0.35 | GitHub stars/forks, download counts, mentions |
| stability | 0.30 | Spec version >= 1.0, > 6 months old, 2+ implementors |
| urgency | 0.20 | CEX gap score (no existing kind covers this) |
| relevance | 0.15 | Domain overlap with CEX pillars |

**Threshold for N07 notification: score >= 6.0**
**Auto-promote to review: score >= 8.0**

### B.5 Candidate File Format

```
.cex/runtime/taxonomy_candidates/
  YYYY-MM-DD_{source}_{slug}.md
```

Example: `2026-04-21_github_tool_invocation_protocol.md`

```yaml
---
candidate_id: tool_invocation_protocol
source: github/modelcontextprotocol/modelcontextprotocol
discovered: 2026-04-21
score: 8.2
score_breakdown:
  adoption_signal: 9.0
  stability: 8.5
  urgency: 7.5
  relevance: 8.0
suggested_kind: tool_invocation_protocol
suggested_pillar: P04
suggested_boundary: "Protocol for agent-to-tool invocation. NOT tool_use (generic pattern) nor mcp_server (MCP-specific server)."
similar_kinds: [mcp_server, cli_tool]
merge_candidate: null
upstream_url: https://github.com/modelcontextprotocol/modelcontextprotocol
status: pending_review
---

## Summary

MCP defines a `ToolInvocationProtocol` as a standardized message envelope for
all tool calls regardless of transport (stdio, SSE, HTTP). This is distinct from
the MCP server definition kind and covers the call/response schema generically.

## Evidence

- 3,420 GitHub stars (spec repo)
- v1.0 released 2025-11
- Implemented by: Claude, Copilot, Cursor, Continue, Windsurf
- Paper: "Model Context Protocol" arXiv 2025.xxxxx

## Decision (N07 fills)

- [ ] Build now
- [ ] Wait for stabilization
- [ ] Merge into existing kind: ___
- [ ] Reject — reason: ___
```

---

## C. Assimilation Protocol

### C.1 Weekly Review Gate

N07 reviews `.cex/runtime/taxonomy_candidates/` every Monday.

Review checklist per candidate:
1. Does a similar kind already exist with a different name? (check boundary field)
2. Is the upstream spec stable enough to base a CEX kind on?
3. Which pillar does it belong to?
4. How many builders would need updating if this kind is added?
5. Is there an existing kind that should be expanded vs creating a new one?

### C.2 Decision Outcomes

| Decision | Action | Who |
|----------|--------|-----|
| Build now | Auto-generate N03 handoff | N07 -> N03 |
| Wait | Update candidate: `status: watching`, set `review_after` date | N07 |
| Merge into existing | Add alias to existing kind's boundary, update description | N04 |
| Reject | Move to `.cex/runtime/taxonomy_candidates/rejected/`, add reason | N07 |

### C.3 Auto-Generated N03 Handoff Template

When decision = "build now":

```markdown
---
mission: TAXONOMY_EXPAND
nucleus: n03
kind: {{candidate_id}}
created: {{date}}
---
# N03 -- Build Kind: {{candidate_id}}

## Upstream
Source: {{upstream_url}}
Spec version: {{spec_version}}

## Deliverables
1. archetypes/builders/{{candidate_id}}-builder/ (13 ISOs)
2. P01_knowledge/library/kind/kc_{{candidate_id}}.md
3. Add to .cex/kinds_meta.json

## Context
Candidate file: .cex/runtime/taxonomy_candidates/{{candidate_file}}

## Commit
git commit -m "[N03] TAXONOMY_EXPAND: add {{candidate_id}} builder"
```

---

## D. Deprecation Protocol

### D.1 Deprecation Triggers

A kind enters `deprecated` status when ANY of:
- Upstream spec explicitly superseded (successor published >= 6 months ago)
- CEX has a newer kind that fully covers the deprecated one
- No compiled artifacts referencing this kind in 180 days
- Upstream repo archived with no active fork

### D.2 Deprecation Workflow

```
1. Set status: deprecated in kinds_meta.json
2. Set deprecated_by: <successor_kind>
3. Create migration file:
   N04_knowledge/migrations/deprecation_{kind}_{date}.md
4. Update all builders that reference deprecated kind
5. Announce in .cex/runtime/signals/ with signal type: deprecation_notice
6. After 90 days: status -> archived
```

### D.3 Migration File Format

```yaml
---
kind: legacy_kind_name
deprecated_by: new_kind_name
deprecated_since: 2026-04-14
archived_after: 2026-07-14
reason: "Upstream MCP v2 superseded this with native support"
---

## Migration Guide

Replace `legacy_kind_name` with `new_kind_name`.

Field mapping:
| Old field | New field | Notes |
|-----------|-----------|-------|
| foo | bar | Same semantics |
| baz | qux | Renamed for clarity |

Auto-migration script:
  python _tools/cex_migrate.py --from legacy_kind_name --to new_kind_name
```

### D.4 Archived Kind Policy

Archived kinds are:
- Removed from `kinds_meta.json` active section -> moved to `.cex/kinds_archive.json`
- Builders preserved in `archetypes/builders/_archived/` (git history)
- Not built by scout; not available in builder sub-agents
- Accessible via `cex_query.py --include-archived`

---

## E. Versioning Strategy

### E.1 Kind Versioning vs Spec Versioning

Two orthogonal version axes:

| Axis | Field | Example | Meaning |
|------|-------|---------|---------|
| Kind version | `version` in frontmatter | 1.0.0 -> 1.1.0 | CEX builder improvement |
| Spec version | `spec_version` in kinds_meta.json | 0.9.0 -> 1.0.0 | Upstream protocol version |

### E.2 Coexisting Versions

When a protocol releases a BREAKING v2:

```json
"mcp_server": {
  "spec_version": "1.0.0",
  "status": "stable"
},
"mcp_server_v2": {
  "spec_version": "2.0.0",
  "status": "draft",
  "deprecated_by": null,
  "upstream_source": "https://github.com/modelcontextprotocol/modelcontextprotocol"
}
```

Both kinds coexist until v2 reaches `stable` (>= 6 months, 2+ implementations).
Then v1 enters `deprecated` with `deprecated_by: mcp_server_v2`.

### E.3 Semver Interpretation for Specs

| Spec change | CEX action | Risk |
|-------------|------------|------|
| Patch (0.0.x) | Update `spec_version`, no builder change | Low |
| Minor (0.x.0) | Review boundary fields, may need KC update | Medium |
| Major (x.0.0) | Assess: new kind vs update existing, migration needed | High |

### E.4 Spec Version Tracking

kinds_meta.json stores `spec_version` as a semver string.
Scout compares against last-known version at each run.
Diff surfaced in candidate file under "## Version Delta" section.

---

## F. Metrics (Taxonomy Health)

### F.1 Coverage Metric

```
coverage = |CEX active kinds| / |industry candidate pool|
```

Industry candidate pool = all candidates with score >= 6.0 (reviewed or not).
Target: coverage >= 85%.

### F.2 Freshness Metric

```
freshness_days = today - last_reviewed (per kind)
```

Thresholds:
- Green: < 90 days
- Yellow: 90-180 days
- Red: > 180 days (triggers auto-candidate for re-review)

### F.3 Deprecation Pipeline Depth

```
pipeline_depth = count of kinds in status: deprecated
```

Target: < 10 kinds in deprecated at any time.
If > 20: trigger N04 deprecation sweep.

### F.4 Scout Cycle Health

Tracked per scout run in `.cex/runtime/taxonomy_candidates/scout_log.tsv`:

```tsv
run_date	source	candidates_found	candidates_new	candidates_merged	candidates_rejected	errors
2026-04-21	github	12	3	2	1	0
2026-04-21	arxiv	8	1	0	3	0
```

### F.5 Health Dashboard Command

```bash
python _tools/cex_taxonomy_scout.py --report
```

Output:
```
=== CEX Taxonomy Health ===
Active kinds:        238 / 280 candidates (85.0% coverage) [GREEN]
Stale kinds (>180d):   4 [YELLOW]
Deprecated kinds:      2 [GREEN]
Archived kinds:       11
Scout last run:   2026-04-21 (3 days ago) [GREEN]
Candidates pending:    3 (review recommended)
===========================
```

---

## G. Schema Extension (kinds_meta.json)

New fields added to every kind entry:

```json
{
  "action_paradigm": {
    "pillar": "P04",
    "llm_function": "CALL",
    "naming": "p04_act_{{name}}.md",
    "max_bytes": 4096,
    "core": false,
    "description": "How agents execute actions in environments",
    "boundary": "Action execution paradigm...",

    "status": "stable",
    "upstream_source": null,
    "spec_version": null,
    "last_reviewed": "2026-04-14",
    "deprecated_by": null
  }
}
```

| Field | Type | Values | Default |
|-------|------|--------|---------|
| status | enum | draft, stable, deprecated, archived | stable |
| upstream_source | string (URL) or null | canonical spec URL | null |
| spec_version | string (semver) or null | "1.0.0" | null |
| last_reviewed | string (ISO date) | "2026-04-14" | today |
| deprecated_by | string (kind name) or null | "new_kind_name" | null |

---

## G2. Source Harvest System

### G2.1 Overview

The Source Harvest System (`cex_source_harvester.py`) is the INPUT layer
of the taxonomy pipeline. It scans the CEX repo itself for external references
and merges them into `taxonomy_sources.yaml` as watchable feeds.

This closes the loop: as N01/N02/N04 produce research artifacts that cite
new sources, the harvester automatically discovers those sources and adds
them to the scout's watch list -- without any manual curation.

### G2.2 What Gets Harvested

The harvester scans these repo directories:

| Directory | Pattern | What it finds |
|-----------|---------|---------------|
| `N01_intelligence/research/` | `**/*.md` | Research KC URLs, arXiv, standards refs |
| `P01_knowledge/library/` | `**/*.md` | Knowledge card citations |
| `_docs/specs/` | `**/*.md` | Spec upstream references |
| `archetypes/builders/` | `**/bld_knowledge_card_*.md` | Builder KC links |
| `.claude/rules/` | `*.md` | Industry term references |
| `.` | `CLAUDE.md` | Root pointers |

### G2.3 Reference Types Extracted

| Type | Pattern | Example |
|------|---------|---------|
| URL | `https?://...` | `https://a2a-protocol.org/latest/specification` |
| GitHub slug | `github.com/org/repo` | `github.com/google-a2a/A2A` |
| W3C TR | `w3.org/TR/...` | `w3.org/TR/vc-data-model-2.0` |
| IETF draft | `datatracker.ietf.org/doc/...` | `datatracker.ietf.org/doc/draft-narajala-ans` |
| ISO standard | `ISO/IEC NNNNN` | `ISO/IEC 42001` |
| IEEE standard | `IEEE PNNNN` | `IEEE P3119` |
| NIST resource | `NIST AI/SP NNN` | `NIST AI 100-1` |
| HuggingFace | `huggingface.co/org/repo` | `huggingface.co/huggingface/transformers` |

arXiv IDs, DOIs, and RFC numbers are detected but classified as
individual citations (not feed sources) and excluded from watch entries.

URLs matching CDN/tracking/social domains are automatically skipped.

### G2.4 Deduplication Strategy

Before adding a new entry, the harvester:

1. **Canonical URL check**: normalize URL (strip trailing `/`, fragments,
   tracking params, lowercase domain) and check against existing entries
2. **Fuzzy domain match**: for URLs with the same domain, compute Levenshtein
   distance against existing entries (threshold: 10 chars)
3. **Skip list**: CDNs, badge services, social media, package registries
   are excluded regardless of where they appear

Entries that pass all 3 checks are added to the `harvested:` section.

### G2.5 Output Format (per entry)

```yaml
harvested:
  - name: google-a2a-a2a
    type: github
    url: https://github.com/google-a2a/A2A
    watch_paths: []
    extract_patterns: []
    cadence: weekly
    priority: medium
    harvested_from: N01_intelligence/research/ai2ai_exhaustive_scan_20260414.md
    last_checked: 2026-04-14
    status: active
```

Fields set by harvester (default values, refine manually):
- `watch_paths: []` -- add specific paths for targeted scanning
- `extract_patterns: []` -- add regex patterns for kind extraction
- `cadence: weekly|biweekly|monthly` -- inferred from source type
- `priority: critical|high|medium|low` -- inferred from source type

### G2.6 CLI Reference

```bash
# Preview new entries without writing
python _tools/cex_source_harvester.py --dry-run

# Apply new entries to taxonomy_sources.yaml
python _tools/cex_source_harvester.py --apply

# Show breakdown by source type
python _tools/cex_source_harvester.py --stats

# Verbose: print each new entry as found
python _tools/cex_source_harvester.py --apply --verbose

# Called by scout (harvest-then-scan)
python _tools/cex_source_harvester.py --harvest-first
```

### G2.7 Integration with Scout

The scout accepts `--harvest-first` which runs the harvester before scanning:

```bash
python _tools/cex_taxonomy_scout.py --harvest-first --source all --since 7
```

This ensures the scout always operates on the most complete source list,
including any sources cited in recently-added research artifacts.

### G2.8 Cadence Recommendations by Source Type

| Source type | Default cadence | Rationale |
|-------------|----------------|-----------|
| github | weekly | Spec repos ship fast; weekly catches new objects |
| arxiv | weekly | New papers every week |
| w3c | monthly | W3C specs move slowly through chartered WGs |
| ietf | monthly | IETF drafts have 6-month revision cycles |
| iso | quarterly | ISO standards take years; quarterly is sufficient |
| ieee | monthly | IEEE SAs publish at irregular pace |
| nist | monthly | NIST AI resources update ~quarterly |
| website | monthly | General docs; less frequent change |
| community | daily/weekly | HN/PH signal fast-moving trends |

### G2.9 Adding Sources Manually

To add a new source not discovered by the harvester:

1. Edit `.cex/config/taxonomy_sources.yaml` directly
2. Add your entry in the correct section (or in `harvested:`)
3. Set `harvested_from: manual` and `last_checked: <today>`
4. Re-run scout:
   ```bash
   python _tools/cex_taxonomy_scout.py --source github --since 30 --dry-run
   ```

The harvester will NOT overwrite manually-added entries -- it only appends
new entries to the `harvested:` block. Existing entries in all sections
are preserved via URL canonical-dedup.

---

## H. Integration with CEX Runtime

### H.1 File Locations

```
.cex/
  config/
    taxonomy_sources.yaml         # source watcher config
  runtime/
    taxonomy_candidates/
      YYYY-MM-DD_*.md             # candidate files (pending review)
      rejected/                   # rejected candidates
      applied/                    # assimilated candidates
      scout_log.tsv               # run history
  kinds_archive.json              # archived kinds (removed from active)
```

### H.2 Cron Integration

Add to `.cex/config/schedules.yaml`:

```yaml
- id: taxonomy_scout_weekly
  command: "python _tools/cex_taxonomy_scout.py --source all --since 7"
  schedule: "0 2 * * 1"  # Monday 02:00 UTC
  notify: n07

- id: taxonomy_scout_daily_github
  command: "python _tools/cex_taxonomy_scout.py --source github --since 1 --dry-run"
  schedule: "0 6 * * *"  # Daily 06:00 UTC
  notify: n07
```

### H.3 Signal Integration

On scout completion (score >= threshold):

```python
from _tools.signal_writer import write_signal
write_signal('n04', 'taxonomy_candidate_ready', score, metadata={
    'candidates': 3,
    'top_score': 8.4,
    'top_candidate': 'tool_invocation_protocol'
})
```

N07 polls `.cex/runtime/signals/` and sees the notification.

---

## I. Operational Runbook

### I.1 Add a new source manually

```bash
# 1. Add entry to .cex/config/taxonomy_sources.yaml
# 2. Run scout for that source only
python _tools/cex_taxonomy_scout.py --source github --repo new-org/new-repo --since 30

# 3. Review candidates
ls .cex/runtime/taxonomy_candidates/

# 4. N07 makes decisions
```

### I.2 Force re-review of all kinds

```bash
python _tools/cex_taxonomy_scout.py --recheck-all --since 180
```

Marks kinds with last_reviewed > 180 days as needing review.
Writes stale-review candidates for N07.

### I.3 Emergency deprecation

```bash
# Immediately deprecate a kind and point to successor
python _tools/cex_taxonomy_scout.py --deprecate kind_name --successor new_kind
```

Writes deprecation record, updates kinds_meta.json, creates migration file.

### I.4 Scout dry-run (no writes)

```bash
python _tools/cex_taxonomy_scout.py --source all --since 7 --dry-run
```

Prints candidates to stdout without writing files. Safe for testing.

---

## Properties

| Property | Value |
|----------|-------|
| Kind | context_doc |
| Pillar | P01 |
| Domain | taxonomy lifecycle |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_23_multiagent_protocols]] | related | 0.24 |
| [[kc_llm_vocabulary_atlas]] | related | 0.22 |
| [[taxonomy_completeness_audit]] | related | 0.21 |
| [[cex_llm_vocabulary_whitepaper]] | related | 0.21 |
| [[ai2ai_coverage_matrix_20260414]] | related | 0.20 |
| [[p01_kc_terminology_rosetta_stone]] | related | 0.20 |
| [[bld_collaboration_handoff_protocol]] | downstream | 0.18 |
| [[bld_tools_model_card]] | downstream | 0.18 |
| [[n07_memory_industry_audit]] | downstream | 0.18 |
| [[ai2ai_exhaustive_scan_20260414]] | related | 0.17 |
