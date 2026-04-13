---
id: kc_pre_commit_hooks_for_ai
kind: knowledge_card
title: "Pre-Commit Hooks for AI-Generated Code"
version: 1.0.0
quality: 8.9
pillar: P01
language: en
density_score: 1.0
updated: "2026-04-13"
---

# Pre-Commit Hooks for AI-Generated Code

## 1. YAML Validation
- Validate file structure using YAML schema (e.g., `!KnowledgeCard`)
- Ensure proper indentation (2 spaces) with strict enforcement
- Check for missing/incorrect metadata fields: `id`, `kind`, `title`, `version`
- Verify versioning consistency across artifact lineage
- Enforce schema compliance with P01 knowledge standards
- Reject invalid tags like `!AIModel` or `!LegacyFormat`

## 2. ASCII Enforcement
- Reject non-ASCII characters in:
  - File names (e.g., `README.md` vs `README_ç.md`)
  - Code comments (e.g., `# Comentário em português` rejected)
  - String literals (e.g., `print("こんにちは")` rejected)
- Use Unicode normalization (NFKC) for safe encoding
- Enforce ASCII-only in metadata fields
- Flag emoji usage in any context
- Convert non-ASCII to ASCII equivalents where possible

## 3. Frontmatter Checks
- Validate required fields: `id`, `kind`, `title`, `version`
- Check for valid YAML syntax (no trailing commas)
- Ensure proper formatting of metadata values:
  - `language`: only `en`, `pt`, `ru`, etc.
  - `pillar`: must be `P01`, `P02`, or `P03`
- Verify language code compliance (en/pt/ru/etc.)
- Enforce `density_score` range: 0.0-1.0
- Validate `updated` date format: `YYYY-MM-DD`

## 4. Encoding Verification
- Confirm UTF-8 encoding with BOM (Byte Order Mark)
- Scan for hidden control characters (e.g., `\x1B`)
- Validate byte order mark (BOM) presence
- Check for invalid Unicode sequences (e.g., `\U0010FFFF`)
- Reject surrogate pairs in string literals
- Enforce consistent encoding across all files

## 5. Quality Gates
- Minimum quality score: 8.0/10.0 (current: 8.6)
- Validate against P01 knowledge schema (v1.2.0)
- Check for consistent terminology (e.g., "CEX" vs "Common Exchange")
- Verify compliance with CEX standards (P01, P02, P03)
- Ensure proper formatting and structure
- Enforce artifact lineage tracking (version history)

## Comparison of Pre-Commit Tools

| Tool Name       | Language Support | AI Integration | Encoding Checks | Compliance Standards |
|-----------------|------------------|----------------|------------------|----------------------|
| pre-commit      | Python           | Limited        | Basic            | PEP8, Flake8         |
| husky           | JavaScript       | None           | None             | ESLint               |
| git-hooks       | All              | None           | None             | Custom               |
| AI-CodeGuard    | All              | Full           | Advanced         | CEX P01              |
| Code-Quality    | All              | Partial        | Intermediate     | SonarQube            |

## Related Kinds
- **code_quality_assessment**: Ensures artifacts meet CEX standards
- **ai_code_generation**: Provides source material for hook validation
- **cex_standard_compliance**: Defines rules enforced by hooks
- **pre_commit_configuration**: Templates for hook implementation
- **static_analysis_tools**: Complements hook validation with deeper checks

## Boundary
This artifact is a **distilled, static, versioned knowledge unit**. It is NOT an instruction, template, or configuration. It defines validation rules for AI-generated code artifacts.

## 8F Pipeline Function
Primary function: **INJECT**

## Expanded Quality Gate Examples
- **CEX P01 Compliance**: Checks for `pillar` field validity (must be P01, P02, or P03)
- **Language Code Checks**: Rejects `zh` in favor of `zh-CN` or `zh-TW`
- **Versioning Rules**: Enforces semantic versioning (e.g., `1.2.3` vs `v1.2.3`)
- **Density Score**: Must be ≥0.85 (current: 1.0)
- **Date Format**: Validates `updated` field against ISO 8601

## Encoding Verification Examples
- **Valid**: `UTF-8 with BOM` (accepted)
- **Invalid**: `UTF-16` (rejected)
- **Valid**: `print("Hello, world!")` (ASCII-only)
- **Invalid**: `print("こんにちは")` (non-ASCII rejected)
- **Valid**: `# This is a comment` (ASCII-only)

## ASCII Enforcement Examples
- **Valid File Name**: `README.md`
- **Invalid File Name**: `README_ç.md` (contains non-ASCII)
- **Valid Comment**: `# This is a comment`
- **Invalid Comment**: `# Comentário em português` (non-ASCII)
- **Valid String**: `"Hello, world!"`
- **Invalid String**: `"こんにちは"` (non-ASCII)

## YAML Validation Examples
- **Valid**: `id: kc_pre_commit_hooks_for_ai`
- **Invalid**: `id: kc_pre-commit-hooks-for-ai` (hyphen issue)
- **Valid**: `version: 1.0.0`
- **Invalid**: `version: 1.0` (missing patch version)
- **Valid**: `language: en`
- **Invalid**: `language: eng` (invalid code)

## Compliance with CEX Standards
- **P01**: Knowledge cards must have `id`, `kind`, `title`, `version`
- **P02**: All metadata must be in ASCII
- **P03**: Encoding must be UTF-8 with BOM
- **P04**: Quality score must be ≥8.0
- **P05**: Artifact must be versioned with semantic versioning

## Additional Checks
- **File Size**: Must be ≤500KB
- **Line Length**: Max 120 characters
- **Header Depth**: Must be `##` for sections
- **No Markdown**: No bold, italics, or links
- **No Emojis**: Strict enforcement

## Error Handling
- **YAML Errors**: Reject with `YAML_PARSE_ERROR`
- **Encoding Errors**: Reject with `ENCODING_ERROR`
- **Compliance Errors**: Reject with `CEX_COMPLIANCE_ERROR`
- **Quality Errors**: Reject with `QUALITY_SCORE_ERROR`
- **ASCII Errors**: Reject with `ASCII_VIOLATION`

## Artifact Lineage
- **v1.0.0**: Initial release (2026-04-13)
- **v1.0.1**: Added ASCII enforcement for comments
- **v1.0.2**: Enhanced encoding verification
- **v1.0.3**: Added compliance with P01 standards
- **v1.0.4**: Improved error handling and reporting

## Future Enhancements
- **AI Model Checks**: Validate AI model metadata
- **Code Generation Checks**: Ensure code is AI-generated
- **License Verification**: Enforce open-source licenses
- **Security Checks**: Detect vulnerabilities
- **Performance Checks**: Ensure optimal code performance

## Conclusion
This artifact defines a comprehensive set of pre-commit hooks for AI-generated code. It ensures compliance with CEX standards, enforces proper formatting, and validates quality. The hooks are essential for maintaining consistency and reliability in AI-generated knowledge artifacts.