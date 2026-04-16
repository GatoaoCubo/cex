---
id: kc_reasoning_strategy
kind: knowledge_card
title: Reasoning Strategy
version: 1.0.0
quality: 8.7
pillar: P01
density_score: 0.94
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