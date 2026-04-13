---
id: atom_23_multiagent_protocols
kind: knowledge_card
title: "Multi-Agent Communication Protocols: Architecture, Paradigms & Interoperability"
version: "1.0.0"
quality: 8.8
tags: [multi-agent, protocols, MCP, ACP, A2A, ANP, communication, architecture, interoperability, ProtocolBench]
pillar: P01
domain: multi-agent-communication
density_score: 0.93
sources:
  - "arxiv:2502.14321 -- Beyond Self-Talk: Communication-Centric Survey of LLM-MAS"
  - "arxiv:2504.16736 -- Survey of AI Agent Protocols"
  - "arxiv:2505.02279 -- Agent Interoperability Protocols: MCP, ACP, A2A, ANP"
  - "ProtocolBench (ICLR 2026 submission) -- Which LLM Multi-Agent Protocol to Choose?"
---

# Multi-Agent Communication Protocols: Architecture, Paradigms & Interoperability

Deep research atom synthesizing three surveys and one benchmark on how LLM-based agents communicate, coordinate, and interoperate. Covers 16 protocols, 5 architecture types, 3 communication paradigms, 4 evaluation axes, and maps all vocabulary to CEX kinds.

---

## 1. Architecture Types (5 canonical forms)

How agents are structurally organized determines information flow, bottleneck locations, and scalability ceiling.

| Architecture | Definition | Characteristics | Strengths | Weaknesses | Example System |
|---|---|---|---|---|---|
| **Flat / Peer-to-Peer** | Decentralized network of peer agents without hierarchy or central oversight | Agents communicate directly; no designated leader; any-to-any messaging | Agile, flexible, fast iteration; no single point of failure | Scalability degrades with agent count; coordination overhead grows O(n^2) | Fact-checking debate agents; opinion dynamics |
| **Hierarchical** | Agents organized in tiers -- strategic oversight above, execution below | Higher-level agents delegate and supervise; lower-level agents execute detailed tasks | Clear chain of command; effective for complex task decomposition | Bottleneck at supervisor; single point of failure at top tier | ChatDev (CEO > CTO > Programmer > Tester) |
| **Team / Group** | Agents segmented into specialized squads, each owning a domain | Intra-team collaboration is tight; inter-team communication is structured | Leverages specialization; parallel team execution | Inter-team communication overhead; coordination cost between squads | MAGIS (admin team, dev team, test team) |
| **Society** | Agents interact within a social environment governed by shared norms and emergent behavior | Relationships form dynamically; agents have memory, reputation, social roles | Supports large-scale simulation; emergent collective intelligence | Unpredictable; hard to control; debugging is difficult | Generative Agents (Smallville sandbox) |
| **Hybrid** | Combines 2+ of the above -- e.g., hierarchical oversight + flat execution within teams | Adapts structure to task requirements dynamically | Best of multiple models; flexible resource allocation | Complex design; coordination overhead between modes | FixAgent (strategic + decentralized execution) |

### CEX Mapping

| Architecture | CEX Kind(s) | CEX Pillar | Notes |
|---|---|---|---|
| Flat | `workflow` (peer chain) | P12 | CEX nuclei in solo dispatch approximate flat |
| Hierarchical | `supervisor` + `handoff` | P12/P02 | N07 > N01-N06 is hierarchical dispatch |
| Team | `dispatch_rule` + `workflow` | P12 | Grid dispatch with wave grouping |
| Society | `entity_memory` + `guardrail` | P10/P11 | Not yet modeled in CEX -- future kind candidate |
| Hybrid | `workflow` + `supervisor` | P12 | CEX default: N07 hierarchical + nuclei autonomous |

---

## 2. Communication Paradigms (3 canonical + strategies)

### 2.1 Core Paradigms

| Paradigm | Definition | Mechanism | Strengths | Weaknesses |
|---|---|---|---|---|
| **Message Passing (MP)** | Direct point-to-point or broadcast exchange of explicit messages | Agent A sends structured message to Agent B (or broadcasts); receiver processes and may reply | Simple, natural for LLMs; flexible content (NL, code, structured data) | Susceptible to overload; no shared state; message ordering challenges |
| **Speech Act (SA)** | Utterances as performative actions -- designed to trigger state changes | Agents issue directives, assertions, commitments, declarations per speech act theory (Austin/Searle) | Enables negotiation, persuasion, debate; rich intentional semantics | Risk of "illocutionary misfires" from ambiguous force-marking; requires standardized performative taxonomy |
| **Blackboard (BB)** | Centralized shared repository where agents read/write collaboratively | All agents access a common workspace; changes are visible to all; coordination via shared state | Unified view of system state; natural for collaborative construction | Single point of failure; potential bottleneck; requires conflict resolution for concurrent writes |

### 2.2 Communication Strategies (turn-taking patterns)

| Strategy | Abbrev | Definition | Latency | Risk |
|---|---|---|---|---|
| **One-by-One** | OO | Sequential turn-based: each agent responds after processing all prior messages | Linear in agent count | Cumulative error propagation |
| **Simultaneous-Talk** | ST | All agents communicate concurrently without waiting | Lowest latency | State staleness; conflict resolution needed |
| **Simultaneous-Talk-with-Summarizer** | SS | Concurrent + a summarizer agent that consolidates into coherent digests | Medium | Summarizer hallucination; reintroduces sequential dependency |

### 2.3 Communication Goals

| Goal | Definition | CEX Parallel |
|---|---|---|
| **Direct Cooperation** | Agents openly share info and resources to jointly complete tasks | Grid dispatch (nuclei share via git) |
| **Cooperation Through Debate** | Agents critique and refine each other's output via structured debate | Peer-review scoring (`cex_score.py`) |
| **Competition** | Agents pursue individual goals that may conflict | Not modeled in CEX (future: auction-based dispatch) |
| **Mixed-Motive** | Cooperation and competition coexist | Not modeled in CEX |

---

## 3. Communication Objects and Content

### 3.1 Communication Objects (who/what agents talk to)

| Object | Description | CEX Parallel |
|---|---|---|
| **Self** | Internal dialogue, reflection, planning | 8F reasoning trace (F1-F8 internal monologue) |
| **Other Agents** | Direct inter-agent exchange | Handoffs, signals, proposals |
| **Environment** | Sensing external state (files, APIs, sensors) | Tool calls (F5 CALL), git state |
| **Human** | User-facing interaction | GDP (Guided Decision Protocol) |

### 3.2 Communication Content

| Type | Subtype | Description | CEX Parallel |
|---|---|---|---|
| **Explicit** | Natural Language | Human-readable text exchange | Handoff `.md` files |
| **Explicit** | Code / Structured Data | JSON, YAML, code blocks | `kinds_meta.json`, signal JSON, compiled YAML |
| **Implicit** | Behavioral Feedback | Intent communicated through actions | Git commit patterns (nucleus signals completion via commit) |
| **Implicit** | Environmental Signal | Context changes influencing behavior | `.cex/runtime/signals/`, file system state |

---

## 4. Protocol Landscape (16 protocols surveyed)

### 4.1 Taxonomy (2 dimensions)

| | General-Purpose | Domain-Specific |
|---|---|---|
| **Context-Oriented** (agent <-> resource) | MCP (Anthropic) | agents.json (WildCardAI) |
| **Inter-Agent** (agent <-> agent) | A2A, ANP, ACP/AComP, AITP, AConP, Coral, Agora | PXP, LOKA, WAP (human-agent); CrowdES, SPPs (robot-agent); LMOS, Agent Protocol (system-agent) |

### 4.2 The Big Four -- Detailed Comparison

| Dimension | MCP | ACP | A2A | ANP |
|---|---|---|---|---|
| **Proposer** | Anthropic (2024) | IBM / AI and Data (2025) | Google (Apr 2025) | ANP Community (2024) |
| **Model** | Client-Server | Brokered Client-Server | Peer-like Client <-> Server | Decentralized P2P |
| **Wire format** | JSON-RPC 2.0 | Multipart MIME (REST) | Task + Artifact JSON (JSON-RPC 2.0) | JSON-LD + ADP |
| **Transport** | HTTP, Stdio, SSE | HTTP incremental streams | HTTP + optional SSE | HTTPS + JSON-LD |
| **Discovery** | Manual / static URL | Registry-based + manifest at well-known path | Agent Card at `/.well-known/agent.json` | Search engine indexing + `/.well-known/agent-descriptions` |
| **Identity / Auth** | OAuth 2.0, token-based | Bearer tokens, mTLS, JWS, DIDs | DID-based handshake, OAuth 2.0 | W3C DIDs (`did:wba`) |
| **Session** | Stateless + context window | Session-aware with run state tracking | Client-managed task IDs | Stateless; DID tokens |
| **Core abstraction** | Tools, Resources, Prompts, Sampling | Agent Detail, Message Parts, Artifacts | Agent Card, Task, Artifact, Message, Parts | DID Document, ADP, JSON-LD graph |
| **Lifecycle** | Init > Operation > Shutdown | Discovery > Connect > Execute > Close | Discover Card > Submit Task > Stream Updates > Complete | Discover > Authenticate > Negotiate > Execute |
| **Primary use case** | LLM <-> tool integration | Model-agnostic multimodal messaging | Enterprise task delegation and workflow | Open internet agent marketplace |
| **Strength** | Tight LLM integration; ecosystem momentum | Multimodal; offline discovery; session management | Negotiation; artifact-driven; enterprise-grade | Trustless identity; no central authority |
| **Limitation** | Centralized server; tool-focused not agent-focused | Registry dependency | Enterprise-focused; heavier setup | High negotiation overhead; nascent ecosystem |
| **Maturity stage** | Standard (production) | Drafting | Landing (early production) | Landing |

### 4.3 Extended Protocol Registry

| Protocol | Proposer | Type | Stage | Core Focus |
|---|---|---|---|---|
| MCP | Anthropic | Context-Oriented | Standard | Agent-resource connection |
| agents.json | WildCardAI | Context-Oriented | Drafting | Website info discovery |
| A2A | Google | Inter-Agent | Landing | Enterprise collaboration |
| ANP | ANP Community | Inter-Agent | Landing | Cross-domain P2P |
| AITP | NEAR | Inter-Agent | Drafting | Secure transactions (blockchain) |
| AConP | Cisco/LangChain | Inter-Agent | Drafting | Agent invocation standardization |
| AComP | IBM | Inter-Agent | Drafting | Multi-team collaboration |
| Coral | Coral Community | Inter-Agent | Drafting | Decentralized infrastructure |
| Agora | Oxford | Inter-Agent | Concept | NL protocol negotiation |
| LMOS | Eclipse | System-Agent | Landing | Internet of Agents |
| Agent Protocol | AI Engineer Fdn | System-Agent | Landing | Lifecycle management |
| LOKA | CMU | Human-Agent | Concept | Ethical consensus |
| PXP | BITS Pilani | Human-Agent | Concept | Mutual intelligibility |
| WAP | OTA Tech AI | Human-Agent | Concept | Web automation |
| CrowdES | GIST.KR | Robot-Agent | Concept | Crowd dynamics |
| SPPs | U. Liverpool | Robot-Agent | Concept | Robotic localization |

### 4.4 Security Model Comparison

| Threat | MCP | ACP | A2A | ANP |
|---|---|---|---|---|
| Identity spoofing | OAuth 2.0 | Bearer + mTLS | Signed Agent Cards | DID verification |
| Tool/manifest poisoning | Unsigned manifests (risk) | Manifest signing | JWS validation | DID signature validation |
| Credential theft | Local client stores | Short-lived tokens + rotation | Capability-scoped credentials | HTTPS-hosted DIDs |
| Session hijacking | N/A (stateless) | Session token expiry | Client-managed IDs | Stateless (no sessions) |
| Mitigation best practice | SBOMs, Sigstore, mTLS | TLS transport, JWS | Immutable versioned manifests | Automated crawling + freshness |

### 4.5 Phased Adoption Roadmap

```
Stage 1: MCP         -- Tool binding. LLM calls external tools via JSON-RPC.
                        Start here. Widest ecosystem. Production-ready.

Stage 2: ACP         -- Structured messaging. REST-native multimodal agent-to-agent.
                        Add when agents need session-aware, typed message exchange.

Stage 3: A2A         -- Enterprise workflow. Agent Cards + task delegation.
                        Add when agents need to discover and delegate to unknown peers.

Stage 4: ANP         -- Open marketplace. Trustless identity, decentralized discovery.
                        Add when agents span organizations without shared trust.
```

---

## 5. ProtocolBench Evaluation Framework

Source: ProtocolBench (ICLR 2026 submission, Hongyi Du et al.)

### 5.1 Four Evaluation Axes

| Axis | What it measures | Key finding |
|---|---|---|
| **Task Success** | End-to-end completion rate per protocol | Success varies significantly by scenario; no single protocol dominates |
| **End-to-End Latency** | Time from task submission to completion | Up to 3.48s mean latency difference across protocols in Streaming Queue |
| **Message/Byte Overhead** | Communication cost (bytes, message count) | Protocol overhead correlates with feature richness (ANP > A2A > ACP > MCP) |
| **Robustness Under Failures** | Recovery from node crashes, network partitions | Resilience differs consistently; no protocol is universally robust |

### 5.2 Scenarios

| Scenario | What it tests | Key result |
|---|---|---|
| **Streaming Queue** | Throughput under sustained load | Completion time varies up to 36.5% across protocols |
| **Fail-Storm Recovery** | Resilience when multiple agents crash simultaneously | Recovery time differs consistently across protocols |
| **GAIA** | Complex multi-step real-world tasks | Scenario-specific protocol advantages emerge |

### 5.3 ProtocolRouter

A learnable meta-component that selects the optimal protocol per-scenario or per-module based on requirement vectors and runtime signals.

- Reduces Fail-Storm recovery time by up to 18.1% vs. best single-protocol baseline
- Achieves scenario-specific gains (higher success in GAIA)
- Implication: no single protocol is optimal -- adaptive routing beats static choice

### 5.4 Extended Evaluation Dimensions (from arxiv:2504.16736)

Seven-dimension framework for comprehensive protocol assessment:

| Dimension | Metrics | Weight |
|---|---|---|
| **Efficiency** | Latency, Throughput (TPS-N), Resource utilization | High |
| **Scalability** | Node scalability, Link scalability, Capability Negotiation Score (CNS) | High |
| **Security** | Auth diversity, Role/ACL granularity, Context desensitization | Critical |
| **Reliability** | Packet retransmission, Flow/congestion control, Persistent connections | High |
| **Extensibility** | Backward compatibility, Flexibility, Customization | Medium |
| **Operability** | Code volume, Deployment complexity, Observability | Medium |
| **Interoperability** | Cross-platform compatibility, Network adaptability | High |

Novel metric -- **Capability Negotiation Score (CNS)**: successful negotiations / total attempts, normalized by average negotiation time.

---

## 6. ANP Layered Architecture (reference model)

The cleanest layered model, applicable as a general reference:

```
Layer 3: Application Protocol
  - Domain-specific task protocols
  - Structured (JSON-RPC, OpenAPI) or Natural Language interfaces

Layer 2: Meta-Protocol
  - Protocol negotiation using natural language
  - Dynamic capability discovery
  - Agora's "Protocol Documents" concept

Layer 1: Identity / Encryption
  - W3C DID standards for decentralized authentication
  - End-to-end encryption
  - Trust establishment
```

---

## 7. Key Terminology Registry

Complete vocabulary extracted from all four sources, with CEX kind mapping.

| Term | Definition | Source(s) | CEX Kind | CEX Pillar |
|---|---|---|---|---|
| Agent Card | JSON manifest advertising agent capabilities, skills, auth requirements | A2A, ACP | `agent_card` | P08 |
| Agent Description Protocol (ADP) | JSON-LD format for semantic agent description | ANP | `agent_card` (extended) | P08 |
| Artifact (protocol) | Tangible output from agent task execution | A2A, ACP | `knowledge_card` (generic artifact) | P01 |
| Blackboard | Centralized shared repository for collaborative read/write | MAS literature | `.cex/runtime/` (signals, handoffs, proposals) | P12 |
| Capability Negotiation | Process of agents discovering and agreeing on shared capabilities | ANP, Agora | `dispatch_rule` | P12 |
| Communication Trilemma | Tension between versatility, efficiency, and portability | Agora (Oxford) | Design constraint for `handoff_protocol` | P02 |
| Context-Oriented Protocol | Standardizes agent access to external tools/data/services | Survey taxonomy | MCP-like; CEX `function_def` + `toolkit` | P04 |
| DID (Decentralized Identifier) | W3C standard for verifiable, self-sovereign identity | ANP, ACP, LOKA | Not in CEX -- future `identity_config` kind | P09 |
| Dispatch | Sending a task to a specific agent/nucleus for execution | CEX + A2A | `dispatch_rule` + `handoff` | P12 |
| Flat Architecture | Peer-to-peer agents without hierarchy | MAS literature | `workflow` (peer chain) | P12 |
| Handoff | Transfer of control/context between agents | A2A, OpenAI SDK, CEX | `handoff` / `handoff_protocol` | P12/P02 |
| Hierarchical Architecture | Tiered agents with oversight/execution separation | MAS literature | `supervisor` + `handoff` | P12 |
| Illocutionary Misfire | Ambiguous speech act where intent is misinterpreted | Speech Act theory | Relates to `guardrail` (message validation) | P11 |
| Inter-Agent Protocol | Facilitates agent-to-agent communication and coordination | Survey taxonomy | `handoff_protocol` + `dispatch_rule` | P02/P12 |
| JSON-LD | Linked Data format enabling semantic interoperability | ANP, LMOS | Not in CEX -- future `schema` extension | P06 |
| Message Passing | Direct point-to-point or broadcast message exchange | MAS literature | `handoff` (point-to-point), `signal` (broadcast) | P12 |
| Meta-Protocol | Protocol for negotiating which protocol to use | ANP Layer 2 | Not in CEX -- future `protocol_negotiation` kind | P12 |
| Protocol Document | Plain-text description enabling autonomous protocol negotiation | Agora | Relates to `handoff_protocol` | P02 |
| Protocol Router | Learnable component selecting optimal protocol per scenario | ProtocolBench | Relates to `dispatch_rule` + `fallback_chain` | P12/P02 |
| Sampling | Server-controlled LLM text generation delegation | MCP | `action_prompt` (server-initiated) | P03 |
| Session | Stateful conversation context across interactions | A2A, MCP, ACP | `session_state` | P10 |
| Signal | Async notification of state change or completion | CEX, MAS literature | `signal` (runtime) | P12 |
| Simultaneous-Talk | Concurrent agent communication without turn-taking | MAS literature | Grid dispatch (parallel nuclei) | P12 |
| Speech Act | Utterance designed to trigger actions or state changes | Austin/Searle, MAS | Relates to `action_prompt` | P03 |
| Supervisor | Higher-level agent providing oversight and delegation | Hierarchical MAS | `supervisor` | P12 |
| Task (protocol) | Atomic unit of work with defined input/output | A2A, CrewAI | `action_prompt` / `handoff` | P03/P12 |
| Tool | Callable function an agent can invoke | MCP, all frameworks | `function_def` / `toolkit` | P04 |
| Workflow | Multi-step orchestrated process | LangGraph, CEX | `workflow` / `dag` | P12 |

---

## 8. CEX Architecture Mapping

How CEX's existing inter-nucleus communication maps to the surveyed landscape.

| CEX Mechanism | Protocol Parallel | Architecture Type | Paradigm |
|---|---|---|---|
| `handoff` (.md file in runtime/) | A2A Task submission | Hierarchical (N07 > N0x) | Message Passing |
| `signal` (JSON in runtime/signals/) | A2A SSE notification | Flat (any nucleus signals) | Blackboard (shared dir) |
| `proposal` (.proposal.md) | ACP structured message | Team (concurrent nuclei) | Blackboard |
| `dispatch_rule` (YAML) | A2A Agent Card (capability routing) | Hierarchical | N/A (config, not runtime) |
| `supervisor` (N07) | A2A Client / orchestrator | Hierarchical | Speech Act (directives in handoffs) |
| `workflow` (DAG) | Coral / LMOS workflow | Hybrid | Sequential Message Passing |
| `brand_config` (YAML) | MCP Resource (shared context) | N/A | Blackboard |
| `git commit` (completion signal) | ANP DID-verified event | Flat (any nucleus commits) | Implicit Environmental Signal |
| GDP (decision manifest) | PXP mutual intelligibility | Human-Agent | Speech Act |

### CEX Gaps Identified (future kind candidates)

| Gap | Industry Term | Recommended CEX Kind | Pillar |
|---|---|---|---|
| No decentralized identity | DID / Verifiable Credential | `identity_config` | P09 |
| No protocol negotiation | Meta-Protocol | `protocol_negotiation` | P12 |
| No capability advertisement | Agent Card (A2A standard) | Enhance existing `agent_card` with skills array | P08 |
| No session state across nuclei | Session Management | Enhance `session_state` with cross-nucleus scope | P10 |
| No auction/competitive dispatch | Competition/Mixed-Motive | `auction_dispatch` | P12 |
| No semantic message format | JSON-LD / Linked Data | `semantic_schema` | P06 |

---

## 9. Future Directions (from all sources)

### Short-Term (now)
- Standardize evaluation with ProtocolBench-style benchmarks
- Adopt MCP for tool binding (CEX already does this)
- Add Agent Card (A2A) capability descriptions to `agent_card` kind

### Mid-Term (6-12 months)
- Protocol-aware routing (ProtocolRouter pattern) -- CEX `cex_router.py` already does provider routing; extend to protocol routing
- Layered architecture (ANP model) -- separate identity, meta-protocol, application layers
- Privacy-preserving agent communication (mTLS, short-lived tokens)

### Long-Term (12+ months)
- Collective intelligence infrastructure -- agents forming temporary coalitions
- Agent Data Networks for cross-organization knowledge sharing
- Scaling laws for multi-agent systems (how does performance change with N agents?)
- Society-type architectures with emergent behavior

---

## 10. References

| # | Paper | ArXiv | Year |
|---|---|---|---|
| 1 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2502.14321 | 2025 |
| 2 | A Survey of AI Agent Protocols | 2504.16736 | 2025 |
| 3 | Agent Interoperability Protocols: MCP, ACP, A2A, ANP | 2505.02279 | 2025 |
| 4 | ProtocolBench: Which LLM Multi-Agent Protocol to Choose? | ICLR 2026 sub | 2025 |
| 5 | MultiAgentBench: Evaluating Collaboration and Competition of LLM agents | 2503.01935 | 2025 |

---

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 |
| Domain | multi-agent-communication |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
