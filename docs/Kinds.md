# Kinds

A **kind** is the atomic artifact type in CEXAI. Every artifact produced by the system is exactly one kind, belongs to exactly one pillar, and is built by exactly one builder.

## What Is a Kind?

Think of a kind as a strongly-typed class for knowledge. Just as a programming language has `int`, `string`, and `boolean`, CEXAI has `knowledge_card`, `agent`, `landing_page`, and 297 others.

Each kind has:

- A **knowledge card** (KC) at `N00_genesis/P01_knowledge/library/kind/kc_{kind}.md`
- A **builder** at `archetypes/builders/{kind}-builder/` with 12 ISOs (one per pillar)
- A **sub-agent** at `.claude/agents/{kind}-builder.md`
- An entry in the **kind registry** at `.cex/kinds_meta.json`

## The Numbers

| Metric | Count |
|--------|-------|
| Total kinds | 300 |
| Builders | 302 |
| ISOs (12 per builder) | 3,647 |
| Kind KCs | 299 |

## Kinds by Pillar

### P01 Knowledge

Kinds for storing, retrieving, and organizing knowledge.

| Kind | Purpose |
|------|---------|
| `knowledge_card` | Structured knowledge unit with frontmatter |
| `knowledge_graph` | Entity-relationship knowledge representation |
| `knowledge_index` | Searchable index over artifacts |
| `chunk_strategy` | How to split documents for RAG |
| `embedding_config` | Vector embedding configuration |
| `rag_source` | Source definition for retrieval-augmented generation |
| `retriever_config` | Retrieval pipeline configuration |
| `glossary_entry` | Controlled vocabulary term definition |
| `citation` | Source citation with provenance |
| `context_doc` | Domain context document |

### P02 Model

Kinds for defining agents, models, and identities.

| Kind | Purpose |
|------|---------|
| `agent` | Complete agent definition |
| `agent_card` | Agent capability declaration (A2A standard) |
| `model_provider` | LLM provider configuration |
| `boot_config` | Agent boot configuration |
| `fallback_chain` | Model fallback sequence |
| `nucleus_def` | Machine-readable nucleus identity |
| `role_assignment` | Binds role to agent in a crew |
| `personality` | Agent persona definition |

### P03 Prompt

Kinds for prompt engineering and composition.

| Kind | Purpose |
|------|---------|
| `prompt_template` | Reusable prompt with variables |
| `system_prompt` | System-level instruction set |
| `action_prompt` | Task-specific prompt |
| `chain` | Multi-step prompt sequence |
| `context_window_config` | Token budget configuration |
| `tagline` | Brand tagline/slogan |
| `prompt_compiler` | Intent-to-prompt transformation rules |
| `context_file` | Workspace instruction file |

### P04 Tools

Kinds for external capabilities and integrations.

| Kind | Purpose |
|------|---------|
| `cli_tool` | Command-line tool definition |
| `browser_tool` | Web browser automation |
| `mcp_server` | Model Context Protocol server |
| `api_client` | API client configuration |
| `webhook` | Webhook endpoint definition |
| `research_pipeline` | Multi-step research automation |
| `messaging_gateway` | Multi-platform messaging integration |

### P05 Output

Kinds for production artifacts and rendered output.

| Kind | Purpose |
|------|---------|
| `landing_page` | Complete web landing page |
| `output_template` | Reusable output format |
| `formatter` | Output formatting rules |
| `parser` | Output parsing/extraction rules |
| `diagram` | Visual diagram definition |

### P06 Schema

Kinds for data contracts and validation.

| Kind | Purpose |
|------|---------|
| `schema` | Data structure definition |
| `validation_schema` | Input/output validation rules |
| `input_schema` | Input data contract |
| `type_def` | Custom type definition |
| `interface` | Integration contract |

### P07 Evaluation

Kinds for quality assurance and testing.

| Kind | Purpose |
|------|---------|
| `quality_gate` | Quality threshold definition |
| `scoring_rubric` | Multi-dimension scoring criteria |
| `benchmark` | Performance benchmark definition |
| `llm_judge` | LLM-as-judge evaluation setup |
| `test_case` | Test scenario definition |

### P08 Architecture

Kinds for system structure and decisions.

| Kind | Purpose |
|------|---------|
| `component_map` | System component inventory |
| `decision_record` | Architecture decision record |
| `naming_rule` | Naming convention definition |
| `capability_registry` | Index of spawnable agents |
| `pattern` | Reusable design pattern |

### P09 Config

Kinds for runtime settings and infrastructure.

| Kind | Purpose |
|------|---------|
| `env_config` | Environment variable configuration |
| `rate_limit_config` | API rate limiting rules |
| `secret_config` | Secret management configuration |
| `feature_flag` | Feature toggle definition |
| `path_config` | File path configuration |
| `terminal_backend` | Execution backend configuration |
| `hibernation_policy` | Idle resource management policy |

### P10 Memory

Kinds for state management and context.

| Kind | Purpose |
|------|---------|
| `entity_memory` | Named entity memory store |
| `memory_scope` | Memory boundary definition |
| `memory_summary` | Compressed memory snapshot |
| `prompt_cache` | Cached prompt compilation |
| `user_model` | User preference profile |

### P11 Feedback

Kinds for learning, correction, and monetization.

| Kind | Purpose |
|------|---------|
| `bugloop` | Automated bug detection and fix loop |
| `learning_record` | Session learning capture |
| `regression_check` | Quality regression detection |
| `guardrail` | Safety constraint definition |
| `content_monetization` | Revenue model for content |
| `revision_loop_policy` | Iteration and revision policy |
| `curation_nudge` | Persistent curation prompt |

### P12 Orchestration

Kinds for workflows, dispatch, and coordination.

| Kind | Purpose |
|------|---------|
| `workflow` | Multi-step process definition |
| `dispatch_rule` | Nucleus dispatch routing rule |
| `schedule` | Timed task schedule |
| `crew_template` | Multi-role team recipe |
| `team_charter` | Mission contract for a crew |
| `pipeline_template` | Scenario-specific pipeline definition |

## How to Find the Right Kind

CEXAI uses intent resolution to map natural language to kinds. You do not need to memorize the taxonomy.

**Method 1: Just describe what you want**

The [[8F Pipeline]] (F1 CONSTRAIN) automatically resolves your intent:

```
"make me a landing page"     --> kind=landing_page, pillar=P05
"document this API"          --> kind=knowledge_card, pillar=P01
"create an agent"            --> kind=agent, pillar=P02
"write a prompt template"    --> kind=prompt_template, pillar=P03
"design pricing tiers"       --> kind=content_monetization, pillar=P11
```

**Method 2: Query the registry**

```bash
python _tools/cex_query.py "research pipeline"
```

Uses TF-IDF to find matching builders from the 302-builder registry.

**Method 3: Browse the kind registry**

The full registry lives at `.cex/kinds_meta.json` (300 entries). Each entry includes:

- `kind`: canonical name
- `pillar`: P01-P12
- `nucleus`: default producing nucleus
- `requires_external_context`: whether the kind needs web/API context

## Builder ISOs

Every builder has 12 ISOs, one per pillar:

| ISO | Pillar | Purpose |
|-----|--------|---------|
| `bld_knowledge_{kind}.md` | P01 | Domain knowledge for this kind |
| `bld_model_{kind}.md` | P02 | Builder identity and role |
| `bld_prompt_{kind}.md` | P03 | Prompt engineering for this kind |
| `bld_tools_{kind}.md` | P04 | Tool usage instructions |
| `bld_output_{kind}.md` | P05 | Output format specification |
| `bld_schema_{kind}.md` | P06 | Schema and validation rules |
| `bld_eval_{kind}.md` | P07 | Quality evaluation criteria |
| `bld_architecture_{kind}.md` | P08 | Structural patterns |
| `bld_config_{kind}.md` | P09 | Configuration options |
| `bld_memory_{kind}.md` | P10 | Memory and context handling |
| `bld_feedback_{kind}.md` | P11 | Feedback and learning |
| `bld_orchestration_{kind}.md` | P12 | Orchestration and composition |

Builders live at `archetypes/builders/{kind}-builder/`.

## Related Pages

- [[Architecture]] -- How kinds fit into the pillar/nucleus structure
- [[8F Pipeline]] -- F1 CONSTRAIN resolves intent to kind
- [[Commands]] -- `/build` produces a single kind; `/mission` produces many
- [[Contributing]] -- How to create a new kind
