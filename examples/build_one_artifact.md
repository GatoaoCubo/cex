# Build One Artifact

This walkthrough uses the `agent` kind because it is easy to inspect, has a mature builder, and routes to `N03_engineering/`. Start here after [quickstart.md](quickstart.md).

## Prerequisites

- The quickstart completed successfully
- Claude CLI is available if you want to use `--execute`

## 1. Inspect the plan first

`cex_run.py` can show the execution plan without spending tokens:

```bash
python _tools/cex_run.py --plan "create simple agent"
```

Expected result: JSON describing the classified kind, active builders, and the 8F function fan-out. In the current repo state this resolves to:

```json
{
  "intent": "create simple agent",
  "parsed": {
    "verb": "create",
    "object": "agent",
    "domain": "P02"
  },
  "classified_kinds": [
    {
      "kind": "agent",
      "pillar": "P02",
      "match_type": "exact"
    }
  ],
  "total_builders": 6
}
```

## 2. Run the 8F builder in dry-run mode

Use the runner directly to see the 8F trace before you execute:

```bash
python _tools/cex_8f_runner.py "create simple agent" --kind agent --dry-run --verbose
```

Expected 8F trace:

```text
[F1 CONSTRAIN] ... constraints: {max_bytes: 5120, fields: 10, id_pattern: /^p02_agent_[a-z][a-z0-9_]+$/}
[F2 BECOME] ... identity: 8 keys
[F3 INJECT] ... ISOs: 12, KCs injected: 2
[F4 REASON] ... plan: 168 words (model=dry-run)
[F5 CALL] ... tools: 19, existing: 9, executed: 5
[F6 PRODUCE] ... artifact: 7897 words
[F7 GOVERN] ... gates: 2/6, retries: 3
[F8 COLLABORATE] ... mode: dry-run, path: None
```

That dry-run is useful for debugging builder behavior because it shows exactly which constraints and knowledge sources the runner assembled.

## 3. Execute the build

When you are ready to actually write an artifact:

```bash
python _tools/cex_run.py "create simple agent" --execute
```

`cex_run.py --help` confirms that `--execute` uses the Claude CLI with subscription auth. If that auth is not configured locally, stay on the dry-run path until it is.

## 4. Inspect the output

Agent outputs for N03 live under `N03_engineering/`. Existing examples in this repo include:

```text
N03_engineering/agents/agent_engineering.md
N03_engineering/compiled/agent_engineering.yaml
```

The artifact itself is a normal CEX markdown file with frontmatter plus typed sections. The current `agent_engineering.md` starts like this:

```yaml
---
id: p02_agent_builder_nucleus
kind: agent
pillar: P02
title: Builder Nucleus Agent
agent_group: builder_hub
domain: meta-construction
llm_function: BECOME
---
```

After a successful `--execute` run, expect:

- a new or updated `.md` artifact in `N03_engineering/agents/`
- a compiled `.yaml` alongside it in `N03_engineering/compiled/`
- a git diff you can review before commit

## 5. What happened under the hood

- F1 loaded the `agent` constraints and size rules.
- F2 loaded the `agent-builder` identity from `archetypes/builders/agent-builder/`.
- F3 injected the `kc_agent.md` kind card plus supporting references.
- F5 discovered tools and similar existing artifacts.
- F7 enforced the hard gates before save/compile.

## Next steps

Dispatch multiple nuclei in parallel with [run_grid.md](run_grid.md).
