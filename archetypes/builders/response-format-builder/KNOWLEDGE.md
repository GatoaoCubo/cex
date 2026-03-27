---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for response_format production
sources: [OpenAI JSON mode, Anthropic structured output, Instructor, Outlines, real agent output templates]
---

# Domain Knowledge: response_format

## Core Concept

Response formats define HOW an LLM structures output. Injected into prompt so model knows expected shape BEFORE generating. Key: (1) explicit structure with named sections, (2) typed placeholder variables, (3) complete example output. Formats are GUIDANCE, not enforcement — make deviation unlikely by being clear and concrete.

## Industry Alignment

| Source | Defines | Maps to |
|--------|---------|---------|
| OpenAI JSON mode | Force JSON via API | format_type: json |
| Anthropic tool_use | Output via tool schema | Sections with typed fields |
| Instructor | Pydantic as output schema | Field-level type constraints |
| Outlines | Regex-guided generation | Grammar-level (P06) |
| LangChain OutputParser | Parse LLM output | Downstream parser |

## Format Compliance Hierarchy

| Format | Compliance | Best for |
|--------|-----------|----------|
| JSON | ~95% | Machine consumption, APIs |
| YAML | ~90% | Configuration, frontmatter |
| Markdown tables | ~88% | Comparisons, inventories |
| Numbered lists | ~85% | Sequential steps |
| YAML frontmatter + MD | ~85% | Hybrid artifacts |
| Free-form markdown | ~70% | Long-form prose |
| CSV | ~60% | Tabular export |

## Template Variable Patterns

**Pattern 1: Typed Variable Table** — for machine-consumed output:

```
| Variable | Type | Constraints | Example |
|----------|------|-------------|---------|
| {{agent_name}} | string | lowercase | "seo_optimizer" |
| {{confidence}} | float | 0.0-1.0 | 0.92 |
```

**Pattern 2: Inline Contextual** — for identity/narrative templates:
`You are {{agent_name}}, a {{domain}} specialist.`

**Pattern 3: Conditional/Loop** — for variable-length reports:
`{{#FINDINGS}} ### Finding {{N}}: {{TITLE}} {{/FINDINGS}}`

Mark every variable required or optional. Ambiguity = inconsistent output.

## Three Rigidity Zones

| Zone | Rigidity | Example |
|------|----------|---------|
| Fixed structure | 100% | Frontmatter, JSON keys, headers |
| Constrained fill | 70% | Enums, typed vars, length limits |
| Open fill | 30% | `{{description}}`, `{{analysis}}` |

- Frontmatter: all fixed. Body headers: fixed. Body content: constrained to open
- Never mix zones within a single field

## Multi-Format Output

```yaml
mode: full | quick | error
```

Each mode shares envelope (agent, timestamp, status), differs in body detail.

## P05/P06 Boundary

| Aspect | response_format (P05) | validation_schema (P06) |
|--------|----------------------|------------------------|
| Audience | LLM (in prompt) | System only (post-gen) |
| Timing | Before/during gen | After generation |
| Enforcement | Soft (guidance) | Hard (system) |

Write response_format as INSTRUCTIONS TO THE LLM, not system validation rules.

## Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| Untyped `{{value}}` | Add type + example for every variable |
| No example output | Always include >= 1 complete example |
| Mixed format in section | One format per section |
| 10+ sections | Consolidate to 4-7 |
| Vague names (`## Details`) | Action-oriented: `## Remediation Steps` |
| No validation rules | List constraints after template |
| Implicit ordering | Number sections or state order requirement |
