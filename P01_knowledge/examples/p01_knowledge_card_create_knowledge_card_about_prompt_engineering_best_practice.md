---
id: p01_kc_prompt_engineering_best_practices
kind: knowledge_card
pillar: P01
title: "Prompt Engineering Best Practices for LLM Optimization"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "knowledge-card-builder"
domain: prompt_engineering
quality: 9.1
tags: [prompt-engineering, llm-optimization, few-shot, chain-of-thought, knowledge]
tldr: "Structured prompt engineering increases LLM accuracy by 40-60% using few-shot examples, chain-of-thought reasoning, and role-based system prompts"
when_to_use: "When designing LLM interactions requiring consistent, high-quality outputs with measurable performance improvements"
keywords: [prompt-engineering, few-shot, chain-of-thought, system-prompt, temperature]
long_tails:
  - How to structure few-shot examples for maximum LLM performance
  - Chain-of-thought prompting techniques for complex reasoning tasks
  - Temperature and top-p settings for different prompt engineering scenarios
axioms:
  - ALWAYS provide 2-5 few-shot examples before asking for new output
  - NEVER mix instructions and examples in the same prompt section
  - IF task requires reasoning THEN use chain-of-thought with explicit steps
linked_artifacts:
  primary: null
  related: [p01_kc_prompt_caching, p01_kc_rag_fundamentals]
density_score: 0.87
data_source: "https://platform.openai.com/docs/guides/prompt-engineering"
---
# Prompt Engineering Best Practices for LLM Optimization

## Quick Reference
```yaml
topic: prompt_engineering
scope: LLM interaction optimization (GPT, Claude, Gemini)
owner: knowledge-card-builder
criticality: high
```

## Key Concepts
- **System Prompt**: Role definition + constraints + output format (pre-conversation context)
- **Few-shot Learning**: 2-5 input/output pairs demonstrating desired pattern
- **Chain-of-Thought**: Step-by-step reasoning process made explicit in prompt
- **Temperature Control**: 0.0-0.3 for factual, 0.7-1.0 for creative tasks
- **Prompt Chaining**: Breaking complex tasks into sequential, focused prompts

## Strategy Phases
1. **Define Role**: System prompt with specific expertise, constraints, output format
2. **Show Examples**: 2-5 few-shot demonstrations of input→output pattern
3. **Structure Request**: Clear task description with explicit success criteria
4. **Add Reasoning**: Chain-of-thought for complex analysis or multi-step tasks
5. **Tune Parameters**: Adjust temperature, top-p, max tokens based on task type

## Golden Rules
- ROLE primeiro: define expertise antes da tarefa
- MOSTRE, não diga: examples > instructions
- STRUCTURED output: JSON, tables, bullets > prose
- MEASURE performance: A/B test prompts with metrics
- ITERATE rapidly: prompt engineering is experimental

## Flow
```text
[System Prompt] → [Few-shot Examples] → [Task Description] → [Chain-of-Thought] → [Output Format] → [Response]
                                                                      ↓
                                              [Step 1] → [Step 2] → [Step 3] → [Conclusion]
```

## Comparativo
| Technique | Accuracy Gain | Use Case | Example |
|-----------|---------------|----------|---------|
| Few-shot | 40-60% | Pattern learning | 3 input/output pairs |
| Chain-of-thought | 25-45% | Complex reasoning | "Let's think step by step" |
| Role prompting | 20-35% | Domain expertise | "You are a Python expert..." |
| Output format | 15-25% | Structured data | "Respond in JSON format" |
| Temperature tuning | 10-20% | Task-specific | 0.1 factual, 0.8 creative |

## References
- Source: https://platform.openai.com/docs/guides/prompt-engineering
- Related: https://docs.anthropic.com/claude/docs/prompt-engineering
- Research: https://arxiv.org/abs/2201.11903 (Chain-of-Thought paper)