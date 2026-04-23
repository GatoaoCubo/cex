# CEX SDK Examples

Runnable examples showing how to use the CEX typed knowledge system,
from a single agent call to full grid dispatch.

## Prerequisites

```bash
cd /path/to/cex
pip install -e .
export ANTHROPIC_API_KEY=sk-...   # or use Ollama (no key needed)
```

## Examples

| # | Name | Difficulty | What you learn |
|---|------|-----------|----------------|
| 01 | [Hello Agent](01_hello_agent/) | Beginner | Create a CEXAgent, run a build, inspect the 8F trace |
| 02 | [Build Artifact](02_build_artifact/) | Beginner | Use the CLI to produce a knowledge_card with proper frontmatter |
| 03 | [Multi-Nucleus Crew](03_multi_nucleus_crew/) | Intermediate | Compose 3 nuclei into a sequential crew with handoffs |
| 04 | [Knowledge RAG](04_knowledge_rag/) | Intermediate | Read markdown, chunk, embed, retrieve, answer |
| 05 | [Grid Mission](05_grid_mission/) | Advanced | Write handoffs and dispatch 6 nuclei in parallel |

## Running

Each example has its own `README.md` with instructions.
Python examples can be run directly:

```bash
cd examples/01_hello_agent
python main.py
```

## Notes

- All Python code is ASCII-only (CEX convention).
- Examples that call LLMs require either an API key or a running Ollama instance.
- Examples 03 and 05 use CLI dispatch and require the full CEX repo structure.
