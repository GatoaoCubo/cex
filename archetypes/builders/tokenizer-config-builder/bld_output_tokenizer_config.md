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
tldr: "Output template for tokenizer config artifacts."
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
