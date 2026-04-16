---
kind: collaboration
id: bld_collaboration_prompt_technique
pillar: P12
llm_function: COLLABORATE
purpose: How prompt_technique-builder works in crews with other builders
quality: 8.9
title: "Collaboration Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, collaboration]
tldr: "How prompt_technique-builder works in crews with other builders"
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Designs and refines specific prompting strategies to enhance model performance, ensuring techniques are adaptable and effective across use cases.  

## Receives From  
| Builder          | What                  | Format      |  
|------------------|-----------------------|-------------|  
| prompt_template-builder | Base templates        | JSON        |  
| reasoning_strategy-builder | Reasoning frameworks | YAML        |  
| feedback-builder | User/evaluator feedback | Text file   |  

## Produces For  
| Builder          | What                  | Format      |  
|------------------|-----------------------|-------------|  
| response_generator-builder | Optimized prompt techniques | JSON        |  
| evaluation-builder | Technique benchmarks  | Markdown    |  
| documentation-builder | Technique descriptions | API endpoint |  

## Boundary  
Does NOT implement templates (handled by prompt_template-builder) or reasoning logic (handled by reasoning_strategy-builder). Execution of techniques is managed by response_generator-builder.
