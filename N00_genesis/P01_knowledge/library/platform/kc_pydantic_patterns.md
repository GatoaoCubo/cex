---
id: p01_kc_pydantic_patterns
kind: knowledge_card
pillar: P01
title: "Pydantic V2 Patterns — Models, Validators, Settings"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [pydantic, validation, models, settings, python]
tldr: "Pydantic V2 patterns: BaseModel for request/response, field_validator for business rules, BaseSettings for env config, model_config for JSON serialization, discriminated unions for polymorphism."
density_score: 1.0
when_to_use: "Apply when pydantic v2 patterns: basemodel for request/response, field_validator for business rules, baseset..."
keywords: [knowledge-card, field-validator, model-config, pydantic, software-engineering]
axioms:
  - "AVOID: ❌ Using `dict` instead of Pydantic models (no validation)"
  - "AVOID: ❌ `os.getenv()` scattered everywhere (use BaseSettings)"
  - "AVOID: ❌ V1 syntax (`class Config: orm_mode = True`) — use `model_config`"
linked_artifacts:
  primary: null
  related: []
---

# Pydantic V2 Patterns

## BaseModel (Request/Response)

```python
from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class CreateTaskRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(default="", max_length=5000)
    priority: int = Field(default=5, ge=1, le=10)
    tags: list[str] = Field(default_factory=list, max_length=20)

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, v):
        return [t.lower().strip() for t in v if t.strip()]

class TaskResponse(BaseModel):
    model_config = {"from_attributes": True}  # ORM mode
    id: str
    title: str
    status: str
    created_at: datetime
```

## Field Constraints

```python
class Product(BaseModel):
    name: str = Field(..., min_length=1, max_length=300)
    price: float = Field(..., gt=0, le=999999.99)
    sku: str = Field(..., pattern=r'^[A-Z0-9-]{3,20}$')
    quantity: int = Field(default=0, ge=0)
    tags: list[str] = Field(default_factory=list, max_length=50)
    metadata: dict = Field(default_factory=dict)
```

## BaseSettings (Environment Config)

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = {"env_prefix": "APP_", "env_file": ".env"}

    database_url: str
    redis_url: str = "redis://localhost:6379/0"
    api_keys: str = ""            # Comma-separated
    debug: bool = False
    workers: int = 4
    log_level: str = "info"
    cors_origins: str = "http://localhost:3000"

    @property
    def api_key_set(self) -> set[str]:
        return {k.strip() for k in self.api_keys.split(",") if k.strip()}

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",")]

settings = Settings()  # Auto-reads from env + .env
```

**Usage**: `settings.database_url` reads `APP_DATABASE_URL` env var.

## Discriminated Unions

```python
from typing import Literal, Union
from pydantic import BaseModel

class EmailNotification(BaseModel):
    type: Literal["email"] = "email"
    to: str
    subject: str

class SlackNotification(BaseModel):
    type: Literal["slack"] = "slack"
    channel: str
    message: str

class WebhookNotification(BaseModel):
    type: Literal["webhook"] = "webhook"
    url: str
    payload: dict

Notification = Union[EmailNotification, SlackNotification, WebhookNotification]

class AlertConfig(BaseModel):
    notifications: list[Notification] = Field(discriminator="type")
```

## Serialization Control

```python
class User(BaseModel):
    model_config = {"from_attributes": True}

    id: str
    email: str
    password_hash: str = Field(exclude=True)   # Never in JSON
    created_at: datetime

    def model_dump_safe(self) -> dict:
        """Public-safe serialization."""
        return self.model_dump(exclude={"password_hash"})
```

## Patterns Summary

| Pattern | When |
|---------|------|
| `BaseModel` | Request/response DTOs |
| `BaseSettings` | Environment configuration |
| `field_validator` | Business rule validation |
| `Field(...)` | Constraints (min, max, pattern, ge, le) |
| `from_attributes=True` | ORM → Pydantic conversion |
| `Field(exclude=True)` | Hide sensitive fields from serialization |
| Discriminated union | Polymorphic types in config/API |

## Anti-Patterns

- ❌ Using `dict` instead of Pydantic models (no validation)
- ❌ `os.getenv()` scattered everywhere (use BaseSettings)
- ❌ V1 syntax (`class Config: orm_mode = True`) — use `model_config`
- ❌ Mutable defaults (`tags: list = []`) — use `Field(default_factory=list)`
- ❌ No `from_attributes` when mapping from ORM/dataclass
