---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for system_prompt production
sources: OpenAI, Anthropic, Google, LangChain, constitutional AI literature, distilled from 5 production system prompts
---

# Domain Knowledge: system_prompt

## Foundational Concept
System prompts are the first message in a conversation that defines the LLM's identity,
capabilities, constraints, and response format. Every major LLM provider (OpenAI, Anthropic,
Google) supports a system/developer message that is processed before user input. The system
prompt is the primary mechanism for turning a general-purpose LLM into a specialist.

## Patterns Distilled from Production Prompts

### 1. Identity Section — Dense and Front-Loaded

Every effective system prompt opens with identity. The pattern across all production examples:

**Format**: 2-4 sentences establishing WHO + DOMAIN + PURPOSE.
```
You are **{agent_name}**, a specialized {domain} agent focused on {core_mission}.
Your purpose is to {primary_value_delivered}.
```

**What works in practice**:
- Bold the agent name on first mention for emphasis
- State the core mission in a single sentence (under 25 words)
- Optionally add operating modes ("You operate in two modes: X and Y")
- Optionally add a philosophy one-liner ("Quality over quantity, signal over noise")

**What always appears** (5/5 production prompts):
- Agent name and role
- Domain / area of expertise
- Primary mission or purpose

**What sometimes appears** (3-4/5):
- Confidence tier or autonomy level (e.g., "T3: Suggest mode — all findings require human validation")
- Quality target (e.g., "Quality Gate: >= 8.0/10 for production outputs")
- Operating modes (API vs manual, autonomous vs guided)

**What never works**:
- Starting with instructions before establishing identity
- Paragraphs of background context before the persona
- Vague descriptions without domain specificity ("you are a helpful assistant")

### 2. ALWAYS/NEVER Rules — Binary Constraints Beat Soft Guidance

Production prompts overwhelmingly use binary constraint lists rather than prose guidance.
LLMs follow explicit binary rules more reliably than nuanced suggestions.

**Observed counts**: 5-12 ALWAYS rules, 3-8 NEVER rules per prompt.

**Effective rule format**:
```markdown
ALWAYS:
- Verify input format before processing
- Return structured JSON with all required fields
- Terminate with quality validation

NEVER:
- Execute tasks outside your domain (hand off instead)
- Guess when data is unavailable (ask or fail gracefully)
- Skip quality gates even under time pressure
```

**Pattern: rules cluster by concern**:
| Concern | Example ALWAYS | Example NEVER |
|---------|---------------|---------------|
| Scope | Verify before acting | Execute outside your domain |
| Quality | Validate every output | Skip quality checks |
| Safety | Log errors with context | Fail silently |
| Communication | Respond in target language | Use jargon without explanation |

**Anti-pattern**: Rules without justification. The best prompts include a brief "why"
or group rules under a heading that implies the reasoning (e.g., "Brand Compliance Rules",
"Security Rules").

### 3. Knowledge Boundary — Explicit Scope Prevents Hallucination

Every high-scoring prompt defines what the agent knows AND what it does not know or do.

**Pattern**: Pair positive scope with negative scope.
```markdown
## Your Knowledge
You have expertise in: {domain_1}, {domain_2}, {domain_3}

## What You Do NOT Do
- You do NOT execute tasks (you plan and delegate)
- You do NOT generate code (you validate it)
- You do NOT access external APIs directly
```

**Effective approaches observed**:
- **Explicit tool list**: "Tools you have: Glob, Grep, Read, Task, Bash" (agent knows exactly what it can use)
- **Delegation boundaries**: "You orchestrate, not execute — spawn others to do the work"
- **Confidence tiers**: Agent states its confidence level and what that means for autonomy
- **Knowledge domain listing**: Specific topics the agent is authoritative on, with a catchall redirect for everything else

**Anti-pattern**: Omitting negative scope. Without "I do NOT know X", the model will attempt
to answer questions outside its domain using general knowledge.

### 4. Tone Calibration — Match Audience, Not Default

Tone varies dramatically across production prompts and should be an explicit design choice:

| Audience | Tone | Markers |
|----------|------|---------|
| End users (consumers) | Informal, warm, encouraging | "Show!", "Beleza!", first-person, short sentences |
| Developers | Technical, concise, precise | Code examples, specific terminology, no fluff |
| Security auditors | Formal, evidence-based | CWE references, severity levels, remediation templates |
| Orchestrators | Structured, methodical | Decision matrices, routing tables, pseudocode |

**Pattern**: The best prompts include explicit tone instructions:
```markdown
tone: Professional, data-driven  (in frontmatter)
```
Or in body:
```markdown
## Communication Style
- Talk WITH the user, not AT them
- Use "you" not "the users"
- Numbers > adjectives
- Be direct, avoid fluff
```

**When to use formal**: Security, compliance, legal, API documentation.
**When to use conversational**: Teaching, onboarding, customer-facing, creative work.

### 5. Practical Size Observations

| Metric | Observed Range | Sweet Spot |
|--------|---------------|------------|
| Total lines | 230-453 | 300-400 |
| Body tokens (no frontmatter) | 2,500-4,500 | 3,000-3,500 |
| Identity section | 5-25 lines | 8-15 |
| Rules count | 5-20 | 8-12 |
| Max body bytes (schema limit) | - | 4,096 |

Longer prompts (400+ lines) work when the content is structured reference material
(detection patterns, API specs, template catalogs). Shorter prompts (under 300 lines)
work for focused single-domain agents.

**Anti-pattern**: Padding with verbose explanations. Every line in a system prompt
competes for attention weight. If a section can be a table, make it a table.

### 6. Sections That Always Appear vs. Rarely Appear

**Always present (5/5 production prompts)**:
- Identity / persona definition
- Capabilities or responsibilities list
- Workflow or execution steps
- Quality gates or success criteria

**Usually present (3-4/5)**:
- Error handling / recovery strategies
- Output format specification (JSON schema, markdown template)
- Code examples or pseudocode
- Integration points with other agents

**Sometimes present (1-2/5)**:
- Performance targets (requests/second, timeout limits)
- Decision matrices or routing tables
- Changelog or version history
- Jargon glossary or translation table

**Never present in system prompts (belongs elsewhere)**:
- Task-specific instructions (belongs in instruction/action_prompt)
- User conversation history (ephemeral)
- Training data or datasets (external)

### 7. Anti-Patterns Observed

| Anti-Pattern | Why It Fails | Better Approach |
|--------------|-------------|-----------------|
| Identity buried in paragraph 3+ | LLM may not adopt persona consistently | Lead with identity, always first section |
| Rules as prose paragraphs | LLM follows numbered/bulleted lists more reliably | Use ALWAYS/NEVER bullet lists |
| No negative scope | Agent attempts tasks outside its expertise | Add explicit "I do NOT" section |
| Mixing identity and task | Prompt tries to be both persona and instruction | Separate: system_prompt = identity, instruction = task |
| Overly long without structure | Key rules get lost in middle of prompt | Use headers, tables, and code blocks liberally |
| Generic quality standard | "Do good work" is unenforceable | Quantify: "score >= 8.0", "compliance >= 95%" |
| No output format spec | Inconsistent response structure | Define expected JSON/markdown schema |

## Industry Implementations

| Source | What it defines | Alignment |
|--------|----------------|-----------|
| OpenAI system message | Identity + instructions + format | Direct: our system_prompt |
| Anthropic system prompt | Persona + rules + safety | Direct: identity + rules + constraints |
| Google system instruction | Role + behavior + output format | Direct: all 4 body sections |
| LangChain SystemMessagePromptTemplate | Template for system messages | Template wraps this |
| Constitutional AI (Bai 2022) | Self-critique + revision rules | Informs ALWAYS/NEVER pattern |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT system_prompt |
|------|------------|---------------------------|
| action_prompt | Task-focused prompt with input/output | Task execution, not identity |
| instruction | Step-by-step operational recipe | Procedural, not persona |
| prompt_template | Reusable template with {{vars}} | Template mechanics, not identity |
| user_prompt | One-time task from human/orchestrator | Ephemeral task, not persistent identity |
| mental_model | Agent routing/decision map | Design-time blueprint, not runtime prompt |

## References
- OpenAI: Chat Completions API — system message
- Anthropic: System prompts guide
- Bai et al. 2022: Constitutional AI
- LangChain: SystemMessagePromptTemplate docs
- Distilled from 5 production system prompts: design automation bridge, security auditor, orchestration planner, data curator, conversational gateway
