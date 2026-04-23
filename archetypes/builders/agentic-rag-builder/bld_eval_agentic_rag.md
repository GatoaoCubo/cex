---
kind: quality_gate
id: p01_qg_agentic_rag
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for agentic_rag
quality: 9.0
title: "Quality Gate Agentic Rag"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for agentic_rag"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_agentic_rag
  - p01_qg_graph_rag_config
  - p11_qg_audit_log
  - p09_qg_marketplace_app_manifest
  - p12_qg_visual_workflow
  - p01_qg_reranker_config
  - p05_qg_github_issue_template
  - bld_instruction_agentic_rag
  - p07_qg_eval_metric
  - p01_qg_faq_entry
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| ID pattern | ^p01_ar_[a-z][a-z0-9_]+.md$ | matches | artifact filename |

## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches ^p01_ar_[a-z][a-z0-9_]+.md$ | ID does not conform to schema pattern |
| H03 | kind field equals 'agentic_rag' | kind field is not 'agentic_rag' |
| H04 | agent_type field present and non-empty | Missing or empty agent_type field |
| H05 | knowledge_source field present and non-empty | Missing or empty knowledge_source field |
| H06 | Execution workflow section present | Missing ## Execution Workflow section |
| H07 | Reflection loop documented (retrieve->reflect->re-query) | No reflection loop specification |
| H08 | Fallback strategy defined | No fallback behavior for retrieval failure |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Schema Completeness | 0.20 | All required frontmatter fields present and typed correctly |
| D02 | Agent Loop Clarity | 0.20 | retrieve->reflect->re-query cycle explicitly documented |
| D03 | Retrieval Strategy | 0.15 | Retriever type, similarity metric, top-k defined |
| D04 | Knowledge Source Provenance | 0.15 | Source type, format, access method documented |
| D05 | Error and Fallback Coverage | 0.10 | CRAG-style corrective fallback or equivalent |
| D06 | Tool Plan Coverage | 0.10 | Agent tools listed against bld_config_agentic_rag.md registry |
| D07 | Documentation Quality | 0.10 | Usage examples and section headers complete |

## Actions
(Table: Score | Action)
| Score      | Action         |
|------------|----------------|
| >=9.5      | GOLDEN         |
| >=8.0      | PUBLISH        |
| >=7.0      | REVIEW         |
| <7.0       | REJECT         |

## Bypass
(Table: conditions, approver, audit trail)
| conditions                  | approver             | audit trail                              |
|-----------------------------|----------------------|------------------------------------------|
| Emergency fix required      | Senior Engineering Lead | "Bypass approved by [name] for [reason]" |

## Examples

## Golden Example
```markdown
---
cex_kind: agentic_rag
name: LegalDocAssistant
description: Agent-driven RAG for contract review using real tools
tools:
  - langchain
  - weaviate
  - openai/gpt-4
---
**Workflow**:
1. User submits contract text to LangChain agent
2. Agent queries Weaviate vector store for relevant legal precedents
3. Agent synthesizes findings with GPT-4 to generate risk assessment
4. Agent proposes amendments with cited precedents
```

## Anti-Example 1: Missing Agent Logic
```markdown
---
cex_kind: agentic_rag
name: SimpleRetriever
description: Basic document search without generation
tools:
  - elasticsearch
  - openai/text-embedding-ada-002
---
**Workflow**:
1. User submits query
2. Elasticsearch returns matching documents
3. Results displayed verbatim to user
```
## Why it fails
Lacks agent orchestration and generation layer - just simple retrieval without synthesis or decision-making

## Anti-Example 2: Missing Retrieval Component
```markdown
---
cex_kind: agentic_rag
name: PureAgent
description: Chatbot with no external data access
tools:
  - langchain
  - openai/gpt-4
---
**Workflow**:
1. User asks question
2. GPT-4 generates response from training data
3. Response delivered without external validation
```
## Why it fails
No retrieval component - agent operates solely on pre-trained knowledge without augmenting with external data sources

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
