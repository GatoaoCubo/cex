---
kind: knowledge_card
id: bld_knowledge_card_director
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for satellite_spec production — atomic searchable facts
sources: satellite-spec-builder MANIFEST.md + SCHEMA.md, microservices architecture, multi-agent systems
---

# Domain Knowledge: satellite_spec
## Executive Summary
Satellite specs define autonomous processing units in multi-agent architectures — each spec declares one satellite's domain, LLM model, MCP servers, boot sequence, constraints, and dispatch keywords. Each satellite owns ONE domain with no cross-domain responsibilities. They differ from agents (individual entities inside a satellite), boot configs (how to start a provider), patterns (abstract reusable solutions), and spawn configs (runtime launch parameters) by being the complete architectural specification of what a satellite IS and what it does.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P08 (architecture) |
| Kind | `satellite_spec` (exact literal) |
| ID pattern | `p08_sat_{slug}` |
| Required frontmatter | 24+ fields |
| Quality gates | 10 HARD + 10 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Key fields | role, model, mcps, domain, boot_sequence, dispatch_keywords |
| Scaling limit | Max 3 concurrent + orchestrator (BSOD at >4) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Single domain ownership | Each satellite owns ONE domain; no cross-domain responsibilities |
| Model-to-task matching | opus for reasoning-heavy; sonnet for speed/volume |
| MCP as tool interface | MCP servers are the satellite's external tool access |
| Ordered boot sequence | Idempotent, ordered initialization steps |
| Constraints as boundaries | Define what satellite CANNOT do, not aspirations |
| Dispatch keywords as contract | Routing contract with orchestrator; concrete nouns/verbs |
| Explicit dependencies | No hidden couplings between satellites |
| Signal-based monitoring | Signal on complete/failure enables autonomous recovery |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Cross-domain responsibilities | Violates single-domain principle; creates coupling |
| Missing boot sequence | Cannot reliably start or recover the satellite |
| No dispatch keywords | Orchestrator cannot route tasks to this satellite |
| Constraints section empty | No boundaries = scope creep inevitable |
| > 4 concurrent satellites | Resource exhaustion; system instability |
| Hidden dependencies | Undeclared coupling causes cascade failures |
| No monitoring/signal config | Cannot detect completion or failure |
## Application
1. Define satellite role and domain (ONE domain only)
2. Select LLM model matching task complexity
3. List MCP servers with config file path
4. Define ordered, idempotent boot sequence
5. Set constraints (what satellite CANNOT do)
6. Define dispatch keywords (routing contract)
7. Specify scaling limits and monitoring config
8. Document dependencies explicitly
9. Validate: 10 HARD + 10 SOFT gates, body <= 4096 bytes
## References
- satellite-spec-builder SCHEMA.md v1.0.0
- Newman, Sam. Building Microservices (2015)
- Wooldridge, Michael. Introduction to MultiAgent Systems (2009)
- Kubernetes Pod Specification (resource limits, health checks)
