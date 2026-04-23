---
id: kc_pre_commit_hooks_for_ai
kind: knowledge_card
title: "Pre-Commit Hooks for AI-Generated Code"
version: 1.0.0
quality: 8.9
pillar: P01
language: en
density_score: 0.92
updated: "2026-04-13"
related:
  - p04_skill_verify
  - p11_qg_artifact
  - validate
  - bld_instruction_function_def
  - tpl_response_format
  - bld_instruction_output_validator
  - p02_agent_code_review
  - bld_instruction_document_loader
  - bld_instruction_kind
  - p03_sp_verification_agent
---

# Pre-Commit Hooks for AI-Generated Code

## 1. YAML Validation
- Validate file structure using YAML schema
- Ensure proper indentation (2 spaces)
- Check for missing/incorrect metadata fields
- Verify versioning consistency
- Enforce schema compliance (id, kind, title, version, language, density_score)
- Validate pillar codes (P01-P05)
- Confirm language codes (en/pt/ru/etc.)
- Check for duplicate metadata entries
- Validate date formats (YYYY-MM-DD)

## 2. ASCII Enforcement
- Reject non-ASCII characters in:
  - File names (e.g., `README.md` ✅ vs `README_ç.md` ❌)
  - Code comments (e.g., `# This is a comment` ✅ vs `# C'est un commentaire` ❌)
  - String literals (e.g., `"Hello"` ✅ vs `"Héllo"` ❌)
- Use Unicode normalization (NFKC) for safe encoding
- Enforce ASCII-only file extensions (.md, .yml, .txt)
- Block surrogate pairs (e.g., `\uD83D\uDE00` ❌)
- Validate control characters (e.g., `\x1B` ❌)

## 3. Frontmatter Checks
- Validate required fields: `id`, `kind`, `title`, `version`
- Check for valid YAML syntax (no trailing commas)
- Ensure proper formatting of metadata values
- Verify language code compliance (en/pt/ru/etc.)
- Validate pillar codes (P01-P05)
- Confirm density_score range (0.0-1.0)
- Check for duplicate metadata entries
- Validate date formats (YYYY-MM-DD)
- Enforce maximum metadata line length (80 chars)

## 4. Encoding Verification
- Confirm UTF-8 encoding with BOM
- Scan for hidden control characters (e.g., `\x00` ❌)
- Validate byte order mark (BOM) presence
- Check for invalid Unicode sequences (e.g., `\U0010FFFF` ❌)
- Enforce BOM consistency (UTF-8 vs UTF-16)
- Validate line endings (CRLF vs LF)
- Check for encoding mismatches (UTF-8 vs ISO-8859-1)
- Block non-printable ASCII (0x00-0x1F)
- Verify file encoding consistency (UTF-8 only)

## 5. Quality Gates
- Minimum quality score: 8.0/10.0
- Validate against P01 knowledge schema
- Check for consistent terminology
- Verify compliance with CEX standards
- Ensure proper formatting and structure
- Enforce minimum line count (50 lines)
- Validate density_score threshold (≥0.85)
- Check for duplicate content
- Verify artifact versioning (semantic versioning)
- Confirm metadata completeness (100% required fields)

## Comparison of Pre-Commit Validation Tools

| Check Type        | Tool/Method       | Supported Languages | Encoding Standards | Compliance Frameworks |
|-------------------|-------------------|---------------------|--------------------|------------------------|
| YAML Schema       | PyYAML            | All                 | UTF-8              | JSON Schema            |
| ASCII Enforcement | re2               | All                 | ASCII              | POSIX                |
| Frontmatter Checks | ruamel.yaml     | All                 | UTF-8              | YAML 1.2             |
| Encoding Verification | chardet     | All                 | UTF-8/UTF-16       | ISO 8859-1           |
| Quality Gates     | CEX Validator     | All                 | UTF-8              | CEX P01-P05          |

## Related Kinds
- **code_standard**: Defines formatting rules enforced by these hooks
- **validation_tool**: Implements the actual checks described in this artifact
- **quality_gate**: Ensures artifacts meet minimum quality thresholds
- **ai_code_policy**: Specifies guidelines for AI-generated content
- **cex_artifact**: Represents the broader category of CEX knowledge cards

## Boundary
Distilled, static, versioned knowledge. NOT instruction, template, or configuration.

## 8F Pipeline Function
Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_skill_verify]] | downstream | 0.23 |
| [[p11_qg_artifact]] | downstream | 0.23 |
| [[validate]] | downstream | 0.22 |
| [[bld_instruction_function_def]] | downstream | 0.21 |
| [[tpl_response_format]] | downstream | 0.21 |
| [[bld_instruction_output_validator]] | downstream | 0.20 |
| [[p02_agent_code_review]] | downstream | 0.19 |
| [[bld_instruction_document_loader]] | downstream | 0.19 |
| [[bld_instruction_kind]] | downstream | 0.19 |
| [[p03_sp_verification_agent]] | downstream | 0.18 |
