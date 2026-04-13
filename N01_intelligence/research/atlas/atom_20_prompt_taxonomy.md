---
id: atom_20_prompt_taxonomy
kind: knowledge_card
pillar: P01
domain: prompt_engineering
version: "1.0"
quality: null
tags: [prompt-engineering, taxonomy, techniques, survey, atlas]
sources:
  - "Schulhoff et al. 2024 - The Prompt Report (arXiv 2406.06608)"
  - "Sahoo et al. 2024 - Systematic Survey of PE in LLMs (arXiv 2402.07927)"
  - "Liu et al. 2026 - Comprehensive Taxonomy of PE (Springer, Frontiers of CS)"
date: 2026-04-13
---

# Atom 20: Prompt Engineering Taxonomy

> Unified atlas of prompting techniques extracted from 3 foundational surveys.
> 58 text-based + 12 multilingual + 40 multimodal + 15 agentic = 125 catalogued techniques.

---

## 1. Vocabulary (33 Core Terms)

From Schulhoff et al. (The Prompt Report, 2024).

| # | Term | Definition |
|---|------|-----------|
| 1 | Prompt | Input provided to a GenAI model to guide its output |
| 2 | Prompt Template | Function with variables that produces a prompt instance when filled |
| 3 | Directive | The core instruction component within a prompt |
| 4 | Examples (Exemplars) | Demonstration input-output pairs included in a prompt |
| 5 | Output Formatting | Constraints on result structure (JSON, table, list, etc.) |
| 6 | Style Instructions | Guidelines for tone, register, and presentation |
| 7 | Role | Assigned persona that shapes model behavior |
| 8 | Additional Context | Supplementary background material injected into the prompt |
| 9 | Prompting | The act of providing input to a GenAI model |
| 10 | Prompt Chain | Sequential connection of prompts where output N feeds input N+1 |
| 11 | Prompting Technique | A specific method for structuring or augmenting prompts |
| 12 | Prompt Engineering | Systematic development and optimization of prompts |
| 13 | PE Technique | Automated or systematic method for optimizing prompts |
| 14 | Exemplar | A single example instance used in a demonstration set |
| 15 | Context Window | Maximum token capacity available for prompt + completion |
| 16 | Priming | Preparatory input that influences subsequent model responses |
| 17 | Hard (Discrete) Prompt | A fixed text-based prompt (human-readable tokens) |
| 18 | Soft (Continuous) Prompt | Learnable embedding vectors prepended to the input |
| 19 | User Prompt | Input originating from end users |
| 20 | Assistant Prompt | Model-generated response components |
| 21 | System Prompt | Framework-level instructions read first by the model |
| 22 | Cloze Prompt | Fill-in-the-blank prediction format |
| 23 | Prefix Prompt | Completion-based prediction format |
| 24 | Prompt-Based Learning | Learning through prompt structures rather than fine-tuning |
| 25 | Prompt Tuning | Optimizing learned soft prompt embeddings via gradients |
| 26 | Answer Shape | Expected structure of the output (list, number, paragraph) |
| 27 | Answer Space | Constrained set of valid output values |
| 28 | Answer Extractor | Mechanism for parsing the final answer from model output |
| 29 | Verbalizer | Mapping from model logits/tokens to answer labels |
| 30 | Regex Extractor | Pattern-based extraction of structured answers |
| 31 | In-Context Learning (ICL) | Learning task behavior from examples within the context window |
| 32 | Few-Shot Learning | Learning from a small number of demonstration examples |
| 33 | Conversational PE | Interactive, multi-turn refinement of prompts with the model |

---

## 2. Text-Based Techniques (58)

### 2.1 In-Context Learning (ICL) -- 5 techniques

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| T01 | Few-Shot Prompting | Provide k input-output exemplars to demonstrate the task | `prompt_template` |
| T02 | KNN-based Example Selection | Select the k most similar examples via embedding distance | `prompt_template` + `embedding_config` |
| T03 | Vote-K | Ensemble of k example variants; majority-vote the best set | `prompt_template` |
| T04 | Self-Generated ICL (SG-ICL) | Model generates its own examples before answering | `action_prompt` |
| T05 | Prompt Mining | Extract effective prompt patterns from existing data/logs | `prompt_compiler` |

### 2.2 Zero-Shot Techniques -- 8 techniques

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| T06 | Role Prompting | Assign a persona/role to shape behavior ("You are a...") | `system_prompt` |
| T07 | Style Prompting | Direct output format, register, and tone | `prompt_template` |
| T08 | Emotion Prompting | Append emotional stimulus ("This is important for my career") | `prompt_template` |
| T09 | System 2 Attention (S2A) | Regenerate input to selectively attend to relevant context only | `action_prompt` |
| T10 | SimToM | Simulate theory-of-mind to reason about other agents' beliefs | `action_prompt` |
| T11 | Rephrase and Respond (RaR) | Model rephrases the question for clarity, then answers | `action_prompt` |
| T12 | Re-reading (RE2) | Model reads the input multiple times before answering | `action_prompt` |
| T13 | Self-Ask | Model generates clarifying sub-questions, answers them, then answers the original | `chain` |

### 2.3 Thought Generation -- 12 techniques

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| T14 | Chain-of-Thought (CoT) | Include explicit step-by-step reasoning before the final answer | `reasoning_trace` |
| T15 | Zero-Shot CoT | Append "Let's think step by step" without exemplars | `action_prompt` |
| T16 | Step-Back Prompting | First extract high-level principles, then solve the specific problem | `chain` |
| T17 | Analogical Prompting | Reason through an analogous problem before solving the target | `chain` |
| T18 | Thread-of-Thought (ThoT) | Organize reasoning into threaded segments for long contexts | `reasoning_trace` |
| T19 | Tabular CoT (Tab-CoT) | Structure intermediate reasoning in table format | `reasoning_trace` |
| T20 | Contrastive CoT | Provide both correct AND incorrect reasoning exemplars | `prompt_template` |
| T21 | Uncertainty-Routed CoT | Route to CoT only when model confidence is below threshold | `router` |
| T22 | Complexity-Based Prompting | Select exemplars by difficulty level; harder = more reasoning | `prompt_template` |
| T23 | Active Prompting | Identify uncertain instances via disagreement, then annotate those | `action_prompt` |
| T24 | Memory-of-Thought (MoT) | Maintain a memory of past reasoning chains for reuse | `memory_summary` + `reasoning_trace` |
| T25 | Auto-CoT | Cluster questions, auto-generate one CoT per cluster | `prompt_template` |

### 2.4 Decomposition -- 8 techniques

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| T26 | Least-to-Most Prompting | Decompose into sub-problems; solve easiest first, build up | `chain` |
| T27 | Decomposed Prompting (DECOMP) | Break task into typed sub-tasks, route each to specialized handler | `workflow` |
| T28 | Plan-and-Solve | Generate a plan first, then execute each step | `chain` |
| T29 | Tree-of-Thought (ToT) | Explore multiple reasoning branches; backtrack if stuck | `workflow` |
| T30 | Recursion-of-Thought | Recursively decompose until base case, then compose answers up | `chain` |
| T31 | Program-of-Thoughts (PoT) | Convert reasoning to executable code; run code for answer | `action_prompt` |
| T32 | Faithful CoT | Two-stage: natural language plan + symbolic execution for faithfulness | `chain` |
| T33 | Skeleton-of-Thought (SoT) | Generate a structural outline first, then flesh out each section | `chain` |

### 2.5 Ensembling -- 10 techniques

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| T34 | Demonstration Ensembling (DENSE) | Run the same query with multiple demo sets; combine results | `prompt_template` |
| T35 | Mixture of Reasoning Experts (MoRE) | Route to specialized reasoning strategies per sub-task type | `router` |
| T36 | Max Mutual Information | Select demonstrations that maximize mutual info with the query | `prompt_template` |
| T37 | Self-Consistency (SC) | Sample N reasoning paths; majority-vote the final answer | `action_prompt` |
| T38 | Universal Self-Consistency | Extend SC across prompt variations and model temperatures | `action_prompt` |
| T39 | Meta-Reasoning over Multiple CoTs | Generate multiple CoTs, then reason about which is best | `chain` |
| T40 | DiVeRSe | Diverse verifier + reasoning ensemble with step-aware voting | `workflow` |
| T41 | COSP (Consistency-based Self-adaptive Prompting) | Adaptively select examples based on self-consistency signal | `action_prompt` |
| T42 | USP (Universal Self-Adaptive Prompting) | Generalize COSP across task types without task-specific tuning | `action_prompt` |
| T43 | Prompt Paraphrasing | Rephrase the same prompt N ways; aggregate results for robustness | `prompt_template` |

### 2.6 Self-Criticism -- 6 techniques

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| T44 | Self-Calibration | Model estimates its own confidence; flag low-confidence answers | `quality_gate` |
| T45 | Self-Refine | Iterative loop: generate -> critique -> revise (no external feedback) | `action_prompt` |
| T46 | Reverse CoT (RCoT) | Reconstruct the problem from the answer to verify consistency | `action_prompt` |
| T47 | Self-Verification | Model checks each reasoning step against known constraints | `action_prompt` |
| T48 | Chain-of-Verification (CoVe) | Plan verification questions -> answer them -> revise original answer | `chain` |
| T49 | Cumulative Reasoning | Build conclusions incrementally; each step verified before proceeding | `reasoning_trace` |

### 2.7 Prompt Optimization (Automated PE) -- 7 techniques

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| T50 | Meta Prompting | Use a prompt to generate/optimize other prompts | `prompt_compiler` |
| T51 | AutoPrompt | Gradient-guided search over discrete token space for optimal prompts | `prompt_compiler` |
| T52 | Automatic Prompt Engineer (APE) | LLM generates candidate prompts; evaluate and select the best | `prompt_compiler` |
| T53 | GrIPS | Gradient-free search: edit, swap, paraphrase, delete operations | `prompt_compiler` |
| T54 | ProTeGi | Use textual "gradients" (error descriptions) to refine prompts | `prompt_compiler` |
| T55 | RLPrompt | Reinforcement learning to optimize discrete prompt tokens | `prompt_compiler` |
| T56 | DP2O | Dialogue-based policy-gradient discrete prompt optimization | `prompt_compiler` |

### 2.8 Additional Text Techniques (from Sahoo et al. + Liu et al.)

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| T57 | Graph-of-Thought (GoT) | Model thoughts as graph nodes with dependency edges; enables merging | `workflow` |
| T58 | Scratchpad Prompting | Allow model to write intermediate tokens before final answer | `action_prompt` |

---

## 3. Extended Techniques (from Sahoo 2024 + Liu 2026)

Techniques catalogued by the second and third surveys that extend or refine the core 58.

### 3.1 Advanced Reasoning Structures

| # | Technique | Source | Definition | CEX Kind |
|---|-----------|--------|-----------|----------|
| E01 | LogiCoT | Sahoo | Apply symbolic logic + verification to CoT steps | `chain` |
| E02 | Chain-of-Symbol (CoS) | Sahoo | Replace natural language with condensed symbols for spatial reasoning | `action_prompt` |
| E03 | Chain-of-Table | Sahoo | Iterative SQL/DataFrame ops for step-by-step tabular reasoning | `action_prompt` |
| E04 | Code Prompting | Sahoo | Reformulate NL problems as code to trigger structured reasoning | `action_prompt` |
| E05 | Self-Harmonized CoT (ECHO) | Sahoo | Cluster diverse reasoning paths into unified coherent patterns | `action_prompt` |
| E06 | Logic-of-Thought | Sahoo | Enrich prompts with propositional logic before reasoning | `chain` |
| E07 | Instance-Adaptive Prompting (IAP) | Sahoo | Dynamically tailor prompt complexity per-instance via saliency | `router` |
| E08 | Layer-of-Thoughts (LoT) | Sahoo | Organize reasoning into constraint hierarchy layers | `chain` |
| E09 | Narrative-of-Thought (NoT) | Sahoo | Temporal reasoning via structured narrative representation | `action_prompt` |
| E10 | Buffer of Thoughts (BoT) | Sahoo | Reusable high-level reasoning templates in a meta-buffer | `prompt_cache` |
| E11 | Chain-of-Draft (CoD) | Sahoo | Concise, information-dense intermediate steps for efficiency | `reasoning_trace` |
| E12 | Contrastive Denoising CoT (CD-CoT) | Sahoo | Contrast noisy vs. clean rationales to handle flawed reasoning | `action_prompt` |
| E13 | Reverse CoT (R-CoT, geometric) | Sahoo | Generate geometric data with step-by-step descriptions | `action_prompt` |
| E14 | End-to-End DAG-Path (EEDP) | Sahoo | Prioritize backbone paths in graph structures | `action_prompt` |
| E15 | Structured CoT (SCoT) | Sahoo | Incorporate program structures (sequence, branch, loop) into CoT | `chain` |
| E16 | Chain-of-Code (CoC) | Sahoo | Format semantic sub-tasks as pseudocode with interpreter simulation | `action_prompt` |
| E17 | Chain-of-Note (CoN) | Sahoo | Evaluate document relevance; filter noise in RAG pipelines | `action_prompt` |
| E18 | Chain-of-Knowledge (CoK) | Sahoo | Dynamic knowledge adaptation from multiple sources per step | `chain` |
| E19 | OPRO (Optimization by Prompting) | Sahoo | LLM as optimizer: iteratively generate improved solutions in NL | `prompt_compiler` |

### 3.2 Knowledge & Retrieval (from Liu 2026)

| # | Technique | Source | Definition | CEX Kind |
|---|-----------|--------|-----------|----------|
| K01 | Basic RAG | Liu | Index -> retrieve top-k -> generate with context | `rag_source` |
| K02 | Query Rewriting (Query2Doc) | Liu | LLM generates pseudo-documents to improve retrieval query | `action_prompt` |
| K03 | ITER-RETGEN | Liu | Iterative retrieval: generate -> retrieve -> refine -> repeat | `chain` |
| K04 | Content Adjusting | Liu | Post-retrieval: reconstruct documents to emphasize critical sections | `action_prompt` |
| K05 | Structure Adjusting | Liu | Post-retrieval: categorize documents by relevance tiers | `action_prompt` |
| K06 | External Memory Management | Liu | Store retrieved results as persistent reference pools | `entity_memory` |
| K07 | Internal Memory Feedback | Liu | Use LLM feedback to evaluate and rank retrieved information | `action_prompt` |

### 3.3 Reliability & Bias Mitigation (from Liu 2026)

| # | Technique | Source | Definition | CEX Kind |
|---|-----------|--------|-----------|----------|
| R01 | Prompt Ensembling (Bagging) | Liu | Multiple prompts + majority voting via Self-Consistency | `action_prompt` |
| R02 | Boosting Prompt (Prefer) | Liu | AdaBoost-style optimization with iterative feedback | `action_prompt` |
| R03 | Bilateral Confidence | Liu | Forward + reverse evaluation for reliability scoring | `quality_gate` |
| R04 | AMA (Ask Me Anything) | Liu | Multi-perspective aggregation using information entropy | `action_prompt` |
| R05 | Detoxification Prompting | Liu | Substitute toxic textual representations at prompt level | `guardrail` |

---

## 4. Multilingual Techniques (12)

From Schulhoff et al. (The Prompt Report, 2024).

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| M01 | Translate First | Translate input to English, process, translate back | `chain` |
| M02 | XLT (Cross-Lingual Thought) | CoT reasoning that crosses language boundaries | `chain` |
| M03 | CLSP (Cross-Lingual Self-Consistent) | Self-consistency across multiple languages | `action_prompt` |
| M04 | X-InSTA | Cross-lingual in-context learning with alignment | `prompt_template` |
| M05 | In-CLT (Cross-Lingual Transfer) | Transfer few-shot learning across languages | `prompt_template` |
| M06 | PARC | Prompts augmented by cross-lingual retrieval | `rag_source` |
| M07 | MAPS (Multi-Aspect Prompting) | Multi-faceted prompting for machine translation | `chain` |
| M08 | Chain-of-Dictionary (CoD) | Dictionary-guided translation with lexical support | `chain` |
| M09 | DiPMT | Dictionary-based prompting for MT | `prompt_template` |
| M10 | DecoMT | Decomposed prompting for modular translation | `chain` |
| M11 | ICP (Interactive Chain Prompting) | Human-in-the-loop translation refinement | `hitl_config` + `chain` |
| M12 | Iterative Prompting | Repeated refinement cycles for translation quality | `action_prompt` |

---

## 5. Multimodal Techniques (40)

From Schulhoff et al. (The Prompt Report, 2024). Grouped by modality.

### 5.1 Image Prompting (7)

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| MM01 | Prompt Modifiers | Text additions that modify image generation style/content | `prompt_template` |
| MM02 | Negative Prompting | Specify unwanted attributes to exclude from generation | `prompt_template` |
| MM03 | Paired-Image Prompting | Use example image pairs to demonstrate desired transformation | `prompt_template` |
| MM04 | Image-as-Text Prompting | Convert images to text descriptions for text-only models | `action_prompt` |
| MM05 | DDCoT (Duty Distinct CoT) | Separate reasoning duties across visual + textual modalities | `chain` |
| MM06 | Multimodal Graph-of-Thought | Graph-structured reasoning across text + image nodes | `workflow` |
| MM07 | Chain-of-Images (CoI) | Sequential image generation with reasoning between steps | `chain` |

### 5.2 Audio Prompting (7)

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| MM08 | Audio Prefix Prompting | Prepend audio context before text instruction | `prompt_template` |
| MM09 | Audio Few-Shot | Provide audio input-output exemplars | `prompt_template` |
| MM10 | Speech Chain-of-Thought | Step-by-step reasoning over speech/audio inputs | `chain` |
| MM11 | Audio Negative Prompting | Specify unwanted audio characteristics | `prompt_template` |
| MM12 | Audio Style Transfer Prompting | Direct audio generation to match a reference style | `prompt_template` |
| MM13 | Interleaved Audio-Text | Alternate between audio and text in multi-turn prompts | `chain` |
| MM14 | Audio Retrieval-Augmented | Retrieve similar audio samples to augment generation | `rag_source` |

### 5.3 Video Prompting (8)

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| MM15 | Video Prefix Prompting | Prepend video context for video understanding tasks | `prompt_template` |
| MM16 | Keyframe Selection Prompting | Select representative frames to reduce video to images | `action_prompt` |
| MM17 | Temporal Chain-of-Thought | Reason step-by-step through temporal video sequences | `chain` |
| MM18 | Video Negative Prompting | Exclude unwanted motion/content from video generation | `prompt_template` |
| MM19 | Storyboard Prompting | Decompose video generation into keyframe storyboard then interpolate | `chain` |
| MM20 | Motion-Guided Prompting | Use motion vectors/trajectories to guide video generation | `prompt_template` |
| MM21 | Video-Text Interleaving | Alternate video clips and text instructions | `chain` |
| MM22 | Temporal Grounding Prompting | Anchor text descriptions to specific time ranges in video | `prompt_template` |

### 5.4 Segmentation Prompting (9)

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| MM23 | Point Prompting | Click-based points to indicate regions of interest | `action_prompt` |
| MM24 | Box Prompting | Bounding boxes to define segmentation regions | `action_prompt` |
| MM25 | Mask Prompting | Provide partial masks as hints for segmentation | `prompt_template` |
| MM26 | Text-Guided Segmentation | Natural language descriptions to identify segments | `action_prompt` |
| MM27 | Scribble Prompting | Rough scribble annotations to indicate foreground/background | `action_prompt` |
| MM28 | Hierarchical Prompt | Multi-level prompts for coarse-to-fine segmentation | `chain` |
| MM29 | Cross-Modal Segment Prompting | Use one modality (text) to segment another (image) | `action_prompt` |
| MM30 | Interactive Segmentation Prompting | Iterative refinement with user feedback per round | `hitl_config` |
| MM31 | Compositional Segment Prompting | Compose multiple prompt types (point + text + box) | `prompt_template` |

### 5.5 3D Prompting (9)

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| MM32 | Text-to-3D Prompting | Natural language description to generate 3D objects | `prompt_template` |
| MM33 | Image-to-3D Prompting | Single or multi-view images as 3D generation input | `prompt_template` |
| MM34 | 3D Negative Prompting | Specify unwanted geometric or textural properties | `prompt_template` |
| MM35 | Multi-View Consistency Prompting | Enforce consistency across multiple viewpoint renders | `action_prompt` |
| MM36 | Depth-Guided Prompting | Use depth maps to guide 3D structure generation | `prompt_template` |
| MM37 | Scene Composition Prompting | Describe spatial layout of multiple 3D objects | `prompt_template` |
| MM38 | NeRF-Style Prompting | Prompts optimized for neural radiance field generation | `prompt_template` |
| MM39 | Texture Transfer Prompting | Separate geometry from texture in 3D generation prompts | `prompt_template` |
| MM40 | 3D Chain-of-Thought | Step-by-step reasoning for complex 3D scene construction | `chain` |

---

## 6. Agentic Techniques (15)

From Schulhoff et al. -- agent extensions that build on prompting foundations.

### 6.1 Tool-Use Agents

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| A01 | MRKL (Modular Reasoning, Knowledge, Language) | Route sub-tasks to specialized tools/modules | `agent` + `router` |
| A02 | CRITIC (Self-Correcting with Tool-Interactive Critiquing) | Use external tools to verify and correct reasoning | `action_prompt` + `cli_tool` |
| A03 | ART (Automatic Reasoning and Tool-use) | Auto-select tools and integrate into multi-step reasoning | `workflow` |
| A04 | Toolformer | LLM learns to insert API calls into its own generation | `agent` + `api_client` |
| A05 | TaskWeaver | Decompose tasks with automatic tool/code integration | `workflow` |

### 6.2 Code-Generation Agents

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| A06 | PAL (Program-Aided Language Model) | Offload computation to code execution | `action_prompt` |
| A07 | ToRA (Tool-Integrated Reasoning Agent) | Structured interleaving of NL reasoning and tool calls | `workflow` |

### 6.3 Observation-Based Agents

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| A08 | ReAct (Reasoning + Acting) | Interleave thought -> action -> observation loops | `workflow` |
| A09 | Reflexion | Learn from execution feedback via episodic memory | `learning_record` + `workflow` |
| A10 | Voyager | Lifelong learning agent with skill library | `agent` + `skill` |
| A11 | GITM (Ghost in the Minecraft) | Persistent environment learning with goal decomposition | `agent` + `workflow` |

### 6.4 RAG Agents

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| A12 | Verify-and-Edit | Retrieve -> verify retrieved facts -> edit answer | `chain` + `rag_source` |
| A13 | Demonstrate-Search-Predict (DSP) | Example-guided retrieval with prediction pipeline | `chain` + `rag_source` |
| A14 | IRCoT (Interleaved Retrieval guided by CoT) | CoT reasoning interleaved with retrieval steps | `chain` + `rag_source` |
| A15 | Iterative Retrieval Augmentation | Multiple retrieval-generation cycles for refinement | `chain` + `rag_source` |

---

## 7. Evaluation Techniques (5)

| # | Technique | Definition | CEX Kind |
|---|-----------|-----------|----------|
| V01 | LLM-EVAL | Model-based evaluation of generated text | `llm_judge` |
| V02 | G-EVAL | Graph-based evaluation framework using CoT criteria | `scoring_rubric` |
| V03 | ChatEval | Multi-agent debate for conversational evaluation | `llm_judge` |
| V04 | Batch Prompting | Group multiple evaluation instances per API call | `action_prompt` |
| V05 | Pairwise Evaluation | Compare two outputs head-to-head with LLM judge | `llm_judge` |

---

## 8. CEX Kind Mapping Summary

How the 125 techniques map to CEX's typed kind system.

| CEX Kind | Count | Techniques (sample) |
|----------|-------|---------------------|
| `prompt_template` | 28 | Few-Shot, Style, Emotion, Negative, MM01-MM40 image/video/3D |
| `action_prompt` | 31 | SG-ICL, S2A, Self-Refine, Self-Verify, Scratchpad, RE2, RaR |
| `chain` | 24 | Self-Ask, Step-Back, Plan-and-Solve, CoVe, Translate First, XLT |
| `workflow` | 8 | DECOMP, ToT, DiVeRSe, GoT, ReAct, TaskWeaver, ART |
| `reasoning_trace` | 5 | CoT, ThoT, Tab-CoT, Cumulative Reasoning, CoD |
| `router` | 3 | Uncertainty-Routed CoT, MoRE, IAP |
| `prompt_compiler` | 8 | Meta Prompting, APE, AutoPrompt, GrIPS, ProTeGi, OPRO |
| `system_prompt` | 1 | Role Prompting |
| `quality_gate` | 2 | Self-Calibration, Bilateral Confidence |
| `rag_source` | 4 | Basic RAG, PARC, Audio RAG, Verify-and-Edit |
| `agent` | 4 | MRKL, Toolformer, Voyager, GITM |
| `llm_judge` | 3 | LLM-EVAL, ChatEval, Pairwise |
| `scoring_rubric` | 1 | G-EVAL |
| `guardrail` | 1 | Detoxification Prompting |
| `memory_summary` | 1 | Memory-of-Thought |
| `entity_memory` | 1 | External Memory Management |
| `prompt_cache` | 1 | Buffer of Thoughts |
| `hitl_config` | 2 | ICP, Interactive Segmentation |
| `learning_record` | 1 | Reflexion |
| `skill` | 1 | Voyager (skill library) |
| `embedding_config` | 1 | KNN Example Selection |

---

## 9. Cross-Survey Reconciliation

Techniques that appear in multiple surveys under different names.

| Schulhoff (2024) | Sahoo (2024) | Liu (2026) | Canonical Name |
|-------------------|-------------|-----------|----------------|
| Step-Back Prompting | Take a Step Back | Abstraction Prompting | Step-Back Prompting |
| Self-Consistency | Self-Consistency | Bagging (majority vote) | Self-Consistency |
| CoVe | CoVe | -- | Chain-of-Verification |
| Self-Refine | Self-Refine | Internal Feedback | Self-Refine |
| Emotion Prompting | Emotion Prompting | -- | Emotion Prompting |
| Tree-of-Thought | Tree-of-Thoughts | Technique-enhanced CoT | Tree-of-Thought |
| Program-of-Thoughts | Program of Thoughts (PoT) | Code Interpreter | Program-of-Thoughts |
| DiVeRSe | DiVeRSe | DiVeRSe | DiVeRSe |
| APE | APE | -- | Automatic Prompt Engineer |
| RaR | RaR | Query Rewriting | Rephrase and Respond |
| -- | GoT | Graph-based CoT | Graph-of-Thought |
| -- | Chain-of-Table | -- | Chain-of-Table |
| -- | -- | Boosting Prompt | Boosting Prompt |

---

## 10. Taxonomy Tree (Hierarchical View)

```
Prompt Engineering Techniques
|
+-- TEXT-BASED (58+19 extended)
|   +-- In-Context Learning (T01-T05)
|   |   +-- Few-Shot, KNN, Vote-K, SG-ICL, Prompt Mining
|   +-- Zero-Shot (T06-T13)
|   |   +-- Role, Style, Emotion, S2A, SimToM, RaR, RE2, Self-Ask
|   +-- Thought Generation (T14-T25)
|   |   +-- CoT, Zero-Shot CoT, Step-Back, Analogical, ThoT
|   |   +-- Tab-CoT, Contrastive CoT, Uncertainty-Routed CoT
|   |   +-- Complexity-Based, Active, MoT, Auto-CoT
|   +-- Decomposition (T26-T33)
|   |   +-- Least-to-Most, DECOMP, Plan-and-Solve, ToT
|   |   +-- Recursion-of-Thought, PoT, Faithful CoT, SoT
|   +-- Ensembling (T34-T43)
|   |   +-- DENSE, MoRE, MMI, SC, Universal SC
|   |   +-- Meta-Reasoning, DiVeRSe, COSP, USP, Paraphrasing
|   +-- Self-Criticism (T44-T49)
|   |   +-- Self-Calibration, Self-Refine, RCoT
|   |   +-- Self-Verification, CoVe, Cumulative Reasoning
|   +-- Prompt Optimization (T50-T56)
|   |   +-- Meta, AutoPrompt, APE, GrIPS, ProTeGi, RLPrompt, DP2O
|   +-- Extended (E01-E19)
|       +-- LogiCoT, GoT, CoS, Chain-of-Table, SCoT, CoC, OPRO...
|
+-- MULTILINGUAL (M01-M12)
|   +-- Translate First, XLT, CLSP, X-InSTA, In-CLT
|   +-- PARC, MAPS, CoD, DiPMT, DecoMT, ICP, Iterative
|
+-- MULTIMODAL (MM01-MM40)
|   +-- Image (7): Modifiers, Negative, Paired, Image-as-Text, DDCoT, MGoT, CoI
|   +-- Audio (7): Prefix, Few-Shot, Speech CoT, Negative, Style, Interleaved, RAG
|   +-- Video (8): Prefix, Keyframe, Temporal CoT, Negative, Storyboard, Motion, Interleaved, Grounding
|   +-- Segmentation (9): Point, Box, Mask, Text, Scribble, Hierarchical, Cross-Modal, Interactive, Compositional
|   +-- 3D (9): Text-to-3D, Image-to-3D, Negative, Multi-View, Depth, Scene, NeRF, Texture, 3D CoT
|
+-- AGENTIC (A01-A15)
|   +-- Tool-Use: MRKL, CRITIC, ART, Toolformer, TaskWeaver
|   +-- Code-Gen: PAL, ToRA
|   +-- Observation: ReAct, Reflexion, Voyager, GITM
|   +-- RAG Agents: Verify-and-Edit, DSP, IRCoT, Iterative RA
|
+-- EVALUATION (V01-V05)
    +-- LLM-EVAL, G-EVAL, ChatEval, Batch, Pairwise
```

---

## 11. CEX Actionability Matrix

Which techniques CEX already implements, and which are opportunities.

| Technique | CEX Status | Where in CEX |
|-----------|-----------|--------------|
| Few-Shot | ACTIVE | `prompt_template` vars + `bld_examples_*.md` ISOs |
| Role Prompting | ACTIVE | `system_prompt` + `bld_system_prompt_*.md` per builder |
| Chain-of-Thought | ACTIVE | `reasoning_trace` kind + 8F pipeline (F4 REASON) |
| Self-Refine | ACTIVE | 8F F7 GOVERN retry loop (max 2 retries) |
| Self-Consistency | PARTIAL | `cex_evolve.py` heuristic vs agent mode comparison |
| Decomposition (DECOMP) | ACTIVE | `cex_mission.py` goal decomposition + wave planning |
| Tree-of-Thought | PARTIAL | Multi-nucleus parallel dispatch (grid) approximates ToT |
| RAG | ACTIVE | `cex_retriever.py` TF-IDF + `rag_source` kind |
| ReAct | ACTIVE | Every nucleus does think -> act -> observe via 8F |
| Prompt Optimization | ACTIVE | `cex_prompt_optimizer.py` + `prompt_compiler` kind |
| Self-Calibration | PARTIAL | `quality: null` + peer scoring (never self-score) |
| Ensembling | OPPORTUNITY | Multi-model grid could vote on artifact quality |
| Step-Back | OPPORTUNITY | Could add abstraction step before F4 REASON |
| Emotion Prompting | NOT USED | Not applicable to technical artifact generation |
| Memory-of-Thought | ACTIVE | `.cex/learning_records/` + `cex_memory_select.py` |
| Reflexion | ACTIVE | `cex_evolve.py` keeps/discards based on quality delta |

---

## Sources

- Schulhoff, S. et al. (2024). "The Prompt Report: A Systematic Survey of Prompting Techniques." arXiv:2406.06608. https://arxiv.org/abs/2406.06608
- Sahoo, P. et al. (2024). "A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications." arXiv:2402.07927. https://arxiv.org/abs/2402.07927
- Liu, Y. et al. (2026). "A Comprehensive Taxonomy of Prompt Engineering Techniques for Large Language Models." Frontiers of Computer Science, Springer. https://link.springer.com/article/10.1007/s11704-025-50058-z
