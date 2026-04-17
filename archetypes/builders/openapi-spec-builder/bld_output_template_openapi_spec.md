---
kind: output_template
id: bld_output_template_openapi_spec
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an openapi_spec artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: null
title: "Output Template OpenAPI Spec"
version: "1.0.0"
author: n03_builder
tags: [openapi_spec, builder, output_template]
tldr: "Fill-in template for openapi_spec: OAS 3.1 document, security scheme, error response table."
domain: "openapi spec construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
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
