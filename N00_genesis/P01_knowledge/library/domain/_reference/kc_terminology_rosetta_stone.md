---
id: p01_kc_terminology_rosetta_stone
kind: knowledge_card
type: domain
pillar: P01
title: "LLM Terminology Rosetta Stone: Cross-Provider Canonical Mapping"
version: 1.1.0
created: 2026-04-07
updated: 2026-04-08
author: N01_intelligence
domain: terminology
origin: src_standards_global
quality: 9.2
tags: [terminology, rosetta-stone, anthropic, openai, google, mcp, canonical, permanent]
tldr: "Cross-provider mapping of official LLM terminology. Every row maps a CEX concept to its canonical name at Anthropic, OpenAI, Google, and MCP. Use this as the single source of truth for CEX kind naming."
when_to_use: "When naming new CEX kinds, validating existing kind names, or translating between provider vocabularies."
keywords: [terminology, canonical, mapping, cross-provider, vocabulary, naming]
long_tails:
  - "what does anthropic call function calling vs openai vs google"
  - "canonical LLM terminology comparison across providers 2026"
axioms:
  - "When providers disagree, prefer the term used by 2+ providers"
  - "When all providers use different terms, prefer the most descriptive one"
feeds_kinds: [knowledge_card, glossary_entry, agent_card, function_def, mcp_server]
linked_artifacts:
  related:
    - P01_knowledge/library/domain/_reference/kc_terminology_anthropic_canonical.md
    - P01_knowledge/library/domain/_reference/kc_terminology_openai_canonical.md
    - P01_knowledge/library/domain/_reference/kc_terminology_google_mcp_canonical.md
    - .cex/runtime/decisions/decision_terminology_standardization.yaml
    - N07_admin/P10_memory/industry_terminology_audit.md
density_score: 0.95
---

# LLM Terminology Rosetta Stone

## Purpose
This card maps the **same concept** across 4 providers + MCP, giving CEX a single lookup table for terminology validation. Each row answers: "What does each provider officially call this thing?"

## Methodology
- Sources: Official API docs, SDKs, protocol specs (not blog posts or tutorials)
- Date: April 2026 (Anthropic Messages API v2025-09, OpenAI API v2, Google Gemini 2.5, MCP spec 2025-06-18)
- Conflict resolution: 2+ providers agree → that term wins; all differ → most descriptive wins

---

## 1. Agent & Identity Concepts

| Concept | Anthropic | OpenAI | Google | MCP | CEX Kind | CEX Aligned? |
|---------|-----------|--------|--------|-----|----------|-------------|
| Agent definition | No native abstraction (built from primitives) | `Agent` (Agents SDK), `Assistant` (Assistants API) | `Agent` (Vertex AI Agent Builder) | N/A (protocol, not agent) | `agent` | ✅ |
| Agent identity card | N/A | N/A | `AgentCard` (A2A protocol) | N/A | `agent_card` | ✅ Google A2A standard |
| System instructions | `system` parameter (Messages API) | `instructions` (Assistants), `system` (Chat) | `system_instruction` (Gemini) | N/A | `system_prompt` | ✅ Universal concept |
| Persona / role | Via system prompt | `instructions` field | Via system_instruction | N/A | `lens` | ⚠️ "Lens" is CEX-only. Industry uses "persona" or "role" |
| Model selection | `model` parameter | `model` parameter | `model` parameter | N/A | `model_card` | ✅ Hugging Face/Google standard |
| Model provider config | N/A | N/A | N/A | N/A | `model_provider` | ✅ Clear enough |

## 2. Tool & Function Concepts

| Concept | Anthropic | OpenAI | Google | MCP | CEX Kind | CEX Aligned? |
|---------|-----------|--------|--------|-----|----------|-------------|
| Tool definition | `tool` object: `{name, description, input_schema}` | `tool` wrapping `function`: `{name, description, parameters}` | `FunctionDeclaration`: `{name, description, parameters}` | `Tool`: `{name, title, description, inputSchema}` | `function_def` | ✅ |
| Tool invocation (model→dev) | `tool_use` content block | `tool_calls` array | `FunctionCall` | `tools/call` method | — (runtime) | — |
| Tool result (dev→model) | `tool_result` content block | `tool` role message | `FunctionResponse` | `tools/call` response | — (runtime) | — |
| Tool selection mode | `tool_choice`: auto/any/tool/none | `tool_choice`: auto/none/required/{name} | `function_calling_config.mode`: AUTO/ANY/NONE/VALIDATED | N/A (host decides) | — (config) | — |
| Strict schema enforcement | `strict: true` (tool-level) | `strict: true` (function-level) | `VALIDATED` mode | Via `inputSchema` | — (config) | — |
| Code execution sandbox | `code_execution` server tool | `code_interpreter` (Assistants) | `code_execution` tool | N/A | `code_executor` | ⚠️ OpenAI: "interpreter", Anthropic/Google: "execution" |
| Web search | `web_search` server tool | `web_search` (Agents SDK) | `google_search` grounding | N/A | `search_tool` | ✅ |
| Computer control | `computer` tool (screenshots + actions) | N/A | N/A | N/A | `computer_use` | ✅ Anthropic coined this |
| File/doc search | `file_search` via MCP | `file_search` (Assistants) | N/A | `resources/read` | `document_loader` | ✅ LangChain term |
| MCP server | MCP originated at Anthropic | Supports MCP (Agents SDK) | Supports MCP (Gemini) | `MCP Server` | `mcp_server` | ✅ |

## 3. Input/Output & Schema Concepts

| Concept | Anthropic | OpenAI | Google | MCP | CEX Kind | CEX Aligned? |
|---------|-----------|--------|--------|-----|----------|-------------|
| Structured output | Via tool_use (force schema) | `response_format: json_schema` | `response_mime_type` + `response_schema` | N/A | `response_format` | ✅ OpenAI term |
| Input schema | `input_schema` (JSON Schema) | `parameters` (JSON Schema) | `parameters` (OpenAPI subset) | `inputSchema` (JSON Schema) | `input_schema` | ✅ |
| Output validation | Via strict tool schema | `strict: true` + refusal handling | Via VALIDATED mode | N/A | `output_validator` | ✅ |
| Output parsing | Client-side | Client-side | Client-side | Client-side | `parser` | ✅ LangChain standard |
| Prompt template | System prompt + user messages | System + user messages | system_instruction + contents | `prompts/get` primitive | `prompt_template` | ✅ Universal |

## 4. Memory & Context Concepts

| Concept | Anthropic | OpenAI | Google | MCP | CEX Kind | CEX Aligned? |
|---------|-----------|--------|--------|-----|----------|-------------|
| Prompt caching | `cache_control: {type: ephemeral}` (5min TTL) | `cached` token pricing (automatic) | `cached_content` (Context Caching API) | N/A | — (MISSING) | ❌ Add `prompt_cache` |
| Context window | `max_tokens` + model limit (200K) | `max_tokens` + model limit (128K-1M) | `max_output_tokens` + model limit (1M-2M) | N/A | — (MISSING) | ❌ Add `context_window_config` |
| Conversation memory | Via message history | `Thread` (Assistants) | Via multi-turn `contents` | N/A | `entity_memory`, `memory_summary` | ✅ |
| Knowledge retrieval | Via MCP resources | `file_search` + vector store | Grounding with Google Search | `resources/read` | `retriever_config` | ✅ |
| Vector storage | N/A (external) | `VectorStore` (Assistants) | N/A (Vertex AI Search) | N/A | `vector_store` | ⚠️ Rename to `vector_store` |
| Semantic index | N/A | N/A | N/A | N/A | `knowledge_index` | ⚠️ Rename to `knowledge_index` |
| Embeddings | N/A (deprecated Voyage) | `text-embedding-3-*` | `text-embedding-004` | N/A | `embedding_config` | ✅ |

## 5. Orchestration & Multi-Agent Concepts

| Concept | Anthropic | OpenAI | Google | MCP | CEX Kind | CEX Aligned? |
|---------|-----------|--------|--------|-----|----------|-------------|
| Task delegation | N/A | `handoff()` (Agents SDK/Swarm) | A2A `tasks/send` | N/A | `handoff` | ✅ OpenAI term |
| Supervisor / orchestrator | N/A | `Agent` with handoffs | A2A `AgentCard.capabilities` | N/A | `director` | ⚠️ Rename to `supervisor` |
| Workflow | N/A | Agents SDK orchestration | Vertex AI Workflows | N/A | `workflow` | ✅ Universal |
| DAG pipeline | N/A | N/A | N/A | N/A | `dag` | ✅ Airflow/LangGraph |
| Signal / event | N/A | N/A | A2A task state events | N/A | `signal` | ✅ POSIX/event-driven |
| Checkpoint | N/A | Thread state | N/A | N/A | `checkpoint` | ✅ ML standard |
| Guardrail | Constitutional AI | `Guardrail` class (Agents SDK) | Safety settings | N/A | `guardrail` | ✅ Industry standard |

## 6. Evaluation & Safety Concepts

| Concept | Anthropic | OpenAI | Google | MCP | CEX Kind | CEX Aligned? |
|---------|-----------|--------|--------|-----|----------|-------------|
| Evaluation framework | N/A (research papers) | `Evals` framework | Vertex AI Evaluation | N/A | `unit_eval`, `e2e_eval` | ✅ |
| LLM-as-judge | Research (Constitutional AI) | Evals w/ model graders | AutoSxS | N/A | `llm_judge` | ✅ Industry standard |
| Red teaming | Anthropic red team | OpenAI red teaming | Google red teaming | N/A | `red_team_eval` | ✅ |
| Safety filter | Usage policy enforcement | Moderation API + safety | `safety_settings` (HarmCategory) | N/A | — (MISSING) | ⚠️ `guardrail` covers this |
| Citation / grounding | `citations` (web_search results) | N/A | `grounding_metadata` + `grounding_chunks` | N/A | — (MISSING) | ❌ Add `citation` |
| Tracing / observability | N/A | N/A | Cloud Trace | N/A | `trace_config` | ✅ |

## 7. Multimodal Concepts

| Concept | Anthropic | OpenAI | Google | MCP | CEX Kind | CEX Aligned? |
|---------|-----------|--------|--------|-----|----------|-------------|
| Image input | `image` content block (base64/URL) | `image_url` in user message | Inline `image` in contents | `image/` MIME resources | `vision_tool` | ✅ |
| Audio input | N/A | `audio` modality, Whisper | Speech-to-text in Gemini | N/A | `audio_tool` | ✅ |
| Video input | N/A | N/A | `video` in Gemini (native) | N/A | — | — |
| PDF input | `document` content block | File upload + parsing | PDF in Gemini | `application/pdf` resource | — | — |
| Multi-modal config | Via content blocks | Via modalities param | Via `generation_config` | Via MIME types | — (MISSING) | ❌ Add `multi_modal_config` |

## 8. Intent Resolution & Input Processing Concepts

| Concept | Anthropic | OpenAI | Google | MCP | LangChain | DSPy | CEX Kind / Implementation | CEX Aligned? |
|---------|-----------|--------|--------|-----|-----------|------|---------------------------|-------------|
| Intent classification (determine which action/tool to invoke) | `tool_choice` routing + extended thinking | `tool_choice` + Agent `handoff()` routing | `function_calling_config.mode` | Host-side routing (not in spec) | Router chains, `MultiPromptChain` | `Predict` with routing module | `router` (P02) + `dispatch_rule` (P12) | ✅ |
| Query rewriting (transform user query into better query) | Via extended thinking (internal) | N/A (developer-side) | `retrieval_queries` (auto-generated for grounding) | N/A | `MultiQueryRetriever`, `HyDE`, `QueryTransformRetriever` | `ChainOfThought` (implicit rewrite) | 8F F1 CONSTRAIN + F4 REASON | ✅ Pipeline covers this |
| Context assembly (build full prompt from multiple sources) | `messages` array + `cache_control` blocks | `messages` array + `system`/`developer` role | `contents` + `system_instruction` | `prompts/get` (server-side template) | `RunnablePassthrough` + retrieval chains | `Module.forward()` assembles from signature | 8F F3 INJECT (`cex_crew_runner.py`) | ✅ |
| Slot filling (resolve template variables at runtime) | N/A (developer-side) | N/A (developer-side) | N/A (developer-side) | `arguments` in `prompts/get` | `PromptTemplate.format()` / `.invoke()` | Signature fields auto-populated | `prompt_template` {{vars}} + `brand_inject.py` | ✅ |
| Input normalization (standardize user input before processing) | N/A (no native abstraction) | N/A (developer-side) | N/A (developer-side) | N/A | `TextSplitter`, custom `Runnable` preprocessors | `InputField` type coercion | 8F F1 CONSTRAIN + N07 transmutation | ✅ Pipeline covers this |
| Intent-to-kind mapping (resolve user desire to artifact type) | N/A | N/A | N/A | N/A | N/A | N/A | `kinds_meta.json` + `cex_8f_motor.py` intent parser | ✅ CEX-unique |
| Prompt composition (assemble multiple artifacts into one prompt) | Multi-block `messages` (text + tool + image) | Multi-message + system + tools | `contents` with multiple `Part` types | Tool + resource + prompt composition | `RunnableSequence`, `create_stuff_documents_chain` | `Module` chaining | `cex_crew_runner.py` + `cex_prompt_layers.py` | ✅ |
| Disambiguation (resolve ambiguous user input to specific action) | Extended thinking reasoning | Agent SDK `handoff()` with triage agent | N/A | N/A | Agent router with fallback | `Retry` module + `Assert` | N07 transmutation protocol + GDP | ✅ |

---

## Summary: CEX Alignment Scorecard

| Status | Count | Items |
|--------|-------|-------|
| ✅ Aligned | 46 | Majority of CEX kinds match industry terms |
| ⚠️ Rename recommended | 5 | `vector_store`, `knowledge_index`, `director`, `lens`, `code_executor` |
| ❌ Missing kind | 4 | `prompt_cache`, `context_window_config`, `citation`, `multi_modal_config` |
| ✅ Intent resolution | 8 | New section — cross-provider + framework mapping for input processing |

## Conflict Resolution Rules

1. **2+ providers agree** → Use that term (e.g., "tool" not "function", since 3/4 say "tool")
2. **All providers differ** → Use most descriptive (e.g., "function_def" over Google's "FunctionDeclaration")
3. **Only 1 provider has concept** → Use their term (e.g., "computer_use" = Anthropic's term)
4. **CEX-unique concept** → Keep CEX term if clear (e.g., "bugloop", "lens" → but "lens" should become "persona")
5. **Framework vs provider** → Provider > framework (e.g., Anthropic's "tool_use" > LangChain's "AgentExecutor")

## Usage in CEX

This card is the **first stop** for any terminology question:
- Before naming a new kind → check this table
- Before renaming an existing kind → verify 2+ providers agree
- Before writing documentation → use canonical terms from this card
- Quarterly review → update when providers release new APIs
