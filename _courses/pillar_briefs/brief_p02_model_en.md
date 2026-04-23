---
quality: 8.1
id: kc_pillar_brief_p02_model_en
kind: knowledge_card
pillar: P02
title: "P02 Model — Agent Identity as Typed Infrastructure"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
language: en
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p02, model, agent-identity, persona, fallback-chain, artificial-sins, llm-engineering]
tldr: "Deep technical brief on P02 Model: 23 kinds covering agent identity, model selection, fallback chains, Artificial Sins lens — typed agent infrastructure patterns."
source_concepts: [kc_lens_index, mentor_context]
related:
  - kc_pillar_brief_p02_model_pt
  - kc_pillar_brief_p01_knowledge_en
  - cm_driver_01_structured_thinking
  - kc_lens_factory
  - kc_lens_index
density_score: 0.79
updated: "2026-04-22"
---

# P02 Model — Agent Identity as Typed Infrastructure

## The Universal Principle: Identity Before Everything

Here is the most underrated insight in modern AI engineering: **the identity you give an AI matters more than the prompts you write to it.**

Think of it this way. An actor without a role is talented but directionless. They can improvise, they can speak clearly, they can follow stage directions — but give them nothing to *be*, and every performance is generic. The moment you say "you are a seasoned detective who trusts no one and asks for evidence on every claim," everything changes. The same actor, the same talent, radically different output.

LLMs work exactly this way. The first 200 words you give any AI — the system prompt, the persona, the role definition — shape every single response that follows. Not a little. Enormously. This is P02 Model: the pillar of agent identity.

**Why this matters to you right now**, regardless of whether you use ChatGPT, Claude, Gemini, or a local Ollama model: if you are not deliberately defining who your AI is before you ask it anything, you are leaving the majority of its capability on the table.

---

### Four Universal Insights About AI Identity

**Insight 1: Persona shapes reasoning, not just tone**

Most people think of persona as "making the AI sound more formal" or "giving it a name." That is the surface. The deep value is that a well-defined persona changes how the AI *reasons about tradeoffs*. A "skeptical risk analyst" will identify different issues in a business plan than a "enthusiastic startup advisor" — even when given identical information. The persona is an objective function, not a costume.

**Insight 2: System prompts are the most powerful 200 words you will ever write**

The system prompt runs before every message you send. It sets the prior. It defines what the AI considers important, how it handles ambiguity, what tone it defaults to under pressure. Most people spend hours crafting the perfect question and five seconds writing the system prompt. The leverage is backwards. A mediocre question with an excellent system prompt produces better output than an excellent question with no system prompt.

**Insight 3: Multi-model thinking beats single-model loyalty**

Every major AI model has a different strength profile. Claude excels at long-form reasoning and nuanced analysis. GPT-4 is fast and broadly capable. Gemini processes images and documents efficiently. Local Ollama models run offline and protect private data. Treating one model as "the best" and using it for everything is like having a team with a carpenter, a plumber, and an electrician but only ever calling the carpenter. The right architecture routes work to the right model for that work.

**Insight 4: Constraint creates excellence — the Artificial Sins insight**

This is counterintuitive. We assume that less constrained AI is better AI. In practice, the opposite is often true. When you tell an AI "be creative but also analytical and also concise and also thorough," it tries to average all those things and produces mediocre output. When you tell it "you are obsessed with finding flaws — you do not praise, you only find risks," it produces razor-sharp risk analysis. Constraint creates a specialization that outperforms generality on the specific task.

This is the "Artificial Sins" pattern encoded in CEXAI: each AI agent carries a sin that defines its optimization target. The AI tasked with research carries "Analytical Envy" — an obsessive need to know more than competitors. The AI tasked with monetization carries "Strategic Greed" — a compulsion to maximize every revenue opportunity. The sin is not decoration. It is the objective function.

---

## What P02 Model Does

P02 Model is the pillar that answers one question with surgical precision: WHO is the agent? Not what it does, not how it speaks, not which tools it calls — but what it fundamentally IS. This is the identity layer of LLM systems, and it is the most under-engineered layer in typical agentic architectures.

In the CEXAI 12-pillar system, P02 sits at the intersection of specification and runtime. P01 governs what the agent knows. P03 governs how it speaks. P08 governs how it is structured. P02 governs what the agent IS — its persona, its model selection, its routing rules, its fallback behavior, its memory configuration, its ability to hand off to other agents, and its immutable principles.

The practical consequence is concrete: an agent without a well-formed P02 is a generic LLM wrapper. An agent WITH a well-formed P02 is a deployable, composable, versioned, quality-gated actor in a multi-agent system. The delta between these two is not cosmetic.

### Why Agent Identity Matters for LLM Engineering

When you build with raw LLM APIs, identity lives in ad-hoc system prompts written by whoever was on call that week. This creates three failure modes:

1. **Identity drift**: the same agent behaves differently across sessions because its identity is not formalized
2. **Routing ambiguity**: orchestrators cannot know which agent handles which domain because capabilities are not typed
3. **Portability failure**: an agent built for Claude cannot be ported to Gemini or Ollama because its identity is encoded in provider-specific prompts

P02 solves all three by treating agent identity as typed, versioned, quality-scored infrastructure — the same way P01 treats knowledge and P06 treats data schemas.

---

## "Works With Any AI" — Practical Patterns

These patterns require zero special tools. You can do all of them today, with any AI you already have.

### Pattern A: The Persona Setup

Open any AI. Before asking your actual question, write:

> "You are a senior financial analyst with 15 years of experience in SaaS metrics. You are deeply skeptical of vanity metrics and always push back to ask for unit economics — CAC, LTV, payback period. You speak directly and do not soften negative assessments."

Now ask your question. Compare the response to asking the same question without this setup. The difference is not subtle. You have just created a P02 `agent` with a defined persona — no code required.

The more specific the role definition, the better the output. "You are an expert" is weak. "You are a skeptical SaaS investor who has seen 400 pitch decks and rejected 380 of them" is strong.

### Pattern B: The Constraint Trick (Artificial Sins in Practice)

Tell your AI: "You are OBSESSED with finding flaws in this business plan. You will NOT praise anything — you are here only to identify risks, assumptions that might be wrong, and fatal flaws."

Then ask it to review your business plan.

Compare this to asking a neutral AI to "analyze the strengths and weaknesses." The constrained version finds three to five times more issues because it has one objective: look for problems. This is the Artificial Sins pattern applied without any framework. The sin here is a kind of adversarial skepticism, and it makes the AI dramatically better at the specific task of risk identification.

You can use this for any specialized task:
- "You are a copy editor who is allergic to passive voice, jargon, and weak adjectives."
- "You are a security engineer who assumes every line of code is a potential attack surface."
- "You are an operations manager who treats every process without a documented SOP as a liability."

### Pattern C: The Boot Config

The most underused practice in LLM work is **saving your best system prompts**. Every time you discover a persona or role definition that produces exceptional output, write it down in a text file. At the start of every new conversation with that AI, paste it in first.

That is a boot config. The AI starts each session "already knowing" its role, rather than starting as a blank slate every time. This is the single highest-leverage habit for people who use AI daily.

Practical implementation: create a folder called `ai_personas` or `system_prompts`. For each recurring use case — research, code review, writing, financial analysis — save one file with the opening persona. Copy-paste it to start a session.

### Pattern D: Multi-Model Routing

You probably have access to several AI models already. The question is: which do you use for what?

A practical routing heuristic:
- **Claude** — long documents, nuanced reasoning, writing with specific tone requirements, code review
- **GPT-4** — quick structured outputs, broad general knowledge, tasks where speed matters
- **Gemini** — anything involving images or documents uploaded as files, Google Workspace integration
- **Local Ollama models** — anything with sensitive data (financial records, medical info, trade secrets), anything that needs to run offline

Deciding which model handles which task type is a fallback chain. If Claude is unavailable or rate-limited, which model takes over? If you are on a plane without internet, which local model handles the work?

This is what production AI systems formalize in P02 `model_provider` and `fallback_chain` artifacts. You can implement the same thinking informally by just being deliberate about which tool you reach for.

### Pattern E: Saving Your Best Self-Prompts

Many people do not realize that AI responses improve dramatically when you tell it how to think, not just what to produce. Some prompts to save:

- "Before answering, list the three most important assumptions you're making."
- "After your answer, identify the weakest point in your own reasoning."
- "Structure this as: bottom line first, then supporting evidence, then caveats."
- "Think step by step before giving a final answer."

These are reusable thinking patterns. They are, in effect, the `mental_model` kind in P02 — instructions about *how to reason*, not just *what to say*.

---

## The 23 Kinds Reframed as Universal Capabilities

P02 contains 23 kinds organized into four functional clusters. Rather than listing them as CEXAI terminology, here is what each represents as a universal LLM engineering capability.

### Agent Identity Kinds — "Who Is This AI?"

| Kind | What It Really Is | Universal Application |
|------|-----------------|-----------------------|
| `agent` | A defined AI worker with role, tools, goals, and behavioral constraints | The core persona file you save and reuse for a specific job |
| `agent_profile` | The method for building a persona from composable traits | A template: "Role + Constraints + Voice + Domain Expertise" |
| `agent_package` | A portable bundle containing everything one AI worker needs to run anywhere | An "export" of an AI persona so it works on Claude, GPT, or Gemini equally |
| `agents_md` | A machine-readable index of all AI workers in a project | The README for a multi-AI system — "here is who does what" |
| `nucleus_def` | The formal identity contract for one specialized AI nucleus | The master spec for one role in a multi-agent team |
| `axiom` | An immutable principle that cannot be overridden by any prompt | "Non-negotiable rules" — what the AI will always and never do |
| `mental_model` | How the AI reasons about ambiguity and routes sub-tasks | The thinking protocol — "when unsure, ask yourself these three questions" |

### Model Infrastructure Kinds — "Which Engine Does What?"

| Kind | What It Really Is | Universal Application |
|------|-----------------|-----------------------|
| `model_card` | A profile of one specific LLM: cost, context limit, strengths, weaknesses | Your notes on each AI model you use and when to use it |
| `model_provider` | Configuration for one AI provider: rate limits, retry policy, auth | The settings you need to connect to and use one AI platform reliably |
| `fallback_chain` | If Model A fails, use Model B; if that fails, use Model C | The backup plan when your primary AI is unavailable or too expensive |
| `router` | Routing rules: simple questions go to cheap model, complex to premium | The decision tree for "which AI do I send this to?" |
| `model_architecture` | How the neural network itself is structured | Deep ML engineering — relevant only if you are training models |
| `finetune_config` | How to fine-tune a base model on your specific data | The spec for "teaching a model your specific domain" |

### Runtime Behavior Kinds — "How Does It Start and Run?"

| Kind | What It Really Is | Universal Application |
|------|-----------------|-----------------------|
| `boot_config` | The startup instructions loaded before any conversation | Your saved system prompt for a given provider and use case |
| `memory_scope` | How much the AI remembers, for how long, in what format | The policy for managing conversation history across sessions |
| `handoff_protocol` | The data contract when one AI passes work to another | The integration spec between two AI workers in a pipeline |

### Persona and Role Kinds — "What Is Its Character?"

| Kind | What It Really Is | Universal Application |
|------|-----------------|-----------------------|
| `lens` | A specialized perspective baked into all decisions — the "sin" | The constraint that makes a general AI excellent at one thing |
| `personality` | Voice, tone, register — swappable without changing capability | The "brand voice" layer on top of the capability layer |
| `role_assignment` | Binding a role name to a specific agent ID in a crew | "In this project, the researcher role is played by Agent X" |
| `customer_segment` | The buyer persona the AI is optimized to serve | Grounding the AI in a specific user type for better output relevance |

---

## Key Engineering Patterns

### Pattern 1: Agent Identity Composition

The correct way to define a deployable agent is to compose three distinct layers:

```
agent          (what it IS: persona, tools, model reference, behavioral prior)
  + personality  (how it SOUNDS: register, tone, values, anti-patterns)
  + boot_config  (how it STARTS: model flags, provider config, env vars)
= deployable agent identity
```

The `agent` kind references a `model_card` (which engine) and a `memory_scope` (how it remembers). The `personality` kind is hot-swappable — you can change the voice without changing the capability set. The `boot_config` is provider-specific: the same agent may have `boot_config_claude.md` and `boot_config_gemini.md` as siblings.

This decomposition solves identity drift: when you need to update the agent's voice, you change `personality` without touching `agent`. When you deploy to a new provider, you write a new `boot_config` without touching either.

**For everyday AI users:** save three separate files for any AI worker you use frequently — one for "what it is" (role and constraints), one for "how it sounds" (tone and voice), one for "how it starts" (the opening lines you paste). Change them independently.

### Pattern 2: Multi-Model Architecture

Production LLM systems need to route across models for cost and resilience. The typed P02 components for this:

```
model_provider   (one per provider: Anthropic, Google, OpenAI, Ollama)
  + model_card   (one per model: opus, sonnet, haiku, gemini-2.5-pro, llama3)
  + fallback_chain  (one per resilience requirement: opus > sonnet > haiku)
  + router       (one per routing strategy: complexity-based, cost-based)
= multi-model architecture
```

A concrete example from the CEXAI repository: a complexity score between 0.00 and 0.44 routes to local Ollama (llama3-8B, free), between 0.45 and 0.69 routes to Claude Sonnet (hybrid, $0.02/request), between 0.70 and 1.00 routes to Claude Opus (cloud, $0.15/request). The cost difference is 75x between the cheapest and most expensive tier. At scale, this routing arithmetic determines budget.

### Pattern 3: Sin-Lens Specialization via nucleus_def

CEXAI's most distinctive P02 pattern is encoding "Artificial Sins" as objective function constraints. The 7 nuclei each carry a sin lens that shapes every ambiguous decision:

```yaml
nucleus_def:
  nucleus_id: n01
  sin_lens: Analytical Envy
  model_tier: sonnet
  routing_domains: [research, analysis, intelligence, competitive]
  quality_target: 9.0
```

The sin lens is not decorative. When N01 (intelligence) faces ambiguous research scope, "Analytical Envy" biases it toward maximum coverage and competitor comparison. When N05 (operations, sin: Gating Wrath) sees a deployment pipeline, it biases toward gating and strict validation. The same input produces different outputs from different nuclei because the objective function is encoded in the identity artifact, not inferred from prompts.

### Pattern 4: Agent-to-Agent Communication via handoff_protocol

The `handoff_protocol` kind formalizes the A2A data contract. It specifies:
- `trigger`: the event that initiates the handoff (e.g., `research_complete`)
- `context_passed`: typed schema of what the sending agent delivers
- `return_contract`: typed schema of what the receiving agent signals back

The research-to-build handoff example: the research agent delivers `findings[]` (with `confidence: float` per item), `sources[]` (with `credibility: float`), a `quality_score` (minimum 7.0 — orchestrator rejects below this), and `seeds[]`. The build agent responds with `artifact_path`, `quality_score`, `tests_passed`, and `commit_sha`.

This was validated in production: Mission ISOFIX had the research agent deliver 47 findings; the build agent executed 7 batches creating 820+ files; final quality score 9.0.

---

## Architecture Deep Dive

### The "Artificial Sins" Pattern: Constraint as Specialization

In cognitive science terms, the sin lens is a prior distribution. A general-purpose agent has a flat prior across all possible responses. A specialized agent with a sin lens has a skewed prior that makes certain outputs more likely.

The operations nucleus with "Gating Wrath" treats ambiguity as an enemy ("Act at 80% certainty"), rejects band-aid fixes ("Fix root cause only"), produces terse authoritative outputs ("No hedging"), and treats downtime as betrayal ("Zero-downtime or wait"). These are not personality traits — they are decision policies encoded in the `lens` kind.

The architectural consequence: seven nuclei with distinct sin lenses produce higher quality outputs on their specialized domains than one general-purpose agent, because each nucleus's prior is aligned with what quality means in that domain.

**Why this matters for everyday AI use:** the next time you have a specialized task — risk analysis, creative writing, financial modeling, code review — try constraining your AI to one optimization target instead of asking it to balance multiple goals. "Find every risk, ignore strengths" outperforms "give me a balanced assessment" for the specific task of risk identification. This is the Artificial Sins insight, applied without any framework, today, with any AI you have.

### The agent_package as Deployment Unit

The `agent_package` kind is the portable format for distributing an AI worker. It bundles 12 files into a self-contained package:

```
manifest.yaml        -> P02 (who the agent is)
system_instruction   -> P03 (how it speaks)
instructions         -> P03 (how it executes tasks)
architecture         -> P08 (system structure)
output_template      -> P05 (output format)
examples             -> P07 (few-shot validation pairs)
error_handling       -> P11 (recovery patterns)
quick_start          -> P01 (onboarding)
input_schema         -> P06 (input validation)
upload_kit           -> P04 (deployment instructions)
```

Each file maps 1:1 to a CEXAI pillar. The same package runs on Claude, GPT, Gemini, or Ollama — the `system_instruction` adapts to provider capabilities but core identity stays constant.

Quality gates at the package level: system instruction max 4096 tokens (fits any LLM context), minimum 2 input/output examples, density >= 0.8, score >= 8.0 for pool promotion, no hardcoded paths.

### Memory Architecture for Agents

The `memory_scope` kind defines how an agent manages state across turns. A 3-layer architecture from the repository:

- **Layer 1 — Buffer**: last 10 messages raw (~2000 tokens). Immediate context.
- **Layer 2 — Summary**: compressed history, triggered when buffer exceeds 10 messages. A cheaper model handles compression. Max 500 tokens.
- **Layer 3 — Entity**: extracted named entities (person, product, date, price). Top 20 by recency + frequency. ~300 tokens.

The assembly order is non-obvious: summary first (background), entities second (reference), buffer last (recent). This ordering is defined in the artifact itself, not in application code.

**For everyday AI users:** when a conversation gets long and the AI starts forgetting earlier context, that is the buffer overflowing. The practical workaround: at the start of the next session, paste a brief "session summary" of what was decided previously. You are manually doing what the `memory_scope` artifact automates in production systems.

---

## Why This Matters For You

**"Most people use AI as a generic assistant. Giving it a specific identity makes it 2-5x more useful for specialized tasks."**

This is not a marketing claim. It is a structural consequence of how language models work. A model without a specified prior defaults to the average of all its training data — which is broad, balanced, and somewhat mediocre for any specific task. A model with a well-defined prior for the specific task you need produces outputs that would require 3x more revision without the identity work.

**"Companies pay $50,000+ for 'custom AI agents' — what they're really paying for is well-defined P02 artifacts: identity, model selection, and behavior rules."**

If you look at what enterprise AI projects deliver, the core deliverable is almost always a set of system prompts and routing rules. The code is commodity. The identity specification is the value. Understanding P02 means you can build what enterprises pay $50K for with a text editor and the models you already have.

**"The difference between a toy chatbot and a production agent is 90% identity definition, 10% code."**

This is the single most important thing to understand about the current state of AI engineering. Most of the complexity in production systems is not the model — it is the specification of who the model is, what it remembers, which model it routes to under which conditions, and how it hands off to other models. That is P02 Model. All of it.

---

## Anti-Patterns as Universal Mistakes

### Anti-Pattern 1: Using the Same Persona for Everything

An AI identity optimized for creative writing will produce weak risk analysis. An AI identity optimized for risk analysis will produce bloodless creative writing. Using the same generic assistant persona for everything produces mediocre output across all use cases — the average of multiple incompatible objectives.

The fix: maintain separate identity setups for each recurring use case. At minimum: one for research/analysis, one for creative work, one for code review.

### Anti-Pattern 2: Never Saving Your Best System Prompts

Every time you stumble onto a persona or instruction that works exceptionally well, you are sitting on a reusable asset. If you do not save it, you will reinvent it the next time — or more likely, produce worse output because you cannot reconstruct the exact phrasing that worked.

The fix: a simple text file per use case. Save the opening persona. Reuse it. This is a boot config by another name.

### Anti-Pattern 3: Loyalty to One Model

Each major AI model has genuine strengths and genuine weaknesses. Routing all tasks to one model means you are getting that model's weaknesses for tasks it is not optimized for. The practical cost is lower output quality and higher per-task cost than necessary.

The fix: know the strength profile of each model you have access to. Route deliberately.

### Anti-Pattern 4: Asking AI to Optimize for Multiple Conflicting Goals

"Be creative AND analytical AND concise AND thorough" gives the AI an impossible objective. It will try to satisfy all constraints simultaneously and produce work that is slightly everything and fully nothing.

The fix: one primary constraint per task. Add secondary constraints only if they do not conflict. If you need both creative and analytical work, do two passes with two different persona setups.

### Anti-Pattern 5: Monolithic System Prompts

Encoding persona, instructions, format requirements, and examples in a single undifferentiated block makes it impossible to update one without risking all the others. When the voice needs to change, you are editing the same text that controls the task logic.

The P02 pattern separates these: `agent` (capability spec) + `personality` (voice layer) + `boot_config` (provider-specific startup) + `memory_scope` (state management). Independently versioned, independently replaceable.

---

## Real Examples from the Repository

### Example 1: Model Cascade Fallback Chain

```yaml
id: p02_fb_model_cascade
kind: fallback_chain
pillar: P02
chain:
  - {model: opus, timeout: 30, max_retries: 1}
  - {model: sonnet, timeout: 15, max_retries: 1}
  - {model: haiku, timeout: 5, max_retries: 2}
trigger_conditions: [timeout, rate_limit, 5xx_error, context_overflow]
```

The cascade is strictly sequential — never skip a tier. Cost matrix: opus at $15/$75 per 1M tokens (100% baseline), sonnet at 20% cost, haiku at 2% cost. Monitoring alert at 15% cascade rate over 5 minutes.

What makes this artifact useful: the `trigger_conditions` field is machine-readable. An implementation can programmatically read this artifact and configure retry behavior without hardcoding anything.

### Example 2: N07 Orchestrator Nucleus Definition

```yaml
id: p02_nd_n07
kind: nucleus_def
nucleus_id: N07
sin_lens: "Orchestrating Sloth"
cli_binding: claude
model_tier: opus
model_specific: claude-opus-4-6
context_tokens: 1000000
pillars_owned: [P12]
domain_agents: [agent_dispatcher, agent_consolidator]
fallback_cli: codex
```

"Orchestrating Sloth" is deliberately paradoxical. The sin is sloth — laziness, aversion to unnecessary work. Applied to an orchestrator, this means N07 never builds directly (always delegates), never re-asks questions already answered in the decision manifest, and optimizes for minimal token burn per dispatched wave. The sin is the objective function: do less to achieve more.

### Example 3: Complexity Router

The router computes a weighted score from 6 factors and routes to one of three tiers. The specification in the artifact captures factors, weights, thresholds, and edge cases in a form that any engineer — or any LLM — can read and implement without clarifying questions:

```python
def complexity_score(request: dict) -> float:
    factors = {
        "token_est": estimate_tokens(request) / 4096,
        "reasoning": classify_reasoning_depth(request),
        "tools": min(len(request.get("tools", [])) / 4, 1.0),
        "domain": domain_specificity(request["intent"]),
        "output": output_complexity(request.get("format", "text")),
        "multi_step": count_dependencies(request) / 5,
    }
    weights = {"token_est": 0.20, "reasoning": 0.25, "tools": 0.15,
               "domain": 0.20, "output": 0.10, "multi_step": 0.10}
    return sum(factors[k] * weights[k] for k in weights)
```

Example calibration: "What's the capital of France?" scores 0.033 (routes local, free). "Summarize this 10-page PDF" scores 0.398 (routes hybrid, $0.02). "Design a PCI-compliant payment microservice" scores 0.82 (routes cloud, $0.15).

### Example 4: Research-to-Build Handoff Protocol

The `p02_hp_research_to_build` artifact encodes the full agent-to-agent contract. Key enforcement points: `quality_score >= 7.0` is a hard gate (orchestrator rejects below this and requests a redo); `findings[]` requires a `confidence: float` per finding; `sources[]` requires a `credibility: float` per source. The `return_contract` specifies `commit_sha` — the build agent must commit its output before signaling complete.

This was validated in production: Mission ISOFIX had the research agent deliver 47 findings with paths to missing files; the build agent executed 7 batches creating 820+ artifacts; final score 9.0.

---

## Connection to Other Pillars

**P02 → P03 (Model Identity Shapes Prompt Construction)**

The `nucleus_def` kind (P02) directly influences how prompts are assembled in P03. The `sin_lens` field is injected into the system prompt as a behavioral prior. The `agent` kind's `model_ref` determines context window limits that govern prompt budgeting. P02 defines WHO speaks; P03 defines WHAT is said.

**P02 → P08 (Agent Card as Deployment Manifest)**

The `agent_card` (P08) is the deployment-facing view of an agent. It differs from `agent` (P02): `agent` is the specification (what the agent IS); `agent_card` is the deployment manifest (what a consuming system needs to know to route work to this agent). N07 reads `agent_card` artifacts to build its routing table. The data flows one way: P02 definitions inform P08 deployment artifacts, not the reverse.

**P02 → P12 (Role Assignment Enables Crew Composition)**

The `role_assignment` kind binds `role_name -> agent_id` with explicit responsibilities, backstory, and delegation rules. This is the connection point to P12 `crew_template` — crews reference role_assignments, role_assignments reference agents. You cannot compose a crew without first having well-formed P02 agent definitions with matching role_assignments.

**P02 → P10 (Memory Scope Feeds Session State)**

The `memory_scope` kind (P02) defines the memory configuration, but the actual runtime state lives in P10 (`entity_memory`, `knowledge_index`, `memory_summary`). P02 is the specification; P10 is the runtime. Changing the `memory_scope` artifact changes what state P10 manages, but the state itself persists in P10 stores.

**P02 → P07 (Axioms Feed Quality Gates)**

The `axiom` kind (P02) encodes immutable principles that feed into quality gates (P07). The Shokunin quality axiom ("no artifact enters the pool with score below 7.0") is referenced by quality gates across all pillars. Axioms are the highest-priority invariants — they cannot be overridden by individual artifact configurations.

---

## Summary for Practitioners

P02 Model is where agent intelligence becomes infrastructure. The pillar's 23 kinds cover the full spectrum from identity specification (`agent`, `nucleus_def`) through model selection (`model_card`, `model_provider`, `fallback_chain`, `router`) to runtime behavior (`boot_config`, `memory_scope`, `handoff_protocol`) and cultural encoding (`lens`, `personality`, `axiom`).

The architectural principle that unifies all 23 kinds: **identity must be typed, versioned, and independently deployable.** An agent's persona, its model choice, its memory configuration, and its inter-agent contracts are all separate typed artifacts with explicit quality gates. This is what separates typed agent infrastructure from ad-hoc system prompt engineering.

For practitioners building at any scale — from one AI conversation per day to production multi-agent systems — the same principle applies: define identity before you define capability. Know who your AI is before you ask it to do anything. Save that definition and reuse it. Compose specialized identities for specialized tasks rather than asking one generic identity to do everything.

The 200 words that define who your AI is will do more for the quality of your outputs than any other investment you can make.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_pillar_brief_p02_model_pt]] | translation | 1.00 |
| [[kc_pillar_brief_p01_knowledge_en]] | sibling | 0.85 |
| [[cm_driver_01_structured_thinking]] | downstream | 0.60 |
| [[kc_lens_factory]] | upstream | 0.45 |
| [[kc_lens_index]] | upstream | 0.40 |
| [[mentor_context]] | upstream | 0.38 |
