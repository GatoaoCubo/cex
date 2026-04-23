---
kind: instruction
id: bld_instruction_repo_map
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for repo_map
quality: 9.1
title: "Instruction Repo Map"
version: "1.1.0"
author: n05_ops
tags: [repo_map, builder, instruction, tree-sitter, pagerank, aider]
tldr: "Repo map production: tree-sitter symbol extraction -> PageRank file ranking -> token budget fit -> output symbol table"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_knowledge_card_repo_map
  - bld_output_template_repo_map
  - bld_examples_repo_map
  - p01_qg_repo_map
  - bld_instruction_agent_package
  - bld_tools_repo_map
  - p10_lr_agent_package_builder
  - bld_instruction_kind
  - p11_qg_kind_builder
  - atom_28_code_agents
---

## Phase 1: RESEARCH -- Discover and Extract

1. Identify repo root and scan all source files (use `git ls-files` or ripgrep).
2. Detect languages per file using pygments or file extension mapping.
3. For each source file: extract symbols using tree-sitter (classes, functions, methods, variables).
   - Use `tree_sitter_languages.get_language(lang)` + language-specific query.
   - Fallback to Universal ctags (`ctags --output-format=json`) for unsupported languages.
4. Build reference graph: directed edges from file A -> file B when A imports or calls B.
   - Parse import statements (Python `import`/`from`, JS `import`/`require`, Go `import`).
5. Identify "personalization" files: files explicitly mentioned in current conversation (+2x weight).
6. Identify "recency" files: files in `git diff HEAD` or recent commits (+1.5x weight).
7. Document: total file count, total symbol count, language distribution.

## Phase 2: RANK -- Apply PageRank and Select Files

1. Apply PageRank to reference graph with `networkx.pagerank(G, alpha=0.85, personalization=weights)`.
2. Sort all files by PageRank score (descending).
3. Set token budget: `--map-tokens` value (default 1024; multiply by 2 if no files in current context).
4. Count tokens for each file's symbol block using tiktoken or anthropic token counter.
5. Add files to map in rank order until token budget is exhausted.
6. If a file's symbols exceed 20% of remaining budget: truncate symbols by line length.
7. Apply file exclusion rules: binaries, generated files, lock files, files > 100KB, .gitignore patterns.
8. Record selection heuristics applied (mentioned, recent, entry-point, test-paired).

## Phase 3: COMPOSE -- Build the Artifact

1. Write YAML frontmatter: id (pattern `p01_rm_{{name}}`), kind, pillar, token_budget,
   symbol_count, file_count, extraction_method.
2. Write Repository Overview section: repo name, root, languages, total files/symbols, tokens used/budget.
3. Write File Ranking table: rank, file path, PageRank score, token count, reason for inclusion.
4. Write Symbol Table section in Aider format:
   ```
   path/to/file.py:
     class ClassName:
       def method_name(self, param: type) -> return_type
     def function_name(param: type) -> return_type
   ```
5. Write Reference Graph Summary: top files by in-degree + out-degree.
6. Write File Selection Heuristics Applied table.
7. Write Excluded Files table with reasons.
8. Validate against OUTPUT_TEMPLATE.md: all sections present.

## Phase 4: VALIDATE

- [ ] id matches pattern `^p01_rm_[a-zA-Z0-9_]+$`
- [ ] token_budget field present and equals configured budget
- [ ] tokens_used <= token_budget (HARD constraint)
- [ ] Symbol table contains function signatures (not just file paths)
- [ ] PageRank scores shown in file ranking table
- [ ] File exclusion rules applied (no binaries, no lock files)
- [ ] H01-H10 HARD gates pass
- [ ] SOFT score >= 8.0 before publish


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_repo_map]] | upstream | 0.50 |
| [[bld_output_template_repo_map]] | downstream | 0.47 |
| [[bld_examples_repo_map]] | downstream | 0.34 |
| [[p01_qg_repo_map]] | downstream | 0.33 |
| [[bld_instruction_agent_package]] | sibling | 0.31 |
| [[bld_tools_repo_map]] | downstream | 0.27 |
| [[p10_lr_agent_package_builder]] | downstream | 0.25 |
| [[bld_instruction_kind]] | sibling | 0.25 |
| [[p11_qg_kind_builder]] | downstream | 0.24 |
| [[atom_28_code_agents]] | upstream | 0.22 |
