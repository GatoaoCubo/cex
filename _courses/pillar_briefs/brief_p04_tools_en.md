---
quality: 8.1
id: kc_pillar_brief_p04_tools_en
kind: knowledge_card
pillar: P04
title: "P04 Tools — The Hands That Reach the World"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
language: en
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p04, tools, mcp, function-calling, agents, retriever, browser-tool, llm-engineering]
tldr: "Deep technical brief on P04 Tools: 36 kinds covering MCP servers, code executors, retrievers, communication tools, voice pipelines — universal framework for AI tool use and agentic capability."
source_concepts: [kc_lens_index, mentor_context, p03_pc_cex_universal]
related:
  - kc_pillar_brief_p04_tools_pt
  - kc_pillar_brief_p03_prompt_en
  - cm_driver_01_structured_thinking
  - kc_lens_factory
  - kc_lens_technical
  - mentor_context
density_score: 0.8
updated: "2026-04-22"
---

# P04 Tools — The Hands: How AI Reaches Into the World

## The Central Principle: AI Needs Hands

Here is the most important mental model in LLM engineering. Imagine the most brilliant person you know — deeply knowledgeable, fast thinker, articulate, creative. Now imagine that person locked in a soundproof room with no windows, no phone, no computer, no connection to the outside world. They can think brilliantly, but they can't touch anything. They can't look things up. They can't send a message. They can't run a calculation. They can only talk to whoever is in the room with them.

That is an LLM without tools.

Now give that person a phone, a laptop, access to the internet, the ability to send emails, run code, query databases, and control software. Suddenly, that same brilliant mind can act on the world. They go from "here's what I think" to "here's what I did."

That is an LLM with tools.

**Tools are the hands, the eyes, the voice, and the ears of an AI agent.** Without them, an LLM is a brain in a jar — extraordinary cognitive capacity with zero ability to interact with the world outside the conversation. With tools, that same model becomes an agent: something that perceives, reasons, acts, and produces real-world outcomes.

This shift is not incremental. It is architectural. And it applies equally to ChatGPT, Claude, Gemini, a local Llama model running on your laptop, or any other LLM you work with. The framework in this pillar is universal.

### The Before and After

**Before tools existed**, every LLM interaction followed the same pattern: user asks, LLM answers, conversation ends. The AI was a very sophisticated text predictor. Its only output was words. If you needed it to actually do something — look up current information, run a calculation, save a file, send a message — you had to do that yourself and paste the result back in.

**After tools**, the pattern changed completely. The AI can now:
- Browse the web to get current information
- Run code and show you the actual output, not just predicted output
- Read your documents and files directly
- Send messages to other systems on your behalf
- Query databases and return real data
- Remember things between sessions via external storage
- Trigger workflows in other applications

The AI is no longer answering your question. It is executing your intent.

### The Tool-Use Loop

Every AI agent, regardless of which model powers it, follows the same fundamental loop when using tools:

1. **Plan**: given the user's goal, decide what needs to happen
2. **Select**: choose which tool or sequence of tools to use
3. **Call**: invoke the tool with the right parameters
4. **Parse**: read and understand the tool's output
5. **Decide**: is the goal accomplished? If yes, synthesize the result. If no, go back to step 1 with new information
6. **Repeat**: most real tasks require multiple tool calls in sequence

This loop is what separates a chatbot from an agent. A chatbot returns one response. An agent iterates through this loop as many times as needed to actually complete the work.

Understanding this loop is the foundation of everything else in this pillar.


## The 5 Categories of AI Tools — A Universal Framework

Before diving into specific implementations, here is a framework that applies to every AI system you will ever work with. Regardless of provider, model, or framework, all AI tools fall into five fundamental categories. Think of them as the five types of hands an AI can have.

### Category A: Hands That BUILD — Execution Tools

These are tools that let AI write AND run things, not just describe them.

**What they do**: execute code, manipulate files, query databases, control processes, interact with operating systems.

**The game changer**: before code execution tools, an AI could write Python. With code execution tools, an AI can write Python, run it in a sandbox, see the output, debug any errors, and give you the final working result. The difference between "here is code that should work" and "here is working code with the actual output" is enormous.

**Works with any AI — try this today**:
- In ChatGPT: click "Code Interpreter" (now called "Advanced Data Analysis"). Upload a CSV file. Ask: "Clean this data, remove duplicates, find the top 10 rows by revenue, and create a chart." The AI just wrote Python, executed it, and showed you real results. No coding on your part.
- In Claude: use Claude Code (this terminal you are in right now). Ask it to create a file, run a script, check system info. It is doing all of this through execution tools.
- In Cursor or GitHub Copilot: the entire "run your tests and fix what fails" loop is execution tools in action.

**Key kinds in this category**: `code_executor`, `cli_tool`, `db_connector`, `daemon`, `computer_use`, `diff_strategy`

The most critical engineering decision in this category is sandboxing. A `cli_tool` that runs shell commands has no isolation — if the command goes wrong, it goes wrong on your real system. A `code_executor` with Docker or E2B isolation runs in a contained environment. The AI can run destructive code in the sandbox without affecting anything real. Always choose the weakest tool that solves the problem, but never skip the sandbox when the risk of side effects is real.

### Category B: Eyes That SEE — Perception Tools

These are tools that let AI observe the world: read websites, understand documents, analyze images, process audio.

**What they do**: browse web pages, extract text from PDFs, interpret screenshots, transcribe audio, read structured data from spreadsheets.

**The game changer**: an LLM's training data has a cutoff date. Without perception tools, the AI is operating from memory — potentially outdated, definitely incomplete. With perception tools, the AI can read any web page right now, process any document you hand it, and see any image you share. Its effective knowledge becomes as fresh and complete as the sources you give it access to.

**Works with any AI — try this today**:
- With ChatGPT or Claude browsing enabled: ask "Go to the Stripe pricing page and summarize their plan tiers compared to our competitor PayPal's pricing." The AI just did competitive research in 30 seconds by reading two live websites.
- With any AI that accepts PDFs: upload a contract, a research paper, or a financial report. Ask questions about it. The AI is using document perception — it is reading that file the way you would, extracting meaning from structure and content.
- With vision-enabled models (GPT-4V, Claude, Gemini): take a screenshot of an error message, a UI wireframe, or a spreadsheet. Paste it in. Ask what you want to know. The AI is using visual perception tools to understand image content.

**Key kinds in this category**: `browser_tool`, `vision_tool`, `document_loader`, `stt_provider`, `search_tool`

The most important distinction here is between `search_tool` and `retriever`. A search tool calls an external service (Tavily, Perplexity, Bing) and returns ranked web results — live, external, potentially unlimited breadth, but you pay per query and your queries go to a third party. A retriever queries a local vector store that you control — private, fast, fixed cost, but only knows what you have indexed. Real systems often use both: the retriever for your proprietary knowledge, the search tool for current external information. A `search_strategy` artifact explicitly encodes this trade-off.

### Category C: Voice That SPEAKS — Communication Tools

These are tools that let AI send messages, make API calls, trigger actions in other systems, and interact with the outside world.

**What they do**: send emails, post messages to Slack or Discord, call REST APIs, trigger webhooks, publish to social media, push notifications.

**The game changer**: before communication tools, AI was reactive — it only responded when you talked to it. With communication tools, AI becomes proactive. It can notice that something happened and do something about it. It can be the one to reach out, not just the one to respond.

**Works with any AI — try this today**:
- Use Zapier or Make.com to connect any AI to over 5,000 apps. Build this: "When a new email arrives with 'URGENT' in the subject, use AI to summarize it, categorize it, and send me a Slack notification with the summary." Zero code. The AI is doing the reading and summarizing; Zapier handles the communication with Gmail and Slack.
- Build a webhook: whenever something happens in your app (new user signs up, payment fails, error logged), send that event to an AI endpoint. The AI reads the event and decides what to do — maybe send a support message, maybe open a ticket, maybe just log it. This is event-driven AI.
- Use OpenAI's function calling or Anthropic's tool use to give your AI an email_send function. Now when a user asks your AI "send a follow-up to the people who didn't respond," the AI can actually do it instead of just drafting the text for you.

**Key kinds in this category**: `api_client`, `webhook`, `notifier`, `messaging_gateway`, `social_publisher`, `event_stream`

### Category D: Ears That LISTEN — Input Tools

These are tools that let AI receive information from external events, not just from direct user input.

**What they do**: receive webhook payloads, process audio streams, monitor real-time data feeds, receive scheduled triggers.

**The game changer**: most AI interactions are initiated by a human typing a message. Input tools break this constraint. AI can now be triggered by external events — a payment processed, a temperature sensor reading, a new commit pushed to GitHub, a cron schedule firing. The AI becomes part of your infrastructure, not just a chat interface.

**Works with any AI — try this today**:
- Set up a webhook in your application that fires when a user churns (cancels). Have that webhook call an AI endpoint with the user's data and churn reason. The AI analyzes the churn, drafts a win-back email, and queues it for your review. You built an AI-powered churn recovery loop with no manual intervention.
- Use a scheduled trigger (cron) to have an AI analyze your sales data every morning at 7 AM and send you a one-paragraph briefing via email. The AI is initiating this, not you.
- Pipe voice input to a speech-to-text tool first, then to your AI. Suddenly your AI application understands spoken language, not just typed text. This is the foundation of every voice assistant that matters.

**Key kinds in this category**: `stt_provider`, `audio_tool`, `webhook` (inbound), `event_stream`, `daemon`

### Category E: Memory That PERSISTS — Storage Tools

These are tools that let AI remember information across sessions, search through large knowledge bases, and access structured data stores.

**What they do**: store and retrieve information by semantic meaning (vector search), search through indexed knowledge bases, query databases, access file systems.

**The game changer**: an LLM's context window is a working memory — what it can hold at once. Without storage tools, every conversation starts from scratch. With storage tools, the AI can have a memory that grows over time, search through documents you have been accumulating for years, and recall facts that are relevant to the current conversation even if they were learned months ago.

**Works with any AI — try this today**:
- Build a RAG (Retrieval-Augmented Generation) pipeline with LlamaIndex or LangChain: index your company's documentation, your email history, your project notes. Connect it to any LLM. Now when users ask questions, the AI searches your knowledge base first and grounds its answers in your actual documents. Hallucination drops dramatically. Accuracy for your specific domain goes up dramatically.
- Use an MCP server (see the next section) to give your AI read access to your Notion workspace, Google Drive, or a local folder. The AI can now search through your actual files to answer questions. It is not making things up from training data — it is reading your stuff.
- Set up persistent memory with a tool like MemGPT or a simple database. Every conversation adds to what the AI knows about you. After 20 conversations, the AI knows your preferences, your ongoing projects, your communication style. It becomes genuinely personalized.

**Key kinds in this category**: `retriever`, `search_tool`, `knowledge_index`, `document_loader`, `mcp_server`


## The MCP Revolution — USB for AI

Of all the tool standards emerging in LLM engineering right now, MCP — the Model Context Protocol — is the one you need to understand most deeply. It is changing the architecture of AI tooling the same way USB changed the architecture of device connectivity.

### The Problem Before MCP

Before MCP, connecting an AI to an external tool meant writing custom integration code — every time, for every combination of AI model and tool. Claude needed Anthropic's tool-use format. GPT needed OpenAI's function-calling format. Gemini needed Google's format. If you wanted your AI to access your GitHub repo, you wrote GitHub integration code. If you also wanted it to access your database, you wrote database integration code. And you wrote all of this separately for each AI model you might want to support.

This was the pre-USB world of AI. Every device needed its own proprietary cable.

### What MCP Does

MCP defines a universal protocol: a standard way for any AI client (Claude, ChatGPT, Gemini, local Ollama models, anything) to connect to any tool server. The server exposes its capabilities. The AI discovers them. The AI calls them with structured arguments. The server returns structured results. Neither side needs to know anything about the other's implementation.

The analogy to USB is precise: just as USB made it so that any device with a USB port could connect to any computer with a USB port — regardless of manufacturer, operating system, or what the device does — MCP makes it so that any MCP-compatible AI can connect to any MCP-compatible tool server.

This is the standardization that will define the next generation of AI tooling.

### How MCP Works in Practice

An MCP server is a piece of software that:
1. Starts up and registers its capabilities (what tools it provides, what data it can access)
2. Waits for requests from an AI client
3. Receives structured calls with arguments
4. Executes the requested operation
5. Returns structured results

An MCP client (your AI) is software that:
1. Discovers what tools the server exposes
2. Includes those capabilities in the AI's available tool set
3. Calls them when the AI's reasoning determines it needs them
4. Processes the results as observations in the AI's reasoning loop

Real examples of MCP servers you can use today:
- **GitHub MCP**: your AI can read your repositories, issues, pull requests, and commit history. Ask Claude: "What are the most common error types in our error logs over the last 30 days?" and it can actually go read your GitHub issues to answer.
- **Slack MCP**: your AI can read and send Slack messages. Your AI assistant can now search your company's Slack history to find context for a question.
- **Filesystem MCP**: your AI can read and write files on your local machine. This is what enables Claude Code to edit your actual project files.
- **Database MCP**: your AI can run SQL queries against your database. Ask questions about your data in plain English; the AI figures out the query and returns the results.
- **Notion/Google Drive MCP**: your AI can search through your knowledge bases and documents.

### Why MCP Matters for You Right Now

If you work with AI and you are not using MCP yet, here is the practical implication: every MCP server you set up multiplies what your AI can do. Once you configure Claude (or any MCP-compatible client) with a set of MCP servers, you have given that AI access to all those capabilities. You did not write custom integration code. You did not change the AI model. You just connected some hands.

The CEXAI `mcp_server` artifact specifies:
- `transport`: `stdio` (local process) or `http_sse` (remote over network)
- `tools_provided`: the list of callable functions the server exposes
- `resources_provided`: data sources the AI can read from

This is the pattern. Define the capability, declare the transport, specify the tools. Any MCP-compatible AI can pick it up and start using it.


## The 36 Kinds in P04 — A Complete Map of AI Hands

All 36 kinds in P04 are organized into five subcategories. Each kind is a typed, versioned artifact definition with a defined role in the system. Every kind has a dedicated builder for creating purpose-fit instances.

### Execution Tools (9 kinds)

| Kind | Purpose | When to Use | Complexity |
|------|---------|-------------|------------|
| `cli_tool` | One-off shell command wrapper | Simple subprocess calls; no sandbox required | Low |
| `code_executor` | Sandboxed runtime (Docker, E2B, Jupyter) | LLM-generated code that must run safely | High |
| `db_connector` | SQL/GraphQL/REST-to-DB access | Structured data queries against any database | Medium |
| `supabase_data_layer` | Supabase-specific: tables + RLS + edge functions | Supabase-backed products with RLS enforcement | Medium |
| `computer_use` | GUI automation: screen, keyboard, mouse | Desktop apps with no API; last resort | High |
| `diff_strategy` | Change application and matching algorithm | Code patching, merge conflict resolution | Medium |
| `daemon` | Persistent background process | Long-running services, watchers, polling loops | High |
| `hook` | Pre/post processing hook | Event-driven side effects at known lifecycle points | Low |
| `hook_config` | Declarative hook lifecycle configuration | Builder-level hook orchestration | Low |

Key distinction: `cli_tool` terminates after each call; `daemon` persists between calls. `code_executor` sandboxes; `cli_tool` does not. Use the weakest tool that solves the problem — unnecessary sandboxing wastes latency and compute.

### Communication Tools (9 kinds)

| Kind | Purpose | When to Use | Complexity |
|------|---------|-------------|------------|
| `mcp_server` | MCP server exposing tools + resources | Any tool that must be shared across LLM clients | High |
| `mcp_app_extension` | MCP App lifecycle: install/launch/terminate | Packaging tools as discoverable MCP apps | High |
| `webhook` | HTTP event-driven endpoint (inbound/outbound) | Receiving external events or pushing notifications | Medium |
| `messaging_gateway` | Multi-platform bidirectional messaging | Telegram/Discord/Slack/WhatsApp unified session | High |
| `notifier` | One-way push notification (email, SMS, Slack) | Alerts without conversation context | Low |
| `api_client` | Typed REST/GraphQL/gRPC client | Outbound calls to external APIs | Medium |
| `agent_name_service_record` | IETF ANS registry entry for agent discovery | Multi-agent networks; A2A routing | Medium |
| `event_stream` | Real-time ordered domain event configuration | Pub/sub feeds; stream processing pipelines | High |
| `social_publisher` | Full social media publish pipeline | Autonomous content publishing | High |

The `messaging_gateway` is architecturally notable. It maintains simultaneous connections across multiple platforms under a single session model — the same identity, the same memory, regardless of whether the user is talking to your AI on Telegram or Discord or Slack at any given moment.

### Research and Knowledge Tools (6 kinds)

| Kind | Purpose | When to Use | Complexity |
|------|---------|-------------|------------|
| `research_pipeline` | 7-stage engine: INTENT→PLAN→RETRIEVE→RESOLVE→SCORE→SYNTHESIZE→VERIFY | Deep intelligence gathering; multi-source synthesis | High |
| `search_tool` | Web/semantic/hybrid search (Tavily, Serper, Perplexity) | External information retrieval | Low |
| `retriever` | Vector/keyword/hybrid local search (RAG core) | Local knowledge base queries | Medium |
| `document_loader` | File ingestion + chunking (PDF, HTML, CSV) | Transforming files into retrieval-ready chunks | Medium |
| `search_strategy` | Inference-time compute allocation for search | Multi-pass RAG; dense vs. sparse trade-offs | Medium |
| `browser_tool` | Playwright/Puppeteer: DOM navigation, screenshots | JS-heavy pages where static fetch fails | High |

The `research_pipeline` is qualitatively different from `search_tool`. A search tool makes one call and returns ranked results. A research pipeline runs seven LLM-mediated stages and produces a cited, quality-scored knowledge artifact. The `min_sources` field is a hard constraint — the pipeline will not proceed to synthesis until a minimum number of distinct sources have been retrieved and resolved, preventing the LLM from hallucinating evidence.

### Media and Multimodal Tools (6 kinds)

| Kind | Purpose | When to Use | Complexity |
|------|---------|-------------|------------|
| `vision_tool` | Image analysis, OCR, screenshot interpretation | Visual data extraction; layout understanding | Medium |
| `audio_tool` | STT/TTS/audio analysis (combined) | Audio I/O where provider is not yet decided | Low |
| `tts_provider` | Text-to-speech provider contract | Stable voice identity for a persona or product | Medium |
| `stt_provider` | Speech-to-text provider contract | Transcription layer for voice pipelines | Medium |
| `voice_pipeline` | End-to-end STT→LLM→TTS architecture | Full spoken conversation agent | High |
| `multi_modal_config` | Input format, resolution, encoding, routing rules | Configuring how multimodal inputs flow to LLMs | Low |

These kinds form a composable media stack. `stt_provider` and `tts_provider` are atomic components; `voice_pipeline` wires them together with an LLM as the brain, specifying latency targets, interruption handling, and turn-taking protocol.

### Integration and Extension Tools (6 kinds)

| Kind | Purpose | When to Use | Complexity |
|------|---------|-------------|------------|
| `toolkit` | Named tool bundle with auto JSON Schema | Assigning a complete tool environment to an agent | Medium |
| `function_def` | LLM-callable function (JSON Schema tool) | Individual callable capability definitions | Low |
| `skill` | Reusable capability with trigger + phases | Auto-firing lazy behaviors; slash command handlers | Medium |
| `plugin` | Pluggable system extension | System-level extensions with lifecycle beyond single event | Medium |
| `action_paradigm` | ReAct/Plan-Execute/event-driven execution contract | Defining how an agent interacts with its tool environment | High |
| `sdk_example` | Canonical SDK integration code per language | Developer reference; reduces integration friction | Low |


## Key Engineering Patterns

### Function Calling — The Foundation of Tool Use

Before MCP became widespread, the way most LLMs used tools was through function calling (OpenAI's term) or tool use (Anthropic's term). The concept is the same across all providers.

You define a function with a JSON Schema description: what the function is called, what arguments it takes, what each argument means. You include this in the API request alongside the user's message. The LLM reads the function definition and, when it determines the function would be useful, it outputs a structured call — not an answer, but an instruction to call that specific function with specific arguments. Your code intercepts that, actually calls the function, and feeds the result back to the LLM. The LLM then continues its reasoning with that result.

This is the fundamental mechanism behind all "AI tool use" you see in products today.

**Practical example in the OpenAI API**:
```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": "Get the current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and state, e.g. San Francisco, CA"
                }
            },
            "required": ["location"]
        }
    }
}]
```

When the user asks "What should I wear in Paris today?", the LLM does not guess. It calls `get_current_weather(location="Paris, France")`, receives the real temperature, and gives a grounded answer.

The `description` field of each parameter is not documentation for humans. It is prompt engineering inside a schema — the LLM reads it to understand what to pass. If the description is ambiguous, the LLM will pass wrong arguments. Write descriptions like you are writing instructions for a smart but literal colleague who has never seen the function before.

### The Toolkit Pattern — Managing Tool Environments

A `toolkit` is the artifact that answers "what tools does this agent have access to?" It bundles multiple tool definitions into a named, versioned package that can be assigned to an agent at boot. The `auto_schema: true` flag triggers automatic JSON Schema generation from all included tool definitions, so the LLM receives a consistent and complete tool schema without manual maintenance.

Example toolkit for an intelligence-gathering agent:
```yaml
id: tk_n01_intelligence_tools
kind: toolkit
pillar: P04
nucleus: n01
auto_schema: true
max_parallel_calls: 5
tools:
  - st_tavily_web_search
  - ret_cex_tfidf_local
  - dl_pdf_semantic_chunker
  - ct_git_ops
```

The `max_parallel_calls` field is an important safety boundary. Without it, a ReAct loop with search tools can generate dozens of concurrent calls under latency pressure, exhausting API quotas and creating race conditions. Always set explicit limits on tool fan-out.

### The Action Paradigm — How Agents Use Tools

The `action_paradigm` kind codifies how tool-use loops operate. There are four fundamental patterns, each with distinct tradeoffs:

**ReAct (Reason + Act)**: the agent interleaves thinking steps with tool calls. "I need to know the current price. Let me call the search tool. OK, the price is X. Now I need to compare it to Y. Let me call the database tool." This is the most common pattern. High transparency, slightly higher latency because each thought step is a separate LLM call.

**Plan-Execute**: the agent generates a complete plan first — "I will call tools A, B, C in sequence" — and then executes all calls without interleaved reasoning. Faster for deterministic workflows. Risky when the environment is dynamic and early results change what later steps should do.

**Event-Driven**: tool calls are triggered by incoming signals, not LLM reasoning steps. A webhook fires, a scheduled event triggers, a sensor reading arrives — the agent responds. This is the pattern for daemons and background processes.

**Reflexion**: the agent makes a tool call, reads the result, critiques its own reasoning, and decides whether to try a different approach before continuing. Highest quality for complex research tasks. Most expensive. Use when accuracy matters more than cost.

The `observation_format` field in an action paradigm definition specifies how tool output is structured for the LLM. Structured output formats — `{"tool": "search", "result": [...], "error": null}` — let the LLM reason directly from the data. Unstructured text output requires the LLM to first parse before reasoning, adding an error-prone step.

### Skills — Auto-Firing Behaviors

The `skill` kind differs from `function_def` in one critical dimension: trigger condition. A function definition is called explicitly by an LLM reasoning step — the model decides to call it. A skill fires automatically when its trigger pattern is detected, without the LLM having to reason about whether to use it.

This is the pattern behind: auto-completion in code editors, slash command handlers in Slack bots, "when you detect X, automatically do Y" behaviors.

Skills have two loading modes: `lazy: true` means the skill loads on first trigger (saves context window space at boot); `lazy: false` means it loads at startup. Lazy loading is the default because loading every possible skill at boot inflates the context window without benefit until the trigger fires.


## Safety and Guardrails — Power Requires Boundaries

Tools give AI power. Power requires explicit limits. This is not optional.

An AI with database write access can also delete your database. An AI that can send emails can spam your entire contact list. An AI with shell access can run `rm -rf /`. These are not hypothetical risks — they are exactly what happens when tools are given without safety boundaries.

The CEXAI framework separates capability definition (P04) from permission constraints (P09 Config). The P04 artifact describes what a tool CAN do. The P09 configuration describes what it is ALLOWED to do in a specific deployment context.

This separation is critical for two reasons. First, it means the same tool definition can be deployed with different permission levels in different contexts — a developer environment with broad access, a production environment with narrow access. Second, it means permissions cannot be defined by accident inside a tool description. They are explicit, reviewed, version-controlled artifacts.

### The Sandbox Pattern

When an AI runs code, always sandbox it. This means running the code in an isolated environment — a Docker container, a cloud sandbox like E2B, a Jupyter kernel — where it cannot affect the host system. If the AI writes malicious or buggy code, only the sandbox breaks. Your real system is untouched.

The `code_executor` kind encodes this pattern. A properly defined code executor specifies:
- `runtime`: which sandboxing technology to use
- `timeout_seconds`: maximum execution time (prevents infinite loops)
- `resource_limits`: CPU, memory, network access (prevents resource exhaustion)

A code executor without resource limits can exhaust host memory. A code executor without a timeout can run forever. These are not edge cases — they are routine in LLM-generated code.

### The Human-in-the-Loop Pattern

For high-risk actions — sending money, deleting data, contacting clients, posting publicly — require human approval before the AI acts. This is not a trust question. It is a risk management question. Even a highly accurate AI making mistakes on 1% of actions is too high a rate when the mistakes involve transferring funds or deleting customer data.

The `revision_loop_policy` kind encodes how many times an AI can attempt a tool call and evaluate the result before requiring human review. Set this explicitly. Never leave it unbounded.

### The Rate Limit Pattern

Every external API has limits. An AI in an agentic loop can exhaust API quotas in seconds if tool calls are not rate-limited. The `api_client` kind encodes the rate limiting contract explicitly — not as a comment, as a machine-readable field:

```yaml
retry_policy:
  tool_error: {max: 3, backoff: exponential}
  rate_limit: {max: 5, backoff: honor_retry_after}
  auth_error: {max: 1, backoff: none}
```

The `auth_error` case is important: authentication failures are not transient. Retrying them wastes time and may trigger account lockouts. Fail fast on auth errors; retry on transient errors only.

### MCP Security — Read-Only by Default

MCP servers can expose both read and write capabilities. The security principle is: start with read-only, add write permissions explicitly and deliberately.

The CEXAI GitHub MCP server enforces this with a whitelist of allowed operations — only `get_*`, `list_*`, and `search_*` operations. All mutation operations are denied at the permission level, not through trust in the LLM's judgment. An LLM might decide it "should" create a branch or merge a PR. The permission system ensures it cannot, regardless of its reasoning.

The messaging gateway kind enforces the same principle at the human level: `dm_pairing: true` requires a user to initiate first contact before the agent will accept commands. This prevents command injection from arbitrary users who find your bot's address.


## Architecture: How Tools Connect to the Rest of the System

P04 is where the agent reaches outside itself, but it does not operate in isolation. Every tool definition connects to other parts of the system in specific, typed relationships.

### Tool Discovery: the Capability Registry

P04 defines tools. P08 (Architecture) provides the index. The `capability_registry` is the authoritative lookup table for all available agents and their tool capabilities. When an orchestrator plans which agent to assign to a task, it queries the capability registry to find which agents can handle which types of tool calls — not by scanning all tool definitions, but through a precomputed index.

This separation is deliberate: definitions are ground truth for what a tool is; the registry is an optimized index for routing decisions. The registry can always be rebuilt from P04 at any time, but routing does not pay the cost of scanning everything on every decision.

### The Prompt Bridge

Tools are defined in P04 but called from P03 (Prompt) artifacts. A chain of prompts executes multiple steps in sequence, and each step may include tool calls. The bridge between the two is the JSON Schema: the `function_def` artifact's parameter definitions become the schema the LLM sees in its tool-use context. Write these definitions as carefully as you write prompt instructions — they are prompt engineering inside a schema.

### The Guardrail Wire

Tool call results feed into P11 (Feedback) evaluation artifacts before reaching the LLM:
- A guardrail can inspect search results and reject disallowed content before the LLM sees it
- A bugloop drives a code executor in a loop until execution output satisfies a quality gate
- A revision loop policy sets the maximum number of tool-call-evaluate iterations before forcing human review

This creates a complete feedback loop: tools execute, evaluators assess the output, and the pipeline either proceeds or iterates. This is how you prevent an AI agent from endlessly retrying failed tool calls or consuming bad tool output.


## Real Examples from the Repository

### 1. Marketplace Scraping Stack (Commerce Intelligence)

The research pipeline and browser tool composition in `N00_genesis/P04_tools/` demonstrates how perception and research tools combine. The research pipeline defines 8 stages (extending the canonical 7 with a brand-specific synthesis stage) and references the browser tool as its execution layer.

Key engineering decisions encoded in the artifact: rate limiting (1 request per second per domain, 5 concurrent globally), respectful scraping (transparent User-Agent, robots.txt compliance), and a typed output contract (market intelligence table row plus daily LLM digest). The browser tool specifies Playwright with explicit rationale over Puppeteer — better network intercept and auto-wait semantics — plus resource limits and TypeScript interface contract.

This is the pattern of encoding decisions as artifacts rather than leaving them in comments or developer memory.

### 2. Shopify API Client (e-commerce Integration)

The production-grade `api_client` example shows how business decisions become machine-readable policy: rate limiting as a leaky bucket contract (1000 cost points, 50 restore per second, emitting the `shopify.rate_limit.remaining` metric), a UTF-8 repair rule applied only on the read path, and a retry strategy that distinguishes between network errors (exponential backoff), rate limits (honor the Retry-After header), and client errors (fail fast).

Brand template variables (`{{BRAND_SHOPIFY_API_VERSION}}`, `{{BRAND_SHOPIFY_ADMIN_TOKEN}}`) mean the same artifact definition serves any Shopify store. The token reference points to an environment variable name, never the actual credential.

### 3. TTS Brand Persona (Voice Identity)

The `tts_provider` example shows how a voice identity decision — which voice represents your brand — becomes a governed artifact rather than a hardcoded string. The voice identifier is a brand configuration variable. The fallback voice for when the primary voice fails is explicitly defined. Selection rules are stated in natural language: "Reject voices that distort product names or CTA phrases."

This pattern — encoding business policy as artifact constraints — is what separates P04 from ad-hoc configuration.

### 4. Messaging Gateway Security (HERMES Architecture)

The messaging gateway template shows security fields as first-class artifact requirements, not optional comments. The `dm_pairing: true` requirement forces a user to initiate the first contact before the agent will accept commands. The `rate_limit_per_user_per_min: 30` field limits how fast any single user can interact. The `command_approval_list: []` and `allowed_user_ids: []` fields start empty and must be explicitly populated — deny by default, allow by exception.


## Anti-Patterns as Universal Mistakes

These mistakes are not specific to any platform. They show up in every AI system that uses tools.

**Giving AI tools without safety boundaries** is like giving a toddler a power drill. The tool is powerful. The user of the tool may not have the judgment to use it safely in every situation. Boundaries are not a lack of trust — they are responsible engineering.

**Not testing tool outputs before trusting them** is the source of most AI-in-production failures. Tool calls can return partial results, malformed data, stale information, or outright errors. A guardrail layer that validates tool output before the LLM reasons from it is not overhead — it is the difference between an agent that works reliably and one that fails spectacularly.

**Building custom integrations when MCP or standard protocols exist** is the pre-USB mistake applied to AI. Every hour you spend building bespoke integration code is technical debt that MCP would have prevented. Check for existing MCP servers before building custom tool integrations.

**Treating tools as optional** is the most common and most costly mistake. Developers who think of AI tools as "advanced features" build chatbots when they need agents. Tools are not optional enhancements — they are the architectural layer that separates a system that suggests from a system that acts. If your AI needs to produce outcomes (not just text), it needs tools.

**Monolithic tool definitions** — one large function that does many things — create brittle coupling and make granular permission impossible. The correct pattern: each function definition does one thing with a narrow, typed schema. Related definitions are bundled into toolkits. Toolkits are assigned to agents. P09 config constrains which toolkits each agent is permitted to use.

**Ignoring error handling** in tool definitions forces every caller to invent its own error handling, creating inconsistency. Tool calls fail routinely in production — network timeouts, API rate limits, malformed responses, authentication errors. Encode the retry policy in the tool definition, not in the calling code.


## Connection to Other Pillars

P04 tools do not operate in isolation. Every tool connects to other parts of the system through typed relationships:

| Source | Target | Relationship | Mechanism |
|--------|--------|-------------|-----------|
| P04 `toolkit` | P02 `agent` | supplies | agent.tools references toolkit ID |
| P04 `function_def` | P03 `chain` | called from | chain steps include tool_call nodes |
| P04 `mcp_server` | P08 `capability_registry` | indexed by | registry stores all mcp_server endpoints |
| P04 `code_executor` | P09 `sandbox_config` | constrained by | P09 sets resource limits and network policy |
| P04 `retriever` | P01 `chunk_strategy` | consumes output of | retriever queries chunks indexed per P01 strategy |
| P04 `research_pipeline` | P01 `knowledge_card` | produces | SYNTHESIZE stage outputs a knowledge_card |
| P04 `browser_tool` | P11 `guardrail` | output evaluated by | guardrails inspect tool output before LLM use |
| P04 `social_publisher` | P12 `schedule` | triggered by | schedule artifact fires social_publisher on cron |
| P04 `skill` | P03 `instruction` | references | skill phases cite instruction artifacts |
| P04 `voice_pipeline` | P04 `stt_provider` + `tts_provider` | composes | pipeline wires the three components |

The most important pattern: P04 tools are defined once in the canonical architecture and instantiated per agent. An intelligence-gathering agent has its own `retriever` instance tuned for competitive research. A knowledge management agent has a different `retriever` tuned for internal knowledge base queries. Both inherit from the same P04 schema. Both are quality-scored against the same rubric. But they are distinct, purpose-fit artifacts — the same hand, holding different tools.

P04 is not a library of tools you copy and paste. It is a typed, governed, quality-scored factory for external capabilities. You do not copy from a factory. You operate it.

The central truth of this pillar is simple: every outcome your AI produces that matters to the real world required a tool to make it happen. The quality of your tool engineering determines the quality of your agent's impact. Build the hands well, and the brain's brilliance can finally reach the world.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_pillar_brief_p04_tools_pt]] | translation | 1.00 |
| [[kc_pillar_brief_p03_prompt_en]] | sibling | 0.85 |
| [[cm_driver_01_structured_thinking]] | downstream | 0.50 |
| [[kc_lens_factory]] | upstream | 0.45 |
| [[kc_lens_technical]] | upstream | 0.42 |
| [[mentor_context]] | upstream | 0.38 |
