---
kind: examples
id: bld_examples_openapi_spec
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of openapi_spec artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: null
title: "Examples OpenAPI Spec"
version: "1.0.0"
author: n03_builder
tags: [openapi_spec, builder, examples]
tldr: "Golden and anti-examples for openapi_spec construction: paths, schemas, security, error responses."
domain: "openapi spec construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Examples: openapi-spec-builder

## Golden Example

INPUT: "Create OpenAPI spec for a User Management API with JWT auth"

WHY THIS IS GOLDEN:
- id matches `^p06_oas_[a-z][a-z0-9_]+$` -- H02 pass
- oas_version declared as 3.1.0 -- H03 pass
- servers array present -- H04 pass
- paths with at least one operation -- H05 pass
- All 3 body sections present -- H06 pass
- quality: null -- H01 pass
- components.schemas referenced via $ref -- best practice
- securitySchemes with global security -- H07 pass

```yaml
id: p06_oas_user_management_api
kind: openapi_spec
pillar: P06
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
api_name: "User Management API"
oas_version: "3.1.0"
quality: null
tags: [openapi_spec, user_management, jwt_auth]
tldr: "OAS 3.1 spec for User Management API: CRUD users, JWT bearer auth, standard error responses"
```

## OpenAPI Document

```yaml
openapi: "3.1.0"
info:
  title: User Management API
  version: "1.0.0"
  description: CRUD operations for user lifecycle management
servers:
  - url: https://api.example.com/v1
    description: Production
  - url: https://staging-api.example.com/v1
    description: Staging
paths:
  /users:
    get:
      operationId: listUsers
      summary: List all users
      tags: [users]
      parameters:
        - name: page
          in: query
          schema: {type: integer, default: 1}
        - name: limit
          in: query
          schema: {type: integer, default: 20, maximum: 100}
      responses:
        "200":
          description: User list
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/UserList"
        "401":
          $ref: "#/components/responses/Unauthorized"
    post:
      operationId: createUser
      summary: Create user
      tags: [users]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CreateUserRequest"
      responses:
        "201":
          description: Created
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/User"
        "400":
          $ref: "#/components/responses/BadRequest"
  /users/{id}:
    get:
      operationId: getUser
      summary: Get user by ID
      tags: [users]
      parameters:
        - name: id
          in: path
          required: true
          schema: {type: string, format: uuid}
      responses:
        "200":
          description: User found
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/User"
        "404":
          $ref: "#/components/responses/NotFound"
components:
  schemas:
    User:
      type: object
      required: [id, email, created_at]
      properties:
        id: {type: string, format: uuid}
        email: {type: string, format: email}
        name: {type: string}
        created_at: {type: string, format: date-time}
    UserList:
      type: object
      properties:
        items:
          type: array
          items: {$ref: "#/components/schemas/User"}
        total: {type: integer}
    CreateUserRequest:
      type: object
      required: [email]
      properties:
        email: {type: string, format: email}
        name: {type: string}
    ErrorResponse:
      type: object
      required: [code, message]
      properties:
        code: {type: string}
        message: {type: string}
  responses:
    BadRequest:
      description: Invalid request
      content:
        application/json:
          schema: {$ref: "#/components/schemas/ErrorResponse"}
    Unauthorized:
      description: Authentication required
      content:
        application/json:
          schema: {$ref: "#/components/schemas/ErrorResponse"}
    NotFound:
      description: Resource not found
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

JWT bearer authentication. Declare `Authorization: Bearer <token>` on all requests.
Security override per-operation: `security: []` for public endpoints (e.g. /health).

## Error Responses

| Code | Meaning | Schema |
|------|---------|--------|
| 400 | Validation error | ErrorResponse |
| 401 | Missing/invalid JWT | ErrorResponse |
| 404 | Resource not found | ErrorResponse |
| 500 | Internal server error | ErrorResponse |

---

## Anti-Example

INPUT: "Create API spec for users"
BAD OUTPUT:
```yaml
id: users-api
kind: api_spec
paths:
  /users:
    get:
      responses:
        200:
          description: ok
quality: 8.0
```

FAILURES:
1. id: "users-api" has hyphens, no p06_oas_ prefix -> H02 FAIL
2. kind: "api_spec" not "openapi_spec" -> H04 FAIL
3. Missing oas_version, servers, components -> H03/H04 FAIL
4. No security scheme declared -> H07 FAIL
5. quality: 8.0 (not null) -> H01 FAIL
6. Missing all 3 body sections -> H06 FAIL
7. Response schema missing content/schema -> incomplete spec
