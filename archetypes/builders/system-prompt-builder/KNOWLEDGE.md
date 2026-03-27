---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for system_prompt production
sources: OpenAI, Anthropic, Google, LangChain, constitutional AI literature, distilled from 5 production system prompts
---

# Domain Knowledge: system_prompt

## Foundational Concept
System prompts define LLM identity, capabilities, constraints, and format. Processed before user input. Primary mechanism for turning a general-purpose LLM into a specialist.

## 1. Identity — Dense and Front-Loaded

Format: `You are **{agent_name}**, a specialized {domain} agent focused on {core_mission}.`

| Frequency | Elements |
|-----------|----------|
| Always (5/5) | Agent name, domain, primary mission |
| Usually (3-4/5) | Confidence tier, quality target, operating modes |
| Never works | Instructions before identity, vague "helpful assistant" |

## 2. ALWAYS/NEVER Rules

Binary constraints beat prose. 5-12 ALWAYS, 3-8 NEVER per prompt.

| Concern | ALWAYS | NEVER |
|---------|--------|-------|
| Scope | Verify before acting | Execute outside domain |
| Quality | Validate every output | Skip quality checks |
| Safety | Log errors with context | Fail silently |
| Comms | Respond in target language | Jargon without explanation |

Group rules by concern. Include brief "why" or heading that implies reasoning.

## 3. Knowledge Boundary

- Pair positive scope with negative scope ("You know X" + "You do NOT do Y")
- List explicit tools, delegation boundaries, confidence tiers
- Without negative scope, model attempts answers outside its domain

## 4. Tone Calibration

| Audience | Tone | Markers |
|----------|------|---------|
| Consumers | Informal, warm | Short sentences, first-person |
| Developers | Technical, concise | Code examples, no fluff |
| Auditors | Formal, evidence-based | CWE refs, severity levels |
| Orchestrators | Structured | Decision matrices, pseudocode |

## 5. Size and Sections

| Metric | Sweet Spot | Range |
|--------|-----------|-------|
| Total lines | 300-400 | 230-453 |
| Body tokens | 3,000-3,500 | 2,500-4,500 |
| Identity | 8-15 lines | 5-25 |
| Rules count | 8-12 | 5-20 |
| Max body bytes | 4,096 | - |

**Always**: Identity, capabilities, workflow, quality gates.
**Usually**: Error handling, output format, code examples.
**Never in system_prompt**: Task instructions, conversation history, training data.

## 6. Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| Identity buried past paragraph 2 | Lead with identity, always first |
| Rules as prose | Use ALWAYS/NEVER bullet lists |
| No negative scope | Add "I do NOT" section |
| Mixing identity and task | system_prompt=identity, instruction=task |
| No output format spec | Define JSON/markdown schema |

## Industry Alignment

| Source | Alignment |
|--------|-----------|
| OpenAI system message | Identity + instructions + format |
| Anthropic system prompt | Persona + rules + constraints |
| Google system instruction | Role + behavior + output format |
| Constitutional AI (Bai 2022) | Informs ALWAYS/NEVER pattern |

## Boundary

| Type | Why NOT system_prompt |
|------|----------------------|
| action_prompt | Task execution, not identity |
| instruction | Procedural, not persona |
| prompt_template | Template mechanics, not identity |
| user_prompt | Ephemeral task, not persistent |
| mental_model | Design-time blueprint, not runtime |
