# Model Card Spec Analysis: A Comparative Review

This document provides a comparative analysis of model cards from 10 leading large language models. The goal is to identify common practices, essential fields, and a recommended format for creating comprehensive and standardized model cards.

## 1. Matriz Comparativa de Campos

| Campo Essencial | Claude 3 (Opus/Sonnet) | GPT-4o / GPT-3 | Gemini 2.5 Pro | Llama 3.1 405B | Mistral Large 2/3 | Command R+ | DeepSeek V2 | Qwen 2/2.5 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Model Name** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Developer** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Release Date** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Model Size / Parameters** | ❌ (Family Only) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Architecture** | ❌ (General) | ✅ | ✅ (MoE) | ✅ (GQA) | ✅ (Dense/MoE) | ✅ | ✅ (MoE+MLA) | ✅ (GQA) |
| **Context Window** | ✅ | ✅ (GPT-4o) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Max Output Tokens** | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ |
| **Knowledge Cutoff** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| **Input Modalities** | ✅ | ✅ | ✅ | ❌ (Text) | ✅ (Text/Image) | ❌ (Text) | ❌ (Text) | ❌ (Text) |
| **Output Modalities** | ✅ (Text) | ✅ (Text/Image) | ✅ (Text) | ✅ (Text) | ✅ (Text) | ✅ (Text) | ✅ (Text) | ✅ (Text) |
| **Training Data Info** | ✅ (High-level) | ✅ | ✅ (High-level) | ✅ | ❌ | ✅ (High-level) | ✅ | ✅ (High-level) |
| **Performance Benchmarks**| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Intended Use Cases** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (Implicit) | ✅ |
| **Limitations & Biases**| ✅ | ✅ | ✅ | ✅ (Implicit) | ❌ | ✅ | ❌ | ❌ |
| **Safety & Ethics** | ✅ | ✅ | ✅ | ✅ (Use Policy) | ❌ | ✅ | ❌ | ❌ |
| **License** | ❌ (Commercial) | ❌ (API) | ❌ (Commercial) | ✅ (Community) | ✅ (Research/Comm) | ✅ (CC-BY-NC) | ✅ (MIT/Custom) | ❌ |
| **Official URL / Paper**| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Pricing** | ✅ | ✅ (API) | ✅ | N/A (Open) | ✅ | N/A (Open) | N/A (Open) | N/A (Open) |

---

## 2. Análise de Frequência de Campos

### Campos Universais (8/10+ ocorrências)
Fields that are consistently present and form the bedrock of a model card.
- **Model Name:** Universal identifier.
- **Developer:** Clear attribution of origin.
- **Release Date:** Provides temporal context for the model's relevance and capabilities.
- **Performance Benchmarks:** Quantitative data (e.g., MMLU, GSM8K, HumanEval) is the primary way providers demonstrate competitiveness.
- **Intended Use Cases:** Defines the model's target applications (e.g., RAG, coding, chat).
- **Official URL / Paper:** A link to a primary source for deeper technical details.
- **Context Window:** A critical technical specification for users.
- **Architecture:** High-level description (e.g., Transformer, MoE) is almost always mentioned.

### Campos Frequentes (5-7/10 ocorrências)
Fields that are common but not universally adopted. Their inclusion adds significant value.
- **Model Size / Parameters:** While frequent, some providers (like Anthropic) are moving away from disclosing specific numbers, focusing instead on performance.
- **Safety & Ethics:** Detailed sections on safety testing, bias mitigation, and responsible AI principles are common but not yet universal.
- **Limitations & Bienses:** Explicitly calling out what the model *cannot* do, its potential for hallucination, and inherent biases.
- **Training Data Info:** High-level descriptions are common, but detailed breakdowns of the corpus are rare.
- **License:** Crucial for open-weight models, but less prominent for models offered exclusively via commercial APIs.
- **Max Output Tokens:** A practical parameter for developers, but not always highlighted.
- **Knowledge Cutoff:** Important for user context but sometimes omitted.

### Campos Raros (<5/10 ocorrências)
Fields that are specialized or inconsistently reported.
- **Pricing:** Only relevant for commercially hosted models.
- **Input/Output Modalities:** While increasingly important, not all models are multimodal, so this field is conditional.
- **Specific Hardware:** Details on training hardware (e.g., TPUs, GPUs) are very rare.

---

## 3. Formato Recomendado para Model Card

Based on the analysis, a comprehensive and effective model card should be structured into three main sections: **Overview**, **Technical Specifications**, and **Responsible AI**.

### **I. Overview & Vitals**
*   **Model Name:** (e.g., `Codexa-Alpha-v1`)
*   **Developer:** (e.g., `Codexa AI`)
*   **Website/Official URL:** (Link to paper, blog post, or product page)
*   **Release Date:** (e.g., `YYYY-MM-DD`)
*   **License:** (e.g., `MIT`, `Apache 2.0`, `Commercial API`)
*   **Contact:** (e.g., `research@codexa.ai`)

### **II. Technical Specifications & Performance**
*   **Architecture:** (e.g., `Dense Transformer`, `Mixture-of-Experts (MoE)`)
*   **Parameters:** (e.g., `7B`, `70B`, `1.5T Total / 45B Active`)
*   **Context Window:** (e.g., `128,000 tokens`)
*   **Knowledge Cutoff:** (e.g., `YYYY-MM`)
*   **Modalities:**
    *   **Input:** (e.g., `Text`, `Image`, `Audio`)
    *   **Output:** (e.g., `Text`, `Code`, `JSON`)
*   **Training Data:**
    *   **Corpus Summary:** (High-level description, e.g., "A diverse mix of public web data, books, and code.")
    *   **Pre-training Tokens:** (e.g., `15 Trillion tokens`)
*   **Performance Benchmarks:** (A table is highly recommended)
| Benchmark | Score | Notes |
| :--- | :--- | :--- |
| **MMLU** | `XX.X%` | 5-shot |
| **GSM8K** | `XX.X%` | 8-shot |
| **HumanEval** | `XX.X%` | 0-shot |

### **III. Responsible AI & Usage**
*   **Intended Use Cases:**
    *   **Primary:** (e.g., "Complex RAG, multi-step tool use, enterprise-grade chatbots.")
    *   **Out-of-Scope:** (e.g., "Not intended for high-stakes medical diagnosis or autonomous decision-making.")
*   **Safety & Alignment:**
    *   **Alignment Method:** (e.g., `RLHF`, `Constitutional AI`, `DPO`)
    *   **Safety Filtering:** (Description of content filters for toxicity, hate speech, etc.)
*   **Limitations & Biases:**
    *   (e.g., "The model may produce factual inaccuracies (hallucinations). It reflects biases present in its training data and may generate stereotyped responses.")
*   **Ethical Considerations:**
    *   (Statement on potential misuse, environmental impact, or other ethical factors.)

This format provides a clear, standardized, and comprehensive overview, enabling developers and stakeholders to quickly assess a model's capabilities, limitations, and responsible use guidelines.
