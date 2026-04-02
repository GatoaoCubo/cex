---
id: p01_kc_python_testing_strategies_ai_agents
kind: knowledge_card
pillar: P01
title: "Python Testing Strategies for AI Agents"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
domain: ai_testing
quality: 9.2
tags: [python, testing, ai-agents, pytest, mocking, async, llm, knowledge]
tldr: "Test AI agents with pytest-asyncio for async flows, respx/responses for LLM API mocking, hypothesis for property-based state validation, and pact-python for contract testing"
when_to_use: "When building or validating test suites for Python-based LLM agents, tool-calling agents, or multi-step autonomous pipelines"
keywords: [pytest-asyncio, llm-mocking, agent-testing, respx, hypothesis, contract-testing]
long_tails:
  - How to mock OpenAI and Anthropic API calls in pytest without hitting real endpoints
  - How to test async LangChain or Claude agent workflows with pytest-asyncio
  - How to validate agent memory and conversation state across multiple turns
  - How to write chaos tests for LLM agent resilience and fallback behavior
axioms:
  - ALWAYS mock external LLM API calls in unit tests — never rely on live endpoints for determinism
  - NEVER assert on exact LLM output text — assert on structure, schema, and behavior
  - IF testing tool-calling agents, THEN validate tool selection logic independently from tool execution
  - ALWAYS seed random state in property-based tests to reproduce agent failures reliably
linked_artifacts:
  primary: null
  related: [p01_kc_prompt_caching, p01_kc_rag_fundamentals]
density_score: 0.91
data_source: "https://docs.pytest.org/en/stable/ | https://pytest-asyncio.readthedocs.io/"
---
# Python Testing Strategies for AI Agents

## Quick Reference
```yaml
topic: python_ai_agent_testing
scope: pytest, async testing, LLM API mocking, agent behavior validation
owner: testing_engineer
criticality: high
stack: pytest >= 7.4 | pytest-asyncio >= 0.23 | respx >= 0.21 | hypothesis >= 6.x
```

## Key Concepts

| Concept | Purpose | Library | Decorator / API |
|---------|---------|---------|-----------------|
| Async agent testing | Test coroutine-based agent loops | `pytest-asyncio` | `@pytest.mark.asyncio` |
| LLM API mocking | Deterministic fake responses | `respx`, `responses` | `respx.mock`, `@responses.activate` |
| Property-based testing | Fuzz agent state with random inputs | `hypothesis` | `@given(st.text())` |
| Contract testing | Validate AI service API schema | `pact-python` | `Pact().given().will_respond_with()` |
| Chaos testing | Inject failures, timeouts, partial responses | `pytest-httpx` | `httpx_mock.add_exception()` |
| Snapshot testing | Pin agent response structure over time | `syrupy` | `assert result == snapshot` |

## Strategy Phases

1. **Unit** — Mock LLM calls; test prompt construction, tool routing, output parsing in isolation
2. **Integration** — Stub external services; test multi-turn conversation state, memory persistence, tool orchestration
3. **Contract** — Validate OpenAI/Anthropic API schema compliance with pact; catch breaking API changes before deploy
4. **Behavioral** — Property-based tests over agent inputs; confirm invariants (never empty response, always valid JSON)
5. **Chaos** — Inject: rate-limit 429, timeout, partial stream, malformed JSON; verify fallback + retry behavior

## Golden Rules

- MOCK at the HTTP transport layer (`respx`, `pytest-httpx`) — not at the SDK client level — catches serialization bugs
- FIXTURE LLM responses as `.json` files; load in conftest.py for reuse across test modules
- SEPARATE tool-selection tests (does agent pick the right tool?) from tool-execution tests (does the tool work?)
- PARAMETRIZE model variants: `@pytest.mark.parametrize("model", ["gpt-4o", "claude-3-5-sonnet"])` on integration tests
- USE `anyio` backend fixture when mixing asyncio and trio in the same test suite

## Flow

```text
[Test Input] -> [respx.mock intercepts HTTP] -> [Agent receives fake LLM response]
                                                          |
                                              [Tool call? -> stub tool return]
                                                          |
                                              [Assert: output schema, state delta, signal]
                                                          |
                                              [hypothesis: repeat 100x with fuzzed inputs]
```

## Comparativo

| Test Type | Library | Speed | LLM Cost | Deterministic | When to Use |
|-----------|---------|-------|----------|---------------|-------------|
| Unit (mocked) | respx + pytest | <1s | $0 | Yes | Always; every commit |
| Integration (stubbed) | pytest-asyncio + httpx_mock | 1–10s | $0 | Yes | Pre-merge |
| Contract | pact-python | 5–30s | $0 | Yes | API version changes |
| Property-based | hypothesis | 10–60s | $0 | Seeds | Core logic refactors |
| Live E2E | pytest + real API | 30–120s | $$$ | No | Release gating only |
| Chaos | pytest-httpx exceptions | 1–10s | $0 | Yes | Resilience validation |

## Code Patterns

```python
# Async agent test with respx mock
import pytest, respx, httpx, json

@pytest.mark.asyncio
async def test_agent_calls_tool_on_ambiguous_query(mock_llm):
    with respx.mock:
        respx.post("https://api.anthropic.com/v1/messages").mock(
            return_value=httpx.Response(200, json=TOOL_CALL_FIXTURE)
        )
        result = await my_agent.run("What is the weather in Lisbon?")
    assert result.tool_used == "get_weather"
    assert result.tool_input["city"] == "Lisbon"

# Property-based test for agent state invariant
from hypothesis import given, settings
import hypothesis.strategies as st

@given(st.text(min_size=1, max_size=500))
@settings(max_examples=200)
def test_agent_always_returns_valid_schema(user_input):
    with respx.mock:
        respx.post(...).mock(return_value=httpx.Response(200, json=VALID_RESPONSE))
        result = agent.run_sync(user_input)
    assert isinstance(result.content, str)
    assert len(result.content) > 0
```

## References

- pytest-asyncio docs: https://pytest-asyncio.readthedocs.io/
- respx HTTP mocking: https://lundberg.github.io/respx/
- Hypothesis property testing: https://hypothesis.readthedocs.io/
- pact-python contract testing: https://docs.pact.io/implementation_guides/python
- Related: p01_kc_prompt_caching (cost control during test runs)
```