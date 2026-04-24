---
id: p04_skill_verify
kind: skill
8f: F5_call
pillar: P04
title: "Skill: Verification Protocol"
version: 1.0.0
quality: 9.0
tags: [skill, verification, quality, validation]
tldr: "Verification skill defining step-by-step procedures for artifact validation. Used by F7 GOVERN and the verification agent."
domain: "tools"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
related:
  - p03_sp_verification_agent
  - shared_skill_verification_protocol
  - p08_ac_verification
  - p11_qg_artifact
  - bld_instruction_kind
  - p11_qg_knowledge
  - p07_qg_12_point_validation
  - p05_output_validator
  - p06_vs_frontmatter
  - skill
---

# Verification Protocol

## Boundary

This artifact defines the **process** for verifying CEX artifacts, including structural, content, and integration checks. It is **not** a tool or agent itself but provides the framework for validation. It does **not** execute verification actions or generate scores directly.

## Related Kinds

| Related Kind         | Relationship Description                                                                 |
|----------------------|------------------------------------------------------------------------------------------|
| skill: validation_agent | Executes the verification steps defined in this protocol.                               |
| tool: cex_compile     | Used during integration validation to compile artifacts into standardized formats.      |
| kind: quality_assurance | Ensures artifacts meet domain-specific quality standards referenced in this protocol.  |
| tool: artifact_registry | Validates cross-references by checking artifact existence in the registry.              |
| skill: compliance_check | Ensures artifacts adhere to governance and regulatory requirements.                     |

## Pre-Verification Checklist

Before scoring, verify these structural requirements:

1. **File existence**: Confirm the file exists at the expected path following the pattern `{pillar_code}_{kind_prefix}_{slug}` (e.g., `p04_skill_verify.md`).  
2. **YAML parsing**: Ensure the frontmatter is valid with required fields: `id`, `kind`, `pillar`, `title`, `version`, `tags`, `tldr`, `domain`, `author`, `created`, `updated`, `density_score`.  
3. **Content density**: Content must exceed 85% substantive bytes (excluding frontmatter) and avoid placeholders like `[TODO]` or `lorem ipsum`.  
4. **Kind validation**: The `kind` field must match one of 123 registered kinds in `kinds_meta.json`.  
5. **Pillar alignment**: The `pillar` field must align with the artifact's functional domain (e.g., `P04` for tools).  

## Verification Steps

### Step 1: Structural Validation

- **Parse frontmatter**: Extract metadata and validate required fields.  
- **Quality field check**: Ensure `quality` is `null` (artifacts are never self-scored).  
- **File size check**: Verify file size is below `max_bytes` (e.g., 5MB for markdown).  
- **Naming pattern**: Confirm filename matches `{pillar_code}_{kind_prefix}_{slug}` (e.g., `p04_skill_verify.md`).  

**Example**:  
- Valid: `p04_skill_verify.md`  
- Invalid: `skill_verify.md` (missing pillar code)  

### Step 2: Content Validation

- **Section completeness**: Ensure all required sections (e.g., `## Boundary`, `## Related Kinds`, `## Verification Steps`) exist.  
- **Density calculation**: Measure substantive bytes (text, code, tables) vs. total bytes (excluding frontmatter).  
- **Placeholder scan**: Detect and flag `[TODO]`, `[PLACEHOLDER]`, or lorem ipsum text.  
- **Cross-reference check**: Validate all links point to existing artifacts in the registry.  

**Example**:  
- Low density: 40% substantive content (fails threshold)  
- High density: 90% substantive content (passes threshold)  

### Step 3: Integration Validation

- **Compile artifact**: Run `python _tools/cex_compile.py {path}` to generate YAML/JSON output.  
- **Output validation**: Ensure compiled artifact is valid YAML/JSON with no syntax errors.  
- **Loading test**: Confirm artifact loads via `prompt_layers` or `retriever` interfaces.  
- **Duplicate check**: Scan for duplicate `id` fields in the compiled directory.  

**Example**:  
- Success: `compiled/p04_skill_verify.yaml` is valid JSON  
- Failure: Duplicate `id: p04_skill_verify` in directory  

### Step 4: Report

- **Score dimensions**: Generate scores across 5 dimensions (D1-D5):  
  - D1: Structural validity (0-100)  
  - D2: Content quality (0-100)  
  - D3: Integration success (0-100)  
  - D4: Cross-reference integrity (0-100)  
  - D5: Compliance with standards (0-100)  
- **Gate results**: List pass/fail status for each verification phase.  
- **Recommendations**: Provide actionable fixes (e.g., "Add missing `## Related Kinds` section").  
- **Structured output**: Format report as JSON for automated processing.  

**Example Report**:  
```json
{
  "D1": 95,
  "D2": 88,
  "D3": 100,
  "D4": 92,
  "D5": 98,
  "gates": {
    "structural": "pass",
    "content": "fail",
    "integration": "pass"
  },
  "recommendations": ["Replace placeholder text in section 2.3", "Add missing `## Related Kinds` section"]
}
```

## Comparison of Verification Tools and Methods

| Verification Phase | Purpose                          | Tools Used                  | Success Criteria                                | Common Issues                              |
|--------------------|----------------------------------|-----------------------------|-------------------------------------------------|--------------------------------------------|
| Structural         | Ensure metadata and format compliance | YAML parser, file system  | All required fields present, valid filename     | Missing `id` field, invalid naming pattern |
| Content            | Validate substantive content quality | Text analyzer, regex engine | Density ≥ 85%, no placeholders, sections complete | Low density, placeholder text, missing sections |
| Integration        | Confirm artifact compatibility   | `cex_compile.py`, loader    | Valid YAML/JSON, no duplicates, loads correctly | Compilation errors, duplicate IDs, load failures |
| Reporting          | Generate structured feedback     | JSON formatter, score engine | Valid JSON output, all gates resolved         | Invalid JSON, incomplete gate results    |
| Compliance         | Ensure adherence to standards    | Registry, policy checker    | All cross-references valid, meets domain rules  | Invalid links, non-compliant metadata    |

## Expanded Use Cases and Data

### Example 1: Structural Validation Failure  
- **Artifact**: `p04_skill_example.md`  
- **Issue**: Missing `domain` field in frontmatter  
- **Fix**: Add `domain: tools` to frontmatter  

### Example 2: Content Density Failure  
- **Artifact**: `p03_skill_template.md`  
- **Issue**: 70% substantive content (fails 85% threshold)  
- **Fix**: Expand sections with technical details or tables  

### Example 3: Integration Validation Success  
- **Artifact**: `p02_skill_guide.md`  
- **Output**: `compiled/p02_skill_guide.yaml` is valid JSON with no errors  
- **Impact**: Artifact is loadable via `retriever` and used in downstream systems  

### Example 4: Cross-Reference Failure  
- **Artifact**: `p01_skill_intro.md`  
- **Issue**: Link to non-existent artifact `p05_skill_unknown.md`  
- **Fix**: Update link to valid artifact `p05_skill_reference.md`  

### Example 5: Compliance Check Failure  
- **Artifact**: `p04_skill_verify.md`  
- **Issue**: Missing `## Related Kinds` section  
- **Fix**: Add section with 3-5 related kinds and relationships  

## Conclusion

This verification protocol ensures CEX artifacts meet structural, content, and integration standards. By following the steps and addressing reported issues, artifacts achieve high quality and compatibility. The process is critical for maintaining consistency across the CEX ecosystem.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_verification_agent]] | upstream | 0.38 |
| [[shared_skill_verification_protocol]] | sibling | 0.33 |
| [[p08_ac_verification]] | downstream | 0.31 |
| [[p11_qg_artifact]] | downstream | 0.30 |
| [[bld_instruction_kind]] | upstream | 0.27 |
| [[p11_qg_knowledge]] | downstream | 0.27 |
| [[p07_qg_12_point_validation]] | downstream | 0.26 |
| [[p05_output_validator]] | downstream | 0.25 |
| [[p06_vs_frontmatter]] | downstream | 0.24 |
| [[skill]] | downstream | 0.23 |
