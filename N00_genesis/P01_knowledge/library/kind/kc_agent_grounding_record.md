---
id: kc_agent_grounding_record
kind: knowledge_card
title: Agent Grounding Record
version: 1.0.0
quality: 8.5
pillar: P01
density_score: 0.92
---

# Agent Grounding Record

A structured provenance record for each inference execution, containing:

1. **Tool Calls** - Full execution history of invoked tools (including parameters)
2. **RAG Chunks** - Contextual documents used for retrieval-augmented generation
3. **Model Signature** - Exact model version and configuration used
4. **Output Hash** - Cryptographic hash of the final output artifact
5. **Traceability** - OTel/C2PA headers for end-to-end auditability

This record enables:
- Reproducibility of inference results
- Debugging of decision-making processes
- Compliance with regulatory traceability requirements
- Artifact versioning and lineage tracking

The record is automatically generated for every inference operation and stored in the `.cex/grounding` directory with a timestamp-based filename.
