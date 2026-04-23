# 01 -- Hello Agent

**Difficulty:** Beginner

## What it does

Creates a `CEXAgent`, runs the 8F pipeline on a simple intent, and prints
the build trace. This is the minimal viable use of the CEX SDK.

## How to run

```bash
# From the repo root:
pip install -e .
export ANTHROPIC_API_KEY=sk-...   # or set OLLAMA_URL for local models

python examples/01_hello_agent/main.py
```

## Expected output

```
=== CEX Hello Agent ===
Kind:    knowledge_card
Pillar:  P01
Score:   8.5/10
Passed:  True
Trace:   F1:knowledge_card/P01 | F3:2srcs(1200chars) | F5:1800chars | F7:8.5/10(pass) | F8:signal_sent
Artifact preview (first 200 chars):
---
id: kc_python_decorators
kind: knowledge_card
...
```

The exact score and content depend on the LLM response. The trace shows
each 8F function that executed.
