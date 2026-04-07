"""
CRM Lead Scoring Engine -- multi-factor scoring for GATO\u00b3 B2B pipeline.

Scores each business on 5 dimensions:
  - Business maturity (rating, reviews, online presence)
  - Geographic alignment (ring proximity to GATO\u00b3 in SCS)
  - Service alignment (cat specialty, premium positioning)
  - Contact quality (validated channels, completeness)
  - Market influence (social following, review volume)

Tiers: S+ (90-100), S (80-89), Tier1 (70-79), Tier2 (60-69), Tier3 (50-59), Unqualified (<50)
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from _tools.crm.crm_parser import CRMBusiness, CRMParser, DEFAULT_CRM

OUTPUT_DIR = Path(__file__).parent.parent.parent / "N01_research" / "output"


@dataclass
class ScoreBreakdown:
    """Detailed score breakdown per dimension."""
    maturity: float = 0.0
    geographic: float = 0.0
    service: float = 0.0
    contact: float = 0.0
    influence: float = 0.0

    @property
    def total(self) -> float:
        return min(self.maturity + self.geographic + self.service + self.contact + self.influence, 100.0)

    def to_dict(self) -> dict[str, float]:
        return {
            "maturity": self.maturity,
            "geographic": self.geographic,
            "service": self.service,
            "contact": self.contact,
            "influence": self.influence,
            "total": self.total,
        }


# --- Scoring weights by dimension (max points) ---
# Maturity: 0-25 | Geographic: 0-20 | Service: 0-25 | Contact: 0-20 | Influence: 0-10

TIER_LABELS = {
    (90, 101): "S+",
    (80, 90): "S",
    (70, 80): "Tier 1",
    (60, 70): "Tier 2",
    (50, 60): "Tier 3",
    (0, 50): "Unqualified",
}

# Cities by ring proximity to SCS (GATO\u00b3 base)
RING_SCORES = {
    "1_abc": 20,
    "2_grande_sp": 12,
    "3_capital": 8,
    "4_interior": 4,
}

CITY_RING_FALLBACK = {
    "sao caetano do sul": 20,
    "santo andre": 18,
    "sao bernardo do campo": 18,
    "diadema": 15,
    "maua": 15,
    "ribeirao pires": 14,
    "rio grande da serra": 14,
    "abc paulista": 16,
    "guarulhos": 12,
    "osasco": 12,
    "barueri": 10,
    "sao paulo": 8,
}

# Segments with cat alignment bonus
CAT_ALIGNED_SEGMENTS = {"clinica_vet", "pet_shop", "banho_tosa"}
PREMIUM_KEYWORDS = {"premium", "boutique", "especialista", "hospital", "24h", "megaloja"}
CAT_KEYWORDS = {"gato", "felino", "cat", "feline", "gatil"}


def score_maturity(biz: CRMBusiness) -> float:
    """Business maturity: 0-25 points based on rating + reviews + porte."""
    pts = 0.0

    # Google rating (0-10)
    if biz.google_rating >= 4.7:
        pts += 10
    elif biz.google_rating >= 4.5:
        pts += 8
    elif biz.google_rating >= 4.0:
        pts += 5
    elif biz.google_rating >= 3.5:
        pts += 2

    # Review volume (0-10)
    if biz.google_reviews >= 500:
        pts += 10
    elif biz.google_reviews >= 200:
        pts += 8
    elif biz.google_reviews >= 100:
        pts += 6
    elif biz.google_reviews >= 50:
        pts += 4
    elif biz.google_reviews >= 20:
        pts += 2

    # Business size / porte (0-5)
    porte_scores = {"grande": 5, "epp": 4, "me": 3, "mei": 2, "ong": 1}
    pts += porte_scores.get(biz.porte.lower(), 1)

    return min(pts, 25.0)


def score_geographic(biz: CRMBusiness) -> float:
    """Geographic alignment: 0-20 points based on ring/city proximity."""
    # Try ring field first
    if biz.ring and biz.ring in RING_SCORES:
        return float(RING_SCORES[biz.ring])

    # Fallback to city name
    city_lower = biz.cidade.lower().strip()
    return float(CITY_RING_FALLBACK.get(city_lower, 5))


def score_service(biz: CRMBusiness) -> float:
    """Service alignment: 0-25 points based on cat specialty + premium + segment fit."""
    pts = 0.0

    # Foco felino explicit flag (0-10)
    if biz.foco_felino:
        pts += 10

    # Cat keywords in name/notes (0-5)
    text = f"{biz.nome_fantasia} {biz.notas} {biz.razao_social}".lower()
    if any(kw in text for kw in CAT_KEYWORDS):
        pts += 5

    # Premium positioning (0-5)
    if any(kw in text for kw in PREMIUM_KEYWORDS):
        pts += 5

    # Segment alignment (0-5)
    seg = biz.segmento.lower().replace(" ", "_")
    if seg in CAT_ALIGNED_SEGMENTS:
        pts += 5

    return min(pts, 25.0)


def score_contact(biz: CRMBusiness) -> float:
    """Contact quality: 0-20 points based on validated channels."""
    pts = 0.0

    # CNPJ validated (0-4)
    if biz.has_cnpj:
        pts += 4

    # Phone (0-4)
    if biz.has_phone:
        pts += 4

    # WhatsApp -- highest value for outreach (0-4)
    if biz.has_whatsapp:
        pts += 4

    # Email (0-3)
    if biz.has_email:
        pts += 3

    # Website (0-3)
    if biz.has_website:
        pts += 3

    # Instagram (0-2)
    if biz.has_instagram:
        pts += 2

    return min(pts, 20.0)


def score_influence(biz: CRMBusiness) -> float:
    """Market influence: 0-10 points based on review volume + social presence."""
    pts = 0.0

    # High review count = market influence (0-5)
    if biz.google_reviews >= 1000:
        pts += 5
    elif biz.google_reviews >= 500:
        pts += 4
    elif biz.google_reviews >= 200:
        pts += 3
    elif biz.google_reviews >= 100:
        pts += 2

    # Social presence (0-3)
    if biz.has_instagram:
        pts += 2
    if biz.website and biz.website != "a_validar":
        pts += 1

    # B2B potential flag from manual classification (0-2)
    pot = biz.potencial_b2b.lower()
    if pot == "alto":
        pts += 2
    elif pot == "medio":
        pts += 1

    return min(pts, 10.0)


def classify_tier(score: float) -> str:
    """Map score to tier label."""
    for (lo, hi), label in TIER_LABELS.items():
        if lo <= score < hi:
            return label
    return "Unqualified"


def recommended_action(tier: str, biz: CRMBusiness) -> str:
    """Generate recommended next action based on tier."""
    actions = {
        "S+": f"PRIORITY: Contato imediato via {'WhatsApp' if biz.has_whatsapp else 'telefone'}. Agendar reuniao presencial.",
        "S": f"Alta prioridade: Enviar proposta personalizada via {'WhatsApp' if biz.has_whatsapp else 'email' if biz.has_email else 'telefone'}.",
        "Tier 1": "Media prioridade: Incluir no proximo lote de outreach. Preparar pitch adaptado ao segmento.",
        "Tier 2": "Pipeline de nutricao: Adicionar a campanhas de email marketing e conteudo educativo.",
        "Tier 3": "Monitoramento: Acompanhar evolucao. Re-avaliar em 90 dias.",
        "Unqualified": "Baixa prioridade: Dados insuficientes ou baixo alinhamento. Validar dados antes de investir esforco.",
    }
    return actions.get(tier, "Avaliar manualmente.")


class LeadScorer:
    """Score all CRM businesses and produce prioritized output."""

    def __init__(self, crm_path: Path | str | None = None):
        self.parser = CRMParser(crm_path)
        self.businesses: list[CRMBusiness] = []
        self.scores: dict[str, ScoreBreakdown] = {}

    def run(self) -> list[CRMBusiness]:
        """Parse CRM, score all businesses, sort by score descending."""
        self.businesses = self.parser.parse()

        for biz in self.businesses:
            breakdown = ScoreBreakdown(
                maturity=score_maturity(biz),
                geographic=score_geographic(biz),
                service=score_service(biz),
                contact=score_contact(biz),
                influence=score_influence(biz),
            )
            biz.lead_score = breakdown.total
            biz.lead_tier = classify_tier(breakdown.total)
            self.scores[biz.id] = breakdown

        # Sort by score descending
        self.businesses.sort(key=lambda b: b.lead_score, reverse=True)
        return self.businesses

    def tier_summary(self) -> dict[str, int]:
        """Count businesses per tier."""
        summary: dict[str, int] = {}
        for biz in self.businesses:
            summary[biz.lead_tier] = summary.get(biz.lead_tier, 0) + 1
        return summary

    def top_leads(self, n: int = 20) -> list[dict]:
        """Return top N leads with full breakdown."""
        results = []
        for biz in self.businesses[:n]:
            breakdown = self.scores.get(biz.id, ScoreBreakdown())
            results.append({
                "nome": biz.nome_fantasia,
                "cidade": biz.cidade,
                "segmento": biz.segmento,
                "score": biz.lead_score,
                "tier": biz.lead_tier,
                "foco_felino": biz.foco_felino,
                "potencial_b2b": biz.potencial_b2b,
                "breakdown": breakdown.to_dict(),
                "action": recommended_action(biz.lead_tier, biz),
                "channels": biz.contact_channels,
            })
        return results

    def export_report(self, output_path: Path | None = None) -> Path:
        """Export full scoring report as JSON."""
        if not self.businesses:
            self.run()

        output_path = output_path or OUTPUT_DIR / "crm_lead_scores.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        report = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_businesses": len(self.businesses),
            "tier_summary": self.tier_summary(),
            "top_20": self.top_leads(20),
            "all_scores": [
                {
                    "id": biz.id,
                    "nome": biz.nome_fantasia,
                    "cidade": biz.cidade,
                    "segmento": biz.segmento,
                    "score": biz.lead_score,
                    "tier": biz.lead_tier,
                    "breakdown": self.scores[biz.id].to_dict(),
                }
                for biz in self.businesses
            ],
        }

        output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        return output_path

    def print_summary(self) -> None:
        """Print tier summary to console."""
        if not self.businesses:
            self.run()

        print("=" * 60)
        print("GATO\u00b3 CRM Lead Scoring -- Summary")
        print("=" * 60)
        print(f"Total businesses: {len(self.businesses)}")
        print()

        for tier, count in sorted(self.tier_summary().items()):
            pct = count / len(self.businesses) * 100
            bar = "#" * int(pct / 2)
            print(f"  {tier:>12}: {count:>4} ({pct:5.1f}%) {bar}")

        print()
        print("Top 10 Leads:")
        print("-" * 60)
        for lead in self.top_leads(10):
            felino = " [FELINO]" if lead["foco_felino"] else ""
            print(f"  {lead['score']:5.1f} [{lead['tier']:>6}] {lead['nome']:<30} {lead['cidade']}{felino}")
            print(f"         -> {lead['action']}")
        print("=" * 60)


# --- CLI ---
if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="CRM Lead Scoring Engine for GATO\u00b3")
    ap.add_argument("--crm", default=str(DEFAULT_CRM), help="Path to CRM .md file")
    ap.add_argument("--export", action="store_true", help="Export full report JSON")
    ap.add_argument("--top", type=int, default=20, help="Number of top leads to show")
    ap.add_argument("--tier", help="Filter by tier (S+, S, Tier 1, Tier 2, Tier 3)")
    ap.add_argument("--json", action="store_true", help="Output as JSON")
    args = ap.parse_args()

    scorer = LeadScorer(args.crm)
    scorer.run()

    if args.tier:
        filtered = [b for b in scorer.businesses if b.lead_tier == args.tier]
        print(f"\n{args.tier} leads ({len(filtered)}):")
        for b in filtered:
            print(f"  {b.lead_score:5.1f} | {b.nome_fantasia:<30} | {b.cidade} | {b.segmento}")
    elif args.json:
        print(json.dumps(scorer.top_leads(args.top), ensure_ascii=False, indent=2))
    elif args.export:
        path = scorer.export_report()
        print(f"Report exported to: {path}")
        scorer.print_summary()
    else:
        scorer.print_summary()
