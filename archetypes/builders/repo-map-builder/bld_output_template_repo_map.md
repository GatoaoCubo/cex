---
kind: output_template
id: bld_output_template_repo_map
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for repo_map production
quality: 9.1
title: "Output Template Repo Map"
version: "1.1.0"
author: n05_ops
tags: [repo_map, builder, output_template, tree-sitter, pagerank, token-budget]
tldr: "Repo map template: symbol table (tree-sitter), PageRank scores, token budget, file selection heuristics"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

```yaml
---
id: p01_rm_{{name}}
kind: repo_map
pillar: P01
title: "{{repo_name}} -- Repository Context Map"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [repo_map, {{language_tags}}]
tldr: "{{one_line_description}}"
token_budget: {{token_budget}}      # max tokens for this map (default: 1024)
symbol_count: {{symbol_count}}      # total symbols extracted
file_count: {{file_count}}          # files included in map
extraction_method: "{{method}}"     # tree-sitter | ctags | hybrid
---
```

## Repository Overview

**Repo:** `{{repo_name}}`
**Root:** `{{repo_root}}`
**Languages:** `{{language_list}}`
**Total files scanned:** `{{total_files}}`
**Total symbols extracted:** `{{total_symbols}}`
**Token budget:** `{{token_budget}}` tokens
**Tokens used:** `{{tokens_used}}` / `{{token_budget}}`

## File Ranking (PageRank)

| Rank | File | PageRank Score | Tokens | Reason |
|------|------|---------------|--------|--------|
| 1 | `{{file_1}}` | {{score_1}} | {{tok_1}} | `{{reason_1}}` |
| 2 | `{{file_2}}` | {{score_2}} | {{tok_2}} | `{{reason_2}}` |
| 3 | `{{file_3}}` | {{score_3}} | {{tok_3}} | `{{reason_3}}` |
| ... | ... | ... | ... | ... |

**Personalization boosts applied:** `{{mentioned_files_list}}` (2x weight)
**Recency boosts applied:** `{{recent_files_list}}` (1.5x weight)

## Symbol Table (tree-sitter extracted)

```
{{file_1_path}}:
  {{symbol_type}} {{symbol_name_1}}({{params_1}})
  {{symbol_type}} {{symbol_name_2}}({{params_2}})

{{file_2_path}}:
  class {{class_name_1}}:
    {{method_name_1}}({{params}})
    {{method_name_2}}({{params}})

{{file_3_path}}:
  {{symbol_type}} {{symbol_name_3}} = {{value_preview}}
```

*Symbol types: def | class | var | const | interface | type | enum*

## Reference Graph Summary

| File | In-degree | Out-degree | Top References |
|------|-----------|------------|---------------|
| `{{file_1}}` | {{in_1}} | {{out_1}} | `{{refs_1}}` |
| `{{file_2}}` | {{in_2}} | {{out_2}} | `{{refs_2}}` |

**Graph stats:** `{{node_count}}` nodes, {{edge_count}} edges, density `{{density}}`

## File Selection Heuristics Applied

| Rule | Files Affected | Effect |
|------|---------------|--------|
| Mentioned in chat | `{{mentioned_count}}` files | +2.0x weight |
| Recent git changes | `{{recent_count}}` files | +1.5x weight |
| Entry points detected | `{{entry_count}}` files | +1.2x weight |
| Test-source pairs | `{{test_count}}` pairs | Linked |
| Binary/generated excluded | `{{excluded_count}}` files | Excluded |

## Extraction Method

| Component | Tool | Version | Notes |
|-----------|------|---------|-------|
| Parser | `{{parser_tool}}` | `{{parser_version}}` | tree-sitter or ctags |
| Languages parsed | `{{lang_list}}` | - | tree-sitter grammar coverage |
| Fallback | ctags | universal-ctags | For unsupported languages |
| Token counter | `{{tokenizer}}` | - | tiktoken cl100k or claude tokenizer |
| Graph library | networkx | 3.x | PageRank alpha=0.85 |

## Excluded Files

| Pattern | Count | Reason |
|---------|-------|--------|
| .gitignore patterns | `{{gitignore_count}}` | User-excluded |
| Binary files | `{{binary_count}}` | Not parseable |
| Generated files (*.pb.go, *_generated.*) | `{{gen_count}}` | Noise |
| Files > 100KB | `{{large_count}}` | Too large for symbol extraction |
| Lock files | `{{lock_count}}` | No symbols |
