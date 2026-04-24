# Architecture

CEXAI is a typed knowledge system built on three structural pillars: 12 domain pillars, 8 operational nuclei, and a fractal directory convention that makes every piece of knowledge discoverable and composable.

## The 12 Pillars (P01-P12)

Every artifact belongs to exactly one pillar. Pillars are domain groupings that organize the entire knowledge space.

| Pillar | Domain | What Lives Here | Example Kinds |
|--------|--------|-----------------|---------------|
| P01 | Knowledge | Storage, retrieval, knowledge cards | `knowledge_card`, `chunk_strategy`, `embedding_config` |
| P02 | Model | Agent definitions, providers, identities | `agent`, `model_provider`, `boot_config` |
| P03 | Prompt | Templates, system prompts, chains | `prompt_template`, `system_prompt`, `chain` |
| P04 | Tools | External capabilities, integrations | `cli_tool`, `browser_tool`, `mcp_server` |
| P05 | Output | Production artifacts, rendered output | `landing_page`, `output_template`, `diagram` |
| P06 | Schema | Data contracts, validation, types | `schema`, `validation_schema`, `input_schema` |
| P07 | Evaluation | Quality, scoring, testing, benchmarks | `quality_gate`, `scoring_rubric`, `benchmark` |
| P08 | Architecture | System structure, decisions, patterns | `agent_card`, `component_map`, `interface` |
| P09 | Config | Runtime settings, secrets, feature flags | `env_config`, `rate_limit_config`, `feature_flag` |
| P10 | Memory | State, context, indexing, entity memory | `knowledge_index`, `memory_scope`, `entity_memory` |
| P11 | Feedback | Learning, correction, monetization | `bugloop`, `learning_record`, `content_monetization` |
| P12 | Orchestration | Workflows, dispatch, scheduling, crews | `workflow`, `dispatch_rule`, `schedule` |

Pillar schemas are defined in `N00_genesis/P{01-12}_*/_schema.yaml`.

## The 8 Nuclei (N00-N07)

Each operational nucleus is a specialized AI agent with a domain focus and a "sin lens" -- a cultural DNA that determines what the nucleus optimizes for when given ambiguous input.

### N00 Genesis (Archetype)

N00 is not operational. It is the pre-sin archetype -- the template from which N01-N07 are born. It holds:

- The 12 pillar schemas (`N00_genesis/P{01-12}_*/`)
- The archetype builders (`archetypes/builders/`)
- The kind knowledge cards (`N00_genesis/P01_knowledge/library/kind/`)
- The prompt compiler (`N00_genesis/P03_prompt/layers/`)

### Operational Nuclei (N01-N07)

| Nucleus | Role | Sin Lens | Optimization Bias | Model Tier |
|---------|------|----------|-------------------|------------|
| N01 | Intelligence | Analytical Envy | Competitive analysis, benchmarking | Sonnet |
| N02 | Marketing | Creative Lust | Creative output, aesthetic | Sonnet |
| N03 | Engineering | Inventive Pride | Technical excellence, precision | **Opus** |
| N04 | Knowledge | Knowledge Gluttony | Volume, completeness, depth | Sonnet |
| N05 | Operations | Gating Wrath | Quality gating, enforcement | Sonnet |
| N06 | Commercial | Strategic Greed | Revenue, monetization | Sonnet |
| N07 | Orchestrator | Orchestrating Sloth | Delegation, efficiency | **Opus** |

**Key constraint:** N07 never builds artifacts directly. It decomposes goals, writes handoffs, dispatches to N01-N06, monitors progress, and consolidates results.

### Nucleus Routing

| Domain | Nucleus | When to use |
|--------|---------|-------------|
| Research, analysis, papers | N01 | Market research, competitor intel, large document analysis |
| Ads, campaigns, brand voice, copy | N02 | Marketing content, social media, brand materials |
| Build, create, scaffold, code | N03 | Any artifact construction, engineering tasks |
| RAG, indexing, knowledge cards, docs | N04 | Documentation, knowledge organization, retrieval |
| Debug, test, CI/CD, code review, deploy | N05 | Operations, testing, infrastructure |
| Pricing, courses, funnels, sales | N06 | Commercial strategy, monetization |
| Orchestrate, dispatch, plan | N07 | Multi-nucleus coordination, mission planning |

## Fractal Directory Structure

Every nucleus mirrors the same 12-pillar directory structure. This is the fractal convention -- the same pattern at every scale.

```
N03_engineering/          # Nucleus root
  P01_knowledge/          # Knowledge artifacts
  P02_model/              # Agent/model definitions
    nucleus_def_n03.md    # Machine-readable nucleus identity
  P03_prompt/             # Prompt templates
  P04_tools/              # Tool definitions
  P05_output/             # Output artifacts
  P06_schema/             # Schema definitions
  P07_evals/              # Evaluation artifacts
  P08_architecture/       # Architecture artifacts
    agent_card_n03.md     # Capability declaration
  P09_config/             # Configuration
  P10_memory/             # Memory and state
  P11_feedback/           # Feedback and learning
  P12_orchestration/      # Workflows and crews
    crews/                # Crew templates
  rules/                  # Nucleus-specific rules
  compiled/               # Auto-generated (gitignored)
```

N00_genesis holds the archetype version of this structure. N01-N07 each have their own copy, populated with domain-specific artifacts.

## Inter-Nucleus Communication

Nuclei communicate through three mechanisms:

### 1. Handoffs

N07 writes handoff files to `.cex/runtime/handoffs/` before dispatching. Each handoff contains:

- Task description
- Kind and pillar to produce
- Artifact references (files the nucleus should read)
- Decision manifest reference (GDP decisions from the user)

### 2. Signals

When a nucleus completes work, it writes a signal via `signal_writer.py`:

```python
from _tools.signal_writer import write_signal
write_signal('n03', 'complete', 9.0)
```

Signals are stored in `.cex/runtime/signals/` and monitored by N07.

### 3. Git Commits

Every artifact is committed to git. N07 monitors `git log` to detect when nuclei complete work. This provides a persistent, auditable record of all production.

## Dispatch Modes

| Mode | Command | Parallelism | Use Case |
|------|---------|-------------|----------|
| Solo | `dispatch.sh solo n03 "task"` | 1 builder | Single artifact production |
| Grid | `dispatch.sh grid MISSION` | Up to 6 parallel | Multi-nucleus mission execution |
| Swarm | `dispatch.sh swarm agent 5 "task"` | N builders of same kind | Coverage -- generate variants |
| Crew | `cex_crew.py run name --execute` | N roles with handoffs | Coherent multi-role deliverable |

### Composable Crews

Crews combine multiple roles into a coherent package with defined handoffs. They use 5 WAVE8 primitives:

| Primitive | Pillar | Function |
|-----------|--------|----------|
| `crew_template` | P12 | Reusable recipe with roles table and process topology |
| `role_assignment` | P02 | Binds a role name to an agent with goal and tools |
| `capability_registry` | P08 | Index of all spawnable agents |
| `nucleus_def` | P02 | Machine-readable nucleus identity |
| `team_charter` | P12 | Mission contract with budget, deadline, and quality gate |

Three process topologies: **sequential** (role N waits for role N-1), **hierarchical** (manager delegates), **consensus** (all roles work in parallel, vote on final).

## Runtime Architecture

CEXAI runs on 4 LLM runtimes. Knowledge lives in the repo, not in the runtime:

| Runtime | Model Support | MCP Support | Sub-agents |
|---------|--------------|-------------|------------|
| Claude Code | Opus, Sonnet, Haiku | Full | Yes (5 parallel) |
| Codex CLI | GPT models | None | Limited |
| Gemini CLI | Gemini models | Partial | Limited |
| Ollama | Local models (llama, qwen, gemma) | None | No |

Model routing is configured in `.cex/config/nucleus_models.yaml` with per-nucleus fallback chains.

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `N00_genesis/` | Archetype -- schemas, builders, KCs |
| `N01_intelligence/` through `N06_commercial/` | Nucleus workspaces |
| `N07_admin/` | Orchestrator workspace |
| `archetypes/builders/` | 302 builder definitions (12 ISOs each) |
| `.claude/agents/` | 301 sub-agent definitions |
| `.claude/rules/` | System-wide rules (8F, GDP, dispatch-depth) |
| `.claude/commands/` | Slash command definitions |
| `.cex/` | Runtime state, config, brand, cache |
| `_tools/` | 144 Python tools |
| `_spawn/` | Dispatch infrastructure |
| `boot/` | PowerShell boot scripts |
| `cex_sdk/` | SDK runtime (100+ Python modules) |

## Related Pages

- [[8F Pipeline]] -- The reasoning protocol every nucleus follows
- [[Kinds]] -- The 300 artifact types organized by pillar
- [[Commands]] -- Dispatch, build, and orchestration commands
- [[Contributing]] -- How to add new nuclei (N08+)
