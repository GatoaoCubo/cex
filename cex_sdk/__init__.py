"""
CEX SDK — Runtime Layer for the CEX Typed Knowledge System.

Absorbed from Agno (https://github.com/agno-agi/agno) and adapted to CEX's
universal LLM standard: 99 kinds, 12 pillars, 8F pipeline.

Version history:
  7.0.0 — Runtime Foundation (models, tools, guardrails, structured output)
  8.0.0 — Knowledge Pipeline (readers, chunking, embeddings, vectordb)
  9.0.0 — Execution Engine (workflows, memory, compression, eval, reasoning)
  10.0.0 — Integrations (MCP, built-in tools, tracing, sessions)

License: Components absorbed under MPL-2.0 from Agno.
         CEX-specific code under project license.

Usage:
  from cex_sdk.models.providers.anthropic import Claude
  from cex_sdk.tools import Toolkit, cex_tool
  from cex_sdk.guardrails import PIIDetectionGuardrail
  from cex_sdk.workflow import Workflow, Step, Parallel
"""

__version__ = "10.0.0"
__agno_source__ = "https://github.com/agno-agi/agno"
__absorbed_date__ = "2026-04-01"
