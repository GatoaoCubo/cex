# Framework Official Taxonomy
> Sources: Official docs only | Scraped: 2026-03-29
> Method: mcp__fetch__fetch on all official documentation URLs
> Frameworks: LangChain, LlamaIndex, CrewAI, DSPy, Haystack, Instructor, Guardrails AI, Outlines

---

## LangChain (python.langchain.com / langchain_core)

| Class/Concept | Module | Category | Description |
|---|---|---|---|
| `create_agent` | `langchain.agents` | Factory | Create a prebuilt LangChain agent in <10 lines |
| `AgentExecutor` | `langchain.agents` | Agent | Executes agent loop with tools (legacy) |
| `BaseTool` | `langchain_core.tools` | Tool | Abstract base for all tools |
| `StructuredTool` | `langchain_core.tools` | Tool | Tool with typed Pydantic input schema |
| `@tool` | `langchain_core.tools` | Decorator | Converts function into a Tool |
| `BaseRetriever` | `langchain_core.retrievers` | Retrieval | Abstract retriever interface |
| `VectorStoreRetriever` | `langchain_core.vectorstores` | Retrieval | Retriever backed by VectorStore |
| `VectorStore` | `langchain_core.vectorstores` | Storage | Abstract vector store interface |
| `Document` | `langchain_core.documents` | Data | Core data container (page_content + metadata) |
| `TextSplitter` | `langchain_text_splitters` | Loading | Abstract base for text chunking |
| `RecursiveCharacterTextSplitter` | `langchain_text_splitters` | Loading | Hierarchical text splitter |
| `BaseDocumentLoader` | `langchain_core.document_loaders` | Loading | Abstract document loader |
| `BaseOutputParser` | `langchain_core.output_parsers` | Output | Abstract output parser |
| `StrOutputParser` | `langchain_core.output_parsers` | Output | Parse LLM output as plain string |
| `JsonOutputParser` | `langchain_core.output_parsers` | Output | Parse LLM output as JSON |
| `PydanticOutputParser` | `langchain_core.output_parsers` | Output | Parse LLM output into Pydantic model |
| `BaseChatModel` | `langchain_core.language_models.chat_models` | Model | Abstract chat model interface |
| `BaseLanguageModel` | `langchain_core.language_models` | Model | Root abstract language model |
| `BaseEmbeddings` | `langchain_core.embeddings` | Model | Abstract embeddings interface |
| `HumanMessage` | `langchain_core.messages` | Message | Human turn in conversation |
| `AIMessage` | `langchain_core.messages` | Message | AI turn in conversation |
| `SystemMessage` | `langchain_core.messages` | Message | System prompt message |
| `FunctionMessage` | `langchain_core.messages` | Message | Function/tool result message |
| `ToolMessage` | `langchain_core.messages` | Message | Tool result message (v0.3+) |
| `ChatPromptTemplate` | `langchain_core.prompts` | Prompt | Prompt template for chat models |
| `PromptTemplate` | `langchain_core.prompts` | Prompt | Classic string prompt template |
| `Runnable` | `langchain_core.runnables` | LCEL | Base interface for composable chains |
| `RunnableSequence` | `langchain_core.runnables` | LCEL | Chain of Runnables via `|` operator |
| `RunnableLambda` | `langchain_core.runnables` | LCEL | Wrap any function as Runnable |
| `RunnableParallel` | `langchain_core.runnables` | LCEL | Run multiple Runnables in parallel |
| `BaseChatMessageHistory` | `langchain_core.chat_history` | Memory | Stores conversation messages |
| `Chain` | `langchain.chains` | Legacy | Base class for legacy chains |
| `LLMChain` | `langchain.chains` | Legacy | Basic LLM + prompt chain (legacy) |

---

## LlamaIndex (docs.llamaindex.ai)

| Class/Concept | Module | Category | Description |
|---|---|---|---|
| `Document` | `llama_index.core` | Data | Generic container for any data source |
| `TextNode` | `llama_index.core.schema` | Data | Chunk of a source Document with metadata |
| `Node` | `llama_index.core.schema` | Data | Abstract node (text, image, etc.) |
| `NodeRelationship` | `llama_index.core.schema` | Data | Relationships between nodes |
| `NodeParser` | `llama_index.core.node_parser` | Loading | Abstract base for document-to-node splitting |
| `SentenceSplitter` | `llama_index.core.node_parser` | Loading | Split by sentence boundaries |
| `SimpleDirectoryReader` | `llama_index.core` | Loading | Easy multi-file document loader |
| `IngestionPipeline` | `llama_index.core.ingestion` | Loading | End-to-end document processing pipeline |
| `VectorStoreIndex` | `llama_index.core` | Indexing | Semantic search index via embeddings |
| `PropertyGraphIndex` | `llama_index.core` | Indexing | Graph-based indexing |
| `VectorStore` | `llama_index.core.storage.docstore` | Storage | Embedding storage interface |
| `DocumentStore` | `llama_index.core.storage.docstore` | Storage | Document persistence |
| `SimpleDocumentStore` | `llama_index.core.storage.docstore` | Storage | In-memory document store |
| `IndexStore` | `llama_index.core.storage.index_store` | Storage | Index metadata storage |
| `StorageContext` | `llama_index.core` | Storage | Unified storage configuration |
| `QueryEngine` | `llama_index.core.query_engine` | Querying | Process and answer queries |
| `ChatEngine` | `llama_index.core.chat_engine` | Querying | Conversational query interface |
| `BaseRetriever` | `llama_index.core.retrievers` | Querying | Abstract retriever interface |
| `ResponseSynthesizer` | `llama_index.core.response_synthesizers` | Querying | Generate coherent answers from context |
| `LLM` | `llama_index.core.llms` | Model | Language model interface |
| `Embedding` | `llama_index.core.embeddings` | Model | Embedding model interface |
| `Settings` | `llama_index.core` | Config | Global LlamaIndex configuration |
| `Workflow` | `llama_index.core.workflow` | Agent | Event-driven agentic workflow base |
| `AgentWorkflow` | `llama_index.core.agent` | Agent | Multi-agent collaboration system |

---

## CrewAI (docs.crewai.com)

| Class/Concept | Module | Category | Description |
|---|---|---|---|
| `Agent` | `crewai` | Core | Autonomous unit with role, goal, backstory |
| `Task` | `crewai` | Core | Specific assignment for an agent |
| `Crew` | `crewai` | Core | Collaborative group of agents + tasks |
| `Process` | `crewai` | Execution | `Process.sequential` or `Process.hierarchical` |
| `Memory` | `crewai` | Memory | Unified memory system (LLM-inferred scopes) |
| `MemoryScope` | `crewai` | Memory | Scoped subtree view of Memory |
| `Flow` | `crewai.flow.flow` | Workflow | Built-in memory + event-driven flow |
| `BaseTool` | `crewai.tools` | Tool | Base class for custom tools |
| `BaseAgent` | `crewai.agents.agent_builder.base_agent` | Agent | Abstract agent interface |
| `BaseKnowledgeSource` | `crewai` | Knowledge | Abstract knowledge source |
| `LLM` | `crewai` | Model | LLM wrapper (LiteLLM-based) |
| `TaskOutput` | `crewai` | Output | Structured task result (raw/json/pydantic) |
| `CrewStreamingOutput` | `crewai` | Output | Real-time streaming output chunks |
| `AgentPlanner` | `crewai` | Planning | Pre-task planning LLM component |
| `CrewBase` | `crewai.project` | Decorator | Marks class as crew definition |
| `@agent` | `crewai.project` | Decorator | Marks method returning Agent |
| `@task` | `crewai.project` | Decorator | Marks method returning Task |
| `@crew` | `crewai.project` | Decorator | Marks method returning Crew |
| `@before_kickoff` | `crewai.project` | Decorator | Hook before crew execution |
| `@after_kickoff` | `crewai.project` | Decorator | Hook after crew execution |
| `@start()` | `crewai.flow.flow` | Decorator | Marks Flow entry method |
| `@listen()` | `crewai.flow.flow` | Decorator | Marks Flow listener method |

**Agent key params:** `role`, `goal`, `backstory`, `llm`, `tools`, `memory`, `max_iter`, `allow_delegation`, `reasoning`, `multimodal`, `knowledge_sources`

**Task key params:** `description`, `expected_output`, `agent`, `tools`, `context`, `output_pydantic`, `guardrail`, `async_execution`

**Crew key params:** `agents`, `tasks`, `process`, `memory`, `embedder`, `planning`, `manager_agent`, `stream`

---

## DSPy (dspy.ai)

| Class/Concept | Module | Category | Description |
|---|---|---|---|
| `Module` | `dspy` | Core | Base class for DSPy programs (PyTorch-inspired) |
| `Signature` | `dspy` | Core | Declarative input/output behavior spec |
| `InputField` | `dspy` | Core | Typed input field in a Signature |
| `OutputField` | `dspy` | Core | Typed output field in a Signature |
| `Prediction` | `dspy` | Core | Output object from any module call |
| `LM` | `dspy` | Model | Language model wrapper |
| `Predict` | `dspy` | Module | Basic predictor — no prompt modification |
| `ChainOfThought` | `dspy` | Module | Step-by-step reasoning before output |
| `ProgramOfThought` | `dspy` | Module | Code-execution-based reasoning |
| `ReAct` | `dspy` | Module | Tool-using agent (Reasoning + Acting) |
| `MultiChainComparison` | `dspy` | Module | Compare multiple CoT outputs |
| `RLM` | `dspy` | Module | Recursive LM for large-context tasks |
| `majority` | `dspy` | Function | Voting across multiple predictions |
| `ColBERTv2` | `dspy` | Retrieval | ColBERT retrieval model integration |
| `Image` | `dspy` | Type | Multimodal image input type |
| `History` | `dspy` | Type | Conversation history type |
| `LabeledFewShot` | `dspy` | Optimizer | Few-shot from labeled examples |
| `BootstrapFewShot` | `dspy` | Optimizer | Self-generate demonstrations |
| `BootstrapFewShotWithRandomSearch` | `dspy` | Optimizer | BootstrapFewShot + random search |
| `KNNFewShot` | `dspy` | Optimizer | KNN-selected demonstrations |
| `COPRO` | `dspy` | Optimizer | Instruction optimization via coordinate ascent |
| `MIPROv2` | `dspy` | Optimizer | Bayesian instruction + demo optimization |
| `SIMBA` | `dspy` | Optimizer | Stochastic mini-batch self-reflection |
| `GEPA` | `dspy` | Optimizer | LM-reflection trajectory optimizer |
| `BootstrapFinetune` | `dspy` | Optimizer | Fine-tune LM weights from demonstrations |
| `Ensemble` | `dspy` | Optimizer | Ensemble multiple DSPy programs |
| `BetterTogether` | `dspy` | Meta-Optimizer | Combines prompt + weight optimization |
| `SemanticF1` | `dspy.evaluate` | Eval | Semantic F1 evaluation metric |
| `answer_exact_match` | `dspy.evaluate` | Eval | Exact match evaluation metric |

---

## Haystack (docs.haystack.deepset.ai) — v2.x

| Class/Concept | Module | Category | Description |
|---|---|---|---|
| `@component` | `haystack` | Decorator | Marks a class as a Haystack component |
| `@component.output_types` | `haystack` | Decorator | Declares component output schema |
| `Pipeline` | `haystack` | Core | Directed multigraph of components |
| `AsyncPipeline` | `haystack` | Core | Async parallel pipeline execution |
| `SuperComponent` | `haystack` | Core | Wraps a complete pipeline as single component |
| `Document` | `haystack` | Data | Core document data structure |
| `DocumentStore` | `haystack` | Storage | Abstract document storage interface |
| `DocumentWriter` | `haystack.components.writers` | Component | Writes documents into a DocumentStore |
| `SentenceTransformersDocumentEmbedder` | `haystack.components.embedders` | Component | Embeds documents via SentenceTransformers |
| `SentenceTransformersTextEmbedder` | `haystack.components.embedders` | Component | Embeds query strings |
| `TransformerSimilarityRanker` | `haystack.components.rankers` | Component | Ranks documents by similarity to query |
| `ConditionalRouter` | `haystack.components.routers` | Component | Routes pipeline flow conditionally |
| `Retriever` | `haystack.components.retrievers` | Component | Retrieves relevant documents |
| `PromptBuilder` | `haystack.components.builders` | Component | Builds prompts from templates |
| `OpenAIGenerator` | `haystack.components.generators` | Component | LLM generation via OpenAI API |
| `OpenAIChatGenerator` | `haystack.components.generators` | Component | Chat LLM generation via OpenAI |
| `from_dict` / `to_dict` | (all components) | Serialization | Serialize/deserialize components |
| `Pipeline.add_component()` | `haystack` | Method | Add component to pipeline |
| `Pipeline.connect()` | `haystack` | Method | Wire component outputs to inputs |
| `Pipeline.run()` | `haystack` | Method | Execute the pipeline |

---

## Instructor (python.useinstructor.com)

| Class/Concept | Module | Category | Description |
|---|---|---|---|
| `from_provider` | `instructor` | Core | Unified client creation for any LLM provider |
| `patch` | `instructor` | Core | Patch an existing LLM client (legacy pattern) |
| `response_model` | `instructor` | Param | Pydantic model defining expected output structure |
| `Mode` | `instructor` | Enum | Output mode: `TOOLS`, `JSON`, `MD_JSON`, `FUNCTIONS` |
| `Retrying` | `instructor` | Validation | Automatic retry with error feedback to LLM |
| `Validator` | `instructor` | Validation | Custom Pydantic validation logic |
| `Hooks` | `instructor` | Observability | Callbacks for monitoring/debugging |
| `Stream Partial` | `instructor` | Streaming | Stream partially completed Pydantic objects |
| `Stream Iterable` | `instructor` | Streaming | Stream collection of completed objects |
| `TypeAdapter` | `instructor` | Types | Use TypeAdapter instead of BaseModel |
| `TypedDict` | `instructor` | Types | Use TypedDict for flexible typing |

**Core pattern:** Define output with `BaseModel` → create client via `instructor.from_provider()` → call `.create(response_model=MyModel)` → get validated Pydantic object.

---

## Guardrails AI (guardrailsai.com)

| Class/Concept | Module | Category | Description |
|---|---|---|---|
| `Guard` | `guardrails` | Core | Main interface — wraps LLM calls + orchestrates validation |
| `GuardResponse` | `guardrails` | Output | Contains: `raw_llm_output`, `validated_output`, `validation_passed` |
| `Validator` | `guardrails` | Validation | Pre-built risk measure from Guardrails Hub |
| `OnFailAction` | `guardrails` | Validation | Action on failure: `fix`, `reask`, `filter`, `refrain`, `exception` |
| `Guard.__call__()` | `guardrails` | Method | Call LLM + validate; pass model + messages |
| `Guard.parse()` | `guardrails` | Method | Validate existing LLM output (post-process) |
| `guard.history` | `guardrails` | Observability | Full call + validation history |
| `num_reasks` | `guardrails` | Param | Number of automatic re-asks on validation failure |

**Two modes:**
1. **Structured output**: `Guard(output_class=MyPydanticModel)` — generate + validate structured data
2. **String guard**: `Guard()` — validate free-form LLM string output

---

## Outlines (dottxt-ai.github.io/outlines)

| Class/Concept | Module | Category | Description |
|---|---|---|---|
| `from_openai` | `outlines` | Factory | Create model from OpenAI client |
| `from_transformers` | `outlines` | Factory | Create model from HuggingFace Transformers |
| `from_vllm` | `outlines` | Factory | Create model from vLLM |
| `from_ollama` | `outlines` | Factory | Create model from Ollama |
| Model callable | `outlines` | Core | `model(prompt, output_type)` — main interface |
| JSON Schema | `outlines` | Structure | Pass `dict` or JSON schema string as output_type |
| Pydantic BaseModel | `outlines` | Structure | Pass Pydantic model as output_type |
| `Literal` types | `outlines` | Structure | Constrained choice generation |
| Regex | `outlines` | Structure | Regex-constrained generation |
| Context-Free Grammar | `outlines` | Structure | CFG-constrained generation |

**Core principle:** Guaranteed structured output during generation — not post-processing. Compilation happens once per schema, then microsecond overhead per request.

---

## Cross-Framework Alignment

| Concept | LangChain | LlamaIndex | CrewAI | DSPy | Haystack |
|---|---|---|---|---|---|
| **Document/Data unit** | `Document` | `Document` / `TextNode` | — | — | `Document` |
| **Text chunking** | `TextSplitter` | `NodeParser` / `SentenceSplitter` | — | — | — |
| **Document loader** | `BaseDocumentLoader` | `SimpleDirectoryReader` | — | — | — |
| **Embeddings** | `BaseEmbeddings` | `Embedding` | `embedder` config | — | `*DocumentEmbedder` |
| **Vector index** | `VectorStore` | `VectorStoreIndex` | — | — | `DocumentStore` |
| **Retriever** | `BaseRetriever` | `BaseRetriever` | — | `ColBERTv2` | `Retriever` component |
| **Agent** | `create_agent` / `AgentExecutor` | `AgentWorkflow` | `Agent` | `dspy.Module` + `ReAct` | Pipeline + `OpenAIChatGenerator` |
| **Tool** | `BaseTool` / `@tool` | LlamaHub tools | `BaseTool` | Python function | `@component` function |
| **Orchestration** | `RunnableSequence` / LCEL | `Workflow` / `IngestionPipeline` | `Crew` + `Process` | `dspy.Module.forward()` | `Pipeline` |
| **Memory** | `BaseChatMessageHistory` | `AgentWorkflow` state | `Memory` / `MemoryScope` | — | — |
| **Output parsing** | `BaseOutputParser` | `ResponseSynthesizer` | `TaskOutput` | `Prediction` | Component outputs |
| **Prompt** | `ChatPromptTemplate` | LLM prompt templates | `system_template` | `Signature` | `PromptBuilder` |
| **Optimization** | LCEL compose | — | — | `MIPROv2` / `BootstrapFewShot` | — |
| **Structured output** | `PydanticOutputParser` | — | `output_pydantic` | Class-based `Signature` | — |
| **Validation/Guards** | — | — | `guardrail` param | — | `ConditionalRouter` |
| **Streaming** | `Runnable.stream()` | `AgentWorkflow` events | `CrewStreamingOutput` | — | `AsyncPipeline` |
| **Config/Settings** | env vars + init | `Settings` | YAML config | `dspy.configure()` | YAML serialization |

---

## CEX Kind Validation

| CEX Kind | Framework Class(es) | Match Quality | Official URL |
|---|---|---|---|
| `Document` | LangChain `Document`, LlamaIndex `Document`, Haystack `Document` | ✅ Exact — universal primitive | Multiple |
| `Node` | LlamaIndex `TextNode` / `Node` | ✅ Exact | docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/ |
| `Tool` | LangChain `BaseTool`, CrewAI `BaseTool`, LlamaHub tools | ✅ Exact | python.langchain.com, docs.crewai.com/concepts/tools |
| `Retriever` | LangChain `BaseRetriever`, LlamaIndex `BaseRetriever`, Haystack `Retriever` | ✅ Exact — universal | Multiple |
| `Pipeline` | Haystack `Pipeline`, LlamaIndex `IngestionPipeline` | ✅ Exact | docs.haystack.deepset.ai/docs/pipelines |
| `Agent` | LangChain `create_agent`, LlamaIndex `AgentWorkflow`, CrewAI `Agent` | ✅ Exact | Multiple |
| `Memory` | CrewAI `Memory` / `MemoryScope`, LangChain `BaseChatMessageHistory` | ✅ Exact | docs.crewai.com/concepts/memory |
| `Signature` | DSPy `Signature` | ✅ Exact — DSPy-native | dspy.ai/learn/programming/signatures/ |
| `Optimizer` | DSPy `MIPROv2`, `BootstrapFewShot`, etc. | ✅ Exact — DSPy-native | dspy.ai/learn/optimization/optimizers/ |
| `Guard` | Guardrails `Guard`, CrewAI `guardrail` param | ✅ Exact | guardrailsai.com/docs/concepts/guard |
| `Crew` | CrewAI `Crew` | ✅ Exact | docs.crewai.com/concepts/crews |
| `Workflow` | LlamaIndex `Workflow`, CrewAI `Flow` | ✅ Exact | docs.llamaindex.ai |
| `Component` | Haystack `@component` | ✅ Exact | docs.haystack.deepset.ai/docs/components |
| `Validator` | Guardrails `Validator`, Instructor `Validator` | ✅ Exact | guardrailsai.com/docs |
| `OutputParser` | LangChain `BaseOutputParser` | ✅ Exact | python.langchain.com/docs/concepts/ |
| `Embedder` | LlamaIndex `Embedding`, Haystack `*DocumentEmbedder`, CrewAI `embedder` | ✅ Strong | Multiple |
| `StructuredOutput` | Instructor `response_model`, Outlines model callable, DSPy class Signature | ✅ Concept-level | Multiple |
