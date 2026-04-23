---
kind: architecture
id: bld_architecture_edit_format
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of edit_format -- inventory, dependencies
quality: 9.0
title: "Architecture Edit Format"
version: "1.1.0"
author: n04_hybrid_review2
tags: [edit_format, builder, architecture]
tldr: "Component map of edit_format -- inventory, dependencies"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - p03_sp_edit_format_builder
  - bld_examples_edit_format
  - bld_knowledge_card_edit_format
  - bld_collaboration_edit_format
  - bld_output_template_edit_format
  - edit-format-builder
  - bld_architecture_diff_strategy
  - hybrid_review2_n04
  - bld_schema_edit_format
  - bld_collaboration_response_format
---

## Component Inventory

This ISO specifies an edit format: how diffs or patches are expressed and applied.

| Name | Role | Owner | Status |
|------|------|-------|--------|
| Format Spec Registry | Catalog of valid format_type/edit_scope combinations | edit_format-builder | Active |
| Syntax Validator | Checks LLM output conforms to declared format_type (markers, structure) | host tooling | Active |
| SEARCH Matcher | Locates SEARCH block content in target file (exact or fuzzy) | diff_strategy-builder | Active |
| Whole-File Applier | Replaces file content verbatim from LLM output | host tooling | Active |
| Unified Diff Applier | Applies `--- a/` / `+++ b/` / `@@` patch via git-apply or patch(1) | host tooling | Active |
| JSON Patch Engine | Executes RFC 6902 operations on JSON/YAML config files | host tooling | Active |
| LSP TextEdit Engine | Applies range-based edits via Language Server Protocol | IDE / LSP client | Active |
| Format Router | Selects format_type based on file size, change scope, tool capability | code_executor | Active |

## Dependencies

| From | To | Type | Notes |
|------|----|------|-------|
| SEARCH Matcher | diff_strategy | required | Matching algorithm is diff_strategy's concern, not edit_format |
| Syntax Validator | Format Spec Registry | required | Validates against declared format_type rules |
| Format Router | Format Spec Registry | required | Reads compatible_tools to select format |
| Whole-File Applier | Format Spec Registry | data | Validates path + content structure |
| Unified Diff Applier | git / patch(1) | required | External tooling handles actual application |

## Architectural Position

`edit_format` is the wire format layer in the LLM code-agent edit pipeline:

```
[LLM reasoning / code generation]
      |
      | emits edit in declared format_type
      v
[edit_format spec]    <-- THIS BUILDER: defines valid syntax the LLM must use
      |
      | validated by Syntax Validator
      v
[diff_strategy]       <-- locates WHERE in the file to apply (SEARCH match, line anchoring)
      |
      v
[host applier]        <-- Whole-File Applier / Unified Diff Applier / JSON Patch Engine
      |
      v
[file system]
```

Adjacent builders:
- `diff_strategy_builder`: matching algorithms (exact, fuzzy, semantic) for locating SEARCH
- `formatter_builder`: output formatting, code style, indentation (separate from edit format)
- `code_executor_builder`: runs the edited code, validates correctness after application
- `parser_builder`: parses LLM response to extract edit blocks from prose context

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_edit_format_builder]] | upstream | 0.49 |
| [[bld_examples_edit_format]] | upstream | 0.44 |
| [[bld_knowledge_card_edit_format]] | upstream | 0.40 |
| [[bld_collaboration_edit_format]] | downstream | 0.39 |
| [[bld_output_template_edit_format]] | upstream | 0.36 |
| [[edit-format-builder]] | upstream | 0.36 |
| [[bld_architecture_diff_strategy]] | sibling | 0.35 |
| [[hybrid_review2_n04]] | upstream | 0.27 |
| [[bld_schema_edit_format]] | upstream | 0.27 |
| [[bld_collaboration_response_format]] | upstream | 0.26 |
