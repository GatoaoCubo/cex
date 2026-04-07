---
description: "N03 Builder constructs → N05 Operator reviews → N03 Builder refines. Build-review-refine cycle."
---
Use the subagent tool with the chain parameter:

1. First, use "n03-builder" to construct the artifact for: $@
2. Then, use "n05-operator" to review and validate the artifact from step 1 — report all issues with file:line precision (use {previous} placeholder)
3. Finally, use "n03-builder" to refine the artifact based on the review feedback from step 2 — fix every issue flagged (use {previous} placeholder)

Execute as a 3-step chain, passing output between steps via {previous}.
