"""Tests for brand_ingest.py -- messy file ingestion into brand signals."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from brand_ingest import (extract_signals_from_text, format_for_llm, ingest,
                          merge_signals, scan_folder)


class TestScanFolder:
    def test_categorizes_files(self, tmp_path):
        (tmp_path / "readme.md").write_text("# Brand", encoding="utf-8")
        (tmp_path / "style.css").write_text("body { color: #333; }", encoding="utf-8")
        (tmp_path / "logo.png").write_bytes(b"\x89PNG\r\n")

        inv = scan_folder(tmp_path)
        assert inv["total_files"] == 3
        assert len(inv["text"]) == 1
        assert len(inv["web"]) == 1
        assert len(inv["images"]) == 1

    def test_empty_folder(self, tmp_path):
        inv = scan_folder(tmp_path)
        assert inv["total_files"] == 0

    def test_nested_folders(self, tmp_path):
        (tmp_path / "sub").mkdir()
        (tmp_path / "sub" / "notes.txt").write_text("brand notes", encoding="utf-8")
        inv = scan_folder(tmp_path)
        assert inv["total_files"] == 1


class TestExtractSignals:
    def test_finds_hex_colors(self):
        text = "Primary color: #FF5733, secondary: #1A1A2E, accent: #50C878"
        sig = extract_signals_from_text(text)
        assert "#FF5733" in sig["colors_hex"]
        assert "#1A1A2E" in sig["colors_hex"]
        assert len(sig["colors_hex"]) == 3

    def test_finds_fonts(self):
        text = "font-family: 'Inter', sans-serif; font: 'Geist'"
        sig = extract_signals_from_text(text)
        assert any("Inter" in f for f in sig["fonts"])

    def test_finds_urls(self):
        text = "Visit https://codexa.dev and https://github.com/codexa"
        sig = extract_signals_from_text(text)
        assert len(sig["urls"]) >= 2

    def test_finds_prices_brl(self):
        text = "Plano Pro: R$ 97/mes. Plano Enterprise: R$ 297/mes."
        sig = extract_signals_from_text(text)
        assert len(sig["prices_brl"]) == 2

    def test_detects_portuguese(self):
        text = "Nossa empresa cria produtos para clientes que valorizam qualidade e preco justo."
        sig = extract_signals_from_text(text)
        assert sig["likely_language"] == "pt-BR"

    def test_detects_english(self):
        text = "Our company creates products for customers who value quality and fair pricing."
        sig = extract_signals_from_text(text)
        assert sig["likely_language"] == "en-US"

    def test_finds_potential_names(self):
        text = "Codexa is an AI platform. Codexa builds agents. Use Codexa today."
        sig = extract_signals_from_text(text)
        assert "Codexa" in sig["potential_names"]

    def test_finds_social_handles(self):
        text = "Follow us @codexa_ai on Twitter and @codexa on Instagram"
        sig = extract_signals_from_text(text)
        assert len(sig["social_handles"]) >= 2

    def test_finds_mission(self):
        text = "Missao: Democratizar o acesso a inteligencia artificial para pequenas empresas."
        sig = extract_signals_from_text(text)
        assert "potential_mission" in sig
        assert "Democratizar" in sig["potential_mission"]

    def test_empty_text(self):
        sig = extract_signals_from_text("")
        assert sig["colors_hex"] == []
        assert sig["potential_names"] == []


class TestMergeSignals:
    def test_merges_multiple_sources(self):
        s1 = {"colors_hex": ["#FF0000"], "fonts": ["Inter"], "potential_names": ["Acme"],
               "colors_rgb": [], "urls": [], "emails": [], "social_handles": [],
               "prices_brl": [], "prices_usd": [], "potential_values": [],
               "likely_language": "pt-BR"}
        s2 = {"colors_hex": ["#00FF00", "#FF0000"], "fonts": ["Geist"], "potential_names": ["Acme", "Acme"],
               "colors_rgb": [], "urls": [], "emails": [], "social_handles": [],
               "prices_brl": [], "prices_usd": [], "potential_values": [],
               "likely_language": "pt-BR"}

        merged = merge_signals([s1, s2])
        assert "Acme" in merged["potential_names"]
        assert merged["potential_names"][0] == "Acme"  # most frequent first
        assert "#FF0000" in merged["colors_hex"]
        assert "#00FF00" in merged["colors_hex"]


class TestIngest:
    def test_full_ingest(self, tmp_path):
        (tmp_path / "brand.md").write_text(
            "# Codexa Brand\nMissao: Construir agentes AI.\nColors: #50C878 #1A1A2E\n"
            "font-family: 'Inter'\nR$ 97/mes",
            encoding="utf-8",
        )
        (tmp_path / "style.css").write_text(
            "body { color: #E0E0E0; background: #0A0A0A; font-family: 'Geist'; }",
            encoding="utf-8",
        )

        signals = ingest(tmp_path)
        assert signals["inventory"]["total_files"] == 2
        assert len(signals["colors_hex"]) >= 2
        assert signals.get("likely_language") in ("pt-BR", "en-US")  # CSS can skew


class TestFormatForLlm:
    def test_produces_readable_output(self, tmp_path):
        (tmp_path / "info.txt").write_text(
            "Codexa - Build AI Agents\nMissao: simplificar AI\n#50C878",
            encoding="utf-8",
        )
        signals = ingest(tmp_path)
        output = format_for_llm(signals)

        assert "Brand Signals" in output
        assert "Source" in output
        assert isinstance(output, str)
        assert len(output) > 100
