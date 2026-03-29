---
kind: knowledge_card
id: bld_knowledge_card_memory_summary
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for memory_summary production — memory compression specification
sources: LangChain ConversationSummaryMemory, Zep, Letta (MemGPT), progressive summarization literature
---

# Domain Knowledge: memory_summary
## Executive Summary
Memory summaries are compressed representations of past conversational or session context, injected into LLM prompts to extend effective context beyond the model's raw window. They trade verbatim fidelity for token efficiency, preserving semantic content (entities, decisions, action items) while dropping low-value turns (greetings, redundant clarifications, filler). Unlike session_state (ephemeral runtime cursor) and learning_record (persistent learned patterns), memory_summary is a reusable compression artifact consumed at injection time.

## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (Memory) |
| llm_function | INJECT (injected into context at runtime) |
| layer | runtime |
| machine_format | yaml |
| max_bytes | 2048 |
| naming | p10_summary_{scope}.md |
| id_prefix | p10_ms |

## Compression Methods
| Method | Mechanism | Compression Ratio | Fidelity | Best For |
|--------|-----------|-------------------|----------|----------|
| abstractive | LLM rewrites context in compressed form | 5:1 to 20:1 | Semantic only | Long sessions, high turn count |
| extractive | Key sentences lifted verbatim | 2:1 to 5:1 | High (exact phrasing) | Short windows, precise recall |
| hybrid | Abstractive narrative + extractive facts/decisions | 4:1 to 10:1 | Moderate-high | General purpose sessions |
| sliding_window | Rolling buffer, oldest turns summarized first | Continuous | Progressive loss | Long-running continuous agents |

## Trigger Patterns
| Trigger | Condition | Typical Threshold |
|---------|-----------|------------------|
| token_threshold | Total context tokens >= N | 3000-6000 tokens |
| turn_count | Message count >= N | 10-20 turns |
| explicit | Caller invokes summarize() directly | N/A |
| time_based | Elapsed time >= N seconds/minutes | Session-specific |

## Retention Taxonomy
What must survive compression:
- **Entities**: named people, systems, files, URLs, IDs referenced in conversation
- **Decisions**: explicit commitments ("we will use PostgreSQL", "deadline is Friday")
- **Action items**: tasks assigned or agreed upon with owner and due date
- **Temporal markers**: when retain_timestamps=true — chronological anchors for multi-session summaries
What is safe to drop:
- Greetings, filler turns, acknowledgment messages
- Redundant clarification loops where final answer supersedes them
- Tool call details when only the result matters
- Intermediate reasoning when conclusion is retained

## Ecosystem Reference
- **LangChain ConversationSummaryMemory**: abstractive via LLM, progressive summarization on each turn
- **Zep**: server-side async summarization, entity extraction, temporal awareness, session-scoped
- **Letta (MemGPT)**: hierarchical memory — core (always present) / archival (vector-stored) / recall (recent window)
- **OpenAI Assistants**: thread summarization built-in with automatic truncation + summary injection

## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Progressive summarization | Each new summary incorporates previous summary + new turns | Continuous agents |
| Hierarchical compression | Different compression ratios for recent vs. old content | Multi-session memory |
| Entity-anchored | Always preserve all entity mentions verbatim | Retrieval-heavy workflows |
| Decision log | Extract decisions as structured list, summarize rest | Planning/project agents |

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No entity retention | Downstream retrieval loses named references; agent hallucinates entity details |
| Over-compression | Summary loses action items; agent forgets commitments silently |
| No max_tokens cap | Summaries grow unbounded; context budget overflows |
| Conflating with session_state | session_state is ephemeral — injecting it as memory poisons future sessions |
| Lossy abstractive on code | LLM rewrites code incorrectly; use extractive for technical content |
| Missing trigger threshold | Summarization fires randomly or never; context overflows without warning |

## Application
1. Identify source_type: single conversation, full session, multi-session span, or document
2. Choose compression_method based on fidelity requirements and turn count
3. Set trigger: token_threshold for token-budget management, turn_count for structured workflows
4. Define source_window: how many turns to consume per summarization pass
5. Declare retention: entities (almost always true), decisions (yes for planning agents), action items (yes if commitments matter)
6. Set freshness_decay: 0.05 for long-lived reference, 0.1 for typical session, 0.2+ for ephemeral context
7. Cap max_tokens to protect downstream context budget

## References
- LangChain: ConversationSummaryMemory, ConversationSummaryBufferMemory
- Zep: https://docs.getzep.com/concepts/memory
- Letta: https://docs.letta.com/concepts/memory
- MemGPT paper: Packer et al. 2023 — hierarchical memory for LLM agents
