---
id: atom_07_llamaindex
kind: knowledge_card
pillar: P01
title: "ATOM-07: LlamaIndex Framework -- Complete Vocabulary Atlas"
version: 1.1.0
date: 2026-04-13
quality: 8.8
tags: [llamaindex, rag, framework, vocabulary, atlas, llm, agents, workflows, propertygraph, agentworkflow, llamaparse-v2]
sources:
  - https://developers.llamaindex.ai/python/framework/
  - https://github.com/run-llama/llama_index
  - https://developers.llamaindex.ai/python/cloud/
  - https://deepwiki.com/run-llama/llama_index
  - https://developers.llamaindex.ai/python/framework/understanding/agent/multi_agent/
  - https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/
  - https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/
  - https://developers.llamaindex.ai/python/examples/workflow/checkpointing_workflows/
  - https://developers.llamaindex.ai/python/framework/understanding/evaluating/evaluating/
scope: "Complete vocabulary extraction: 300+ classes, 7-stage pipeline, 6 orchestration systems, AgentWorkflow deep dive, PropertyGraphIndex extractors+retrievers, LlamaParse v2 full API, WorkflowCheckpointer, evaluator scoring formulas"
related:
  - p01_kc_llamaindex_patterns
  - atom_05_semantic_kernel
  - atom_12_dify
  - p01_kc_document_loader
  - p01_emb_openai_text_embedding_3_small
  - bld_architecture_document_loader
  - bld_architecture_embedding_config
  - p06_arch_rag_pipeline
  - bld_collaboration_embedding_config
  - atom_10_haystack_vercel
---

# ATOM-07: LlamaIndex Framework -- Complete Vocabulary Atlas

> LlamaIndex is the leading document agent and OCR platform.
> Core repo: `run-llama/llama_index`. Python-first, TypeScript port.
> 300+ integration packages. Modular architecture since v0.10+.

---

## 1. Package Architecture

### Meta Package

| Package | Purpose |
|---------|---------|
| `llama-index` | Starter bundle (core + OpenAI defaults) |
| `llama-index-core` | Foundation: all base abstractions |
| `llama-index-cli` | CLI tooling |

### Integration Naming Convention

```
llama-index-{category}-{provider}
```

| Category | Examples |
|----------|----------|
| `llms` | `openai`, `anthropic`, `ollama`, `azure-openai`, `bedrock-converse`, `google-genai`, `minimax` |
| `embeddings` | `openai`, `fireworks`, `upstage`, `bedrock`, `huggingface` |
| `vector-stores` | `chroma`, `qdrant`, `pinecone`, `milvus`, `postgres`, `faiss`, `weaviate`, `azureaisearch`, `redis`, `solr`, `couchbase`, `lancedb` |
| `readers` | `file`, `docling`, `layoutir`, `kibela`, `web` |
| `graph-stores` | `neo4j`, `kuzu`, `nebula`, `falkordb` |
| `agent` | Various agent implementations |
| `callbacks` | Observability (Langfuse, Arize, etc.) |
| `ingestion` | `ray` (distributed pipeline) |
| `retrievers` | `bm25`, various custom retrievers |

---

## 2. Seven-Stage Pipeline Architecture

```
INGEST --> TRANSFORM --> EMBED --> STORE --> INDEX --> RETRIEVE --> SYNTHESIZE
  |           |           |         |         |          |            |
Reader    NodeParser  Embedding  Storage   Index    Retriever   Response
                                 Context            + Query     Synthesizer
                                                     Engine
```

---

## 3. Schema & Data Primitives

Module: `llama_index.core.schema`

### Document

| Class | Description |
|-------|-------------|
| `Document` | Generic container around any data source (PDF, API, DB). Stores text + metadata + relationships. |

Key attributes:
- `text` -- raw content
- `metadata` -- annotations dict
- `relationships` -- connections to other Documents/Nodes
- `doc_id` -- unique identifier
- `embedding` -- optional pre-computed vector

### Node Hierarchy

| Class | Parent | Description |
|-------|--------|-------------|
| `BaseNode` | -- | Abstract base for all nodes |
| `TextNode` | BaseNode | Text chunk with metadata + relationships |
| `ImageNode` | BaseNode | Image-based chunk |
| `IndexNode` | TextNode | Reference node pointing to an index |

### Node Relationships

| Enum / Class | Purpose |
|--------------|---------|
| `NodeRelationship` | Enum: SOURCE, PREVIOUS, NEXT, PARENT, CHILD |
| `RelatedNodeInfo` | Stores node_id + metadata for a relationship |
| `MetadataMode` | Controls metadata visibility: ALL, NONE, LLM, EMBED |
| `ObjectType` | Classification system for schema objects |

### Query & Response

| Class | Purpose |
|-------|---------|
| `QueryBundle` | Query string + optional pre-computed embedding |
| `Response` | Answer text + source_nodes attribution |

---

## 4. Data Loading (Readers)

Module: `llama_index.core.readers`

### Core Readers

| Class | Description |
|-------|-------------|
| `BaseReader` | Abstract interface for all data connectors |
| `SimpleDirectoryReader` | Local file loader, auto-selects parser by extension. Supports `fs` param for remote filesystems (S3, Azure, GDrive via fsspec). |
| `SimpleWebPageReader` | Web page to Document |
| `LlamaParseReader` | Cloud-powered document parsing (see Section 13) |

### LlamaHub

Community connector registry: 160+ data sources.
Import pattern: `from llama_index.readers.{source} import {Reader}`

---

## 5. Node Parsers (Transformation / Chunking)

Module: `llama_index.core.node_parser`

### Text Splitters

| Class | Strategy | Key Params |
|-------|----------|------------|
| `SentenceSplitter` | Respects sentence boundaries. Default chunker. | `chunk_size`, `chunk_overlap` |
| `TokenTextSplitter` | Raw token count splitting | `chunk_size`, `chunk_overlap`, `separator` |
| `SemanticSplitterNodeParser` | Adaptive breakpoints via embedding similarity | `buffer_size`, `breakpoint_percentile_threshold`, `embed_model` |
| `SentenceWindowNodeParser` | Individual sentences + surrounding window in metadata | `window_size`, `window_metadata_key`, `original_text_metadata_key` |
| `HierarchicalNodeParser` | Multi-level parent-child hierarchy | `chunk_sizes` (list of levels) |
| `CodeSplitter` | Language-aware code splitting | `language`, `chunk_lines`, `chunk_lines_overlap`, `max_chars` |
| `LangchainNodeParser` | Wraps LangChain text splitters | -- |
| `Chunker` | Wraps chonkie chunking strategies | strategy alias, `chunk_size` |

### File-Based Parsers

| Class | Format |
|-------|--------|
| `SimpleFileNodeParser` | Auto-selects by content type |
| `HTMLNodeParser` | Raw HTML via BeautifulSoup. Tags: `p, h1-h6, li, b, i, u, section` |
| `JSONNodeParser` | Raw JSON |
| `MarkdownNodeParser` | Markdown text |

### Post-Processors

| Class | Purpose |
|-------|---------|
| `MetadataReplacementNodePostProcessor` | Replaces node text with metadata (e.g., sentence window context) |
| `SimilarityPostprocessor` | Filters by similarity score threshold |
| `KeywordNodePostprocessor` | Include/exclude by keywords |
| `LongContextReorder` | Reorders nodes for "lost in the middle" mitigation |
| `CohereRerank` | Cohere reranking |
| `SentenceTransformerRerank` | Cross-encoder reranking |
| `LLMRerank` | LLM-based reranking |

---

## 6. Embeddings

Module: `llama_index.core.embeddings`

| Class | Description |
|-------|-------------|
| `BaseEmbedding` | Abstract text-to-vector interface |
| `OpenAIEmbedding` | OpenAI embedding models |
| `HuggingFaceEmbedding` | Local HF models |
| `CohereEmbedding` | Cohere embedding API |
| `OllamaEmbedding` | Ollama local embedding |

---

## 7. Index Types

Module: `llama_index.core.indices`

### Base

| Class | Description |
|-------|-------------|
| `BaseIndex` | Abstract base. Location: `llama_index.core.indices.base.BaseIndex` |

### Built-in Index Types

| Index | Mechanism | Query Pattern |
|-------|-----------|---------------|
| `VectorStoreIndex` | Stores Node + embedding in vector store | Top-k similarity search --> ResponseSynthesizer |
| `SummaryIndex` (formerly ListIndex) | Sequential chain of Nodes | Load all or top-k by embedding/keyword filter |
| `TreeIndex` | Hierarchical tree (Nodes = leaves) | Root-to-leaf traversal. `child_branch_factor` controls breadth. |
| `KeywordTableIndex` | Keyword-to-Node mapping | Extract query keywords --> match pre-extracted Node keywords |
| `PropertyGraphIndex` | Labeled knowledge graph with optional embeddings | Combines keyword expansion + vector retrieval over triples |
| `KnowledgeGraphIndex` | Legacy graph index | Entity-relation extraction |
| `DocumentSummaryIndex` | Per-document summaries + nodes | Summary-based retrieval then drill into nodes |

### Integration Index Types

| Index | Provider |
|-------|----------|
| `LlamaCloudIndex` | LlamaCloud managed |
| `VectaraIndex` | Vectara |
| `LanceDBIndex` | LanceDB |
| `PostgresMLIndex` | PostgresML |
| `GoogleIndex` | Google Vertex AI |

### Index Methods (all indices)

| Method | Returns |
|--------|---------|
| `.as_query_engine()` | `RetrieverQueryEngine` |
| `.as_chat_engine()` | Chat engine (modes: BEST, CONTEXT, CONDENSE_QUESTION, CONDENSE_PLUS_CONTEXT, SIMPLE) |
| `.as_retriever()` | Index-specific `BaseRetriever` |

---

## 8. Storage

Module: `llama_index.core.storage`

### StorageContext

Central manager for all persistence. Created via `StorageContext.from_defaults()`.

| Parameter | Type | Purpose |
|-----------|------|---------|
| `docstore` | BaseDocumentStore | Document storage |
| `index_store` | BaseIndexStore | Index metadata |
| `vector_store` | BasePydanticVectorStore | Single vector store |
| `vector_stores` | dict | Multiple named vector stores |
| `image_store` | -- | Image storage |
| `graph_store` | -- | Graph database |
| `property_graph_store` | -- | Property graph DB |
| `persist_dir` | str | Local persistence directory |

### Store Implementations

| Class | Backend |
|-------|---------|
| `SimpleDocumentStore` | In-memory / JSON file |
| `SimpleIndexStore` | In-memory / JSON file |
| `SimpleVectorStore` | In-memory / JSON file |
| `MongoDocumentStore` | MongoDB |
| `RedisDocumentStore` | Redis |
| `ChatStore` | Persistent chat message history |

### Vector Store Integrations

| Class | Provider |
|-------|----------|
| `ChromaVectorStore` | Chroma |
| `QdrantVectorStore` | Qdrant |
| `PineconeVectorStore` | Pinecone |
| `MilvusVectorStore` | Milvus / Zilliz |
| `FaissVectorStore` | FAISS |
| `WeaviateVectorStore` | Weaviate |
| `PGVectorStore` | PostgreSQL pgvector |
| `RedisVectorStore` | Redis |
| `AzureAISearchVectorStore` | Azure AI Search |
| `OpensearchVectorStore` | OpenSearch |
| `LanceDBVectorStore` | LanceDB |

Properties: `stores_text`, `flat_metadata`, `collection_name`, `host`, `port`, `ssl`, `headers`, `persist_dir`

---

## 9. Retriever Types

Module: `llama_index.core.retrievers`

### Base

| Class | Description |
|-------|-------------|
| `BaseRetriever` | Abstract interface. Returns `List[NodeWithScore]` |

### Built-in Retrievers

| Retriever | Source | Mechanism |
|-----------|--------|-----------|
| `VectorIndexRetriever` | VectorStoreIndex | Top-k similarity search |
| `KeywordTableLLMRetriever` | KeywordTableIndex | LLM extracts keywords from query |
| `KeywordTableSimpleRetriever` | KeywordTableIndex | Frequency-based keyword extraction |
| `KeywordTableRAKERetriever` | KeywordTableIndex | RAKE algorithm keyword extraction |
| `TreeSelectLeafRetriever` | TreeIndex | Root-to-leaf traversal |
| `TreeAllLeafRetriever` | TreeIndex | Returns all leaf nodes |
| `SummaryIndexRetriever` | SummaryIndex | Returns all nodes sequentially |
| `SummaryIndexEmbeddingRetriever` | SummaryIndex | Top-k by embedding similarity |
| `SummaryIndexLLMRetriever` | SummaryIndex | LLM selects relevant nodes |
| `AutoMergingRetriever` | HierarchicalNodeParser | Merges child nodes into parent when majority retrieved |
| `RouterRetriever` | Multiple | LLM selects which sub-retriever to use |
| `RecursiveRetriever` | IndexNode | Follows IndexNode references recursively |
| `BM25Retriever` | Integration | BM25 (Best Matching 25) keyword ranking |
| `QueryFusionRetriever` | Multiple | Generates multiple queries, fuses results |

---

## 10. Query Engines

Module: `llama_index.core.query_engine`

### Base

| Class | Description |
|-------|-------------|
| `BaseQueryEngine` | Abstract. Orchestrates retrieval + synthesis |

### Built-in Query Engines

| Engine | Mechanism |
|--------|-----------|
| `RetrieverQueryEngine` | Wraps Retriever + ResponseSynthesizer into pipeline |
| `SubQuestionQueryEngine` | Decomposes query into sub-questions, answers each via QueryEngineTool, combines |
| `RouterQueryEngine` | LLM routes query to best sub-engine |
| `MultiStepQueryEngine` | Iterative query refinement across steps |
| `CitationQueryEngine` | Adds source citations to responses |
| `PandasQueryEngine` | Natural language --> Pandas DataFrame queries |
| `SQLTableRetrieverQueryEngine` | NL --> SQL queries |
| `NLSQLTableQueryEngine` | Natural language to SQL |
| `KnowledgeGraphQueryEngine` | Queries over knowledge graph |
| `RetryQueryEngine` | Retries with evaluation feedback |
| `RetrySourceQueryEngine` | Retries with source filtering |
| `RetryGuidelineQueryEngine` | Retries with guideline feedback |
| `FLAREInstructQueryEngine` | FLARE retrieval-augmented generation |
| `JSONQueryEngine` | NL queries over JSON data |
| `CustomQueryEngine` | User-defined (subclass and override `custom_query`) |

---

## 11. Response Synthesis

Module: `llama_index.core.response_synthesizers`

### Base

| Class | Description |
|-------|-------------|
| `BaseSynthesizer` | Abstract response synthesizer |

### Response Modes

| Mode | Behavior | LLM Calls |
|------|----------|-----------|
| `compact` (default) | Concatenate chunks to fit context, then refine | Fewer (packed) |
| `refine` | Sequential: query + chunk1 --> answer1, answer1 + chunk2 --> answer2, ... | N-1 (one per chunk) |
| `tree_summarize` | Recursive summarization tree until single answer | Log(N) |
| `simple_summarize` | Truncate all chunks to single prompt | 1 |
| `accumulate` | Apply query to each chunk separately, accumulate | N |
| `compact_accumulate` | Pack chunks then accumulate | Fewer than N |
| `no_text` | Retrieval only, no LLM call. Inspect via `response.source_nodes` | 0 |
| `context_only` | Return concatenated chunk text, no LLM | 0 |

### Factory

```python
get_response_synthesizer(response_mode="compact", streaming=False)
```

Options: `response_mode`, `structured_answer_filtering`, custom `PromptTemplate`, `streaming`

---

## 12. Configuration & Settings

### Settings (Global Singleton)

Module: `llama_index.core.settings`

```python
from llama_index.core import Settings
Settings.llm = OpenAI(model="gpt-4")
Settings.embed_model = OpenAIEmbedding()
Settings.chunk_size = 1024
Settings.chunk_overlap = 20
```

Replaces deprecated `ServiceContext`.

### ServiceContext (DEPRECATED)

Legacy configuration container. Params: `llm`, `embed_model`, `chunk_size`, `chunk_overlap`, `node_parser`, `callback_manager`.

Replaced by `Settings` singleton in v0.10+.

---

## 13. Ingestion Pipeline

Module: `llama_index.core.ingestion`

### Core Classes

| Class | Purpose |
|-------|---------|
| `IngestionPipeline` | Sequential transformation pipeline with caching + dedup |
| `IngestionCache` | Wrapper for cache backends (node+transform pairs) |
| `TransformComponent` | Base class for all pipeline stages |

### Pipeline Configuration

```python
pipeline = IngestionPipeline(
    transformations=[SentenceSplitter(), OpenAIEmbedding()],
    vector_store=QdrantVectorStore(...),
    cache=IngestionCache(cache=RedisCache(...)),
    docstore=SimpleDocumentStore(),
)
```

| Parameter | Purpose |
|-----------|---------|
| `transformations` | Ordered list of TransformComponent |
| `vector_store` | Direct node insertion target |
| `cache` | IngestionCache for dedup |
| `docstore` | Document dedup via doc_id + content hash |
| `num_workers` | Parallel processing via multiprocessing.Pool |

### Execution

| Method | Mode |
|--------|------|
| `pipeline.run(documents=[...])` | Synchronous |
| `pipeline.arun(documents=[...])` | Asynchronous |
| `pipeline.persist()` / `pipeline.load()` | Local cache persistence |
| `cache.clear()` | Cache deletion |

### Cache Backends

| Backend | Class |
|---------|-------|
| Local file | Default (persist/load) |
| Redis | `RedisCache` |
| MongoDB | `MongoDBCache` |
| Firestore | `FirestoreCache` |

### Metadata Extractors (Pipeline Transforms)

| Class | Extracts |
|-------|----------|
| `TitleExtractor` | Document titles |
| `QuestionsAnsweredExtractor` | Questions the node can answer |
| `SummaryExtractor` | Node summaries |
| `KeywordExtractor` | Keywords |
| `EntityExtractor` | Named entities |

---

## 14. Agents

Module: `llama_index.core.agent`

### Agent Types

| Class | Mechanism | When to Use |
|-------|-----------|-------------|
| `FunctionAgent` | Native LLM function/tool calling API | LLMs with tool calling (OpenAI, Anthropic, Gemini) |
| `ReActAgent` | Reason + Act prompting loop | Any LLM, no function-calling needed |
| `CodeActAgent` | Code-based action execution | Code generation agents |
| `StructuredPlannerAgent` | Decomposes input into sub-tasks, wraps any AgentWorker | Complex multi-step planning |

### Agent Architecture

```
AgentRunner (orchestrator, state, memory, high-level interface)
    |
    +-- AgentWorker (step execution, tool calling)
            |
            +-- Tools (FunctionTool, QueryEngineTool, etc.)
```

| Class | Role |
|-------|------|
| `AgentRunner` | Orchestrator: manages state, memory, creates tasks, runs steps |
| `AgentWorker` | Executor: performs individual steps, calls tools |

### Tool Types

| Class | Description |
|-------|-------------|
| `BaseTool` | Abstract tool interface |
| `FunctionTool` | Wraps any Python function as a tool |
| `QueryEngineTool` | Wraps a QueryEngine for agent use |
| `RetrieverTool` | Wraps a Retriever for agent use |
| `ToolSpec` | Pre-defined tool collection for common APIs |

### Multi-Agent (AgentWorkflow)

| Class | Purpose |
|-------|---------|
| `AgentWorkflow` | Multi-agent orchestration with handoff coordination |
| `BaseWorkflowAgent` | Base class for FunctionAgent and ReActAgent |
| `ChatMemoryBuffer` | Default memory for agents |
| `ChatMessage` | Message object (supports multimodal: TextBlock, ImageBlock) |

### Agent Handoff Pattern

Agents can hand off control to other agents in an AgentWorkflow.
Each agent declares which other agents it can hand off to.

---

## 15. Workflow System (Event-Driven)

Module: `llama_index.core.workflow`

### Core Classes

| Class | Purpose |
|-------|---------|
| `Workflow` | Base class. Contains @step-decorated methods. |
| `Event` | User-defined Pydantic objects carrying data between steps |
| `StartEvent` | Framework entry event. Accepts arbitrary kwargs. |
| `StopEvent` | Framework exit event. Terminates execution. |
| `Context` | Global state management across steps |
| `WorkflowCheckpointer` | Checkpoint and resume workflow execution |

### Decorators

| Decorator | Purpose |
|-----------|---------|
| `@step` | Marks method as workflow step. Auto-infers input/output event types from signature. |

### Execution

| Method | Behavior |
|--------|----------|
| `workflow.run(**kwargs)` | Async execution with keyword args via StartEvent |
| `timeout` param | Execution time limit (seconds) |
| `verbose` param | Debug logging |

### Context Methods

| Method | Purpose |
|--------|---------|
| `ctx.store.set(key, value)` | Store state |
| `ctx.store.get(key)` | Retrieve state |
| `ctx.collect_events()` | Accumulate events until all required are received |
| `ctx.send_event(event)` | Emit event to trigger next step |

### Control Flow

- Steps are triggered by typed Events (not explicit edges)
- Loops and branches encoded as vanilla Python (not graph edges)
- Concurrent step execution supported
- DAGs are a subset (Workflows are more general)

### Advanced Patterns

| Pattern | Description |
|---------|-------------|
| Human-in-the-Loop | Stateful pause/resume for user interaction |
| Durable Workflows | DBOS integration for fault-tolerant execution |
| Streaming Events | Event streaming from running workflows |
| Workflow composition | Nested workflows as steps |

---

## 16. Evaluation

Module: `llama_index.core.evaluation`

### Evaluator Types

| Class | Measures |
|-------|----------|
| `FaithfulnessEvaluator` | Is answer faithful to retrieved context? (hallucination detection) |
| `RelevancyEvaluator` | Is retrieved context relevant to query? |
| `CorrectnessEvaluator` | Does answer match reference? (requires labels) |
| `GuidelineEvaluator` | Does response follow custom guidelines? |
| `SemanticSimilarityEvaluator` | Embedding similarity between response and reference |
| `AnswerRelevancyEvaluator` | Is answer relevant to the query? |
| `ContextRelevancyEvaluator` | Is context relevant? |
| `PairwiseComparisonEvaluator` | Compare two responses |

### Batch Execution

| Class | Purpose |
|-------|---------|
| `BatchEvalRunner` | Run multiple evaluations asynchronously. `num_workers` controls concurrency. |

### Evaluation Output

Fields: `query`, `contexts`, `response`, `passing` (bool), `feedback` (text), `score` (float)

---

## 17. Observability & Callbacks

| Class | Purpose |
|-------|---------|
| `CallbackManager` | Central event dispatcher |
| `LlamaDebugHandler` | Built-in debug logging |
| `TokenCountingHandler` | Token usage tracking |
| `WandbCallbackHandler` | Weights & Biases integration |
| `AimCallback` | Aim tracking |

Integrations: Langfuse, Arize Phoenix, OpenLLMetry, Traceloop, DeepEval

---

## 18. LlamaCloud Platform

Cloud-hosted services from LlamaIndex Inc.

### Services

| Service | Purpose |
|---------|---------|
| `LlamaParse` | Agentic OCR and parsing (130+ formats) |
| `LlamaExtract` | Structured data extraction via custom schemas |
| `LlamaCloud Index` | Managed ingestion, chunking, embedding for RAG |
| `LlamaClassify` | Document categorization via NL rules |
| `LlamaSplit` | PDF segmentation into logical sections |
| `LlamaSheets` | Spreadsheet table and metadata extraction |

### SDK Classes

| Class | Purpose |
|-------|---------|
| `LlamaCloud` | Sync Python/TypeScript client |
| `AsyncLlamaCloud` | Async Python client |
| `LlamaCloudIndex` / `ManagedIndex` | Cloud-managed index |
| `LlamaCloudRetriever` | Cloud retrieval interface |

### SDK Methods

| Method | Purpose |
|--------|---------|
| `client.files.create()` | File upload |
| `client.parsing.parse()` | Parse operations |
| `client.extract.create()` | Extraction jobs |
| `client.pipelines.retrieve()` | Index querying |

### LlamaCloud Retrieval Params

| Parameter | Purpose |
|-----------|---------|
| `dense_similarity_top_k` | Dense vector top-k |
| `sparse_similarity_top_k` | Sparse retrieval top-k |
| `alpha` | Dense/sparse blend ratio |
| `reranking` | Reranker configuration |

---

## 19. LlamaParse (Document Parsing)

### Parsing Tiers

| Tier | Use Case | Cost |
|------|----------|------|
| `fast` | Quick text extraction, speed priority | Lowest |
| `cost_effective` | Mixed content, structured output | Low |
| `agentic` | Complex docs, high accuracy with reasoning | Medium |
| `agentic_plus` | Maximum fidelity: dense layouts, financial reports | Highest |

### API v2 Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/v2/parse` | JSON parse (file_id or source_url) |
| POST | `/api/v2/parse/upload` | Multipart file upload |
| GET | `/api/v2/parse` | List jobs (paginated) |
| GET | `/api/v2/parse/{job_id}` | Job status + results |

### Request Parameters

| Parameter | Type | Purpose |
|-----------|------|---------|
| `file_id` | str | Reference to uploaded file |
| `source_url` | str | URL to remote document |
| `tier` | enum | Processing tier |
| `version` | str | Parser version (latest, dated) |
| `disable_cache` | bool | Force reprocessing |
| `max_pages` | int | Page limit |
| `target_pages` | list | Specific pages (1-based) |
| `languages` | list | OCR language codes |
| `custom_prompt` | str | AI guidance (non-fast tiers) |

### Output Expand Options

| Option | Description |
|--------|-------------|
| `text` | Plain text |
| `markdown` | Markdown formatted |
| `items` | Structured items |
| `metadata` | Document metadata |
| `spatial_text` | Layout-preserving text |
| `tables_as_spreadsheet` | Table extraction |
| `embedded_images` | Image extraction |

### Markdown Options

`annotate_links`, `output_tables_as_markdown`, `compact_markdown_tables`, `markdown_table_multiline_separator`, `merge_continued_tables`

### Spatial Text Options

`preserve_layout_alignment_across_pages`, `preserve_very_small_text`, `do_not_unroll_columns`

### Job Status Values

`PENDING`, `RUNNING`, `COMPLETED`, `FAILED`, `CANCELLED`

### Webhook Config

`webhook_url`, `webhook_headers`, `webhook_events` (`parse.success`)

---

## 20. CEX Pillar Mapping

### P01 Knowledge (Storage, Retrieval, KCs)

| LlamaIndex Concept | CEX Equivalent | Notes |
|---------------------|----------------|-------|
| `Document` | Artifact (any .md file) | Container for content + metadata |
| `TextNode` | Chunk / Section | Atomic unit of knowledge |
| `VectorStoreIndex` | `cex_retriever.py` (TF-IDF index) | CEX uses TF-IDF; LlamaIndex uses dense vectors |
| `BaseReader` / `SimpleDirectoryReader` | `cex_compile.py --scan` | Document ingestion |
| `KnowledgeGraphIndex` | P01 library cross-references | Entity-relation mapping |
| `NodeParser` | Chunking (implicit in CEX) | CEX chunks by artifact boundaries |
| `IngestionPipeline` | 8F pipeline (F1-F3) | Sequential transformation of raw input |
| `IngestionCache` | `.cex/cache/` (prompt cache) | Dedup and acceleration |
| `Embedding` | `cex_retriever.py` TF-IDF vectors | CEX uses sparse; LlamaIndex uses dense |
| `MetadataExtractor` | YAML frontmatter extraction | Structured metadata per artifact |

### P04 Tools (External Capabilities)

| LlamaIndex Concept | CEX Equivalent | Notes |
|---------------------|----------------|-------|
| `FunctionTool` | `_tools/cex_*.py` (79 tools) | Callable capabilities |
| `QueryEngineTool` | `cex_query.py` (TF-IDF discovery) | Search over knowledge base |
| `ToolSpec` | Builder ISOs (13 per kind) | Pre-defined tool collections |
| `BaseTool` | Tool interface in `cex_sdk/` | Abstract capability |
| `LlamaParse` | `cex_compile.py` + `cex_hygiene.py` | Document processing pipeline |
| `AgentRunner` | `cex_mission_runner.py` | Orchestrated multi-step execution |
| `AgentWorkflow` | `_spawn/dispatch.sh grid` | Multi-agent parallel dispatch |

### P10 Memory (State, Context, Indexing)

| LlamaIndex Concept | CEX Equivalent | Notes |
|---------------------|----------------|-------|
| `StorageContext` | `.cex/runtime/` | Central state management |
| `SimpleDocumentStore` | `.cex/runtime/handoffs/` + signals | Document state tracking |
| `ChatMemoryBuffer` | `.cex/learning_records/` + memory/ | Conversation persistence |
| `VectorStore` | `.cex/cache/` + compiled/ | Indexed artifact storage |
| `IngestionCache` | `.cex/cache/prompt_cache` | 125 pre-compiled builder prompts |
| `Context` (Workflow) | `.cex/runtime/decisions/decision_manifest.yaml` | Cross-step state |
| `entity_memory` | `P10_memory/` + entity_memory artifacts | Named entity persistence |

### Additional Pillar Mappings

| LlamaIndex | CEX Pillar | Mapping |
|------------|------------|---------|
| `Workflow` / `@step` | P12 Orchestration | Event-driven multi-step execution |
| `FaithfulnessEvaluator` | P07 Evaluation | Quality gate scoring |
| `BatchEvalRunner` | `cex_score.py --apply` | Batch quality assessment |
| `ResponseSynthesizer` | F6 PRODUCE (8F) | Final output generation |
| `Settings` singleton | `.cex/config/` | Global configuration |
| `CallbackManager` | `cex_hooks.py` | Event interception |
| `Agent` (FunctionAgent/ReActAgent) | Nucleus (N01-N06) | Autonomous execution unit |
| `AgentWorkflow` handoff | `.cex/runtime/handoffs/` | Inter-agent task transfer |

---

## 21. Vocabulary Quick Reference (Alphabetical)

| Term | Category | Description |
|------|----------|-------------|
| `accumulate` | Response mode | Query each chunk separately, accumulate results |
| `AgentRunner` | Agent | Orchestrator: state, memory, task management |
| `AgentWorker` | Agent | Step executor, tool caller |
| `AgentWorkflow` | Agent | Multi-agent orchestration with handoffs |
| `AsyncLlamaCloud` | Cloud | Async Python client for LlamaCloud |
| `AutoMergingRetriever` | Retriever | Merges child nodes into parent |
| `BaseEmbedding` | Embedding | Abstract text-to-vector interface |
| `BaseIndex` | Index | Abstract base for all indices |
| `BaseLLM` | LLM | Language model interface |
| `BaseNode` | Schema | Abstract base for all nodes |
| `BaseQueryEngine` | Query | Abstract query orchestrator |
| `BaseReader` | Loading | Abstract data connector |
| `BaseRetriever` | Retrieval | Abstract node fetcher |
| `BaseSynthesizer` | Response | Abstract response generator |
| `BaseTool` | Agent | Abstract tool interface |
| `BatchEvalRunner` | Evaluation | Async batch evaluation runner |
| `BM25Retriever` | Retriever | BM25 keyword ranking |
| `CallbackManager` | Observability | Event dispatcher |
| `ChatMemoryBuffer` | Agent | Default agent memory |
| `ChatMessage` | Agent | Message (text/image blocks) |
| `ChatStore` | Storage | Persistent chat history |
| `ChromaVectorStore` | Vector Store | Chroma integration |
| `CitationQueryEngine` | Query | Adds source citations |
| `CodeActAgent` | Agent | Code-based action execution |
| `CodeSplitter` | NodeParser | Language-aware code chunking |
| `compact` | Response mode | Pack chunks, then refine |
| `Context` | Workflow | Cross-step state management |
| `CorrectnessEvaluator` | Evaluation | Reference-based answer scoring |
| `CustomQueryEngine` | Query | User-defined query engine |
| `Document` | Schema | Generic data container |
| `DocumentSummaryIndex` | Index | Per-document summary retrieval |
| `Event` | Workflow | Typed data carrier between steps |
| `FaissVectorStore` | Vector Store | FAISS integration |
| `FaithfulnessEvaluator` | Evaluation | Hallucination detection |
| `FLAREInstructQueryEngine` | Query | FLARE retrieval-augmented |
| `FunctionAgent` | Agent | Native function-calling agent |
| `FunctionCallingLLM` | LLM | Tool-calling LLM interface |
| `FunctionTool` | Agent | Python function as tool |
| `HierarchicalNodeParser` | NodeParser | Multi-level parent-child hierarchy |
| `HTMLNodeParser` | NodeParser | HTML via BeautifulSoup |
| `ImageBlock` | Agent | Image content in messages |
| `ImageNode` | Schema | Image-based chunk |
| `IndexNode` | Schema | Reference to another index |
| `IngestionCache` | Ingestion | Node+transform caching |
| `IngestionPipeline` | Ingestion | Sequential transformation pipeline |
| `JSONNodeParser` | NodeParser | JSON document parser |
| `JSONQueryEngine` | Query | NL over JSON data |
| `KeywordTableIndex` | Index | Keyword-to-node mapping |
| `KnowledgeGraphIndex` | Index | Entity-relation graph |
| `LangchainNodeParser` | NodeParser | LangChain splitter wrapper |
| `LlamaClassify` | Cloud | Document categorization |
| `LlamaCloud` | Cloud | Sync client |
| `LlamaCloudIndex` | Cloud | Managed index |
| `LlamaCloudRetriever` | Cloud | Cloud retrieval |
| `LlamaExtract` | Cloud | Structured extraction |
| `LlamaParse` | Cloud | Agentic OCR/parsing |
| `LlamaSheets` | Cloud | Spreadsheet extraction |
| `LlamaSplit` | Cloud | PDF segmentation |
| `ManagedIndex` | Cloud | Cloud-managed index |
| `MarkdownNodeParser` | NodeParser | Markdown parser |
| `MetadataMode` | Schema | ALL, NONE, LLM, EMBED |
| `MetadataReplacementNodePostProcessor` | PostProcessor | Replace text with metadata |
| `MilvusVectorStore` | Vector Store | Milvus integration |
| `MultiStepQueryEngine` | Query | Iterative refinement |
| `NLSQLTableQueryEngine` | Query | Natural language to SQL |
| `NodeRelationship` | Schema | SOURCE, PREVIOUS, NEXT, PARENT, CHILD |
| `PandasQueryEngine` | Query | NL to Pandas |
| `PGVectorStore` | Vector Store | PostgreSQL pgvector |
| `PineconeVectorStore` | Vector Store | Pinecone integration |
| `PropertyGraphIndex` | Index | Labeled knowledge graph |
| `QdrantVectorStore` | Vector Store | Qdrant integration |
| `QueryBundle` | Schema | Query string + embedding |
| `QueryEngineTool` | Agent | Query engine as tool |
| `QueryFusionRetriever` | Retriever | Multi-query fusion |
| `ReActAgent` | Agent | Reason+Act prompting |
| `RecursiveRetriever` | Retriever | Follow IndexNode references |
| `RedisVectorStore` | Vector Store | Redis integration |
| `refine` | Response mode | Sequential chunk-by-chunk refinement |
| `RelatedNodeInfo` | Schema | Relationship metadata |
| `RelevancyEvaluator` | Evaluation | Context relevancy scoring |
| `Response` | Schema | Answer + source_nodes |
| `RetrieverQueryEngine` | Query | Retriever + Synthesizer pipeline |
| `RetrieverTool` | Agent | Retriever as tool |
| `RetryQueryEngine` | Query | Retry with eval feedback |
| `RouterQueryEngine` | Query | LLM routes to sub-engine |
| `RouterRetriever` | Retriever | LLM selects sub-retriever |
| `SemanticSplitterNodeParser` | NodeParser | Embedding-based breakpoints |
| `SentenceSplitter` | NodeParser | Sentence-boundary chunking |
| `SentenceWindowNodeParser` | NodeParser | Sentence + context window |
| `Settings` | Config | Global singleton (replaces ServiceContext) |
| `SimpleDirectoryReader` | Reader | Local file loader |
| `SimpleDocumentStore` | Storage | In-memory/JSON doc store |
| `SimpleFileNodeParser` | NodeParser | Auto-selects by format |
| `simple_summarize` | Response mode | Truncate all to single prompt |
| `StartEvent` | Workflow | Entry event |
| `StopEvent` | Workflow | Exit event |
| `StorageContext` | Storage | Central persistence manager |
| `StructuredLLM` | LLM | Structured output support |
| `StructuredPlannerAgent` | Agent | Multi-step task decomposition |
| `SubQuestionQueryEngine` | Query | Decompose into sub-questions |
| `SummaryIndex` | Index | Sequential node chain |
| `TextBlock` | Agent | Text content in messages |
| `TextNode` | Schema | Text chunk with metadata |
| `TokenTextSplitter` | NodeParser | Raw token count splitting |
| `ToolSpec` | Agent | Pre-defined tool collection |
| `TransformComponent` | Ingestion | Pipeline stage base class |
| `tree_summarize` | Response mode | Recursive summarization tree |
| `TreeIndex` | Index | Hierarchical tree structure |
| `VectorStoreIndex` | Index | Embedding-based similarity search |
| `WeaviateVectorStore` | Vector Store | Weaviate integration |
| `Workflow` | Workflow | Event-driven execution engine |
| `WorkflowCheckpointer` | Workflow | Checkpoint/resume |

---

## 22. Key Architectural Patterns

| Pattern | Implementation |
|---------|----------------|
| Plugin architecture | Integration packages inherit core base classes |
| Global config singleton | `Settings` replaces per-component ServiceContext |
| Multi-layer storage | Document store + Index store + Vector store + Chat store |
| Async-first | Comprehensive async/await throughout pipeline |
| Convention over configuration | Import core = `.core.`; integrations omit it |
| Event-driven orchestration | Workflow @step + typed Events |
| Tool abstraction | Any function/engine/retriever wrappable as agent tool |
| Hierarchical chunking | Parent-child node relationships + auto-merging retrieval |
| Hybrid retrieval | Dense (vector) + Sparse (BM25/keyword) fusion |

---

*Research conducted 2026-04-13. Sources: LlamaIndex OSS docs, GitHub, LlamaCloud docs, DeepWiki, community articles.*

---

## 23. AgentWorkflow -- Deep Implementation Reference

Source: https://developers.llamaindex.ai/python/framework/understanding/agent/multi_agent/

### AgentWorkflow Constructor

```python
from llama_index.core.agent.workflow import AgentWorkflow, FunctionAgent, ReActAgent

workflow = AgentWorkflow(
    agents=[agent1, agent2, agent3],
    root_agent="agent1",
    initial_state={},
    state_prompt="Current state: {state}\nUser: {msg}",
    timeout=None,
    verbose=False,
)
```

### FunctionAgent / ReActAgent Parameters

Both inherit from `BaseWorkflowAgent`. Use `FunctionAgent` for LLMs with native tool calls; `ReActAgent` for any LLM.

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | str | Agent identifier -- used in handoff routing |
| `description` | str | Capability summary -- injected into other agents' handoff tool description |
| `system_prompt` | str | Agent-specific prompt (merged with ChatHistory on activation) |
| `tools` | list[BaseTool] | Tools available to this agent |
| `can_handoff_to` | list[str] | Agent names this agent can transfer control to (defines collaboration graph) |
| `llm` | BaseLLM | LLM for this specific agent (overrides global Settings) |

### Handoff Mechanism Internals

```
1. Duty agent receives task
2. LLM decides: generate answer OR invoke handoff tool
3. Handoff tool matched from can_handoff_to list
4. handoff() sets ctx.next_agent = target_name
5. aggregate_tool_results() detects next_agent is set
6. setup_agent() activates new agent: merge system_prompt + ChatHistory
7. Loop restarts with new agent as duty agent
```

| Internal Method | Role |
|----------------|------|
| `init_run()` | Initialize Context + ChatMemory for session |
| `setup_agent()` | Extract system_prompt, merge with history, activate duty agent |
| `aggregate_tool_results()` | Consolidate tool outputs, detect handoff trigger |
| `handoff()` | Sets ctx.next_agent; auto-injected as tool at runtime |

### State Management

```python
workflow = AgentWorkflow(
    agents=[...],
    initial_state={"user_name": None, "task_status": "pending"},
    state_prompt="State: {state}\nUser message: {msg}",
)
# Agents read/write state via Context
state = await ctx.store.get("task_status")
await ctx.store.set("task_status", "in_progress")
```

### Topology Patterns

| Pattern | can_handoff_to config | Use Case |
|---------|----------------------|----------|
| Linear chain | A -> B -> C | Staged processing pipeline |
| Hub-and-spoke | Coordinator -> [N agents] | Specialized skill routing |
| Mesh | All -> all | Flexible peer negotiation |
| Hierarchical | Manager -> Sub-managers -> Workers | Enterprise multi-tier flows |

---

## 24. PropertyGraphIndex -- Deep Implementation Reference

Source: https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/

### Constructor Parameters

```python
from llama_index.core import PropertyGraphIndex

index = PropertyGraphIndex.from_documents(
    documents,
    kg_extractors=[SimpleLLMPathExtractor(llm=llm)],
    property_graph_store=Neo4jPropertyGraphStore(...),
    embed_model=OpenAIEmbedding(),
    embed_kg_nodes=True,
    show_progress=True,
)
```

### Knowledge Graph Extractors

| Class | Strategy | Schema Required? | Best For |
|-------|----------|-----------------|---------|
| `SimpleLLMPathExtractor` | LLM extracts (entity1, relation, entity2) triples | No | Exploratory RAG, wide coverage |
| `DynamicLLMPathExtractor` | Schema hints + free-form expansion | Optional | Rich diverse graph with some consistency |
| `SchemaLLMPathExtractor` | Strict allowed entity/relation types via Pydantic schema | Yes | Structured, consistent knowledge bases |
| `ImplicitPathExtractor` | Node relationships without LLM calls | No | Fast, metadata-only, no inference |

#### SimpleLLMPathExtractor Params

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `llm` | BaseLLM | Settings.llm | LLM for extraction |
| `max_paths_per_chunk` | int | 10 | Max triples per text chunk |
| `num_workers` | int | 4 | Async concurrency |
| `show_progress` | bool | False | Progress bar |

#### SchemaLLMPathExtractor Params

| Parameter | Type | Description |
|-----------|------|-------------|
| `possible_entities` | list[str] | Allowed entity type names |
| `possible_relations` | list[str] | Allowed relation type names |
| `possible_relation_props` | list[str] | Allowed relation property names |
| `strict` | bool | Reject triples outside schema if True |

### PropertyGraph Retrievers

| Retriever | Mechanism | Key Params |
|-----------|-----------|------------|
| `LLMSynonymRetriever` | LLM generates keywords/synonyms -> match node labels | `llm`, `max_keywords`, `path_depth` (int hops), `include_text` |
| `VectorContextRetriever` | Embed query -> cosine sim vs node embeddings -> fetch connected paths | `embed_model`, `similarity_top_k`, `path_depth`, `include_text`, `include_properties` |
| `TextToCypherRetriever` | LLM converts NL -> Cypher -> execute on graph store | `graph_schema`, `llm`, `cypher_validator` |
| `CypherTemplateRetriever` | Fill slots in predefined Cypher template (safer than TextToCypher) | `cypher_template`, `template_vars`, `llm` |

Default (if no sub_retrievers provided): `LLMSynonymRetriever` + `VectorContextRetriever` (when embeddings enabled).

### Graph Store Backends

| Class | Backend | Notes |
|-------|---------|-------|
| `SimplePropertyGraphStore` | In-memory | Dev/testing only |
| `Neo4jPropertyGraphStore` | Neo4j | Production; Cypher + vector search |
| `NebulaGraphStore` | NebulaGraph | Open-source distributed |
| `FalkorDBPropertyGraphStore` | FalkorDB | Redis-based graph DB |
| `KuzuPropertyGraphStore` | Kuzu | Embedded, no server required |
| `MemgraphPropertyGraphStore` | Memgraph | Bolt protocol, Cypher-compatible |

### Extraction + Retrieval Pipeline

```
Documents
  -> kg_extractors (attach entity/relation metadata to each TextNode)
  -> PropertyGraphStore (nodes: labeled entities + props; edges: relations + props)
  -> sub_retrievers (LLMSynonym + VectorContext in parallel)
  -> Retrieved (node_text, path_text, source_chunk)
  -> ResponseSynthesizer
  -> Final answer
```

---

## 25. WorkflowCheckpointer -- Complete Reference

Source: https://developers.llamaindex.ai/python/examples/workflow/checkpointing_workflows/

### Constructor

```python
from llama_index.core.workflow import WorkflowCheckpointer
checkpointer = WorkflowCheckpointer(workflow=my_workflow)
```

### Checkpoint Data Structure

| Field | Type | Description |
|-------|------|-------------|
| `last_completed_step` | str | Name of step that just finished |
| `input_event` | Event | Event that triggered the step |
| `output_event` | Event | Event emitted by the step |
| `ctx_snapshot` | bytes | Serialized Context state at checkpoint |
| `run_id` | str | UUID of the containing run |

### Run Methods

| Method | Description |
|--------|-------------|
| `checkpointer.run(**kwargs)` | Full async run with auto-checkpointing after every step. Returns handler with `run_id`. |
| `checkpointer.run_from(checkpoint, **kwargs)` | Resume from a checkpoint. Restores ctx_snapshot, skips already-completed steps. |

```python
# Full run
handler = checkpointer.run(query="What is X?")
result = await handler
run_id = handler.run_id

# Inspect checkpoints
all_ckpts = checkpointer.checkpoints          # dict[run_id -> list[Checkpoint]]
ckpts_for_run = checkpointer.checkpoints[run_id]

# Resume from checkpoint index 2
chosen_ckpt = ckpts_for_run[2]
new_handler = checkpointer.run_from(checkpoint=chosen_ckpt, query="What is X?")
result2 = await new_handler
```

### filter_checkpoints() Method

Multiple filters use AND semantics.

| Filter Param | Type | Matches by |
|-------------|------|------------|
| `last_completed_step` | str | Step name equality |
| `output_event_type` | type[Event] | Output event class |
| `input_event_type` | type[Event] | Input event class |

```python
ckpts = checkpointer.filter_checkpoints(
    last_completed_step="gather",
    output_event_type=ReadyEvent,
)
```

### Checkpoint Storage Backends

| Backend | Class | Durability |
|---------|-------|-----------|
| In-memory dict | Default | Lost on process exit |
| DBOS Postgres | `DBOSWorkflowCheckpointer` | Durable, fault-tolerant |
| Custom | Subclass `BaseWorkflowCheckpointer` | Implement `save()` + `load()` |

### Human-in-the-Loop Pattern

```python
# Suspend on awaiting approval
handler = checkpointer.run(query=query)
async for event in handler.stream_events():
    if isinstance(event, ApprovalNeededEvent):
        approval_ckpt = checkpointer.filter_checkpoints(
            output_event_type=ApprovalNeededEvent
        )[-1]
        break  # Suspend; persist approval_ckpt.run_id + index

# Later: resume with human feedback injected
handler = checkpointer.run_from(checkpoint=approval_ckpt, human_feedback="Approved.")
```

---

## 26. Evaluation -- Scoring Formulas and Internals

Source: https://developers.llamaindex.ai/python/framework/understanding/evaluating/evaluating/

### Per-Evaluator Scoring Details

| Evaluator | Score Type | Score Range | Passing Default | Formula |
|-----------|-----------|------------|----------------|---------|
| `FaithfulnessEvaluator` | Binary | {0.0, 1.0} | score == 1.0 | LLM: "Is response supported by context?" -> YES=1.0, NO=0.0 |
| `RelevancyEvaluator` | Binary | {0.0, 1.0} | score == 1.0 | LLM: "Does response + context match query?" -> YES=1.0, NO=0.0 |
| `CorrectnessEvaluator` | Continuous | 1.0 - 5.0 | >= 4.0 | LLM compares vs reference: 1=wrong, 3=partial, 5=perfect |
| `SemanticSimilarityEvaluator` | Continuous | 0.0 - 1.0 | >= 0.8 | cosine_similarity(embed(response), embed(reference)) |
| `AnswerRelevancyEvaluator` | Binary | {0.0, 1.0} | score == 1.0 | LLM: "Is answer directly relevant to the question?" |
| `ContextRelevancyEvaluator` | Binary | {0.0, 1.0} | score == 1.0 | LLM: "Is retrieved context relevant to query?" |
| `GuidelineEvaluator` | Binary | {0.0, 1.0} | score == 1.0 | LLM: evaluates response against user-defined guideline string |
| `PairwiseComparisonEvaluator` | Categorical | {1, 2, 0} | -- | LLM: A vs B -> 1=A wins, 2=B wins, 0=tie |

### EvaluationResult Fields

| Field | Type | Description |
|-------|------|-------------|
| `query` | str | Original query |
| `contexts` | list[str] | Source chunks used |
| `response` | str | Generated response text |
| `passing` | bool | True if score meets threshold |
| `feedback` | str | LLM explanation for score |
| `score` | float | Numeric score |
| `pairwise_source` | str | For PairwiseComparison: which response was evaluated |

### CorrectnessEvaluator Rubric (1-5)

| Score | Meaning |
|-------|---------|
| 1 | Completely incorrect, irrelevant, or missing |
| 2 | Mostly incorrect with minor relevant elements |
| 3 | Partially correct -- missing key aspects |
| 4 | Mostly correct, minor errors only |
| 5 | Perfectly correct and complete |

Default `score_threshold = 4.0` -> `passing = True`.

### BatchEvalRunner

```python
from llama_index.core.evaluation import BatchEvalRunner

runner = BatchEvalRunner(
    evaluators={
        "faithfulness": FaithfulnessEvaluator(),
        "relevancy": RelevancyEvaluator(),
        "correctness": CorrectnessEvaluator(),
    },
    workers=8,
    show_progress=True,
)

results = await runner.aevaluate_queries(
    query_engine,
    queries=["What is X?", "How does Y work?"],
)
# Access: results["faithfulness"][0].score
```

---

## 27. LlamaParse v2 -- Extended Parameter Reference

Source: https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/

### v2 vs v1 Key Differences

| Dimension | v1 | v2 |
|-----------|----|----|
| Mode selection | parsing_instruction + free-form | tier enum (fast/cost_effective/agentic/agentic_plus) |
| Output format | Mixed flat params | Structured expand query param |
| Config organization | Flat | Nested: input_options, output_options, processing_options |
| File upload | Always multipart | Upload file -> get file_id -> parse by ID |
| Version control | None | Explicit version string (e.g., "2024-12-01", "latest") |

### Full Request Parameter Reference

#### Top-Level (`POST /api/v2/parse` or `POST /api/v2/parse/upload`)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file_id` | str | One of | ID of pre-uploaded file |
| `source_url` | str | One of | Remote URL to parse directly |
| `tier` | enum | No | fast, cost_effective (default), agentic, agentic_plus |
| `version` | str | No | Parser version string ("latest" or date string) |
| `disable_cache` | bool | No | Force reprocess even if cached result exists |
| `max_pages` | int | No | Maximum pages to process |
| `target_pages` | list[int] | No | 1-based page numbers to process selectively |
| `custom_prompt` | str | No | AI guidance (agentic tiers only) |
| `webhook_url` | str | No | Callback URL on job completion |
| `webhook_headers` | dict | No | Headers for webhook POST |
| `webhook_events` | list[str] | No | Events: ["parse.success"] |

#### `input_options`

| Sub-parameter | Type | Description |
|---------------|------|-------------|
| `html.embed_extra_context` | bool | Embed surrounding HTML context into extracted text |
| `spreadsheet.sheet_names` | list[str] | Specific sheets to parse (default: all) |
| `spreadsheet.include_formulas` | bool | Include cell formulas in output |
| `presentation.include_slide_notes` | bool | Extract presenter notes from PPTX |

#### `output_options`

| Sub-parameter | Type | Description |
|---------------|------|-------------|
| `markdown.output_tables_as_markdown` | bool | Render tables as Markdown grid |
| `markdown.compact_markdown_tables` | bool | Remove padding whitespace in tables |
| `markdown.markdown_table_multiline_separator` | str | Separator for multiline cell content |
| `markdown.merge_continued_tables` | bool | Merge tables split across page breaks |
| `markdown.annotate_links` | bool | Include hyperlinks in Markdown output |
| `images_to_save` | list[str] | Extract: "screenshot", "figure", "table_image" |

#### `processing_options`

| Sub-parameter | Type | Description |
|---------------|------|-------------|
| `ignore.ignore_diagonal_text` | bool | Skip watermarks / rotated text |
| `ignore.ignore_headers_and_footers` | bool | Strip running headers and footers |
| `ignore.ignore_page_numbers` | bool | Strip page number lines |
| `ocr_parameters.languages` | list[str] | BCP-47 codes: ["fr", "de", "ja"] |
| `ocr_parameters.ocr_mode` | str | "auto" (default), "always", "never" |

### `expand` Query Parameter

Controls fields returned by `GET /api/v2/parse/{job_id}`. Multiple values comma-separated.

| Value | Returns |
|-------|---------|
| `text` | Plain text extraction |
| `markdown` | Markdown-formatted text |
| `items` | Structured items tree (JSON) |
| `metadata` | Document metadata (title, author, page count) |
| `spatial_text` | Layout-preserving text with coordinates |
| `tables_as_spreadsheet` | Tables as structured spreadsheet data |
| `embedded_images` | Base64-encoded extracted images |

### Spatial Text Sub-options

| Option | Description |
|--------|-------------|
| `preserve_layout_alignment_across_pages` | Maintain column alignment across pages |
| `preserve_very_small_text` | Include sub-8pt text (footnotes, captions) |
| `do_not_unroll_columns` | Keep multi-column layout (no linearization) |

### Python SDK Quick Reference

```python
from llama_parse import LlamaParse

parser = LlamaParse(
    api_key="...",
    tier="agentic",
    target_pages=[1, 2, 3],
    languages=["en", "fr"],
    custom_prompt="Extract all financial figures as structured data.",
    output_tables_as_markdown=True,
    images_to_save=["screenshot"],
    result_type="markdown",    # SDK maps to expand param
    num_workers=4,
    verbose=True,
    ignore_errors=False,
)
documents = parser.load_data("report.pdf")
# async: documents = await parser.aload_data("report.pdf")
```

---

*v1.0 research conducted 2026-04-13. v1.1 enrichment (sections 23-27) added 2026-04-13.*
*Sources: LlamaIndex OSS docs (developers.llamaindex.ai), LlamaIndex blog, Neo4j labs, Mistral AI cookbooks, HuggingFace agents course, DataLeadsFuture analysis.*

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_llamaindex_patterns]] | sibling | 0.34 |
| [[atom_05_semantic_kernel]] | sibling | 0.24 |
| [[atom_12_dify]] | sibling | 0.23 |
| [[p01_kc_document_loader]] | sibling | 0.22 |
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.21 |
| [[bld_architecture_document_loader]] | downstream | 0.21 |
| [[bld_architecture_embedding_config]] | downstream | 0.20 |
| [[p06_arch_rag_pipeline]] | downstream | 0.20 |
| [[bld_collaboration_embedding_config]] | downstream | 0.20 |
| [[atom_10_haystack_vercel]] | sibling | 0.20 |
