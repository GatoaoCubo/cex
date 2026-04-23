---
kind: output_template
id: bld_output_template_openapi_spec
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an openapi_spec artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 8.6
title: "Output Template OpenAPI Spec"
version: "1.0.0"
author: n03_builder
tags: [openapi_spec, builder, output_template]
tldr: "Fill-in template for openapi_spec: OAS 3.1 document, security scheme, error response table."
domain: "openapi spec construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_output_template_input_schema
  - p04_function_def_NAME
  - bld_output_template_function_def
  - bld_schema_validation_schema
  - p03_ch_kc_to_notebooklm
  - p03_ch_content_pipeline
  - bld_knowledge_card_input_schema
  - p03_react_web_research
  - bld_schema_input_schema
  - bld_schema_model_registry
---

# Output Template: openapi_spec

```yaml
id: p06_oas_{{api_slug}}
kind: openapi_spec
pillar: P06
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
api_name: "{{human_friendly_api_name}}"
oas_version: "3.1.0"
quality: null
tags: [openapi_spec, {{api_slug}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
```

## OpenAPI Document

```yaml
openapi: "3.1.0"
info:
  title: {{api_name}}
  version: "{{api_version}}"
  description: {{api_description_one_line}}
servers:
  - url: {{production_base_url}}
    description: Production
paths:
  {{path_1}}:
    {{method_1}}:
      operationId: {{camelCaseOperationId}}
      summary: {{short_imperative_phrase}}
      tags: [{{tag}}]
      parameters:
        - name: {{param_name}}
          in: {{path|query|header|cookie}}
          required: {{true|false}}
          schema:
            type: {{string|integer|boolean}}
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/{{RequestSchema}}"
      responses:
        "{{success_code}}":
          description: {{success_description}}
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/{{ResponseSchema}}"
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "404":
          $ref: "#/components/responses/NotFound"
components:
  schemas:
    {{ModelName}}:
      type: object
      required: [{{required_fields}}]
      properties:
        {{field_name}}:
          type: {{type}}
          format: {{format_optional}}
    ErrorResponse:
      type: object
      required: [code, message]
      properties:
        code: {type: string}
        message: {type: string}
  responses:
    BadRequest:
      description: Invalid request parameters
      content:
        application/json:
          schema: {$ref: "#/components/schemas/ErrorResponse"}
    Unauthorized:
      description: Authentication required or invalid
      content:
        application/json:
          schema: {$ref: "#/components/schemas/ErrorResponse"}
    NotFound:
      description: Resource not found
      content:
        application/json:
          schema: {$ref: "#/components/schemas/ErrorResponse"}
  securitySchemes:
    {{scheme_name}}:
      type: {{http|apiKey|oauth2|openIdConnect}}
      scheme: {{bearer|basic}}
      bearerFormat: {{JWT|optional}}
security:
  - {{scheme_name}}: []
```

## Security

`{{auth_method_description_1_sentence}}`
Operations without auth: `{{list_public_paths_or_none}}`

## Error Responses

| Code | Meaning | Schema |
|------|---------|--------|
| 400 | {{validation_error_description}} | ErrorResponse |
| 401 | {{auth_error_description}} | ErrorResponse |
| 404 | {{not_found_description}} | ErrorResponse |
| 500 | Internal server error | ErrorResponse |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_input_schema]] | sibling | 0.27 |
| [[p04_function_def_NAME]] | upstream | 0.25 |
| [[bld_output_template_function_def]] | sibling | 0.25 |
| [[bld_schema_validation_schema]] | downstream | 0.22 |
| [[p03_ch_kc_to_notebooklm]] | upstream | 0.22 |
| [[p03_ch_content_pipeline]] | upstream | 0.22 |
| [[bld_knowledge_card_input_schema]] | upstream | 0.21 |
| [[p03_react_web_research]] | upstream | 0.21 |
| [[bld_schema_input_schema]] | downstream | 0.21 |
| [[bld_schema_model_registry]] | downstream | 0.20 |
