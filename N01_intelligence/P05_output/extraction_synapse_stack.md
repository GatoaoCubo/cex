---
id: extraction_synapse_stack
kind: knowledge_card
8f: F3_inject
pillar: P01_knowledge
title: "Extraction: Synapse 8-Layer Context Stack from aiox-core"
version: 1.1
quality: 8.9
tags: [extraction, synapse, context, layers, prompt_composition, aiox, port]
created: 2026-04-12
updated: 2026-04-13
author: n01_intelligence
domain: prompt composition architecture
source: SynkraAI/aiox-core
tldr: "aiox-core injects context via 8 sequential layers (L0 Constitution -> L7 Star-Command) with bracket-based token budgets. Maps directly to CEX F3 INJECT as a canonical envelope structure."
related:
  - spec_context_assembly
  - kc_model_context_protocol
  - p01_kc_handoff_protocol
  - extraction_gate_severity
  - p01_kc_token_budgeting
  - bld_schema_memory_architecture
  - port_plan_external_repos
  - bld_collaboration_context_doc
  - p01_kc_context_doc
  - bld_instruction_memory_architecture
---

# Extraction: Synapse 8-Layer Context Stack (A1) from aiox-core

## 1. The 8 Layers

aiox-core's SYNAPSE system processes rules through 8 layers, executed
sequentially. Each layer has a trigger condition, priority, and timeout.

| Layer | Name | Trigger | Priority | Timeout | CEX Equivalent |
|-------|------|---------|----------|---------|----------------|
| L0 | Constitution | ALWAYS_ON | HIGHEST | 5ms | `.claude/rules/*.md` (hardcoded rules) |
| L1 | Global + Context | ALWAYS_ON | HIGH | 10ms | `CLAUDE.md` + pillar schemas |
| L2 | Agent-Scoped | AGENT_TRIGGER | MED-HIGH | 15ms | `agent_card_n0x.md` (nucleus identity) |
| L3 | Workflow-Scoped | WORKFLOW_TRIGGER | MEDIUM | 15ms | Mission handoff context |
| L4 | Task Context | Active task | MEDIUM | 15ms | Handoff file (`n0x_task.md`) |
| L5 | Squad Discovery | Active squad | MED-LOW | 15ms | No equivalent (CEX has no squads) |
| L6 | Keyword (RECALL) | Prompt keywords | LOW | 15ms | `cex_retriever.py` (F3 similarity) |
| L7 | Star-Command | User `*command` | HIGHEST | 5ms | `/slash commands` |

### Execution order

```
L0 Constitution -> L1 Global -> L2 Agent -> L3 Workflow -> L4 Task -> L5 Squad -> L6 Keyword -> L7 Star-Command
```

## 2. Implementation Details

### 2.1 Base class (layer-processor.js)

```javascript
class LayerProcessor {
  constructor({ name, layer, timeout = 15 }) {
    this.name = name;
    this.layer = layer;
    this.timeout = timeout;  // milliseconds
  }

  process(context) {
    throw new Error('must implement');
  }

  _safeProcess(context) {
    const start = Date.now();
    try {
      const result = this.process(context);
      const elapsed = Date.now() - start;
      if (elapsed > this.timeout) {
        console.warn(`[synapse:${this.name}] exceeded timeout`);
      }
      return result;
    } catch (error) {
      console.warn(`[synapse:${this.name}] Error: ${error.message}`);
      return null;  // graceful degradation -- layer skipped, pipeline continues
    }
  }
}
```

### 2.2 Layer return type

```javascript
{
  rules: string[],           // array of rule strings (one per line from domain file)
  metadata: {
    layer: number,           // 0-7
    source?: string,         // domain name or agent ID
    nonNegotiable?: boolean, // L0 only
    agentId?: string,        // L2 only
    workflowId?: string,     // L3 only
    matches?: Array,         // L6 keyword matches
    command?: string         // L7 star-command
  }
}
```

### 2.3 Context Bracket System (context-tracker.js)

Token budget varies by how much context window remains:

| Bracket | Context % | Token Budget | Active Layers | Behavior |
|---------|-----------|--------------|---------------|----------|
| FRESH | 60-100% | 800 tokens | [0,1,2,7] | Lean injection |
| MODERATE | 40-60% | 1500 tokens | [0-7] | All layers active |
| DEPLETED | 25-40% | 2000 tokens | [0-7] + memory | L6 keyword skipped |
| CRITICAL | 0-25% | 2500 tokens | [0-7] + memory | Handoff warning |

```javascript
const usedTokens = promptCount * avgTokensPerPrompt * 1.2;  // XML safety multiplier
const contextPercent = 100 - (usedTokens / maxContext * 100);
const bracket = contextPercent >= 60 ? 'FRESH'
              : contextPercent >= 40 ? 'MODERATE'
              : contextPercent >= 25 ? 'DEPLETED'
              : 'CRITICAL';
```

**Key insight**: FRESH bracket injects FEWER rules (only critical ones).
As context depletes, MORE rules are injected to prevent drift. Counter-intuitive
but correct -- early in conversation the model is aligned; late, it needs reminders.

### 2.4 Conflict Resolution

1. **NON_NEGOTIABLE wins** -- L0 Constitution can never be overridden
2. **Higher layer number = more specific** -- L7 overrides L1 for current prompt
3. **Agent > Global** -- L2 overrides L1
4. **Workflow > Agent** -- L3 augments L2
5. **Explicit > Implicit** -- star-commands override automatic rules

### 2.5 Deduplication (L6 keyword layer)

```javascript
// L6 skips domains already loaded by L0-L5
const loadedSources = this._extractLoadedSources(previousLayers || []);
if (loadedSources.has(domainName)) continue;  // dedup
```

### 2.6 Performance targets

| Metric | Target | Hard limit |
|--------|--------|-----------|
| Total pipeline | <70ms | <100ms |
| Individual layer | <15ms | <20ms |
| L0/L7 (critical) | <5ms | <5ms |
| Startup | <5ms | <10ms |

### 2.7 Output format (formatter.js)

```xml
<synapse-rules>
[CONTEXT BRACKET: MODERATE] 40-60% context remaining
[CONSTITUTION] CLI First | Agent Authority | Story-Driven | No Invention | Quality First
[ACTIVE AGENT: @dev] Follow story tasks, update Dev Agent Record only
[ACTIVE WORKFLOW: story_development] Follow SDC phases
[TASK CONTEXT] Current task details
[SQUAD: mmos] Squad-specific rules
[KEYWORD MATCHES] Matched domain rules
[MEMORY_HINTS] Cached memories
[STAR-COMMANDS] *dev: Code over explanation, minimal changes
[LOADED DOMAINS SUMMARY] constitution, global, context, agent-dev, etc.
</synapse-rules>
```

Section ordering is priority-based for truncation: constitution first, summary last.

## 3. CEX Integration Plan: Canonical F3 INJECT Envelope

### Current state

CEX F3 INJECT is **ad-hoc**: each builder/nucleus loads what it remembers to load.
There's no enforced structure ensuring all context layers are present.
`cex_crew_runner.py` (839 lines) does prompt composition but without a defined
layer protocol.

### Proposed: F3 Envelope Structure

Map aiox-core's 8 layers to CEX's domain:

| CEX F3 Layer | Source | aiox Equivalent | Required? |
|--------------|--------|-----------------|-----------|
| **C0: Rules** | `.claude/rules/*.md` | L0 Constitution | ALWAYS |
| **C1: System** | `CLAUDE.md` + `_schema.yaml` | L1 Global | ALWAYS |
| **C2: Identity** | `agent_card_n0x.md` + sin lens | L2 Agent | ALWAYS |
| **C3: Mission** | `decision_manifest.yaml` + GDP | L3 Workflow | IF dispatched |
| **C4: Task** | `n0x_task.md` handoff | L4 Task | IF dispatched |
| **C5: Brand** | `brand_config.yaml` | L5 Squad | IF bootstrapped |
| **C6: Knowledge** | `cex_retriever.py` results + KCs | L6 Keyword | IF relevant |
| **C7: Builder** | 13 builder ISOs | L7 Star-Command | IF building |

### Context budget by conversation depth

Adapt aiox-core's bracket system for CEX's 1M context:

| Bracket | Context % | F3 Budget | Active layers | Notes |
|---------|-----------|-----------|---------------|-------|
| FRESH | 80-100% | 5K tokens | C0,C1,C2,C7 | Lean -- model is aligned |
| WORKING | 40-80% | 15K tokens | C0-C7 all | Full injection |
| DEEP | 10-40% | 20K tokens | C0-C7 + memory | Add explicit reminders |
| CRITICAL | 0-10% | 25K tokens | C0-C7 + full KC | Maximum reinforcement |

### Implementation

Update `_tools/cex_crew_runner.py` to enforce the envelope:

```python
class F3Envelope:
    """Canonical F3 INJECT context assembly."""

    LAYERS = [
        ("C0_rules", load_rules, True),
        ("C1_system", load_system_context, True),
        ("C2_identity", load_agent_card, True),
        ("C3_mission", load_mission_context, False),
        ("C4_task", load_task_handoff, False),
        ("C5_brand", load_brand_config, False),
        ("C6_knowledge", load_retriever_results, False),
        ("C7_builder", load_builder_isos, False),
    ]

    def assemble(self, context: dict) -> str:
        bracket = self.detect_bracket(context)
        active = self.active_layers(bracket)
        sections = []
        for name, loader, required in self.LAYERS:
            if name in active or required:
                content = loader(context)
                if content:
                    sections.append(f"## {name}\n{content}")
        return "\n\n".join(sections)
```

### Files to create/modify

| File | Action | Lines est. |
|------|--------|-----------|
| `_tools/cex_f3_envelope.py` | CREATE -- F3Envelope class | ~150 |
| `_tools/cex_crew_runner.py` | MODIFY -- use F3Envelope in compose() | ~40 |
| `.claude/rules/8f-reasoning.md` | MODIFY -- document C0-C7 layers in F3 section | ~30 |
| `cex_sdk/prompt_compiler.py` | MODIFY -- integrate envelope if present | ~20 |

### Estimated effort

- **Complexity**: Low (refactor existing code into structured layers)
- **Lines of code**: ~150 new + ~90 modified
- **Dependencies**: None
- **Risk**: Low -- formalizes what already happens informally

## 4. Comparative Analysis

| Dimension | aiox-core Synapse | CEX F3 (current) | Proposed CEX F3 Envelope |
|-----------|------------------|-------------------|--------------------------|
| Structure | 8 explicit layers | Ad-hoc per builder | 8 explicit layers (C0-C7) |
| Token budget | Bracket-based (800-2500) | Fixed (no budget) | Bracket-based (5K-25K) |
| Deduplication | Yes (L6 skips loaded) | No | Yes (envelope tracks loaded) |
| Timeout per layer | Yes (5-15ms) | No | Not needed (Python, not hook) |
| Conflict resolution | Priority hierarchy | None | Priority hierarchy |
| Context bracket | 4 levels (FRESH->CRITICAL) | None | 4 levels (FRESH->CRITICAL) |
| Output format | XML sections | Raw concatenation | Markdown sections |
| Performance | <100ms total | N/A (build-time) | N/A (build-time) |

### What NOT to port

1. **XML output format** -- CEX uses Markdown throughout
2. **Millisecond timeouts** -- aiox runs as a Claude hook (real-time); CEX assembles at build time
3. **Squad layer (L5)** -- CEX has no squad concept; brand fills this slot
4. **Star-command layer (L7)** -- CEX uses slash commands differently; builder ISOs fill this slot

## 5. Key Code References in aiox-core

| File (relative to aiox-core/) | What it contains |
|-------------------------------|-----------------|
| `core/synapse/engine.js` | Main orchestrator -- pipeline execution |
| `core/synapse/layers/layer-processor.js` | Abstract base class |
| `core/synapse/layers/l0-constitution.js` | L0 -- non-negotiable rules |
| `core/synapse/layers/l1-global.js` | L1 -- global + context |
| `core/synapse/layers/l2-agent.js` | L2 -- agent-scoped (12 agents) |
| `core/synapse/layers/l6-keyword.js` | L6 -- keyword recall + dedup |
| `core/synapse/layers/l7-star-command.js` | L7 -- mode switching |
| `core/synapse/context/context-tracker.js` | Bracket calculation |
| `core/synapse/output/formatter.js` | XML output assembly |
| `.claude/skills/synapse/references/layers.md` | Layer reference docs |

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_context_assembly]] | related | 0.23 |
| [[kc_model_context_protocol]] | sibling | 0.22 |
| [[p01_kc_handoff_protocol]] | sibling | 0.22 |
| [[extraction_gate_severity]] | sibling | 0.21 |
| [[p01_kc_token_budgeting]] | sibling | 0.19 |
| [[bld_schema_memory_architecture]] | related | 0.19 |
| [[port_plan_external_repos]] | related | 0.18 |
| [[bld_collaboration_context_doc]] | related | 0.18 |
| [[p01_kc_context_doc]] | sibling | 0.18 |
| [[bld_instruction_memory_architecture]] | related | 0.17 |
