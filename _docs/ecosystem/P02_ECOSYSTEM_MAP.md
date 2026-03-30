# P02 Model — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| CrewAI | Multi-agent orchestration | Agent (role, goal, backstory), Task, Crew, Process (sequential/hierarchical), Tool, Memory |
| AutoGen | Conversational agents | ConversableAgent, AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager, ConversationPattern |
| DSPy | Programmatic LLM | Module, Signature, Predictor, Optimizer (BootstrapFewShot, MIPRO), Metric, Teleprompter |
| Semantic Kernel | Enterprise AI | Kernel, Plugin, Function, Planner (Handlebars/Stepwise), Memory, Connector |
| Pydantic AI | Type-safe agents | Agent (system_prompt, model, tools, result_type), RunContext, ModelRetry, Tool, Dependency |
| Mastra | TypeScript agents | Agent, Tool, Workflow (step/parallel/branch), Memory, Syncs, RAG, Voice |
| Swarm (OpenAI) | Lightweight handoffs | Agent (instructions, functions), Handoff, Response, context_variables |
| Smolagents (HF) | Code-first agents | CodeAgent, ToolCallingAgent, Tool, ManagedAgent, AgentType, GradioUI |
| OpenAI Assistants | API agents | Assistant (instructions, model, tools), Thread, Run, RunStep, FileSearch, CodeInterpreter |
| Anthropic Agents | Claude agents | Agent (instructions, model, tools), Handoff, GuardrailConfig, RunResult, ToolResult |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| Agent Definition | CrewAI, AutoGen, Pydantic AI, Mastra, Swarm, Smolagents, OpenAI Assistants, Anthropic | Core entity: name + instructions + model + tools + constraints | 8 |
| Agent Role/Persona | CrewAI (role+backstory), AutoGen (system_message), Pydantic AI (system_prompt), Swarm (instructions) | Identity and behavioral framing of the agent | 7 |
| Model Config | DSPy (lm), Pydantic AI (model), Semantic Kernel (Connector), OpenAI (model param), Anthropic (model) | LLM provider + model name + params (temp, max_tokens) | 7 |
| Tool Binding | CrewAI, Pydantic AI, Mastra, Smolagents, OpenAI Assistants, Anthropic, Semantic Kernel | Which tools an agent can invoke | 7 |
| Multi-Agent Topology | CrewAI (Process), AutoGen (GroupChat), Mastra (Workflow), Swarm (Handoff), Anthropic (Handoff) | How agents are composed: sequential, parallel, hierarchical, handoff | 5 |
| Memory System | CrewAI (Memory), Mastra (Memory), Semantic Kernel (Memory), AutoGen (teachability) | Short-term, long-term, entity, episodic memory for agents | 4 |
| Guardrail/Constraint | Anthropic (GuardrailConfig), Pydantic AI (ModelRetry+result_validators), CrewAI (max_iter) | Limits and safety checks on agent behavior | 3 |
| Handoff Protocol | Swarm, Anthropic, Mastra | Transfer of control from one agent to another | 3 |
| Optimization/Tuning | DSPy (Optimizer/Teleprompter), Semantic Kernel (Planner) | Automatic prompt/parameter optimization | 2 |
| Agent Package/Export | OpenAI Assistants (API-stored), Smolagents (push_to_hub) | Portable agent definition that can be stored/shared | 2 |
| Router/Dispatcher | CrewAI (hierarchical process), AutoGen (GroupChatManager), Anthropic (Handoff routing) | Decision logic for which agent handles a task | 3 |
| Fallback Strategy | Pydantic AI (ModelRetry), DSPy (Retry module), Semantic Kernel (Planner retry) | What to do when primary model/agent fails | 3 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| agent | Agent Definition + Role/Persona | 90% | Excellent coverage. CEX agent is richer (iso_vectorstore, quality gates). Industry agents are simpler. |
| lens | (niche) | 50% | Loosely maps to DSPy "Signature" perspective or CrewAI "backstory". No direct industry match — CEX innovation. |
| boot_config | (fragmented) | 55% | Industry does model+tools binding inside Agent, not as separate config. boot_config is CEX-specific for multi-provider. |
| mental_model | Router/Dispatcher (partial) | 60% | Industry dispatchers are simpler (keyword routing). CEX mental_model adds decision trees + domain map. |
| model_card | Model Config | 85% | Well-aligned with industry model selection patterns (pricing, context, capabilities). |
| router | Router/Dispatcher | 80% | Good alignment. Industry has keyword/semantic routing. CEX router is more formal. |
| fallback_chain | Fallback Strategy | 80% | Direct match with Pydantic AI ModelRetry, DSPy retry. Well-scoped. |
| agent_package | Agent Package/Export | 70% | CEX is far richer (13 files). Industry just stores JSON/YAML config. CEX pioneered the "portable agent" concept. |
| axiom | (unique to CEX) | 30% | No industry equivalent. Closest: Anthropic's GuardrailConfig, but axioms are identity-level, not safety rules. |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| handoff_protocol | Formalized agent-to-agent transfer: trigger condition, context passed, return contract. Growing industry standard. | Swarm, Anthropic, Mastra | high |
| agent_memory_config | Memory type (short/long/entity), backend, TTL, scope. Currently implicit in CEX mental_model. Industry treats memory as explicit config. | CrewAI, Mastra, Semantic Kernel, AutoGen | med |
| multi_agent_topology | How agents compose: sequential pipeline, parallel fan-out, hierarchical delegation, debate. CEX has this in P12 workflows but not as a P02 Model kind. | CrewAI, AutoGen, Mastra, Swarm, Anthropic | low |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| lens | KEEP but clarify | Unique to CEX. Closest industry: DSPy "Signature" as perspective on data. Boundary is clear, low confusion risk. |
| axiom | REVIEW placement | Currently in P02 but naming says `p10_ax_*`. If identity-level, belongs in P02. If governance, P08. Resolve naming inconsistency. |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| agent | CrewAI Agent, Pydantic AI Agent, AutoGen ConversableAgent, Swarm Agent, OpenAI Assistant, Anthropic Agent |
| model_card | DSPy lm config, Pydantic AI model param, OpenAI model selection, Anthropic model param |
| router | CrewAI hierarchical Process, AutoGen GroupChatManager, Anthropic Handoff routing |
| fallback_chain | Pydantic AI ModelRetry, DSPy Retry, Semantic Kernel Planner retry |
| agent_package | OpenAI Assistants (stored), Smolagents push_to_hub (portable agents) |
| boot_config | Semantic Kernel Connector config, multi-provider patterns |
| mental_model | CrewAI backstory + goal, routing decision trees |
| lens | DSPy Signature perspective (loose match) |
| axiom | (CEX-unique — identity axioms) |

## 7. Summary
Current: 9 kinds → Proposed: 12 kinds (+handoff_protocol, +agent_memory_config, +multi_agent_topology) | Coverage: ~67% → ~85%

Key insight: The industry's biggest evolution since 2024 is **agent handoffs** (Swarm, Anthropic, Mastra) and **explicit memory config** (CrewAI, Mastra). CEX's agent definition is best-in-class (agent_package with 13 files is richer than any framework), but lacks formalized handoff contracts and memory configuration as standalone kinds. The axiom kind has a naming inconsistency (`p10_ax_*` prefix but lives in P02) that should be resolved.
