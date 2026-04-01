---
id: "p01_fse_{{TOPIC_SLUG}}"
kind: few_shot_example
pillar: P01
version: 1.0.0
title: Template - Few Shot Example
tags: [template, few-shot, example, prompt, icl]
tldr: Input-output pair for in-context learning. Shows LLM what good output looks like.
quality: 8.6
---

# Few Shot Example: [NAME]

## Purpose
[WHAT this few_shot_example does]
## Schema
```yaml
target_kind: [WHAT_KIND_THIS_EXEMPLIFIES]
input: "[SAMPLE_INPUT]"
output: "[EXPECTED_OUTPUT]"
```
## Example Pair
### Input
```
[NATURAL_LANGUAGE_REQUEST]
```
### Expected Output
```
[COMPLETE_ARTIFACT — full valid output with frontmatter]
```
## Selection Criteria
| Criterion | Requirement |
|-----------|-------------|
| Relevance | Same kind as target |
| Quality | Score >= 8.5 |
| Diversity | Cover different use cases |
| Size | <= 2000 tokens (context budget) |
## Usage in 8F
Injected during F3 (INJECT). 2-3 examples per kind is optimal.
## Quality Gate
- [ ] Input is natural language
- [ ] Output is a complete valid artifact
- [ ] Output passes F7 gates
- [ ] Example is representative of common use
