---
description: "N01 Analyst scouts → N03 Builder constructs. Research first, build second."
---
Use the subagent tool with the chain parameter to execute this workflow:

1. First, use "n01-analyst" to research and gather all relevant context for: $@
2. Then, use "n03-builder" to construct the artifact using the research from the previous step (use {previous} placeholder)

Execute as a chain, passing findings between steps via {previous}.
