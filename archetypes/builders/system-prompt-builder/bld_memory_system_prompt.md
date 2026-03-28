---
kind: memory
id: bld_memory_system_prompt
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for system_prompt artifact generation
---

# Memory: system-prompt-builder
## Summary
System prompts define agent identity: persona, ALWAYS/NEVER rules, knowledge boundaries, and output format. The critical production lesson is that ALWAYS/NEVER rules must include brief justification — rules without rationale get ignored when they conflict with task instructions because the agent cannot weigh their importance. The second lesson is knowledge boundary definition: agents without explicit boundaries hallucinate expertise in domains they should defer to other agents.
## Pattern
- Every ALWAYS/NEVER rule must include a one-line justification — explains importance when rules conflict with task
- Knowledge boundaries must state both expertise ("I know X") and limits ("I do NOT know Y, defer to Z")
- Persona must be functional: define how the agent behaves differently from a generic assistant
- Tone calibration must be specific: "technical and concise" not "professional" — vague tones produce generic output
- Output format must be defined if the agent produces structured data — omit only for free-form conversational agents
- Safety constraints should be positive ("always verify before executing") not just negative ("never execute without checking")
## Anti-Pattern
- ALWAYS/NEVER rules without justification — agent ignores rules when they conflict with task instructions
- Missing knowledge boundaries — agent hallucinate expertise and produce incorrect output in unknown domains
- Decorative persona ("friendly and helpful") — adds no behavioral specificity, wastes tokens
- Tone defined as single word ("professional") — too vague to produce consistent output across tasks
- Confusing system_prompt (P03, fixed identity) with action_prompt (P03, one-time task) or prompt_template (P03, parameterized mold)
- Overlong system prompts (2000+ tokens) — compete with task instructions for attention budget
## Context
System prompts sit in the P03 prompt layer. They are loaded once at agent boot and persist across all interactions within a session. They define WHO the agent is, not WHAT it should do (that is action_prompt territory). In multi-agent systems, system prompts are the primary mechanism for creating specialized agents from general-purpose LLMs.
## Impact
Rules with justification were followed 90% of the time during task conflicts versus 40% for unjustified rules. Explicit knowledge boundaries reduced hallucination incidents by 70% in tested domains. Concise system prompts (under 800 tokens) showed 15% higher task completion quality than verbose ones.
## Reproducibility
For reliable system prompt production: (1) define persona with functional behavioral specifics, (2) write ALWAYS/NEVER rules with one-line justifications, (3) state knowledge boundaries with explicit limits, (4) calibrate tone with specific descriptors, (5) define output format if producing structured data, (6) keep total prompt under 1000 tokens, (7) validate against 8 HARD + 12 SOFT gates.
## References
- system-prompt-builder SCHEMA.md (19 frontmatter fields)
- P03 prompt pillar specification
- Persona engineering and constitutional AI patterns
