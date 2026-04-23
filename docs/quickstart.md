# Quickstart

Build your first CEX artifact in under 5 minutes.

## Prerequisites

- Python 3.10 or higher
- git
- An LLM provider: Anthropic API key, OpenAI API key, or Ollama running locally

## Install

```bash
git clone https://github.com/GatoaoCubo/cex.git
cd cex
pip install -r requirements.txt
pip install -r requirements-llm.txt    # optional: LLM provider SDKs
pip install -e .                       # install cex_sdk as a local package
```

## Bootstrap your brand (optional)

CEX works without this, but artifacts will be generic. Answer 6 questions to personalize everything:

```bash
python _tools/cex_bootstrap.py
```

Or type `/init` inside a Claude Code session with CEX loaded.

## Build your first artifact (CLI)

If you are using CEX inside Claude Code (the typical way):

```
/build create a knowledge card about customer onboarding best practices
```

Or from the command line:

```bash
python _tools/cex_8f_runner.py "create knowledge card about customer onboarding" \
    --kind knowledge_card --execute
```

This runs the full 8F pipeline: resolves the artifact type, loads context from the knowledge library, generates a structured markdown file with frontmatter, validates it, and saves it.

## Build your first artifact (SDK)

```python
from cex_sdk import CEXAgent

agent = CEXAgent(nucleus="n03", kind="knowledge_card")
result = agent.build("customer onboarding best practices")

print(result.artifact)   # the generated markdown
print(result.score)      # quality score (0-10)
print(result.trace)      # F1:knowledge_card/P01 | F3:2srcs(...) | ...
print(result.passed)     # True if score >= 8.0
```

## What you just built

The output is a **knowledge card** -- a structured markdown file with:

- **Frontmatter** (YAML header): id, kind, pillar, version, tags
- **Body**: organized sections with domain knowledge
- **Quality score**: validated against structural and rubric gates

This artifact is now part of your CEX knowledge base. Other nuclei can reference it, the retriever can find it, and future builds get smarter because it exists.

## Validate system health

```bash
python _tools/cex_doctor.py              # check builder integrity
python _tools/cex_hooks.py validate-all  # frontmatter validation
```

## Next steps

- [Concepts](concepts.md) -- Understand the architecture: 8F, pillars, nuclei
- [CLI Reference](cli-reference.md) -- All available commands
- [SDK Reference](sdk-reference.md) -- Python API for programmatic use
- [FAQ](faq.md) -- Common questions
