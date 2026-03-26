---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for chain production
sources: LangChain, DSPy, Anthropic prompt chaining guide, pipeline design patterns
---

# Domain Knowledge: chain

## Foundational Concept
Prompt chaining decomposes complex LLM tasks into sequential steps where each step's
output feeds the next step's input. Formalized in LangChain's SequentialChain and
DSPy's Module composition. Core principle: each step does ONE thing well, with typed
inputs/outputs enabling reliable composition without agent overhead.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| LangChain SequentialChain | Chains of LLMChains with variable passing | Direct: our chain steps with I/O |
| DSPy Module composition | Composable modules with typed signatures | Informs: typed I/O per step |
| Anthropic prompt chaining | Best practices for multi-step prompts | Informs: step atomicity, error strategy |
| LangGraph | Stateful graph-based chains with branching | Extends: our branching/parallel flow types |
| LCEL (LangChain Expression Language) | Pipe operator for chain composition | Related: declarative chain definition |

## Key Patterns
- Atomic steps: 1 step = 1 LLM call with 1 clear purpose
- Typed contracts: explicit input/output types prevent data mismatches between steps
- Context passing strategies: full (all prior output), filtered (relevant subset), summary (compressed)
- Error propagation: fail_fast for critical paths, skip for enrichment steps
- Step independence: each step testable in isolation (unit_eval compatible)
- Data flow diagrams: ASCII visualizations prevent hidden dependencies
- Narrowing funnel: early steps gather, later steps filter and refine

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| steps_count | Integrity check: count matches body | No direct equivalent |
| flow | Explicit flow type (sequential/branching/parallel/mixed) | LangGraph routing |
| context_passing | Strategy for inter-step context | LangChain memory patterns |
| error_strategy | Chain-level error handling policy | LangChain error callbacks |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT chain |
|------|------------|---------------------|
| workflow (P12) | Runtime orchestration with agents+tools+signals | Chains are text-only, no agent coordination |
| dag (P12) | Dependency graph without execution semantics | Chains define execution, not just dependencies |
| chain_of_thought (P03) | Reasoning technique within single prompt | CoT is intra-prompt, chain is inter-prompt |
| instruction (P03) | Step-by-step recipe for one agent | Instruction guides humans/agents, chain composes LLM calls |
| prompt_template (P03) | Reusable template with {{vars}} | Template is single-step with slots, chain is multi-step |

## References
- LangChain: SequentialChain, LCEL documentation
- DSPy: Module composition and typed signatures
- Anthropic: Prompt chaining best practices
- LangGraph: Stateful graph-based chains
