# P08 Architecture — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| AWS Well-Architected AI/ML | Cloud architecture | ML Lens pillars (operational excellence, security, reliability, performance, cost), MLOps maturity model, model governance, data lineage, inference patterns (real-time, batch, edge) |
| Google MLOps | ML lifecycle | ML pipeline patterns (CT/CI/CD), feature stores, model registry, experiment tracking, ML system design patterns (Level 0-2 automation) |
| NVIDIA NeMo Guardrails | Safety architecture | Dialog rails, topical rails, input/output rails, retrieval rails, execution rails, Colang flow language, action chains |
| Microsoft Semantic Kernel | AI orchestration | Plugins, planners (Handlebars, Stepwise), kernel, memory connectors, function calling, orchestration patterns |
| 12-Factor AI | Cloud-native AI | Config-driven, stateless processes, disposable, dev/prod parity, logs as streams, backing services, port binding |
| Martin Fowler / ThoughtWorks | Software architecture | Strangler fig, feature toggles, evolutionary architecture, fitness functions, ADR (Architecture Decision Records), microservices patterns |
| LLM Design Patterns | Prompt engineering | Chain-of-Thought (CoT), Tree-of-Thought (ToT), Graph-of-Thought (GoT), ReAct (Reason+Act), Reflection, Self-Consistency, Ensemble, Skeleton-of-Thought |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| Architecture Pattern | AWS (reference architectures), Google (ML system design), 12-Factor (principles), Martin Fowler (patterns catalog), LLM patterns (CoT/ToT/ReAct) | Reusable solution template for recurring design problems | 7 |
| Architecture Decision Record (ADR) | Martin Fowler (ADR), AWS (decision log), Google (design docs), Microsoft (design decisions) | Structured record of WHY a design decision was made, with context and consequences | 4 |
| Fitness Function | Martin Fowler (evolutionary architecture), AWS (Well-Architected Review), Google (ML metrics) | Automated objective function that evaluates architecture health against desired characteristics | 3 |
| Diagram / Visual | AWS (architecture diagrams), Google (system design docs), Microsoft (Semantic Kernel visualizer), Martin Fowler (C4 model) | Visual representation of system structure at varying abstraction levels | 4 |
| Component Map / Service Map | AWS (service catalog), Google (dependency graphs), Microsoft (kernel plugin registry) | Structured inventory of components and their connections | 3 |
| Orchestrator / Planner | Microsoft (Semantic Kernel planners), NVIDIA (action chains), LLM patterns (ReAct, ToT) | High-level coordinator that decomposes goals into executable steps | 3 |
| Guardrail Architecture | NVIDIA (NeMo rails), AWS (governance controls), 12-Factor (constraint patterns) | Architectural constraints that enforce safety/compliance boundaries | 3 |
| Inference Pattern | AWS (real-time/batch/edge), Google (serving patterns), LLM patterns (CoT vs parallel) | Deployment pattern for model inference (latency, throughput, cost trade-offs) | 3 |
| Operational Law / Principle | AWS (Well-Architected pillars), 12-Factor (12 principles), Martin Fowler (SOLID, DRY) | Inviolable constraint governing system behavior | 3 |
| Pipeline Pattern | Google (CT/CI/CD for ML), AWS (SageMaker Pipelines), Martin Fowler (deployment pipeline) | Multi-stage automated workflow for build/train/deploy | 3 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| pattern | Architecture Pattern | 85% | Well-aligned. CEX patterns (e.g., continuous_batching) match industry reusable-solution concept. Minor gap: no formal "forces/consequences" section like Martin Fowler patterns. |
| law | Operational Law / Principle | 80% | Strong match to AWS pillars and 12-Factor principles. CEX adds "inviolable" enforcement which is stricter than industry "best practice". Gap: no link to fitness functions that verify compliance. |
| diagram | Diagram / Visual | 90% | Excellent coverage. CEX supports ASCII and Mermaid. Gap: no explicit abstraction levels (C4: Context/Container/Component/Code). |
| component_map | Component Map / Service Map | 75% | Good structural match. Gap: industry maps include health status, version, and dependency direction (AWS service catalog). CEX is static topology only. |
| director | Orchestrator / Planner | 70% | CEX director = crew orchestrator composing builders. Maps to Semantic Kernel planners and NVIDIA action chains. Gap: no plan representation format (industry planners emit structured plans before execution). |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| decision_record | Architecture Decision Records are universal in mature engineering orgs. Records WHY a decision was made with context, options considered, and consequences. Distinct from `law` (prescriptive, inviolable) and `pattern` (reusable solution). A decision_record is descriptive — it explains a one-time choice. | Martin Fowler (ADR), AWS (decision log), Google (design docs), Microsoft (design decisions) | high |
| inference_pattern | How models are served (real-time, batch, streaming, edge, hybrid). Distinct from `pattern` (general architecture) because inference patterns carry specific latency/throughput/cost constraints and deployment configs. Critical for multi-model systems like organization. | AWS (inference endpoints), Google (Vertex AI serving), NVIDIA (Triton serving modes), LLM patterns (CoT streaming vs batch) | med |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| director | KEEP (with boundary tightening) | Valid CEX concept. Boundary should clarify: director is a P08 architectural role, NOT a P12 workflow (which defines execution steps). Director defines WHO orchestrates; workflow defines HOW steps execute. |
| diagram | KEEP (consider C4 levels) | Add optional `abstraction_level` field (context/container/component/code) to align with industry C4 standard. No rename needed. |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| pattern | AWS reference architectures, Google ML system design patterns, Martin Fowler patterns catalog, 12-Factor principles, LLM design patterns (CoT, ReAct, ToT) |
| law | AWS Well-Architected pillars, 12-Factor AI principles, Martin Fowler SOLID/DRY, NVIDIA Guardrails Colang constraints |
| diagram | AWS architecture diagrams, Google system design docs, Martin Fowler C4 model, Microsoft Semantic Kernel visualizer |
| component_map | AWS service catalog, Google dependency graphs, Microsoft kernel plugin registry |
| director | Microsoft Semantic Kernel planners, NVIDIA NeMo action chains, LLM ReAct orchestration loop |

## 7. Summary
Current: 5 kinds → Proposed: 7 kinds (+decision_record, +inference_pattern) | Coverage: ~80% → ~91%

Key insight: CEX's architecture pillar is strong on **prescriptive patterns** (pattern, law) and **visual documentation** (diagram, component_map) but lacks **decision archaeology** (why was X chosen over Y?) and **inference-specific patterns** (how models are served). Adding decision_record aligns with the industry-universal ADR practice. Adding inference_pattern captures the deployment dimension that AWS/Google/NVIDIA all treat as first-class. The existing director kind is validated but unique to CEX — its boundary with P12 workflows should be made explicit.
