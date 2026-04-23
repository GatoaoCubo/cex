#!/usr/bin/env python3
# 03_multi_nucleus_crew -- Sequential crew: research -> document -> price
# Uses cex_sdk.workflow.Workflow to chain 3 CEXAgent calls.
# ASCII-only (CEX convention).

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from cex_sdk import CEXAgent, Workflow, Step
from cex_sdk.workflow.types import StepInput, StepOutput

TOPIC = "AI-powered code review tools"

# -- Step executors: each wraps a CEXAgent.build() call --

def research(inp):
    # N01 Intelligence: research the domain
    agent = CEXAgent(nucleus="n01", kind="knowledge_card")
    result = agent.build(f"Research {TOPIC}: market size, key players, trends")
    print(f"[N01] Research done. Score: {result.score}/10")
    return StepOutput(content=result.artifact, session_state={"research": result.artifact})

def document(inp):
    # N04 Knowledge: polish research into a knowledge card
    research_text = inp.session_state.get("research", "")
    agent = CEXAgent(nucleus="n04", kind="knowledge_card")
    prompt = f"Document this research as a knowledge card:\n\n{research_text[:2000]}"
    result = agent.build(prompt)
    print(f"[N04] Documentation done. Score: {result.score}/10")
    return StepOutput(content=result.artifact, session_state={"kc": result.artifact})

def price(inp):
    # N06 Commercial: create pricing tiers from the knowledge
    kc_text = inp.session_state.get("kc", "")
    agent = CEXAgent(nucleus="n06", kind="content_monetization")
    prompt = f"Create pricing tiers for a product based on:\n\n{kc_text[:2000]}"
    result = agent.build(prompt)
    print(f"[N06] Pricing done. Score: {result.score}/10")
    return StepOutput(content=result.artifact)

# -- Compose into a sequential workflow --
pipeline = Workflow(
    name="Research-to-Pricing Crew",
    steps=[
        Step(name="N01_research", executor=research),
        Step(name="N04_document", executor=document),
        Step(name="N06_price", executor=price),
    ],
)

if __name__ == "__main__":
    print(f"=== Crew: Research-to-Pricing ===")
    print(f"Topic: {TOPIC}\n")
    output = pipeline.run()
    print(f"\nWorkflow status: {output.status.value}")
    print(f"Final artifact preview:\n{(output.content or '')[:300]}")
