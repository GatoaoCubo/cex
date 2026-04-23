"""Tests for cex_query.py -- builder discovery by keyword."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_query import normalize, score_builder, stem, tokenize


class TestNormalize:
    def test_lowercase(self):
        assert normalize("Hello World") == "hello world"

    def test_strips_punctuation(self):
        r = normalize("hello, world!")
        assert "," not in r
        assert "!" not in r

    def test_empty(self):
        assert normalize("") == ""


class TestStem:
    def test_removes_suffix(self):
        s = stem("testing")
        assert len(s) <= len("testing")

    def test_short_word(self):
        assert stem("ai") == "ai"


class TestTokenize:
    def test_splits_words(self):
        tokens = tokenize("create a knowledge card")
        assert "knowledge" in tokens or "knowledg" in tokens
        assert len(tokens) >= 2  # stopwords removed

    def test_removes_stopwords(self):
        tokens = tokenize("a the an is are")
        # most should be filtered
        assert len(tokens) <= 2

    def test_empty(self):
        assert tokenize("") == []


class TestScoreBuilder:
    def test_matching_keywords(self):
        builder = {
            "id": "test-builder",
            "kind": "knowledge_card",
            "domain": "testing",
            "keywords": "knowledge card research",
            "triggers": "create knowledge",
        }
        tokens = tokenize("create a knowledge card")
        idf = {t: 1.0 for t in tokens}
        result = score_builder(builder, tokens, idf)
        # score_builder may return float or tuple (score, details)
        score = result[0] if isinstance(result, tuple) else result
        assert score > 0

    def test_no_match(self):
        builder = {
            "id": "test-builder",
            "kind": "workflow",
            "domain": "devops",
            "keywords": "workflow pipeline deploy",
            "triggers": "create workflow",
        }
        tokens = tokenize("quantum physics simulation")
        idf = {t: 1.0 for t in tokens}
        result = score_builder(builder, tokens, idf)
        score = result[0] if isinstance(result, tuple) else result
        assert score == 0 or score < 0.1

    def test_empty_tokens(self):
        builder = {"id": "x", "kind": "y", "domain": "z", "keywords": "a b", "triggers": "c"}
        result = score_builder(builder, [], {})
        score = result[0] if isinstance(result, tuple) else result
        assert score == 0
