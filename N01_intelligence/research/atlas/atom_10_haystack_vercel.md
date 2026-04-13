---
id: atom_10_haystack_vercel
kind: knowledge_card
title: "Atom 10: Haystack (deepset) + Vercel AI SDK -- Full Type Registry & CEX Mapping"
version: 2.0.0
date: 2026-04-13
quality: 8.8
pillar: P01
tags: [haystack, deepset, vercel, ai-sdk, pipeline, rag, streaming, agents, type-registry, serialization, middleware, wire-protocol]
sources:
  - https://docs.haystack.deepset.ai/
  - https://ai-sdk.dev/
  - https://github.com/deepset-ai/haystack
  - https://github.com/vercel/ai
  - https://docs.haystack.deepset.ai/docs/serialization
  - https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat
  - https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-completion
  - https://ai-sdk.dev/docs/ai-sdk-core/middleware
  - https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol
---

# Atom 10: Haystack (deepset) + Vercel AI SDK

Two complementary frameworks: Haystack owns the Python RAG/pipeline/agent backend;
Vercel AI SDK owns the TypeScript streaming-first LLM frontend. Together they cover
the full stack from document ingestion to real-time UI.

---

## 1. HAYSTACK (deepset) -- Python AI Orchestration Framework

### 1.1 Architecture

Haystack 2.x is a directed-graph pipeline engine. Components are nodes; connections
are typed edges. The `@component` decorator registers a class; `run()` is the only
required method. Inputs are declared via method signature or `set_input_type()`.
Outputs via `@component.output_types()` decorator. All return `dict`.

```
Pipeline.add_component(name, instance)
Pipeline.connect("source.output", "target.input")
Pipeline.run({"component": {"input": value}})
Pipeline.inputs()  -> dict of required inputs with types
```

Serialization: YAML-native (pipeline.to_yaml() / from_yaml()).

### 1.1a Pipeline Serialization Format (YAML)

Source: https://docs.haystack.deepset.ai/docs/serialization

Full YAML schema produced by `pipeline.to_yaml()`:

```yaml
# Top-level keys
components:           # dict of component_name -> ComponentSpec
  {name}:
    type: {fully.qualified.ClassName}   # e.g. haystack.components.retrievers.in_memory.bm25_retriever.InMemoryBM25Retriever
    init_parameters:                     # kwargs passed to __init__
      {param_name}: {param_value}
      # Complex objects serialized as dicts with __class__ + __haystack_type__ markers
      document_store:
        type: haystack.document_stores.in_memory.document_store.InMemoryDocumentStore
        init_parameters:
          bm25_algorithm: BM25Okapi
          bm25_parameters: {}
          bm25_tokenization_regex: "(?u)\\b\\w\\w+\\b"
          embedding_similarity_function: dot_product
          index: null
connections:          # list of typed edge specs
  - sender: {component_name}.{output_socket_name}
    receiver: {component_name}.{input_socket_name}
max_runs_per_component: 100   # loop-protection ceiling (default: 100)
metadata:             # arbitrary user-defined key-value pairs
  {key}: {value}
```

**JSON equivalent:** `pipeline.to_dict()` / `Pipeline.from_dict()` produces the same structure as Python dicts, serialized to JSON.

**Versioning:** No explicit schema version field; compatibility tracked by Haystack release. Migration utilities in `haystack.core.serialization`.

**Custom component serialization:**
```python
@component
class MyComponent:
    def to_dict(self) -> dict:
        return default_to_dict(self, param1=self.param1)

    @classmethod
    def from_dict(cls, data: dict) -> "MyComponent":
        return default_from_dict(cls, data)
```
`default_to_dict` / `default_from_dict` handle `__class__` injection automatically.

**Nested component serialization:** Warm components (with document stores, tokenizers, etc.) serialize their entire init_parameters graph recursively. Non-serializable objects (lambdas, file handles) raise `SerializationError`.

Source: https://docs.haystack.deepset.ai/docs/serialization

### 1.2 Core Data Model

| Type | Description |
|------|-------------|
| `Document` | Dataclass: id, content, meta, embedding, score, blob |
| `ChatMessage` | Role-based message: system, user, assistant, tool |
| `GeneratedAnswer` | Answer with source documents and metadata |
| `StreamingChunk` | Token-level streaming output from generators |
| `ByteStream` | Raw file content with MIME type metadata |

### 1.3 Full Component Type Registry

#### 1.3.1 Generators (Chat)

| Component | Provider | Module |
|-----------|----------|--------|
| OpenAIChatGenerator | OpenAI | haystack_integrations.components.generators.openai |
| AzureOpenAIChatGenerator | Azure OpenAI | haystack_integrations.components.generators.azure |
| AzureOpenAIResponsesChatGenerator | Azure (Responses API) | haystack_integrations.components.generators.azure |
| AnthropicChatGenerator | Anthropic | haystack_integrations.components.generators.anthropic |
| AnthropicVertexChatGenerator | Anthropic via Vertex | haystack_integrations.components.generators.anthropic |
| GoogleGenAIChatGenerator | Google Gemini | haystack_integrations.components.generators.google_genai |
| AmazonBedrockChatGenerator | AWS Bedrock | haystack_integrations.components.generators.amazon_bedrock |
| CohereChatGenerator | Cohere | haystack_integrations.components.generators.cohere |
| MistralChatGenerator | Mistral | haystack_integrations.components.generators.mistral |
| OllamaChatGenerator | Ollama (local) | haystack_integrations.components.generators.ollama |
| HuggingFaceAPIChatGenerator | HF API | haystack_integrations.components.generators.huggingface |
| HuggingFaceLocalChatGenerator | HF local | haystack_integrations.components.generators.huggingface |
| LlamaCppChatGenerator | llama.cpp | haystack_integrations.components.generators.llamacpp |
| LlamaStackChatGenerator | Llama Stack | haystack_integrations.components.generators.llama_stack |
| MetaLlamaChatGenerator | Meta Llama API | haystack_integrations.components.generators.meta_llama |
| NvidiaChatGenerator | NVIDIA NIM | haystack_integrations.components.generators.nvidia |
| OpenRouterChatGenerator | OpenRouter | haystack_integrations.components.generators.openrouter |
| TogetherAIChatGenerator | Together AI | haystack_integrations.components.generators.togetherai |
| WatsonxChatGenerator | IBM Watsonx | haystack_integrations.components.generators.watsonx |
| FallbackChatGenerator | (wrapper) | haystack.components.generators |
| AIMLAPIChatGenerator | AIMLAPI | haystack_integrations.components.generators.aimlapi |
| CometAPIChatGenerator | Comet API | haystack_integrations.components.generators.comet |
| STACKITChatGenerator | STACKIT | haystack_integrations.components.generators.stackit |
| OpenAIResponsesChatGenerator | OpenAI Responses API | haystack_integrations.components.generators.openai |

#### 1.3.2 Generators (Text / Non-Chat)

| Component | Provider |
|-----------|----------|
| OpenAIGenerator | OpenAI |
| AzureOpenAIGenerator | Azure |
| AnthropicGenerator | Anthropic |
| AmazonBedrockGenerator | AWS Bedrock |
| CohereGenerator | Cohere |
| OllamaGenerator | Ollama |
| HuggingFaceAPIGenerator | HF API |
| HuggingFaceLocalGenerator | HF local |
| LlamaCppGenerator | llama.cpp |
| NvidiaGenerator | NVIDIA |
| TogetherAIGenerator | Together AI |
| WatsonxGenerator | IBM Watsonx |
| SagemakerGenerator | AWS Sagemaker |
| VertexAITextGenerator | Google Vertex |
| VertexAICodeGenerator | Google Vertex (code) |
| DALLEImageGenerator | OpenAI DALL-E (images) |
| VertexAIImageGenerator | Google Vertex (images) |
| VertexAIImageCaptioner | Google Vertex (captions) |
| VertexAIImageQA | Google Vertex (image QA) |

#### 1.3.3 Retrievers

**Sparse / BM25:**

| Component | Document Store |
|-----------|---------------|
| InMemoryBM25Retriever | InMemoryDocumentStore |
| ElasticsearchBM25Retriever | ElasticsearchDocumentStore |
| OpenSearchBM25Retriever | OpenSearchDocumentStore |
| PgvectorKeywordRetriever | PgvectorDocumentStore |
| WeaviateBM25Retriever | WeaviateDocumentStore |
| AzureAISearchBM25Retriever | AzureAISearchDocumentStore |
| MongoDBAtlasFullTextRetriever | MongoDBAtlasDocumentStore |

**Dense / Embedding:**

| Component | Document Store |
|-----------|---------------|
| InMemoryEmbeddingRetriever | InMemoryDocumentStore |
| ElasticsearchEmbeddingRetriever | ElasticsearchDocumentStore |
| OpenSearchEmbeddingRetriever | OpenSearchDocumentStore |
| PgvectorEmbeddingRetriever | PgvectorDocumentStore |
| ChromaEmbeddingRetriever | ChromaDocumentStore |
| PineconeEmbeddingRetriever | PineconeDocumentStore |
| QdrantEmbeddingRetriever | QdrantDocumentStore |
| WeaviateEmbeddingRetriever | WeaviateDocumentStore |
| AzureAISearchEmbeddingRetriever | AzureAISearchDocumentStore |
| MongoDBAtlasEmbeddingRetriever | MongoDBAtlasDocumentStore |
| AstraEmbeddingRetriever | AstraDocumentStore |
| FAISSEmbeddingRetriever | FAISSDocumentStore |
| ArcadeDBEmbeddingRetriever | ArcadeDBDocumentStore |
| ValkeyEmbeddingRetriever | ValkeyDocumentStore |

**Hybrid:**

| Component | Document Store |
|-----------|---------------|
| AzureAISearchHybridRetriever | AzureAISearchDocumentStore |
| OpenSearchHybridRetriever | OpenSearchDocumentStore |
| QdrantHybridRetriever | QdrantDocumentStore |
| WeaviateHybridRetriever | WeaviateDocumentStore |

**Sparse Embedding:**

| Component | Document Store |
|-----------|---------------|
| QdrantSparseEmbeddingRetriever | QdrantDocumentStore |

**Advanced / Specialized:**

| Component | Purpose |
|-----------|---------|
| FilterRetriever | Metadata-filter-only retrieval (no embedding/BM25) |
| AutoMergingRetriever | Returns parent documents from child chunk matches |
| MultiQueryTextRetriever | Parallel multi-query over BM25 retrievers |
| MultiQueryEmbeddingRetriever | Parallel multi-query over embedding retrievers |
| SentenceWindowRetriever | Expands retrieved chunks to neighboring sentences |
| SnowflakeTableRetriever | SQL queries against Snowflake tables |
| ChromaQueryTextRetriever | Chroma native query API |

#### 1.3.3a Retriever Config Params (Implementation Detail)

Source: https://docs.haystack.deepset.ai/docs/retrievers

**Common params shared by all retrievers:**
- `filters: Optional[Dict]` -- metadata filter dict (REPLACE or MERGE via FilterPolicy)
- `top_k: int = 10` -- max documents returned
- `filter_policy: FilterPolicy` -- REPLACE (default) or MERGE

**InMemoryBM25Retriever**
```python
InMemoryBM25Retriever(
    document_store: InMemoryDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    scale_score: bool = False,     # normalize BM25 score to [0,1]
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
)
```

**ElasticsearchBM25Retriever**
```python
ElasticsearchBM25Retriever(
    document_store: ElasticsearchDocumentStore,
    filters: Optional[Dict] = None,
    fuzziness: str = "AUTO",       # ES fuzziness: AUTO, 0, 1, 2
    top_k: int = 10,
    scale_score: bool = False,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    raise_on_failure: bool = True,
)
```

**OpenSearchBM25Retriever**
```python
OpenSearchBM25Retriever(
    document_store: OpenSearchDocumentStore,
    filters: Optional[Dict] = None,
    fuzziness: str = "AUTO",
    top_k: int = 10,
    scale_score: bool = False,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    all_terms_must_match: bool = False,  # AND vs OR for query terms
    raise_on_failure: bool = True,
)
```

**PgvectorKeywordRetriever**
```python
PgvectorKeywordRetriever(
    document_store: PgvectorDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    # Uses PostgreSQL full-text search (tsvector / tsquery)
)
```

**WeaviateBM25Retriever**
```python
WeaviateBM25Retriever(
    document_store: WeaviateDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    move_to: Optional[Dict] = None,        # concept vector boost {concepts, objects, force}
    move_away_from: Optional[Dict] = None, # concept avoidance
)
```

**InMemoryEmbeddingRetriever**
```python
InMemoryEmbeddingRetriever(
    document_store: InMemoryDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    scale_score: bool = False,
    return_embedding: bool = False,  # include embedding vector in result doc
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
)
# Input socket: query_embedding(List[float])
```

**ElasticsearchEmbeddingRetriever**
```python
ElasticsearchEmbeddingRetriever(
    document_store: ElasticsearchDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    num_candidates: Optional[int] = None,  # ANN candidate pool (default: 10*top_k)
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    raise_on_failure: bool = True,
)
```

**PgvectorEmbeddingRetriever**
```python
PgvectorEmbeddingRetriever(
    document_store: PgvectorDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    vector_function: Optional[str] = None,  # "l2_distance" | "max_inner_product" | "cosine_distance"
)
```

**ChromaEmbeddingRetriever**
```python
ChromaEmbeddingRetriever(
    document_store: ChromaDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    # ChromaDocumentStore handles HNSW index params internally
)
```

**QdrantEmbeddingRetriever**
```python
QdrantEmbeddingRetriever(
    document_store: QdrantDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    scale_score: bool = False,
    return_embedding: bool = False,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
)
```

**WeaviateEmbeddingRetriever**
```python
WeaviateEmbeddingRetriever(
    document_store: WeaviateDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    distance: Optional[float] = None,    # max vector distance threshold
    certainty: Optional[float] = None,   # min cosine similarity [0,1]
    move_to: Optional[Dict] = None,
    move_away_from: Optional[Dict] = None,
)
```

**QdrantHybridRetriever**
```python
QdrantHybridRetriever(
    document_store: QdrantDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    return_embedding: bool = False,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
)
# Inputs: query_embedding(List[float]) + query_sparse_embedding(SparseEmbedding)
# SparseEmbedding: { indices: List[int], values: List[float] }
```

**AzureAISearchHybridRetriever**
```python
AzureAISearchHybridRetriever(
    document_store: AzureAISearchDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    # Uses Reciprocal Rank Fusion (RRF) in Azure for BM25+vector blend
)
```

**OpenSearchHybridRetriever**
```python
OpenSearchHybridRetriever(
    document_store: OpenSearchDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    normalization_technique: str = "min_max",      # or "l2"
    combination_technique: str = "arithmetic_mean", # or "geometric_mean", "harmonic_mean"
    combination_weights: Optional[List[float]] = None,  # [bm25_weight, embedding_weight]
)
```

**WeaviateHybridRetriever**
```python
WeaviateHybridRetriever(
    document_store: WeaviateDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    alpha: float = 0.5,   # 0=BM25 only, 1=vector only, 0.5=equal blend
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
    fusion_type: Optional[str] = None,  # "rankedFusion" | "relativeScoreFusion"
)
```

**QdrantSparseEmbeddingRetriever**
```python
QdrantSparseEmbeddingRetriever(
    document_store: QdrantDocumentStore,
    filters: Optional[Dict] = None,
    top_k: int = 10,
    scale_score: bool = False,
    return_embedding: bool = False,
    filter_policy: FilterPolicy = FilterPolicy.REPLACE,
)
# Input: query_sparse_embedding(SparseEmbedding) -- SPLADE / BM25s vectors
```

**FilterRetriever**
```python
FilterRetriever(
    document_store: BaseDocumentStore,
    filters: Optional[Dict] = None,
    # No vector search. Metadata filter operators: eq, ne, gt, gte, lt, lte, in, not in
    # Logical: AND, OR, NOT (nested dicts)
)
```

**AutoMergingRetriever**
```python
AutoMergingRetriever(
    document_store: BaseDocumentStore,
    threshold: float = 0.5,  # fraction of child matches to trigger parent return
)
# Input: matched_documents(List[Document]) from any upstream retriever
# Output: documents -- swaps child chunks for parent if threshold met
```

**SentenceWindowRetriever**
```python
SentenceWindowRetriever(
    document_store: BaseDocumentStore,
    window_size: int = 3,  # sentences before + after the matched sentence
)
# Input: retrieved_documents(List[Document])
# Output: context_windows(List[Document]) with expanded content field
```

**MultiQueryTextRetriever**
```python
MultiQueryTextRetriever(
    retriever: InMemoryBM25Retriever,  # any BM25-compatible retriever
    llm: BaseChatGenerator,
    query_count: int = 4,              # number of sub-queries to generate
    include_original: bool = True,     # prepend original query to generated set
    system_prompt: Optional[str] = None,
)
# LLM generates query_count rephrasings; runs N BM25 retrievals; deduplicates
```

**SnowflakeTableRetriever**
```python
SnowflakeTableRetriever(
    user: str,
    account: str,
    api_key: Secret,          # Haystack Secret (env var, AWS SM, Azure KV)
    database: Optional[str] = None,
    db_schema: Optional[str] = None,
    warehouse: Optional[str] = None,
    login_timeout: Optional[int] = None,
)
# Input: query(str) -- NL2SQL via companion LLM or raw SQL
# Output: documents(List[Document]) -- each row as Document
```

**FilterPolicy enum:**
```python
class FilterPolicy(Enum):
    REPLACE = "replace"  # component filter replaces init filter
    MERGE   = "merge"    # logical AND merge of init + runtime filters
```

#### 1.3.4 Embedders

**Text Embedders (query-time):**

| Component | Provider |
|-----------|----------|
| OpenAITextEmbedder | OpenAI |
| AzureOpenAITextEmbedder | Azure OpenAI |
| AmazonBedrockTextEmbedder | AWS Bedrock |
| CohereTextEmbedder | Cohere |
| GoogleGenAITextEmbedder | Google |
| MistralTextEmbedder | Mistral |
| NvidiaTextEmbedder | NVIDIA |
| OllamaTextEmbedder | Ollama |
| JinaTextEmbedder | Jina AI |
| HuggingFaceAPITextEmbedder | HF API |
| SentenceTransformersTextEmbedder | SentenceTransformers (local) |
| SentenceTransformersSparseTextEmbedder | SentenceTransformers sparse |
| FastembedTextEmbedder | Fastembed |
| FastembedSparseTextEmbedder | Fastembed sparse |
| OptimumTextEmbedder | HF Optimum |
| STACKITTextEmbedder | STACKIT |
| WatsonxTextEmbedder | IBM Watsonx |

**Document Embedders (index-time):**

| Component | Provider |
|-----------|----------|
| OpenAIDocumentEmbedder | OpenAI |
| AzureOpenAIDocumentEmbedder | Azure OpenAI |
| AmazonBedrockDocumentEmbedder | AWS Bedrock |
| CohereDocumentEmbedder | Cohere |
| GoogleGenAIDocumentEmbedder | Google |
| GoogleGenAIMultimodalDocumentEmbedder | Google (multimodal) |
| MistralDocumentEmbedder | Mistral |
| NvidiaDocumentEmbedder | NVIDIA |
| OllamaDocumentEmbedder | Ollama |
| JinaDocumentEmbedder | Jina AI |
| HuggingFaceAPIDocumentEmbedder | HF API |
| SentenceTransformersDocumentEmbedder | SentenceTransformers |
| SentenceTransformersSparseDocumentEmbedder | SentenceTransformers sparse |
| FastembedDocumentEmbedder | Fastembed |
| FastembedSparseDocumentEmbedder | Fastembed sparse |
| OptimumDocumentEmbedder | HF Optimum |
| STACKITDocumentEmbedder | STACKIT |
| WatsonxDocumentEmbedder | IBM Watsonx |

**Image / Multimodal Embedders:**

| Component | Provider |
|-----------|----------|
| AmazonBedrockDocumentImageEmbedder | AWS Bedrock |
| CohereDocumentImageEmbedder | Cohere |
| JinaDocumentImageEmbedder | Jina AI |
| SentenceTransformersDocumentImageEmbedder | SentenceTransformers |

#### 1.3.5 Rankers

| Component | Strategy |
|-----------|----------|
| SentenceTransformersSimilarityRanker | Cross-encoder similarity scoring |
| TransformersSimilarityRanker | Legacy cross-encoder (deprecated) |
| SentenceTransformersDiversityRanker | Diversity-optimized reranking |
| CohereRanker | Cohere Rerank API |
| JinaRanker | Jina Reranker API |
| AmazonBedrockRanker | AWS Bedrock reranking |
| NvidiaRanker | NVIDIA NIM reranking |
| HuggingFaceTEIRanker | HF Text Embeddings Inference |
| FastembedRanker | Fastembed cross-encoder |
| LLMRanker | LLM-as-judge ranking (returns JSON indices) |
| LostInTheMiddleRanker | Position-aware reordering (begin/end focus) |
| MetaFieldRanker | Sort by metadata field value |
| MetaFieldGroupingRanker | Group documents by metadata key |
| PyversityRanker | Relevance + diversity balancing |

#### 1.3.6 Converters

| Component | Input Format |
|-----------|-------------|
| TextFileToDocument | .txt |
| PDFMinerToDocument | .pdf (complex layouts) |
| PyPDFToDocument | .pdf |
| DOCXToDocument | .docx |
| HTMLToDocument | .html |
| MarkdownToDocument | .md |
| CSVToDocument | .csv |
| XLSXToDocument | .xlsx |
| PPTXToDocument | .pptx |
| MSGToDocument | .msg (Outlook) |
| JSONConverter | .json |
| ImageFileToDocument | images |
| MultiFileConverter | CSV, DOCX, HTML, JSON, MD, PPTX, PDF, TXT, XLSX |
| KreuzbergConverter | 91+ formats (Rust engine) |
| AzureDocumentIntelligenceConverter | PDF, JPEG, PNG, BMP, TIFF, DOCX, XLSX, PPTX, HTML |
| AzureOCRDocumentConverter | Same as above (OCR variant) |
| MistralOCRDocumentConverter | Documents via Mistral OCR API |
| PaddleOCRVLDocumentConverter | Documents via PaddleOCR |
| TikaDocumentConverter | Various via Apache Tika |
| UnstructuredFileConverter | Text files/directories |
| OpenAPIServiceToFunctions | OpenAPI specs -> function defs |
| OutputAdapter | Component output format adaptation |
| FileToFileContent | Any file -> FileContent objects |
| DocumentToImageContent | Document -> ImageContent objects |
| ImageFileToImageContent | Image files -> ImageContent objects |
| PDFToImageContent | PDF pages -> ImageContent objects |

#### 1.3.7 Preprocessors

| Component | Purpose |
|-----------|---------|
| DocumentCleaner | Remove whitespace, empty lines, headers/footers, regex patterns |
| DocumentSplitter | Split by word/sentence/passage/page/line/function |
| DocumentPreprocessor | Combined split + clean in single component |
| HierarchicalDocumentSplitter | Multi-level parent-child document trees |
| RecursiveSplitter | Recursive separator-based chunking |
| MarkdownHeaderSplitter | Split at markdown headers preserving hierarchy |
| ChineseDocumentSplitter | Chinese-specific segmentation via HanLP |
| CSVDocumentCleaner | Remove empty CSV rows/columns |
| CSVDocumentSplitter | Split CSV by empty row/column boundaries |
| TextCleaner | Remove regex, punctuation, numbers; lowercase |

#### 1.3.8 Routers

| Component | Routing Logic |
|-----------|--------------|
| ConditionalRouter | User-defined conditions (Jinja2 expressions) |
| FileTypeRouter | Route by file MIME type |
| DocumentTypeRouter | Route documents by MIME type |
| DocumentLengthRouter | Route by document content length |
| MetadataRouter | Route by metadata field values |
| TextLanguageRouter | Route by detected language |
| LLMMessagesRouter | LLM classifies and routes chat messages |
| TransformersTextRouter | Model-defined category labels |
| TransformersZeroShotTextRouter | User-defined zero-shot category labels |

#### 1.3.9 Joiners

| Component | Merges |
|-----------|--------|
| DocumentJoiner | Lists of Documents (with dedup + score merge) |
| BranchJoiner | Pipeline branches into single output |
| AnswerJoiner | Multiple GeneratedAnswer lists |
| StringJoiner | Strings from different components |
| ListJoiner | Generic lists into flat list |

#### 1.3.10 Writers

| Component | Purpose |
|-----------|---------|
| DocumentWriter | Write Documents to any DocumentStore |

#### 1.3.11 PromptBuilder

| Component | Purpose |
|-----------|---------|
| PromptBuilder | Jinja2 template rendering -> string prompt |
| ChatPromptBuilder | Jinja2 template rendering -> ChatMessage list |

Input: template string + dynamic variables. Output: rendered prompt string or messages.
Templates use `{{ variable }}` syntax with full Jinja2 (loops, conditionals, filters).

#### 1.3.12 Document Stores

| Store | Backend | BM25 | Embedding | Hybrid | Filtering |
|-------|---------|------|-----------|--------|-----------|
| InMemoryDocumentStore | Python dicts | Yes | Yes | No | Yes |
| ElasticsearchDocumentStore | Elasticsearch | Yes | Yes | No | Yes |
| OpenSearchDocumentStore | OpenSearch | Yes | Yes | Yes | Yes |
| PgvectorDocumentStore | PostgreSQL + pgvector | Yes | Yes | No | Yes |
| ChromaDocumentStore | Chroma | No | Yes | No | Yes |
| PineconeDocumentStore | Pinecone (cloud) | No | Yes | No | Yes |
| QdrantDocumentStore | Qdrant | No | Yes | Yes | Yes |
| WeaviateDocumentStore | Weaviate | Yes | Yes | Yes | Yes |
| AzureAISearchDocumentStore | Azure AI Search | Yes | Yes | Yes | Yes |
| MongoDBAtlasDocumentStore | MongoDB Atlas | Yes | Yes | No | Yes |
| AstraDocumentStore | DataStax Astra | No | Yes | No | Yes |
| FAISSDocumentStore | FAISS | No | Yes | No | No |
| Neo4jDocumentStore | Neo4j | No | Yes | No | Yes |
| MilvusDocumentStore | Milvus | No | Yes | No | Yes |
| ArcadeDBDocumentStore | ArcadeDB | No | Yes | No | Yes |
| ValkeyDocumentStore | Valkey | No | Yes | No | Yes |

#### 1.3.13 Agent & Tools

| Component | Purpose |
|-----------|---------|
| Agent | Iterative tool-calling loop over a ChatGenerator |
| Tool | Callable function with name, description, JSON schema params |
| ComponentTool | Wraps any Haystack Component as an Agent Tool |
| MCPTool | Model Context Protocol tool integration |

Agent constructor: `Agent(chat_generator, tools, system_prompt, exit_conditions, state_schema, max_agent_steps, streaming_callback)`.

Agent loop: generate -> detect tool calls -> execute tools -> feed results back -> repeat until exit_condition met ("text" response or named tool).

---

## 2. VERCEL AI SDK -- TypeScript Streaming-First LLM Framework

### 2.1 Architecture

Three layers: **AI SDK Core** (provider-agnostic primitives), **AI SDK UI** (React/Next.js hooks), **AI SDK Providers** (model adapters). Built around the `LanguageModelV4` interface -- every provider implements it, enabling zero-code model switching.

### 2.2 Full Type Registry

#### 2.2.1 Core Generation Functions

**generateText**

```typescript
generateText({
  model: LanguageModel,
  prompt?: string,
  messages?: ModelMessage[],
  system?: string | SystemModelMessage | SystemModelMessage[],
  tools?: ToolSet,
  toolChoice?: "auto" | "none" | "required" | { type: "tool"; toolName: string },
  maxOutputTokens?: number,
  temperature?: number,
  topP?: number,
  topK?: number,
  presencePenalty?: number,
  frequencyPenalty?: number,
  stopSequences?: string[],
  seed?: number,
  maxRetries?: number,
  maxSteps?: number,           // enables agentic multi-step loop
  timeout?: number | { totalMs?; stepMs? },
  abortSignal?: AbortSignal,
  headers?: Record<string, string>,
  prepareStep?: (options) => PrepareStepResult,
  stopWhen?: StopCondition | StopCondition[],
  output?: Output,
  onStepFinish?: (result) => void,
  onFinish?: (result) => void,
  providerOptions?: Record<string, JSONObject>,
  activeTools?: string[],
}): Promise<GenerateTextResult>
```

Returns: `{ text, reasoning, reasoningText, sources, files, toolCalls, toolResults, finishReason, usage, totalUsage, steps, request, response, warnings, providerMetadata }`

**streamText**

```typescript
streamText({
  // same core params as generateText, plus:
  onChunk?: (event) => void,
  onError?: (event) => void,
  onAbort?: (event) => void,
  experimental_transform?: StreamTextTransform[],
  experimental_telemetry?: TelemetrySettings,
}): StreamTextResult
```

Returns: `{ textStream, fullStream, text, content, finishReason, usage, totalUsage, toolCalls, toolResults, steps, reasoning, sources, files, toUIMessageStream(), toUIMessageStreamResponse(), toTextStreamResponse(), pipeUIMessageStreamToResponse(), consumeStream() }`

**generateObject**

```typescript
generateObject({
  model: LanguageModel,
  schema: ZodSchema | JSONSchema7,   // structured output constraint
  schemaName?: string,
  schemaDescription?: string,
  prompt?: string,
  messages?: ModelMessage[],
  system?: string,
  mode?: "auto" | "json" | "tool",   // generation strategy
  // + same tuning params as generateText
}): Promise<GenerateObjectResult>
```

Returns: `{ object, finishReason, usage, warnings, request, response }`

**streamObject**

```typescript
streamObject({
  // same params as generateObject
}): StreamObjectResult
```

Returns: `{ partialObjectStream, object, finishReason, usage, elementStream }`

#### 2.2.2 Message Types

| Type | Role | Description |
|------|------|-------------|
| SystemModelMessage | system | System instructions |
| UserModelMessage | user | User input (text, images, files) |
| AssistantModelMessage | assistant | Model response (text, tool calls, reasoning) |
| ToolModelMessage | tool | Tool execution results |
| ModelMessage | (union) | Union of all four message types |
| CoreMessage | (legacy) | Previous name for ModelMessage |

**UIMessage** (client-side):

```typescript
{
  id: string,
  role: "system" | "user" | "assistant",
  parts: UIMessagePart[],     // text, tool-invocation, reasoning, source, file, data
  metadata?: unknown,
  status: "submitted" | "streaming" | "ready" | "error"
}
```

#### 2.2.3 Tool System

**tool() helper:**

```typescript
tool({
  description: string,
  inputSchema: ZodSchema | JSONSchema,
  execute?: async (input, context) => RESULT,
  strict?: boolean,
  inputExamples?: Array,
  needsApproval?: boolean | async (input) => boolean,
  toModelOutput?: (output) => ContentPart,
})
```

Execute context: `{ toolCallId, messages, abortSignal, experimental_context }`

**ToolInvocation:**

```typescript
{
  toolName: string,
  toolCallId: string,
  state: "partial-call" | "call" | "result",
  args: Record<string, unknown>,
  result?: unknown,
}
```

**ToolCall / ToolResult:**

```typescript
ToolCall<NAME extends string, ARGS>
ToolResult<NAME extends string, ARGS, RESULT>
TypedToolCall<TOOLS>     // extracts types from ToolSet
TypedToolResult<TOOLS>   // extracts types from ToolSet
```

#### 2.2.4 Provider Interface

```typescript
// Model creation pattern
const model = provider(modelId)  // e.g. openai("gpt-4.1")

// LanguageModelV4 interface (abstract)
interface LanguageModelV4 {
  doGenerate(options): Promise<GenerateResult>
  // supports: streaming, structured output, tool calling
}
```

**Official Providers:**

| Provider | Factory | Models |
|----------|---------|--------|
| OpenAI | `openai()` | gpt-4.1, gpt-4o, o3, o4-mini |
| Anthropic | `anthropic()` | claude-opus-4-6, claude-sonnet-4, etc |
| Google GenAI | `google()` | gemini-2.5-pro, gemini-2.5-flash |
| Azure OpenAI | `azure()` | gpt-4.1 via Azure |
| Amazon Bedrock | `bedrock()` | Claude, Llama, etc via AWS |
| Mistral | `mistral()` | mistral-large, codestral |
| Groq | `groq()` | llama, mixtral on Groq hardware |
| xAI | `xai()` | Grok models |
| DeepSeek | `deepseek()` | deepseek-v3, deepseek-r1 |
| Cohere | `cohere()` | command-r-plus |
| Together AI | `togetherai()` | open-source models |
| Fireworks | `fireworks()` | fast open-source inference |
| Perplexity | `perplexity()` | search-augmented models |
| Cerebras | `cerebras()` | fast Llama inference |
| DeepInfra | `deepinfra()` | open-source models |

**Community providers:** Ollama, OpenRouter, Cloudflare Workers AI, Portkey, LM Studio, 30+ more.

#### 2.2.5 Streaming & Data Protocol

**DataStreamProtocol:** Wire format for streaming custom data alongside text.

Source: https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol

The protocol is **newline-delimited lines**, each line formatted as:
```
{type_code}:{json_value}\n
```

**Complete type code table:**

| Code | Type | Payload shape | Notes |
|------|------|--------------|-------|
| `0` | text-delta | `"chunk string"` | Raw text token |
| `1` | tool-call | `{toolCallId, toolName, args}` | Complete tool invocation |
| `2` | data | `[...JSONValue]` | Array of arbitrary JSON |
| `3` | error | `"error message string"` | Error from server |
| `8` | message-annotations | `[...JSONValue]` | Annotation array |
| `9` | tool-call-streaming-start | `{toolCallId, toolName}` | Begin streaming args |
| `a` | tool-call-delta | `{toolCallId, argsTextDelta}` | Partial args chunk |
| `b` | tool-result | `{toolCallId, result}` | Tool execution result |
| `c` | step-start | `{messageId, stepType}` | stepType: "initial"\|"continue" |
| `d` | finish-step | `{finishReason, usage?, isContinued}` | Per-step completion |
| `e` | finish-message | `{finishReason, usage}` | Full message done |
| `f` | file | `{url, mediaType}` | File output |
| `g` | reasoning | `"reasoning text chunk"` | Extended thinking |
| `h` | source | `{sourceType, id, url, title, ...}` | Citation source |

**Wire format examples:**

```
0:"Hello"
0:" world"
9:{"toolCallId":"abc","toolName":"get_weather"}
a:{"toolCallId":"abc","argsTextDelta":"{\"city\":\""}
a:{"toolCallId":"abc","argsTextDelta":"Paris\"}"}
1:{"toolCallId":"abc","toolName":"get_weather","args":{"city":"Paris"}}
b:{"toolCallId":"abc","result":{"temp":22,"unit":"C"}}
0:"The weather in Paris is 22C."
d:{"finishReason":"tool-calls","usage":{"promptTokens":45,"completionTokens":12},"isContinued":false}
e:{"finishReason":"stop","usage":{"promptTokens":78,"completionTokens":38}}
```

**Server-side helpers:**

```typescript
// Stream to Response
return result.toUIMessageStreamResponse();  // Content-Type: text/event-stream

// Pipe to Node.js response
result.pipeUIMessageStreamToResponse(res, {
  headers: { "X-Custom": "value" },
  sendReasoning: true,
  sendSources: true,
  onError: (error) => error.message,  // returns string to send as error part
});

// Manual data appending
const dataStream = createDataStream({
  execute: async (writer) => {
    writer.writeData({ progress: 50 });        // type 2
    writer.writeMessageAnnotation({ id: "x" }); // type 8
  },
});
```

**Text stream protocol (simpler alternative):**
Plain `text/plain` with `streamProtocol: "text"` in useChat.
No tool calls, no data parts -- raw text only.

**Stream part types:** text-delta, tool-call, tool-call-streaming-start, tool-call-delta, tool-result, reasoning, source, file, data, error, finish, step-start, step-finish.

#### 2.2.6 UI Hooks (React)

Source: https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat

| Hook | Purpose |
|------|---------|
| `useChat()` | Full chat UI state management + streaming |
| `useCompletion()` | Single-turn text completion |
| `useObject()` | Streaming structured object generation |

**useChat -- full parameter API:**

```typescript
useChat({
  // Identity & routing
  id?: string,                     // chat ID -- stable across re-renders
  api?: string,                    // default: "/api/chat"

  // Initial state
  initialMessages?: UIMessage[],
  initialInput?: string,

  // Request customization
  body?: Record<string, unknown>,  // extra JSON fields merged into POST body
  headers?: Record<string, string>,
  credentials?: RequestCredentials, // "include" | "omit" | "same-origin"
  sendExtraMessageFields?: boolean, // send id/createdAt in message POST

  // Protocol
  streamProtocol?: "data" | "text", // default: "data"
  maxSteps?: number,                // agentic loop: steps per user message

  // Callbacks
  onResponse?: (response: Response) => void | Promise<void>,
  onFinish?: (message: UIMessage, options: {
    usage: { promptTokens: number; completionTokens: number; totalTokens: number };
    finishReason: FinishReason;
  }) => void,
  onError?: (error: Error) => void,
  onToolCall?: ({ toolCall: ToolCall }) => void | unknown | Promise<unknown>,

  // Performance
  experimental_throttle?: number,  // ms between UI re-renders during streaming

  // Advanced
  experimental_prepareRequestBody?: (options: {
    messages: UIMessage[];
    id: string;
    requestBody?: Record<string, unknown>;
  }) => Record<string, unknown>,

  fetch?: typeof globalThis.fetch,  // custom fetch impl
})
```

**useChat return object:**

```typescript
{
  // State
  messages: UIMessage[],
  input: string,
  status: "ready" | "submitted" | "streaming" | "error",
  error?: Error,
  id: string,
  data?: JSONValue[],              // data parts from stream (type 2)

  // Actions
  sendMessage: (message: CreateMessage | string) => void,
  append: (message: Message | CreateMessage) => Promise<string | null | undefined>,
  reload: () => Promise<string | null | undefined>,  // regenerate last assistant msg
  stop: () => void,               // abort in-flight stream
  addToolResult: ({ toolCallId: string; result: unknown }) => void,

  // State setters
  setMessages: Dispatch<SetStateAction<UIMessage[]>>,
  setInput: Dispatch<SetStateAction<string>>,
  setData: Dispatch<SetStateAction<JSONValue[] | undefined>>,

  // Form helpers
  handleInputChange: (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => void,
  handleSubmit: (
    event?: React.FormEvent<HTMLFormElement>,
    options?: { experimental_attachments?: FileList | File[] }
  ) => void,
}
```

**useCompletion -- full parameter API:**

Source: https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-completion

```typescript
useCompletion({
  api?: string,                   // default: "/api/completion"
  id?: string,
  initialInput?: string,
  initialCompletion?: string,
  body?: Record<string, unknown>,
  headers?: Record<string, string>,
  credentials?: RequestCredentials,
  streamProtocol?: "data" | "text",  // default: "data"
  onResponse?: (response: Response) => void | Promise<void>,
  onFinish?: (prompt: string, completion: string) => void,
  onError?: (error: Error) => void,
  experimental_throttle?: number,
  fetch?: typeof globalThis.fetch,
})
```

**useCompletion return object:**

```typescript
{
  completion: string,            // accumulated completion text
  input: string,
  isLoading: boolean,
  error?: Error,
  data?: JSONValue[],            // data parts from stream

  // Actions
  complete: (prompt: string, options?: {
    headers?: Record<string, string>;
    body?: Record<string, unknown>;
  }) => Promise<string | null | undefined>,
  stop: () => void,
  setCompletion: Dispatch<SetStateAction<string>>,
  setInput: Dispatch<SetStateAction<string>>,

  // Form helpers
  handleInputChange: (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => void,
  handleSubmit: (e?: React.FormEvent<HTMLFormElement>) => void,
}
```

**useObject -- full parameter API:**

```typescript
useObject({
  api?: string,                  // default: "/api/use-object"
  id?: string,
  schema: ZodSchema,             // Zod schema for the target object shape
  initialValue?: DeepPartial<T>,
  headers?: Record<string, string>,
  credentials?: RequestCredentials,
  fetch?: typeof globalThis.fetch,
  onFinish?: (result: { object: T | undefined; error: Error | undefined }) => void,
  onError?: (error: Error) => void,
})

// Returns:
{
  object: DeepPartial<T> | undefined,   // partial object during streaming
  isLoading: boolean,
  error?: Error,
  stop: () => void,
  submit: (input: unknown) => void,
}
```

#### 2.2.7 Agent Pattern

Agents in Vercel AI SDK are `generateText` + `maxSteps` + tools:

```typescript
const result = await generateText({
  model: anthropic("claude-sonnet-4-20250514"),
  tools: { search, calculate, writeFile },
  maxSteps: 10,
  stopWhen: stepCountIs(10),
  prompt: "Research and summarize...",
  onStepFinish: ({ text, toolCalls, toolResults }) => {
    console.log("Step completed", toolCalls.length, "tool calls");
  },
});
// result.steps contains the full execution trace
```

No separate Agent class -- the loop is implicit in generateText/streamText when maxSteps > 1.

#### 2.2.8 Middleware System

Source: https://ai-sdk.dev/docs/ai-sdk-core/middleware

Middleware wraps a `LanguageModelV4` to intercept `doGenerate` and `doStream` calls.
Used for: logging, caching, rate limiting, prompt injection, reasoning extraction.

**Core API:**

```typescript
import { wrapLanguageModel, type LanguageModelMiddleware } from "ai";

const wrappedModel = wrapLanguageModel({
  model: anthropic("claude-opus-4-6"),
  middleware: myMiddleware,   // single middleware
  // OR
  middleware: [mw1, mw2],    // array -- applied left to right
});
```

**Middleware interface:**

```typescript
interface LanguageModelMiddleware {
  // Transform non-streaming calls
  wrapGenerate?: (options: {
    doGenerate: () => ReturnType<LanguageModelV4["doGenerate"]>,
    doStream:   () => ReturnType<LanguageModelV4["doStream"]>,
    params:     Parameters<LanguageModelV4["doGenerate"]>[0],
    model:      LanguageModelV4,
  }) => ReturnType<LanguageModelV4["doGenerate"]>;

  // Transform streaming calls
  wrapStream?: (options: {
    doGenerate: () => ReturnType<LanguageModelV4["doGenerate"]>,
    doStream:   () => ReturnType<LanguageModelV4["doStream"]>,
    params:     Parameters<LanguageModelV4["doStream"]>[0],
    model:      LanguageModelV4,
  }) => ReturnType<LanguageModelV4["doStream"]>;

  transformParams?: {
    (options: { params: LanguageModelV4CallOptions; type: "generate" | "stream" })
      : Promise<LanguageModelV4CallOptions> | LanguageModelV4CallOptions,
  };
}
```

**Built-in middleware:**

| Middleware | Import | Purpose |
|------------|--------|---------|
| `extractReasoningMiddleware` | `ai` | Extract `<think>` tags as reasoning field |
| `simulateStreamingMiddleware` | `ai` | Convert non-streaming response to stream |
| `defaultSettingsMiddleware` | `ai` | Override model default params |

**extractReasoningMiddleware config:**

```typescript
extractReasoningMiddleware({
  tagName: "think",         // tag to extract (default: "think")
  separator: "\n",          // separator between reasoning and text
  startWithReasoning: false, // true = reasoning precedes text
})
```

**Custom logging middleware example:**

```typescript
const loggingMiddleware: LanguageModelMiddleware = {
  wrapGenerate: async ({ doGenerate, params }) => {
    console.log("Prompt:", params.prompt);
    const result = await doGenerate();
    console.log("Response:", result.text);
    return result;
  },
  wrapStream: async ({ doStream, params }) => {
    console.log("Stream start:", params.prompt);
    const { stream, ...rest } = await doStream();
    return {
      stream: stream.pipeThrough(new TransformStream({
        transform(chunk, controller) {
          if (chunk.type === "text-delta") console.log(chunk.textDelta);
          controller.enqueue(chunk);
        },
      })),
      ...rest,
    };
  },
};
```

**Custom caching middleware example:**

```typescript
const cacheMiddleware: LanguageModelMiddleware = {
  wrapGenerate: async ({ doGenerate, params }) => {
    const cacheKey = JSON.stringify(params);
    const cached = cache.get(cacheKey);
    if (cached) return cached;
    const result = await doGenerate();
    cache.set(cacheKey, result);
    return result;
  },
};
```

**Middleware composition order:** leftmost = outermost wrapper (called first on input, last on output).

---

## 3. COMPARATIVE ANALYSIS

### 3.1 Architecture Comparison

| Dimension | Haystack | Vercel AI SDK |
|-----------|----------|---------------|
| Language | Python | TypeScript |
| Paradigm | Directed graph pipeline | Function-call with implicit loop |
| Component model | @component decorator + run() | Function params + LanguageModelV4 |
| Typing | Python type hints + dict returns | TypeScript generics + Zod schemas |
| Streaming | StreamingChunk callback | AsyncIterableStream native |
| Agent model | Explicit Agent class with tool loop | generateText + maxSteps |
| Serialization | YAML native | JSON (no built-in pipeline serialization) |
| Document store | 16 integrations built-in | None (not in scope) |
| Structured output | Via PromptBuilder templates | generateObject with Zod/JSON Schema |
| State | Pipeline-level (no cross-run state) | React hooks (useChat) for UI state |
| Primary use | Backend RAG/pipeline/agent | Frontend streaming + API routes |

### 3.2 Component Equivalence Map

| Haystack Component | Vercel AI SDK Equivalent | Notes |
|--------------------|--------------------------|-------|
| Pipeline | (no equivalent) | Vercel has no graph engine |
| Generator / ChatGenerator | generateText / streamText | Function vs component |
| Retriever | (external, e.g. via tool) | Vercel delegates retrieval to tools |
| Embedder | (external, via provider) | Vercel has embedding support via providers |
| Ranker | (none) | Must implement as tool or middleware |
| Converter | (none) | Not in scope |
| Router | (none -- implicit in code) | TypeScript if/switch replaces routers |
| Joiner | (none -- implicit in code) | Promise.all or array merge |
| DocumentStore | (none) | Not in scope |
| PromptBuilder | system/prompt params | String interpolation replaces Jinja2 |
| Agent | generateText + maxSteps | Implicit vs explicit agent |
| Tool | tool() helper | Near-identical concept |
| ChatMessage | ModelMessage / CoreMessage | Role-based in both |
| Document | (no equivalent) | Vercel has no document abstraction |
| StreamingChunk | textStream / fullStream | Different streaming models |

---

## 4. CEX PILLAR MAPPING

### 4.1 Haystack -> CEX Pillars

| Haystack Concept | CEX Pillar | CEX Kind | Rationale |
|------------------|-----------|----------|-----------|
| Pipeline | P12 Orchestration | workflow | Directed graph = workflow |
| Component (base) | P04 Tools | cli_tool | Reusable processing unit |
| @component decorator | P08 Architecture | naming_rule | Convention-over-config pattern |
| ChatGenerator | P02 Model | agent | LLM interface abstraction |
| Generator | P03 Prompt | prompt_template | Text generation = prompt execution |
| Retriever | P01 Knowledge | rag_source | Core RAG retrieval |
| Embedder | P01 Knowledge | embedding_config | Vector representation |
| Ranker | P07 Evaluation | scoring_rubric | Document relevance scoring |
| Converter | P04 Tools | cli_tool | File format transformation |
| Router | P12 Orchestration | dispatch_rule | Conditional routing |
| Joiner | P12 Orchestration | workflow | Branch merge |
| Writer | P01 Knowledge | knowledge_index | Persistence to store |
| DocumentStore | P01 Knowledge | rag_source | Storage backend |
| PromptBuilder | P03 Prompt | prompt_template | Template rendering |
| Agent | P02 Model | agent | Autonomous tool-using entity |
| Tool | P04 Tools | cli_tool | External capability |
| Document | P06 Schema | schema | Core data contract |
| ChatMessage | P06 Schema | input_schema | Message protocol |

### 4.2 Vercel AI SDK -> CEX Pillars

| Vercel AI SDK Concept | CEX Pillar | CEX Kind | Rationale |
|-----------------------|-----------|----------|-----------|
| generateText | P03 Prompt | action_prompt | Single-shot generation |
| streamText | P03 Prompt | action_prompt | Streaming generation |
| generateObject | P06 Schema | schema | Schema-constrained output |
| streamObject | P06 Schema | schema | Streaming structured output |
| tool() | P04 Tools | cli_tool | Callable capability |
| LanguageModelV4 | P02 Model | model_provider | Provider abstraction |
| Provider | P02 Model | model_provider | Model factory |
| CoreMessage / ModelMessage | P06 Schema | input_schema | Message contract |
| UIMessage | P05 Output | output_template | Client-side representation |
| ToolInvocation | P04 Tools | cli_tool | Tool execution record |
| useChat | P05 Output | landing_page | UI state management |
| DataStreamProtocol | P06 Schema | interface | Wire protocol contract |
| maxSteps (agent loop) | P12 Orchestration | workflow | Iterative execution |
| StopCondition | P11 Feedback | quality_gate | Termination criteria |
| prepareStep | P12 Orchestration | dispatch_rule | Per-step configuration |
| onStepFinish | P11 Feedback | learning_record | Step-level feedback |

---

## 5. KEY INSIGHTS FOR CEX

### 5.1 What CEX Can Learn from Haystack

1. **Typed component protocol**: Haystack's `@component` + typed `run()` is close to CEX's kind system. Each component declares its I/O contract -- analogous to CEX ISOs declaring builder inputs/outputs.

2. **Pipeline serialization**: YAML-native serialization means pipelines are data, not code. CEX already uses YAML for schemas -- a Pipeline kind could serialize CEX workflows the same way.

3. **Document Store abstraction**: 16 backends behind one interface. CEX's `rag_source` kind could adopt this pattern for storage-agnostic retrieval.

4. **Retriever taxonomy**: The BM25/embedding/hybrid/sparse split maps directly to CEX chunk_strategy and embedding_config kinds. Haystack proves the taxonomy is industry-standard.

5. **Agent as component**: Haystack's Agent is just another pipeline component with a tool loop. This validates CEX's decision to treat agents as composable artifacts, not special entities.

### 5.2 What CEX Can Learn from Vercel AI SDK

1. **Streaming-first**: Every function has a streaming variant. CEX's output pipeline (P05) should assume streaming as default, not batch.

2. **Schema-as-output-constraint**: `generateObject` with Zod proves that structured output is a first-class concern. CEX's `schema` kind should include output schemas, not just input validation.

3. **Provider abstraction depth**: LanguageModelV4 hides 30+ providers behind one interface. CEX's `model_provider` kind + `fallback_chain` already does this -- Vercel validates the pattern.

4. **Implicit agent loop**: No Agent class needed -- just generateText + maxSteps. This is simpler than Haystack's explicit Agent. CEX could offer both patterns.

5. **UI message protocol**: UIMessage with parts (text, tool-invocation, reasoning, source, file) is a rich output format. CEX's `output_template` kind could adopt this part-based structure.

### 5.3 Component Count Summary

| Category | Haystack | Vercel AI SDK |
|----------|----------|---------------|
| Generators / LLM functions | 44 | 4 (generateText, streamText, generateObject, streamObject) |
| Retrievers | 28 | 0 (delegated to tools) |
| Embedders | 40 | via providers |
| Rankers | 14 | 0 |
| Converters | 26 | 0 |
| Preprocessors | 10 | 0 |
| Routers | 9 | 0 (code-level routing) |
| Joiners | 5 | 0 |
| Document Stores | 16 | 0 |
| Prompt Builders | 2 | string params |
| Agent/Tool | 4 | 1 (tool helper) |
| UI Hooks | 0 | 3 |
| **Total components** | **198** | **8 core functions** |

Haystack = wide component catalog for backend pipelines.
Vercel AI SDK = narrow, deep API for streaming LLM interactions.

---

## 6. REFERENCES

- Haystack docs: https://docs.haystack.deepset.ai/
- Haystack GitHub: https://github.com/deepset-ai/haystack
- Vercel AI SDK docs: https://ai-sdk.dev/
- Vercel AI SDK GitHub: https://github.com/vercel/ai
- Haystack integrations: https://haystack.deepset.ai/integrations
- AI SDK providers: https://ai-sdk.dev/docs/ai-sdk-core/providers-and-models

---

## 1.4 Pipeline Serialization Format (YAML)

Haystack pipelines are data, not code. `pipeline.dumps()` / `pipeline.loads()` round-trip
through a canonical YAML schema. Every component must implement `to_dict()` / `from_dict()`
for the pipeline serializer to reconstruct it.

### 1.4.1 Schema Structure

```yaml
# Top-level fields
max_runs_per_component: 100          # int, default 100; caps loops
metadata: {}                         # dict, arbitrary pipeline metadata
components:                          # dict of named component definitions
  <component_name>:
    type: <fully.qualified.class>    # e.g. haystack.components.preprocessors.document_cleaner.DocumentCleaner
    init_parameters:                 # dict of constructor args (primitives + nested objects)
      <param>: <value>
connections:                         # list of typed edges
  - sender: <comp_name>.<output>     # e.g. embedder.embedding
    receiver: <comp_name>.<input>    # e.g. retriever.query_embedding
```

### 1.4.2 Serialization API

```python
from haystack import Pipeline

# Serialize
yaml_str: str = pipeline.dumps()            # -> YAML string
pipeline.dump(file_obj)                     # -> write to file

# Deserialize
pipeline = Pipeline.loads(yaml_str)
pipeline = Pipeline.load(file_obj)

# Dict round-trip (lower-level)
d: dict = pipeline.to_dict()
pipeline = Pipeline.from_dict(d, callbacks=DeserializationCallbacks())
```

`DeserializationCallbacks` allow patching components during reconstruction
(e.g. injecting secrets, swapping implementations without changing YAML).

### 1.4.3 Full Serialized Pipeline Example (RAG)

```yaml
max_runs_per_component: 100
metadata:
  name: basic-rag
  description: Embedding RAG pipeline
components:
  text_embedder:
    type: haystack_integrations.components.embedders.openai.text_embedder.OpenAITextEmbedder
    init_parameters:
      model: text-embedding-3-small
      dimensions: 1536
  retriever:
    type: haystack_integrations.components.retrievers.pinecone.embedding_retriever.PineconeEmbeddingRetriever
    init_parameters:
      document_store:
        type: haystack_integrations.document_stores.pinecone.document_store.PineconeDocumentStore
        init_parameters:
          index: my-index
          namespace: ""
          dimension: 1536
          metric: cosine
      top_k: 5
      filter_policy: replace
  prompt_builder:
    type: haystack.components.builders.prompt_builder.PromptBuilder
    init_parameters:
      template: |
        Answer using the documents below.
        Documents: {% for doc in documents %}{{ doc.content }}{% endfor %}
        Question: {{ question }}
  llm:
    type: haystack_integrations.components.generators.openai.chat.chat_generator.OpenAIChatGenerator
    init_parameters:
      model: gpt-4o-mini
      generation_kwargs:
        temperature: 0.1
        max_tokens: 512
connections:
  - sender: text_embedder.embedding
    receiver: retriever.query_embedding
  - sender: retriever.documents
    receiver: prompt_builder.documents
  - sender: prompt_builder.prompt
    receiver: llm.prompt
```

### 1.4.4 Component `to_dict()` Contract

Any custom component MUST implement:

```python
@component
class MyComponent:
    def to_dict(self) -> dict:
        return default_to_dict(self, param1=self.param1, param2=self.param2)

    @classmethod
    def from_dict(cls, data: dict):
        return default_from_dict(cls, data)
```

`default_to_dict` injects `type` as the fully qualified class name automatically.

### 1.4.5 AsyncPipeline

`AsyncPipeline` is a drop-in replacement that executes independent branches in parallel:

```python
from haystack import AsyncPipeline

pipeline = AsyncPipeline()
pipeline.add_component("embedder", embedder)
pipeline.add_component("retriever", retriever)
pipeline.connect("embedder.embedding", "retriever.query_embedding")
result = await pipeline.run({"embedder": {"text": "query"}})
```

Branches with no shared dependency run concurrently. Components with input dependencies
wait for their upstream outputs before starting.

---

## 1.5 Retriever Config Params (All 28+ Implementations)

All retrievers share this interface pattern:
- **Constructor**: receives `document_store` (mandatory) + retrieval strategy params
- **run()**: receives `query` or `query_embedding` (mandatory) + `top_k`, `filters` (optional)
- **Output**: `{"documents": List[Document]}`

`filters` always uses Haystack logical filter syntax:

```python
filters = {
  "operator": "AND",
  "conditions": [
    {"field": "meta.lang", "operator": "==", "value": "en"},
    {"field": "meta.score", "operator": ">=", "value": 0.8},
  ]
}
```

`FilterPolicy` enum: `FilterPolicy.REPLACE` (run() filters override constructor) or
`FilterPolicy.MERGE` (run() filters AND-merged with constructor filters).

### 1.5.1 BM25 / Keyword Retrievers

| Retriever | Constructor Params | run() Params |
|-----------|-------------------|--------------|
| InMemoryBM25Retriever | `document_store`, `filters=None`, `top_k=10`, `scale_score=True`, `filter_policy=REPLACE` | `query: str`, `filters`, `top_k`, `scale_score` |
| ElasticsearchBM25Retriever | `document_store`, `filters={}`, `fuzziness="AUTO"`, `top_k=10`, `scale_score=True`, `filter_policy=REPLACE` | `query`, `filters`, `fuzziness`, `top_k` |
| OpenSearchBM25Retriever | `document_store`, `filters={}`, `fuzziness="AUTO"`, `top_k=10`, `scale_score=True`, `custom_query=None` | `query`, `filters`, `top_k` |
| PgvectorKeywordRetriever | `document_store`, `filters=None`, `top_k=10`, `filter_policy=REPLACE` | `query`, `filters`, `top_k` |
| WeaviateBM25Retriever | `document_store`, `filters=None`, `top_k=10`, `filter_policy=REPLACE` | `query`, `filters`, `top_k` |
| AzureAISearchBM25Retriever | `document_store`, `filters=None`, `top_k=10`, `filter_policy=REPLACE` | `query`, `filters`, `top_k` |
| MongoDBAtlasFullTextRetriever | `document_store`, `filters=None`, `top_k=10` | `query`, `filters`, `top_k` |

### 1.5.2 Embedding / Dense Retrievers

| Retriever | Constructor Params | run() Params | Notes |
|-----------|-------------------|--------------|-------|
| InMemoryEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10`, `scale_score=True`, `return_embedding=False`, `filter_policy=REPLACE` | `query_embedding: List[float]`, `filters`, `top_k`, `scale_score`, `return_embedding` | L2/cosine |
| ElasticsearchEmbeddingRetriever | `document_store`, `filters={}`, `top_k=10`, `num_candidates=100`, `filter_policy=REPLACE` | `query_embedding`, `filters`, `top_k`, `num_candidates` | ES kNN |
| OpenSearchEmbeddingRetriever | `document_store`, `filters={}`, `top_k=10`, `filter_policy=REPLACE`, `custom_query=None` | `query_embedding`, `filters`, `top_k` | approx kNN |
| PgvectorEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10`, `filter_policy=REPLACE` | `query_embedding`, `filters`, `top_k` | exact/HNSW per store config |
| ChromaEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10` | `query_embedding`, `filters`, `top_k` | Chroma query() |
| PineconeEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10`, `filter_policy=REPLACE` | `query_embedding`, `filters`, `top_k` | Pinecone query() |
| QdrantEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10`, `return_embedding=False`, `score_threshold=None` | `query_embedding`, `filters`, `top_k`, `score_threshold` | Qdrant nearest |
| WeaviateEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10`, `filter_policy=REPLACE`, `distance=None`, `certainty=None` | `query_embedding`, `filters`, `top_k` | nearVector |
| AzureAISearchEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10`, `filter_policy=REPLACE` | `query_embedding`, `filters`, `top_k` | Azure vector search |
| MongoDBAtlasEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10`, `filter_policy=REPLACE` | `query_embedding`, `filters`, `top_k` | Atlas Vector Search |
| AstraEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10` | `query_embedding`, `filters`, `top_k` | DataStax Astra |
| FAISSEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10` | `query_embedding`, `filters`, `top_k` | FAISS flat/IVF/HNSW |
| ArcadeDBEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10` | `query_embedding`, `filters`, `top_k` | ArcadeDB vector |
| ValkeyEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10` | `query_embedding`, `filters`, `top_k` | Valkey VSEARCH |

### 1.5.3 Hybrid Retrievers

Hybrid = BM25 + vector in one call; merged by RRF or weighted sum. Requires a single query
string AND a query embedding -- both must be supplied to `run()`.

| Retriever | Constructor Params | run() Params | Merge Strategy |
|-----------|-------------------|--------------|----------------|
| AzureAISearchHybridRetriever | `document_store`, `filters=None`, `top_k=10`, `filter_policy=REPLACE` | `query_embedding`, `query: str`, `filters`, `top_k` | Azure native hybrid |
| OpenSearchHybridRetriever | `document_store`, `filters={}`, `top_k=10`, `bm25_weight=0.5`, `embedding_weight=0.5` | `query_embedding`, `query`, `filters`, `top_k` | Weighted sum |
| QdrantHybridRetriever | `document_store`, `filters=None`, `top_k=10`, `return_embedding=False` | `query_embedding: List[float]`, `sparse_embedding: SparseEmbedding`, `filters`, `top_k` | RRF |
| WeaviateHybridRetriever | `document_store`, `filters=None`, `top_k=10`, `alpha=0.75`, `filter_policy=REPLACE` | `query_embedding`, `query`, `filters`, `top_k`, `alpha` | alpha=1.0 pure vector; alpha=0.0 pure BM25 |

### 1.5.4 Sparse Embedding

| Retriever | Constructor Params | run() Params | Input Type |
|-----------|-------------------|--------------|------------|
| QdrantSparseEmbeddingRetriever | `document_store`, `filters=None`, `top_k=10`, `return_embedding=False`, `score_threshold=None` | `query_sparse_embedding: SparseEmbedding`, `filters`, `top_k` | `{indices: List[int], values: List[float]}` |

`SparseEmbedding` matches output of `FastembedSparseTextEmbedder` or `SentenceTransformersSparseTextEmbedder`.

### 1.5.5 Advanced / Specialized Retrievers

| Retriever | Constructor Params | run() Params | Notes |
|-----------|-------------------|--------------|-------|
| FilterRetriever | `document_store`, `filters=None` | `filters` | No ranking; pure metadata filter |
| AutoMergingRetriever | `document_store`, `threshold=0.5` | `matched_leaf_documents: List[Document]` | Merges child chunks into parent when >= threshold matched |
| MultiQueryTextRetriever | `document_store`, `top_k=10`, `retriever_params={}` | `queries: List[str]`, `filters`, `top_k` | Fan-out BM25; deduplicates by doc ID |
| MultiQueryEmbeddingRetriever | `document_store`, `top_k=10`, `retriever_params={}` | `query_embeddings: List[List[float]]`, `filters`, `top_k` | Fan-out embedding; deduplicates |
| SentenceWindowRetriever | `document_store`, `window_size=3` | `retrieved_documents: List[Document]` | Expands to +/- window_size sentences |
| SnowflakeTableRetriever | `user`, `account`, `api_key`, `database`, `db_schema`, `warehouse`, `login_timeout=30` | `query: str` | NL -> SQL on Snowflake |
| ChromaQueryTextRetriever | `document_store`, `filters=None`, `top_k=10` | `query: str`, `filters`, `top_k` | Chroma text query (internal embedding) |

---

## 2.3 Vercel AI SDK Middleware System

### 2.3.1 Architecture

Middleware wraps `LanguageModelV3` via `wrapLanguageModel()`, intercepting calls before/after
the model without changing call-site code. Multiple middlewares form an onion: first in list
is outermost (first to see params, last to see results).

### 2.3.2 `wrapLanguageModel()` API

```typescript
import { wrapLanguageModel } from "ai";

const wrapped = wrapLanguageModel({
  model: openai("gpt-4.1"),          // base LanguageModelV3
  middleware: myMiddleware,           // or: [mw1, mw2, mw3]
  modelId?: "custom-id",             // override model.modelId
  providerId?: "custom-provider",    // override model.provider
});
// wrapped is a LanguageModelV3 -- drop-in replacement
```

Execution order with `[mw1, mw2]`:
- transformParams: `mw1 -> mw2 -> model`
- results: `model -> mw2 -> mw1`

### 2.3.3 `LanguageModelV3Middleware` Interface

```typescript
interface LanguageModelV3Middleware {
  // Runs before BOTH generate and stream calls.
  transformParams?: (options: {
    params: LanguageModelV3CallOptions;
    type: "generate" | "stream";
  }) => Promise<LanguageModelV3CallOptions>;

  // Intercept non-streaming doGenerate().
  wrapGenerate?: (options: {
    doGenerate: () => Promise<LanguageModelV3GenerateResult>;
    doStream: () => Promise<{ stream: ReadableStream<LanguageModelV3StreamPart>; rawCall: RawCallResponse }>;
    params: LanguageModelV3CallOptions;
    model: LanguageModelV3;
  }) => Promise<LanguageModelV3GenerateResult>;

  // Intercept streaming doStream().
  wrapStream?: (options: {
    doGenerate: () => Promise<LanguageModelV3GenerateResult>;
    doStream: () => Promise<{ stream: ReadableStream<LanguageModelV3StreamPart>; rawCall: RawCallResponse }>;
    params: LanguageModelV3CallOptions;
    model: LanguageModelV3;
  }) => Promise<{ stream: ReadableStream<LanguageModelV3StreamPart>; rawCall: RawCallResponse }>;
}
```

All three methods are optional. Pass context via `params.providerMetadata.yourKey`.

### 2.3.4 Built-in Middlewares

**extractReasoningMiddleware** -- strips `<think>` blocks into separate reasoning field:

```typescript
import { extractReasoningMiddleware, wrapLanguageModel } from "ai";

wrapLanguageModel({
  model: deepseek("deepseek-r1"),
  middleware: extractReasoningMiddleware({
    tagName: "think",           // default: "think"
    startWithReasoning: false,  // prepend reasoning to generation if true
  }),
});
// result.reasoning / result.reasoningText populated
```

**simulateStreamingMiddleware** -- makes non-streaming models stream:

```typescript
import { simulateStreamingMiddleware } from "ai";

wrapLanguageModel({
  model: nonStreamingModel,
  middleware: simulateStreamingMiddleware(),
});
// wrapStream() calls doGenerate() internally, emits fake stream parts
```

**defaultSettingsMiddleware** -- apply model defaults per-app:

```typescript
import { defaultSettingsMiddleware } from "ai";

wrapLanguageModel({
  model: openai("gpt-4.1"),
  middleware: defaultSettingsMiddleware({
    settings: {
      temperature: 0.2,
      maxOutputTokens: 1024,
      providerOptions: {
        openai: { store: false },
      },
    },
  }),
});
```

**addToolInputExamplesMiddleware** -- inject tool examples into descriptions:

```typescript
import { addToolInputExamplesMiddleware } from "ai";

wrapLanguageModel({
  model: provider("model"),
  middleware: addToolInputExamplesMiddleware({
    prefix: "Input Examples:",
    format: (example, index) => `${index + 1}. ${JSON.stringify(example.input)}`,
    remove: true,   // strip inputExamples from schema after injection
  }),
});
```

**extractJsonMiddleware** -- strip markdown code fences from JSON responses:

```typescript
import { extractJsonMiddleware } from "ai";

wrapLanguageModel({
  model: provider("model"),
  middleware: extractJsonMiddleware(),
});
```

### 2.3.5 Custom Middleware Pattern

```typescript
const loggingMiddleware: LanguageModelV3Middleware = {
  transformParams: async ({ params, type }) => {
    console.log(`[${type}] messages: ${params.prompt?.length ?? 0}`);
    return params;
  },
  wrapGenerate: async ({ doGenerate, params }) => {
    const t0 = Date.now();
    const result = await doGenerate();
    console.log(`generate: ${Date.now() - t0}ms, tokens: ${result.usage?.totalTokens}`);
    return result;
  },
  wrapStream: async ({ doStream }) => {
    const { stream, ...rest } = await doStream();
    const transform = new TransformStream();
    stream.pipeTo(transform.writable);
    return { stream: transform.readable, ...rest };
  },
};
```

---

## 2.4 DataStreamProtocol -- Complete Wire Format

Wire format between Vercel AI SDK server helpers and `useChat`/`useCompletion` clients.
Built on Server-Sent Events (SSE) + JSON per part.

### 2.4.1 Transport Layer

```
HTTP/1.1 200 OK
Content-Type: text/event-stream
x-vercel-ai-ui-message-stream: v1    # REQUIRED -- signals protocol version v1
Cache-Control: no-cache
Transfer-Encoding: chunked

data: {"type":"start","messageId":"msg_abc123"}
data: {"type":"text-start","id":"txt_1"}
data: {"type":"text-delta","id":"txt_1","delta":"Hello"}
data: {"type":"text-delta","id":"txt_1","delta":" world"}
data: {"type":"text-end","id":"txt_1"}
data: {"type":"finish"}
data: [DONE]
```

### 2.4.2 All Part Types

**Message lifecycle:**

| Type | Fields | Description |
|------|--------|-------------|
| `start` | `messageId: string` | Opens a new message frame |
| `finish` | _(none)_ | Closes the message frame |
| `abort` | `reason?: string` | Client-side abort notification |

**Text content (start/delta/end pattern):**

| Type | Fields | Description |
|------|--------|-------------|
| `text-start` | `id: string` | Opens a text block |
| `text-delta` | `id: string`, `delta: string` | Appends text fragment |
| `text-end` | `id: string` | Closes text block |

**Reasoning (models with extended thinking):**

| Type | Fields | Description |
|------|--------|-------------|
| `reasoning-start` | `id: string` | Opens reasoning block |
| `reasoning-delta` | `id: string`, `delta: string` | Appends reasoning fragment |
| `reasoning-end` | `id: string` | Closes reasoning block |

**Tool execution:**

| Type | Fields | Description |
|------|--------|-------------|
| `tool-input-start` | `toolCallId`, `toolName` | Opens tool input streaming |
| `tool-input-delta` | `toolCallId`, `inputTextDelta: string` | Streams tool arg JSON fragment |
| `tool-input-available` | `toolCallId`, `toolName`, `input: object` | Complete tool args ready |
| `tool-output-available` | `toolCallId`, `output: unknown` | Tool execution result |

**Sources and media:**

| Type | Fields | Description |
|------|--------|-------------|
| `source-url` | `sourceId`, `url`, `title?`, `providerMetadata?` | URL citation |
| `source-document` | `sourceId`, `mediaType`, `title?`, `data?` | Document citation |
| `file` | `url`, `mediaType` | Generated file attachment |

**Custom data and control:**

| Type | Fields | Description |
|------|--------|-------------|
| `data-<suffix>` | `data: unknown`, `transient?: boolean` | App-defined; `transient=true` = not persisted to message history |
| `error` | `errorText: string` | Error during generation |

**Step boundaries (agentic multi-step):**

| Type | Fields | Description |
|------|--------|-------------|
| `start-step` | `messageId?` | Opens an agent step |
| `finish-step` | `messageId?`, `isContinued: boolean` | `isContinued=true` means more steps follow |

### 2.4.3 Server-Side Emission

```typescript
// Next.js Route Handler
export async function POST(req: Request) {
  const result = streamText({
    model: openai("gpt-4o"),
    messages: await req.json(),
  });
  return result.toUIMessageStreamResponse({
    sendReasoning: true,
    sendSources: true,
    headers: { "X-Custom": "value" },
    onError: (err) => err.message,   // transform errors before sending
  });
}
```

### 2.4.4 Custom Data Parts

```typescript
// Server: write data parts alongside text
const response = createDataStreamResponse({
  execute: async (writer) => {
    writer.writeData({ status: "processing" });          // -> data-* part
    writer.writeMessageAnnotation({ hitRate: 0.87 });    // -> annotation on message
    const result = await streamText({ model, prompt });
    result.mergeIntoDataStream(writer);
  },
});

// Client: receive via onData
useChat({
  onData: (items) => items.forEach(i => console.log(i)),
});
```

---

## 2.5 Complete useChat API (v5 / SDK 5.x)

### 2.5.1 Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api` | `string` | `"/api/chat"` | Endpoint URL |
| `chat` | `Chat<UIMessage>` | -- | Reuse existing Chat instance |
| `transport` | `ChatTransport` | DefaultChatTransport | Custom transport layer |
| `id` | `string` | random UUID | Stable ID; same ID shares state across components |
| `messages` | `UIMessage[]` | `[]` | Initial message history |
| `messageMetadataSchema` | `FlexibleSchema` | -- | Validation schema for message.metadata |
| `dataPartSchemas` | `UIDataTypesToSchemas` | -- | Schemas for data-* part validation |
| `generateId` | `IdGenerator` | nanoid | Custom ID generator |
| `credentials` | `RequestCredentials` | -- | Fetch credentials mode |
| `headers` | `Record<string,string>` | -- | Extra request headers |
| `body` | `object` | -- | Extra request body fields |
| `fetch` | `FetchFunction` | global fetch | Custom fetch implementation |
| `prepareSendMessagesRequest` | `(options) => RequestOptions` | -- | Customize request before send |
| `prepareReconnectToStreamRequest` | `(options) => RequestOptions` | -- | Customize reconnect |
| `onToolCall` | `async ({ toolCall }) => result` | -- | Client-side tool handler |
| `sendAutomaticallyWhen` | `(message) => boolean` | -- | Auto-send after stream if condition met |
| `onFinish` | `(message: UIMessage) => void` | -- | Called on response completion |
| `onError` | `(error: Error) => void` | -- | Error handler |
| `onData` | `(data: unknown[]) => void` | -- | Called when data-* parts arrive |
| `experimental_throttle` | `number` | -- | UI re-render throttle in ms |
| `resume` | `boolean` | `false` | Reconnect to in-progress generation on mount |

### 2.5.2 Return Values

| Property | Type | Description |
|----------|------|-------------|
| `id` | `string` | Chat identifier |
| `messages` | `UIMessage[]` | Full conversation history |
| `status` | `"ready" \| "submitted" \| "streaming" \| "error"` | Current request state |
| `error` | `Error \| undefined` | Active error |
| `sendMessage` | `async (msg) => void` | Submit a new user message |
| `regenerate` | `async (options?) => void` | Regenerate last assistant message |
| `stop` | `() => void` | Abort the current stream |
| `clearError` | `() => void` | Reset error state |
| `resumeStream` | `() => void` | Resume an interrupted stream |
| `addToolOutput` | `(toolCallId: string, result: unknown) => void` | Inject tool result |
| `addToolApprovalResponse` | `(toolCallId: string, approved: boolean) => void` | Respond to needsApproval |
| `setMessages` | `(messages: UIMessage[]) => void` | Overwrite messages locally |

### 2.5.3 sendMessage Options

```typescript
sendMessage({
  text: string;
  files?: FileList | FileUIPart[];
  metadata?: unknown;        // validated against messageMetadataSchema
  messageId?: string;        // custom ID; else generateId() used
});
```

---

## 2.6 Complete useCompletion API

Single-turn text completion (no conversation history).

### 2.6.1 Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api` | `string` | `"/api/completion"` | API endpoint |
| `id` | `string` | random | Shared state identifier across components |
| `initialInput` | `string` | -- | Pre-fill the prompt input |
| `initialCompletion` | `string` | -- | Pre-fill the completion output |
| `credentials` | `"omit" \| "same-origin" \| "include"` | `"same-origin"` | Fetch credentials |
| `headers` | `Record<string,string>` | -- | Extra request headers |
| `body` | `object` | -- | Extra request body fields |
| `streamProtocol` | `"text" \| "data"` | `"data"` | Stream interpretation mode |
| `fetch` | `FetchFunction` | global fetch | Custom fetch |
| `onFinish` | `(prompt: string, completion: string) => void` | -- | Completion callback |
| `onError` | `(error: Error) => void` | -- | Error handler |
| `experimental_throttle` | `number` | -- | UI update throttle ms |

### 2.6.2 Return Values

| Property | Type | Description |
|----------|------|-------------|
| `completion` | `string` | Current completion text |
| `input` | `string` | Current input value |
| `setInput` | `Dispatch<SetStateAction<string>>` | Update input state |
| `handleInputChange` | `(event: any) => void` | onChange handler for input |
| `handleSubmit` | `(event?: FormEvent) => void` | onSubmit handler for form |
| `complete` | `async (prompt, options?) => string \| null` | Programmatic trigger |
| `setCompletion` | `(text: string) => void` | Override completion manually |
| `stop` | `() => void` | Abort in-progress stream |
| `error` | `Error \| undefined` | Active error |
| `isLoading` | `boolean` | Whether request is in flight |

### 2.6.3 `streamProtocol` Difference

| Mode | Server returns | Client parses |
|------|---------------|---------------|
| `"data"` | DataStreamProtocol SSE | Parses all part types, extracts text |
| `"text"` | Plain text stream | Appends raw chunks directly |

Use `"text"` for simple backends; `"data"` to receive annotations and metadata.
