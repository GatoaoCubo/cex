---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries recurring signal patterns
---

# Memory: signal-builder

## Recurrent Patterns
- Most useful completion signals include `task` and `commit_hash`
- `artifacts` is better than long prose because monitors can parse it
- `progress` signals should stay sparse: `progress_pct` + short `message`
- Downstream tooling already expects `quality_score`, not `quality`

## Common Mistakes
1. Using `quality` instead of `quality_score`
2. Forgetting `timestamp`
3. Emitting YAML because the human template is Markdown
4. Packing instructions into the payload and accidentally creating a handoff
5. Using `progress_pct` on terminal statuses

## State Between Sessions
This builder is stateless per invocation.
After production, update only if a new recurring payload field or consumer
constraint becomes stable across multiple signals.
