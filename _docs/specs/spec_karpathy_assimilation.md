---
id: spec_karpathy_assimilation
kind: context_doc
pillar: P01
title: "Spec: Karpathy Assimilation -- autoresearch + LLM Wiki + Obsidian Vault"
version: 1.0.0
quality: 8.7
tags: [karpathy, autoresearch, llm-wiki, obsidian, cross-reference, wiring]
created: "2026-04-20"
updated: "2026-04-20"
author: n07_orchestrator
tldr: "Wire cross-references into every artifact (schema + builder + existing), add Obsidian vault layer, upgrade autoresearch loop with diff tracking. One final repo-wide modification to make knowledge compound."
density_score: 0.92
---

# Spec: Karpathy Assimilation

## Thesis

CEX is already the most structured LLM Wiki in existence (300 kinds, 424 KCs,
12 pillar schemas, 8F editorial pipeline). CEX already has the autoresearch loop
(`cex_evolve.py` = modify -> score -> keep/discard). What's missing is the GRAPH --
artifacts don't link to each other. Knowledge accumulates but doesn't compound.

This spec wires cross-references into every layer of CEX:
1. **Schema layer** -- add `related:` to all 12 pillar schemas
2. **Builder layer** -- add `## Related Artifacts` to all 298 builder ISOs
3. **Existing artifacts** -- one-time sweep to populate `related:` in 2000+ files
4. **Obsidian layer** -- vault config + dashboards + graph view (DONE)
5. **Tool layer** -- `cex_ripple.py` propagates changes to related artifacts
6. **Evolve layer** -- upgrade overnight loop with diff tracking + cluster mode

After this, every artifact knows its neighbors. Every change ripples. Obsidian
shows the graph. The 8F pipeline enforces it on production. One final repo-wide
modification, then the system is fully wired.

## Sources

| Source | What it contributes |
|--------|-------------------|
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | Overnight experiment loop: modify -> train 5min -> eval metric -> keep/discard |
| [karpathy/LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Ingest -> summarize -> update 10-15 related pages -> query -> lint |
| CEX cex_evolve.py | Already implements keep/discard loop for artifacts |
| CEX cex_retriever.py | TF-IDF similarity (2184 docs, 12K vocab) -- finds related artifacts |
| CEX P01 _schema.yaml | Already has `linked_artifacts: {primary, related}` (P01 only) |
| CEX P02 _schema.yaml | Already has `related_agents` (P02 only) |

## Architecture

```
LAYER 1: SCHEMA (modify once, enforced forever)
  All 12 _schema.yaml files get: related: [list of artifact IDs]
  All 298 bld_schema_*.md get: related field documentation
  Shared skill: skill_cross_reference.md (HOW to populate related)

LAYER 2: BUILDER (templates produce cross-refs automatically)
  All 298 bld_prompt_*.md get: ## Related Artifacts section in output template
  All 298 bld_eval_*.md get: cross-ref gate (SOFT -- warn if empty)
  New: archetypes/builders/_shared/skill_cross_reference.md

LAYER 3: EXISTING ARTIFACTS (one-time sweep)
  cex_wikilink.py: scan 2000+ .md files, use cex_retriever.py to find
  top-10 similar per artifact, populate related: frontmatter + [[wikilinks]]

LAYER 4: OBSIDIAN VAULT (human navigation)
  .obsidian/ config: DONE (app.json, graph.json, community-plugins, dataview)
  _dashboards/: DONE (quality_heatmap, kind_census, orphan_detector, pillar_health)
  Graph View: colored by nucleus, edges from [[wikilinks]]

LAYER 5: RIPPLE ENGINE (knowledge compounds)
  cex_ripple.py: on artifact save, find 10-15 related, patch cross-refs
  cex_semantic_lint.py: detect contradictions, stale claims, broken links

LAYER 6: AUTORESEARCH UPGRADE (overnight learning)
  cex_evolve.py --cluster: evolve related artifacts atomically
  cex_evolve.py --diff-log: track hypothesis + diff + quality delta
  cex_experiment_analytics.py: aggregate results.tsv into trends
```

## Wave Plan

### Wave 0: Obsidian Vault (DONE)

| # | Artifact | Path | Status |
|---|----------|------|--------|
| 0.1 | Obsidian app config | .obsidian/app.json | DONE |
| 0.2 | Graph color config | .obsidian/graph.json | DONE |
| 0.3 | Community plugins | .obsidian/community-plugins.json | DONE |
| 0.4 | Core plugins | .obsidian/core-plugins.json | DONE |
| 0.5 | Dataview config | .obsidian/plugins/dataview/data.json | DONE |
| 0.6 | Quality heatmap dashboard | _dashboards/quality_heatmap.md | DONE |
| 0.7 | Kind census dashboard | _dashboards/kind_census.md | DONE |
| 0.8 | Orphan detector dashboard | _dashboards/orphan_detector.md | DONE |
| 0.9 | Pillar health dashboard | _dashboards/pillar_health.md | DONE |
| 0.10 | .gitignore selective tracking | .gitignore (obsidian section) | DONE |

### Wave 1: Schema Wiring (N03 solo -- modifies 12 schemas + 1 shared skill)

**Task**: Add `related:` field to all 12 pillar schemas + create shared cross-reference skill.

| # | Artifact | Path | Kind | Action |
|---|----------|------|------|--------|
| 1.1 | P01 schema | N00_genesis/P01_knowledge/_schema.yaml | schema | UPDATE -- already has linked_artifacts, normalize to `related:` |
| 1.2 | P02 schema | N00_genesis/P02_model/_schema.yaml | schema | UPDATE -- already has related_agents, add `related:` |
| 1.3 | P03 schema | N00_genesis/P03_prompt/_schema.yaml | schema | UPDATE -- add `related:` to frontmatter_cex |
| 1.4 | P04 schema | N00_genesis/P04_tools/_schema.yaml | schema | UPDATE -- add `related:` |
| 1.5 | P05 schema | N00_genesis/P05_output/_schema.yaml | schema | UPDATE -- add `related:` |
| 1.6 | P06 schema | N00_genesis/P06_schema/_schema.yaml | schema | UPDATE -- add `related:` |
| 1.7 | P07 schema | N00_genesis/P07_evals/_schema.yaml | schema | UPDATE -- add `related:` |
| 1.8 | P08 schema | N00_genesis/P08_architecture/_schema.yaml | schema | UPDATE -- add `related:` |
| 1.9 | P09 schema | N00_genesis/P09_config/_schema.yaml | schema | UPDATE -- add `related:` |
| 1.10 | P10 schema | N00_genesis/P10_memory/_schema.yaml | schema | UPDATE -- add `related:` |
| 1.11 | P11 schema | N00_genesis/P11_feedback/_schema.yaml | schema | UPDATE -- add `related:` |
| 1.12 | P12 schema | N00_genesis/P12_orchestration/_schema.yaml | schema | UPDATE -- add `related:` |
| 1.13 | Cross-ref skill | archetypes/builders/_shared/skill_cross_reference.md | skill | CREATE |

**Field specification** (universal across all pillars):
```yaml
# In frontmatter_cex section of every _schema.yaml:
related:
  type: list[string]
  required: recommended
  description: "Artifact IDs of related artifacts (upstream, downstream, sibling, alternative)"
  format: "[p{XX}_{kind}_{slug}, ...]"
  max: 15
  min: 0
  validator: S_RELATED
  note: "Auto-populated by cex_wikilink.py, manually curated by builders"
```

**Shared skill** (`skill_cross_reference.md`) teaches builders:
- WHEN to link: always (recommended, never empty for published artifacts)
- WHAT to link: upstream producers, downstream consumers, sibling variants, alternatives
- HOW to link: artifact ID in frontmatter `related:`, `[[wikilink]]` in body
- HOW MANY: 3-15 (target 8-10 for knowledge cards, 3-5 for config kinds)
- CATEGORIES: upstream | downstream | sibling | alternative | supersedes

### Wave 2: Builder ISO Wiring (N03 grid -- modifies 298 x 2 ISOs = 596 files)

**Task**: Add `## Related Artifacts` to output templates + cross-ref soft gate to eval ISOs.

This is the BIG change. 301 builders x 2 ISOs each (bld_prompt + bld_eval) = 596 file modifications.

**Approach**: Automated via Python script, NOT manual. N03 builds the script, runs it.

| # | Artifact | Action | Count |
|---|----------|--------|-------|
| 2.1 | bld_prompt_*.md (all builders) | APPEND `## Related Artifacts` section to OUTPUT_TEMPLATE | 298 files |
| 2.2 | bld_eval_*.md (all builders) | ADD soft gate S_RELATED: warn if `related:` is empty | 298 files |
| 2.3 | Wire script | _tools/cex_wire_cross_refs.py (one-time, runs Wave 2) | 1 file |

**Output template addition** (appended to every bld_prompt_*.md):
```markdown
## Related Artifacts

| Artifact | Relationship | Why |
|----------|-------------|-----|
| [[{artifact_id}]] | upstream / downstream / sibling / alternative | {one-line reason} |
```

**Eval gate addition** (appended to every bld_eval_*.md):
```markdown
### S_RELATED: Cross-Reference Check (SOFT)
- [ ] `related:` frontmatter field populated (3-15 entries)
- [ ] `## Related Artifacts` section present in body
- [ ] At least 1 upstream and 1 downstream reference
- Penalty: -0.3 if empty (does not block, encourages wiring)
```

### Wave 3: Existing Artifact Sweep (N03 + tool -- modifies 2000+ files)

**Task**: Build `cex_wikilink.py` and run it on the entire repo.

| # | Artifact | Path | Action |
|---|----------|------|--------|
| 3.1 | Wikilink engine | _tools/cex_wikilink.py | CREATE |
| 3.2 | Run sweep | `python _tools/cex_wikilink.py --sweep --dry-run` then `--apply` | EXECUTE |

**cex_wikilink.py specification:**

```
INPUT:  path to .md file (or --sweep for all)
PROCESS:
  1. Parse frontmatter (extract id, kind, pillar, tags)
  2. Run cex_retriever.py to find top-10 similar artifacts
  3. Filter: same-kind siblings, cross-pillar references, upstream/downstream
  4. Classify relationship: upstream | downstream | sibling | alternative
  5. Write to frontmatter: related: [id1, id2, ...]
  6. Write to body: ## Related Artifacts table with [[wikilinks]]
OUTPUT: modified .md file with cross-references
FLAGS:
  --sweep     Process all .md files in repo
  --dry-run   Show what would change, don't write
  --apply     Actually write changes
  --min-score 0.3  Minimum similarity threshold (default: 0.3)
  --max-refs  10   Maximum related refs per artifact (default: 10)
```

**Estimated impact**: ~2000 files modified with `related:` frontmatter + `## Related Artifacts` section.
This is the "modify the repo one last time" operation.

### Wave 4: Ripple Engine + Semantic Lint (N03 solo -- 2 new tools)

**Task**: Build the tools that MAINTAIN cross-references going forward.

| # | Artifact | Path | Kind | Size |
|---|----------|------|------|------|
| 4.1 | Ripple engine | _tools/cex_ripple.py | cli_tool | L |
| 4.2 | Semantic lint | _tools/cex_semantic_lint.py | cli_tool | L |

**cex_ripple.py specification:**

```
TRIGGER: called by post-tool-use hook after any artifact save
INPUT:   path to saved/modified artifact
PROCESS:
  1. Read modified artifact's related: field
  2. For each related artifact:
     a. Check if the modification affects the relationship
     b. If yes: update related artifact's cross-refs
     c. If the content contradicts: flag for semantic review
  3. For NEW relationships (not in related: yet):
     a. Run cex_retriever.py to find newly-relevant artifacts
     b. Add bidirectional cross-refs
OUTPUT:  list of modified files + ripple report
BUDGET:  max 15 files modified per ripple (prevent cascade)
```

**cex_semantic_lint.py specification:**

```
INPUT:  --sweep (all) or specific path
CHECKS:
  1. CONTRADICTION: two artifacts claim conflicting facts about same entity
  2. STALE: artifact references date/version older than 6 months
  3. ORPHAN: artifact has zero inlinks AND zero outlinks (after wikilink sweep)
  4. BROKEN_LINK: [[wikilink]] target doesn't exist
  5. CIRCULAR: A -> B -> C -> A (warn, not block)
  6. DENSITY: related: field has < 3 entries (below recommended minimum)
OUTPUT: report with severity (ERROR | WARN | INFO) per finding
```

### Wave 5: Autoresearch Upgrade (N03 solo -- 2 tool patches + 1 new tool)

**Task**: Upgrade the overnight evolution loop with Karpathy-style experiment tracking.

| # | Artifact | Path | Action |
|---|----------|------|--------|
| 5.1 | Cluster evolution | _tools/cex_evolve.py | PATCH -- add --cluster flag |
| 5.2 | Diff tracking | _tools/cex_evolve.py | PATCH -- add --diff-log flag |
| 5.3 | Experiment analytics | _tools/cex_experiment_analytics.py | CREATE |
| 5.4 | Overnight harness | _spawn/overnight_evolve.sh | PATCH -- add cluster + analytics |

**Cluster evolution spec:**
```
--cluster flag on cex_evolve.py:
  1. Take input artifact
  2. Read its related: field -> get cluster (max 5 neighbors)
  3. Git snapshot ALL cluster files
  4. Evolve primary artifact
  5. Run cex_ripple.py on cluster
  6. Score ALL cluster files
  7. If average quality improved: keep ALL
  8. If average quality dropped: discard ALL (git restore)
  9. Log: cluster_size, individual_deltas, aggregate_delta
```

**Diff tracking spec:**
```
--diff-log flag on cex_evolve.py:
  For each evolution round, log to .cex/experiments/diff_log.jsonl:
  {
    "timestamp": "ISO-8601",
    "filepath": "path",
    "round": N,
    "hypothesis": "what we tried",
    "diff_summary": "added 2 tables, removed 3 filler paragraphs",
    "quality_before": X,
    "quality_after": Y,
    "delta": Y-X,
    "kept": true/false,
    "affected_refs": ["id1", "id2"]
  }
```

**Experiment analytics spec:**
```
cex_experiment_analytics.py:
  INPUT:  .cex/experiments/results.tsv + diff_log.jsonl
  OUTPUT:
    - Convergence rate by kind (how many rounds to reach 9.0)
    - Best/worst deltas (which changes had biggest positive/negative impact)
    - Success rate by hypothesis type (table addition, filler removal, etc.)
    - Quality distribution histogram (text-based)
    - Top 10 most-improved artifacts
    - Top 10 stubbornly-low artifacts
  FLAGS:
    --kind <kind>    Filter to specific kind
    --since <date>   Filter by date range
    --format tsv|md  Output format (default: md)
```

### Wave 6: Integration + Documentation (N04 solo)

| # | Artifact | Path | Kind |
|---|----------|------|------|
| 6.1 | KC: Cross-Reference Wiring | N00_genesis/P01_knowledge/library/kind/kc_cross_reference.md | knowledge_card |
| 6.2 | KC: Autoresearch Pattern | N00_genesis/P01_knowledge/library/kind/kc_autoresearch.md | knowledge_card |
| 6.3 | KC: LLM Wiki Pattern | N00_genesis/P01_knowledge/library/kind/kc_llm_wiki.md | knowledge_card |
| 6.4 | Dashboard: Cross-ref health | _dashboards/cross_ref_health.md | dashboard |

## Dependency Graph

```
Wave 0: Obsidian vault ............... DONE
  |
Wave 1: Schema wiring (12 schemas + 1 skill) ......... N03 solo
  |
Wave 2: Builder ISO wiring (596 files via script) .... N03 solo (depends on W1)
  |
Wave 3: Existing artifact sweep (2000+ files) ........ N03 tool (depends on W1)
  |
  +--- Wave 4: Ripple + semantic lint ................. N03 solo (depends on W3)
  |
  +--- Wave 5: Autoresearch upgrade ................... N03 solo (independent of W4)
  |
Wave 6: Documentation ............................... N04 solo (after W4+W5)
```

W2 and W3 can run in PARALLEL (both depend on W1 only).
W4 and W5 can run in PARALLEL (W4 depends on W3, W5 is independent).
W6 is last (documentation after all tools exist).

## Estimated Effort

| Wave | Files Modified | New Files | Nucleus | Time |
|------|---------------|-----------|---------|------|
| 0 | 1 (.gitignore) | 9 | N07 (done) | DONE |
| 1 | 12 | 1 | N03 | 1 session |
| 2 | 596 (automated) | 1 (script) | N03 | 1 session |
| 3 | ~2000 (automated) | 1 (tool) | N03 | 1 session |
| 4 | 0 | 2 | N03 | 1 session |
| 5 | 2 | 1 | N03 | 1 session |
| 6 | 0 | 4 | N04 | 1 session |
| **Total** | **~2600** | **19** | **2 nuclei** | **~6 sessions** |

## Decision Manifest (from /guide)

```yaml
decisions:
  dp1_cross_ref_mode: auto_with_safety_net
  dp1_reason: "Auto-apply ripple patches, git-snapshot before, revert if quality drops >0.5"
  dp2_semantic_lint_severity: warn
  dp2_reason: "New capability, start soft, tighten to block after 2 weeks of data"
  dp3_synthesis_model: haiku
  dp3_reason: "Synthesis is summarization not creation, cheapest tier sufficient"
  dp4_experiment_storage: tsv
  dp4_reason: "Append to existing results.tsv, grep-friendly, zero deps"
```

## What This Unlocks (post-assimilation)

| Capability | Before | After |
|------------|--------|-------|
| Cross-references | 0 systematic (P01 has field, unused) | Every artifact links to 3-15 neighbors |
| Obsidian Graph | 2000 isolated dots | Connected knowledge graph, colored by nucleus |
| Quality visibility | CLI tools only | Dataview dashboards (live in Obsidian) |
| Ripple on edit | None (edit one file, others stale) | Auto-update 10-15 related artifacts |
| Semantic consistency | Structural lint only | Contradiction + stale + orphan detection |
| Overnight evolution | Single-file polish | Cluster evolution (related artifacts together) |
| Experiment learning | quality delta only | Hypothesis + diff + affected refs tracked |
| Human navigation | File explorer / grep | Obsidian vault with backlinks + graph + search |

## Post-Assimilation: The Compound Loop

```
User creates artifact via 8F pipeline
  |
  v
F6 PRODUCE: builder injects ## Related Artifacts (from skill_cross_reference.md)
  |
  v
F7 GOVERN: S_RELATED gate checks related: field populated
  |
  v
F8 COLLABORATE: save -> cex_ripple.py fires -> updates 10-15 neighbors
  |
  v
Overnight: cex_evolve.py --cluster evolves related artifacts together
  |
  v
cex_semantic_lint.py detects contradictions from ripple
  |
  v
User opens Obsidian -> Graph View shows the new connections
  |
  v
Dataview dashboards show quality trends, orphans, clusters
  |
  v
REPEAT (every artifact makes the next one smarter)
```

This is the final wiring. After this, CEX is a self-improving, self-linking,
human-navigable knowledge system. Karpathy's patterns are not bolted on --
they are the natural completion of what CEX was already building toward.
