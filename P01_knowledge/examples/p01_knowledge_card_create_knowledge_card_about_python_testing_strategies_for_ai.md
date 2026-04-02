---
id: p01_kc_python_testing_ai_agents
kind: knowledge_card
pillar: P01
title: "Python Testing Strategies for AI Agents"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder"
domain: ai_testing
quality: 0.0
tags: [python-testing, ai-agents, llm-testing, async-testing, mocking, integration-testing, knowledge]
tldr: "Test AI agents with pytest-asyncio for async flows, mock LLM APIs with respx/httpx-mock, use contract testing for external AI services, and implement chaos testing for resilience validation"
when_to_use: "When building Python-based AI agents that interact with LLM APIs, need async testing, or require validation of agent behaviors and decision-making flows"
keywords: [pytest-asyncio, llm-mocking, contract-testing, chaos-testing, agent-testing]
long_tails:
  - How to mock OpenAI API calls in pytest for deterministic agent tests
  - Testing async agent workflows with pytest-asyncio and proper event loop handling
  - Contract testing strategies for AI agent integration with external LLM services
axioms:
  - ALWAYS mock external LLM API calls in unit tests to ensure deterministic behavior
  - NEVER test real LLM APIs in CI/CD pipelines due to cost and rate limits
  - IF testing agent decision flows THEN use property-based testing with hypothesis for edge cases
linked_artifacts:
  primary: null
  related: [p01_kc_async_python_patterns, p01_kc_api_testing_strategies]
density_score: 0.89
data_source: "https://pytest-asyncio.readthedocs.io/en/latest/"
---

# Python Testing Strategies for AI Agents

## Quick Reference
```yaml
topic: python_ai_agent_testing
scope: pytest, async testing, LLM API mocking, agent behavior validation
owner: testing_engineer
criticality: high
```

## Key Concepts
| Concept | Purpose | Implementation | Key Library |
|---------|---------|----------------|-------------|
| pytest-asyncio | Test async agent workflows | `@pytest.mark.asyncio` decorator | pytest-asyncio |
| LLM API Mocking | Deterministic LLM responses | Mock OpenAI/Anthropic with fixed responses | respx, responses |
| Agent State Testing | Validate memory/conversation state | Property-based tests for decision history | hypothesis |
| Contract Testing | Verify AI service interfaces | Schema validation for API contracts | pact-python |
| Chaos Testing | Test resilience under failures | Inject timeouts, rate limits, errors | custom fixtures |

## Strategy Phases
1. **Unit Layer**: Mock all external APIs; test individual agent components with pytest fixtures
2. **Integration Layer**: Test agent-to-service interactions with contract tests and stubbed responses  
3. **End-to-End Layer**: Run full agent workflows against test LLM endpoints with known prompts/outputs
4. **Chaos Layer**: Inject failures using chaos-engineering to validate retry/fallback mechanisms
5. **Performance Layer**: Load test agent throughput with concurrent requests and measure response times

## Golden Rules
- MOCK all LLM API calls in unit tests - use respx for httpx or responses for requests
- ISOLATE agent state between tests - reset conversation memory and persistent storage
- VALIDATE both successful paths and error handling - test API timeouts, rate limits, malformed responses
- MEASURE agent performance - track token usage, response latency, and decision accuracy
- VERSION test data - use fixed prompt/response pairs for regression testing

## Flow
```text
[Test Setup] -> [Mock LLM APIs] -> [Initialize Agent] -> [Execute Workflow] 
      |                                                        |
[Teardown] <- [Assert Outcomes] <- [Validate State] <- [Check Calls]
```

## Comparativo
| Testing Approach | Use Case | Tools | Pros | Cons |
|------------------|----------|-------|------|------|
| Unit + Mocks | Fast feedback | pytest + respx | Deterministic, fast | No real API validation |
| Contract Testing | API changes | pact-python | Catches breaking changes | Setup complexity |
| E2E with Test APIs | Full workflows | pytest + test endpoints | Real behavior | Slow, costly |
| Property-Based | Edge cases | hypothesis | Finds unexpected bugs | Hard to debug failures |

## References
- pytest-asyncio docs: https://pytest-asyncio.readthedocs.io/en/latest/
- respx mocking: https://lundberg.github.io/respx/
- pact-python: https://github.com/pact-foundation/pact-python
- hypothesis property testing: https://hypothesis.readthedocs.io/