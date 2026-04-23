---
kind: tools
id: bld_tools_repo_map
pillar: P04
llm_function: CALL
purpose: Tools available for repo_map production
quality: 9.1
title: "Tools Repo Map"
version: "1.1.0"
author: n05_ops
tags: [repo_map, builder, tools, tree-sitter, ctags, networkx, tiktoken]
tldr: "Real repo map tools: tree-sitter (symbol extraction), NetworkX (PageRank), tiktoken (token budget), ctags (fallback)"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_knowledge_card_repo_map
  - bld_instruction_repo_map
  - bld_output_template_repo_map
  - n05_audit_hybrid_review2
  - atom_28_code_agents
  - bld_examples_repo_map
  - bld_tools_diff_strategy
  - p01_qg_repo_map
  - n06_hybrid_review2_final
  - bld_tools_api_reference
---

## Symbol Extraction Tools
| Tool | Purpose | Command / API |
|------|---------|---------------|
| tree-sitter (Python) | Incremental CST parser; extract functions/classes | `pip install tree-sitter tree-sitter-languages` |
| tree-sitter-languages | Pre-built grammars for 40+ languages | `from tree_sitter_languages import get_language` |
| Universal ctags | Fallback symbol extractor for rare languages | `ctags --output-format=json -R .` |
| pygments (Lexer) | Tokenize source for language detection | `pygments.lexers.guess_lexer_for_filename()` |

## Graph Ranking Tools
| Tool | Purpose | API |
|------|---------|-----|
| NetworkX | Graph construction + PageRank | `nx.DiGraph()`, `nx.pagerank(G, alpha=0.85)` |
| scipy (sparse) | Sparse matrix PageRank (large repos) | `scipy.sparse.linalg.eigs` |
| igraph | Fast alternative to NetworkX for large graphs | `igraph.Graph.PageRank()` |

## Token Budget Tools
| Tool | Purpose | API |
|------|---------|-----|
| tiktoken | BPE tokenizer for OpenAI models | `tiktoken.get_encoding("cl100k_base")` |
| anthropic SDK | Token counting for Claude models | `client.beta.messages.count_tokens()` |
| tokenizers (HuggingFace) | Fast Rust tokenizers | `AutoTokenizer.from_pretrained(model)` |

## File Discovery and Filtering
| Tool | Purpose | Command |
|------|---------|---------|
| ripgrep (rg) | Fast file search; apply .gitignore | `rg --files --glob "*.py"` |
| pathspec (Python) | Parse and apply .gitignore rules | `pathspec.PathSpec.from_lines("gitwildmatch", patterns)` |
| git ls-files | List tracked files respecting .gitignore | `git ls-files --cached --others --exclude-standard` |
| watchdog (Python) | File system events for incremental update | `watchdog.observers.Observer()` |

## Reference / Import Analysis
| Tool | Purpose | Language |
|------|---------|---------|
| ast (stdlib) | Python AST import extraction | `ast.parse()`, walk for `Import`/`ImportFrom` |
| acorn / esprima | JavaScript/TypeScript import analysis | `acorn.parse()` |
| go/parser (stdlib) | Go import extraction | `go/parser.ParseFile()` |
| javap / jdeprscan | Java class dependency analysis | `javap -p -c *.class` |

## CEX Infrastructure Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | YAML compilation | Post-production |
| cex_score.py | Quality scoring | After artifact generation |
| cex_doctor.py | System health check | Pre-dispatch |
| cex_retriever.py | Similarity search | Find similar maps |

## Reference Implementation
| Source | What to Study |
|--------|--------------|
| aider/repomap.py | Full Aider repo map implementation (PageRank + tree-sitter) |
| aider/linter.py | Tree-sitter language dispatch and query patterns |
| github.com/paul-gauthier/aider | Reference implementation for repo_map concept |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_repo_map]] | upstream | 0.55 |
| [[bld_instruction_repo_map]] | upstream | 0.40 |
| [[bld_output_template_repo_map]] | downstream | 0.37 |
| [[n05_audit_hybrid_review2]] | downstream | 0.30 |
| [[atom_28_code_agents]] | upstream | 0.28 |
| [[bld_examples_repo_map]] | downstream | 0.28 |
| [[bld_tools_diff_strategy]] | sibling | 0.25 |
| [[p01_qg_repo_map]] | downstream | 0.19 |
| [[n06_hybrid_review2_final]] | downstream | 0.17 |
| [[bld_tools_api_reference]] | sibling | 0.17 |
