---
kind: output_template
id: bld_output_tokenizer_config
pillar: P05
llm_function: PRODUCE
purpose: Template for producing a tokenizer_config artifact
quality: null
title: "Tokenizer Config Builder - Output ISO"
version: "1.0.0"
author: n03_builder
tags: [tokenizer_config, builder, output]
tldr: "Output template for tokenizer config: frontmatter field guide, required body sections, filled example, and quality gate checklist for bpe, sentencepiece, or tiktoken tokenizer parameters and vocabulary configuration."
domain: "tokenizer configuration"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_tokenizer_config
---

# Output Template: tokenizer_config

```yaml
id: p09_tc_{{tokenizer_slug}}
kind: tokenizer_config
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
algorithm: "{{bpe_or_sentencepiece_or_wordpiece}}"
library: "{{tiktoken_or_sentencepiece_or_hf_tokenizers}}"
vocab_size: {{integer}}
max_length: {{integer}}
padding: "{{left_or_right}}"
truncation: {{boolean}}
domain: "{{domain_value}}"
quality: null
tags: [tokenizer, {{algorithm_tag}}, {{model_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```

## Algorithm
`{{algorithm_type_library_and_version}}`

## Vocabulary
`{{vocab_size_encoding_language_coverage}}`

## Special Tokens
`{{bos_eos_pad_unk_mappings}}`

## Limits
`{{max_length_truncation_padding}}`

## Compatibility
`{{supported_models_and_pipelines}}`

## Quality Gate Checklist

| Gate | Check | Pass Condition |
|------|-------|---------------|
| H01 | Frontmatter complete | All required fields present with valid types |
| H02 | ID matches filename | id field equals filename stem |
| H03 | Naming convention | Follows p09_tc_{{name}}.md + .yaml pattern |
| H04 | Body sections present | All required sections non-empty |
| H05 | Size within limits | Total <= 4096 bytes |
| H06 | No placeholder text | No {{var}} unreplaced |
| H07 | quality: null | Never self-scored |

## Properties

| Property | Value |
|----------|-------|
| Kind | `output` |
| Pillar | P05 |
| Domain | tokenizer config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
