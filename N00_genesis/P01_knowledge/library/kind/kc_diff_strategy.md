---
quality: null
id: kc_diff_strategy
kind: knowledge_card
8f: F3_inject
title: "Diff Strategy: Change Application and Matching Algorithm"
version: 1.1.0
pillar: P01
related:
  - p10_lr_diff_strategy_builder
  - diff-strategy-builder
  - p08_kc_capability_registry
  - intent_resolution_fixes_results
  - bld_collaboration_diff_strategy
  - p01_kc_pattern_extraction
  - bld_config_knowledge_index
  - bld_instruction_diff_strategy
  - bld_examples_edit_format
density_score: 0.90
updated: "2026-04-22"
---

# Diff Strategy: Change Application and Matching Algorithm

## Purpose

Define systematic approaches to apply changes and match algorithms for knowledge evolution. A diff strategy determines how two versions of an artifact are compared, what constitutes a meaningful change, and how that change is applied to produce the next version. This is foundational for artifact versioning, incremental compilation, and knowledge base evolution.

## Key Concepts

1. **Change Application**: Process of implementing modifications to existing knowledge while preserving structural integrity
2. **Matching Algorithm**: Computational method to identify pattern similarities between source and target
3. **Conflict Resolution**: Strategy for handling overlapping or contradictory changes from multiple sources
4. **Change Granularity**: The atomic unit of change -- line-level, block-level, semantic-level, or AST-level

## Diff Algorithm Comparison

| Algorithm | Type | Time Complexity | Space Complexity | Best For |
|-----------|------|----------------|-----------------|----------|
| Myers (git default) | Line-based LCS | O(ND) where D=edit distance | O(N) | Source code, text files |
| Patience | Anchor-based | O(N log N) | O(N) | Files with many unique lines |
| Histogram | Frequency-based | O(N) average | O(N) | Large files with repetition |
| Tree-diff (GumTree) | AST-based | O(N^2) worst | O(N) | Structured code, XML, JSON |
| Semantic diff | Embedding-based | O(N*D) where D=embed dim | O(N*D) | Natural language, knowledge cards |
| OT (Operational Transform) | Operation-based | O(N*M) concurrent ops | O(N) | Real-time collaborative editing |
| CRDT (Conflict-free) | State-based | O(1) per operation | O(N) | Distributed systems, offline-first |

## Application Process

1. **Validation Phase**: Verify change relevance using quality gates
   - Check source artifact exists and is well-formed
   - Verify target artifact version matches expected base
   - Validate change set against schema constraints
2. **Normalization**: Canonicalize both source and target (whitespace, encoding, ordering)
3. **Matching**: Run selected algorithm to produce edit script (insertions, deletions, modifications)
4. **Conflict Detection**: Identify overlapping regions from concurrent edits
5. **Transformation**: Convert changes to compatible format (patch, merge commit, OT operations)
6. **Integration**: Apply edit script to produce merged artifact
7. **Verification**: Confirm structural integrity via schema validation and regression checks

## Matching Algorithm Types

| Type | Mechanism | Use Case | Precision | Recall |
|------|-----------|----------|-----------|--------|
| Exact Match | Byte-for-byte comparison | Identical pattern detection, deduplication | 100% | Low |
| Fuzzy Match | Edit distance (Levenshtein, Jaro-Winkler) | Partial pattern similarity, typo tolerance | Medium | Medium |
| Token Match | Tokenized comparison (word/subword) | NLP text comparison, prompt diff | Medium | High |
| Semantic Match | Embedding cosine similarity | Meaning-preserving changes, paraphrase detection | Variable | High |
| Structural Match | AST/DOM tree comparison | Code refactoring, schema evolution | High | High |
| Heuristic | Rule-based pattern matching | Contextual pattern recognition, domain-specific | Medium | Medium |

## Concrete Example: Knowledge Card Diff

```yaml
# Base version (v1.0.0)
---
id: kc_example
kind: knowledge_card
version: 1.0.0
quality: 8.2
---
# Example Topic
## Section A
Content about topic A.

## Section B
Content about topic B.
```

```yaml
# Modified version (v1.1.0) -- diff applied
---
id: kc_example
kind: knowledge_card
version: 1.1.0           # CHANGED: version bump
quality: null             # CHANGED: reset for re-scoring
---
# Example Topic
## Section A
Content about topic A.
Additional detail added.  # ADDED: new line

## Section B
Revised content for B.    # MODIFIED: replacement

## Section C              # ADDED: new section
Entirely new section.
```

## Merge Strategies

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Ours | Keep local version on conflict | Local edits are authoritative |
| Theirs | Keep remote version on conflict | Remote source is authoritative |
| Union | Keep both sides | Additive-only changes (lists, tags) |
| Recursive | 3-way merge with common ancestor | Standard git merge workflow |
| Octopus | N-way merge | Merging multiple feature branches |
| Rebase | Replay commits on new base | Linear history preference |

## Best Practices

- Use exact matching for precise updates and deduplication passes
- Apply fuzzy matching for semantic similarity when exact match fails
- Use structural (AST) diff for code artifacts to avoid false positives from formatting changes
- Always validate schema compliance after integration
- Maintain version history for traceability -- every diff produces a lineage_record
- Prefer 3-way merge (with common ancestor) over 2-way diff for conflict resolution
- Set conflict resolution policy before starting batch operations
- Use semantic diff for knowledge_card evolution where meaning matters more than surface form

## Anti-Patterns

- **Blind overwrite**: Replacing entire artifact without diff -- destroys traceability
- **Unversioned merge**: Applying changes without version bump -- breaks lineage
- **Silent conflict drop**: Discarding one side of a conflict without logging -- data loss risk
- **Format-sensitive diff**: Using line-diff on structured data (YAML, JSON) -- false positives from reordering

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_diff_strategy_builder]] | downstream | 0.28 |
| [[diff-strategy-builder]] | downstream | 0.23 |
| [[p08_kc_capability_registry]] | sibling | 0.20 |
| [[intent_resolution_fixes_results]] | downstream | 0.19 |
| [[bld_collaboration_diff_strategy]] | downstream | 0.19 |
| [[p01_kc_pattern_extraction]] | sibling | 0.17 |
| [[bld_config_knowledge_index]] | downstream | 0.16 |
| [[bld_instruction_diff_strategy]] | downstream | 0.15 |
| [[bld_examples_edit_format]] | downstream | 0.15 |
