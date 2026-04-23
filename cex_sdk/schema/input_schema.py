"""
cex_sdk.schema.input_schema -- Input schema validation for 8F F1 CONSTRAIN.

kind: input_schema
pillar: P06
8F: F1 CONSTRAIN (validate incoming intent/payload before processing)
"""
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from cex_sdk.schema.type_def import BaseType, FieldDef, TypeDef


@dataclass
class SchemaField(FieldDef):
    """Extended field with CEX-specific pillar/kind metadata."""
    pillar: str = ""
    kind: str = ""
    example: Any = None


@dataclass
class InputSchema:
    """
    kind: input_schema
    pillar: P06
    Validates intent payloads at F1 CONSTRAIN before the 8F pipeline runs.
    Also used as interface contract between nuclei (LLM-to-LLM handoff schema).
    """
    name: str
    fields: list[SchemaField] = field(default_factory=list)
    description: str = ""
    nucleus: str = ""
    strict: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self, payload: dict[str, Any]) -> list[str]:
        errors: list[str] = []
        field_names = {f.name for f in self.fields}

        # Unknown fields (strict mode)
        if self.strict:
            for key in payload:
                if key not in field_names:
                    errors.append(f"unknown_field: {key}")

        # Field-level validation
        for f in self.fields:
            value = payload.get(f.name, f.default)
            errors.extend(f.validate(value))

        return errors

    def is_valid(self, payload: dict[str, Any]) -> bool:
        return len(self.validate(payload)) == 0

    def to_type_def(self) -> TypeDef:
        return TypeDef(
            name=self.name,
            fields=self.fields,
            description=self.description,
        )

    def to_json_schema(self) -> dict[str, Any]:
        return self.to_type_def().to_json_schema()

    @classmethod
    def for_intent(cls, nucleus: str) -> "InputSchema":
        """Standard CEX intent input schema (F1 CONSTRAIN input)."""
        return cls(
            name=f"intent_schema_{nucleus}",
            nucleus=nucleus,
            description="Standard CEX intent payload validated at F1 CONSTRAIN",
            fields=[
                SchemaField("intent", BaseType.STRING, required=True, description="User intent text"),
                SchemaField("kind", BaseType.STRING, required=False, description="Target artifact kind"),
                SchemaField("pillar", BaseType.STRING, required=False, description="Target pillar (P01-P12)"),
                SchemaField("nucleus", BaseType.STRING, required=False, description="Target nucleus (n01-n07)"),
                SchemaField("mission", BaseType.STRING, required=False, description="Mission name"),
            ],
        )
