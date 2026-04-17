---
id: p01_kc_research_pipeline
kind: knowledge_card
type: kind
pillar: P04
title: "Research Pipeline — Deep Knowledge for research_pipeline"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: builder_agent
domain: research_pipeline
quality: 9.1
tags: [research_pipeline, P04, PRODUCE, kind-kc, research, STORM, CRAG]
tldr: "7-stage autonomous research motor (INTENT>PLAN>RETRIEVE>RESOLVE>SCORE>SYNTHESIZE>VERIFY) using STORM multi-perspective + CRAG corrective retrieval + CRITIC self-verification patterns"
when_to_use: "Building, reviewing, or reasoning about research_pipeline artifacts"
keywords: [research_pipeline, STORM, CRAG, CRITIC, retrieval, synthesis, verification]
feeds_kinds: [research_pipeline]
density_score: null
---

# Research Pipeline

## Spec
```yaml
kind: research_pipeline
pillar: P04
llm_function: PRODUCE
max_bytes: 5120
naming: p04_rp_{{name}}.md
core: false
```

## What It Is
A research_pipeline is a multi-stage autonomous research motor that transforms a research question into a verified, cited synthesis. It orchestrates 7 stages: INTENT (parse question), PLAN (decompose into sub-queries), RETRIEVE (multi-source fetch), RESOLVE (deduplicate + reconcile), SCORE (relevance + credibility ranking), SYNTHESIZE (produce structured output), VERIFY (fact-check against sources). It draws from 3 research patterns: STORM (multi-perspective synthesis from Stanford, 2024), CRAG (Corrective RAG with web fallback), and CRITIC (self-verification with tool feedback). It is NOT a retriever (which handles a single fetch step) nor a search_tool (which wraps a single search API).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| STORM (Stanford) | Co-STORM multi-perspective | Generates diverse expert perspectives before synthesis |
| CRAG (2024) | Corrective Retrieval-Augmented Generation | Evaluates retrieval quality; falls back to web search |
| CRITIC (2023) | Self-verify with tools | LLM critiques own output; uses tools to fact-check |
| LangChain | create_retrieval_chain + web_search | Chain of retriever + web fallback + reranker |
| LlamaIndex | SubQuestionQueryEngine | Decomposes into sub-questions across multiple indices |
| Perplexity | Internal pipeline | RETRIEVE>RERANK>SYNTHESIZE>CITE pattern |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| stages | list[str] | all 7 | Fewer stages = faster but less reliable |
| sources | list[str] | required | web, arxiv, local_rag, api; breadth vs latency |
| max_iterations | int | 3 | More iterations = better coverage but higher cost |
| scoring_model | str | null | Dedicated reranker vs LLM-as-judge; accuracy vs cost |
| verification_mode | str | self_check | self_check / tool_check / human_review |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| STORM multi-perspective | Broad topic exploration | 5 expert perspectives on "AI agent frameworks" |
| CRAG corrective loop | When retrieval quality varies | Score retrieval; if low, fall back to web search |
| Sub-question decomposition | Complex multi-faceted question | "Compare X vs Y" -> 4 sub-queries per dimension |
| Citation-grounded synthesis | Trustworthy output required | Every claim linked to source URL + paragraph |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| No VERIFY stage | Hallucinated claims persist | Add CRITIC-style self-check or tool-check |
| Single source | Bias and coverage gaps | Use >= 3 diverse sources (web + academic + local) |
| Skip RESOLVE | Duplicate and contradictory facts | Deduplicate and reconcile before SYNTHESIZE |

## Integration Graph
```
[research_question] --> [INTENT] --> [PLAN] --> [RETRIEVE]
                                                    |
                         [VERIFY] <-- [SYNTHESIZE] <-- [SCORE] <-- [RESOLVE]
                            |
                     [verified_synthesis]
```

## Decision Tree
- IF need single-source retrieval THEN use retriever
- IF need web search wrapper THEN use search_tool
- IF need knowledge storage THEN use knowledge_card
- IF need multi-stage autonomous research with verification THEN research_pipeline
- DEFAULT: research_pipeline when question requires multi-source retrieval + synthesis + fact-checking

## Quality Criteria
- GOOD: At least 5 stages defined; 2+ sources configured; verification present
- GREAT: All 7 stages; STORM + CRAG patterns applied; citation-grounded output; max_iterations tuned; scoring_model specified
- FAIL: No VERIFY stage; single source; no scoring/ranking step; ungrounded synthesis
