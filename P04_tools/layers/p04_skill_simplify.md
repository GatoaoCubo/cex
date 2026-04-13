---
id: p04_skill_simplify
kind: skill
pillar: P04
title: "Skill: Code Simplification"
version: 1.0.0
quality: 8.8
tags: [skill, simplify, refactor, code-quality]
tldr: "Code simplification skill for reviewing changed code for reuse opportunities, quality issues, and efficiency improvements."
domain: "tools"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.89
---

# Simplification Procedures

## When to Simplify

Trigger simplification review after any code change that:
- Adds more than 50 lines to a single file
- Introduces a new abstraction (class, module, utility)
- Duplicates logic that exists elsewhere in the codebase
- Has cyclomatic complexity > 10 in any function

## Simplification Checklist

### 1. Reuse Analysis
- Search for existing utilities that do the same thing
- Check if a library already handles this use case
- Identify copy-paste patterns across files
- Prefer composition over new abstractions

### 2. Complexity Reduction
- Extract complex conditionals into named boolean variables
- Replace nested if/else chains with early returns
- Use data structures (dicts, tables) over switch/case
- Eliminate dead code and unreachable branches

### 3. Readability Improvements
- Rename variables to reveal intent (not implementation)
- Break long functions into steps with descriptive names
- Remove comments that restate the code
- Add comments only where logic is non-obvious

### 4. Efficiency Review
- Identify O(n^2) loops that could be O(n) with a set/dict
- Check for repeated expensive operations (file I/O, API calls)
- Verify resource cleanup (file handles, connections)
- Review error handling for missing edge cases

## Output

Report changes as a diff with rationale for each simplification.
