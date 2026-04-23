#!/usr/bin/env python3
# 01_hello_agent -- Minimal CEXAgent usage
# Runs the 8F pipeline on a single intent and prints the trace.
# ASCII-only (CEX convention).

import os
import sys

# Ensure cex_sdk is importable when running from examples/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from cex_sdk import CEXAgent

# Create an agent bound to nucleus N03 (engineering).
# Use "qwen3:14b" instead of the default claude model for local/free usage.
agent = CEXAgent(nucleus="n03", model="claude-sonnet-4-6")

# Run the 8F pipeline: F1 CONSTRAIN -> F7 GOVERN -> F8 COLLABORATE
result = agent.build("Write a knowledge card about Python decorators")

# Inspect the result
print("=== CEX Hello Agent ===")
print(f"Kind:    {result.kind}")
print(f"Pillar:  {result.pillar}")
print(f"Score:   {result.score}/10")
print(f"Passed:  {result.passed}")
print(f"Trace:   {result.trace}")
print(f"Artifact preview (first 200 chars):")
print(result.artifact[:200])
