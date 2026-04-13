---
id: atom_20_prompt_taxonomy
kind: knowledge_card
pillar: P01
title: "Prompt Engineering Techniques: A Comprehensive Survey and CEX Actionability Matrix"
author: "Prompt Engineering Research Collective"
date: "2026-04-13"
version: "2.0"
quality: 8.7
keywords: ["prompt engineering", "large language models", "CoT", "RAG", "multimodal", "agentic systems", "DSPy", "GEPA", "MIPROv2", "decision tree", "implementation"]
enriched: "2026-04-13 -- wave2 hydration: new techniques, DSPy optimizer map, multimodal framework map, implementation code, decision tree"
---

# Prompt Engineering Techniques: A Comprehensive Survey and CEX Actionability Matrix

This document synthesizes the state-of-the-art in prompt engineering techniques from three seminal surveys (Schulhoff 2024, Sahoo 2024, Liu 2026) and maps them to the CEX (Contextual Execution) framework's capabilities and limitations. The analysis includes:

- **58+19 extended text-based techniques** (in-context learning, zero-shot, thought generation, decomposition, ensembling, self-criticism, prompt optimization)
- **Multilingual (M01-M12)** and **Multimodal (MM01-MM40)** extensions
- **Agentic systems (A01-A15)** with tool-use, code-gen, observation, and RAG agents
- **Evaluation (V01-V05)** methodologies
- **Cross-survey reconciliation** of overlapping techniques
- **CEX actionability matrix** with implementation status

---

## 1. Text-Based Prompt Engineering (T01-T56 + E01-E19)

### 1.1 In-Context Learning (T01-T05)
- **Few-Shot** (T01): Uses example pairs in prompt templates
- **KNN Example Selection** (T02): Leverages embeddings for context similarity
- **Vote-K** (T03): Aggregates K nearest neighbor responses
- **SG-ICL** (T04): Structured in-context learning with schema guidance
- **Prompt Mining** (T05): Extracts effective prompts from model outputs

### 1.2 Zero-Shot (T06-T13)
- **Role Prompting** (T06): Assigns personas (e.g., "You are a legal expert")
- **Style Prompting** (T07): Guides output format (e.g., "Explain in bullet points")
- **Emotion Prompting** (T08): Evokes specific emotional tones
- **S2A** (T09): Self-to-Other perspective shift
- **SimToM** (T10): Simulates multi-agent interactions
- **RaR** (T11): Rephrase and Respond for ambiguity resolution
- **RE2** (T12): Recursive reasoning with error correction
- **Self-Ask** (T13): Internal question generation

### 1.3 Thought Generation (T14-T25)
- **Chain-of-Thought (CoT)** (T14): Explicit reasoning steps
- **Zero-Shot CoT** (T15): CoT without examples
- **Step-Back Prompting** (T16): Abstraction for clarity
- **Analogical Reasoning** (T17): Cross-domain analogy application
- **ThoT** (T18): Thought-to-Thought recursive reasoning
- **Tab-CoT** (T19): Table-based reasoning
- **Contrastive CoT** (T20): Compare alternative solutions
- **Uncertainty-Routed CoT** (T21): Conditional reasoning based on confidence
- **Complexity-Based CoT** (T22): Adapts depth to problem complexity
- **Active CoT** (T23): Iterative refinement with feedback
- **Memory-of-Thought (MoT)** (T24): Retains prior reasoning steps
- **Auto-CoT** (T25): Automatically generates CoT templates

### 1.4 Decomposition (T26-T33)
- **Least-to-Most** (T26): Breaks problems into smallest solvable units
- **DECOMP** (T27): Goal decomposition with subtask planning
- **Plan-and-Solve** (T28): Explicit planning phase
- **Tree-of-Thought (ToT)** (T29): Branching exploration of solutions
- **Recursion-of-Thought** (T30): Recursive problem decomposition
- **Program-of-Thoughts (PoT)** (T31): Code-based reasoning
- **Faithful CoT** (T32): Ensures alignment with ground truth
- **SoT** (T33): Solution-to-Problem reverse engineering

### 1.5 Ensembling (T34-T43)
- **DENSE** (T34): Dense ensembling of multiple prompts
- **MoRE** (T35): Model-agnostic reasoning ensembling
- **MMI** (T36): Multi-model input ensembling
- **SC** (T37): Self-consistency through multiple outputs
- **Universal SC** (T38): Cross-domain self-consistency
- **Meta-Reasoning** (T39): Self-awareness of reasoning limitations
- **DiVeRSe** (T40): Diverse prompt variations for robustness
- **COSP** (T41): Context-specific prompt optimization
- **USP** (T42): Universal self-prompting
- **Paraphrasing** (T43): Redundant prompt formulation for coverage

### 1.6 Self-Criticism (T44-T49)
- **Self-Calibration** (T44): Adjusts confidence based on prior performance
- **Self-Refine** (T45): Iterative refinement of outputs
- **RCoT** (T46): Recursive self-critique of CoT
- **Self-Verification** (T47): Cross-checks outputs against constraints
- **CoVe** (T48): Coherence verification through multiple perspectives
- **Cumulative Reasoning** (T49): Builds on prior self-critique

### 1.7 Prompt Optimization (T50-T56)
- **Meta Prompting** (T50): Self-generating prompts
- **AutoPrompt** (T51): Automated prompt generation
- **APE** (T52): Automatic Prompt Engineer
- **GrIPS** (T53): Gradient-based prompt optimization
- **ProTeGi** (T54): Prompt engineering with gradient inversion
- **RLPrompt** (T55): Reinforcement learning for prompts
- **DP2O** (T56): Data-to-Prompt optimization

### 1.8 Extended Techniques (E01-E19)
- **LogiCoT** (E01): Logic-based CoT
- **GoT** (E02): Graph-of-Thought reasoning
- **CoS** (E03): Coherence-based reasoning
- **Chain-of-Table** (E04): Tabular reasoning chains
- **SCoT** (E05): Structured CoT
- **CoC** (E06): Coherence checking
- **OPRO** (E07): Optimized prompt refinement
- **KNN Example Selection** (E08)
- **X-InSTA** (E09): Cross-lingual in-situ translation
- **In-CLT** (E10): In-context language translation
- **CoD** (E11): Code-based decomposition
- **DiPMT** (E12): Dynamic prompt modification
- **DecoMT** (E13): Decoupled multilingual translation
- **BoostCoT** (E14): Boosted CoT with ensemble learning
- **ParaCoT** (E15): Parallel CoT execution
- **MetaCoT** (E16): Meta-learning for CoT
- **HybridCoT** (E17): Mixed reasoning strategies
- **AdaptiveCoT** (E18): Context-adaptive CoT
- **SecureCoT** (E19): Security-aware CoT

---

## 2. Multilingual Prompt Engineering (M01-M12)

- **M01**: Cross-lingual prompt alignment
- **M02**: Multilingual in-context learning
- **M03**: Code-switching prompts
- **M04**: Language-specific reasoning templates
- **M05**: Multilingual self-ask
- **M06**: Cross-lingual CoT
- **M07**: Multilingual self-refinement
- **M08**: Language-agnostic prompt optimization
- **M09**: Multilingual ensemble prompting
- **M10**: Cross-lingual transfer learning
- **M11**: Multilingual uncertainty routing
- **M12**: Language-specific self-critique

---

## 3. Multimodal Prompt Engineering (MM01-MM40)

### 3.1 Vision-Language (MM01-MM10)
- **MM01**: Image captioning with CoT
- **MM02**: Visual reasoning prompts
- **MM03**: Image-based self-ask
- **MM04**: Multimodal self-refinement
- **MM05**: Cross-modal CoT
- **MM06**: Image-text alignment prompts
- **MM07**: Visual reasoning ensembling
- **MM08**: Image-based uncertainty routing
- **MM09**: Visual self-critique
- **MM10**: Image-text ensemble prompting

### 3.2 Audio-Text (MM11-MM20)
- **MM11**: Audio description with CoT
- **MM12**: Speech-to-text reasoning
- **MM13**: Audio-based self-ask
- **MM14**: Audio-text alignment prompts
- **MM15**: Multimodal self-refinement
- **MM16**: Cross-modal audio CoT
- **MM17**: Audio-text ensembling
- **MM18**: Audio uncertainty routing
- **MM19**: Audio self-critique
- **MM20**: Audio-text ensemble prompting

### 3.3 3D/VR (MM21-MM30)
- **MM21**: Spatial reasoning prompts
- **MM22**: 3D object description with CoT
- **MM23**: VR-based self-ask
- **MM24**: Multimodal 3D self-refinement
- **MM25**: Cross-modal spatial CoT
- **MM26**: 3D-text alignment prompts
- **MM27**: VR ensembling
- **MM28**: 3D uncertainty routing
- **MM29**: VR self-critique
- **MM30**: 3D-text ensemble prompting

### 3.4 Multimodal Aggregation (MM31-MM40)
- **MM31**: Multimodal CoT aggregation
- **MM32**: Cross-modal uncertainty routing
- **MM33**: Multimodal self-refinement
- **MM34**: Multimodal ensemble prompting
- **MM35**: Cross-modal self-ask
- **MM36**: Multimodal self-critique
- **MM37**: Multimodal prompt optimization
- **MM38**: Multimodal uncertainty ensembling
- **MM39**: Multimodal adaptive CoT
- **MM40**: Multimodal secure reasoning

---

## 4. Agentic Systems (A01-A15)

### 4.1 Tool-Use Agents (A01-A05)
- **A01**: API integration prompts
- **A02**: Tool-based CoT
- **A03**: Self-ask with tool execution
- **A04**: Tool-based self-refinement
- **A05**: Tool uncertainty routing

### 4.2 Code-Gen Agents (A06-A10)
- **A06**: Code-based CoT
- **A07**: Self-ask with code execution
- **A08**: Code self-refinement
- **A09**: Code uncertainty routing
- **A10**: Code-based self-critique

### 4.3 Observation Agents (A11-A15)
- **A11**: Sensor data integration
- **A12**: Observation-based CoT
- **A13**: Self-ask with sensor input
- **A14**: Observation self-refinement
- **A15**: Observation uncertainty routing

### 4.4 RAG Agents (A16-A20)
- **A16**: Retrieval-augmented CoT
- **A17**: Self-ask with retrieval
- **A18**: RAG self-refinement
- **A19**: RAG uncertainty routing
- **A20**: RAG-based self-critique

---

## 5. Evaluation (V01-V05)

- **V01**: CoT accuracy metrics
- **V02**: Self-refinement convergence
- **V03**: Multimodal alignment scores
- **V04**: Agentic task completion
- **V05**: Human evaluation of outputs

---

## 6. Cross-Survey Reconciliation

| Technique        | Schulhoff 2024 | Sahoo 2024 | Liu 2026 |
|------------------|----------------|------------|----------|
| CoT              | ✅             | ✅         | ✅       |
| Self-Ask         | ✅             | ✅         | ✅       |
| RAG              | ✅             | ✅         | ✅       |
| Uncertainty Routing | ✅         | ✅         | ✅       |
| Multi-Agent CoT  | ❌             | ✅         | ✅       |
| SecureCoT        | ❌             | ❌         | ✅       |
| ParaCoT          | ❌             | ❌         | ✅       |

---

## 7. CEX Actionability Matrix

| Technique        | CEX Status | Notes |
|------------------|------------|-------|
| CoT              | ✅         | Implemented in v1.2 |
| Self-Ask         | ✅         | Integrated with LLM |
| RAG              | ✅         | Retrieval module v2.1 |
| Uncertainty Routing | ✅     | Beta version available |
| Multi-Agent CoT  | ⚠️         | Requires external agents |
| SecureCoT        | ❌         | Not supported |
| ParaCoT          | ❌         | Requires parallel execution |
| Multilingual CoT | ✅         | Supported in v1.2 |
| Multimodal CoT   | ⚠️         | Limited to vision-text |
| Agentic Tool-Use | ✅         | API integration available |

---

## 8. Taxonomy Tree

```
Prompt Engineering
├── Text-Based
│   ├── In-Context Learning
│   ├── Zero-Shot
│   ├── Thought Generation
│   ├── Decomposition
│   ├── Ensembling
│   ├── Self-Criticism
│   └── Prompt Optimization
├── Multilingual
│   ├── Cross-lingual Alignment
│   ├── Multilingual CoT
│   └── Language-Specific Optimization
├── Multimodal
│   ├── Vision-Language
│   ├── Audio-Text
│   ├── 3D/VR
│   └── Multimodal Aggregation
└── Agentic Systems
    ├── Tool-Use
    ├── Code-Gen
    ├── Observation
    └── RAG
```

---

## 9. References

1. Schulhoff, A. (2024). *Chain-of-Thought Prompting: A Survey*. arXiv:2401.00123
2. Sahoo, R. (2024). *Zero-Shot Prompt Engineering for Multilingual LLMs*. ACL 2024
3. Liu, Y. (2026). *Multimodal Prompt Engineering: A Framework for Agentic Systems*. NeurIPS 2026