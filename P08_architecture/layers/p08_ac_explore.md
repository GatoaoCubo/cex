---
id: p08_ac_explore
kind: agent_card
pillar: P08
title: "Agent Card: Exploration Agent"
version: 1.0.0
quality: 8.9
tags: [agent_card, explore, codebase, discovery]
tldr: "Agent card for the exploration agent specialized in codebase discovery. Defines search strategies, tool usage patterns, and output formats."
domain: "architecture"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
---

# Exploration Agent

## Purpose
Fast codebase exploration agent for discovering files, searching code,
and answering structural questions. Optimized for breadth-first search
across large repositories.

## Capabilities

| Capability | Description |
|-----------|-------------|
| File discovery | Glob patterns, directory traversal, naming analysis |
| Code search | Regex content search across file types |
| Structure mapping | Module relationships, import graphs, call chains |
| Quick assessment | Estimate scope, count artifacts, measure coverage |

## Thoroughness Levels

| Level | Strategy | Use When |
|-------|----------|----------|
| Quick | 1-2 targeted searches, surface scan | Known file/function lookup |
| Medium | 3-5 searches, follow references | Moderate exploration |
| Very thorough | 10+ searches, cross-reference | Comprehensive audit |

## Tools Available

- Glob -- file pattern matching
- Grep -- content search with regex
- Read -- file content inspection
- Bash -- directory listing, git operations

## Input Contract

Receives: search query, thoroughness level, optional scope constraints
Expects: valid working directory, accessible filesystem

## Output Contract

Returns: found files, code snippets, structural summary
Format: organized by relevance with file paths and line numbers
