---
id: agent_customer_support_triage
kind: agent
title: "Customer Support Triage Agent with RAG Knowledge Retrieval"
version: 1.0.0
quality: 8.0
tags:
  - customer-support
  - triage
  - rag
  - escalation
  - multi-language
  - agent
tldr: >
  Autonomous customer support triage agent that classifies incoming tickets by
  urgency and domain, retrieves relevant knowledge via RAG, drafts responses in
  the customer's language, and escalates to human agents when confidence or
  policy thresholds are not met.
density_score: 1.0
updated: "2026-04-22"
---

# Customer Support Triage Agent

## 1. System Prompt

```
You are a customer support triage agent. Your job is to handle incoming
support requests by classifying them, retrieving relevant knowledge from the
company knowledge base, drafting accurate responses, and escalating to human
agents when necessary.

Core behaviors:
- ALWAYS respond in the language the customer used.
- NEVER fabricate product information. If the knowledge base does not contain
  an answer, say so and escalate.
- NEVER promise refunds, credits, or policy exceptions without explicit
  authorization from the escalation path.
- Classify every ticket before responding. Classification drives routing.
- When confidence in your answer is below 70%, escalate rather than guess.
- Preserve the full conversation context for any handoff to a human agent.
- Be empathetic but concise. Customers want solutions, not filler.

You have access to the following tools: knowledge_search, ticket_classify,
escalate_to_human, translate_text, sentiment_analyze, ticket_update,
csat_survey_send.

For every incoming message:
1. Detect language.
2. Run sentiment analysis.
3. Classify the ticket (category + urgency + complexity).
4. Search the knowledge base for relevant articles.
5. If a confident answer exists (>= 70% relevance score), draft a response.
6. If not, escalate with full context.
7. Log the interaction and update the ticket.
```

## 2. Capabilities and Tools

### 2.1 Tool Inventory

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `knowledge_search` | Vector similarity search over the company knowledge base | query string, top_k, language filter | Ranked list of articles with relevance scores |
| `ticket_classify` | ML classifier for ticket category, urgency, complexity | ticket text, metadata (account tier, product) | `{category, urgency, complexity, confidence}` |
| `escalate_to_human` | Route ticket to the appropriate human queue | ticket_id, reason, priority, suggested_team | Confirmation with queue position and ETA |
| `translate_text` | Translate between supported languages | text, source_lang, target_lang | Translated text |
| `sentiment_analyze` | Detect customer sentiment and frustration level | text | `{sentiment, frustration_score, flags}` |
| `ticket_update` | Write metadata and internal notes to the ticket | ticket_id, fields dict | Updated ticket |
| `csat_survey_send` | Trigger a satisfaction survey after resolution | ticket_id, channel, delay_minutes | Survey scheduled confirmation |

### 2.2 Capability Matrix

| Capability | Description | Autonomous? |
|------------|-------------|-------------|
| Ticket classification | Assign category, urgency (P1-P4), and complexity (low/med/high) | Yes |
| Knowledge retrieval | Search vector store, rank results, synthesize answer | Yes |
| Response drafting | Compose reply in customer's language using retrieved knowledge | Yes |
| Sentiment monitoring | Flag frustrated or at-risk customers for priority handling | Yes |
| Refund/credit processing | Issue monetary compensation | No -- requires human approval |
| Account modification | Change subscription, delete data, transfer ownership | No -- requires human approval |
| Bug confirmation | Confirm a product bug exists and file an engineering ticket | No -- requires human review |
| Policy exception | Grant any deviation from standard policy | No -- requires manager approval |

### 2.3 Knowledge Base Schema

The RAG knowledge base is organized into the following document types:

| Document Type | Example | Typical Count |
|---------------|---------|---------------|
| FAQ | "How do I reset my password?" | 200-500 |
| Troubleshooting guide | "Error 403 when uploading files" | 100-300 |
| Product documentation | Feature reference, API docs | 500-2000 |
| Policy document | Refund policy, SLA terms, privacy policy | 20-50 |
| Internal runbook | Escalation procedures, known issues | 50-100 |
| Release notes | Changelog entries per version | 50-200 |

Each document is chunked (512 tokens, 128-token overlap), embedded using a
multilingual embedding model (e.g., `multilingual-e5-large` or
`cohere-embed-multilingual-v3`), and stored in a vector database with metadata
filters for language, product area, and document type.

## 3. Escalation Rules

### 3.1 Escalation Triggers

Escalation is mandatory when ANY of the following conditions is true:

| # | Trigger | Priority | Target Queue |
|---|---------|----------|--------------|
| E1 | RAG confidence score < 0.70 on all retrieved documents | P3 | General Support |
| E2 | Customer requests refund, credit, or billing adjustment | P2 | Billing Team |
| E3 | Customer mentions legal action, lawsuit, or regulatory complaint | P1 | Legal + Manager |
| E4 | Sentiment frustration score > 0.85 | P2 | Senior Agent |
| E5 | Customer is on Enterprise/VIP tier and has any unresolved issue | P2 | Enterprise Success |
| E6 | Ticket involves account security (compromise, unauthorized access) | P1 | Security Team |
| E7 | Customer has sent 3+ messages without resolution in current session | P2 | Senior Agent |
| E8 | Ticket involves data deletion or GDPR/privacy request | P1 | Privacy + Legal |
| E9 | Product bug confirmed or strongly suspected | P2 | Engineering Triage |
| E10 | Agent cannot determine category after 2 classification attempts | P3 | General Support |

### 3.2 Priority Definitions

| Priority | Response SLA | Description |
|----------|-------------|-------------|
| P1 - Critical | 15 minutes | Security, legal, data breach, system outage |
| P2 - High | 1 hour | Billing, frustrated VIP, confirmed bug, repeated failure |
| P3 - Medium | 4 hours | Low-confidence answers, general complexity |
| P4 - Low | 24 hours | Feature requests, general inquiries, feedback |

### 3.3 Escalation Handoff Format

When escalating, the agent produces a structured handoff:

```yaml
escalation:
  ticket_id: "SUP-20260422-1847"
  trigger: "E2 - Customer requests refund"
  priority: P2
  target_queue: "Billing Team"
  customer:
    name: "A. Smith"
    account_tier: "Professional"
    language: "de"
    sentiment: "frustrated"
    frustration_score: 0.72
  context:
    summary: >
      Customer purchased annual plan 3 days ago. Wants full refund
      because feature X (advertised on landing page) does not work
      as expected. Feature X functions correctly per documentation
      but customer's use case requires integration Y which is not
      supported.
    messages_exchanged: 4
    knowledge_articles_consulted:
      - id: "KB-0342"
        title: "Feature X - Setup Guide"
        relevance: 0.82
      - id: "KB-0891"
        title: "Refund Policy"
        relevance: 0.91
    attempted_resolution: >
      Offered workaround using API endpoint /v2/export. Customer
      declined -- workaround does not meet their throughput requirements.
  recommended_action: >
    Refund is within 7-day policy window. Recommend processing full
    refund and offering 1-month free trial of Enterprise tier where
    integration Y is available.
```

### 3.4 Escalation Anti-Patterns

The agent must NOT:

1. **Escalate silently** -- always tell the customer they are being connected
   to a specialist and provide an ETA.
2. **Escalate without context** -- the handoff must include the full summary
   so the human agent never asks the customer to repeat themselves.
3. **Escalate for questions it can answer** -- if the knowledge base has a
   relevant article with score >= 0.70, answer first. Escalate only if the
   customer is unsatisfied with the answer.
4. **Loop on escalation** -- if an escalation is returned to the agent (human
   agent sends it back), the agent attempts ONE more resolution. If that fails,
   it re-escalates to a manager queue, never the same queue.

## 4. Multi-Language Support

### 4.1 Architecture

```
Customer message (any language)
    |
    v
Language Detection (fastText lid.176 or equivalent)
    |
    +---> detected_language (ISO 639-1 code)
    |
    v
Knowledge Search
    |
    +---> Strategy A (preferred): search in detected_language
    |     using multilingual embeddings (same vector space)
    |
    +---> Strategy B (fallback): if <3 results in detected_language,
    |     search in English, then translate top results
    |
    v
Response Generation
    |
    +---> Generate response in detected_language
    |     (LLM native generation, NOT post-translation)
    |
    v
Quality Check
    |
    +---> If detected_language is a Tier 2/3 language,
          run back-translation verification before sending
```

### 4.2 Language Tiers

| Tier | Languages | Support Level | Knowledge Base Coverage |
|------|-----------|--------------|----------------------|
| Tier 1 (native) | English, Spanish, Portuguese, French, German, Japanese | Full autonomous support. Native KB articles exist. Response generated directly. | 95%+ of articles available |
| Tier 2 (supported) | Italian, Dutch, Korean, Chinese (Simplified), Arabic | Autonomous with fallback. KB may be English-only; cross-lingual retrieval + native generation. | 50-80% of articles translated |
| Tier 3 (best-effort) | All other languages detectable by the model | Best-effort. English KB search, translate results, generate in target language. Back-translation QA mandatory. | English-only, translated on the fly |

### 4.3 Multi-Language Constraints

1. **Language lock**: once the agent detects the customer's language, ALL
   subsequent messages in that conversation use the same language unless the
   customer switches.
2. **No mixing**: never mix languages in a single response. Internal tool
   calls and logs are in English; customer-facing text is in their language.
3. **Cultural adaptation**: for Tier 1 languages, adapt formality level
   (e.g., Portuguese uses "voce" in Brazil but "senhor/senhora" in Portugal;
   Japanese requires keigo for business contexts).
4. **Escalation language**: the handoff to human agents is always in English
   (internal lingua franca). The human agent's reply to the customer follows
   the customer's language.
5. **Unsupported scripts**: if the language detection confidence is below
   0.60, ask the customer: "I want to help you in your preferred language.
   Could you confirm which language you'd like to use?" (asked in English +
   the best-guess language).

### 4.4 Translation Quality Safeguards

| Safeguard | When Applied | Method |
|-----------|-------------|--------|
| Back-translation check | Tier 2 and Tier 3 responses | Translate response back to English; if semantic similarity to original intent < 0.80, flag for human review |
| Terminology consistency | All tiers | Maintain a per-language glossary of product terms (e.g., "dashboard" stays "dashboard" in Portuguese, not "painel") |
| Sensitive content lock | Refund amounts, legal text, SLA terms | Always pull from pre-approved translated templates; never generate financial or legal text dynamically |
| Customer feedback loop | Post-resolution | CSAT survey includes "Was the response in your language clear?" question |

## 5. RAG Integration

### 5.1 Retrieval Pipeline

```
User query
    |
    v
Query Preprocessing
    |-- Remove PII (email, phone, account numbers)
    |-- Normalize product names (aliases -> canonical)
    |-- Detect intent category for metadata filtering
    |
    v
Hybrid Search
    |
    +---> Dense retrieval: multilingual embedding similarity (top 20)
    +---> Sparse retrieval: BM25 keyword match (top 20)
    +---> Reciprocal Rank Fusion (RRF) to merge (top 10)
    |
    v
Reranking
    |-- Cross-encoder reranker (e.g., ms-marco-multilingual)
    |-- Apply metadata boosts: +0.1 for same product area,
    |   +0.05 for recent articles (< 30 days)
    |-- Output: top 5 ranked chunks with scores
    |
    v
Context Assembly
    |-- Include parent document context (surrounding chunks)
    |-- Include document metadata (last updated, author, product area)
    |-- Total context budget: 4096 tokens max
    |
    v
Answer Generation
    |-- System prompt + conversation history + retrieved context
    |-- Generate answer with inline citations [KB-XXXX]
    |-- Confidence score = average relevance of top 3 chunks used
    |
    v
Post-Generation Validation
    |-- Hallucination check: every factual claim must trace to a chunk
    |-- Citation verification: cited KB IDs must exist in retrieved set
    |-- If validation fails: strip uncited claims, regenerate, or escalate
```

### 5.2 Retrieval Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Embedding model | `multilingual-e5-large` (1024 dims) | Best cross-lingual transfer for support content |
| Chunk size | 512 tokens | Balances granularity vs. context coherence |
| Chunk overlap | 128 tokens | Prevents information loss at boundaries |
| Dense retrieval top-k | 20 | Wide initial net before reranking |
| Sparse retrieval top-k | 20 | Catches keyword-specific matches dense misses |
| Reranked top-k | 5 | Keeps context window manageable |
| Context budget | 4096 tokens | Leaves room for system prompt + conversation history |
| Relevance threshold | 0.70 | Below this, escalate rather than answer |
| Index refresh | Every 6 hours | Balance freshness vs. indexing cost |
| Stale document threshold | 90 days | Flag articles not updated in 90 days for review |

### 5.3 Knowledge Base Maintenance

| Process | Frequency | Owner |
|---------|-----------|-------|
| New article ingestion | Real-time (webhook on CMS publish) | Automated pipeline |
| Embedding reindex | Daily (full) + real-time (incremental) | Automated pipeline |
| Stale article review | Weekly | Knowledge team |
| Low-retrieval audit | Monthly -- articles never retrieved in 30 days | Knowledge team |
| Hallucination log review | Weekly -- all cases where validation caught uncited claims | QA team |
| Relevance score calibration | Quarterly -- compare agent confidence vs. CSAT outcomes | ML team |

### 5.4 Failure Modes and Mitigations

| Failure Mode | Detection | Mitigation |
|-------------|-----------|------------|
| Vector DB unavailable | Health check timeout > 2s | Fall back to BM25-only search against cached index |
| No relevant results (all scores < 0.40) | Score check | Acknowledge gap, escalate, log the query for KB gap analysis |
| Contradictory articles retrieved | Top 2 articles give opposing answers | Escalate with both articles cited; flag for knowledge team review |
| Stale information | Article `last_updated` > 90 days and product version has changed | Warn customer that information may be outdated; escalate if critical |
| Embedding model degradation | Weekly A/B test against golden set of 100 query-article pairs | Alert ML team; roll back to previous model version |

## 6. Conversation Flow

```
START
  |
  v
Receive message
  |
  +---> Detect language --> store as session.language
  +---> Analyze sentiment --> store as session.sentiment
  +---> Classify ticket --> store as session.category, .urgency, .complexity
  |
  v
Check escalation triggers (E1-E10)
  |
  +--[trigger hit]--> Escalate with full context --> END (human takes over)
  |
  +--[no trigger]--> Continue
  |
  v
Search knowledge base (hybrid retrieval)
  |
  v
Evaluate top results
  |
  +--[best score >= 0.70]--> Draft response with citations
  |                          |
  |                          v
  |                    Send response in session.language
  |                          |
  |                          v
  |                    Ask: "Did this resolve your issue?"
  |                          |
  |                    +--[yes]--> Close ticket, send CSAT survey --> END
  |                    +--[no]---> Increment attempt counter
  |                                |
  |                                +--[attempts >= 3]--> Escalate (E7)
  |                                +--[attempts < 3]---> Loop to "Receive message"
  |
  +--[best score < 0.70]--> Escalate (E1) with retrieved context --> END
```

## 7. Observability and Metrics

### 7.1 Key Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| First-response time | < 30 seconds | Timestamp delta: message received to response sent |
| Autonomous resolution rate | > 60% | Tickets resolved without human escalation / total tickets |
| Escalation accuracy | > 90% | Escalations where human agrees with triage category / total escalations |
| RAG retrieval relevance | > 0.75 avg | Mean top-3 relevance score across all queries |
| Customer satisfaction (CSAT) | > 4.2 / 5.0 | Post-resolution survey scores |
| Language detection accuracy | > 98% | Spot-check sample vs. human annotation |
| Hallucination rate | < 1% | Responses with uncited factual claims / total responses |
| Mean time to escalation | < 2 minutes | For tickets that need human help, how fast do we route them |

### 7.2 Logging Schema

Every interaction produces a structured log entry:

```json
{
  "ticket_id": "SUP-20260422-1847",
  "timestamp": "2026-04-22T18:47:32Z",
  "language": "de",
  "sentiment": "neutral",
  "frustration_score": 0.31,
  "category": "billing",
  "urgency": "P3",
  "complexity": "medium",
  "rag_query": "Rechnung herunterladen monatlich",
  "rag_results": [
    {"id": "KB-0221", "score": 0.87, "used_in_response": true},
    {"id": "KB-0445", "score": 0.74, "used_in_response": false}
  ],
  "response_confidence": 0.87,
  "escalated": false,
  "resolution": "autonomous",
  "csat_score": 4,
  "tokens_used": 1842
}
```

## 8. Security and Privacy

| Concern | Control |
|---------|---------|
| PII in queries | Strip email, phone, SSN before embedding search. Store raw query in encrypted ticket log only. |
| Customer data in RAG context | Knowledge base contains NO customer-specific data. Only product docs and policies. |
| Access control | Agent cannot access customer account details without explicit tool call with audit log. |
| Data retention | Conversation logs retained 90 days for QA, then anonymized. GDPR deletion requests honored within 72 hours. |
| Prompt injection | Input sanitization layer before classification. System prompt includes injection resistance instructions. |
| Model output filtering | Post-generation filter blocks: competitor recommendations, internal-only URLs, employee names. |
