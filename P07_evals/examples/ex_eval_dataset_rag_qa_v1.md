---
id: p07_dataset_rag_qa_v1
kind: eval_dataset
pillar: P07
name: "RAG QA Dataset v1"
description: "500-sample evaluation dataset for RAG question-answering over organization knowledge base"
size: 500
splits:
  train: 400
  test: 100
schema:
  question: "string — natural language query"
  answer: "string — ground truth answer"
  context: "string — relevant retrieved passage"
  source: "string — KC/pool artifact ID"
version: 1.0.0
created: 2026-03-29
author: builder_agent
quality: 9.0
tags: [eval-dataset, rag, qa, knowledge-base, ground-truth]
---

# Eval Dataset: RAG QA v1

## Purpose

Ground-truth dataset for evaluating organization's RAG pipeline (brain_query -> context retrieval -> answer generation). 500 human-verified question-answer pairs drawn from real knowledge cards, pool artifacts, and agent_group documentation.

## Dataset Schema

```yaml
# Each record follows this structure:
- question: "What embedding model does organization use for vector search?"
  answer: "nomic-embed-text via Ollama, producing 768-dim vectors at ~10ms/query locally"
  context: "KC_EMBED_001: organization uses nomic-embed-text through Ollama for local embedding generation. Dimensions: 768. Latency: ~10ms per query."
  source: "p01_kc_embedding_config_nomic"
  difficulty: "easy"        # easy | medium | hard
  category: "infrastructure" # infrastructure | agent | workflow | config | marketing
```

## Split Strategy

| Split | Size | Purpose | Selection Criteria |
|-------|------|---------|-------------------|
| Train | 400 | Few-shot calibration, prompt tuning | Stratified by category + difficulty |
| Test | 100 | Final evaluation, regression checks | Held out, never seen during tuning |

### Difficulty Distribution

| Difficulty | Train | Test | Total | Description |
|------------|-------|------|-------|-------------|
| Easy | 200 | 50 | 250 | Single-hop, answer in one KC |
| Medium | 140 | 35 | 175 | Multi-hop, 2-3 KCs needed |
| Hard | 60 | 15 | 75 | Reasoning required, implicit info |

### Category Distribution

| Category | Count | Example Question |
|----------|-------|-----------------|
| Infrastructure | 120 | "How does BM25 fallback work when Ollama is down?" |
| Agent | 110 | "Which agent handles marketplace scraping?" |
| Workflow | 100 | "What is the spawn_grid continuous batching flow?" |
| Config | 90 | "What are the Firecrawl rate limits per research?" |
| Marketing | 80 | "How does marketing_agent generate Instagram carousel copy?" |

## Sample Records

### Easy — Single-hop retrieval
```yaml
question: "What is the maximum number of agent_groups orchestrator can spawn simultaneously?"
answer: "3 agent_groups plus orchestrator itself (4 total). More than 4 causes BSOD due to RAM limits."
context: "MEMORY: Max terminals = 3 sats + orchestrator. BSOD if >4. Power-save features disabled to prevent crashes."
source: "memory_bsod_prevention"
difficulty: "easy"
category: "infrastructure"
```

### Medium — Multi-hop
```yaml
question: "How should a new agent be registered so brain_query can find it?"
answer: "Create README.md + iso_vectorstore/ (MANIFEST, INSTRUCTIONS, EXAMPLES minimum), register in AGENT_ROUTING_INDEX.md, then rebuild FAISS index with build_indexes_ollama.py --scope all (~20 min)."
context: "KC_AGENT_AUTH: Structure requires README.md + iso_vectorstore/. CLAUDE.md: Register in AGENT_ROUTING_INDEX.md. Brain rebuild: build_indexes_ollama.py --scope all (~20 min)."
source: "agents_context_rule + claude_md"
difficulty: "medium"
category: "agent"
```

### Hard — Requires reasoning
```yaml
question: "If Firecrawl credits drop below 20%, which marketplace enrichments should be cut first and why?"
answer: "Cut magalu/americanas/casas_bahia/shein first (1 credit each, lower data quality) before shopee (3 credits, high value) and amazon (3 credits, high value). Conservation mode activates automatically at <20%."
context: "KC_FIRECRAWL: Conservation mode at <20% credits. Shopee=3 credits, amazon=3 credits, magalu/americanas/casas_bahia/shein=1 each. Budget: 3000/month, 10/research."
source: "memory_firecrawl_config"
difficulty: "hard"
category: "config"
```

## Quality Assurance

| Check | Method | Threshold |
|-------|--------|-----------|
| Answer accuracy | Human verification (2 reviewers) | 100% of test split |
| Context sufficiency | Answer derivable from context alone | >= 95% |
| No label leakage | Test answers not in train contexts | 0 leaks |
| Source validity | All source IDs resolve to real artifacts | 100% |
| Freshness | Answers match current system state | Quarterly re-validation |

## Usage

```python
import yaml

with open("datasets/rag_qa_v1.yaml") as f:
    dataset = yaml.safe_load(f)

train = [r for r in dataset if r["split"] == "train"]
test = [r for r in dataset if r["split"] == "test"]

# Evaluate RAG pipeline
for record in test:
    generated = rag_pipeline(record["question"])
    score = llm_judge(
        question=record["question"],
        context=record["context"],
        answer=generated,
        ground_truth=record["answer"]
    )
```

## Versioning

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-29 | Initial 500 samples, 5 categories |
| _planned_ 1.1.0 | 2026-Q2 | Add 200 Portuguese-language queries |
| _planned_ 2.0.0 | 2026-Q3 | Multi-turn conversation pairs |

## Anti-Patterns
- Testing on train split (data leakage, inflated metrics)
- Ground truth from LLM generation without human verification
- Static dataset never refreshed (knowledge drifts, answers become stale)
- Single difficulty level only (hides performance gaps on hard queries)
