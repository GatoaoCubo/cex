---
id: kc_pre_commit_hooks_for_ai
kind: knowledge_card
title: "Pre-Commit Hooks for AI-Generated Code"
version: 1.0.0
quality: 8.7
pillar: P01
language: en
---

# Pre-Commit Hooks for AI-Generated Code

## 1. YAML Validation
- Validate file structure using YAML schema
- Ensure proper indentation (2 spaces)
- Check for missing/incorrect metadata fields
- Verify versioning consistency

## 2. ASCII Enforcement
- Reject non-ASCII characters in:
  - File names
  - Code comments
  - String literals
- Use Unicode normalization (NFKC) for safe encoding

## 3. Frontmatter Checks
- Validate required fields: `id`, `kind`, `title`, `version`
- Check for valid YAML syntax
- Ensure proper formatting of metadata values
- Verify language code compliance (en/pt/ru/etc.)

## 4. Encoding Verification
- Confirm UTF-8 encoding with BOM
- Scan for hidden control characters
- Validate byte order mark (BOM) presence
- Check for invalid Unicode sequences

## 5. Quality Gates
- Minimum quality score: 8.0/10.0
- Validate against P01 knowledge schema
- Check for consistent terminology
- Verify compliance with CEX standards
- Ensure proper formatting and structure
