---
id: bench_a
kind: knowledge_card
title: Prompt Caching
version: 1.0.0
quality: null
---

**Prompt Caching** is a technique to store and reuse previously generated responses to identical or similar prompts, reducing computation time and resource usage.

### 3 Strategies
1. **TTL (Time-to-Live)**  
   - Evicts entries after a fixed duration  
   - Best for short-term, time-sensitive tasks  
   - High performance for frequent reuse  

2. **LRU (Least Recently Used)**  
   - Evicts least recently accessed items  
   - Ideal for dynamic workloads with varying access patterns  
   - Balances memory and performance  

3. **Semantic**  
   - Uses similarity metrics to identify duplicate prompts  
   - Optimal for complex, context-dependent queries  
   - Higher memory overhead but better accuracy  

| Strategy | Eviction Method | Use Case                  | Performance | Memory Usage |
|----------|------------------|---------------------------|-------------|--------------|
| TTL      | Time-based       | API rate limiting         | ⭐⭐⭐⭐      | Low          |
| LRU      | Access-based     | Web applications          | ⭐⭐⭐⭐      | Medium       |
| Semantic | Similarity-based | Research, creative tasks  | ⭐⭐⭐        | High         |
