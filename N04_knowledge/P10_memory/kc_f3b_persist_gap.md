---
id: kc_f3b_persist_gap
kind: knowledge_card
pillar: P10
nucleus: n04
domain: memory_architecture
quality: 8.9
title: "F3b PERSIST Gap: Auto-Wiring Knowledge from Production to Memory"
version: "1.0.0"
tags: [f3b, persist, memory, 8F, gap_analysis, cex_memory_update]
created: "2026-04-18"
updated: "2026-04-18"
tldr: "F3b PERSIST is documented in 8f-reasoning.md but never auto-triggered. The gap: no post-F6 hook calls cex_memory_update.py to extract and persist entities, facts, and patterns discovered during artifact production."
related:
  - bld_collaboration_entity_memory
  - entity-memory-builder
  - bld_collaboration_kind
  - agent_card_n04
  - p03_sp_entity_memory_builder
  - p01_kc_entity_memory
  - kind-builder
  - p01_kc_memory_persistence
  - bld_architecture_kind
  - bld_architecture_entity_memory
---

# F3b PERSIST Gap

## What F3b Is (from 8F spec)

F3b PERSIST is a sub-step of F3 INJECT, defined in `.claude/rules/8f-reasoning.md`:

```
F3b PERSIST (sub-step, optional)
  After assembling context, declare what new knowledge should be persisted:
  - New entities discovered -> entity_memory
  - Updated facts -> knowledge_card update
  - Session learnings -> learning_record
  Output: "F3b: Persist {N} items (entities: {n1}, facts: {n2}, learnings: {n3})"
```

The word "optional" is the gap. In practice, F3b is marked optional and never fires.

## Why It Should Fire Automatically

Every F6 PRODUCE run generates:
1. **New entities**: domain objects not previously indexed (a new builder, a new kind, a new provider name)
2. **Updated facts**: revised versions of existing KC entries (a kind's max_bytes changed, a provider deprecated)
3. **Patterns**: recurrent structural choices that should be promoted to procedural memory

Without F3b auto-firing, every session produces knowledge that evaporates on context reset.
The entity memory, knowledge card, and learning record stores stay stale.
The next nucleus session re-discovers what the previous session already learned.

This is the antithesis of Knowledge Gluttony. N04 must hoard, not leak.

## When F3b Should Trigger (Trigger Conditions)

F3b fires automatically when ANY of these conditions are true after F6 PRODUCE:

| Condition | What to Persist | Target Kind |
|-----------|-----------------|-------------|
| New proper noun encountered (company, tool, person, standard) | name + context + source | entity_memory |
| Existing KC fact contradicted by produced artifact | corrected fact + source | knowledge_card (update) |
| New kind-to-pillar mapping discovered or confirmed | kind, pillar, nucleus routing | entity_memory + kinds_meta update |
| Builder pattern reused identically from example | pattern name + template path | procedural_memory |
| Quality gate failure reason identified | failure reason + fix applied | learning_record |
| New API or tool integration path documented | integration steps + versions | knowledge_card |
| Nucleus routing decision made for ambiguous intent | input phrase + resolved {kind, pillar, nucleus} | entity_memory (intent pattern) |
| User preference expressed | preference type + value | user_model (P10) |
| Performance benchmark completed | metric name + value + context | knowledge_card |
| Gap or missing artifact identified | gap description + proposed kind | learning_record |

**NOT triggered by**: pure reformatting runs, template-fill with no new information, failed F7 gates that produce no artifact.

## What Should Be Persisted Per Category

### Entity Memory (`cex_sdk/memory/manager.py`, kind: entity_memory)

An entity_memory entry captures a named thing:
```yaml
entity: "Cohere Reranker"
type: external_tool
pillar: P01
context: "Reranking API for RAG pipelines -- cross-encoder model, improves precision@k"
source: "archetypes/builders/reranker-config-builder/bld_knowledge_card_reranker_config.md"
discovered_at: "F6 PRODUCE -- reranker_config artifact for N04"
confidence: 0.92
```

The entity memory store is queried at F3 INJECT so the next artifact production already knows this tool exists.

### Knowledge Card Update (kind: knowledge_card)

When a fact in an existing KC is superseded:
```
Old KC fact: "document_loader supports: markdown, PDF, web"
New fact from F6: "document_loader also supports: CSV, JSON (added 2026-04-07)"
Action: append fact to kc_document_loader.md, update `updated` timestamp
```

Use `cex_memory_update.py --from-artifact {artifact_path} --update-kc {kc_path}` to apply the diff.

### Learning Record (kind: learning_record, pillar: P11)

A learning record captures what the nucleus got wrong or surprisingly right:
```yaml
session: "BOOTSTRAP_SELF_W1"
nucleus: n04
artifact: "kc_sdk_coverage_gap.md"
finding: "P09 has 37 kinds but only session_state is partially covered by cex_sdk/session/"
lesson: "config_sdk should be the highest-priority new module; it gates F1 CONSTRAIN quality"
applied: false
priority: high
```

Learning records feed the `cex_quality_monitor.py` regression detection loop.

## How to Wire F3b (The Fix)

### Option 1: PostToolUse Hook (Recommended)

In `.claude/settings.json`, the `PostToolUse` hook already runs after Write tool calls.
Extend `cex_hooks_native.py post-tool-use` to detect artifact saves and trigger F3b:

```python
# In cex_hooks_native.py -- post_tool_use handler
def post_tool_use(tool_name, tool_input, tool_output):
    if tool_name == "Write" and tool_input.get("file_path", "").endswith(".md"):
        path = tool_input["file_path"]
        if is_artifact(path):  # has frontmatter with kind + pillar
            run_f3b_persist(path)

def run_f3b_persist(artifact_path):
    # Extract entities, facts, patterns from artifact
    subprocess.run([
        "python", "_tools/cex_memory_update.py",
        "--from-artifact", artifact_path,
        "--auto"   # auto-classify: entity vs. KC update vs. learning record
    ], check=False)
```

The `--auto` flag on `cex_memory_update.py` needs to be implemented: it should:
1. Parse artifact frontmatter + body
2. Extract named entities (NER pass or LLM-assisted)
3. Compare against existing KCs for fact delta
4. Write to appropriate store (entity_memory / KC update / learning_record)

### Option 2: Explicit F3b Step in 8F Trace

Until the hook is wired, nuclei should execute F3b manually after every F6 PRODUCE:

```
F3b PERSIST:
  - Scan produced artifact for new entities -> list
  - Check each against N04_knowledge/P10_memory/knowledge_memory_index.md
  - For each new entity: write entity_memory stub
  - For each KC fact delta: update the relevant KC file
  - For quality gate result: append to learning_record
  Output: "F3b: Persisted 3 items (entities: 2, facts: 1, learnings: 0)"
```

This is the zero-infrastructure fallback. It requires discipline but no new code.

### Option 3: Async Persistence Daemon

A long-running `cex_memory_update.py --watch .cex/runtime/handoffs/` daemon:
- Watches for new artifact writes via filesystem events (watchdog)
- Queues F3b extraction jobs
- Processes asynchronously so nucleus is not blocked
- Suitable for overnight grid runs where many artifacts are produced in parallel

**Implementation**: extend `daemon-builder` kind to generate this pattern.

## Implementation Priority

| Option | Effort | Impact | Recommended For |
|--------|--------|--------|-----------------|
| 2 (explicit step) | Zero | Medium -- requires discipline | Immediate use, all nuclei |
| 1 (PostToolUse hook) | Medium (1-2 days N05) | High -- automatic, no discipline needed | W2 engineering sprint |
| 3 (async daemon) | High (3-5 days N05+N03) | High -- best for overnight grids | V2 after hook proven |

## Gap Metrics

- F3b fires in: 0% of current 8F runs (manual inspection of recent commits confirms zero `cex_memory_update.py --from-artifact` calls)
- entity_memory store: 1 file (`N04_knowledge/P10_memory/entity_memory_n04.md`) -- hand-written, not auto-populated
- learning_record store: 1 file (`N04_knowledge/P10_memory/mem_learning_record_n04.md`) -- hand-written
- knowledge_memory_index: exists but manually maintained (`knowledge_memory_index.md`)

Without F3b auto-wiring, the memory system is a write-once snapshot, not a compound-over-time store.
The core CEX promise -- "self-assimilating enterprise brain" -- is broken at the F3b seam.

## Acceptance Criteria (F3b Wired)

- [ ] PostToolUse hook detects artifact writes and calls cex_memory_update.py --from-artifact
- [ ] cex_memory_update.py --auto extracts entities, fact deltas, learning records
- [ ] entity_memory store grows by >5 entries per typical grid run
- [ ] knowledge_memory_index.md is auto-updated (not hand-maintained)
- [ ] F3b trace line appears in 8F output: "F3b: Persisted N items"
- [ ] cex_quality_monitor.py ingests learning records for regression detection

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_entity_memory]] | downstream | 0.36 |
| [[entity-memory-builder]] | related | 0.30 |
| [[bld_collaboration_kind]] | downstream | 0.28 |
| [[agent_card_n04]] | upstream | 0.28 |
| [[p03_sp_entity_memory_builder]] | related | 0.28 |
| [[p01_kc_entity_memory]] | sibling | 0.27 |
| [[kind-builder]] | upstream | 0.27 |
| [[p01_kc_memory_persistence]] | sibling | 0.26 |
| [[bld_architecture_kind]] | upstream | 0.26 |
| [[bld_architecture_entity_memory]] | upstream | 0.25 |
