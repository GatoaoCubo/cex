---
kind: knowledge_card
id: bld_knowledge_card_edit_format
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for edit_format production
quality: null
title: "Knowledge Card Edit Format"
version: "1.0.0"
author: wave1_builder_gen
tags: [edit_format, builder, knowledge_card]
tldr: "Domain knowledge for edit_format production"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Domain Overview  
Edit_format specifies how LLMs communicate changes to host systems, ensuring precise, actionable modifications to files. It bridges language models' abstract reasoning with concrete code/Configuration edits, requiring unambiguous syntax and semantics. Key use cases include code generation, configuration management, and CI/CD pipeline scripting. Unlike diff_strategy (e.g., Myers diff), edit_format focuses on *how* changes are structured, not *how* they are computed.  

The specification must align with host system capabilities (e.g., file parsers, version control), ensuring compatibility across languages, frameworks, and tools. It often integrates with standards like JSON Patch (RFC 6943) or Git's diff format, but tailors them for LLM output. Proper edit_format minimizes ambiguity, reduces merge conflicts, and enables tooling to apply changes reliably.  

## Key Concepts  
| Concept           | Definition                                                                 | Source                |  
|-------------------|----------------------------------------------------------------------------|-----------------------|  
| Edit Operation    | Atomic change to a file (e.g., insert, delete, replace)                    | RFC 6943              |  
| File Path         | Absolute or relative path to the target file                              | POSIX                 |  
| Line Number       | 1-based index for locating edits within a file                            | Language Server Protocol |  
| Context Window    | Surrounding lines included to disambiguate edits                          | GitHub API v3         |  
| Operation Type    | Enumerated action (e.g., `add`, `remove`, `modify`)                       | JSON Patch            |  
| Encoding Scheme   | Character set (e.g., UTF-8) and line endings (CRLF/LF)                    | IETF RFC 2049         |  
| Conflict Marker   | Token to resolve overlapping edits (e.g., `<<<<<`, `>>>>>`)              | Git                   |  
| Version Stamp     | Metadata indicating file version (e.g., Git SHA, timestamp)              | Semantic Versioning   |  

## Industry Standards  
- JSON Patch (RFC 6943)  
- Git diff format (Git v2.9+)  
- Language Server Protocol (LSP)  
- ASTM E2500-21 (Software Engineering Standards)  
- POSIX file path conventions  
- IETF RFC 2049 (MIME standards for encoding)  

## Common Patterns  
1. Use JSON for structured, hierarchical edits.  
2. Include pre/post context to disambiguate ambiguous edits.  
3. Prioritize atomic operations over bulk replacements.  
4. Embed version stamps for reconciliation with host systems.  
5. Use conflict markers for merge scenarios.  

## Pitfalls  
- Omitting context windows leads to misapplied edits.  
- Assuming line numbers are stable across file versions.  
- Ignoring host-specific encoding schemes (e.g., CRLF vs. LF).  
- Overloading operation types with vague verbs (e.g., "update").  
- Failing to align with LSP or Git conventions, causing tooling friction.
