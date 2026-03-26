---
pillar: P12
llm_function: COLLABORATE
version: 1.0.0
---

# Collaboration: rag-source-builder

## Crew Role
EXTERNAL SOURCE CATALOGER.

I answer: "where is authoritative external data for this domain?"
I produce: structured pointers (rag_source) that retrieval pipelines can crawl and index.

## What I Do NOT Do

| Task | Who Does It |
|------|------------|
| Distill content from a source | knowledge-card-builder |
| Write domain context for agents | context-doc-builder |
| Configure vector embedding models | embedding-config-builder [PLANNED] |
| Score quality of artifacts | validation pipeline / validator-builder |
| Define validation rules | validator-builder |

## Knowledge Pipeline Crew

```
rag-source-builder          <- I am here
  "catalog the external source"
        |
        v
knowledge-card-builder
  "distill content from that source into structured knowledge"
        |
        v
brain-index config [PLANNED]
  "configure how to embed and chunk for vector search"
        |
        v
retrieval layer
  "serve knowledge to agents"
```

## Handoff Protocol

### Receives From
| Input | Source | Required |
|-------|--------|---------|
| url | user / orchestrator | YES |
| domain | user / orchestrator | YES |
| reliability hint | user | optional |
| extraction notes | user | optional |

### Produces For
| Output | Consumer | Format |
|--------|----------|--------|
| p01_rs_{slug}.md | brain_index, knowledge-card-builder | .md + .yaml |
| source metadata | domain catalog | frontmatter fields |

## Parallel Operation
rag-source-builder operates independently. No blocking dependency on other builders.
Multiple rag_sources for the same domain can be cataloged in parallel without conflict.

## Escalation
If URL is inaccessible or source requires authentication not documented:
- Flag in Extraction Notes: "Auth required: yes — credentials not configured"
- Set reliability: low
- Set last_checked to today — do not block creation

## Signal on Completion
After producing artifact:
```python
write_signal('rag-source-builder', 'complete', 8.0)
```
