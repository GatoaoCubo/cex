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

| Hook | Purpose |
|------|---------|
| `useChat()` | Full chat UI state management + streaming |
| `useCompletion()` | Single-turn text completion |
| `useObject()` | Streaming structured object generation |

**useChat return:**

```typescript
{
  messages: UIMessage[],
  status: "ready" | "submitted" | "streaming" | "error",
  error?: Error,
  sendMessage: (message) => void,
  regenerate: () => void,
  stop: () => void,
  addToolOutput: (toolCallId, result) => void,
  setMessages: (messages) => void,
  id: string,
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
