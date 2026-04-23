# P03 Prompt — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| DSPy Signatures | Programmatic prompts | Signature (input→output fields), InputField, OutputField, Module, Predict, ChainOfThought, ReAct |
| Guidance | Constrained generation | Program (handlebars syntax), gen(), select(), block, role markers (system/user/assistant) |
| LMQL | Query language for LLMs | LMQL query, constraint clauses (where/stops), decoder (argmax/sample/beam), distribution |
| Outlines | Structured generation | Generator, RegexGuide, JSONGuide, CFGGuide, FSMGuide, Choice, Format |
| Instructor | Structured extraction | client.chat.completions.create(response_model=), retry, validation_context, Partial, Iterable |
| Priompt | Priority-based prompts | Scope, priority levels, token budget, overflow handling, first/last isolation |
| PromptLayer | Prompt management | PromptTemplate, version, A/B test, publish, track, score, metadata, registry |
| LangChain PromptTemplate | Template engine | PromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, FewShotPromptTemplate, PipelinePromptTemplate |
| Prompt Caching | Token reuse | Anthropic cache_control, OpenAI cached prompts, prefix caching, breakpoint |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| System Prompt/Message | LangChain, Guidance (role:system), DSPy (implicit), Instructor (system msg), Anthropic, OpenAI | Identity + rules injected as system message | 6 |
| Prompt Template | LangChain, PromptLayer, DSPy (Signature), Guidance (program), Priompt (scope) | Reusable prompt with variables/slots | 6 |
| Chain/Pipeline | LangChain (SequentialChain), DSPy (Module composition), Guidance (sequential blocks) | Ordered sequence of prompt steps where output feeds next input | 3 |
| User/Action Prompt | LangChain (HumanMessage), DSPy (InputField), Guidance (role:user), LMQL (query body) | The task/question sent by human or orchestrator | 5 |
| Constrained Generation | Outlines (RegexGuide, JSONGuide), LMQL (where clause), Guidance (select/gen), Instructor (response_model) | Forcing LLM output to match a schema/regex/grammar | 4 |
| Prompt Versioning | PromptLayer (version+publish), DSPy (optimized prompts), LangChain Hub | Track, version, and roll back prompt changes | 3 |
| Few-shot Injection | LangChain (FewShotPromptTemplate), DSPy (BootstrapFewShot), PromptLayer | Dynamically selecting and injecting examples into prompts | 3 |
| Token Priority/Budget | Priompt (priority scopes), Anthropic (cache_control breakpoints), prompt compression | Managing which prompt sections survive token limits | 2 |
| Prompt Optimization | DSPy (MIPRO, BootstrapFewShot), PromptLayer (A/B test) | Automatic improvement of prompts via search/eval | 2 |
| Role Markers | Guidance, LangChain, LMQL, Instructor | system/user/assistant turn delimiters | 4 |
| Instruction Block | DSPy (Signature docstring), LangChain (system), Guidance (system block) | Step-by-step execution instructions embedded in prompt | 3 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| system_prompt | System Prompt/Message | 95% | Excellent. Direct 1:1 match with industry. CEX adds quality scoring. |
| prompt_template | Prompt Template | 90% | Strong alignment. CEX uses {{mustache}} vars, industry uses {f-string} or Jinja2. Semantically identical. |
| chain | Chain/Pipeline | 75% | Good match. Industry chains are more programmatic (DSPy Module, LangChain LCEL). CEX chain is more declarative. |
| action_prompt | User/Action Prompt | 85% | Well-aligned. CEX adds structured input_required/output_expected. Industry is more freeform. |
| instruction | Instruction Block | 80% | Reasonable match. Overlaps with DSPy Signature docstring and LangChain system message instructions. Boundary with system_prompt could be clearer. |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| constraint_spec | Constrained generation rules: regex patterns, JSON schema refs, grammar rules, stop sequences. A distinct artifact from the prompt itself — it governs the decoder, not the LLM's reasoning. | Outlines, LMQL, Guidance, Instructor | high |
| prompt_version | Versioned prompt snapshot with metadata (author, A/B group, performance metrics, rollback pointer). Industry treats prompt versioning as first-class. CEX versions via git but lacks explicit version metadata per prompt. | PromptLayer, DSPy (optimized), LangChain Hub | med |
| cache_directive | Token caching configuration: which prompt sections to cache, breakpoints, TTL. Distinct from prompt content — it's an optimization layer. | Anthropic (cache_control), OpenAI (cached prefixes) | low |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| instruction | CLARIFY boundary | High overlap with system_prompt (both contain instructions). Industry typically puts instructions INSIDE system_prompt. Consider: instruction = standalone step-by-step for non-LLM consumers (humans, pipelines); system_prompt = LLM-consumed identity. |
| action_prompt | RENAME consideration | Industry overwhelmingly uses "user message" or "human message". CEX's "action_prompt" is clearer about intent but less recognizable. Keep name, add `industry_terms` to schema (already present). |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| system_prompt | LangChain SystemMessage, Guidance role:system, DSPy (implicit), OpenAI system, Anthropic system |
| prompt_template | LangChain PromptTemplate, PromptLayer PromptTemplate, DSPy Signature, Guidance program |
| chain | LangChain SequentialChain/LCEL, DSPy Module composition, Guidance sequential blocks |
| action_prompt | LangChain HumanMessage, DSPy InputField, Guidance role:user, LMQL query body |
| instruction | DSPy Signature docstring, LangChain system instructions (partial) |

## 7. Summary
Current: 5 kinds → Proposed: 8 kinds (+constraint_spec, +prompt_version, +cache_directive) | Coverage: ~85% → ~95%

Key insight: CEX's P03 is already well-aligned with industry. The biggest gap is **constrained generation** (Outlines, LMQL, Guidance, Instructor) — an entirely new category of prompt engineering that controls the decoder, not just the LLM's reasoning. Adding constraint_spec would capture this growing pattern. The instruction/system_prompt boundary overlap deserves clarification but both kinds are valid.
