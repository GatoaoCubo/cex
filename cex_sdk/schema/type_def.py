"""
cex_sdk.schema.type_def -- Canonical type and enum definitions.

kind: type_def
kind: enum_def
pillar: P06
8F: F1 CONSTRAIN (type resolution)
"""
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class BaseType(str, Enum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"
    NULL = "null"
    ANY = "any"


@dataclass
class FieldDef:
    """Single field in a type definition."""
    name: str
    type: BaseType | str
    required: bool = True
    default: Any = None
    description: str = ""
    constraints: dict[str, Any] = field(default_factory=dict)

    def validate(self, value: Any) -> list[str]:
        errors: list[str] = []
        if value is None:
            if self.required and self.default is None:
                errors.append(f"{self.name}: required but null")
            return errors
        if self.type == BaseType.STRING and not isinstance(value, str):
            errors.append(f"{self.name}: expected string, got {type(value).__name__}")
        elif self.type == BaseType.INTEGER and not isinstance(value, int):
            errors.append(f"{self.name}: expected integer, got {type(value).__name__}")
        elif self.type == BaseType.BOOLEAN and not isinstance(value, bool):
            errors.append(f"{self.name}: expected boolean, got {type(value).__name__}")
        elif self.type == BaseType.ARRAY and not isinstance(value, list):
            errors.append(f"{self.name}: expected array, got {type(value).__name__}")
        min_len = self.constraints.get("min_length")
        if min_len is not None and isinstance(value, (str, list)) and len(value) < min_len:
            errors.append(f"{self.name}: length {len(value)} < min {min_len}")
        max_len = self.constraints.get("max_length")
        if max_len is not None and isinstance(value, (str, list)) and len(value) > max_len:
            errors.append(f"{self.name}: length {len(value)} > max {max_len}")
        return errors


@dataclass
class TypeDef:
    """
    kind: type_def
    pillar: P06
    Typed schema definition for a CEX artifact field or API payload.
    Foundation kind -- no depends_on.
    """
    name: str
    fields: list[FieldDef] = field(default_factory=list)
    description: str = ""
    extends: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def required_fields(self) -> list[str]:
        return [f.name for f in self.fields if f.required]

    def optional_fields(self) -> list[str]:
        return [f.name for f in self.fields if not f.required]

    def to_json_schema(self) -> dict[str, Any]:
        props: dict[str, Any] = {}
        required: list[str] = []
        for f in self.fields:
            props[f.name] = {"type": f.type if isinstance(f.type, str) else f.type.value}
            if f.description:
                props[f.name]["description"] = f.description
            if f.required:
                required.append(f.name)
        schema: dict[str, Any] = {
            "type": "object",
            "title": self.name,
            "properties": props,
        }
        if required:
            schema["required"] = required
        return schema


@dataclass
class EnumDef:
    """
    kind: enum_def
    pillar: P06
    Named enumeration of allowed string values.
    """
    name: str
    values: list[str]
    description: str = ""
    default: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def is_valid(self, value: str) -> bool:
        return value in self.values

    def to_json_schema(self) -> dict[str, Any]:
        schema: dict[str, Any] = {"type": "string", "enum": self.values, "title": self.name}
        if self.description:
            schema["description"] = self.description
        if self.default:
            schema["default"] = self.default
        return schema
