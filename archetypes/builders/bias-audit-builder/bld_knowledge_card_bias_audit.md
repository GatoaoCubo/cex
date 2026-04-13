---
kind: knowledge_card
id: bld_knowledge_card_bias_audit
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for bias_audit production
quality: null
title: "Knowledge Card Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, knowledge_card]
tldr: "Domain knowledge for bias_audit production"
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Domain Overview  
Bias audit artifacts evaluate algorithmic fairness by analyzing model outputs across protected attributes (e.g., race, gender) to detect systemic inequities. Industries like finance, healthcare, and HR increasingly mandate such audits to comply with regulations (e.g., EU AI Act, FDA guidelines) and mitigate reputational risks. Techniques focus on disparity metrics, counterfactual analysis, and fairness-aware ML, emphasizing transparency and accountability in AI systems.  

## Key Concepts  
| Concept               | Definition                                                                 | Source                          |  
|----------------------|----------------------------------------------------------------------------|---------------------------------|  
| Disparate Impact     | Statistical disparity in outcomes between groups (e.g., 80% rule)         | AI Act (EU)                    |  
| Demographic Parity   | Equal prediction rates across protected groups                            | Hardt et al. (2016)            |  
| Equal Opportunity    | Equal true positive rates across groups                                   | Hardt et al. (2016)            |  
| Proxy Variables      | Correlated attributes used to infer protected classes (e.g., zip codes)   | FAT\* Conference (2019)        |  
| Fairness-aware ML    | Algorithms incorporating fairness constraints during training             | Zafar et al. (2017)            |  
| Counterfactual Fairness | Outcomes remain invariant under hypothetical interventions              | Kusner et al. (2017)           |  
| Audit Trail        | Documented process of data collection, model training, and evaluation     | IEEE Ethically Aligned Design  |  
| Intersectional Bias  | Disparities arising from overlapping protected attributes (e.g., race + gender) | Algorithmic Justice League     |  

## Industry Standards  
- EU AI Act (2024): Mandates fairness evaluations for high-risk systems  
- FAT\* Conference guidelines on algorithmic fairness  
- IEEE Ethically Aligned Design (2022)  
- OECD AI Principles (2021)  
- NIST AI Risk Management Framework (2023)  

## Common Patterns  
1. Use demographic parity for binary classification audits  
2. Detect proxy variables via correlation analysis  
3. Apply fairness-aware ML during model training  
4. Validate counterfactual fairness through synthetic data  
5. Leverage audit trails for regulatory compliance  

## Pitfalls  
- Relying on single fairness metrics without contextual analysis  
- Ignoring intersectional bias in multi-attribute evaluations  
- Using biased training data without preprocessing  
- Overlooking deployment context (e.g., historical inequities)  
- Overfitting fairness constraints to reduce model utility
