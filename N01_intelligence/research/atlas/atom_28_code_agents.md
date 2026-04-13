---
id: atom_28_code_agents
kind: knowledge_card
pillar: P01
title: "Code Agent Vocabulary Atlas -- Complete Taxonomy of AI Coding Agent Concepts"
version: 1.0.0
created: 2026-04-13
author: N01
domain: code-agents
quality: 8.9
tags: [code-agent, edit-format, repo-map, sandbox, SWE-bench, Claude-Code, Codex, Aider, Cursor, Devin, Windsurf, OpenHands, subagent, lint-fix-loop, spec-to-code, claude-agent-sdk, pagerank, vm-isolation, decision-tree]
tldr: "Complete vocabulary of the code agent ecosystem (2024-2026): 9 major platforms, 9 edit format families with code examples, 4 sandbox models, 3 context strategies, 2 inter-agent protocols. Maps 140+ terms to CEX kinds and proposes 8 new kinds. Includes Agent SDK API, Aider PageRank internals, Cursor VM architecture, and agent selection decision tree."
---

# Code Agent Vocabulary Atlas

## 1. Platforms Surveyed

| Platform | Vendor | Type | Open Source | Key Innovation |
|----------|--------|------|-------------|----------------|
| Claude Code | Anthropic | CLI agent | No | Subagents, hooks, CLAUDE.md, SDK headless mode |
| Codex CLI | OpenAI | CLI agent | Yes (Rust) | Sandbox modes, AGENTS.md hierarchy, CSV batch spawn |
| Aider | Paul Gauthier | Terminal pair programmer | Yes | 6 edit formats, repo map (tree-sitter + PageRank), architect mode |
| Cursor | Anysphere | IDE agent | No | Background agents in VMs, Apply model, worktree isolation |
| Windsurf | Cognition (ex-Codeium) | IDE agent | No | Cascade flow awareness, implicit memory, multi-pane agents |
| Devin | Cognition | Autonomous agent | No | Full desktop environment, dynamic re-planning, PR merge rate |
| SWE-Agent | Princeton NLP | Research agent | Yes | Agent-Computer Interface (ACI), trajectory recording, YAML config |
| OpenHands | All Hands AI | Platform | Yes (MIT) | CodeAct unified action space, event-stream architecture, Docker sandbox |
| Augment Code | Augment | Context engine | Partial (MCP) | Semantic dependency graph, 400K+ file indexing, cross-repo |

---

## 2. Edit Formats (Complete Taxonomy)

The mechanism by which an LLM communicates file changes to the host system.

### 2.1 Format Families

| Format | Origin | Mechanism | Pros | Cons |
|--------|--------|-----------|------|------|
| **Whole file** | Aider | LLM returns entire file content | Simple, no matching errors | Slow, expensive for large files, encourages lazy elision |
| **Search/replace blocks** | Aider (`diff`) | `<<<<<<< SEARCH` / `=======` / `>>>>>>> REPLACE` markers | Precise, compact | Pattern matching can break with code evolution |
| **Unified diff (udiff)** | Aider | Modified `diff -U0` format with `@@` hunks | Standard tooling compatibility, reduces lazy coding | High technical complexity for LLMs |
| **Diff-fenced** | Aider (Gemini) | Search/replace with filepath inside fence | Gemini-compatible | Gemini-specific workaround |
| **Editor-diff / editor-whole** | Aider | Streamlined variants for architect mode | Separates planning from editing | Two-model overhead |
| **OpenAI patch** | Codex | `*** Begin Patch` / `*** End Patch` with `@@` context | No line-number dependency | Codex-specific format |
| **Tool-based edits** | Claude Code, OpenHands | Function calls (Read, Edit, Write tools) | Structured, validated, atomic | Requires tool infrastructure |
| **Sketch + Apply model** | Cursor | Primary LLM sketches change; dedicated 7B model applies | Fast (10.5K tok/s), 98% accuracy | Two-model pipeline |
| **Semantic edit** | Morph | AST-aware transformations, not text-based | 98% accuracy, scope-aware | Proprietary, limited availability |

### 2.2 Edit Application Strategies

| Strategy | Used By | Description |
|----------|---------|-------------|
| **Exact match** | Aider, Codex | Search string must match file content exactly |
| **Fuzzy match (Levenshtein)** | RooCode, Aider fallback | Tolerate small differences in search block |
| **Layered matching** | RooCode | Exact -> whitespace-insensitive -> fuzzy cascade |
| **Indentation-relative replacement** | RooCode | Preserve surrounding indent context |
| **Middle-out fuzzy** | RooCode | Match from center of block outward |
| **Fast Apply model** | Cursor, Morph | Dedicated small model (7B) trained for code merge at 10.5K tok/s |
| **Speculative decoding** | Morph Fast Apply | CUDA-kernel-level optimization for apply speed |

### 2.3 Concrete Format Examples (All 9 Families)

**1. Whole file** — LLM returns the complete file after changes:
```
show_greeting.py
` ` `python
import sys
def greeting(name):
    print("Hey", name)
if __name__ == '__main__':
    greeting(sys.argv[1])
` ` `
```

**2. Search/replace (Aider `diff`)** — most common Aider format:
```
mathweb/flask/app.py
` ` `python
<<<<<<< SEARCH
from flask import Flask
=======
import math
from flask import Flask
>>>>>>> REPLACE
` ` `
```

**3. Unified diff (`udiff`)** — standard `-U0` variant:
```diff
--- mathweb/flask/app.py
+++ mathweb/flask/app.py
@@ ... @@
-class MathWeb:
+import sympy
+
+class MathWeb:
```

**4. Diff-fenced** — search/replace with filepath inside fence (Gemini variant):
```python
# filepath: mathweb/flask/app.py
<<<<<<< SEARCH
from flask import Flask
=======
import math
from flask import Flask
>>>>>>> REPLACE
```

**5. Editor-diff / editor-whole** — Same syntax as formats 2/1 but produced by a second, smaller model in Aider architect mode. Architect outputs plan; editor model produces final diffs.

**6. OpenAI patch (Codex):**
```
*** Begin Patch
*** Update File: src/utils.py
@@ def add(a, b):
-    return a + b
+    return int(a) + int(b)
*** End Patch
```
No line-number dependency; context lines anchor the hunk.

**7. Tool-based edits (Claude Code, OpenHands):**
```json
{"tool": "Edit", "file_path": "src/utils.py",
 "old_string": "return a + b",
 "new_string": "return int(a) + int(b)"}
```
Structured function call. Atomic. No diff syntax needed.

**8. Sketch + Apply model (Cursor):**
- Primary LLM outputs a "sketch" (loose prose description of the change)
- Dedicated 7B apply model reads sketch + original file, produces merged output at 10.5K tok/s

**9. Semantic edit (Morph):**
- LLM specifies the change at the AST level (e.g., rename parameter in function scope)
- Apply model transforms the AST -- scope-aware, 98% accuracy, robust to code evolution

---

### 2.4 Architect Mode (Two-Phase Editing)

Aider pioneered this pattern; Cursor and others adopted it.

```
Phase 1: ARCHITECT (large model)     Phase 2: EDITOR (same or smaller model)
  - Reads full context                 - Receives architect's plan
  - Reasons about approach             - Produces actual file edits
  - Outputs high-level plan            - Uses editor-diff or editor-whole format
  - Does NOT touch files               - Applies changes atomically
```

**CEX parallel**: N07 (orchestrator/architect) dispatches to N03/N05 (editor/builder).

---

## 3. Codebase Context Strategies

How agents understand the repository beyond the current file.

### 3.1 Repo Map (Aider)

| Component | Technology | Purpose |
|-----------|-----------|---------|
| AST parsing | Tree-sitter | Extract function/class definitions and references |
| Dependency graph | Custom graph builder | Map call relationships between symbols |
| Ranking | PageRank | Prioritize most-connected symbols |
| Output | Condensed text map | Fits in context window, provides symbol-level visibility |

The repo map provides **symbol-level visibility** without loading full file content. Aider automatically selects relevant context based on the current chat.

#### 3.1a PageRank Algorithm — Implementation Detail

The repo map is the core reason Aider achieves higher edit accuracy than agents using naive file inclusion. The algorithm runs in 5 stages:

**Stage 1 — Tag extraction via tree-sitter**
Each supported language has a `tags.scm` query file defining what counts as a *definition* (function/class declared) vs. a *reference* (called/imported). Tree-sitter parses all files into ASTs; the query files extract tagged symbols with line numbers. 130+ languages supported.

**Stage 2 — Multigraph construction**
A directed multigraph is built:
- Node = file or symbol
- Edge = reference from one symbol to another
- Self-loop edges (weight=0.1) added for definitions with zero references (prevents isolated nodes from being ignored by PageRank)

**Stage 3 — Personalized PageRank via NetworkX**
```python
# Simplified from aider/repomap.py
import networkx as nx

G = build_reference_graph(tags)           # multigraph
personalization = {f: 1.0 for f in chat_files}  # files in current chat
ranked = nx.pagerank(G, personalization=personalization, weight="weight")
# Result: dict {symbol -> float score}, higher = more central
```
Files currently in the chat window receive boosted personalization scores, causing their callers/callees to rank higher — context expands outward from current work.

**Stage 4 — Token budget allocation via binary search**
The ranked symbol list is too large for the context window. Aider uses binary search over the inclusion threshold to find the largest subset that fits the token budget (configurable via `--map-tokens`, default 1024).

**Stage 5 — Compact text output**
Selected symbols are rendered as a tree outline (file path + function signatures only, no bodies). This gives the LLM structural awareness of 10K+ symbol codebases in ~1K tokens.

| Metric | Value |
|--------|-------|
| Languages supported | 130+ |
| Default map token budget | 1,024 tokens |
| Graph algorithm | NetworkX `pagerank()` with personalization |
| Self-loop weight (isolated nodes) | 0.1 |
| Benchmark improvement vs no map | Significantly higher edit accuracy |

Source: [Building a better repository map with tree-sitter](https://aider.chat/2023/10/22/repomap.html)

### 3.2 Codebase Indexing (Cursor, Augment)

| Approach | Vendor | Scale | Method |
|----------|--------|-------|--------|
| Hybrid semantic-lexical | Cursor | Full project | Embedding + keyword index at project open |
| Semantic dependency graph | Augment Code | 400K+ files | Call graphs, dependency chains, cross-repo |
| Three-tier retrieval | Cline | Per-query | ripgrep (lexical) + fzf (fuzzy) + tree-sitter (AST) |
| Knowledge graph | Codebase-Memory MCP | 66 languages | Tree-sitter -> SQLite graph, 14 MCP query tools |
| Code review graph | code-review-graph | Per-repo | Persistent map, 6.8x fewer tokens on reviews |

### 3.3 Context Window Management

| Technique | Description | Used By |
|-----------|-------------|---------|
| **Context pruning** | Drop older/irrelevant messages from conversation | All agents |
| **Subagent delegation** | Offload research to separate context window | Claude Code, Codex |
| **Repo map injection** | Add condensed codebase overview to system prompt | Aider |
| **Semantic retrieval** | Query embeddings for relevant code chunks | Cursor, Augment |
| **File watching** | Re-index only changed files (content-hash based) | Augment, Codebase-Memory |

---

## 4. Task Files (Configuration-as-Context)

Files that persist instructions across sessions, read by agents at startup.

| File | Agent | Location | Hierarchy |
|------|-------|----------|-----------|
| **CLAUDE.md** | Claude Code | Root, `.claude/`, `~/.claude/` | Project > directory > user-level |
| **AGENTS.md** | Codex CLI | Root + subdirectories | Global -> project root -> cwd (walk down) |
| **AGENTS.override.md** | Codex CLI | Same locations | Overrides AGENTS.md at same level |
| **.cursorrules** | Cursor | Project root | Single file (legacy) |
| **.cursor/rules/*.mdc** | Cursor | Project `.cursor/` dir | Multiple rule files, versioned |
| **Rules & Memory** | Windsurf | Settings | Cascade learns conventions over ~48h |
| **.windsurfrules** | Windsurf | Project root | Project-level instructions |
| **config.yaml** | SWE-Agent | Repo root | Single YAML governs entire agent behavior |

### Key Design Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| **Hierarchical override** | More specific files override general ones | Codex: global AGENTS.md < project AGENTS.md < subdir AGENTS.md |
| **Separation of concerns** | Different file for different rule types | Cursor: project rules, user rules, team rules, agent rules |
| **Implicit learning** | Agent builds memory from usage patterns | Windsurf: ~48h to learn architecture patterns |
| **Compound memory** | Multiple channels persist knowledge | AGENTS.md + git history + progress logs + task JSON |

---

## 5. Sandbox and Isolation Models

How agents execute code safely.

| Model | Agent | Isolation | Network | Persistence |
|-------|-------|-----------|---------|-------------|
| **Local sandbox (macOS Seatbelt/Linux Landlock)** | Codex CLI | OS-level policy per command | Configurable (deny/allow) | Working directory only |
| **Docker container** | OpenHands, SWE-Agent | Container per session | Configurable | Ephemeral by default |
| **Cloud VM** | Cursor Background Agents, Devin | Ubuntu VM per agent | Full internet | Branch + PR output |
| **Git worktree** | Cursor, Claude Code | Filesystem isolation via git | Local | Separate branch |
| **Approval gates** | Claude Code, Codex | Human-in-the-loop before dangerous ops | N/A | N/A |

### Codex Sandbox Modes

| Mode | Reads | Writes | Commands | Network |
|------|-------|--------|----------|---------|
| **Read-only** | Yes | Approval needed | Approval needed | No |
| **Auto** (default) | Yes | Yes (in workdir) | Yes (in workdir) | No |
| **Full access** | Yes | Yes (anywhere) | Yes (anywhere) | Yes |
| **YOLO** | Yes | Yes | Yes (no approval) | Yes |

### Cursor Background Agent Architecture

```
User starts task in Cursor
  |
  v
Cloud VM provisioned (Ubuntu on AWS)
  |-- Repo cloned from GitHub
  |-- Dockerfile applied (custom base image, optional)
  |-- setup.sh executed (deps installed, services started)
  |-- Agent works on feature branch
  |-- Tests executed in VM
  |-- Video recording of session (since Feb 2026)
  |-- Browser / Computer Use access (since Feb 2026)
  |
  v
PR created on GitHub
  |-- User reviews in Cursor or GitHub
  |-- Up to 8 parallel agents
```

#### VM Isolation Specification

| Property | Value |
|----------|-------|
| Infrastructure | AWS (Ubuntu-based VMs) |
| Network | Full internet access (configurable) |
| Storage | Ephemeral VM disk; output via PR |
| Configuration file | `.cursor/environment.json` (committable) |
| Custom base image | Dockerfile supported |
| Post-checkout setup | `setup.sh` script |
| Docker-in-Docker | Supported via `sudo service docker start` in setup.sh |
| Parallel agents | Up to 8 per project |
| Computer Use | Browser + video recording (Feb 2026 update) |
| Secrets injection | Via Cursor settings, NOT in Dockerfile |

**`.cursor/environment.json` example:**
```json
{
  "build": {
    "dockerfile": ".cursor/Dockerfile"
  },
  "startScript": ".cursor/setup.sh"
}
```

**Key isolation properties vs alternatives:**
- More persistent than Codex sandbox (VM survives across steps; Codex resets per command)
- More capable than Claude Code worktree (full OS, not just filesystem branch)
- Less controllable than OpenHands Docker (no direct container config beyond Dockerfile)

Source: [Cursor Background Agents docs](https://docs.cursor.com/en/background-agent)

---

## 6. Multi-File Edit Coordination

Patterns for agents editing multiple files in a single task.

| Pattern | Description | Used By |
|---------|-------------|---------|
| **Atomic multi-file commit** | All file changes committed together | Claude Code (git add + commit) |
| **Fan-out edit** | Single intent produces edits across N files | Aider (auto-adds related files via repo map) |
| **Worktree isolation** | Each agent works in separate git worktree | Cursor 3 (`/worktree` command) |
| **Proposal pattern** | Write `.proposal` files, merge post-wave | CEX (shared-file-proposal rule) |
| **Sequential file processing** | Edit files one-by-one with tool calls | Claude Code, Codex (tool-based edits) |
| **Sketch-then-apply** | Plan all changes first, apply in batch | Cursor (architect + apply model) |
| **Dependency-aware ordering** | Edit in topological order of imports | Augment Code (dependency graph) |

---

## 7. Agent Loop Patterns

The core execution cycle of code agents.

### 7.1 Standard Agent Loop (ReAct)

```
OBSERVE  ->  THINK  ->  ACT  ->  OBSERVE  ->  ...
(read file)  (plan)  (edit/run)  (check result)
```

### 7.2 Named Loop Variants

| Pattern | Description | Source |
|---------|-------------|-------|
| **Lint-fix loop** | Run linter -> collect errors -> fix -> re-run until clean | Common in all agents |
| **Test-repair cycle** | Run tests -> parse failures -> fix code -> re-test -> commit | RepairAgent, SWE-Agent |
| **Spec-to-code** | Read specification -> generate code -> validate against spec | Intent (Augment), Devin |
| **Bugloop** | Detect bug -> localize fault -> generate patch -> verify fix | CEX bugloop kind, RepairAgent |
| **Self-evaluation loop** | Generate -> score own output -> revise if below threshold | Claude Code (8F F7 GOVERN) |
| **Backtracking loop** | Generate -> detect syntax error -> revert -> retry with context | ROCODE |
| **Ralph Wiggum technique** | Pick task -> implement -> validate -> commit -> reset context -> next task | Addy Osmani blog |
| **Continuous coding loop** | Task selection -> implementation -> validation -> commit -> progress log -> repeat | Self-improving agents pattern |

### 7.3 Multi-Agent Orchestration Patterns

| Pattern | Description | Used By |
|---------|-------------|---------|
| **Planner-Worker** | Planner agent strategizes; worker agents implement | Devin, CEX (N07 + N01-N06) |
| **Best-of-N** | N agents generate competing solutions; pick best | Cursor 3 |
| **Wave dispatch** | Groups of agents run in dependency-ordered waves | CEX (mission_runner) |
| **Parallel worktree** | Each agent in isolated git worktree, merged after | Cursor, Intent |
| **Hierarchical delegation** | Parent spawns child agents for subtasks | Claude Code subagents, Codex subagents |
| **Compound loops** | Analysis -> Planning -> Execution chained across agents | Multi-agent pattern |

---

## 8. Background / Headless / Autonomous Agents

| Capability | Claude Code | Codex CLI | Cursor | Devin |
|-----------|-------------|-----------|--------|-------|
| **Headless mode** | `-p` flag (stdout, exit) | `exec` subcommand | Background agents | Always headless |
| **SDK integration** | Claude Agent SDK | Agents SDK | API (limited) | Slack/web interface |
| **Parallel agents** | Subagents (5 per nucleus) | `max_threads: 6` | 8 worktree agents | 1 per session |
| **Session persistence** | Context window | Transcript + plan history | VM state + branch | Full environment |
| **Output mechanism** | Files + git commits | Files + git commits | PR on GitHub | PR on GitHub |
| **Monitoring** | Hooks (PreToolUse, PostToolUse, Stop) | Approval queue | Agent dashboard | Session playback |

---

## 9. Code Review Agent Patterns

| Pattern | Description | Tools |
|---------|-------------|-------|
| **Diff review** | Analyze uncommitted changes or branch diff | Codex (`--review`), Claude Code |
| **PR review** | Comment on pull request changes | GitHub Copilot, Claude Code (gh CLI) |
| **Inline annotation** | Add comments at specific lines | Cursor, Copilot |
| **Security scan** | Check for vulnerabilities in changes | Augment, SonarQube integration |
| **Style enforcement** | Verify code matches project conventions | .cursorrules, CLAUDE.md rules |
| **Graph-aware review** | Use dependency graph to assess impact | Augment Context Engine, code-review-graph |

---

## 10. Inter-Agent Protocols

| Protocol | Scope | Purpose | Status (2026) |
|----------|-------|---------|---------------|
| **MCP (Model Context Protocol)** | Agent <-> Tools | Standardize tool access for LLMs | Anthropic standard, widely adopted |
| **A2A (Agent2Agent Protocol)** | Agent <-> Agent | Inter-agent communication and task delegation | Google/Linux Foundation, v0.3, 150+ orgs |
| **Agent Cards (A2A)** | Discovery | JSON-LD metadata describing agent capabilities | Part of A2A spec |
| **Signals (CEX)** | Nucleus <-> Nucleus | Completion/status notification via JSON files | CEX internal |
| **Handoffs (CEX)** | N07 <-> N0x | Task delegation with full context | CEX internal |

---

## 11. Benchmarks and Evaluation

| Benchmark | Focus | Scale | Key Metric |
|-----------|-------|-------|------------|
| **SWE-bench** | GitHub issue resolution | 2,294 issue-PR pairs, 12 Python repos | % issues resolved |
| **SWE-bench Verified** | Curated subset | ~500 verified instances | % resolved (top: ~75%) |
| **SWE-bench++** | Multi-language | 11 languages, 3,971 repos, 11,133 instances | Cross-language resolution |
| **SWE-EVO** | Long-horizon evolution | Multi-commit sequences | Sustained quality over time |
| **DPAI Arena** | Developer productivity | JetBrains, multi-language | Comparative agent ranking |
| **Aider edit leaderboard** | Edit accuracy per model | All major LLMs | % correct edits, cost per edit |

---

## 12. Complete Glossary (140+ terms)

### A

| Term | Definition | Domain |
|------|-----------|--------|
| **ACI (Agent-Computer Interface)** | The set of tools/commands available to an agent for interacting with code | SWE-Agent |
| **Action space** | Range of operations an agent can perform (edit, run, navigate, git) | SWE-Agent, RL |
| **AGENTS.md** | Instruction file for Codex CLI, hierarchical override support | Codex |
| **AGENTS.override.md** | Higher-priority override for AGENTS.md at same directory level | Codex |
| **Agent card** | JSON-LD metadata describing agent capabilities (A2A protocol) | A2A, CEX |
| **Agent teams** | Multiple agents coordinating across separate sessions | Claude Code |
| **Apply model** | Dedicated small model (7B) that merges LLM edits into files | Cursor, Morph |
| **Approval gate** | Human-in-the-loop checkpoint before dangerous operations | Codex, Claude Code |
| **Architect mode** | Two-phase: large model plans, smaller model edits | Aider |

### B

| Term | Definition | Domain |
|------|-----------|--------|
| **Background agent** | Agent running asynchronously in cloud VM or separate process | Cursor, Devin |
| **Backtracking** | Reverting failed edit and retrying with error context | ROCODE |
| **Best-of-N** | Generate N competing solutions, select best | Cursor 3 |
| **Bugloop** | Automated detect -> fix -> verify cycle for defects | CEX kind |

### C

| Term | Definition | Domain |
|------|-----------|--------|
| **Cascade** | Windsurf's AI agent engine with flow awareness | Windsurf |
| **CLAUDE.md** | Persistent instruction file for Claude Code sessions | Claude Code |
| **CodeAct** | Unified code action space -- all agent actions expressed as code | OpenHands |
| **Compound learning** | 4 memory channels: git + logs + task JSON + knowledge base | Self-improving agents |
| **Context pruning** | Removing older/irrelevant messages to fit context window | All agents |
| **Context window** | Maximum token capacity of the model during a session | All LLMs |
| **Continuous coding loop** | Select task -> implement -> validate -> commit -> log -> repeat | Pattern |
| **.cursorrules** | Project-level instruction file for Cursor (legacy) | Cursor |

### D

| Term | Definition | Domain |
|------|-----------|--------|
| **Diff-fenced** | Aider edit format with filepath inside code fence (for Gemini) | Aider |
| **Diff review** | Analyzing code changes (staged, unstaged, or branch diff) | Codex, all |
| **Draft editor** | LLM-based line-range targeting edit mode | OpenHands |
| **Dynamic re-planning** | Changing execution strategy mid-task when blocked | Devin v3 |

### E

| Term | Definition | Domain |
|------|-----------|--------|
| **Edit format** | The protocol by which an LLM communicates file changes | Aider, all |
| **Editor-diff** | Streamlined diff variant for architect mode | Aider |
| **Event-stream architecture** | Modeling agent-environment interaction as event sequence | OpenHands |

### F

| Term | Definition | Domain |
|------|-----------|--------|
| **Fan-out edit** | Single intent producing edits across multiple files | Aider, Cursor |
| **Fast Apply** | 7B model merging edits at 10.5K tok/s with 98% accuracy | Morph |
| **Flow awareness** | Tracking user actions (edits, commands, clipboard) to infer intent | Windsurf |
| **Full access mode** | Sandbox mode with unrestricted file/network permissions | Codex |
| **Function calling** | Structured tool invocation (vs free-form text output) | Claude Code, OpenHands |
| **Fuzzy matching** | Tolerating small differences when locating edit targets | RooCode, Aider |

### G

| Term | Definition | Domain |
|------|-----------|--------|
| **Git worktree** | Isolated working directory on separate branch for parallel work | Cursor 3, git |

### H

| Term | Definition | Domain |
|------|-----------|--------|
| **Handoff** | Task delegation document with full context (CEX: N07 -> N0x) | CEX, multi-agent |
| **Headless mode** | Agent running without UI, output via stdout or files | Claude Code (`-p`), Codex (`exec`) |
| **Hooks** | Event callbacks (PreToolUse, PostToolUse, Stop) for agent control | Claude Code, Codex |
| **Human-in-the-loop** | Requiring user approval at defined checkpoints | All agents |

### I-K

| Term | Definition | Domain |
|------|-----------|--------|
| **Implicit memory** | Agent learning conventions from usage without explicit instruction | Windsurf (~48h) |
| **Intent resolution** | Mapping vague user input to structured action (kind, pillar, tool) | CEX, NLU |

### L

| Term | Definition | Domain |
|------|-----------|--------|
| **Layered matching** | Exact -> whitespace-insensitive -> fuzzy cascade for edit application | RooCode |
| **Lint-fix loop** | Run linter -> parse errors -> fix -> re-lint until clean | All agents |

### M

| Term | Definition | Domain |
|------|-----------|--------|
| **MCP (Model Context Protocol)** | Standard for LLM-tool interop (Anthropic) | Anthropic, ecosystem |
| **Middle-out fuzzy** | Matching from center of code block outward | RooCode |
| **Multi-file coordination** | Editing multiple files atomically in single task | All agents |

### N-O

| Term | Definition | Domain |
|------|-----------|--------|
| **Non-interactive execution** | Running agent without user confirmation prompts | Codex (`exec`), Claude Code (`-p`) |
| **Observation space** | Information returned from tool execution (file content, errors, state) | SWE-Agent, RL |
| **OpenAI patch format** | `*** Begin Patch` / `*** End Patch` edit syntax | Codex |

### P

| Term | Definition | Domain |
|------|-----------|--------|
| **PageRank (repo map)** | Ranking symbols by graph connectivity for context selection | Aider |
| **Plan approval** | User reviews agent's plan before execution begins | Codex, Cursor |
| **Planner-Worker model** | Hierarchical: planner strategizes, workers implement | Devin, CEX |
| **Proposal pattern** | Writing change proposals for post-wave merge (concurrent safety) | CEX |

### R

| Term | Definition | Domain |
|------|-----------|--------|
| **ReAct loop** | Observe -> Think -> Act -> Observe cycle | Standard agent pattern |
| **Repo map** | Condensed representation of codebase structure for context | Aider (tree-sitter + PageRank) |

### S

| Term | Definition | Domain |
|------|-----------|--------|
| **Sandbox** | Isolated execution environment for agent-generated code | All agents |
| **Search/replace block** | Edit format using `SEARCH`/`REPLACE` markers | Aider `diff` format |
| **Semantic dependency graph** | AST-level mapping of code relationships across files | Augment Code |
| **Semantic edit** | Code transformation based on AST understanding, not text | Morph |
| **Session resumption** | Restoring agent state from prior conversation | Codex, Claude Code |
| **Sketch + Apply** | Two-phase: LLM sketches change, small model applies it | Cursor |
| **Spec-to-code** | Generating implementation from specification document | Intent, Devin |
| **Speculative decoding** | CUDA-level optimization predicting likely next tokens | Morph Fast Apply |
| **Subagent** | Specialized child agent with own context window and tools | Claude Code, Codex |
| **SWE-bench** | Benchmark: resolve real GitHub issues in Python repos | Princeton NLP |

### T

| Term | Definition | Domain |
|------|-----------|--------|
| **Task file** | Persistent instruction file read at agent startup | CLAUDE.md, AGENTS.md, .cursorrules |
| **Test-repair cycle** | Run tests -> parse failures -> fix -> re-test until green | RepairAgent, all |
| **Tool-based edit** | File changes via structured function calls (Read, Edit, Write) | Claude Code |
| **Trajectory** | Complete record of agent actions for a task (states + actions + observations) | SWE-Agent |
| **Tree-sitter** | Incremental parser generator for AST extraction (66+ languages) | Aider, Cline, Codebase-Memory |

### U-W

| Term | Definition | Domain |
|------|-----------|--------|
| **Unified diff (udiff)** | Standard patch format adapted for LLM edits | Aider |
| **Wave dispatch** | Dependency-ordered groups of parallel agent executions | CEX |
| **Whole file format** | LLM returns complete file content as edit mechanism | Aider |
| **Worktree isolation** | Each parallel agent in separate git worktree | Cursor 3 |
| **Writable roots** | Multiple project directories an agent can modify | Codex (`--add-dir`) |

### Y

| Term | Definition | Domain |
|------|-----------|--------|
| **YOLO mode** | No approval, no sandbox, full access | Codex CLI |

---

## 13. CEX Kind Mapping

### Existing CEX kinds that map directly

| Industry Term | CEX Kind | Pillar | Notes |
|---------------|----------|--------|-------|
| Sandbox / code executor | `code_executor` | P04 | Docker, E2B, Jupyter runtime |
| Lint-fix loop / test-repair cycle | `bugloop` | P11 | Detect -> fix -> verify |
| CLI agent tool | `cli_tool` | P04 | Aider, Codex CLI as tools |
| Agent definition | `agent` | P02 | Persona + capabilities |
| Agent deployment spec | `agent_card` | P08 | A2A-compatible capability card |
| Background process | `daemon` | P04 | Background agent process |
| MCP tool server | `mcp_server` | P04 | Tool provider for agents |
| Browser automation | `browser_tool` | P04 | Devin desktop use, browser agents |
| Desktop automation | `computer_use` | P04 | Devin 2.2 desktop capability |
| Quality validation | `quality_gate` | P11 | F7 GOVERN pattern |
| Task scheduling | `schedule` | P12 | Wave dispatch timing |
| Workflow definition | `workflow` | P12 | Agent loop orchestration |
| Process optimizer | `optimizer` | P11 | Self-improving agent patterns |
| System prompt | `system_prompt` | P03 | CLAUDE.md, AGENTS.md content |
| Scoring criteria | `scoring_rubric` | P07 | SWE-bench evaluation |
| Benchmark | `benchmark` | P07 | SWE-bench, DPAI Arena |

### Proposed new CEX kinds (8)

| Proposed Kind | Pillar | Description | Boundary | Industry Source |
|---------------|--------|-------------|----------|----------------|
| `edit_format` | P06 | Schema defining how LLM communicates file changes (search/replace, udiff, whole, patch) | NOT a formatter (P05, output rendering) nor a parser (P05, input parsing). Defines the wire protocol between LLM and file system. | Aider 6 formats, Codex patch, Cursor sketch |
| `repo_map` | P10 | Condensed codebase representation for context injection (tree-sitter AST + PageRank ranking) | NOT an embedding_config (vector index) nor a knowledge_index (text search). Graph-based symbol map. | Aider repo map, Augment dependency graph |
| `sandbox_config` | P09 | Execution environment isolation policy (permissions, network, filesystem scope) | NOT an env_config (runtime vars) nor a rate_limit_config (throttling). Defines security boundary. | Codex sandbox modes, Docker, VM isolation |
| `task_file` | P03 | Persistent instruction file read by agents at session start (CLAUDE.md, AGENTS.md, .cursorrules) | NOT a system_prompt (injected per-call) nor a context_doc (reference material). File-based agent configuration. | Claude Code, Codex, Cursor, Windsurf |
| `apply_model` | P02 | Specialized small model trained to merge LLM edits into source files accurately and fast | NOT a model_provider (API config) nor a fallback_chain (routing). Purpose-trained edit applicator. | Morph Fast Apply 7B, Cursor apply model |
| `trajectory` | P07 | Complete recorded sequence of agent actions for replay, evaluation, or training | NOT a learning_record (post-hoc lesson) nor a trace_config (logging setup). Full state-action-observation sequence. | SWE-Agent trajectory, OpenHands events |
| `agent_protocol` | P06 | Inter-agent communication standard (A2A, MCP, signals) | NOT an interface (code contract) nor a webhook (HTTP callback). Protocol spec for agent interop. | Google A2A, Anthropic MCP |
| `worktree_config` | P09 | Git worktree isolation configuration for parallel agent execution | NOT a spawn_config (process launch) nor a path_config (directory layout). Branch isolation for concurrent agents. | Cursor 3 /worktree, git worktree |

---

## 14. Cross-Reference: CEX 8F Pipeline vs Industry Patterns

| CEX 8F Stage | Industry Pattern | Agents Using It |
|--------------|-----------------|-----------------|
| F1 CONSTRAIN | Intent resolution, query rewriting | All (implicit) |
| F2 BECOME | Agent persona loading, system prompt injection | Claude Code (subagent .md), Codex (AGENTS.md) |
| F3 INJECT | Repo map, semantic retrieval, RAG, codebase indexing | Aider, Cursor, Augment |
| F4 REASON | Plan generation, architect mode, ReAct reasoning | Aider architect, Cursor planning, Devin |
| F5 CALL | Tool use (MCP), function calling, shell execution | All agents |
| F6 PRODUCE | Code generation via edit format (diff, whole, tool-based) | All agents |
| F7 GOVERN | Lint-fix loop, test-repair cycle, self-evaluation | All agents (implicit or explicit) |
| F8 COLLABORATE | Git commit, PR creation, signal completion | All agents |

---

## 15. Maturity Landscape (April 2026)

| Capability | Mature | Emerging | Early |
|-----------|--------|----------|-------|
| Single-file edits | All agents | - | - |
| Multi-file coordination | Claude Code, Cursor, Aider | Codex, OpenHands | - |
| Background/headless | Cursor, Devin, Claude Code SDK | Codex exec | OpenHands |
| Parallel agents | Cursor (8), Claude Code (subagents) | Codex (6 threads) | SWE-Agent |
| Codebase understanding | Augment (400K files) | Cursor index, Aider repo map | SWE-Agent |
| Inter-agent protocol | MCP (tools) | A2A v0.3 (agents) | CEX signals |
| Self-improving loops | Pattern documented | Claude Code 8F, Aider architect | RepairAgent |
| Semantic edits | Morph (98%) | Cursor apply model | Research |

---

## Sources

- [Aider edit formats](https://aider.chat/docs/more/edit-formats.html)
- [Codex CLI features](https://developers.openai.com/codex/cli/features)
- [Codex AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md)
- [Codex subagents](https://developers.openai.com/codex/subagents)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code CLAUDE.md guide](https://claude.com/blog/using-claude-md-files)
- [SWE-Agent GitHub](https://github.com/SWE-agent/SWE-agent)
- [Cursor background agents](https://docs.cursor.com/en/background-agent)
- [Cursor 3 worktrees](https://cursor.com/docs/configuration/worktrees)
- [Windsurf Cascade](https://windsurf.com/cascade)
- [Devin AI](https://cognition.ai/blog/introducing-devin)
- [Devin 2025 review](https://cognition.ai/blog/devin-annual-performance-review-2025)
- [OpenHands CodeAct 2.1](https://openhands.dev/blog/openhands-codeact-21-an-open-state-of-the-art-software-development-agent)
- [Augment Code Context Engine](https://www.augmentcode.com/context-engine)
- [A2A Protocol](https://a2a-protocol.org/latest/)
- [Morph Fast Apply](https://www.morphllm.com/fast-apply-model)
- [Morph edit formats guide](https://www.morphllm.com/edit-formats)
- [Code surgery: how AI assistants make edits](https://fabianhertwig.com/blog/coding-assistants-file-edits/)
- [Self-improving coding agents](https://addyosmani.com/blog/self-improving-agents/)
- [SWE-EVO benchmark](https://arxiv.org/html/2512.18470v2)
- [Codebase-Memory MCP](https://github.com/DeusData/codebase-memory-mcp)
