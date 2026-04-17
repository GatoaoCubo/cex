---
id: p01_report_intent_resolution
kind: knowledge_card
type: domain
pillar: P01
title: "Intent Resolution in Agent Frameworks -- Cross-Industry Pattern Survey"
version: 1.0.0
created: 2026-04-08
updated: 2026-04-08
author: N01_intelligence
domain: intent-resolution
origin: src_standards_global
quality: 8.9
tags: [intent, resolution, transmutation, query-transformation, routing, NLU, compiler, survey]
tldr: "Survey of how 13 frameworks handle the transformation of vague human input into precise LLM-consumable instructions. Maps CEX 'transmutation' to canonical industry terms. Identifies 5 CEX strengths and 8 gaps."
when_to_use: "When naming or redesigning CEX's input processing pipeline. When comparing CEX against industry patterns."
keywords: [intent-resolution, query-transformation, slot-filling, routing, prompt-composition, NLU, compiler-front-end]
long_tails:
  - "what is the industry term for transforming vague user input into LLM instructions"
  - "how do LangChain DSPy CrewAI handle intent classification compared"
  - "canonical term for query rewriting across agent frameworks 2026"
axioms:
  - "No single framework uses one term -- the pattern is always a COMPOSITE of 3-5 sub-patterns"
  - "The industry converges on 'intent resolution' (NLU) + 'query transformation' (IR) as the two pillars"
  - "CEX's unique contribution is taxonomy mapping -- no other framework does kind/pillar/nucleus routing"
feeds_kinds: [knowledge_card, glossary_entry, context_doc, router, instruction]
linked_artifacts:
  related:
    - .claude/rules/n07-input-transmutation.md
    - .claude/rules/n07-technical-authority.md
    - _docs/specs/spec_metaphor_dictionary.md
    - P01_knowledge/library/domain/_reference/kc_terminology_rosetta_stone.md
    - P01_knowledge/library/domain/_reference/kc_routing_resilience.md
    - P01_knowledge/library/domain/patterns/kc_query_decomposition.md
density_score: 0.93
---

# Intent Resolution in Agent Frameworks

## Executive Summary

CEX calls it "transmutation." The industry has no single term -- the pattern is a **composite** of 3-5 sub-patterns that every framework implements differently. After surveying 13 frameworks, 3 academic domains, and 2 protocol specs, the closest canonical terms are:

| Scope | Canonical Term | Domain |
|-------|---------------|--------|
| Full pipeline | **Intent Resolution Pipeline** | NLU / Dialog Systems |
| Query rewriting | **Query Transformation** | Information Retrieval |
| Parameter extraction | **Slot Filling** | NLU / Conversational AI |
| Handler selection | **Intent Routing** | Agent Frameworks |
| Context assembly | **Prompt Composition** | Prompt Engineering |
| Input-to-IR | **Front-End Compilation** | Compiler Theory |

**Recommendation**: Rename CEX "transmutation" to **"Intent Resolution Pipeline"** (IRP). It is the most descriptive, maps to NLU literature, and encompasses all 5 sub-patterns CEX implements.

---

## Part 1: Industry Term Survey

### 1.1 Agent Frameworks

| Framework | Term for Input->Instruction | Sub-Components | How It Works |
|-----------|---------------------------|----------------|--------------|
| **LangChain** | **Query Transformation** (umbrella) | Multi-Query Retriever, Step-Back Prompting, HyDE, Query Decomposition | LLM rewrites user query into 1+ reformulated queries. Modern routing via LangGraph `add_conditional_edges()` replaces deprecated `RouterChain`. Context assembly via LCEL `RunnablePassthrough.assign()`. Structured output via `.with_structured_output(PydanticModel)`. |
| **LlamaIndex** | **Query Transformation** (module: `query_transformations`) | RouterQueryEngine, SubQuestionQueryEngine, HyDE, StepDecomposeQueryTransform | `RouterQueryEngine` + `Selector` (LLM/Pydantic) picks which query engine handles input. `SubQuestionQueryEngine` decomposes complex queries into N sub-questions routed by metadata. No explicit slot filling -- Selector metadata matching serves as implicit disambiguation. |
| **DSPy** | **Prompt Compilation / Optimization** | Signature, Module, Optimizer (Teleprompter), Assertion | DSPy IS the transmutation framework. `Signature` declares I/O fields. `Module` wraps parameterized LLM calls. `Optimizer` (formerly Teleprompter) automatically tunes prompts from examples. Intent is captured declaratively, not through rewriting. The entire framework replaces manual prompt engineering with compiled optimization. |
| **CrewAI** | **Task Description Interpolation + Planning + Hierarchical Delegation** | Task.description, AgentPlanner, Manager Agent, human_input | No single named module. Developer pre-structures intent via `Task.description` + `expected_output`. `AgentPlanner` (`planning=True`) generates step-by-step plan before execution. `Manager Agent` in hierarchical process routes by matching task against agent `role`/`goal`/`backstory`. `human_input=True` enables explicit user clarification. |
| **AutoGen** | **Speaker Selection + Nested Chat** | ConversableAgent, GroupChat, GroupChatManager, speaker_selection_method | `GroupChatManager` routes messages to the correct agent via `speaker_selection_method` (round_robin, random, auto, or custom function). `auto` mode uses LLM to classify which agent should speak next. `Nested chat` enables complex multi-step flows. No query rewriting -- agents respond to raw input. |
| **Semantic Kernel** | **Intent Detection + Planner** | KernelFunction, Planner (Handlebars/Stepwise), Plugin | `Planner` decomposes user goal into a plan of `KernelFunction` calls. Stepwise planner iteratively refines. Intent mapped to available plugins/functions via description matching. |

### 1.2 LLM Providers

| Provider | Term for Input->Instruction | Sub-Components | How It Works |
|----------|---------------------------|----------------|--------------|
| **OpenAI Assistants** | **Instructions + Function Calling** | Thread, Run, instructions, tools | `instructions` field defines agent behavior. Function calling forces structured output with JSON Schema. No explicit query transformation -- the model resolves intent internally. |
| **OpenAI Agents SDK** | **Triage Agent + Handoff** | Agent, handoff(), guardrail, Runner | **Triage pattern**: a triage agent classifies user intent and `handoff()`s to specialist agents. Each agent has `instructions` + `tools`. Guardrails validate input/output. This is the closest to CEX's transmutation -- explicit routing layer before execution. |
| **Anthropic Claude** | **System Prompt + Tool Use + Prefill** | system parameter, tool definitions, assistant prefill | System prompt defines behavioral context. Tool use forces structured output via `input_schema`. Assistant prefill guides output format. No named "intent resolution" module -- patterns described in prompt engineering docs. Extended thinking provides chain-of-thought reasoning. |
| **Google Gemini** | **System Instruction + Function Calling + Grounding** | system_instruction, FunctionDeclaration, google_search grounding | `system_instruction` sets context. Function calling maps to available tools. Google Search grounding retrieves live data. Vertex AI Agent Builder uses Dialogflow CX intents for explicit NLU. |

### 1.3 Protocols

| Protocol | Term for Input->Instruction | Sub-Components | How It Works |
|----------|---------------------------|----------------|--------------|
| **MCP** | **Prompts + Resources + Sampling** | prompts/get, resources/read, tools/call, sampling/createMessage | `prompts/get` retrieves structured prompt templates with arguments. `resources/read` provides context. `sampling` enables server-initiated LLM calls. MCP itself does not transform queries -- it provides primitives that hosts use for transformation. |
| **A2A** | **Capability-Based Routing via AgentCard** | AgentCard, Task, Message, capabilities | `AgentCard` declares agent capabilities (skills, supported content types). Client matches user intent against AgentCard capabilities to select the right agent. `Task` wraps the interaction. Routing is capability-matching, not query rewriting. |

### 1.4 Academic / Foundational Domains

| Domain | Term for Input->Instruction | Sub-Patterns | How It Works |
|--------|---------------------------|--------------|--------------|
| **Compiler Theory** | **Front-End Compilation** (lexing -> parsing -> semantic analysis -> IR) | Lexical analysis, Syntax parsing, Semantic analysis, Type inference, Intermediate Representation | Source code (vague) -> tokens -> AST -> typed AST -> IR (precise). The closest analogy to transmutation: raw text is progressively refined into an unambiguous intermediate representation that the back-end can execute. Type inference fills gaps the programmer left implicit. |
| **NLU / NLP** | **Intent Resolution** (classification + slot filling + dialog state tracking) | Intent Classification, Entity Extraction (NER), Slot Filling, Dialog State Tracking (DST), Dialog Management | User utterance -> classify intent (e.g., "book_flight") -> extract entities (e.g., city="NYC", date="tomorrow") -> fill required slots -> track state across turns -> select action. This is the most mature formalization of "transmutation." |
| **Search / IR** | **Query Understanding** (rewriting + expansion + classification) | Query Rewriting, Query Expansion, Spell Correction, Entity Resolution, Query Relaxation, Query Classification | User query -> correct spelling -> expand with synonyms -> classify intent (navigational/informational/transactional) -> rewrite for retrieval -> execute. Google calls this layer "Query Understanding" internally. |

---

## Part 2: Pattern Decomposition

CEX's "transmutation" decomposes into 6 sub-steps. Each has a canonical industry term:

| CEX Step | CEX Description | Canonical Term | Used By | Maturity |
|----------|----------------|---------------|---------|----------|
| 1. Capture intent | What does the user WANT? | **Intent Classification** (NLU) | Dialogflow CX, Rasa, Amazon Lex, every NLU system | Very High -- 20+ years of research |
| 2. Map to taxonomy | Which kind? pillar? nucleus? | **Capability Matching / Service Discovery** (SOA, A2A) | A2A AgentCard, MCP tool discovery, Kubernetes service mesh | High -- SOA pattern since 2000s |
| 3. Resolve ambiguity | Fill gaps the user left | **Slot Filling** (NLU) + **Type Inference** (compilers) | Dialogflow, Rasa, every dialog system; Hindley-Milner type inference | Very High -- core NLU primitive |
| 4. Restate in precise terms | Show user what was understood | **Confirmation / Grounding** (dialog systems) | Alexa ("Did you mean...?"), Google Assistant, Siri | High -- standard UX pattern |
| 5. Teach correct term | User learns industry jargon | **Pedagogical Feedback / Terminology Alignment** | No direct industry equivalent -- CEX-unique | Low -- novel pattern |
| 6. Execute structured | LLM-to-LLM language | **Prompt Composition + Structured Invocation** | Every framework (system prompt + tools + context) | Very High -- universal |

### Comparative: How Each Framework Handles Each Sub-Step

| Sub-Step | LangChain | LlamaIndex | DSPy | CrewAI | OpenAI Agents SDK | Anthropic |
|----------|-----------|------------|------|--------|-------------------|-----------|
| 1. Classify | LangGraph conditional edge | RouterQueryEngine Selector | Signature (declarative) | Manager Agent matching | Triage Agent | System prompt |
| 2. Map | Node routing in StateGraph | QueryEngineTool selection | Module composition | Agent role/goal match | handoff() to specialist | Tool selection |
| 3. Fill gaps | `.with_structured_output()` | SubQuestionQueryEngine | Assertion constraints | `human_input=True` | Guardrail validation | Tool `input_schema` |
| 4. Confirm | Not built-in | Not built-in | Not built-in | `human_input=True` | Not built-in | Not built-in |
| 5. Teach | Not built-in | Not built-in | Not built-in | Not built-in | Not built-in | Not built-in |
| 6. Execute | LCEL chain invocation | QueryEngine.query() | Module.__call__() | Crew.kickoff() | Runner.run() | messages.create() |

**Key finding**: Steps 4 (Confirmation) and 5 (Teaching) are **unique to CEX**. No surveyed framework implements pedagogical terminology alignment. This is a genuine differentiator.

---

## Part 3: Related Patterns

All patterns that boost LLM performance from imprecise input, organized by mechanism:

### 3.1 Pre-Processing Patterns (Before LLM Call)

| Pattern | What It Does | Frameworks That Use It | CEX Equivalent |
|---------|-------------|----------------------|----------------|
| **Query Rewriting** | LLM reformulates user query for better retrieval | LangChain (MultiQueryRetriever), LlamaIndex (HyDE), Google (query expansion) | Transmutation step 1-3 |
| **Query Decomposition** | Split complex query into atomic sub-queries | LangChain (Query Decomposition), LlamaIndex (SubQuestionQueryEngine) | kc_query_decomposition.md |
| **Step-Back Prompting** | Generate a more abstract/general question first | LangChain (StepBackPrompting), academic (Zheng et al. 2023) | Not implemented |
| **Intent Classification** | Categorize user input into predefined intents | Dialogflow CX, Rasa, LangGraph, OpenAI Agents SDK (triage) | Transmutation step 1 |
| **Slot Filling** | Extract required parameters from utterance | Dialogflow, Rasa, Amazon Lex, every NLU system | Transmutation step 3 |
| **Entity Extraction (NER)** | Identify named entities in input | spaCy, Hugging Face, Google NL API | Not explicit in CEX |
| **Spell/Grammar Correction** | Fix typos before processing | Google Search, Bing, search engines | Not implemented |

### 3.2 Context Assembly Patterns (Building the Prompt)

| Pattern | What It Does | Frameworks That Use It | CEX Equivalent |
|---------|-------------|----------------------|----------------|
| **Prompt Composition** | Assemble system + user + context into prompt | All frameworks (universal) | 8F pipeline (F2 BECOME + F3 INJECT) |
| **RAG (Retrieval-Augmented Generation)** | Retrieve relevant docs, inject into prompt | LangChain, LlamaIndex, Anthropic (MCP), Google (grounding) | F3 INJECT + retriever_config |
| **Few-Shot Injection** | Add examples to guide output format | All frameworks (universal) | few_shot_example kind |
| **System Prompt Engineering** | Craft behavioral instructions | All providers | system_prompt kind |
| **Context Window Management** | Budget tokens across context sections | LangChain (token counting), Anthropic (cache_control) | cex_token_budget.py |
| **Memory Injection** | Load conversation/entity memory | LangChain (ConversationBufferMemory), OpenAI (Threads) | cex_memory_select.py |

### 3.3 Reasoning Patterns (During LLM Call)

| Pattern | What It Does | Frameworks That Use It | CEX Equivalent |
|---------|-------------|----------------------|----------------|
| **Chain-of-Thought (CoT)** | Elicit step-by-step reasoning | Universal (Wei et al. 2022) | 8F sequential reasoning |
| **Self-Reflection / Self-Correction** | LLM checks and revises own output | Reflexion (Shinn et al. 2023), LangGraph loops | F7 GOVERN (quality gate) |
| **Tree-of-Thought** | Explore multiple reasoning paths | Academic (Yao et al. 2023) | Not implemented |
| **ReAct (Reasoning + Acting)** | Interleave reasoning with tool calls | LangChain (ReAct agent), most agent frameworks | 8F pipeline (F4 REASON + F5 CALL) |

### 3.4 Post-Processing Patterns (After LLM Call)

| Pattern | What It Does | Frameworks That Use It | CEX Equivalent |
|---------|-------------|----------------------|----------------|
| **Output Parsing** | Extract structured data from LLM output | LangChain (OutputParser), LlamaIndex (OutputParser) | parser kind |
| **Output Validation** | Verify output meets schema | OpenAI (strict mode), Anthropic (tool schemas) | output_validator kind |
| **Guardrails** | Reject harmful/invalid output | OpenAI Agents SDK, NeMo Guardrails, Anthropic (Constitutional AI) | guardrail kind |
| **Structured Output Forcing** | Force JSON/schema compliance | OpenAI (json_schema), Anthropic (tool_use), Google (response_schema) | response_format kind |

---

## Part 4: CEX Gap Analysis

### 4.1 What CEX Does Better Than Industry

| CEX Strength | Why It Matters | Industry Comparison |
|-------------|---------------|-------------------|
| **Taxonomy-driven routing** (kind/pillar/nucleus) | Input maps to a 123-kind ontology, not just "which agent." Ensures output type, location, and format are pre-determined. | No framework has an equivalent ontology. LangChain routes to chains/tools. CrewAI routes to agents. Neither routes to a typed artifact schema. |
| **Pedagogical feedback** (step 5: teach) | User learns industry terms over time, reducing future ambiguity. Creates a positive learning loop. | Unique to CEX. No surveyed framework teaches users terminology. All accept raw input silently. |
| **Confirmation/restatement** (step 4) | Shows user what the system understood before executing. Prevents costly misinterpretation. | Only CrewAI (`human_input=True`) offers a weak version. Dialogflow has slot confirmation prompts. CEX's is more comprehensive. |
| **Full-pipeline trace** (8F) | Every resolution step is logged (F1-F8). Debuggable, auditable, reproducible. | LangSmith (LangChain) offers tracing but not at the intent-resolution level. Most frameworks are opaque. |
| **Terminology enforcement** across all output | Output always uses industry terms regardless of input language. Prevents jargon drift across agents. | No equivalent. Frameworks output in whatever terms the prompt uses. |

### 4.2 What CEX Is Missing

| Gap | Industry Pattern | Who Does It Well | Impact if Added | Priority |
|-----|-----------------|-----------------|-----------------|----------|
| **Semantic intent classification** | Embedding-based cosine similarity against intent vectors | LangChain (SemanticRouter), Dialogflow CX (ML-based intent matching) | Replaces brittle keyword matching with semantic understanding. "deploy my app" and "ship my code" would match the same intent even without explicit mapping. | HIGH |
| **Confidence scoring** | Report match confidence (0.0-1.0) on intent classification | Dialogflow CX (confidence threshold), Rasa (intent ranking), LlamaIndex (Selector scores) | Enables fallback: "I'm 60% sure you mean X -- is that right?" vs. silent misrouting. | HIGH |
| **Query decomposition at resolution time** | Split complex input into sub-intents before routing | LlamaIndex (SubQuestionQueryEngine), LangChain (QueryDecomposition) | "Research competitors AND build a pricing page" would be split into N01 + N03 tasks automatically instead of requiring N07 manual decomposition. | MEDIUM |
| **Step-back prompting** | Generate abstract question first, then specific | LangChain (StepBackPrompting), academic literature | "Fix the auth bug" -> first ask "What is the auth architecture?" then "What could cause this specific bug?" Better context gathering. | MEDIUM |
| **Entity extraction (NER)** | Extract named entities from input | spaCy, Hugging Face, Google NL API, Dialogflow CX | "Research Stripe and PayPal pricing" would extract entities [Stripe, PayPal] and tag them as [competitors], feeding structured data to N01. | LOW |
| **Multi-turn clarification protocol** | Systematic follow-up questions when slots are missing | Dialogflow CX (slot filling prompts), Rasa (forms), Amazon Lex | CEX has GDP (ask user) but no structured multi-turn dialog for progressive slot filling. GDP is all-or-nothing. | MEDIUM |
| **Feedback loop on resolution quality** | Track which resolutions succeeded/failed and learn | DSPy (Optimizer learns from examples), Rasa (interactive learning) | Over time, the system would learn that "fix tests" -> N05 is correct 95% of the time, and "make content" -> needs clarification 80% of the time. | LOW |
| **HyDE (Hypothetical Document Embeddings)** | Generate hypothetical answer to improve retrieval | LlamaIndex (HyDE), LangChain (HyDE) | When resolving "build me something for onboarding," generate a hypothetical artifact first, embed it, then find the closest real artifacts/builders. Better F3 INJECT. | LOW |

### 4.3 Recommendation Summary

| Action | What to Do | Impact |
|--------|-----------|--------|
| **Rename** | "Transmutation" -> "Intent Resolution Pipeline" (IRP) | Aligns with NLU literature. Searchable, teachable, precise. |
| **Add** | Confidence scoring to intent classification | Prevents silent misrouting. Enables "did you mean?" UX. |
| **Add** | Semantic similarity fallback for unmapped intents | Handles novel inputs without explicit mapping table entries. |
| **Integrate** | Query decomposition into IRP (before routing) | Multi-intent inputs ("research X AND build Y") auto-split into parallel tasks. |
| **Formalize** | GDP as a slot-filling dialog (not all-or-nothing) | Progressive clarification instead of 6 questions upfront. |
| **Keep** | Pedagogical feedback (step 5: teach) | Genuine differentiator. No competitor does this. |
| **Keep** | Taxonomy-driven routing (kind/pillar/nucleus) | Structural advantage. Maps to typed output, not just agent selection. |
| **Keep** | Full 8F trace | Observability advantage. |

---

## Appendix A: Term Frequency Across Surveyed Sources

| Term | Frameworks Using It | Verdict |
|------|-------------------|---------|
| Query Transformation | LangChain, LlamaIndex | Standard in RAG/IR context |
| Intent Classification | Dialogflow, Rasa, Amazon Lex, NLU literature | Universal in dialog systems |
| Slot Filling | Dialogflow, Rasa, Lex, NLU literature | Universal in dialog systems |
| Triage | OpenAI Agents SDK | Provider-specific |
| Query Understanding | Google Search, Bing, search literature | Standard in search/IR |
| Front-End Compilation | Compiler textbooks (Aho, Appel) | Academic analogy |
| Prompt Compilation | DSPy | Framework-specific |
| Speaker Selection | AutoGen | Framework-specific |
| Routing | LangGraph, LlamaIndex, A2A | Universal in agent systems |
| Planning | CrewAI, Semantic Kernel | Common in agent frameworks |
| Handoff | OpenAI Agents SDK, CEX | Emerging standard (2 users) |
| Capability Matching | A2A, MCP | Standard in service discovery |
| Transmutation | CEX only | CEX-specific (non-standard) |
| Intent Resolution | NLU literature, dialog systems | Most comprehensive single term |

## Appendix B: CEX Transmutation Steps -> Industry Term Mapping

| CEX Step | Current Name | Recommended Rename | Source |
|----------|-------------|-------------------|--------|
| Full pipeline | "Transmutation" | **Intent Resolution Pipeline** | NLU / Dialog Systems |
| Step 1 | "Capture intent" | **Intent Classification** | NLU (Dialogflow, Rasa) |
| Step 2 | "Map to CEX taxonomy" | **Capability Matching** | SOA / A2A / Service Discovery |
| Step 3 | "Resolve ambiguity" | **Slot Filling** | NLU (Dialog State Tracking) |
| Step 4 | "Restate in precise terms" | **Confirmation Grounding** | Dialog Systems (Grounding Theory) |
| Step 5 | "Teach correct term" | **Pedagogical Feedback** (keep -- CEX-unique) | Novel |
| Step 6 | "Execute structured" | **Structured Invocation** | Agent Frameworks (universal) |

## Appendix C: Sources

| Source | Type | Date |
|--------|------|------|
| LangChain Docs: Query Transformations | Official docs | 2025 |
| LangGraph Docs: Branching + Conditional Edges | Official docs | 2025 |
| LlamaIndex Docs: Router, SubQuestion, QueryTransform | Official docs | 2025 |
| DSPy: Signatures, Modules, Optimizers | Official docs + paper (Khattab et al.) | 2024-2025 |
| CrewAI Docs: Hierarchical Process, Planning, Tasks | Official docs | 2025 |
| AutoGen Docs: GroupChat, Speaker Selection | Official docs | 2025 |
| OpenAI Agents SDK: Handoffs, Triage pattern | Official docs | 2025 |
| Anthropic: Tool Use, System Prompts, Prompt Engineering | Official docs | 2025 |
| Google: Gemini API, Dialogflow CX, Vertex AI Agent Builder | Official docs | 2025 |
| MCP Spec: prompts, resources, tools, sampling | Protocol spec (2025-06-18) | 2025 |
| A2A Protocol: AgentCard, Task, capabilities | Google spec | 2025 |
| Aho et al., Compilers: Principles, Techniques, and Tools | Textbook (3rd ed.) | 2022 |
| Jurafsky & Martin, Speech and Language Processing (Ch. 15: Dialog) | Textbook (3rd ed.) | 2024 |
| Wei et al., Chain-of-Thought Prompting (NeurIPS) | Paper | 2022 |
| Khattab et al., DSPy: Compiling Declarative Language Model Calls | Paper | 2024 |
| Zheng et al., Take a Step Back: Evoking Reasoning via Abstraction | Paper | 2023 |

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**
