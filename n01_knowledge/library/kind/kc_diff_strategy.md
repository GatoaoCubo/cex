---
id: kc_diff_strategy
kind: knowledge_card
title: Diff Strategy
version: 1.0.0
quality: null
pillar: P01
---

# Diff Strategy

## Purpose
This knowledge card defines the methodology for applying changes to knowledge artifacts using a matching algorithm that prioritizes semantic relevance over superficial similarity.

## Key Concepts
1. **Change Vector**: Quantifies the magnitude and direction of modifications
2. **Semantic Matching**: Uses contextual understanding rather than literal text comparison
3. **Priority Queue**: Orders changes by impact potential and contextual relevance

## Change Application
1. **Preprocessing**:
   - Normalize text (lowercase, remove punctuation)
   - Tokenize using contextual embeddings
   - Identify semantic clusters

2. **Matching Algorithm**:
   ```python
   def calculate_similarity(change, artifact):
       # Calculate cosine similarity between change vector and artifact vector
       return cosine_similarity(change_vector, artifact_vector)
   ```

3. **Application Rules**:
   - Apply changes with >0.85 similarity first
   - Flag potential conflicts for manual review
   - Maintain version history for all modifications

## Best Practices
- Use weighted scoring for different change types
- Implement fallback mechanisms for ambiguous matches
- Regularly update reference corpora for better accuracy
- Monitor and refine the matching algorithm continuously
