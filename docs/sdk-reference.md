# SDK Reference

The `cex_sdk` package provides a Python API for building artifacts, calling LLMs, defining tools, and running workflows. Install with `pip install -e .` from the repo root.

## CEXAgent

The main entry point for building artifacts programmatically. Wraps `chat()` with the full 8F pipeline.

```python
from cex_sdk import CEXAgent

agent = CEXAgent(
    nucleus="n03",                # which nucleus identity to use
    kind="knowledge_card",        # artifact type (optional -- inferred from intent if omitted)
    model="claude-sonnet-4-6",    # LLM model to use
    repo_root=".",                # path to the CEX repo (for context loading)
    min_score=8.0,                # minimum quality threshold
)
```

### agent.build(intent, system="", **kwargs) -> BuildResult

Runs F1 through F8 and returns a `BuildResult`:

```python
result = agent.build("best practices for API rate limiting")

result.artifact       # str -- the generated markdown (with frontmatter)
result.kind           # str -- resolved kind (e.g. "knowledge_card")
result.pillar         # str -- resolved pillar (e.g. "P01")
result.score          # float -- quality score 0-10
result.passed         # bool -- True if score >= min_score and has frontmatter
result.trace          # str -- pipeline trace (e.g. "F1:knowledge_card/P01 | F3:2srcs...")
result.errors         # list[str] -- validation errors (empty if passed)
result.signal_path    # str | None -- path to the signal file written at F8
result.context_chars  # int -- total characters of context injected at F3
```

### agent.validate(payload) -> ValidatorResult

Run F7 validation standalone. Returns `ValidatorResult` with `.score`, `.passed`, `.errors`.

### agent.signal(score, status="complete") -> str

Emit an F8 signal manually. Returns the signal file path.

## chat()

Thin synchronous LLM call. Auto-detects the provider from the model name.

```python
from cex_sdk import chat

response = chat("Explain microservices in 3 sentences")
response = chat("Translate to French", model="gpt-4o", system="You are a translator.")
response = chat("Summarize this", model="llama3.1:8b")  # uses Ollama
```

Parameters: `prompt` (str), `model` (str, default `"claude-sonnet-4-6"`), `provider` (str, default `"auto"`), `max_tokens` (int, default 4096), `system` (str). Provider auto-detection: `claude-*` -> Anthropic, `gpt-*`/`o1-*`/`o3-*` -> OpenAI, else -> Ollama.

## Toolkit and @cex_tool

Define tools that LLMs can call:

```python
from cex_sdk import Toolkit, cex_tool

class SearchTools(Toolkit):
    @cex_tool(name="search_docs", description="Search the knowledge base")
    def search(self, query: str) -> str:
        return do_search(query)
```

## Workflow

Compose multi-step workflows: `Workflow`, `Step`, `Parallel`, `Loop`, `Condition`, `Router`.

```python
from cex_sdk import Workflow, Step, Parallel

wf = Workflow(name="research_and_write")
wf.add(Step(name="research", fn=research_fn))
wf.add(Parallel(steps=[Step(name="a", fn=draft), Step(name="b", fn=draft)]))
```

## Other modules

| Module | Purpose |
|--------|---------|
| `cex_sdk.schema` | InputSchema, DataContract, Validator for artifact validation |
| `cex_sdk.knowledge` | Document readers (PDF, CSV, JSON, markdown, web), chunking, embeddings |
| `cex_sdk.memory` | Memory manager, compression, stores |
| `cex_sdk.guardrails` | PII detection, prompt injection guard |
| `cex_sdk.vectordb` | Vector store abstraction (Chroma adapter) |
| `cex_sdk.config` | Env config, feature flags, rate limits, retry policies |
| `cex_sdk.output` | Formatters, parsers, validators, streaming |
| `cex_sdk.tracing` | Trace exporter for observability |
