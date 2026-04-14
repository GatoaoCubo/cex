---
kind: examples
id: bld_examples_edit_format
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of edit_format artifacts
quality: null
title: "Examples Edit Format"
version: "1.0.0"
author: wave1_builder_gen
tags: [edit_format, builder, examples]
tldr: "Golden and anti-examples of edit_format artifacts"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```yaml
---
file_path: /docs/README.md
format_version: 2.0
description: Update documentation structure and content
---
- edit: replace_header
  from: "## Introduction"
  to: "## Overview"
  reason: "More descriptive title"
- edit: modify_section
  target: "## Features"
  changes:
    - replace "Fast" with "High-performance"
    - add bullet: "Scalable architecture"
- edit: add_section
  after: "## Features"
  content: "## Usage\n\nBasic commands:\n- `cmd --help`\n- `cmd run`"
```

## Anti-Example 1: Missing Frontmatter
```markdown
- edit: replace_header
  from: "## Introduction"
  to: "## Overview"
  reason: "More descriptive title"
- edit: modify_section
  target: "## Features"
  changes:
    - replace "Fast" with "High-performance"
```
## Why it fails
Lacks metadata required for file identification and version control. No way to determine target file path or format specification version.

## Anti-Example 2: Mixing Diff Strategy
```yaml
---
file_path: /docs/README.md
format_version: 2.0
---
- edit: replace_header
  from: "## Introduction"
  to: "## Overview"
  reason: "More descriptive title"
  diff_strategy: "line-based"
- edit: modify_section
  target: "## Features"
  changes:
    - replace "Fast" with "High-performance"
    - diff_strategy: "semantic"
```
## Why it fails
Includes diff_strategy parameters which belong to a different specification layer. Edit_format should only describe what changes to make, not how to compute them.
