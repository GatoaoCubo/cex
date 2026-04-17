---
id: kc_prompt_engineering_taxonomy
kind: knowledge_card
title: "Prompt Engineering Taxonomy"
version: 1.0.0
quality: 9.0
pillar: P01
density_score: 1.0
updated: "2026-04-13"
---

# Prompt Engineering Taxonomy

This knowledge card explores core prompt engineering paradigms and their characteristics.

## Core Techniques

1. **Zero-shot**  
   - Definition: Directly asks for a task without examples  
   - Use Case: Simple, straightforward queries  
   - Advantages: Minimal input, fast execution

2. **Few-shot**  
   - Definition: Includes 1-3 example inputs/outputs  
   - Use Case: Complex tasks requiring pattern recognition  
   - Advantages: Balances specificity and flexibility

3. **Chain-of-thought (CoT)**  
   - Definition: Explicitly asks for reasoning steps  
   - Use Case: Mathematical problem solving, logical deduction  
   - Advantages: Improves accuracy for complex reasoning

4. **Tree-of-thought (ToT)**  
   - Definition: Explores multiple reasoning paths simultaneously  
   - Use Case: Open-ended creative tasks, multi-faceted problems  
   - Advantages: Captures diverse perspectives

5. **ReAct**  
   - Definition: Combines reasoning and action execution  
   - Use Case: Tasks requiring both analysis and implementation  
   - Advantages: Enables iterative problem solving

6. **Self-consistency**  
   - Definition: Uses multiple reasoning paths to verify answers  
   - Use Case: High-stakes decision making, critical analysis  
   - Advantages: Reduces error through cross-verification

## Comparison Table

| Technique         | Definition                     | Use Case                  | Advantages               |
|------------------|-------------------------------|---------------------------|--------------------------|
| Zero-shot        | Direct task instruction       | Simple queries            | Minimal input           |
| Few-shot         | 1-3 example inputs/outputs   | Complex pattern tasks    | Balanced flexibility    |
| Chain-of-thought | Explicit reasoning steps      | Mathematical problems    | Improved accuracy       |
| Tree-of-thought  | Multiple reasoning paths      | Creative tasks           | Diverse perspectives    |
| ReAct            | Reasoning + action execution | Complex problem solving  | Iterative approach      |
| Self-consistency | Cross-verified reasoning     | High-stakes decisions    | Error reduction         |
```

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**
