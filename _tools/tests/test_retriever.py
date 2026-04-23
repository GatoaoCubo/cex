"""Tests for cex_retriever.py -- TF-IDF semantic search over CEX artifacts."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_retriever import (build_tfidf, cosine_similarity,
                           find_examples_for_kind, find_similar, load_index,
                           scan_artifacts, strip_frontmatter, tokenize)

CEX_ROOT = Path(__file__).resolve().parent.parent.parent


# =============================================================================
# Tokenization
# =============================================================================

class TestTokenize:
    @pytest.mark.unit
    def test_basic_tokenization(self):
        tokens = tokenize("Hello world, this is a test document")
        assert "hello" in tokens
        assert "world" in tokens
        assert "test" in tokens
        assert "document" in tokens

    @pytest.mark.unit
    def test_stopword_removal(self):
        tokens = tokenize("this is a the and or but i")
        assert len(tokens) == 0

    @pytest.mark.unit
    def test_min_length(self):
        tokens = tokenize("ab cd ef longer_word ok")
        assert "longer_word" in tokens
        assert "ab" not in tokens
        assert "cd" not in tokens

    @pytest.mark.unit
    def test_underscore_words(self):
        tokens = tokenize("knowledge_card chunk_strategy agent_builder")
        assert "knowledge_card" in tokens
        assert "chunk_strategy" in tokens


class TestStripFrontmatter:
    @pytest.mark.unit
    def test_strips_yaml(self):
        text = "---\nid: test\nkind: agent\n---\n# Body"
        assert strip_frontmatter(text) == "# Body"

    @pytest.mark.unit
    def test_no_frontmatter(self):
        text = "Just plain text"
        assert strip_frontmatter(text) == text


# =============================================================================
# TF-IDF
# =============================================================================

class TestTfIdf:
    @pytest.mark.unit
    def test_empty_corpus(self):
        vocab, vectors = build_tfidf([])
        assert vocab == {}
        assert vectors == []

    @pytest.mark.unit
    def test_single_doc(self):
        vocab, _vectors = build_tfidf([["hello", "world"]])
        # Single doc: no word appears in 2+ docs, so vocab is empty
        assert len(vocab) == 0

    @pytest.mark.unit
    def test_two_docs_shared_term(self):
        corpus = [
            ["agent", "builder", "construct"],
            ["agent", "validator", "check"],
            ["retriever", "search", "query"],
        ]
        vocab, vectors = build_tfidf(corpus)
        assert "agent" in vocab  # appears in 2/3 docs
        assert len(vectors) == 3

    @pytest.mark.unit
    def test_vectors_are_sparse(self):
        corpus = [
            ["alpha", "beta", "gamma"],
            ["alpha", "delta", "epsilon"],
            ["alpha", "beta", "zeta"],
        ]
        _vocab, vectors = build_tfidf(corpus)
        for vec in vectors:
            assert isinstance(vec, dict)
            assert all(isinstance(v, float) for v in vec.values())


class TestCosineSimilarity:
    @pytest.mark.unit
    def test_identical_vectors(self):
        v = {"a": 1.0, "b": 2.0}
        assert cosine_similarity(v, v) == pytest.approx(1.0)

    @pytest.mark.unit
    def test_orthogonal_vectors(self):
        v1 = {"a": 1.0}
        v2 = {"b": 1.0}
        assert cosine_similarity(v1, v2) == 0.0

    @pytest.mark.unit
    def test_empty_vector(self):
        assert cosine_similarity({}, {"a": 1.0}) == 0.0

    @pytest.mark.unit
    def test_partial_overlap(self):
        v1 = {"a": 1.0, "b": 1.0}
        v2 = {"a": 1.0, "c": 1.0}
        sim = cosine_similarity(v1, v2)
        assert 0 < sim < 1


# =============================================================================
# Scanning
# =============================================================================

class TestScanArtifacts:
    @pytest.mark.unit
    def test_scan_finds_artifacts(self):
        artifacts = scan_artifacts(CEX_ROOT)
        assert len(artifacts) > 100
        # All have required fields
        for a in artifacts[:10]:
            assert "path" in a
            assert "kind" in a
            assert "tokens" in a

    @pytest.mark.unit
    def test_scan_skips_compiled(self):
        artifacts = scan_artifacts(CEX_ROOT)
        for a in artifacts:
            assert "compiled/" not in a["path"]


# =============================================================================
# Index Build & Load
# =============================================================================

class TestIndex:
    @pytest.mark.unit
    def test_load_index_exists(self):
        index = load_index()
        # Index may or may not exist; test both paths
        if index:
            assert "docs" in index
            assert "vocab" in index
            assert "vectors" in index
            assert index["n_docs"] > 0


# =============================================================================
# Search
# =============================================================================

class TestSearch:
    @pytest.fixture(autouse=True)
    def _load_idx(self):
        self.index = load_index()
        if not self.index:
            pytest.skip("No retriever index built")

    @pytest.mark.unit
    def test_find_similar_basic(self):
        results = find_similar("RAG chunking strategy", index=self.index, top_k=5)
        assert len(results) > 0
        assert results[0]["score"] > 0

    @pytest.mark.unit
    def test_find_similar_with_kind_filter(self):
        results = find_similar("agent builder", index=self.index, kind="agent", top_k=5)
        for r in results:
            assert r["kind"] == "agent"

    @pytest.mark.unit
    def test_find_similar_result_structure(self):
        results = find_similar("knowledge card", index=self.index, top_k=1)
        if results:
            r = results[0]
            assert "path" in r
            assert "id" in r
            assert "kind" in r
            assert "score" in r
            assert isinstance(r["score"], float)

    @pytest.mark.unit
    def test_find_examples_for_kind(self):
        results = find_examples_for_kind("agent", "create a validation agent", index=self.index)
        assert len(results) > 0
        # Same-kind should be boosted
        if results[0]["kind"] == "agent":
            assert results[0]["score"] > 0

    @pytest.mark.unit
    def test_empty_query(self):
        results = find_similar("", index=self.index)
        assert results == []
