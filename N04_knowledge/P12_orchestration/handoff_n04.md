---
quality: 7.8
quality: 7.4
id: handoff_n04
kind: handoff
8f: F8_collaborate
nucleus: n04
pillar: P12
mirrors: N00_genesis/P12_orchestration/tpl_handoff.md
mirror_version: 1.0.0
promoted_from: null
overrides:
  tone: archival, dense, citation-thick
  voice: third-person encyclopedic
  sin_lens: GULA DO CONHECIMENTO
  required_fields:
    - sources
    - retrieval_method
    - freshness
  quality_threshold: 9.2
  density_target: 0.92
  example_corpus: 3+ examples with source manifest
version: 1.0.0
tags: [mirror, n04, knowledge, handoff, hermes_assimilation, retrieval_manifest, citation_trail]
related:
  - self_audit_n04_codex_2026_04_15
  - p02_nd_n04.md
  - bld_architecture_supabase_data_layer
  - spec_n01_n04_verticalization
  - p12_spawn_knowledge_engineer
  - bld_collaboration_supabase_data_layer
  - p01_kc_supabase_data_layer_n04
  - p11_qg_intelligence
  - n04_dr_knowledge
  - n04_agent_embedding_engineer
density_score: 1.0
---

## Override Rationale

N04 handoffs carry a **retrieval manifest**: a structured record of every source
consulted during the task, with confidence scores and freshness stamps. Downstream
nuclei receiving an N04 handoff never need to re-retrieve the same sources -- they
inherit the citation trail. This prevents redundant retrieval across a multi-wave
mission and ensures the knowledge corpus is utilized maximally.

## Handoff Structure (N04)

### Standard Fields (N00 inherited)

| Field | Description |
|-------|-------------|
| `from_nucleus` | n04 |
| `to_nucleus` | {{target}} |
| `mission` | {{mission_id}} |
| `wave` | {{wave_number}} |
| `task_summary` | What N04 completed |
| `deliverables` | List of artifact paths produced |

### N04 Extensions

| Field | Description | Required |
|-------|-------------|---------|
| `retrieval_manifest` | Ordered list of all sources consulted | yes |
| `citation_trail` | Claim -> source mappings from session | yes |
| `corpus_gaps` | Gaps found during task; requires downstream ingestion | if any |
| `taught_terms` | New metaphor->industry mappings surfaced | if any |
| `knowledge_index_updated` | Whether cex_index.py was run | yes |

## Retrieval Manifest Format

```yaml
retrieval_manifest:
  - source: kc_{{kind}}.md
    path: N00_genesis/P01_knowledge/library/kind/kc_{{kind}}.md
    confidence: 0.93
    method: hybrid
    retrieved_at: "{{YYYY-MM-DD}}"
  - source: "{{source_id}}"
    path: "{{file_path}}"
    confidence: {{0.0-1.0}}
    method: {{dense|sparse|hybrid|graph}}
    retrieved_at: "{{YYYY-MM-DD}}"
```

## Citation Trail Format

```yaml
citation_trail:
  - claim: "{{claim_summary}}"
    source: "{{source_id}}"
    path: "{{file_path}}"
    confidence: {{0.0-1.0}}
    verified: {{true|false}}
```

## Corpus Gap Format

```yaml
corpus_gaps:
  - gap: "{{gap_description}}"
    triggered_by: "{{skill_or_query}}"
    ingestion_priority: {{high|medium|low}}
    recommended_source: "{{url_or_path}}"
```

## Example Handoff (N04 -> N07)

```markdown
---
from_nucleus: n04
to_nucleus: n07
mission: HERMES_ASSIMILATION
wave: W3
task_summary: "Produced 7 fractal mirrors for N04 with GULA DO CONHECIMENTO sin lens"
deliverables:
  - N04_knowledge/P10_memory/user_model_n04.md
  - N04_knowledge/P11_feedback/revision_loop_policy_n04.md
  - N04_knowledge/P11_feedback/curation_nudge_n04.md
  - N04_knowledge/P04_tools/skill_n04.md
  - N04_knowledge/P10_memory/session_state_n04.md
  - N04_knowledge/P02_model/agent_n04.md
  - N04_knowledge/P12_orchestration/handoff_n04.md
retrieval_manifest:
  - source: tpl_user_model.md
    confidence: 0.97
    method: glob
  - source: user_model_n01.md (reference mirror)
    confidence: 0.94
    method: glob
corpus_gaps: []
taught_terms: []
knowledge_index_updated: false
---
```

## Links

- N00 archetype: [[N00_genesis/P12_orchestration/tpl_handoff.md]]
- N00 KC: [[N00_genesis/P01_knowledge/library/kind/kc_handoff.md]]
- Related: [[N04_knowledge/P10_memory/session_state_n04.md]]
- Related: [[N04_knowledge/P12_orchestration/dispatch_rule_knowledge.md]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[self_audit_n04_codex_2026_04_15]] | upstream | 0.34 |
| [[p02_nd_n04.md]] | upstream | 0.28 |
| [[bld_architecture_supabase_data_layer]] | upstream | 0.26 |
| [[spec_n01_n04_verticalization]] | upstream | 0.25 |
| [[p12_spawn_knowledge_engineer]] | related | 0.25 |
| [[bld_collaboration_supabase_data_layer]] | related | 0.25 |
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.24 |
| [[p11_qg_intelligence]] | upstream | 0.23 |
| [[n04_dr_knowledge]] | related | 0.22 |
| [[n04_agent_embedding_engineer]] | upstream | 0.22 |
