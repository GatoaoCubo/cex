---
quality: 8.4
id: kc_pillar_brief_p03_prompt_en
kind: knowledge_card
pillar: P03
title: "P03 Prompt — Prompts Are Programs"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
language: en
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p03, prompt, chains, reasoning, cot, system-prompt, llm-engineering]
tldr: "Deep technical brief on P03 Prompt: 21 kinds covering prompt templates, chains, reasoning strategies, context windows — universal prompt engineering patterns."
source_concepts: [kc_lens_index, mentor_context, p03_pc_cex_universal]
related:
  - kc_pillar_brief_p03_prompt_pt
  - kc_pillar_brief_p02_model_en
  - kc_pillar_brief_p04_tools_en
  - cm_driver_01_structured_thinking
  - kc_lens_factory
density_score: 0.81
updated: "2026-04-22"
---

# P03 Prompt — The Language Layer of Typed AI Infrastructure

## Universal Principle: Prompts Are Programs

Most people treat prompts as questions. They type something into ChatGPT, get something back,
wonder why it was not quite right, and try again with slightly different wording. This is
the equivalent of debugging code by randomly changing words and hoping for the best.

The real insight: **prompts are programs written in natural language**. Every prompt you
write is an instruction set for the most sophisticated execution engine ever created. The
quality of your output is directly proportional to the quality of your program. Not your
luck, not the AI's intelligence — your program.

This reframing is not just philosophical. It has immediate practical consequences:

**Programs are structured.** Random strings of text are not programs. A program has inputs,
a defined execution context, constraints, and an expected output shape. When you write a
prompt with these four elements explicit, you stop being a user and start being an engineer.

**Programs are reusable.** The best prompts you write today should work tomorrow, next month,
and with the next model release. If your prompts live in a chat window and disappear when
you close the tab, you are throwing away your most valuable LLM assets.

**Programs are composable.** Complex tasks break into steps. Each step is a focused,
testable unit. Chain them together. The output of step one becomes the input to step two.
This is how you build reliable AI workflows from simple, verifiable pieces.

**Programs have versions.** When you find a prompt that reliably produces great output,
freeze it. Save it. Name it. When you improve it, keep the old version. When something
breaks, you can diff version 1 against version 2 and find exactly what changed.

This is what P03 Prompt teaches: not tricks and hacks for a specific AI platform, but the
engineering discipline that makes YOUR AI usage systematically better — with ChatGPT,
with Gemini, with Claude, with local Llama models running on your laptop.

---

## The 3-Layer Architecture That All Good AI Usage Follows

Every effective AI interaction — whether you are using the chat interface, building an
application, or running a local model — shares the same three-layer structure. Understanding
this structure is the most immediately actionable thing in this entire pillar.

```
Layer 1: SYSTEM   — WHO the AI is for this session
Layer 2: CONTEXT  — WHAT it knows and what constraints apply
Layer 3: ACTION   — WHAT you want it to do right now
```

Here is what this looks like in practice, and it works identically with any AI:

**SYSTEM (who):**
"You are a senior copywriter specializing in B2B SaaS landing pages. You write in a
direct, benefit-first style. You never use passive voice. You always lead with the
customer's pain, not the product's features."

**CONTEXT (what you know):**
"Our product is a time-tracking tool for remote teams. Our target customer is an
operations manager at a 50-100 person company. Their main pain is that remote
employees forget to log hours, and they cannot bill clients accurately. Our current
conversion rate on the homepage is 1.2%. We want to double it."

**ACTION (what to do):**
"Write three alternative hero section headlines and subheadlines. For each, identify
the specific pain it targets. Format as: Headline | Subheadline | Pain targeted."

Without the SYSTEM layer, the AI has no role and produces generic output. Without the
CONTEXT layer, it has no domain knowledge and makes up plausible-sounding details.
Without the ACTION layer, it does not know what form the output should take.

Three layers. Every time. This is not a CEXAI pattern — this is how every well-engineered
LLM interaction works. It maps to the universal pattern: persona + context + task.

---

## Why Chains Beat Single Prompts

Here is the honest truth about complex tasks: no single prompt, no matter how well crafted,
will reliably produce high-quality complex output. The reason is architectural, not stylistic.

LLMs generate tokens one at a time, left to right. Each token influences the next.
When you ask for a complete marketing plan in one prompt, the model has to simultaneously
maintain the strategic frame, write tactical recommendations, ensure consistency, format
correctly, and stay within your requirements — all in a single linear generation pass.

Chains solve this by breaking the generation into focused steps, each with its own
context window, its own constraints, and its own quality verification. The output of
each step becomes the input to the next.

**Practical example — marketing content from scratch:**

Instead of: "Write me a full marketing campaign for our product launch."

Try this chain:
- **Step 1:** "List 5 distinct customer segments for [product]. For each: segment name, core job they hire the product for, top fear about switching tools."
- **Step 2:** "Given this segment analysis: [paste step 1 output]. Which segment has the highest urgency AND the fewest strong alternatives? Explain in 3 sentences."
- **Step 3:** "For the [winning segment from step 2], list their 3 most specific pain points — the ones they would describe to a colleague, not marketing speak."
- **Step 4:** "Write 3 landing page hero headlines targeting each of these pain points: [paste step 3]. Each headline must be under 10 words and make a specific, provable claim."
- **Step 5:** "Of these headlines, which would perform best for cold traffic with no brand awareness? Explain your reasoning. Then write a 200-word body copy paragraph for that headline."

The result of this chain is infinitely better than any single-prompt approach because:
1. Each step is verifiable — you can check that step 2 made a defensible choice
2. Each step informs the next with actual output, not hallucinated assumptions
3. If step 4 is weak, you fix that prompt in isolation — you do not restart everything
4. The chain is reusable: substitute a different product in step 1 and run the whole chain again

This is `chain` thinking, and it works with any AI. You do not need infrastructure. You
can do this in any chat window by pasting the output of each step into the next message.

---

## Reasoning Strategies: How to Make AI Think Better

The single most underused technique in LLM usage is controlling HOW the AI reasons,
not just WHAT it produces. Most people optimize for output format. The real leverage
is in the reasoning process.

### Chain-of-Thought (CoT): "Think Step by Step"

Adding "think step by step" or "show your reasoning" to any complex question
measurably improves accuracy — by 20 to 40 percent on reasoning-heavy tasks in
controlled experiments. The reason is that LLMs process tokens sequentially. When
you force explicit intermediate steps, the model cannot skip to a plausible-sounding
conclusion while skipping the actual reasoning.

**Any AI, right now:** Instead of "What pricing tier should I use?", ask:
"Think through this step by step: [describe situation]. First, identify what information
is most critical. Then analyze each option against that criterion. Then give your
recommendation with the specific reason it wins."

You are not asking for a different output. You are asking for a different reasoning path.
The output quality difference is significant and immediate.

### Tree-of-Thought (ToT): Consider Multiple Paths

Chain-of-thought is linear — one path through the problem. For complex decisions,
you want the AI to consider multiple approaches before committing to one.

**Prompt pattern:** "Consider three different approaches to solving [problem].
For each approach: describe the approach in one sentence, list its two biggest advantages,
list its two biggest risks. Then evaluate which approach has the best risk-adjusted outcome
given [specific constraints]. Make a recommendation."

This is Tree-of-Thought without any special infrastructure. Just explicit multi-path
reasoning. Use it when you are making significant decisions, architectural choices,
or complex analyses where a single-path answer is likely to miss something important.

### ReAct: Think, Then Act, Then Reflect

For tool-using agents and multi-step workflows, ReAct (Reason + Act) produces
dramatically better results than just issuing commands. The pattern: the agent reasons
about what to do, takes an action, observes the result, and then reasons again before
the next action.

**Prompt pattern for any complex task:** "Before taking any action on [task], first:
(1) State what you know and what you need to find out. (2) List the three most likely
approaches. (3) Identify the first action that would give you the most information.
Then proceed, but pause after each major step to reassess."

### Self-Consistency: Ask Multiple Times, Take the Majority

For factual questions where you need high confidence, ask the same question three
different ways (or ask the AI to answer three times with different reasoning paths) and
look for convergence. When multiple independent reasoning paths reach the same conclusion,
confidence in that conclusion is justified. When they diverge, you have identified an
ambiguous or genuinely uncertain question that needs more information.

**Practical use:** "Answer this question three times, using a different reasoning
approach each time. Then tell me which answer you are most confident in and why."

### Few-Shot: Show, Do Not Just Tell

Instead of describing the format you want, show it. Give three examples of input-output
pairs, then present the new input. This is one of the most reliable prompt engineering
techniques and it works with every AI.

**Template:** "Here are three examples of what I want:
Example 1: [input] -> [output]
Example 2: [input] -> [output]
Example 3: [input] -> [output]
Now do the same for: [new input]"

The AI learns the pattern from examples, not from your description of the pattern.
For format-sensitive tasks (tone, structure, length, style), examples beat instructions.

---

## The 21 Kinds in P03 — Reframed as Universal Capabilities

P03 Prompt contains 21 typed artifact kinds. CEXAI uses them as structured, versioned
engineering artifacts. Here is how each maps to something every AI user can benefit from
immediately, regardless of what tools you use.

### Identity and Runtime Layer (3 kinds)

| Kind | What it is for any AI user | Practical takeaway |
|------|---------------------------|-------------------|
| `system_prompt` | The 200-400 words that define WHO your AI IS for this session | Write a system prompt for every recurring task you use AI for. Re-use it. The system message is the highest-leverage position in any prompt. |
| `context_file` | Standing instructions that apply to EVERY conversation in a workspace | If you use ChatGPT custom instructions, Claude projects, or Cursor rules — this is what you are building. Invest in making these great. |
| `constraint_spec` | What the AI must NOT do — negative space instructions | Constraints are often more powerful than positive instructions. "Do not use jargon. Do not exceed 150 words. Do not speculate beyond the provided data." Write a constraint list for every deployment. |

### Template and Parameterization Layer (4 kinds)

| Kind | What it is for any AI user | Practical takeaway |
|------|---------------------------|-------------------|
| `prompt_template` | A saved prompt with [BLANK] slots you fill each time | Build a library of templates. "You are a [ROLE] helping a [AUDIENCE] with [TASK]. Use [TONE] tone. Output in [FORMAT]." Save these in a notes app, a doc, anywhere. |
| `action_prompt` | The specific task you send in a given session | This is your standard user message. Make it specific, structured, and format-explicit. |
| `prompt_version` | A saved, frozen version of your best prompt | When you find something that works reliably, save it with a date and note. This is version control for prompts. |
| `instruction` | Step-by-step procedural guides included by reference | For complex agents, write the procedure once and reference it everywhere instead of repeating it. |

### Orchestration and Composition Layer (4 kinds)

| Kind | What it is for any AI user | Practical takeaway |
|------|---------------------------|-------------------|
| `chain` | Multi-step prompt sequences where each output feeds the next | See the chain example above. Build chains for any complex deliverable. |
| `planning_strategy` | Explicit instructions on HOW the AI should plan before acting | Tell the AI your preferred planning approach: "Before writing, create an outline. Before coding, write pseudocode. Before deciding, list the criteria." |
| `prompt_compiler` | A system that maps vague input to precise AI instructions | This is what separates accidental AI use from systematic AI use. It is the pre-filter that turns "write something about marketing" into a precise task. |
| `multimodal_prompt` | Prompts that work across text, images, and audio | As AI becomes multimodal, cross-modal prompting becomes a core skill. |

### Reasoning and Cognition Layer (4 kinds)

| Kind | What it is for any AI user | Practical takeaway |
|------|---------------------------|-------------------|
| `reasoning_strategy` | HOW the AI thinks, not just what it produces | Apply CoT, ToT, or ReAct patterns explicitly. Do not leave the reasoning process to chance. |
| `reasoning_trace` | A saved record of the AI's step-by-step thinking | For important decisions, ask the AI to show all its reasoning. Save it. Audit it. |
| `prompt_technique` | Documented, named techniques (few-shot, role, self-ask) | Build your personal library of techniques. Name them. Reuse them. |
| `prompt_optimizer` | Automated analysis of what makes a prompt weak or strong | When a prompt consistently underperforms, analyze it systematically: is it missing context? Is the task ambiguous? Are the constraints too loose? |

### Meta and Configuration Layer (1 kind)

| Kind | What it is for any AI user | Practical takeaway |
|------|---------------------------|-------------------|
| `context_window_config` | How much your AI can "see" at once — and how to use it wisely | Understand your model's context window: GPT-4o (128K), Claude (200K-1M), Gemini (1M). Bigger is not always better — focused, relevant context beats raw length. |

### Cross-Domain Kinds (6 kinds)

These live in P03 because they are primarily linguistic artifacts: `tagline` (brand
identity phrase), `webinar_script` (structured presentation artifact), `sales_playbook`
(sales conversation framework), `churn_prevention_playbook` (customer retention plays),
`expansion_play` (account growth plays). Each is a specialized prompt-driven document.

---

## Token Budgets: Why Efficiency Is Money

A 4,000-token prompt costs approximately $0.01 with GPT-4o. A 40,000-token prompt costs
$0.10. Run a 40,000-token prompt 1,000 times in a production application and that is $100
per 1,000 calls instead of $10. Multiply by application scale and token efficiency becomes
a genuine business concern.

But token budgets are not only about cost. They are about quality. Here is the counter-
intuitive truth: **shorter, more focused prompts often produce better output than
longer ones**. Adding irrelevant context does not help the model — it dilutes the signal.

The principle that governs token budgets in any serious AI system:

```
Priority 1: Identity (system prompt, persona) — never evict
Priority 2: Task specification (what to do, format, constraints)
Priority 3: Relevant domain knowledge (examples, facts, context)
Priority 4: Conversation history (recent turns only)
Priority 5: Generated output headroom (space to respond)
```

When your context window fills up, start evicting from the bottom of this list, not the top.
A model that knows who it is and what to do with minimal context will outperform a model
that has been given everything but lost track of its identity and task.

In CEXAI, this is managed via a `context_window_config` artifact. In any AI tool, you can
apply the same discipline manually: before submitting a complex prompt, ask yourself —
what can I remove from this that the AI does not actually need?

---

## Key Engineering Patterns

### Pattern 1: The Three-Layer Prompt Architecture

Every production prompt in CEXAI is assembled from three distinct layers, each a separate
typed artifact:

```
Layer 1: system_prompt     -- WHO the agent is (identity, behavioral rules)
         context_file      -- WHERE it is (workspace context, standing instructions)
Layer 2: action_prompt     -- WHAT it should do now (task, inputs, expected output)
Layer 3: constraint_spec   -- HOW generation is bounded (format, tokens, forbidden patterns)
```

The separation is not stylistic. Each layer has a different byte budget:
- `system_prompt`: 4096 bytes max (kept lean — read every turn)
- `context_file`: 8192 bytes (workspace-scoped, injected at session start)
- `action_prompt`: 2048 bytes (task-specific, changes each invocation)
- `constraint_spec`: 2048 bytes (machine-readable rules, JSON format)

### Pattern 2: Chain as Multi-Step Prompt Orchestration

A `chain` is not a workflow. A `chain` (P03) is a sequence of prompt invocations where
output A becomes input B. A `workflow` (P12) involves agents and tools, not just prompts.

Real example from the repository — `ex_chain_content_factory`:

```yaml
steps:
  - name: clarify_brief
    prompt_goal: resolve audience, offer, stage, and CTA
  - name: choose_angle
    prompt_goal: select one strong hook from {{BRAND_CONTENT_THEMES}}
  - name: draft
    prompt_goal: write the first version in {{BRAND_VOICE}}
  - name: tighten
    prompt_goal: remove fluff, sharpen proof, improve CTA
  - name: approve
    prompt_goal: verify accuracy, brand fit, and readiness
```

Each step passes its output as a key to the next step. Chain topology can be `linear`,
`branching` (conditional next step), or `conditional` (early termination on stop condition).
The engineering value: each step can be individually prompted, tested, and versioned as an
`action_prompt`, then wired into the chain.

### Pattern 3: The Prompt Compiler as Intent Resolution Engine

The most architecturally significant kind in P03 is `prompt_compiler`. It is what
separates CEXAI from raw LLM usage.

The canonical instance is `p03_pc_cex_universal.md` — a bilingual (EN + PT-BR) resolution
table mapping 284 natural-language phrase patterns to `{kind, pillar, nucleus, verb}` tuples.

When a user inputs anything — in any language, using any metaphor — the prompt_compiler
resolves it to a precise tuple before the 8F pipeline begins:

```
User: "write me a landing page"
Compiler: kind=landing_page, pillar=P05, nucleus=N03, verb=create

User: "fazer um scraper pro site do concorrente"
Compiler: kind=browser_tool, pillar=P04, nucleus=N05, verb=create

User: "document this API"
Compiler: kind=knowledge_card OR context_doc, pillar=P01, nucleus=N04, verb=create
         (ambiguous -- prompt boundary check: KC=atomic fact, context_doc=long-form)
```

Confidence threshold: 0.60. Below that, top-3 candidates are surfaced. Above that,
auto-resolve and flag with score.

This is the industry equivalent of **intent resolution** (Rasa, Dialogflow, Amazon Lex) —
but applied to a typed artifact taxonomy rather than a dialog action set.

### Pattern 4: context_window_config as Token Budget Management

A `context_window_config` artifact specifies how the available context window is partitioned:

```yaml
total_tokens: 200000       # Sonnet context window
budget_allocation:
  system: 8000             # system_prompt + context_file
  inject: 60000            # P01 knowledge cards + P10 memory
  history: 100000          # conversation turns
  generate: 32000          # model output headroom
overflow_strategy: summarize
```

When multiple context sources compete at F3 INJECT, the config determines which slots get
evicted first under the `priority_tiers` ordering. Without this artifact, context assembly
is implicit and non-reproducible. Different model deployments (8K, 200K, 1M) have different
`context_window_config` instances — the same nucleus logic runs unchanged, only the config switches.

### Pattern 5: reasoning_strategy + reasoning_trace = Auditable Inference

A `reasoning_strategy` defines HOW the model should think. A `reasoning_trace` captures
WHAT it actually thought, step by step, with confidence annotations.

Strategy kinds: CoT (chain-of-thought), ToT (tree-of-thought), self-consistency
(multiple independent reasoning paths + vote), reflexion (self-critique loop), ReAct
(interleaved reasoning and action). Each is a typed artifact with schema fields:
`methodology`, `task_types`, `verification_step`, `confidence_scoring`.

The trace produced is a first-class artifact — it can be scored, stored as a `learning_record`,
used as fine-tuning signal, or fed to an `llm_judge` for evaluation.

---

## Architecture Deep Dive: How P03 Artifacts Flow Through 8F

| 8F Stage | P03 Artifacts Involved |
|----------|------------------------|
| F1 CONSTRAIN | `prompt_compiler` (resolves intent to kind tuple) + `constraint_spec` (loads generation envelope) + `context_window_config` (sets token budget) |
| F2 BECOME | `system_prompt` (identity definition) — the builder "becomes" the nucleus role |
| F2b SPEAK | `context_file` (vocabulary and workspace instructions overlaid before any generation) |
| F3 INJECT | `action_prompt` (task specification) + `prompt_technique` (technique recommendations) + `instruction` (procedural context) |
| F4 REASON | `reasoning_strategy` (applied reasoning protocol) + `planning_strategy` (decomposition method) |
| F5 CALL | `chain` (orchestrates multi-step prompt sequences using tool outputs) |
| F6 PRODUCE | `prompt_template` (hydrated with variables to generate output) |
| F7 GOVERN | `prompt_version` (comparison baseline) + `prompt_optimizer` (quality improvement suggestions) |
| F8 COLLABORATE | `reasoning_trace` (saved as auditable artifact of the inference run) |

The `prompt_compiler` is unique: it runs at F1 CONSTRAIN before 8F starts, making it
the only P03 artifact that operates outside the pipeline proper.

---

## Real Repository Examples

### Example 1: p03_pc_cex_universal.md (prompt_compiler, quality 9.2)

Location: `N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md`

The canonical CEXAI prompt compiler. Key properties:
- Coverage: 284 kinds across 12 pillars
- Languages: PT-BR and EN simultaneously
- Ambiguity resolution: five-step chain with GDP fallback
- Verb resolution table: 27 PT/EN verb pairs mapped to canonical actions and primary 8F function
- Fallback heuristics: TF-IDF via `cex_query.py` -> semantic comparison -> 60% confidence gate -> top-3 GDP

This artifact makes "5 words in, professional artifact out" technically accurate.

### Example 2: p03_sp_cex_core_identity.md (system_prompt, quality 9.1)

Location: `N00_genesis/P03_prompt/layers/p03_sp_cex_core_identity.md`

The base identity block injected into every CEXAI agent. Uses `{{INCLUDE}}` directives:

```
{{INCLUDE p03_ins_doing_tasks}}
{{INCLUDE p03_ins_action_protocol}}
```

The system_prompt is a skeleton; instruction artifacts are its flesh. Changing
`p03_ins_action_protocol` updates every agent that includes it — no mass-editing needed.

### Example 3: p03_ins_action_protocol.md (instruction, quality 9.1)

Location: `N00_genesis/P03_prompt/layers/p03_ins_action_protocol.md`

Defines the blast radius assessment and reversibility check required before any action.
Three tables cover blast radius (local/project/shared/external), reversibility
(easily reversible through irreversible), and six action rules.

### Example 4: ex_chain_content_factory.md (chain, quality 8.7)

Location: `N00_genesis/P03_prompt/ex_chain_content_factory.md`

A five-step linear chain that takes a raw brief and produces publishable content.
Pass-forward data flows through named keys. Uses `{{BRAND_VOICE}}` and
`{{BRAND_CONTENT_THEMES}}` template variables hydrated from `brand_config.yaml` at runtime.

---

## Anti-Patterns: Universal Mistakes in LLM Usage

### Anti-Pattern 1: Prompt Amnesia — Never Saving Your Best Prompts

You spend 20 minutes iterating to find a prompt that works perfectly. Then you close the tab.
Next week you need it again. You start from scratch. This is prompt amnesia, and it is the
single biggest waste in most AI workflows.

Save every prompt that works. Give it a name. Include the context it works best in. Note
what model you tested it on. This is prompt version control and it costs nothing except
the habit of doing it.

### Anti-Pattern 2: One Giant Prompt Instead of a Chain

Writing one massive prompt for a complex task is writing a monolith. When it fails (and it
will), you cannot tell which part failed. When it succeeds, you cannot improve the weak
sections without breaking the whole thing. Break complex tasks into focused steps.

### Anti-Pattern 3: Ignoring System Prompts

The system message is the highest-leverage position in any LLM interaction. It sets role,
constraints, format defaults, and behavioral rules. Most people never write one. They send
raw task messages to a default generic assistant and wonder why the output is generic.

Every recurring task you do with AI deserves a purpose-built system prompt. This is true
whether you use ChatGPT, Claude, Gemini, or a local model.

### Anti-Pattern 4: Asking for Creativity Without Constraints

"Be creative." "Make it interesting." These instructions produce the AI's average idea of
interesting, which is mediocre by definition. The counterintuitive truth: constraints enable
creativity. "Write three headlines for a B2B SaaS product, each under 8 words, each starting
with a number, each targeting a different pain point" produces more interesting output than
"write something creative."

Constraints force the AI off the most obvious path. Use them deliberately.

### Anti-Pattern 5: Stuffing Context Instead of Curating It

Pasting 50,000 tokens of documentation and hoping the AI will find what it needs is not
context management — it is noise injection. Every token in your context window competes for
the model's attention. Irrelevant context dilutes relevant context. The fix: curate.
Include only what the model needs for this specific task. Remove everything else.

### Anti-Pattern 6: Reasoning Without a Strategy

Expecting the model to reason well on complex analytical tasks without an explicit strategy
leaves reasoning behavior undefined. When outputs are inconsistent, there is nothing to
debug against. Specify HOW you want the model to reason, not just WHAT you want it to produce.

### Anti-Pattern 7: Copy-Pasting Prompts Without Adapting

A prompt that works for someone else's context probably does not work for yours. The audience
is different, the product is different, the constraints are different, the model may be different.
Generic prompts from the internet are starting points, not solutions. Always adapt.

---

## Connections to Other Pillars

The prompt pillar is the hub of the 12-pillar system. It sends and receives from every other pillar:

**P01 Knowledge -> P03 Prompt (upstream)**
Knowledge cards are the primary source of injected context for F3 INJECT.

**P02 Model -> P03 Prompt (upstream)**
Agent identity definitions determine what system_prompt values are valid. The `nucleus_def`
artifact defines the nucleus's sin lens, which becomes a required field in the system_prompt.

**P03 Prompt -> P02 Model (downstream)**
The `system_prompt` is the artifact that instantiates the agent: generic LLM + system_prompt
= specialized nucleus. Without P03, P02 model definitions are inert specifications.

**P03 Prompt -> P05 Output (downstream)**
`prompt_template` and `constraint_spec` define the output format. A `constraint_spec` with
`output_format: json` combined with a `prompt_template` that includes an output schema
drives the model to produce structured, parseable output that P05 can consume without post-processing.

**P03 Prompt -> P07 Evaluation (downstream)**
`prompt_version` artifacts are the comparison baseline for quality evaluation. `prompt_optimizer`
uses `scoring_rubric` (P07) criteria to measure improvement between prompt versions.

**P06 Schema -> P03 Prompt (upstream)**
`type_def` (P06) feeds into `prompt_template` by defining the shape of template variables.

**P10 Memory -> P03 Prompt (upstream)**
`memory_summary` (P10) artifacts are injected into the `context` slot of a
`context_window_config`, providing compressed history without consuming the full history budget.

**P11 Feedback -> P03 Prompt (bidirectional)**
`guardrail` (P11) artifacts define safety constraints expressed as `constraint_spec` (P03) fields.
`prompt_optimizer` receives quality feedback from `scoring_rubric` and `learning_record` to drive
iterative improvement.

---

## Why P03 is an Engineering Discipline, Not a Dark Art

The field has spent years treating prompt engineering as intuition-driven iteration: try a
phrase, measure output, adjust the phrase, repeat. P03 makes this a typed, versioned, testable
engineering practice — and the principles translate directly to anyone using any AI.

The key insight is that a `prompt_compiler` makes the system self-documenting. Every
natural-language pattern that successfully resolves to a kind tuple is a registered artifact.
Every ambiguity that triggered a clarification is a signal to add boundary notes. Every quality
failure traced to a prompt is a candidate for `prompt_optimizer` improvement.

For you, without the CEXAI infrastructure: every prompt that works is a pattern worth saving.
Every prompt that fails is a debugging opportunity. Every complex task is a chain waiting to
be decomposed. Every AI interaction is a program waiting to be engineered.

The 21 kinds in P03 cover the full vocabulary of what can happen between user input and
LLM inference. Master this vocabulary and prompt engineering stops being a skill and starts
being infrastructure — infrastructure you can build with any AI you already have access to.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_pillar_brief_p03_prompt_pt]] | translation | 1.00 |
| [[kc_pillar_brief_p02_model_en]] | sibling | 0.85 |
| [[kc_pillar_brief_p04_tools_en]] | sibling | 0.85 |
| [[cm_driver_01_structured_thinking]] | downstream | 0.55 |
| [[p03_pc_cex_universal]] | upstream | 0.70 |
| [[kc_lens_factory]] | upstream | 0.45 |
| [[mentor_context]] | upstream | 0.38 |
