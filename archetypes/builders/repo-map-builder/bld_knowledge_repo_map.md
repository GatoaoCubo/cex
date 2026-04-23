---
kind: knowledge_card
id: bld_knowledge_card_repo_map
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for repo_map production
quality: 9.2
title: "Knowledge Card Repo Map"
version: "1.1.0"
author: n05_ops
tags: [repo_map, builder, knowledge_card, tree-sitter, aider, pagerank, token-budget]
tldr: "Repo map: Aider's codebase context strategy -- tree-sitter symbol extraction, PageRank file ranking, token budget, file selection heuristics"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_instruction_repo_map
  - bld_output_template_repo_map
  - bld_tools_repo_map
  - bld_examples_repo_map
  - p01_qg_repo_map
  - atom_28_code_agents
  - n05_audit_hybrid_review2
  - bld_instruction_agent_package
  - p01_kc_anti_file_storage
  - p08_ac_explore
---

## Domain Overview
Repo_map is the codebase context strategy pioneered by Aider (github.com/paul-gauthier/aider).
The core problem: LLM context windows are finite; codebases are large. The solution: rank
ALL files by relevance and fit the top-ranked symbols into the token budget.

The Aider repo map uses tree-sitter to extract symbols (classes, functions, variables) from
every source file, then applies a graph-ranking algorithm (similar to PageRank) to determine
which files/symbols are most relevant to the current conversation. Only the highest-ranked
symbols are included, respecting the token budget.

Key insight: a repo map is NOT a file tree listing. It is a **ranked symbol table** where
importance is determined by graph centrality, not alphabetical order.

## Core Technical Concepts
| Concept | Definition | Implementation |
|---------|------------|----------------|
| tree-sitter | Incremental parser library producing concrete syntax trees | `tree_sitter.Language`, `tree_sitter_languages` pip package |
| Symbol extraction | Parsing source files to extract named code entities | tree-sitter queries: `(function_definition name: (identifier) @name)` |
| AST (Abstract Syntax Tree) | Tree representation of source code structure | tree-sitter produces CST; simplified to AST via queries |
| PageRank (graph ranking) | Iterative link-analysis to rank nodes by centrality | `networkx.pagerank(G, alpha=0.85)` on symbol reference graph |
| Token budget | Max tokens allocatable to repo map context | Controlled by `--map-tokens` in Aider (default: 1024) |
| File selection heuristics | Rules for prioritizing files to include | Mentioned files get 2x weight; recently changed get 1.5x boost |
| ctags | Universal ctags -- symbol extraction without full parse | Fallback when tree-sitter language unavailable |
| Reference graph | Directed graph: file A -> file B if A imports/calls B | Built from import statements + function call sites |
| Context window fit | Truncation strategy to stay within token budget | Rank by PageRank score, add files until token limit reached |
| Incremental update | Re-map only changed files, not full repo scan | Cache tree-sitter parse results; invalidate on file mtime change |

## tree-sitter Symbol Extraction
tree-sitter parses source files into typed syntax trees using language grammars.
Queries extract named symbols:

```python
# Python: extract all function/class definitions
query = lang.query("""
    (function_definition name: (identifier) @name) @def
    (class_definition name: (identifier) @name) @def
""")
matches = query.matches(tree.root_node)
```

Supported in Aider repo map: Python, JavaScript, TypeScript, Go, Rust, Java, C/C++, Ruby,
PHP, C#, Swift, Kotlin, Scala -- 40+ languages via tree-sitter-languages.

Fallback: Universal ctags (`ctags --output-format=json -R .`) for languages without tree-sitter grammar.

## Graph Ranking (PageRank)
Build a directed reference graph where nodes = files, edges = symbol references:

```python
import networkx as nx

G = nx.DiGraph()
for file, symbols in repo_symbols.items():
    for ref in symbols['references']:
        target = resolve_symbol(ref, repo_symbols)
        if target:
            G.add_edge(file, target['file'])

# Boost files mentioned in current conversation
personalization = {f: 2.0 for f in mentioned_files}
scores = nx.pagerank(G, alpha=0.85, personalization=personalization)
```

Files mentioned in the chat get personalization boost. High in-degree = many files reference
this file = high importance. The top-N files by score are included until token budget exhausted.

## Token Budget Management
| Parameter | Default | Purpose |
|-----------|---------|---------|
| --map-tokens | 1024 | Total token budget for repo map |
| --map-multiplier-no-files | 2 | Budget multiplier when no files in context |
| symbol truncation | 100 chars/symbol | Truncate long signatures to save tokens |
| file cap | 20 files max | Never include more than 20 files even if budget allows |

Token counting: `tiktoken` (OpenAI) or `anthropic.count_tokens()` for Claude models.

```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = len(enc.encode(repo_map_text))
```

## File Selection Heuristics
Aider's file selection priority order:
1. **Files explicitly mentioned** in current conversation (highest priority, 2x boost)
2. **Files in current diff/git status** (recently changed, 1.5x boost)
3. **High PageRank score** (frequently referenced by other files)
4. **Test files paired with source** (test_foo.py <-> foo.py linked)
5. **Entry points** (main.py, index.ts, app.go -- named by convention)
6. **Files with recent git commits** (active development areas)

Exclusion rules:
- Binary files (images, compiled artifacts)
- Lock files (package-lock.json, poetry.lock)
- Generated files (.pb.go, _generated.ts)
- Files larger than 100KB (too large for symbol extraction)
- Paths matching .gitignore

## Industry Standards and References
- Aider repo map: github.com/paul-gauthier/aider (aider/repomap.py)
- tree-sitter: github.com/tree-sitter/tree-sitter (C library + Python bindings)
- Universal ctags: github.com/universal-ctags/ctags
- NetworkX PageRank: networkx.org/documentation/stable/reference/algorithms/link_analysis.html
- tiktoken: github.com/openai/tiktoken (BPE tokenizer)
- SPDX: Software Bill of Materials standard for dependency tracking
- IEEE 12207: Software lifecycle processes

## Common Patterns
1. Parse all files with tree-sitter, cache results keyed on (path, mtime)
2. Build reference graph from import statements + call sites
3. Apply PageRank with personalization for mentioned files
4. Sort files by score, add to map until token budget reached
5. Output as structured text: `path/to/file.py:\n  class Foo:\n  def bar(self):`
6. Regenerate map on every conversation turn (fast with incremental update)

## Pitfalls
- Including too many files: exceeds token budget, dilutes context quality
- Missing reference graph: PageRank degenerates to file size ranking (inaccurate)
- No ctags fallback: fails on rare/new languages without tree-sitter grammar
- Ignoring personalization: mentioned files buried under high-PageRank files
- Static file tree listing (naive approach): wastes tokens on irrelevant files
- Not truncating long signatures: 1 file with verbose docstrings eats entire budget

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_repo_map]] | downstream | 0.62 |
| [[bld_output_template_repo_map]] | downstream | 0.54 |
| [[bld_tools_repo_map]] | downstream | 0.47 |
| [[bld_examples_repo_map]] | downstream | 0.44 |
| [[p01_qg_repo_map]] | downstream | 0.35 |
| [[atom_28_code_agents]] | sibling | 0.30 |
| [[n05_audit_hybrid_review2]] | downstream | 0.30 |
| [[bld_instruction_agent_package]] | downstream | 0.19 |
| [[p01_kc_anti_file_storage]] | sibling | 0.18 |
| [[p08_ac_explore]] | downstream | 0.18 |
