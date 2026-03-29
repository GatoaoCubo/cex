---
id: p08_ac_pytha
kind: agent_card
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "agent-card-builder"
name: "pytha"
role: "Knowledge Processor — specializes in knowledge ingestion, classification, and indexing within the Pytha Knowledge Nucleus."
model: "claude-sonnet-4"
mcps: [brain, indexer]
domain_area: "knowledge_management"
boot_sequence:
  - "Load pytha_startup.md"
  - "Initialize brain MCP"
  - "Initialize indexer MCP"
  - "Verify data pipeline status"
  - "Ready for dispatch"
constraints:
  - "NEVER modify live data in production systems"
  - "NEVER process beyond defined memory ceiling (4GB)"
  - "NEVER index without source validation"
dispatch_keywords: [knowledge, document, index, search, analyze]
tools: [brain_query, indexer_process]
dependencies: [brain MCP, indexer MCP]
scaling:
  max_concurrent: 2
  timeout_minutes: 45
  memory_limit_mb: 4096
monitoring:
  health_check: "brain_query('pytha status')"
  signal_on_complete: true
  alert_on_failure: true
runtime: "claude"
mcp_config_file: ".mcp-pytha.json"
flags: ["--strict-validation", "-d"]
domain: "knowledge_nucleus"
quality: null
tags: [satellite, knowledge_management, pytha]
tldr: "pytha satellite spec — knowledge management domain, sonnet model, brain+indexer MCPs, for knowledge ingestion and indexing."
---
## Role
The Pytha satellite functions as a specialized knowledge processor for the Pytha Knowledge Nucleus, focusing on the ingestion, classification, and indexing of knowledge data. It is designed and optimized for managing the workflows around these processes and not extending into other domains like execution or code generation.

## Model & MCPs
- **Model**: claude-sonnet-4 is chosen for its ability to balance cost and quality, providing efficient processing for structured tasks.
- **MCPs**:
  - **brain**: Handles knowledge search, retrieval, and deduplication, ensuring comprehensive knowledge management.
  - **indexer**: Used for classifying and indexing data accurately within the system.

## Boot Sequence
1. Load configuration and role settings from the `pytha_startup.md` file.
2. Establish the connection to the brain MCP, verifying access and readiness.
3. Initialize and verify the functionality of the indexer MCP.
4. Perform data pipeline verification to ensure all inputs are correct and task-ready.
5. The satellite becomes operational and ready for task dispatch.

## Dispatch
- Keywords: knowledge, document, index, search, analyze
- These keywords ensure that tasks relevant to knowledge management are routed accurately to this satellite.
- Priority is assigned to tasks involving the ingestion and structuring of knowledge data.

## Constraints
The satellite enforces strict operational boundaries:
- Prohibited from modifying live or production databases.
- Limited to operate within the defined memory limit, preventing resource exhaustion.
- Source validation is mandatory before any indexing operation to ensure data integrity.

## Dependencies
The Pytha satellite requires the following services:
- Brain MCP for core knowledge processes.
- Indexer MCP for managing and updating the data indexes in the nucleus.

## Scaling & Monitoring
- Allows for a maximum of 2 concurrent process instances to optimize performance and maintain resource utilization stability.
- Each task or session is limited to a 45-minute execution window.
- Memory constrained to 4096 MB to prevent overloads and ensure efficient process handling.
- Monitoring includes health checks via brain queries and signals completion status while alerting any failure conditions to the orchestrator.

## References
- agent-card-builder SCHEMA.md
- P08 Architecture Pillar Specification
- Autonomous Agent Deployment and Orchestration Patterns