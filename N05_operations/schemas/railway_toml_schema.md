---
id: p06_schema_railway_toml
kind: input_schema
pillar: P06
title: Railway TOML Configuration Schema
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: n05_operations
domain: railway-backend-operations
quality: 9.1
tags: [schema, railway, toml, nixpacks, deployment]
tldr: Schema for railway.toml configuration validation covering buildCommand, startCommand, healthcheckPath, and nixpacks settings.
schema_type: toml_config
validation_level: strict
---

# Railway TOML Schema

## Purpose

Validates railway.toml configuration files for Railway platform deployments
to ensure proper buildCommand, startCommand, healthcheckPath, and nixpacks settings.

## Schema Definition

```yaml
railway_toml:
  required: true
  sections:
    build:
      required: true
      properties:
        builder:
          type: string
          enum: ["nixpacks", "dockerfile", "buildpacks"]
          default: "nixpacks"
        buildCommand:
          type: string
          pattern: "^(npm|yarn|pip|python|poetry|cargo).*"
        watchPatterns:
          type: array
          items: {type: string}
    
    deploy:
      required: true  
      properties:
        startCommand:
          type: string
          required: true
          pattern: "^(uvicorn|gunicorn|npm|node|python).*"
        healthcheckPath:
          type: string
          required: true
          pattern: "^/health"
        healthcheckTimeout:
          type: integer
          minimum: 30
          maximum: 300
          default: 300
        restartPolicyType:
          type: string
          enum: ["always", "on_failure", "never"]
          default: "on_failure"
        restartPolicyMaxRetries:
          type: integer
          minimum: 1
          maximum: 10
          default: 10
```

## Validation Rules

- buildCommand must match deployment technology (npm/pip/poetry/cargo)
- startCommand required for uvicorn/gunicorn FastAPI applications
- healthcheckPath must start with "/health" for monitoring
- healthcheckTimeout between 30-300 seconds for Railway platform
- restartPolicy configured for production resilience

## Example Valid Config

```toml
[build]
builder = "nixpacks"
buildCommand = "pip install -r requirements.txt"

[deploy]
startCommand = "uvicorn main:app --host 0.0.0.0 --port $PORT"
healthcheckPath = "/health"
healthcheckTimeout = 30
restartPolicyType = "on_failure"
restartPolicyMaxRetries = 3
```


## Railway Deployment Configuration

The Railway TOML schema defines deployment parameters with validation:

- **Build configuration**: specify builder, build command, and environment variables
- **Service routing**: configure custom domains, ports, and health check paths
- **Scaling rules**: define min/max instances and auto-scaling triggers
- **Environment separation**: distinct configs per environment (dev/staging/prod)

### Full Configuration Example

```toml
# railway.toml - production configuration
[build]
builder = "nixpacks"
buildCommand = "pip install -r requirements.txt"

[deploy]
startCommand = "python main.py"
healthcheckPath = "/health"
healthcheckTimeout = 30
restartPolicyType = "on-failure"
restartPolicyMaxRetries = 3

[service]
internalPort = 8080
```

| Field | Required | Default | Validation |
|-------|----------|---------|-----------|
| builder | No | nixpacks | Enum: nixpacks, dockerfile |
| startCommand | Yes | - | Non-empty string |
| healthcheckPath | No | / | Valid URL path |
| internalPort | No | 8080 | 1-65535 |

