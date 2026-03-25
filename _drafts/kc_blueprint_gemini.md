# META-TEMPLATE: PYTHA Knowledge Card (KC) Architecture
# Version: 1.0
# Satellite: PYTHA (知)
# Status: DRAFT

---

## 1. INTENTION: THE PURPOSE OF A KNOWLEDGE CARD (KC)

This document is a **Meta-Template**. It defines the universal structure and guiding principles for creating any **Knowledge Card (KC)** within the Codexa ecosystem. Its purpose is to ensure that all captured knowledge is **discoverable, interoperable, and machine-readable**.

A KC is the atomic unit of knowledge. It is a self-contained, versioned artifact that encapsulates a specific domain of expertise, a technical specification, a research finding, or a set of operational procedures.

PYTHA, as the Knowledge satellite, is the primary custodian of this architecture.

## 2. KC FILE NAMING CONVENTION

All KCs MUST adhere to the following file naming convention to enable automated discovery and indexing.

`KC_[SATELLITE]_[ID]_[DESCRIPTOR_UPPERCASE].md`

- **`KC`**: Prefix indicating this is a Knowledge Card.
- **`SATELLITE`**: The creating satellite (e.g., `PYTHA`, `SHAKA`, `EDISON`).
- **`ID`**: A zero-padded 3-digit number (e.g., `001`, `042`).
- **`DESCRIPTOR_UPPERCASE`**: A brief, descriptive title in `SCREAMING_SNAKE_CASE` (e.g., `BLING_API_AUTHENTICATION`).

**Example**: `KC_PYTHA_001_BLING_FIELD_PARAMETRIZATION.md`

## 3. KC HEADER BLOCK: THE METADATA SIGNATURE

Every KC MUST begin with a YAML-compliant header block. This is critical for machine-readability and integration with the Codexa Knowledge Architecture.

```yaml
# --- KC Header: Start ---
#
# id: KC_[SATELLITE]_[ID]
# title: "[Clear, Human-Readable Title]"
# version: "1.0.0" # Use Semantic Versioning (Major.Minor.Patch)
#
# satellite: "[SATELLITE_NAME]" # (e.g., PYTHA, SHAKA)
# domain: "[Primary Domain]" # (e.g., Knowledge Architecture, API Integration, Frontend)
#
# created_date: "YYYY-MM-DD"
# last_updated: "YYYY-MM-DD"
#
# author: "[Author/Agent Name]"
# quality_score: [0.0-10.0] # Objective score based on review/validation
# status: "[Draft | Active | Deprecated | Archived]"
#
# tags:
#   - "tag1"
#   - "tag2"
#   - "relevant_domain"
#
# dependencies: # Optional: List other KC IDs this card depends on
#   - "KC_EDISON_005_..."
#
# --- KC Header: End ---
```

## 4. UNIVERSAL KC BODY STRUCTURE

While the content will vary, the structure SHOULD follow this general schema to maintain consistency.

### 4.1. `## 1. Executive Summary`

A concise, single-paragraph summary of the KC's purpose and content. What problem does it solve? What knowledge does it contain? This section is vital for quick previews and RAG retrieval.

### 4.2. `## 2. Core Principles / Axioms`

If applicable, list the fundamental rules, laws, or principles that govern this knowledge domain. These should be immutable truths within the context of the KC.

> **Principle 1:** [Name of Principle]. [Brief explanation].
>
> **Principle 2:** [Name of Principle]. [Brief explanation].

### 4.3. `## 3. Architecture / Specification`

This is the main body of the KC. Use diagrams, code blocks, tables, and detailed descriptions to present the knowledge.

For technical KCs, this section might contain:
-   ASCII diagrams of system architecture.
-   Data schemas (JSON Schema, SQL DDL).
-   API endpoint definitions (OpenAPI snippets).
-   Sequence diagrams.

```
[Detailed content, code blocks, diagrams, and tables go here.]
```

### 4.4. `## 4. Operational Procedures / Implementation`

Provide actionable instructions, workflows, or code examples demonstrating how to use the knowledge described.

**Example: Bling API Authentication**
```python
# Step 1: Obtain API Key from Bling Dashboard
api_key = os.getenv("BLING_API_KEY")

# Step 2: Make a request to the /produtos endpoint
import requests

url = "https://bling.com.br/Api/v2/produtos/json/"
params = {"apikey": api_key}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Successfully fetched products.")
    # process_data(response.json())
else:
    print(f"Error: {response.status_code}")
```

### 4.5. `## 5. Validation & Quality Gates`

Describe the metrics and procedures used to validate this knowledge. How is the `quality_score` in the header determined?

-   **MRR@10**: [Value] for retrieval tasks.
-   **Code Coverage**: [Percentage] for code-related KCs.
-   **Manual Review Checklist**: [Link to checklist or description].

### 4.6. `## 6. Cross-References`

A list of related KCs, documents, or external resources. This builds the knowledge graph.

-   **Parent**: `[KC_ID_...]`
-   **Child**: `[KC_ID_...]`
-   **Related**: `[KC_ID_...]`, `[External URL]`

## 5. THE ROLE OF KCs IN THE CODEXA KNOWLEDGE ARCHITECTURE

KCs are the source material for the `EMBEDDING_AGENT`. PYTHA extracts and prepares KCs, which are then vectorized and stored for retrieval by the `Retriever Agent` to augment LLM context (RAG).

```
┌────────────────────┐
│   Knowledge Card   │  ◄── YOU ARE HERE (as a template)
│   (KC_*.md)        │
└──────────┬─────────┘
           │ (PYTHA: Extraction/Chunking)
           v
┌────────────────────┐
│  EMBEDDING_AGENT   │
└──────────┬─────────┘
           │ (Vectorization)
           v
┌────────────────────┐
│   Vector Index     │ (FAISS, ChromaDB)
└──────────┬─────────┘
           │ (Retrieval)
           v
┌────────────────────┐
│   LLM Context      │ (RAG)
└────────────────────┘
```

Adherence to this meta-template is **non-negotiable** for maintaining the integrity and performance of the entire knowledge system.

---
*This meta-template is managed by PYTHA. Any proposed changes must be submitted via a PR and validated against the knowledge architecture principles.*
