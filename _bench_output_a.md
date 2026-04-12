---
id: bench_a
kind: knowledge_card
title: Prompt Caching
version: 1.0.0
quality: null
---

# Prompt Caching Strategies

**What is prompt caching?**  
A technique to store and reuse previously computed responses to identical or similar prompts, reducing redundant computation and improving efficiency.

## 3 Strategies

### 1. **TTL (Time-to-Live)**  
Evicts cached entries after a fixed duration.  
- **Eviction**: Based on time  
- **Memory Usage**: Low  
- **Dynamic Data**: Best for static data  
- **Use Case**: APIs with predictable request patterns  

### 2. **LRU (Least Recently Used)**  
Evicts the least recently accessed items.  
- **Eviction**: Based on usage frequency  
- **Memory Usage**: Moderate  
- **Dynamic Data**: Suitable for mixed workloads  
- **Use Case**: Systems with varying request patterns  

### 3. **Semantic**  
Evicts based on content similarity (e.g., vector similarity).  
- **Eviction**: Based on semantic relevance  
- **Memory Usage**: High  
- **Dynamic Data**: Ideal for dynamic data  
- **Use Case**: NLP tasks with semantically similar queries  

## Comparison Table

| Strategy | Eviction Method | Memory Usage | Dynamic Data | Use Case                     |
|---------|------------------|--------------|--------------|------------------------------|
| TTL     | Time-based       | Low          | ❌           | Static data                  |
| LRU     | Usage-based      | Moderate     | ✅           | Mixed workloads              |
| Semantic| Semantic-based   | High         | ✅           | Dynamic, semantically rich   |
