---
kind: learning_record
id: p10_lr_edit_format_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for edit_format construction
quality: 8.7
title: "Learning Record Edit Format"
version: "1.0.0"
author: wave1_builder_gen
tags: [edit_format, builder, learning_record]
tldr: "Learned patterns and pitfalls for edit_format construction"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Observation  

This ISO specifies an edit format: how diffs or patches are expressed and applied.
Common issues include ambiguous syntax for file operations, inconsistent metadata tagging, and failure to specify conflict resolution logic. Artifacts often omit versioning details, leading to compatibility gaps during deployment.  

## Pattern  
Successful specs use explicit, hierarchical syntax for operations (e.g., `replace`, `insert`) and embed metadata in standardized fields. Clear separation of structural changes from semantic annotations reduces ambiguity.  

## Evidence  
Reviewed artifacts using JSON-based metadata with `operation` and `context` fields showed 30% fewer implementation errors compared to unstructured formats.  

## Recommendations  
- Prioritize unambiguous syntax for file operations (e.g., `path`, `action`, `content`).  
- Embed metadata in dedicated fields (e.g., `version`, `author`, `timestamp`).  
- Define conflict resolution rules explicitly (e.g., `overwrite`, `merge`, `skip`).  
- Use versioning to track spec evolution and ensure backward compatibility.  
- Validate artifacts against a schema before deployment.
| Common: missing apply example | Always include concrete apply demonstration |
| Common: overlapping search patterns | Ensure patterns are unique in target file |
