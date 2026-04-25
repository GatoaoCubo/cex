---
id: kc_reasoning_strategy
kind: knowledge_card
8f: F3_inject
title: Reasoning Strategy
version: 1.0.0
quality: 8.7
pillar: P01
tldr: "Structured prompting framework using CoT, ToT, and role assignment to guide LLM problem-solving"
when_to_use: "When designing multi-step reasoning flows that require systematic analysis and validation"
density_score: 0.94
related:
  - reasoning-strategy-builder
  - bld_instruction_reasoning_strategy
  - p03_sp_reasoning_strategy_builder
  - p01_kc_chain_of_thought
  - p01_kc_prompt_engineering_best_practices
  - bld_knowledge_card_reasoning_strategy
  - p03_qg_reasoning_strategy
  - p10_lr_chain_builder
  - kc_prompt_engineering_taxonomy
  - bld_output_template_reasoning_strategy
---

# Reasoning Strategy

## Overview
A structured prompting technique to guide LLMs through complex problem-solving by breaking tasks into logical steps, ensuring systematic analysis and coherent outputs.

## Key Components
1. **Structured Prompts**  
   Use explicit frameworks like "Chain-of-Thought" (CoT) or "Tree of Thoughts" to outline reasoning phases.

2. **Step-by-Step Breakdown**  
   Decompose tasks into:  
   - Problem definition  
   - Assumptions analysis  
   - Evidence gathering  
   - Logical inference  
   - Conclusion validation  

3. **Role Assignment**  
   Assign distinct roles to LLMs (e.g., "Analyst", "Evaluator") to simulate collaborative reasoning.

4. **Example Templates**  
   ```markdown
   [Role]: [Task]  
   1. [Step 1]  
   2. [Step 2]  
   ...  
   Final Answer: [Result]
   ```

5. **Integration with Phases**  
   Align reasoning steps with phase lifecycle:  
   - `discover`: Define problem scope  
   - `configure`: Set reasoning parameters  
   - `execute`: Perform step-by-step analysis  
   - `validate`: Cross-check logical consistency  
   - `archive`: Store structured reasoning output  

6. **Best Practices**  
   - Use concrete examples for complex concepts  
   - Include constraints to guide output format  
   - Iterate with feedback loops for refinement  
   - Combine with visualization tools for abstract reasoning
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[reasoning-strategy-builder]] | downstream | 0.41 |
| [[bld_instruction_reasoning_strategy]] | downstream | 0.39 |
| [[p03_sp_reasoning_strategy_builder]] | downstream | 0.38 |
| [[p01_kc_chain_of_thought]] | sibling | 0.37 |
| [[p01_kc_prompt_engineering_best_practices]] | sibling | 0.35 |
| [[bld_knowledge_card_reasoning_strategy]] | sibling | 0.33 |
| [[p03_qg_reasoning_strategy]] | downstream | 0.32 |
| [[p10_lr_chain_builder]] | downstream | 0.31 |
| [[kc_prompt_engineering_taxonomy]] | sibling | 0.30 |
| [[bld_output_template_reasoning_strategy]] | downstream | 0.30 |
