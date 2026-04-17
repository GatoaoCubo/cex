---
id: p11_qg_toolkit
kind: quality_gate
pillar: P11
title: "Gate: Toolkit"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: builder
domain: toolkit
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - toolkit
  - permissions
  - p11
tldr: "Gates ensuring toolkits enforce least-privilege with correct confirmation tiers, deny lists override allow lists, tool count stays under 15, and no implementation code leaks into the permission bundle."
llm_function: GOVERN
---
## Definition
A toolkit is a permission bundle defining which tools an agent can access and under what constraints. It passes this gate when every write tool requires confirmation, deny lists are explicit with reasons, the tool count stays under 15, no tool implementation code is present, and the least-privilege principle is demonstrably applied.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches pattern `p04_tk_{name}` | Mismatched IDs cause routing failures |
| H03 | `kind` is exactly `toolkit` (literal match) | Kind drives the loader; wrong literal silently misroutes |
| H04 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H05 | `name` field is non-empty snake_case string | Invalid names break lookup and indexing |
| H06 | `tools` is a non-empty list with 1-15 entries | Empty toolkits are useless; >15 indicates domain split needed |
| H07 | Each tool has `name`, `description`, and `confirmation` fields | Missing fields break runtime tool resolution |
| H08 | `confirmation` values are one of: auto, confirm, deny | Unknown tiers cause undefined runtime behavior |
| H09 | No write/delete tool has `confirmation: auto` | Write operations without confirmation are security violations |
| H10 | Total YAML size <= 4096 bytes | Oversized toolkits exceed token budget |
| H11 | No tool implementation code (functions, classes, scripts) in the toolkit | Toolkits define permissions, not implementations |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every line carries information |
| 2 | Least-privilege compliance (only tools the agent demonstrably needs) | 1.5 | Kitchen sink — every tool included | Most tools justified | Every tool has clear usage justification |
| 3 | Confirmation tier accuracy (tiers match risk: reads=auto, writes=confirm, dangerous=deny) | 1.5 | All tools on auto | Most tiers correct | Every tier accurately reflects operation risk |
| 4 | Deny lists are explicit with reasons (not just names) | 1.0 | No deny lists | Deny lists without reasons | Every denial has an evidence-based reason |
| 5 | Tool descriptions are precise (one-line purpose, not usage instructions) | 1.0 | Descriptions are paragraphs | Most are concise | Every description is under 80 chars and actionable |
| 6 | No cross-toolkit tool duplication | 0.5 | Many duplicates across toolkits | One or two overlaps | Zero duplicates; each tool in exactly one toolkit |
| 7 | MCP endpoints mapped where applicable | 0.5 | No MCP mapping despite remote tools | Some tools mapped | All remote tools have valid MCP endpoints |
| 8 | Category matches toolkit domain (file_ops toolkit has file tools) | 0.5 | Category mismatches tool domain | Category broadly correct | Category precisely matches all tool domains |
