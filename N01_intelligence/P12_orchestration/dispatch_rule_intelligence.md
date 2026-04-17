---
id: n01_dr_intelligence
kind: dispatch_rule
pillar: P12
title: "Dispatch Rule: N01 Research & Intelligence"
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "N01_rebuild_8F"
quality: 9.1
tags: [dispatch, routing, orchestration, n01, research]
tldr: "Routes complex research, analysis, and synthesis tasks to the N01 Research & Intelligence Nucleus based on semantic intent, keywords, and trigger phrases."
target_agent: "n01_agent_intelligence"
priority: 10 # Highest priority for specialist tasks
confidence_threshold: 0.85 # Requires a strong semantic match
fallback_agent: "n04_knowledge"
density_score: 0.95
---

## 1. PURPOSE
This rule identifies and routes tasks that require deep, analytical research and synthesis to the **N01 Research & Intelligence Nucleus**. The goal is to ensure that complex, long-running analytical jobs are handled by the appropriate specialist agent (Gemini 2.5-pro, 1M context) instead of a generalist agent.

## 2. ROUTING STRATEGY: HIERARCHICAL
Routing is determined by a hierarchical evaluation:
1.  **Trigger Phrase Match**: Highest weight. Direct match to common N01 tasks.
2.  **Semantic Intent Analysis**: The core of the strategy. The system evaluates if the user's underlying goal is research and synthesis.
3.  **Keyword Match**: Lowest weight. Used as a supporting signal.

## 3. TRIGGER PHRASES (HIGH CONFIDENCE)
If the prompt starts with or contains these phrases, route to N01 with high confidence:
- "Research the state of..."
- "Analyze the competitive landscape of..."
- "Provide a literature review on..."
- "Summarize the key findings from these papers..."
- "Benchmark X against Y on..."
- "Create a trend report for..."
- "Conduct a competitor analysis of..."

## 4. CORE KEYWORDS (MEDIUM CONFIDENCE)
Presence of these keywords strongly suggests N01 is the correct agent:
- `research`
- `analysis`
- `competitor`
- `intelligence`
- `papers`
- `trends`
- `summarize` (in the context of long documents)
- `benchmark`
- `RAG`
- `literature review`
- `market analysis`
- `synthesis`
- `findings`

## 5. EXCLUSION CRITERIA (ANTI-PATTERNS)
Even if keywords match, **DO NOT** route to N01:

| Query Type | Example | Route Instead |
|------------|---------|---------------|
| Simple factual questions | "What is React?" | N04 Knowledge |
| Code writing requests | "Write a Python script for data parsing" | N05 Operations |
| Creative content | "Write a poem about AI" | N02 Marketing |
| Operational actions | "Restart the server", "Deploy to prod" | N05 Operations |
| Real-time info | "What's the weather?", "Latest stock price" | External API |
| Quick definitions | "Define machine learning" | N04 Knowledge |
| Build requests | "Create a new component", "Generate docs" | N03 Builder |
| Single-source summary | "Summarize this one article" | N04 Knowledge |
| Implementation tasks | "How do I configure X?" | N05 Operations |

## 6. FALLBACK LOGIC
If the routing confidence score is below the `confidence_threshold` (0.85), or if the N01 agent is offline or at capacity, the task MUST be routed to the `n04_knowledge` nucleus. N04 serves as the general-purpose knowledge agent and can handle broader, less specialized queries, ensuring system resilience.