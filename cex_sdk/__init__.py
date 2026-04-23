"""
CEX SDK -- Runtime Layer for the CEX Typed Knowledge System.

Absorbed from Agno (https://github.com/agno-agi/agno) and adapted to CEX's
universal LLM standard: 99 kinds, 12 pillars, 8F pipeline.

Version history:
  7.0.0 -- Runtime Foundation (models, tools, guardrails, structured output)
  8.0.0 -- Knowledge Pipeline (readers, chunking, embeddings, vectordb)
  9.0.0 -- Execution Engine (workflows, memory, compression, eval, reasoning)
  10.0.0 -- Integrations (MCP, built-in tools, tracing, sessions)

License: Components absorbed under MPL-2.0 from Agno.
         CEX-specific code under project license.

Usage:
  from cex_sdk.models.providers.anthropic import Claude
  from cex_sdk.tools import Toolkit, cex_tool
  from cex_sdk.guardrails import PIIDetectionGuardrail
  from cex_sdk.workflow import Workflow, Step, Parallel
"""

__version__ = "10.2.0"
__agno_source__ = "https://github.com/agno-agi/agno"
__absorbed_date__ = "2026-04-01"
# Pillar SDK coverage: 12/12 (P01-P12, all pillars). W4 added P05+P08+P09, W4b added P06 Schema.
__pillar_coverage__ = "12/12"

from cex_sdk.agent import BuildResult, CEXAgent
# Core barrel exports for external users (repo-fork: pip install -e .)
from cex_sdk.models.chat import chat
from cex_sdk.models.providers.anthropic import Claude
from cex_sdk.schema import DataContract, InputSchema, Validator
from cex_sdk.tools import Toolkit, cex_tool
from cex_sdk.workflow import Parallel, Step, Workflow

__all__ = [
    "chat", "Claude",
    "InputSchema", "DataContract", "Validator",
    "Workflow", "Step", "Parallel",
    "Toolkit", "cex_tool",
    "CEXAgent", "BuildResult",
]
