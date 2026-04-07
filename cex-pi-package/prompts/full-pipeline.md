---
description: "Full CEX pipeline: N01 research → N03 build → N05 validate. Scout, construct, enforce."
---
Use the subagent tool with the chain parameter to execute the full CEX pipeline:

1. First, use "n01-analyst" to research and gather all context relevant to: $@
2. Then, use "n03-builder" to construct the artifact using the research from step 1 (use {previous} placeholder)
3. Finally, use "n05-operator" to validate the constructed artifact from step 2 — check YAML, tests, encoding, quality gates (use {previous} placeholder)

Execute as a 3-step chain, passing output between steps via {previous}.
