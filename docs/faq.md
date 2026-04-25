# FAQ

## What does the X in CEXAI mean?

Exchange. CEXAI stands for Cognitive Exchange AI. The core idea is that intelligence compounds faster when shared. Every typed artifact -- a knowledge card, a builder, a vertical nucleus -- is a portable exchange unit. Export it from one CEXAI instance, import it into another, run `cex_doctor.py`, and it validates automatically. Brand config, memory, and secrets stay private. The exchange is about cognition, not identity.

## How is CEX different from CrewAI / LangChain / AutoGen?

Those frameworks give you primitives for building multi-agent systems. CEXAI is a complete, opinionated system already built on top of similar primitives. It ships with 300 artifact types, 301 builders, 12 domain pillars, 7 specialized nuclei, and a quality governance pipeline. You do not assemble the pieces -- you configure and use them.

The tradeoff: CrewAI/LangChain are more flexible if you want to build from scratch. CEXAI is more productive if your work fits the AI brain model -- especially when you want typed, governed, exchangeable knowledge assets instead of throwaway LLM outputs.

## Do I need to know Python?

For basic use inside Claude Code, no. You interact through slash commands like `/build`, `/mission`, and `/guide`. The system handles file generation, validation, and git commits.

For SDK use or extending CEX with custom tools, yes -- Python 3.10+ is required.

## Can I use GPT / Gemini / Ollama instead of Claude?

Yes. CEX is provider-agnostic. It supports Claude, GPT (via OpenAI API), Gemini, and Ollama (fully local). Routing is configured in `.cex/config/nucleus_models.yaml` -- you can set different models per nucleus and define fallback chains.

The `chat()` function auto-detects the provider from the model name: `claude-*` goes to Anthropic, `gpt-*` goes to OpenAI, anything else goes to Ollama.

## What does 8F mean?

8F is the eight-function pipeline that every task runs through: Constrain, Become, Inject, Reason, Call, Produce, Govern, Collaborate. Think of it as a quality-enforcing assembly line. A vague 5-word request enters at F1 and a validated, structured artifact exits at F8.

See [Concepts](concepts.md) for a full breakdown.

## How do I add a new kind?

1. Define the kind in `.cex/kinds_meta.json`
2. Create a knowledge card at `N00_genesis/P01_knowledge/library/kind/kc_yourkind.md`
3. Create a builder directory at `archetypes/builders/yourkind-builder/` with 12 ISO files (one per pillar)
4. Add a sub-agent definition at `.claude/agents/yourkind-builder.md`
5. Add entries to the prompt compiler at `N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md`
6. Run `python _tools/cex_doctor.py` to verify everything is wired correctly

This is a non-trivial process because every kind is fully typed and governed. The builder ISOs are what teach the LLM to produce high-quality instances of your new kind.

## Is this production-ready?

CEX is actively used in production by its creators. The core pipeline (8F, builders, validation, multi-runtime dispatch) is stable. The SDK (`cex_sdk`) is functional but still evolving -- API surfaces may change between versions.

The system has 135+ tools, 54 system tests, pre-commit hooks, and a flywheel audit with 109 checks. That said, it is a complex system with many moving parts. Expect to invest time understanding the architecture before relying on it for critical workloads.

## What is the "sin" thing about?

Each nucleus has a "sin lens" -- a personality based on one of the seven deadly sins. This is not decoration. It is a cultural heuristic that determines what the nucleus optimizes for when given ambiguous input. For example, N01 (Intelligence) runs on Analytical Envy -- it is driven to surpass every existing source. N06 (Commercial) runs on Strategic Greed -- it extracts maximum revenue from every opportunity. The sin biases the LLM toward a specific optimization axis without requiring explicit instructions for every edge case.

## Where does my data go?

Nowhere external. Everything CEX produces lives in your git repository: artifacts, decisions, signals, memory, compiled metadata. There is no external database. The LLM provider sees your prompts during generation (same as any LLM usage), but all persistent state is local files under git version control.
