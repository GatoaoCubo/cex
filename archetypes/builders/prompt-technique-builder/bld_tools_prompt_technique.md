---
kind: tools
id: bld_tools_prompt_technique
pillar: P04
llm_function: CALL
purpose: Tools available for prompt_technique production
quality: 8.9
title: "Tools Prompt Technique"
version: "1.1.0"
author: n01_hybrid_review4
tags: [prompt_technique, builder, tools]
tldr: "Real CEX tools for producing prompt_technique artifacts."
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml | After saving |
| cex_score.py | Apply peer-review quality score | Post-production |
| cex_retriever.py | Find similar prompt_technique artifacts for reference | Before composing |
| cex_doctor.py | Validate artifact health (frontmatter, kind, pillar) | During validation |
| cex_prompt_optimizer.py | Analyze prompt patterns for improvement opportunities | Post-production |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_wave_validator.py | Structural checks: domain keywords, required fields | Pre-commit |
| cex_hygiene.py | Artifact CRUD hygiene: naming, orphan detection | Post-production |

## External References
- Wei et al. (2022): Chain-of-Thought Prompting Elicits Reasoning in LLMs. NeurIPS 2022.
- Yao et al. (2022): ReAct: Synergizing Reasoning and Acting in Language Models.
- Yao et al. (2023): Tree of Thoughts: Deliberate Problem Solving with Large Language Models.
- Wang et al. (2022): Self-Consistency Improves Chain of Thought Reasoning in LLMs.
- Dhuliawala et al. (2023): Chain-of-Verification Reduces Hallucination in LLMs.
