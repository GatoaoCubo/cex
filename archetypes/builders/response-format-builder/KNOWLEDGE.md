---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for response_format production
sources: [OpenAI JSON mode, Anthropic structured output, Instructor, Outlines, real agent output templates, builder output templates]
---

# Domain Knowledge: response_format

## Foundational Concepts

Response formats define HOW an LLM structures its output. They are injected into the prompt so the model knows the expected shape before generating. The core insight from production systems: LLMs follow format instructions dramatically better when given (1) explicit structure with named sections, (2) typed placeholder variables, and (3) a complete example output.

Response formats are GUIDANCE, not enforcement — the LLM may deviate. The builder's job is to make deviation unlikely by being clear, concrete, and consistent.

## Industry Patterns

| Source | What it defines | Alignment |
|--------|----------------|-----------|
| OpenAI JSON mode | Force JSON output via API parameter | format_type: json |
| Anthropic tool_use | Structured output via tool schema | Sections with typed fields |
| Instructor (Python) | Pydantic models as output schema | Field-level type constraints |
| Outlines | Regex-guided generation for format | Grammar-level (P06, not P05) |
| LangChain OutputParser | Parse LLM output into structured data | Downstream parser |

## Format Compliance Hierarchy

Not all formats are equally respected by LLMs. Observed compliance ranking:

| Format | Compliance | Best for | LLM behavior |
|--------|-----------|----------|---------------|
| JSON | Highest (~95%) | Machine consumption, APIs | LLMs trained heavily on JSON; follow schema well |
| YAML | High (~90%) | Configuration, frontmatter | Clean indentation; less nesting confusion than JSON |
| Markdown tables | High (~88%) | Structured comparisons, inventories | Familiar from training data; consistent column alignment |
| Numbered lists | Good (~85%) | Sequential steps, procedures | Natural ordering; LLMs rarely skip or reorder |
| YAML frontmatter + MD body | Good (~85%) | Hybrid artifacts (metadata + prose) | Best of both: structured header + flexible body |
| Free-form markdown | Moderate (~70%) | Long-form prose, reports | LLM may improvise sections or reorder |
| CSV | Low (~60%) | Tabular data export | Quoting/escaping errors common |

## Template Variable Patterns

### The `{{variable}}` Convention

Template variables use double-brace syntax `{{variable_name}}` as placeholders for LLM completion. Three production-proven patterns:

#### Pattern 1: Typed Variable Table
Define each variable with type, constraints, and example in a reference table. The LLM fills variables by consulting the table.

```markdown
| Variable | Type | Constraints | Example |
|----------|------|-------------|---------|
| {{agent_name}} | string | lowercase, no spaces | "seo_optimizer" |
| {{confidence}} | float | 0.0-1.0 | 0.92 |
| {{severity}} | enum | critical|high|medium|low | "high" |
| {{subtasks}} | integer | >= 0 | 3 |
```

**When to use**: Machine-consumed output (JSON, YAML), API responses, structured records.
**Why it works**: Explicit types prevent format drift. Enum constraints reduce hallucination.

#### Pattern 2: Inline Contextual Variables
Variables embedded directly in prose with surrounding context providing implicit typing.

```markdown
You are {{agent_name}}, a {{domain}} specialist.
You produce {{primary_output}} with {{quality_attribute}}, no filler.
```

**When to use**: Identity definitions, narrative templates, human-readable documents.
**Why it works**: Context makes intent obvious; LLM infers type from position.

#### Pattern 3: Conditional/Loop Blocks
Mustache-style sections for repeated or conditional content.

```markdown
{{#FINDINGS}}
### Finding {{FINDING_NUMBER}}: {{TITLE}}
**Severity**: {{SEVERITY}} (CVSS {{CVSS_SCORE}})
{{/FINDINGS}}

{{#IF STATUS == "VERIFIED"}}
Authorized to proceed.
{{/IF}}
```

**When to use**: Reports with variable-length lists, conditional sections.
**Why it works**: Explicit loop/conditional syntax prevents LLM from guessing repetition count.

### Required vs Optional Variables

| Classification | Signal | LLM behavior |
|---------------|--------|---------------|
| Required | Listed in "Required Fields" table, no default value | LLM must fill; empty = validation failure |
| Optional with default | Has `Default` column value | LLM may skip; system uses default |
| Optional without default | Marked "REC" or "optional" | LLM fills if context available; omits otherwise |

**Rule**: Mark every variable as required or optional. Ambiguity causes inconsistent output.

## Rigidity vs Flexibility Balance

The central design tension: too rigid and the LLM produces stilted output; too flexible and output is unpredictable.

### The Three Zones

| Zone | Rigidity | Example | When to use |
|------|----------|---------|-------------|
| **Fixed structure** | 100% rigid | Frontmatter fields, JSON keys, section headers | Metadata, machine parsing, validation |
| **Constrained fill** | 70% rigid | Enum values, typed variables, length limits | Structured content within known categories |
| **Open fill** | 30% rigid | `{{description}}`, `{{analysis}}` | Prose, analysis, creative content |

### Proven Heuristic
- Frontmatter/metadata: **all fixed structure** (exact field names, types, enums)
- Body section headers: **fixed** (ordered, named, required)
- Body section content: **constrained fill** to **open fill** depending on domain
- Never mix zones within a single field — a field is either typed or free-form, not both

## Multi-Format Output Pattern

Production agents often need multiple output formats for different audiences or modes. Proven pattern from routing agents, security tools, and meta-constructors:

```
Format 1: Full mode (all sections, complete detail)
Format 2: Minimal/quick mode (status + path + score only)
Format 3: Error mode (error code + message + recovery action)
```

**Implementation**: Define each format as a separate template section. Use a mode variable to select:
```yaml
mode: full | quick | error
```

Each format shares the same envelope (agent name, timestamp, status) but differs in body detail. This prevents the LLM from producing inconsistent structures across modes.

## The P05/P06 Boundary (critical distinction)

| Aspect | response_format (P05) | validation_schema (P06) |
|--------|----------------------|------------------------|
| Who sees it? | LLM (injected in prompt) | System only (post-generation) |
| When applied? | Before/during generation | After generation |
| Enforcement | Soft (LLM guidance) | Hard (system enforcement) |
| Language | Natural language + examples | Formal constraints (regex, enum) |

**Implication for builders**: Write response_format as INSTRUCTIONS TO THE LLM, not as system validation rules. The LLM reads this text. Use clear language, show examples, state constraints in natural language.

## Anti-Patterns

| Anti-pattern | Why it fails | Fix |
|-------------|-------------|-----|
| Untyped variables | `{{value}}` with no type/example — LLM guesses wrong format | Add type + example for every variable |
| Template without example | Structure description only, no concrete filled output | Always include >= 1 complete example |
| Mixed format within section | JSON keys alongside markdown headers in same block | One format per section; separate machine and human blocks |
| 10+ sections | LLMs lose track after ~7-8 sections | Consolidate related sections; aim for 4-7 |
| Vague section names | `## Details`, `## Other` — no semantic signal | Use action-oriented names: `## Remediation Steps`, `## Risk Assessment` |
| No validation rules | No constraints on field values | List validation rules after template: enums, ranges, required fields |
| Implicit ordering | Sections not numbered or dependency-ordered | Number sections or state: "sections MUST appear in this order" |

## Key Principles Summary

1. **Show, don't just tell**: A complete example output teaches format better than any description
2. **Type every variable**: Type + constraints + example = reliable fill
3. **Fewer sections, higher compliance**: 4-7 sections is the sweet spot
4. **JSON for machines, YAML+MD for humans**: Match format to consumer
5. **Separate modes, shared envelope**: Full/quick/error share metadata, differ in body
6. **Frontmatter is rigid, body is flexible**: Never reverse this
7. **Injection point matters**: system_prompt for persistent format, user_message for per-request

## References
- OpenAI JSON mode: https://platform.openai.com/docs/guides/structured-outputs
- Instructor: https://python.useinstructor.com/
- Outlines: https://github.com/outlines-dev/outlines
- Anthropic tool use: https://docs.anthropic.com/en/docs/build-with-claude/tool-use
