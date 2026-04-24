---
quality: 8.6
quality: 8.3
id: p06_oas_cex_sdk
kind: openapi_spec
8f: F5_call
pillar: P06
version: "1.0.0"
created: "2026-04-19"
updated: "2026-04-19"
author: "n03_engineering"
api_name: "CEX SDK Runtime API"
oas_version: "3.1.0"
tags: [openapi_spec, cex_sdk, P06, rest, artifact_production]
tldr: "CEX SDK Runtime API OAS 3.1: 5 operations (build, validate, score, get artifact, health). Bearer token auth. Source: cex_sdk v10.2.0."
related:
  - bld_examples_workflow_primitive
  - p06_is_creation_data
  - p06_is_knowledge_data_model
  - bld_schema_model_registry
  - p04_function_def_NAME
  - bld_knowledge_card_function_def
  - bld_output_template_input_schema
  - ctx_cex_new_dev_guide
  - n06_input_schema_content_order
  - bld_knowledge_card_input_schema
density_score: 1.0
---

# OpenAPI Spec: CEX SDK Runtime API

REST-like interface exposed by `cex_sdk` for programmatic artifact production.
Describes the surface area used by nuclei (N01-N07) and external contributors
to trigger builds, validate outputs, and retrieve scored artifacts.

Source library: `cex_sdk/__init__.py` v10.2.0
Key imports: `CEXAgent`, `Claude`, `Workflow`, `InputSchema`, `Validator`

## OpenAPI Document

```yaml
openapi: "3.1.0"
info:
  title: CEX SDK Runtime API
  version: "1.0.0"
  description: Programmatic interface for CEX artifact production, validation, and retrieval.
servers:
  - url: http://localhost:8900
    description: Local development (cex_sdk serve)
paths:
  /build:
    post:
      operationId: buildArtifact
      summary: Build artifact from intent via 8F pipeline
      tags: [artifacts]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/BuildRequest"
      responses:
        "202":
          description: Build accepted, returns job_id for async poll
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/BuildJob"
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"

  /build/{job_id}:
    get:
      operationId: getBuildStatus
      summary: Poll build job status
      tags: [artifacts]
      parameters:
        - name: job_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        "200":
          description: Job status and result when complete
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/BuildResult"
        "404":
          $ref: "#/components/responses/NotFound"

  /validate:
    post:
      operationId: validateArtifact
      summary: Validate artifact against quality gates (F7 GOVERN)
      tags: [quality]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/ValidateRequest"
      responses:
        "200":
          description: Validation result with gate pass/fail breakdown
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ValidateResult"
        "400":
          $ref: "#/components/responses/BadRequest"

  /artifacts/{id}:
    get:
      operationId: getArtifact
      summary: Retrieve artifact by canonical id
      tags: [artifacts]
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            description: Canonical artifact id (e.g., p06_ar_artifact)
      responses:
        "200":
          description: Artifact frontmatter and body
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Artifact"
        "404":
          $ref: "#/components/responses/NotFound"

  /health:
    get:
      operationId: healthCheck
      summary: SDK health and version info
      tags: [meta]
      security: []
      responses:
        "200":
          description: Health OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/HealthResponse"

components:
  schemas:
    BuildRequest:
      type: object
      required: [intent, nucleus]
      properties:
        intent:
          type: string
          description: Natural language or structured intent (e.g., "document the 8F pipeline")
        nucleus:
          type: string
          enum: [n01, n02, n03, n04, n05, n06, n07]
          description: Target nucleus to execute the build
        kind:
          type: string
          description: Override resolved kind (optional; if omitted, resolved via intent transmutation)
        pillar:
          type: string
          pattern: "^P(0[1-9]|1[0-2])$"
          description: Override pillar (optional)

    BuildJob:
      type: object
      required: [job_id, status]
      properties:
        job_id:
          type: string
          format: uuid
        status:
          type: string
          enum: [queued, running, complete, failed]
        created_at:
          type: string
          format: date-time

    BuildResult:
      type: object
      required: [job_id, status]
      properties:
        job_id:
          type: string
          format: uuid
        status:
          type: string
          enum: [queued, running, complete, failed]
        artifact_id:
          type: string
          description: Canonical artifact id if status=complete
        artifact_path:
          type: string
          description: Relative path to written file
        score:
          type: number
          minimum: 0.0
          maximum: 10.0
        error:
          type: string
          description: Error message if status=failed

    ValidateRequest:
      type: object
      required: [artifact_path]
      properties:
        artifact_path:
          type: string
          description: Relative path to artifact .md file

    ValidateResult:
      type: object
      required: [passed, score, gates]
      properties:
        passed:
          type: boolean
        score:
          type: number
          minimum: 0.0
          maximum: 10.0
        gates:
          type: object
          description: "Gate id -> pass/fail: {H01: true, H02: false, ...}"
        twelve_lp:
          type: object
          description: "12LP checklist results: {LP01: true, ...}"

    Artifact:
      type: object
      required: [id, kind, pillar, quality]
      properties:
        id:
          type: string
        kind:
          type: string
        pillar:
          type: string
        quality:
          type: number
          nullable: true
        frontmatter:
          type: object
          description: Full parsed frontmatter as key-value map
        body:
          type: string
          description: Markdown body of the artifact

    HealthResponse:
      type: object
      required: [status, version]
      properties:
        status:
          type: string
          enum: [ok, degraded]
        version:
          type: string
          description: cex_sdk version (e.g., 10.2.0)
        pillar_coverage:
          type: string
          description: "12/12"
        kinds_loaded:
          type: integer

    ErrorResponse:
      type: object
      required: [code, message]
      properties:
        code:
          type: string
        message:
          type: string

  responses:
    BadRequest:
      description: Invalid request parameters or schema violation
      content:
        application/json:
          schema: {$ref: "#/components/schemas/ErrorResponse"}
    Unauthorized:
      description: Bearer token missing or invalid
      content:
        application/json:
          schema: {$ref: "#/components/schemas/ErrorResponse"}
    NotFound:
      description: Artifact or job not found
      content:
        application/json:
          schema: {$ref: "#/components/schemas/ErrorResponse"}

  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - bearerAuth: []
```

## Security

Bearer JWT token required on all operations except `GET /health`.
Token encodes `nucleus_id` claim for audit attribution (who requested which build).
Operations without auth: `GET /health` only.

## Error Responses

| Code | Meaning | Schema |
|------|---------|--------|
| 400 | Invalid intent, missing required field, or kind not in kinds_meta.json | ErrorResponse |
| 401 | Bearer token absent, expired, or invalid nucleus_id claim | ErrorResponse |
| 404 | Artifact id not found or job_id not in queue | ErrorResponse |
| 500 | Internal 8F pipeline failure (F8 save error, compile crash) | ErrorResponse |

## References

- SDK source: `cex_sdk/__init__.py` (v10.2.0, 12/12 pillar coverage)
- CEXAgent: `cex_sdk/agent/`
- Validator: `cex_sdk/schema/` -> maps to ValidateRequest/Result above
- Kind registry: `.cex/kinds_meta.json` (constrains valid `kind` values in BuildRequest)
- Aggregate root: `N03_engineering/P06_schema/aggregate_root_artifact.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_workflow_primitive]] | downstream | 0.21 |
| [[p06_is_creation_data]] | related | 0.21 |
| [[p06_is_knowledge_data_model]] | related | 0.20 |
| [[bld_schema_model_registry]] | related | 0.19 |
| [[p04_function_def_NAME]] | upstream | 0.19 |
| [[bld_knowledge_card_function_def]] | upstream | 0.19 |
| [[bld_output_template_input_schema]] | upstream | 0.19 |
| [[ctx_cex_new_dev_guide]] | related | 0.18 |
| [[n06_input_schema_content_order]] | related | 0.18 |
| [[bld_knowledge_card_input_schema]] | upstream | 0.18 |
