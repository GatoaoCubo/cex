---
id: atom_09_autogen_ag2
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "AutoGen / AG2 Framework -- Deep Vocabulary Atlas"
version: 1.1.0
quality: 8.8
tags: [multi-agent, autogen, ag2, microsoft, orchestration, groupchat, swarm, graphflow, declarative]
date: 2026-04-13
sources:
  - https://github.com/ag2ai/ag2
  - https://docs.ag2.ai/
  - https://docs.ag2.ai/latest/docs/user-guide/advanced-concepts/orchestration/group-chat/patterns/
  - https://docs.ag2.ai/latest/docs/user-guide/advanced-concepts/orchestration/group-chat/handoffs/
  - https://docs.ag2.ai/latest/docs/user-guide/advanced-concepts/orchestration/swarm/deprecation/
  - https://docs.ag2.ai/latest/docs/blog/2025/04/28/0.9-Release-Announcement/
  - https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/graph-flow.html
  - https://learn.microsoft.com/en-us/agent-framework/agents/declarative
  - https://learn.microsoft.com/en-us/agent-framework/workflows/declarative
  - https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/
related:
  - atom_05_semantic_kernel
  - atom_03_openai_agents_sdk
  - p01_kc_agent
  - kc_llm_agent_frameworks
  - bld_knowledge_card_crew_template
  - atom_06_langchain_langgraph
  - bld_collaboration_agent
  - cex_llm_vocabulary_whitepaper
  - agent-builder
  - atom_11_agentscope
---

# AutoGen / AG2 Framework -- Deep Vocabulary Atlas

## 1. Historical Context & Fork Lineage

| Date | Event |
|------|-------|
| 2023-09 | Microsoft Research publishes AutoGen paper (Wu et al.) |
| 2023-10 | `microsoft/autogen` open-sourced, PyPI: `pyautogen` |
| 2024-11 | Chi Wang & Qingyun Wu leave Microsoft, fork to `ag2ai/ag2` |
| 2024-11 | AG2AI inherits `autogen` + `pyautogen` PyPI packages + Discord (20K+) |
| 2025-01 | Microsoft releases AutoGen 0.4 -- complete architectural redesign |
| 2025-04 | AG2 v0.9 -- unified GroupChat replaces Swarm + old GroupChat |
| 2025-10 | Microsoft Agent Framework public preview (AutoGen + Semantic Kernel merger) |
| 2026-Q1 | Microsoft Agent Framework GA planned (C#, Python, Java) |
| 2026-04 | Microsoft AutoGen v0.4 enters maintenance-only mode |

### Three Divergent Codebases (as of 2026)

| Codebase | Repo | Status | PyPI |
|----------|------|--------|------|
| **AG2** (community) | `ag2ai/ag2` | Active, heading to 1.0 | `ag2`, `autogen`, `pyautogen` |
| **Microsoft AutoGen** | `microsoft/autogen` | Maintenance (bugs/security only) | `autogen` (0.4.x) |
| **Microsoft Agent Framework** | `microsoft/agent-framework` | Active (successor) | `agent-framework` |

**Key insight**: AG2 preserves the 0.2 API (ConversableAgent-based). Microsoft's path abandoned that API entirely in 0.4 and then merged with Semantic Kernel into Agent Framework. The two communities are now fully divergent.

---

## 2. Agent Type Hierarchy

### AG2 (0.2 / 0.8 / 0.9 lineage)

```
ConversableAgent (base)
  |-- AssistantAgent       (llm_config=True, code_execution_config=False)
  |-- UserProxyAgent       (human_input_mode="ALWAYS", code_execution_config=True)
  |-- GroupChatManager     (orchestrates GroupChat speaker selection)
  |-- CompressibleAgent    (token-aware context compression)
  |-- RetrieveAssistantAgent  (RAG-augmented assistant)
  |-- RetrieveUserProxyAgent  (RAG-augmented user proxy)
  |-- GPTAssistantAgent    (wraps OpenAI Assistants API)
  |-- MultimodalConversableAgent  (image + text)
```

### Microsoft AutoGen 0.4 (event-driven)

```
RoutedAgent (low-level, message-handler based)
BaseChatAgent (high-level)
  |-- AssistantAgent       (redesigned, single-turn default)
  |-- CodeExecutorAgent    (wraps code executors)
  |-- OpenAIAssistantAgent (Assistants API wrapper)
  |-- SocietyOfMindAgent   (agent-as-team)
  |-- UserProxyAgent       (human input bridge)
```

### Microsoft Agent Framework (2025-2026 successor)

```
BaseAgent
  |-- Agent                (stateless, multi-turn by default)
  |-- FoundryAgent         (Azure AI Foundry managed agent)
  |-- Custom agents via BaseAgent subclass
```

---

## 3. ConversableAgent -- Full API

### Constructor Parameters

| Parameter | Type | Default | Purpose |
|-----------|------|---------|---------|
| `name` | str | required | Unique agent identifier |
| `system_message` | str/list | "You are a helpful AI Assistant." | LLM system prompt |
| `is_termination_msg` | callable | None | Function(msg) -> bool to end conversation |
| `max_consecutive_auto_reply` | int | class constant | Auto-reply ceiling |
| `human_input_mode` | str | "TERMINATE" | "ALWAYS" / "TERMINATE" / "NEVER" |
| `function_map` | dict | None | name -> callable mapping |
| `code_execution_config` | dict/False | False | Code executor settings |
| `llm_config` | LLMConfig/dict/False/None | None | Model configuration |
| `default_auto_reply` | str/dict | "" | Fallback reply |
| `description` | str | None | Summary for speaker selection |
| `chat_messages` | dict | None | Conversation history |
| `silent` | bool | None | Suppress output |
| `context_variables` | ContextVariables | None | Persistent state (v0.9) |
| `functions` | list/callable | None | Tools to register |
| `update_agent_state_before_reply` | list/callable | None | State hooks |
| `handoffs` | Handoffs | None | Transition conditions (v0.9) |

### Key Methods

| Category | Method | Purpose |
|----------|--------|---------|
| **Communication** | `initiate_chat(recipient, message, max_turns)` | Start conversation |
| | `initiate_chats(chat_queue)` | Multiple sequential chats |
| | `send(message, recipient)` | Send message |
| | `receive(message, sender)` | Process incoming message |
| **Reply Generation** | `generate_reply(messages, sender)` | Produce response |
| | `generate_oai_reply()` | LLM-based reply |
| | `generate_code_execution_reply()` | Code execution reply |
| | `generate_tool_calls_reply()` | Tool invocation reply |
| **Registration** | `register_reply(trigger, reply_func)` | Custom reply handler |
| | `register_for_llm(func)` | Expose function to LLM |
| | `register_for_execution(func)` | Enable function execution |
| | `register_hook(hookable, hook)` | Lifecycle hook |
| | `register_model_client(client_cls)` | Custom model client |
| | `register_handoff(conditions)` | Agent transitions (v0.9) |
| | `register_nested_chats(chat_queue, trigger)` | Nested chat workflow |
| | `register_input_guardrail(fn)` | Input validation |
| | `register_output_guardrail(fn)` | Output validation |
| **State** | `reset()` | Clear agent state |
| | `clear_history(recipient)` | Remove chat history |
| | `update_system_message(msg)` | Change system prompt |
| **Utility** | `get_human_input(prompt)` | Solicit user input |
| | `run_code(code, lang)` | Execute code block |
| | `print_usage_summary()` | Token usage stats |
| | `get_actual_usage()` / `get_total_usage()` | Programmatic usage |

### human_input_mode Values

| Value | Behavior |
|-------|----------|
| `"ALWAYS"` | Ask human every turn before auto-reply |
| `"TERMINATE"` | Ask human only when termination detected |
| `"NEVER"` | Fully autonomous, no human input |

---

## 4. GroupChat Vocabulary

### GroupChat Constructor

| Parameter | Type | Default | Purpose |
|-----------|------|---------|---------|
| `agents` | list[ConversableAgent] | required | Participants (unique names) |
| `messages` | list | [] | Shared conversation thread |
| `max_round` | int | 10 | Maximum conversation iterations |
| `speaker_selection_method` | str/callable | "auto" | How next speaker is chosen |
| `send_introductions` | bool | False | Agents introduce themselves |
| `allowed_or_disallowed_speaker_transitions` | dict | None | Agent -> [agents] transition map |
| `speaker_transitions_type` | str | "allowed" | "allowed" or "disallowed" |
| `admin_name` | str | "Admin" | Name for admin messages |
| `func_call_filter` | bool | True | Filter function-calling agents |
| `role_for_select_speaker_messages` | str | "system" | Role for selection prompts |

### GroupChatManager Constructor

| Parameter | Type | Purpose |
|-----------|------|---------|
| `groupchat` | GroupChat | The chat instance to manage |
| `llm_config` | LLMConfig | For "auto" speaker selection |
| `name` | str | Manager identifier |
| `is_termination_msg` | callable | Conversation end condition |

### Speaker Selection Methods (Legacy, pre-0.9)

| Method | Behavior |
|--------|----------|
| `"auto"` | LLM selects next speaker based on context (default) |
| `"round_robin"` | Sequential rotation through agent list |
| `"random"` | Random agent selection |
| `"manual"` | Human selects next speaker each turn |
| callable | Custom function(last_speaker, groupchat) -> agent |

### Constrained Speaker Transitions

```python
# Only allow A->B, B->C, C->A (circular)
allowed_or_disallowed_speaker_transitions = {
    agent_a: [agent_b],
    agent_b: [agent_c],
    agent_c: [agent_a],
}
speaker_transitions_type = "allowed"
```

---

## 5. AG2 v0.9 -- Unified GroupChat (NEW)

v0.9 merged Swarm + GroupChat into a single pattern. Swarm is deprecated.

### New Pattern Classes

| Pattern | Behavior |
|---------|----------|
| `AutoPattern` | LLM selects next speaker intelligently |
| `RoundRobinPattern` | Sequential rotation |
| `RandomPattern` | Random selection (excl. current speaker) |
| `ManualPattern` | Human selects next speaker |
| `DefaultPattern` | Explicit handoffs control flow |

### Transition Targets (v0.9)

| Target | Purpose |
|--------|---------|
| `AgentTarget` | Direct agent reference |
| `AgentNameTarget` | Agent by name string |
| `RevertToUserTarget` | Return control to user |
| `TerminateTarget` | End conversation |
| `StayTarget` | Current agent continues |
| `RandomAgentTarget` | Random next agent |
| `AskUserTarget` | Request human decision |
| `NestedChatTarget` | Enter nested chat |
| `GroupChatTarget` | Enter sub-group-chat |
| `GroupManagerTarget` | Delegate to manager |

### Handoff Conditions (v0.9)

| Condition | Purpose |
|-----------|---------|
| `StringLLMCondition` | LLM evaluates string condition |
| `ExpressionContextCondition` | Evaluate context variable expression |
| `OnCondition` | Explicit trigger-based handoff |
| `OnContextCondition` | Context-variable-based handoff |

### ContextVariables (v0.9)

Structured state management replacing raw dict passing. Persists across agents within a GroupChat session.

### ReplyResult (v0.9)

Function return type containing: message, target agent, updated context variables.

---

## 6. Conversation Patterns (Orchestration)

### Two-Agent Chat

Simplest pattern. One `initiate_chat()` call between two agents.

```python
result = agent_a.initiate_chat(
    agent_b,
    message="Hello",
    max_turns=5
)
```

**Key params**: `message`, `max_turns`, `summary_method`, `clear_history`

### Sequential Chat

Chained two-agent conversations with carryover.

```python
results = agent_a.initiate_chats([
    {"recipient": agent_b, "message": "Task 1", "max_turns": 3,
     "summary_method": "reflection_with_llm"},
    {"recipient": agent_c, "message": "Task 2", "max_turns": 3,
     "carryover": "auto"},  # carries summary from chat 1
])
```

**Key params**: `carryover` (str/list/"auto"), `summary_method` ("last_msg" / "reflection_with_llm"), `summary_prompt`

### Nested Chat

Package a multi-step workflow as a single agent's reply handler.

```python
agent.register_nested_chats(
    chat_queue=[
        {"recipient": reviewer, "message": reflect_msg, "max_turns": 1},
        {"recipient": editor, "max_turns": 1}
    ],
    trigger=writer  # activates when writer sends message
)
```

### Swarm (DEPRECATED in v0.9)

```python
from autogen import initiate_swarm_chat, AfterWorkOption

chat_result, context, last_agent = initiate_swarm_chat(
    initial_agent=triage_agent,
    agents=[triage_agent, specialist_a, specialist_b],
    user_agent=user_proxy,
    messages="Help me with X",
    swarm_manager_args={"llm_config": config},
    after_work=AfterWorkOption.SWARM_MANAGER
)
```

**Key vocab**: `initiate_swarm_chat`, `SwarmAgent`, `ON_CONDITION`, `AFTER_WORK`, `AfterWorkOption` (TERMINATE, REVERT_TO_USER, STAY, SWARM_MANAGER), `SwarmResult`, `context_variables`, `register_hand_off`

---

## 7. Code Execution Vocabulary

### Executor Classes

| Class | Isolation | State | Use Case |
|-------|-----------|-------|----------|
| `LocalCommandLineCodeExecutor` | None (host) | Stateless | Dev/prototyping |
| `DockerCommandLineCodeExecutor` | Docker container | Stateless | Production |
| `JupyterCodeExecutor` | Jupyter kernel | **Stateful** | Data science workflows |

### code_execution_config Parameters

| Parameter | Type | Purpose |
|-----------|------|---------|
| `executor` | CodeExecutor | Which executor class to use |
| `work_dir` | str | Directory for code files |
| `use_docker` | bool/str | Docker image or False |
| `timeout` | int | Execution timeout (seconds) |
| `last_n_messages` | int | How many messages to scan for code |

### Supported Languages

Python, Bash/Shell/Sh, PowerShell (pwsh, ps1), HTML, CSS, JavaScript

### Code Execution Flow

```
AssistantAgent generates code block
  -> UserProxyAgent detects code fence
  -> Executor writes to work_dir
  -> Executor runs subprocess / Docker / Jupyter
  -> CodeResult returned (exit_code, output)
  -> UserProxyAgent sends result back to AssistantAgent
  -> Loop until termination or max_turns
```

### Key Types

| Type | Purpose |
|------|---------|
| `CodeBlock` | Parsed code with language + content |
| `CodeResult` | Execution result: exit_code + output |
| `CodeExecutor` | Base class for all executors |

---

## 8. LLM Configuration Vocabulary

### LLMConfig (AG2)

```python
llm_config = LLMConfig(
    api_type="openai",        # "openai", "azure", "anthropic", etc.
    model="gpt-4",
    api_key="sk-...",
    temperature=0.7,
    max_tokens=4096,
    seed=42,                  # reproducibility
    cache_seed=None,          # disable caching
    config_list=[...],        # multiple model configs for fallback
)
```

### config_list Pattern (Legacy)

```python
config_list = [
    {"model": "gpt-4", "api_key": "key1"},
    {"model": "gpt-3.5-turbo", "api_key": "key2"},  # fallback
]
llm_config = {"config_list": config_list, "temperature": 0}
```

### Model Client Classes (AutoGen 0.4)

| Class | Provider |
|-------|----------|
| `OpenAIChatCompletionClient` | OpenAI |
| `AzureOpenAIChatCompletionClient` | Azure OpenAI |
| `AzureAIChatCompletionClient` | Azure AI |
| `AnthropicChatCompletionClient` | Anthropic |
| `OllamaChatCompletionClient` | Ollama (local) |
| `ChatCompletionCache` | Caching wrapper |

---

## 9. Tool Integration Vocabulary

| Concept | AG2 (0.2/0.8) | AutoGen 0.4 | Agent Framework |
|---------|----------------|-------------|-----------------|
| Define tool | `register_for_llm` + `register_for_execution` | `FunctionTool(func)` | `@tool` decorator |
| Caller agent | Sets `llm_config` | `AssistantAgent(tools=[...])` | `Agent(tools=[...])` |
| Executor agent | Sets `code_execution_config` | `CodeExecutorAgent` | Built-in (multi-turn) |
| Agent-as-tool | N/A | `AgentTool(agent=)` | `agent.as_tool()` |
| MCP integration | Limited | Extension-based | `MCPStdioTool`, `MCPStreamableHTTPTool`, `MCPWebsocketTool` |
| Hosted tools | N/A | N/A | `client.get_code_interpreter_tool()`, `client.get_web_search_tool()` |

---

## 10. Multi-Agent Orchestration (AutoGen 0.4 / Agent Framework)

### AutoGen 0.4 Teams

| Class | Pattern |
|-------|---------|
| `RoundRobinGroupChat` | Sequential rotation |
| `SelectorGroupChat` | LLM-based selection |
| `MagenticOneGroupChat` | Microsoft's Magentic-One pattern |
| `Swarm` | Handoff-based routing |
| `GraphFlow` | DAG-based control flow |

### AutoGen 0.4 Key Types

| Type | Purpose |
|------|---------|
| `Team` | Base class for multi-agent groups |
| `RoutedAgent` | Low-level event-driven agent |
| `DiGraphBuilder` | Build directed graphs for GraphFlow |
| `StopAfterNMessages` | Termination condition |
| `TextMessage` | Standard text message |
| `StopMessage` | Termination signal message |
| `TaskResult` | Final result from team.run() |
| `ModelClientStreamingChunkEvent` | Streaming event |

### Agent Framework Workflow

| Concept | Class/Decorator | Purpose |
|---------|-----------------|---------|
| Workflow builder | `WorkflowBuilder` | Compose executor graph |
| Executor | `@executor(id="...")` | Node in workflow graph |
| Context | `WorkflowContext` | Send messages, yield output |
| Session | `AgentSession` | Persist state across turns |
| Middleware | `AgentContext`, `FunctionInvocationContext` | Cross-cutting concerns |

### Flow Paradigm Comparison

| Aspect | AG2 GroupChat | AutoGen 0.4 GraphFlow | Agent Framework Workflow |
|--------|---------------|----------------------|--------------------------|
| Flow type | Broadcast | Control flow (transitions) | Data flow (typed edges) |
| Node types | Agents only | Agents only | Agents + functions + sub-workflows |
| State | Shared messages | Broadcast messages | Edge-routed typed data |
| Join | N/A | `activation_group` + `activation_condition` | Executor-level logic |
| Routing | Speaker selection | Conditional edges | `target_id` explicit routing |

---

## 11. Termination Vocabulary

| Mechanism | Where | Example |
|-----------|-------|---------|
| `is_termination_msg` | ConversableAgent / GroupChatManager | `lambda msg: "DONE" in msg["content"]` |
| `max_turns` | `initiate_chat()` | `max_turns=5` |
| `max_round` | GroupChat | `max_round=12` |
| `max_consecutive_auto_reply` | ConversableAgent | Limit auto-replies before asking human |
| `StopAfterNMessages(n)` | AutoGen 0.4 Team | Terminate after n messages |
| `TerminateTarget` | AG2 v0.9 | Handoff target that ends chat |

---

## 12. Mapping to CEX Pillars

| AG2/AutoGen Concept | CEX Pillar | CEX Kind | Notes |
|---------------------|------------|----------|-------|
| ConversableAgent | P02 Model | `agent` | Base agent definition |
| AssistantAgent | P02 Model | `agent` | LLM-backed agent variant |
| UserProxyAgent | P02 Model | `agent` | Human-in-loop agent |
| system_message | P03 Prompt | `system_prompt` | Agent instructions |
| GroupChat | P12 Orchestration | `workflow` | Multi-agent coordination |
| GroupChatManager | P12 Orchestration | `workflow` | Speaker selection orchestrator |
| speaker_selection_method | P12 Orchestration | `dispatch_rule` | Routing strategy |
| NestedChat | P12 Orchestration | `workflow` | Sub-workflow pattern |
| sequential_chat | P12 Orchestration | `workflow` | Chained conversations |
| Swarm / handoff | P12 Orchestration | `workflow` | Agent transfer pattern |
| code_execution_config | P04 Tools | `cli_tool` | Code executor config |
| LocalCommandLineCodeExecutor | P04 Tools | `cli_tool` | Local execution |
| DockerCommandLineCodeExecutor | P04 Tools | `cli_tool` | Container execution |
| JupyterCodeExecutor | P04 Tools | `cli_tool` | Stateful notebook execution |
| register_for_llm / FunctionTool | P04 Tools | `api_client` | Tool definition |
| llm_config / config_list | P09 Config | `env_config` | Model routing |
| is_termination_msg | P11 Feedback | `guardrail` | Conversation boundary |
| description (for selection) | P08 Architecture | `agent_card` | Agent capability summary |
| context_variables | P10 Memory | `entity_memory` | Persistent state |
| summary_method | P10 Memory | `memory_summary` | Chat summarization |
| register_hook | P11 Feedback | `quality_gate` | Lifecycle interceptor |
| register_input_guardrail | P11 Feedback | `guardrail` | Input validation |
| register_output_guardrail | P11 Feedback | `guardrail` | Output validation |
| Agent Framework Workflow | P12 Orchestration | `workflow` | Data-flow graph |
| Agent Framework @tool | P04 Tools | `cli_tool` | Declarative tool definition |
| Agent Framework Middleware | P11 Feedback | `guardrail` | Cross-cutting concerns |
| AgentSession | P10 Memory | `memory_scope` | Conversation state |

---

## 13. Package & Installation Reference

```bash
# AG2 (community fork)
pip install ag2[openai]          # Core + OpenAI
pip install ag2[anthropic]       # + Anthropic
pip install ag2[jupyter]         # + Jupyter executor
pip install ag2[docker]          # + Docker executor
pip install ag2[websockets]      # + WebSocket support

# Microsoft AutoGen 0.4 (maintenance)
pip install autogen-agentchat    # High-level
pip install autogen-core         # Low-level
pip install autogen-ext          # Extensions

# Microsoft Agent Framework (successor)
pip install agent-framework
```

- Python requirement: >= 3.10, < 3.14
- AG2 repo: github.com/ag2ai/ag2 (4.4K stars, Apache 2.0)
- Microsoft repo: github.com/microsoft/autogen (maintenance)
- Agent Framework: github.com/microsoft/agent-framework

---

## 14. Key Architectural Differences Summary

| Dimension | AG2 (community) | MS AutoGen 0.4 | MS Agent Framework |
|-----------|-----------------|-----------------|---------------------|
| API style | ConversableAgent (0.2 compat) | Event-driven + Team | Stateless Agent + Workflow |
| State | Agent holds history | Agent holds history | Stateless; AgentSession opt-in |
| Orchestration | GroupChat (unified v0.9) | Team + GraphFlow | WorkflowBuilder (data-flow DAG) |
| Tool iteration | Manual (caller/executor split) | `max_tool_iterations` | Auto until completion |
| MCP | Basic | Extension-based | First-class (Stdio, HTTP, WS) |
| Code execution | 3 executors (local/Docker/Jupyter) | Same 3 executors | Hosted code interpreter (cloud) |
| Governance | Community (AG2AI) | Microsoft (maintenance) | Microsoft (active, Semantic Kernel team) |
| Target | 1.0 release | End of life | GA Q1 2026 |

---

## 15. AG2 v0.9 Pattern Classes -- Full API

All patterns live in `autogen.agentchat.group.patterns`. Every pattern shares the same
base constructor; behavior differs only in next-speaker selection logic.

### Common Constructor Signature

```python
Pattern(
    initial_agent: ConversableAgent,             # First agent to speak
    agents: list[ConversableAgent],              # All participants
    user_agent: ConversableAgent | None,         # Human-in-loop agent (optional)
    group_manager_args: dict | None,             # Passed to internal GroupChatManager
    context_variables: ContextVariables | None,  # Shared state
    after_work: TransitionTarget | None,         # Default post-turn behavior
)
```

### Pattern Decision Matrix

| Pattern | Next-speaker selection | Handoffs respected? | Human input? | Use when |
|---------|----------------------|---------------------|--------------|----------|
| `AutoPattern` | LLM reads conversation + agent descriptions | Yes (override) | Optional | Dynamic routing, customer service |
| `RoundRobinPattern` | Fixed index rotation through `agents` list | Yes (override) | Optional | Turn-taking, brainstorming |
| `RandomPattern` | Uniform random, excludes current speaker | Yes (override) | Optional | Diverse viewpoints, creative tasks |
| `ManualPattern` | Always reverts to `user_agent` for selection | N/A (user decides) | Required | Debugging, demos, education |
| `DefaultPattern` | Purely handoff-driven; no fallback LLM | Required | Optional | Compliance, approval chains |

### AutoPattern -- Full Example

```python
from autogen import ConversableAgent, LLMConfig
from autogen.agentchat import initiate_group_chat
from autogen.agentchat.group.patterns import AutoPattern
from autogen.agentchat.group import (
    AgentTarget, RevertToUserTarget,
    OnCondition, StringLLMCondition, ContextVariables
)

llm_config = LLMConfig(api_type="openai", model="gpt-4o", temperature=0)

triage = ConversableAgent("triage", system_message="Route queries.", llm_config=llm_config)
billing = ConversableAgent("billing", system_message="Handle billing.", llm_config=llm_config)
tech = ConversableAgent("tech", system_message="Handle technical issues.", llm_config=llm_config)
user = ConversableAgent("user", human_input_mode="ALWAYS")

triage.handoffs.add_llm_conditions([
    OnCondition(target=AgentTarget(billing),
                condition=StringLLMCondition(prompt="Issue is billing-related")),
    OnCondition(target=AgentTarget(tech),
                condition=StringLLMCondition(prompt="Issue is technical")),
])
triage.handoffs.set_after_work(RevertToUserTarget())

pattern = AutoPattern(
    initial_agent=triage,
    agents=[triage, billing, tech],
    user_agent=user,
    group_manager_args={"llm_config": llm_config},
)

result, context, last_agent = initiate_group_chat(
    pattern=pattern,
    messages="My invoice is wrong.",
    max_rounds=10,
)
```

### DefaultPattern -- Full Example (handoff-only, no LLM fallback)

```python
from autogen.agentchat.group.patterns import DefaultPattern
from autogen.agentchat.group import TerminateTarget

writer.handoffs.add_llm_conditions([
    OnCondition(target=AgentTarget(reviewer),
                condition=StringLLMCondition(prompt="Draft is ready for review")),
])
writer.handoffs.set_after_work(TerminateTarget())

reviewer.handoffs.add_llm_conditions([
    OnCondition(target=AgentTarget(writer),
                condition=StringLLMCondition(prompt="Needs revision")),
])
reviewer.handoffs.set_after_work(TerminateTarget())

pattern = DefaultPattern(
    initial_agent=writer,
    agents=[writer, reviewer],
    user_agent=None,
)
result, context, last = initiate_group_chat(pattern=pattern, messages="Write a blog post", max_rounds=20)
```

### Required Imports (v0.9+)

```python
from autogen.agentchat import initiate_group_chat
from autogen.agentchat.group.patterns import (
    AutoPattern, RoundRobinPattern, RandomPattern, ManualPattern, DefaultPattern
)
from autogen.agentchat.group import (
    AgentTarget, AgentNameTarget, FunctionTarget,
    AskUserTarget, NestedChatTarget, GroupManagerTarget,
    RandomAgentTarget, RevertToUserTarget, StayTarget, TerminateTarget,
    OnCondition, OnContextCondition,
    StringLLMCondition, ExpressionContextCondition, StringAvailableCondition,
    ContextVariables, ContextExpression,
    ReplyResult, FunctionTargetResult,
)
```

### FunctionTarget Pattern (custom routing logic)

```python
from autogen.agentchat.group import FunctionTarget, FunctionTargetResult

def route_by_score(output: str, context_variables: ContextVariables) -> FunctionTargetResult:
    score = context_variables["quality_score"]
    if score >= 8:
        return FunctionTargetResult(message="Approved", target=AgentTarget(publisher))
    return FunctionTargetResult(message="Needs revision", target=AgentTarget(editor))

agent.handoffs.set_after_work(FunctionTarget(func=route_by_score))
```

---

## 16. GraphFlow API -- AutoGen 0.4 (DiGraphBuilder)

GraphFlow enables DAG-based (and cyclic) control flow between agents.
Status: **experimental** -- API subject to change before stable.
Package: `autogen_agentchat.teams.GraphFlow` + `autogen_agentchat.teams._graph_flow.DiGraphBuilder`

### DiGraphBuilder Method Reference

| Method | Signature | Returns | Purpose |
|--------|-----------|---------|---------|
| `add_node` | `add_node(agent)` | `self` | Register agent as graph node |
| `add_edge` | `add_edge(src, dst, condition=None, activation_group=None, activation_condition="all")` | `self` | Define directed edge |
| `set_entry_point` | `set_entry_point(agent)` | `self` | Force start node (required for cyclic graphs) |
| `build` | `build()` | `DiGraph` | Validate and produce graph |
| `get_participants` | `get_participants()` | `list[Agent]` | Return all registered agents |

### `add_edge` Parameters

| Parameter | Type | Default | Purpose |
|-----------|------|---------|---------|
| `source` | `BaseChatAgent` | required | Source node |
| `target` | `BaseChatAgent` | required | Destination node |
| `condition` | `callable(msg) -> bool` | `None` | Edge fires only if True |
| `activation_group` | `str` | `None` | Fan-in coordination label |
| `activation_condition` | `"all"` or `"any"` | `"all"` | Gate: wait for all or any grouped input |

### Pattern: Sequential

```python
from autogen_agentchat.teams import GraphFlow
from autogen_agentchat.teams._graph_flow import DiGraphBuilder

builder = DiGraphBuilder()
builder.add_node(writer).add_node(reviewer).add_node(publisher)
builder.add_edge(writer, reviewer)
builder.add_edge(reviewer, publisher)
flow = GraphFlow(participants=builder.get_participants(), graph=builder.build())
await flow.run(task="Write an article about AI")
```

### Pattern: Fan-Out (Parallel)

```python
builder = DiGraphBuilder()
builder.add_node(coordinator).add_node(editor_a).add_node(editor_b)
builder.add_edge(coordinator, editor_a)
builder.add_edge(coordinator, editor_b)
flow = GraphFlow(participants=builder.get_participants(), graph=builder.build())
```

### Pattern: Fan-In (Convergence)

```python
builder = DiGraphBuilder()
builder.add_node(editor_a).add_node(editor_b).add_node(final_reviewer)
builder.add_edge(editor_a, final_reviewer, activation_group="reviews", activation_condition="all")
builder.add_edge(editor_b, final_reviewer, activation_group="reviews", activation_condition="all")
flow = GraphFlow(participants=builder.get_participants(), graph=builder.build())
```

### Pattern: Conditional Loop (Retry until approved)

```python
builder = DiGraphBuilder()
builder.add_node(generator).add_node(reviewer).add_node(publisher)
builder.set_entry_point(generator)
builder.add_edge(generator, reviewer)
# Loop back if NOT approved
builder.add_edge(reviewer, generator,
                 condition=lambda msg: "APPROVE" not in msg.to_model_text())
# Exit to publisher if approved
builder.add_edge(reviewer, publisher,
                 condition=lambda msg: "APPROVE" in msg.to_model_text())
flow = GraphFlow(participants=builder.get_participants(), graph=builder.build())
```

### Pattern: Diamond (Fan-Out + Fan-In)

```python
builder = DiGraphBuilder()
builder.add_node(planner).add_node(researcher).add_node(writer).add_node(summarizer)
builder.add_edge(planner, researcher)
builder.add_edge(planner, writer)
builder.add_edge(researcher, summarizer, activation_group="inputs", activation_condition="all")
builder.add_edge(writer, summarizer, activation_group="inputs", activation_condition="all")
flow = GraphFlow(participants=builder.get_participants(), graph=builder.build())
```

### Execution Semantics

| Concept | Behavior |
|---------|----------|
| Source nodes | Nodes with no incoming edges execute first automatically |
| `activation_group` | Tags edges pointing to same target for coordination |
| `activation_condition="all"` | Target waits until ALL grouped edges have fired |
| `activation_condition="any"` | Target fires on FIRST grouped edge |
| Termination | Flow ends when no pending executable nodes remain |
| Cyclic graphs | Require `set_entry_point()` to avoid ambiguous start detection |

### Known Limitations (AutoGen 0.4 stable)

- Callable conditions not serialized in `dump_component()` (no YAML round-trip)
- First-node double-call in some conditional configs (issue #6716)
- Experimental: breaking changes expected before v1.0

---

## 17. Microsoft Agent Framework -- Declarative YAML Spec (GA April 2026)

Agent Framework 1.0 (GA April 2026) supports YAML/JSON definitions for agents and workflows.
Sources: `learn.microsoft.com/en-us/agent-framework/agents/declarative`
         `learn.microsoft.com/en-us/agent-framework/workflows/declarative`

### Declarative Agent Schema (Python)

```yaml
kind: Prompt                              # required; "Prompt" for LLM-backed agents
name: DiagnosticAgent                     # required; unique identifier
displayName: Diagnostic Assistant         # optional; human-readable label
description: Performs system diagnostics  # optional; used in multi-agent routing
instructions: You are a diagnostic...     # required; system prompt

model:
  id: =Env.AZURE_OPENAI_MODEL             # =Env.VAR_NAME resolves env vars at runtime
  connection:
    kind: remote                          # "remote" = Azure Foundry, "local" = local LLM
    endpoint: =Env.FOUNDRY_PROJECT_ENDPOINT
  options:                                # LLM sampling parameters
    temperature: 0.9
    topP: 0.95

outputSchema:                             # optional; enforces structured JSON output
  properties:
    language:
      type: string
      required: true
      description: Language of the answer
    answer:
      type: string
      required: true
      description: The answer text
```

### Loading a Declarative Agent (Python)

```python
import asyncio
from agent_framework.declarative import AgentFactory
from azure.identity.aio import AzureCliCredential

async def main():
    yaml_str = open("agent-config.yaml").read()
    async with (
        AzureCliCredential() as credential,
        AgentFactory(client_kwargs={"credential": credential})
            .create_agent_from_yaml(yaml_str) as agent,
    ):
        response = await agent.run("Check system health")
        print(response.text)

asyncio.run(main())
```

### Declarative Workflow Schema (Python)

```yaml
name: my-workflow                         # required; unique identifier
description: What this workflow does      # optional

inputs:                                   # optional; typed parameters
  userQuery:
    type: string
    description: User query text

actions:                                  # required; sequential action list
  - kind: SetVariable
    id: capture_input
    variable: Local.query
    value: =inputs.userQuery

  - kind: InvokeAzureAgent
    id: call_agent
    agentId: DiagnosticAgent
    input: =Local.query

  - kind: If
    id: check_severity
    condition: =Local.severity >= 8
    actions:
      - kind: InvokeAzureAgent
        id: escalate
        agentId: EscalationAgent
        input: "Critical issue detected"

  - kind: SendActivity
    id: respond
    activity: =Local.result

  - kind: EndWorkflow
    id: done
```

### Declarative Workflow Action Types

| Category | Action | Python | C# | Purpose |
|----------|--------|--------|-----|---------|
| Variables | `SetVariable` | Yes | Yes | Set a single variable |
| Variables | `SetMultipleVariables` | Yes | Yes | Batch variable assignment |
| Variables | `ResetVariable` | Yes | Yes | Clear a variable |
| Variables | `AppendValue` | Yes | No | Append to list variable |
| Control | `If` | Yes | Yes | Conditional branching |
| Control | `ConditionGroup` | Yes | Yes | Multi-branch switch |
| Control | `Foreach` | Yes | Yes | Iterate over collection |
| Control | `BreakLoop` | Yes | Yes | Exit current loop |
| Control | `GotoAction` | Yes | Yes | Jump to named action |
| Control | `RepeatUntil` | Yes | No | Loop until condition |
| Output | `SendActivity` | Yes | Yes | Send message to user |
| Output | `EmitEvent` | Yes | No | Emit workflow event |
| Agent | `InvokeAzureAgent` | Yes | Yes | Call a deployed agent |
| Tool | `InvokeFunctionTool` | Yes | Yes | Call a function tool |
| Tool | `InvokeMcpTool` | No | Yes | Call an MCP tool |
| Human | `Question` | Yes | Yes | Ask user a question |
| Human | `WaitForInput` | Yes | No | Block until input received |
| Workflow | `EndWorkflow` | Yes | Yes | Terminate workflow |
| Workflow | `EndConversation` | Yes | Yes | End the conversation |

### Loading a Declarative Workflow (Python)

```python
from agent_framework.declarative import WorkflowFactory
from azure.identity import AzureCliCredential

factory = WorkflowFactory(client_kwargs={"credential": AzureCliCredential()})
workflow = await factory.create_workflow_from_yaml_path("my-workflow.yaml")
result = await workflow.run(inputs={"userQuery": "Check system health"})
```

---

## 18. Termination Mechanisms -- Complete Reference with Examples

### AG2 Termination (0.2 / 0.8 / 0.9)

#### 1. `is_termination_msg` -- Agent-level, per-message

```python
agent = ConversableAgent(
    "agent",
    is_termination_msg=lambda msg: "DONE" in msg.get("content", ""),
    llm_config=llm_config,
)
```

#### 2. `max_turns` -- Two-agent chat ceiling

```python
result = agent_a.initiate_chat(agent_b, message="Start", max_turns=5)
```

#### 3. `max_round` -- GroupChat ceiling

```python
groupchat = GroupChat(agents=[a, b, c], messages=[], max_round=12)
```

#### 4. `max_consecutive_auto_reply` -- Human-gating

```python
# After 3 consecutive auto-replies, agent requests human input
agent = ConversableAgent("agent", max_consecutive_auto_reply=3)
```

#### 5. `TerminateTarget` -- v0.9 handoff-driven

```python
from autogen.agentchat.group import TerminateTarget, OnCondition, StringLLMCondition

agent.handoffs.add_llm_conditions([
    OnCondition(
        target=TerminateTarget(),
        condition=StringLLMCondition(prompt="Task is fully complete and verified")
    )
])
agent.handoffs.set_after_work(TerminateTarget())  # fallback: terminate if no condition matches
```

#### 6. `ExpressionContextCondition` -- context-variable-driven

```python
from autogen.agentchat.group import OnContextCondition, ExpressionContextCondition, ContextExpression

agent.handoffs.add_context_conditions([
    OnContextCondition(
        target=TerminateTarget(),
        condition=ExpressionContextCondition(
            expression=ContextExpression("${task_complete} == True")
        )
    )
])
```

### AutoGen 0.4 Team Termination

#### 7. `StopAfterNMessages(n)`

```python
from autogen_agentchat.conditions import StopAfterNMessages
team = RoundRobinGroupChat(participants=[a, b], termination_condition=StopAfterNMessages(10))
```

#### 8. `TextMentionTermination`

```python
from autogen_agentchat.conditions import TextMentionTermination
team = SelectorGroupChat(
    participants=[a, b],
    model_client=model,
    termination_condition=TextMentionTermination("TERMINATE"),
)
```

#### 9. `MaxMessageTermination`

```python
from autogen_agentchat.conditions import MaxMessageTermination
termination = MaxMessageTermination(max_messages=20)
```

#### 10. Composing Conditions (OR / AND)

```python
# Either condition fires -> stop
termination = TextMentionTermination("DONE") | MaxMessageTermination(50)

# Both conditions required -> stop
termination = StopAfterNMessages(5) & TextMentionTermination("DONE")
```

### Termination Mechanism Matrix

| Mechanism | Framework | Level | Trigger | Recommended for |
|-----------|-----------|-------|---------|-----------------|
| `is_termination_msg` | AG2 | Agent | Content check | Content-based stopping |
| `max_turns` | AG2 | Chat | Hard limit | Safety fallback |
| `max_round` | AG2 | GroupChat | Hard limit | Safety fallback |
| `max_consecutive_auto_reply` | AG2 | Agent | Count | Human-in-loop gating |
| `TerminateTarget` | AG2 v0.9 | Handoff | Explicit routing | Workflow-driven stopping |
| `ExpressionContextCondition` | AG2 v0.9 | Context var | State value | Data-driven stopping |
| `StopAfterNMessages` | AutoGen 0.4 | Team | Count | Simple caps |
| `TextMentionTermination` | AutoGen 0.4 | Team | Content | Signal-word stopping |
| `MaxMessageTermination` | AutoGen 0.4 | Team | Count | Hard safety limit |
| `\|` (OR compose) | AutoGen 0.4 | Team | Either fires | Flexible multi-condition |
| `&` (AND compose) | AutoGen 0.4 | Team | Both fire | Strict compound gate |

---

## 19. Swarm Deprecation -- Full Migration Path (v0.8 -> v0.9)

Status: Swarm classes functional in v0.9 but deprecated. No removal date set.
Source: `docs.ag2.ai/latest/docs/user-guide/advanced-concepts/orchestration/swarm/deprecation/`

### Deprecated Classes and Replacements

| Deprecated | Replacement |
|-----------|-------------|
| `SwarmAgent` | `ConversableAgent` with `.handoffs` |
| `SwarmResult` | `ReplyResult` |
| `initiate_swarm_chat` | `initiate_group_chat` + Pattern |
| `register_hand_off` | `agent.handoffs.add_llm_conditions()` |
| `OnCondition` (swarm import) | `OnCondition` from `autogen.agentchat.group` |
| `OnContextCondition` (swarm) | `OnContextCondition` from `autogen.agentchat.group` |
| `AfterWork` / `AfterWorkOption` | `agent.handoffs.set_after_work(Target())` |
| `context_variables: dict[str, Any]` | `context_variables: ContextVariables` |

### Option A: Quick Fix (Keep Swarm Code Running)

```python
# BEFORE (v0.8)
from autogen import initiate_swarm_chat, AfterWorkOption, OnCondition, SwarmAgent, SwarmResult

# AFTER (v0.9 compat shim -- deprecated but still runs)
from autogen.agentchat.contrib.swarm_agent import (
    AfterWork, AfterWorkOption, initiate_swarm_chat,
    OnCondition, OnContextCondition, register_hand_off,
    SwarmAgent, SwarmResult
)
from autogen.agentchat.group import ContextVariables

# ContextVariables: was dict, now a class
my_ctx = ContextVariables(data={"confidence": 0, "task_complete": False})
```

### Option B: Full Migration to v0.9 GroupChat

#### Step 1: Replace `SwarmResult` with `ReplyResult`

```python
# BEFORE
def my_tool(param: str, context_variables: dict) -> SwarmResult:
    context_variables["done"] = True
    return SwarmResult(agent=next_agent, context_variables=context_variables, values="Done")

# AFTER
from autogen.agentchat.group import ReplyResult, AgentTarget, ContextVariables

def my_tool(param: str, context_variables: ContextVariables) -> ReplyResult:
    context_variables["done"] = True
    return ReplyResult(target=AgentTarget(next_agent), context_variables=context_variables, message="Done")
```

#### Step 2: Replace `register_hand_off` with `agent.handoffs`

```python
# BEFORE
register_hand_off(
    agent=triage_agent,
    hand_to=[
        ON_CONDITION(billing_agent, "Issue is billing related"),
        AfterWork(AfterWorkOption.REVERT_TO_USER),
    ]
)

# AFTER
from autogen.agentchat.group import (
    OnCondition, AgentTarget, StringLLMCondition,
    StringAvailableCondition, RevertToUserTarget
)

triage_agent.handoffs.add_llm_conditions([
    OnCondition(
        target=AgentTarget(billing_agent),
        condition=StringLLMCondition(prompt="Issue is billing related"),
    ),
])
triage_agent.handoffs.set_after_work(RevertToUserTarget())
```

#### Step 3: Replace `initiate_swarm_chat` with Pattern + `initiate_group_chat`

```python
# BEFORE
chat_result, context, last_agent = initiate_swarm_chat(
    initial_agent=triage_agent,
    agents=[triage_agent, billing_agent, tech_agent],
    user_agent=user_proxy,
    messages="Help me",
    after_work=AfterWorkOption.SWARM_MANAGER,
    context_variables={"confidence": 0},
)

# AFTER
from autogen.agentchat import initiate_group_chat
from autogen.agentchat.group.patterns import DefaultPattern
from autogen.agentchat.group import ContextVariables

ctx = ContextVariables(data={"confidence": 0})
pattern = DefaultPattern(
    initial_agent=triage_agent,
    agents=[triage_agent, billing_agent, tech_agent],
    context_variables=ctx,
    user_agent=user_proxy,
    group_manager_args={"llm_config": llm_config},
)
result, final_context, last_agent = initiate_group_chat(
    pattern=pattern, messages="Help me", max_rounds=40
)
```

### AfterWorkOption to Target Mapping

| Old `AfterWorkOption` | New Target class |
|----------------------|-----------------|
| `TERMINATE` | `TerminateTarget()` |
| `REVERT_TO_USER` | `RevertToUserTarget()` |
| `STAY` | `StayTarget()` |
| `SWARM_MANAGER` | `GroupManagerTarget()` |

### Migration Checklist

```
[ ] 1. Move imports from autogen.* -> autogen.agentchat.group.*
[ ] 2. ContextVariables: dict -> ContextVariables(data={...})
[ ] 3. Tool function param type: dict -> ContextVariables
[ ] 4. SwarmResult -> ReplyResult (agent->target, values->message)
[ ] 5. register_hand_off -> agent.handoffs.add_llm_conditions()
[ ] 6. AfterWork(AfterWorkOption.X) -> agent.handoffs.set_after_work(XTarget())
[ ] 7. initiate_swarm_chat -> initiate_group_chat with Pattern
[ ] 8. Pick Pattern: DefaultPattern (Swarm equivalent) or AutoPattern (LLM-driven)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_05_semantic_kernel]] | sibling | 0.35 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.29 |
| [[p01_kc_agent]] | sibling | 0.26 |
| [[kc_llm_agent_frameworks]] | sibling | 0.23 |
| [[bld_knowledge_card_crew_template]] | sibling | 0.22 |
| [[atom_06_langchain_langgraph]] | sibling | 0.21 |
| [[bld_collaboration_agent]] | downstream | 0.21 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.20 |
| [[agent-builder]] | downstream | 0.19 |
| [[atom_11_agentscope]] | sibling | 0.19 |
