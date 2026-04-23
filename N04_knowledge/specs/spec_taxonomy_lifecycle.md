---
id: spec_taxonomy_lifecycle
kind: context_doc
pillar: P01
nucleus: N04
domain: taxonomy-lifecycle
version: 1.0.0
status: stable
created: 2026-04-19
quality: 8.5
tags: [taxonomy, lifecycle, scout, assimilation, deprecation, versioning]
related:
  - atom_23_multiagent_protocols
  - cex_llm_vocabulary_whitepaper
  - bld_collaboration_handoff_protocol
  - bld_knowledge_card_capability_registry
  - kc_llm_vocabulary_atlas
  - p01_kc_terminology_rosetta_stone
  - taxonomy_completeness_audit
  - ai2ai_coverage_matrix_20260414
  - n07_memory_industry_audit
  - bld_tools_capability_registry
density_score: 1.0
updated: "2026-04-22"
---

# CEX Taxonomy Non-Aging Lifecycle System

## Purpose

CEX operates on 293 typed kinds. Without active stewardship, this taxonomy
becomes stale within 12-18 months as new AI2AI protocols, schema standards,
and agent interoperability specs emerge. This document specifies the automated
lifecycle system that keeps CEX kinds synchronized with the industry.

**The core invariant:** every kind in CEX must map to at least one active
upstream source (spec, protocol, paper, or standard). Kinds without upstream
traceability are candidates for review or deprecation.

---

## Architecture Overview

```
[External Sources] --> [Scout Layer] --> [Candidate Pool] --> [Review Gate] --> [Assimilation]
                                                                    |
                                                              [Deprecation]
                                                                    |
                                                              [kinds_meta.json]
```

The lifecycle has five subsystems:

1. **Sources Feed** -- watchers for 8 source categories (Section A)
2. **Discovery Protocol** -- weekly `cex_taxonomy_scout.py` run (Section B)
3. **Assimilation Protocol** -- human-gated N07 review (Section C)
4. **Deprecation Protocol** -- kinds aging out of relevance (Section D)
5. **Versioning Strategy** -- multi-version coexistence for evolving specs (Section E)
6. **Metrics** -- taxonomy health dashboard (Section F)

---

## A. Sources Feed (Auto-Watchers)

### A1. GitHub Protocol Repos (Priority: CRITICAL)

| Repo | Watch Paths | Extract Pattern | Cadence |
|------|-------------|----------------|---------|
| google-a2a/A2A | spec/, drafts/ | `"type": "[A-Z]` | weekly |
| modelcontextprotocol/modelcontextprotocol | schema/, spec/ | `interface [A-Z]` | weekly |
| open-telemetry/semantic-conventions | model/metrics/, model/trace/ | `brief:` yaml keys | weekly |
| w3c/verifiable-credentials | index.html, core/ | `term:`, `@type:` | biweekly |
| sigstore/cosign | docs/specs/ | protocol markers | monthly |
| c2pa-org/c2pa-spec | specs/, docs/ | manifest schema keys | monthly |
| huggingface/hub-docs | docs/hub/ | card schema keys | biweekly |
| openai/openai-openapi | openai.yaml | `components/schemas` | biweekly |
| anthropics/anthropic-sdk-python | anthropic/types/ | TypedDict defs | biweekly |
| anyscale/ray | doc/source/serve/ | deployment patterns | monthly |

### A2. arXiv Daily Feed (Priority: HIGH)

Categories: `cs.AI`, `cs.MA`, `cs.CL`, `cs.NI`

Keyword triggers (title/abstract):
- "protocol", "schema", "interoperability", "agent-to-agent"
- "multi-agent", "tool use", "function calling", "capability"
- "knowledge graph", "ontology", "taxonomy"
- "evaluation framework", "benchmark", "alignment"
- "memory", "context", "retrieval", "RAG"

Signal threshold: 3+ keyword hits in abstract = candidate extraction.

### A3. Standards Bodies (Priority: HIGH)

| Body | Source | Cadence | Notes |
|------|--------|---------|-------|
| IETF | datatracker.ietf.org/doc/search/?states=active | biweekly | Filter: AI, ML, agents in title |
| ISO/IEC JTC 1/SC 42 | iso.org/committee/6794475 | monthly | Public WDs only |
| IEEE SA | standards.ieee.org/search/?q=AI | monthly | P-drafts only |
| W3C | w3.org/TR/?status=WD&status=CR | biweekly | AI/data CGs |
| NIST | csrc.nist.gov/publications | monthly | AI RMF updates |
| EU AI Act | eur-lex.europa.eu | monthly | Technical standards |

### A4. Vendor Protocol Announcements (Priority: MEDIUM)

Sources: HackerNews (Show HN, Ask HN), Product Hunt (AI category),
AWS re:Invent/Google Next/Microsoft Build release notes.

Trigger: posts with title matching: agent, MCP, protocol, schema, interoperability,
standard, specification.

Recency filter: posts from last 7 days with > 50 points.

### A5. Conference System Papers (Priority: MEDIUM)

| Conference | Track | Cadence |
|------------|-------|---------|
| NeurIPS | Systems and Benchmarks | annually (Dec) |
| ICML | Systems | annually (Jul) |
| EMNLP | System Demonstrations | annually (Nov) |
| ACL | Demo Track | annually (Jul) |
| ICLR | Reproducibility | annually (May) |
| SysML/MLSys | All tracks | annually (Mar) |

---

## B. Discovery Protocol (Weekly Scout Cycle)

### B1. cex_taxonomy_scout.py Schedule

```
Every Monday 08:00 UTC:
  1. Pull diffs from all active watchers (since last run)
  2. Extract candidate kind names via NER + schema heuristics
  3. Dedupe against existing 293 kinds (embedding similarity > 0.85 = skip)
  4. Score each candidate: adoption + stability + urgency
  5. Write .cex/runtime/taxonomy_candidates/YYYY-MM-DD_{source}_{slug}.md
  6. Signal N07 if any candidate scores >= 7.0
```

### B2. Candidate Extraction Heuristics

From GitHub diffs:
- New TypeScript `interface` or `type` with 3+ fields -> candidate
- New JSON Schema `$defs` entry with `title` -> candidate
- New YAML `components/schemas` block -> candidate
- New Protobuf `message` with `repeated` or nested fields -> candidate

From arXiv abstracts:
- Capitalized noun phrases preceded by "introduce", "define", "propose" -> candidate
- Section titles matching `^\d+\.\s+[A-Z][a-z]+ [A-Z][a-z]+` -> candidate

From standards:
- New normative `shall` requirements with concrete noun subject -> candidate
- New annex titles -> candidate

### B3. Candidate Scoring Formula

```
score = (adoption * 0.4) + (stability * 0.3) + (urgency * 0.2) + (relevance * 0.1)

adoption:  0-10  (GitHub stars, paper citations, vendor support count)
stability: 0-10  (spec version >= 1.0 = 10; RC = 7; alpha = 3; informal = 1)
urgency:   0-10  (3 competitors adopted = 10; 1 = 5; none = 0)
relevance: 0-10  (pillar match: P01-P12 coverage gap = 10; fully covered = 0)
```

Thresholds:
- score >= 8.0: **auto-flag** to N07 for immediate review
- score 6.0-7.9: **queue** for weekly review batch
- score < 6.0: **archive** in `.cex/runtime/taxonomy_candidates/low/`

### B4. Candidate File Schema

```markdown
---
candidate_id: {source}_{slug}_{date}
source: github|arxiv|ietf|w3c|ieee|iso|vendor|conference
source_url: https://...
extracted_date: YYYY-MM-DD
suggested_kind: snake_case_name
suggested_pillar: P01-P12
score: 0.0-10.0
adoption: 0-10
stability: 0-10
urgency: 0-10
relevance: 0-10
status: pending|approved|rejected|merged
decision_date: null
decision_by: n07
notes: ""
---

# Candidate: {suggested_kind}

## Source Evidence
{snippet from source that triggered extraction}

## Existing Kind Overlap
Closest existing kind: {kind} ({similarity}% similar)
Distinction: {how this differs}

## Suggested Definition
{1-2 sentence definition in CEX style}

## Suggested Boundary
NOT {closest_existing_kind} ({distinction}).
```

---

## C. Assimilation Protocol

### C1. N07 Weekly Review Gate

Every Monday afternoon (after scout runs), N07 reviews the candidate batch:

```
READ .cex/runtime/taxonomy_candidates/*.md
FOR EACH candidate:
  DECISION: build | wait | merge | reject
  WRITE decision to candidate file
  IF build:
    WRITE handoff to .cex/runtime/handoffs/n03_task.md
    DISPATCH N03 to build kind (builder + ISOs + kc + archetype + subagent + meta)
  IF merge:
    UPDATE existing kind in kinds_meta.json with new upstream_source
  IF reject:
    MOVE to .cex/runtime/taxonomy_candidates/rejected/
  IF wait:
    SET next_review_date (default: +30 days)
```

### C2. Build Decision Criteria

| Situation | Decision |
|-----------|----------|
| New protocol with stable spec (>= v1.0), adopted by 3+ vendors | build now |
| Protocol in RC/beta, 1-2 vendors | wait (30d) |
| Similar to existing kind, minor variation | merge (update upstream_source) |
| Informal blog post, no spec | reject |
| Standard body draft, no implementations | wait (90d) |
| Academic paper only, no adoption | reject (add to watchlist) |

### C3. New Kind Build Checklist (dispatched to N03)

When N07 approves a candidate for build, N03 must create:
1. `kinds_meta.json` entry (status: draft, spec_version, upstream_source)
2. `archetypes/builders/{kind}-builder/` -- 13 ISOs
3. `N00_genesis/P01_knowledge/library/kind/kc_{kind}.md`
4. `N00_genesis/P{pillar}/{schema_dir}/tpl_{kind}.md`
5. `.claude/agents/{kind}-builder.md`
6. `_schema.yaml` update for target pillar
7. `kind_index.md` update for target pillar
8. Compile: `python _tools/cex_compile.py`
9. Verify: `python _tools/cex_doctor.py`

---

## D. Deprecation Protocol

### D1. Deprecation Triggers

A kind enters deprecation review when ANY of the following:

| Trigger | Threshold | Action |
|---------|-----------|--------|
| Upstream spec frozen + no activity | 180 days | flag for review |
| Successor kind exists | status = stable | auto-deprecate (if no compiled artifacts) |
| No compiled artifacts in nucleus | 180 days | flag for review |
| Standard body withdraws spec | immediate | deprecate |
| Vendor abandons protocol | 1 year no commits | flag for review |
| Merged into larger kind | after merge confirmed | archive |

### D2. Deprecation States

```
draft -> stable -> deprecated -> archived
              |                      ^
              +----> deprecated -----+
```

| Status | Meaning | Behavior |
|--------|---------|----------|
| draft | New kind, spec not stable | Builds OK, not recommended for production |
| stable | Spec >= v1.0, adopted | Normal build target |
| deprecated | Superseded or abandoned | Builder exists, new builds warned |
| archived | No builder maintained | Builder removed from active index |

### D3. Deprecated Kind Fields

```json
{
  "status": "deprecated",
  "deprecated_by": "new_kind_name",
  "spec_version": "1.2.0",
  "last_reviewed": "2026-04-19",
  "upstream_source": "https://..."
}
```

### D4. Successor Migration

When a kind is deprecated with a successor:
1. Update `kinds_meta.json`: `deprecated_by: successor_kind`
2. Update kind's KC: add deprecation notice + migration guide
3. Update kind's builder manifest: add `DEPRECATED` header
4. Create migration KC: `kc_{old_kind}_to_{new_kind}_migration.md`
5. Keep builder in repo for 6 months (backwards compatibility)
6. After 6 months: move to `archetypes/deprecated/`

---

## E. Versioning Strategy

### E1. Protocol Evolution

Major AI2AI protocols (MCP, A2A, OTel) will have v2, v3+. CEX handles this via:

**Multi-version coexistence**: kinds can have version suffixes when major
spec revisions introduce breaking changes.

Example:
```
mcp_server        -- v1.x spec (current stable)
mcp_server_v2     -- v2.0 spec (when released, incompatible)
```

Both kinds remain active until mcp_server is deprecated_by mcp_server_v2.

### E2. Version Fields in kinds_meta.json

```json
{
  "spec_version": "1.2.0",
  "upstream_source": "https://spec.modelcontextprotocol.io/specification/2025-03-26/",
  "last_reviewed": "2026-04-19",
  "status": "stable"
}
```

`spec_version` tracks the UPSTREAM spec version, not the CEX builder version.
CEX builder versioning is implicit in git history.

### E3. Minor vs Major Version Policy

| Change type | Action |
|-------------|--------|
| Minor spec update (new optional fields) | Update existing kind + spec_version |
| New required fields added | Update existing kind + bump spec_version |
| Breaking schema change | Create new kind with _v{N} suffix |
| Spec split (one spec becomes two) | Two new kinds, original deprecated |
| Spec merge (two specs become one) | New merged kind, two deprecated |

---

## F. Taxonomy Health Metrics

### F1. Health Dashboard (cex_taxonomy_scout.py --health)

| Metric | Formula | Target | Warning |
|--------|---------|--------|---------|
| Coverage % | CEX kinds / candidate pool size | >= 80% | < 70% |
| Freshness | Avg days since last_reviewed | <= 90 days | > 180 days |
| Stale kinds | kinds with last_reviewed > 365d | 0 | > 5 |
| Draft backlog | kinds with status=draft > 30d | 0 | > 3 |
| Deprecated backlog | deprecated kinds not yet archived | 0 | > 5 |
| Scout health | days since last successful scout run | <= 8 | > 14 |
| Candidate queue | pending candidates unreviewed | <= 5 | > 15 |

### F2. Health Report Format

Generated weekly by `cex_taxonomy_scout.py --health`:

```
=== TAXONOMY HEALTH REPORT ===
Date: YYYY-MM-DD
Total kinds: 293
  status=stable:     285 (97.3%)
  status=draft:        4 ( 1.4%)
  status=deprecated:   2 ( 0.7%)
  status=archived:     2 ( 0.7%)

Freshness:
  Reviewed in last 30d:   48 kinds
  Reviewed in last 90d:  241 kinds
  Reviewed in last 180d: 288 kinds
  Stale (>365d):           0 kinds [OK]

Candidate queue: 3 pending (0 critical, 3 normal)
Scout last run: 2026-04-14 (5 days ago) [OK]

Coverage estimate:
  Known protocol space: ~350 kinds
  CEX coverage: 293/350 = 83.7% [OK]

Action items:
  - Review 3 pending candidates
  - Update spec_version for mcp_server (MCP 2025-03-26 released)
==============================
```

### F3. Alert Conditions

Conditions that trigger N07 immediate signal:
- Critical candidate (score >= 8.0) discovered
- Scout run fails for 3+ consecutive days
- Stale kind count exceeds 10
- Deprecated backlog exceeds 10 (builder cleanup needed)

---

## G. Implementation Roadmap

| Phase | Deliverable | Owner | Timeline |
|-------|-------------|-------|----------|
| G1 | spec_taxonomy_lifecycle.md (this doc) | N04 | Day 1 |
| G2 | taxonomy_sources.yaml (30 sources) | N04 | Day 1 |
| G3 | cex_taxonomy_scout.py (GitHub + arXiv) | N04 | Day 1 |
| G4 | kinds_meta.json lifecycle fields backfill | N04 | Day 1 |
| G5 | Scout cron schedule (weekly Monday) | N05 | Week 2 |
| G6 | N07 review workflow integration | N07 | Week 2 |
| G7 | Remaining source adapters (IETF, W3C) | N04 | Month 1 |
| G8 | Embedding-based dedupe (vs TF-IDF) | N04 | Month 1 |
| G9 | Health dashboard CLI | N04 | Month 1 |

---

## H. Integration Points

### H1. File Locations

| Artifact | Path |
|----------|------|
| This spec | `N04_knowledge/specs/spec_taxonomy_lifecycle.md` |
| Scout tool | `_tools/cex_taxonomy_scout.py` |
| Source config | `.cex/P09_config/taxonomy_sources.yaml` |
| Kind registry | `.cex/kinds_meta.json` |
| Candidate pool | `.cex/runtime/taxonomy_candidates/` |
| Scout state | `.cex/runtime/taxonomy_candidates/.scout_state.json` |
| Health reports | `.cex/runtime/taxonomy_candidates/health/` |

### H2. 8F Integration

Scout runs are not 8F pipeline runs -- they are infrastructure tasks.
However, assimilation of a new kind DOES trigger a full 8F run (via N03).

Scout signal to N07:
```python
write_signal('n04', 'taxonomy_candidate', score, {
    'candidate_id': candidate_id,
    'suggested_kind': kind_name,
    'suggested_pillar': pillar,
    'score': score,
    'source': source_type,
})
```

### H3. kinds_meta.json Lifecycle Fields

All 293 existing kinds already have these fields (backfilled 2026-04-19):

```json
{
  "status": "stable",          // draft|stable|deprecated|archived
  "upstream_source": null,     // URL or null
  "spec_version": null,        // semver or null
  "last_reviewed": "2026-04-14",
  "deprecated_by": null        // kind_name or null
}
```

New kinds added via assimilation MUST populate `upstream_source` and `spec_version`.

---

## Properties

| Property | Value |
|----------|-------|
| Kind | context_doc |
| Pillar | P01 |
| Nucleus | N04 |
| Domain | taxonomy-lifecycle |
| Pipeline | 8F |
| Version | 1.0.0 |
| Quality target | 9.0+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_23_multiagent_protocols]] | related | 0.22 |
| [[cex_llm_vocabulary_whitepaper]] | related | 0.22 |
| [[bld_collaboration_handoff_protocol]] | downstream | 0.21 |
| [[bld_knowledge_card_capability_registry]] | related | 0.20 |
| [[kc_llm_vocabulary_atlas]] | related | 0.20 |
| [[p01_kc_terminology_rosetta_stone]] | related | 0.19 |
| [[taxonomy_completeness_audit]] | related | 0.19 |
| [[ai2ai_coverage_matrix_20260414]] | related | 0.19 |
| [[n07_memory_industry_audit]] | downstream | 0.18 |
| [[bld_tools_capability_registry]] | downstream | 0.18 |
