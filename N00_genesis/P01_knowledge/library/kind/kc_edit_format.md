---
id: kc_edit_format
kind: knowledge_card
title: Edit Format Specification
version: 1.0.0
quality: 8.7
pillar: P01
density_score: 1.0
related:
  - bld_output_template_edit_format
  - tpl_response_format
  - kc_c2pa_manifest
  - bld_collaboration_content_filter
  - bld_examples_edit_format
  - p05_output_validator
  - p03_sp_edit_format_builder
  - p11_qg_response_format
  - bld_instruction_edit_format
  - p11_qg_content_filter
---

# LLM-to-Host File Change Format Specification

This document defines the standardized format for requesting file modifications to the host system. All change requests must follow this structure:

## 1. Base Structure
```yaml
change_type: [modify|create|delete]
file_path: "/absolute/path/to/file"
content: "new content"
metadata:
  reason: "change justification"
  timestamp: "ISO 8601 format"
```

## 2. Field Requirements
- **change_type** (required): Operation type (modify, create, delete)
- **file_path** (required): Absolute path with proper permissions
- **content** (required for modify/create): String content for modification
- **metadata** (optional): Additional context about the change

## 3. Special Cases
- **Delete Operation**: Omit content field
- **Binary Files**: Use base64 encoding for content
- **Permissions**: Include `permissions` field for file access control

## 4. Validation Rules
- All paths must be normalized
- Content must be UTF-8 encoded
- Metadata must include at least reason field
- Timestamp must be current UTC time

## 5. Example
```yaml
change_type: modify
file_path: "/home/user/config.yaml"
content: |
  format: yaml
  version: 2.1.0
metadata:
  reason: "Update configuration format to YAML"
  timestamp: "2023-10-15T14:48:00Z"
```

## 6. Error Handling
- Invalid format: Return 400 Bad Request
- Permission denied: Return 403 Forbidden
- File not found: Return 404 Not Found
```
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_edit_format]] | downstream | 0.25 |
| [[tpl_response_format]] | downstream | 0.22 |
| [[kc_c2pa_manifest]] | sibling | 0.20 |
| [[bld_collaboration_content_filter]] | downstream | 0.19 |
| [[bld_examples_edit_format]] | downstream | 0.18 |
| [[p05_output_validator]] | downstream | 0.18 |
| [[p03_sp_edit_format_builder]] | downstream | 0.18 |
| [[p11_qg_response_format]] | downstream | 0.18 |
| [[bld_instruction_edit_format]] | downstream | 0.18 |
| [[p11_qg_content_filter]] | downstream | 0.17 |
