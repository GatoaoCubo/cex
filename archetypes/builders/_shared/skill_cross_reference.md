---
id: skill_cross_reference
kind: instruction
scope: shared
purpose: "Teach all builders to wire cross-references into every artifact they produce. Part of the Karpathy Assimilation -- turning CEX from 2000 isolated dots into a connected knowledge graph."
version: 1.0.0
created: 2026-04-20
author: n03_engineering
quality: 9.2
tags: [skill, shared, cross-reference, wikilinks, karpathy, graph, related]
tldr: "Every artifact must declare its neighbors. 3-15 related: IDs in frontmatter + ## Related Artifacts table in body. Auto-populated by cex_wikilink.py, curated by builders."
density_score: 0.93
related:
  - p04_skill_verify
  - bld_instruction_kind
  - p06_arch_knowledge_graph
  - bld_instruction_golden_test
  - p03_sp_n03_creation_nucleus
  - shared_skill_verification_protocol
  - self_audit_newpc_2026_04_13
  - ctx_cex_new_dev_guide
  - p02_agent_creation_nucleus
  - bld_collaboration_retriever_config
---

# Skill: Cross-Reference Wiring

## The Principle

> **Isolated knowledge decays. Connected knowledge compounds.**
>
> An artifact that knows its neighbors is 10x more useful than one that doesn't.
> The same fact, linked from 15 directions, becomes a hub. Hubs become canonical.
> Canonical artifacts stop being rewritten from scratch every session.

This skill is mandatory for all builders at F6 PRODUCE and enforced at F7 GOVERN (S_RELATED gate).
Schema-level spec: `N00_genesis/P{01-12}/_schema.yaml` -- `frontmatter_cex.related`.
Auto-population tool: `_tools/cex_wikilink.py`.

---

## WHEN to Link

Always. No exceptions for published artifacts.

| Condition | Action |
|-----------|--------|
| New artifact, first version | Populate at F6 PRODUCE -- at least 3 links |
| Existing artifact, no related: field | Add during next F7 GOVERN review |
| related: field empty | S_RELATED gate: REJECT (hard, blocks publishing) |
| related: field has 1-2 entries | S_RELATED gate: warn (target 3-15) |
| related: field has 3-15 entries | S_RELATED gate: PASS |

---

## WHAT to Link (4 Relationship Types)

| Type | Meaning | Example |
|------|---------|---------|
| `upstream` | Artifact that FEEDS this one (input, dependency) | knowledge_card feeds prompt_template |
| `downstream` | Artifact this one FEEDS (consumer, dependent) | prompt_template feeds system_prompt |
| `sibling` | Same kind, same domain, different scope/variant | knowledge_card A and knowledge_card B on same topic |
| `alternative` | Different kind that could replace this one in some contexts | retriever vs search_tool |

Every published artifact should have at least **1 upstream** and **1 downstream** link.
Pure leaf artifacts (no upstream) or pure root artifacts (no downstream) are exceptions -- document why.

---

## HOW to Link (Format Spec)

### Frontmatter (required)

```yaml
related:
  - p01_kc_rag_patterns          # upstream: knowledge source
  - p03_pt_retrieval_query        # downstream: uses this KC
  - p10_ki_faiss_index            # sibling: same domain
  - p04_search_tavily             # alternative: could replace in web-search context
```

**ID format**: `p{XX}_{kind_prefix}_{slug}` where:
- `p{XX}` = pillar number (p01 through p12)
- `{kind_prefix}` = 2-3 char abbreviation of kind (kc=knowledge_card, pt=prompt_template, etc.)
- `{slug}` = artifact-specific identifier (filename stem)

### Body (required for published artifacts)

Append this section to the artifact body (after main content, before any footer):

```markdown

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_skill_verify]] | related | 0.24 |
| [[bld_instruction_kind]] | sibling | 0.20 |
| [[p06_arch_knowledge_graph]] | related | 0.20 |
| [[bld_instruction_golden_test]] | sibling | 0.20 |
| [[p03_sp_n03_creation_nucleus]] | related | 0.20 |
| [[shared_skill_verification_protocol]] | related | 0.20 |
| [[self_audit_newpc_2026_04_13]] | related | 0.18 |
| [[ctx_cex_new_dev_guide]] | related | 0.18 |
| [[p02_agent_creation_nucleus]] | related | 0.18 |
| [[bld_collaboration_retriever_config]] | related | 0.18 |

## HOW MANY Links

| Kind type | Target | Minimum | Maximum |
|-----------|--------|---------|---------|
| knowledge_card | 8-10 | 3 | 15 |
| prompt_template, system_prompt | 5-8 | 3 | 15 |
| config kinds (env_config, secret_config, etc.) | 3-5 | 1 | 10 |
| eval kinds (unit_eval, benchmark, etc.) | 4-6 | 2 | 12 |
| orchestration kinds (workflow, handoff, etc.) | 6-10 | 3 | 15 |
| agent, agent_card | 8-12 | 5 | 15 |

---

## HOW to Find Related Artifacts (Discovery Protocol)

At F6 PRODUCE, before writing the Related Artifacts section:

```bash
# Step 1: TF-IDF similarity search (fast, no tokens)
python _tools/cex_retriever.py --query "{artifact title}" --top 20

# Step 2: Filter results by relationship type
# -- Look for upstream: artifacts in P01/P03 that define concepts this artifact uses
# -- Look for downstream: artifacts in P03/P05/P12 that would IMPORT this artifact
# -- Look for siblings: same kind in same domain
# -- Look for alternatives: different kind that solves same problem

# Step 3: Classify (upstream | downstream | sibling | alternative)
# Step 4: Write to frontmatter related: list and ## Related Artifacts table
```

Manual heuristics when retriever is unavailable:

1. **Check the builder's bld_schema_*.md** -- it lists `feeds_from` and `feeds_into`
2. **Check the pillar schema** -- `kinds.{this_kind}.source_map.receives_input_from`
3. **Read the artifact body** -- any kind/artifact name mentioned is a candidate link
4. **Check same directory** -- siblings live in the same `P{XX}_{domain}/` folder

---

## Relationship Categories (CATEGORIES field)

When writing the ## Related Artifacts table, use these exact category strings:

| Category | Meaning |
|----------|---------|
| `upstream` | This artifact CONSUMES the linked artifact |
| `downstream` | This artifact PRODUCES FOR the linked artifact |
| `sibling` | Same kind, same domain, different scope |
| `alternative` | Different kind, overlapping use case |
| `supersedes` | This artifact REPLACES the linked (older) artifact |

---

## S_RELATED Gate (F7 GOVERN)

The cross-reference gate is a HARD gate (reject, blocks publishing):

```
H_RELATED: Cross-Reference Check (HARD)
  [ ] related: frontmatter field populated (min 3 entries)        -- PASS/REJECT
  [ ] ## Related Artifacts section present in body                -- PASS/REJECT
  [ ] At least 1 upstream reference                               -- PASS/REJECT
  [ ] At least 1 downstream or sibling reference                  -- PASS/REJECT
  Action: REJECT if any check fails (score 0, return to F6)
  Auto-fix: cex_wikilink.py runs at F6.5 (after PRODUCE, before GOVERN)
  Note: translation pairs (EN/PT) count as 1 entry, not 2
```

### Why HARD (not SOFT)

An artifact without cross-references is an orphan node. Orphan nodes:
- Cannot be discovered by the retriever (no inbound links)
- Cannot feed downstream artifacts (no outbound links)
- Decay into stale, unreferenced content that gets rewritten from scratch
- Break the Convention-over-Configuration contract for multi-instance CEXAI projects

The auto-fix at F6.5 ensures builders never hit this gate unprepared:
```bash
# Runs automatically between F6 PRODUCE and F7 GOVERN
python _tools/cex_wikilink.py --path {artifact_path} --apply --min-score 0.15 --max-refs 10
```

---

## Integration with cex_wikilink.py (Auto-Population)

`cex_wikilink.py` can auto-populate `related:` for existing artifacts:

```bash
# Dry-run: see what would change
python _tools/cex_wikilink.py --sweep --dry-run

# Apply: write related: to all artifacts
python _tools/cex_wikilink.py --sweep --apply --min-score 0.3 --max-refs 10

# Single artifact
python _tools/cex_wikilink.py --path N01_intelligence/P01_knowledge/kc_competitor.md
```

Auto-populated entries are tagged with `# auto` comment so curators can review:

```yaml
related:
  - p01_kc_market_sizing   # auto
  - p01_kc_pricing_models  # auto
  - p06_is_competitor      # curated
```

Curators should review and promote or remove `# auto` entries during artifact refinement.

---

## Integration with cex_ripple.py (Propagation)

When an artifact is modified, `cex_ripple.py` fires automatically (post-tool-use hook):

```
1. Read modified artifact's related: list
2. For each related artifact: check if the modification affects it
3. If yes: update that artifact's cross-refs bidirectionally
4. Budget: max 15 files modified per ripple cascade
5. Log: .cex/runtime/ripple_log.jsonl
```

Builders do NOT need to manually trigger this -- it fires via the hook system.

---

## Anti-Patterns

| Anti-pattern | Problem | Correct approach |
|-------------|---------|-----------------|
| Empty related: field | Knowledge stays isolated, Obsidian graph shows orphan node | Always link 3+ artifacts |
| Only same-kind links | Misses the cross-pillar connections that make knowledge compound | Include cross-pillar refs |
| Generic links ("see also p01") | Pillar-level links are meaningless -- need artifact-level IDs | Use full artifact ID |
| More than 15 links | Diminishing returns, cognitive overload | Cap at 15, prioritize highest-value |
| Circular-only links (A->B->A) | Creates echo chambers, not knowledge trees | Include external anchors |

---

## Properties

| Property | Value |
|----------|-------|
| Kind | instruction |
| Pillar | cross-cutting |
| Domain | knowledge graph wiring |
| Applies to | ALL builders (N01-N07), all kinds |
| Schema spec | `N00_genesis/P{01-12}/_schema.yaml` -- `frontmatter_cex.related` |
| Auto-tool | `_tools/cex_wikilink.py` |
| Propagation | `_tools/cex_ripple.py` (post-save hook) |
| Gate | H_RELATED (hard, rejects if < 3 related — auto-populated at F6.5 by cex_wikilink.py) |
| Quality target | 9.0+ |
| Density target | 0.85+ |
| Source | Karpathy LLM Wiki pattern (ingest -> summarize -> update 10-15 related pages) |
