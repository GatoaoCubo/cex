---
id: p04_skill_verify
kind: skill
pillar: P04
title: "Skill: Verification Protocol"
version: 1.0.0
quality: null
tags: [skill, verification, quality, validation]
tldr: "Verification skill defining step-by-step procedures for artifact validation. Used by F7 GOVERN and the verification agent."
domain: "tools"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
---

# Verification Protocol

## Pre-Verification Checklist

Before scoring, verify these structural requirements:

1. File exists at expected path matching naming convention
2. YAML frontmatter is parseable with all required fields
3. Content is non-empty and exceeds minimum density threshold
4. Kind matches one of the 123 registered kinds in kinds_meta.json
5. Pillar assignment is correct for the artifact kind

## Verification Steps

### Step 1: Structural Validation
- Parse frontmatter, extract id/kind/pillar/title/version
- Verify quality field is null (never self-scored)
- Check file size against max_bytes from schema
- Validate naming pattern: {pillar_code}_{kind_prefix}_{slug}

### Step 2: Content Validation
- Verify all required sections exist per kind template
- Check content density (substantive bytes / total bytes >= 0.85)
- Scan for placeholder text ([TODO], [PLACEHOLDER], lorem ipsum)
- Verify cross-references point to existing artifacts

### Step 3: Integration Validation
- Compile artifact: python _tools/cex_compile.py {path}
- Verify compiled output is valid YAML/JSON
- Check artifact loads via prompt_layers or retriever
- Verify no duplicate IDs in the compiled directory

### Step 4: Report
- Generate score across 5 dimensions (D1-D5)
- List all gate pass/fail results
- Provide actionable fix recommendations for failures
- Output in structured format for automated processing
