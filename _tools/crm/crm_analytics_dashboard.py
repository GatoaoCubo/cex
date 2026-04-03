"""
CRM Analytics Dashboard — business intelligence for GATO³ B2B pipeline.

Generates:
  - Market penetration analysis by city and segment
  - Lead tier distribution and conversion funnel
  - Geographic heat map data
  - Competitive landscape overview
  - Interactive HTML dashboard
  - JSON/CSV export for reporting
"""

from __future__ import annotations

import html
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from _tools.crm.crm_parser import CRMBusiness, CRMParser, DEFAULT_CRM
from _tools.crm.crm_lead_scorer import LeadScorer

OUTPUT_DIR = Path(__file__).parent.parent.parent / "N01_research" / "output"


class AnalyticsDashboard:
    """Generate analytics and dashboard for CRM data."""

    def __init__(self, crm_path: Path | str | None = None):
        self.scorer = LeadScorer(crm_path)
        self.businesses: list[CRMBusiness] = []

    def load(self) -> None:
        """Load and score CRM data."""
        self.businesses = self.scorer.run()

    def market_penetration(self) -> dict[str, Any]:
        """Analyze market penetration by city and segment."""
        if not self.businesses:
            self.load()

        by_city: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        by_segment: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        by_ring: dict[str, int] = defaultdict(int)

        for biz in self.businesses:
            city = biz.cidade or "Desconhecida"
            seg = biz.segmento or "Outro"
            ring = biz.ring or "unknown"

            by_city[city]["total"] += 1
            by_city[city][seg] += 1
            by_city[city][f"tier_{biz.lead_tier}"] += 1
            if biz.foco_felino:
                by_city[city]["foco_felino"] += 1

            by_segment[seg]["total"] += 1
            by_segment[seg][city] += 1

            by_ring[ring] += 1

        # Sort cities by count
        city_ranking = sorted(by_city.items(), key=lambda x: x[1]["total"], reverse=True)

        return {
            "by_city": {k: dict(v) for k, v in city_ranking},
            "by_segment": {k: dict(v) for k, v in sorted(by_segment.items(), key=lambda x: x[1]["total"], reverse=True)},
            "by_ring": dict(sorted(by_ring.items())),
            "total_cities": len(by_city),
            "total_segments": len(by_segment),
        }

    def conversion_funnel(self) -> dict[str, Any]:
        """Analyze lead tier distribution as a conversion funnel."""
        if not self.businesses:
            self.load()

        tiers = defaultdict(int)
        tier_by_city: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        tier_by_segment: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

        for biz in self.businesses:
            tier = biz.lead_tier or "Unscored"
            tiers[tier] += 1
            tier_by_city[biz.cidade][tier] += 1
            tier_by_segment[biz.segmento][tier] += 1

        total = len(self.businesses)
        funnel = {
            "total_database": total,
            "tiers": {},
        }

        tier_order = ["S+", "S", "Tier 1", "Tier 2", "Tier 3", "Unqualified"]
        cumulative = 0
        for tier in tier_order:
            count = tiers.get(tier, 0)
            cumulative += count
            funnel["tiers"][tier] = {
                "count": count,
                "percentage": round(count / max(total, 1) * 100, 1),
                "cumulative": cumulative,
                "cumulative_pct": round(cumulative / max(total, 1) * 100, 1),
            }

        funnel["actionable_leads"] = sum(tiers.get(t, 0) for t in ["S+", "S", "Tier 1", "Tier 2"])
        funnel["high_priority"] = sum(tiers.get(t, 0) for t in ["S+", "S", "Tier 1"])
        funnel["tier_by_city"] = {k: dict(v) for k, v in tier_by_city.items()}
        funnel["tier_by_segment"] = {k: dict(v) for k, v in tier_by_segment.items()}

        return funnel

    def competitive_landscape(self) -> dict[str, Any]:
        """Analyze competitive landscape — top businesses, market concentration."""
        if not self.businesses:
            self.load()

        # Segment concentration
        segment_counts: dict[str, int] = defaultdict(int)
        segment_felino: dict[str, int] = defaultdict(int)
        porte_dist: dict[str, int] = defaultdict(int)

        top_rated = []
        top_reviewed = []

        for biz in self.businesses:
            seg = biz.segmento or "Outro"
            segment_counts[seg] += 1
            if biz.foco_felino:
                segment_felino[seg] += 1
            porte_dist[biz.porte or "desconhecido"] += 1

            if biz.google_rating > 0:
                top_rated.append((biz.nome_fantasia, biz.cidade, biz.google_rating, biz.google_reviews))
            if biz.google_reviews > 0:
                top_reviewed.append((biz.nome_fantasia, biz.cidade, biz.google_reviews, biz.google_rating))

        top_rated.sort(key=lambda x: (x[2], x[3]), reverse=True)
        top_reviewed.sort(key=lambda x: x[2], reverse=True)

        felino_total = sum(1 for b in self.businesses if b.foco_felino)

        return {
            "total_businesses": len(self.businesses),
            "felino_specialists": felino_total,
            "felino_percentage": round(felino_total / max(len(self.businesses), 1) * 100, 1),
            "segment_distribution": dict(sorted(segment_counts.items(), key=lambda x: -x[1])),
            "segment_felino": dict(sorted(segment_felino.items(), key=lambda x: -x[1])),
            "porte_distribution": dict(sorted(porte_dist.items(), key=lambda x: -x[1])),
            "top_10_rated": [
                {"name": n, "city": c, "rating": r, "reviews": rv}
                for n, c, r, rv in top_rated[:10]
            ],
            "top_10_reviewed": [
                {"name": n, "city": c, "reviews": rv, "rating": r}
                for n, c, rv, r in top_reviewed[:10]
            ],
        }

    def geographic_heatmap_data(self) -> list[dict]:
        """Generate data for geographic heat mapping."""
        if not self.businesses:
            self.load()

        city_data: dict[str, dict[str, Any]] = defaultdict(lambda: {
            "count": 0, "avg_score": 0.0, "felino": 0, "high_priority": 0,
            "scores": [],
        })

        for biz in self.businesses:
            city = biz.cidade or "Desconhecida"
            city_data[city]["count"] += 1
            city_data[city]["scores"].append(biz.lead_score)
            if biz.foco_felino:
                city_data[city]["felino"] += 1
            if biz.lead_tier in ("S+", "S", "Tier 1"):
                city_data[city]["high_priority"] += 1

        result = []
        for city, data in city_data.items():
            scores = data["scores"]
            result.append({
                "city": city,
                "total": data["count"],
                "avg_lead_score": round(sum(scores) / len(scores), 1) if scores else 0,
                "felino_specialists": data["felino"],
                "high_priority_leads": data["high_priority"],
                "market_density": "high" if data["count"] > 100 else "medium" if data["count"] > 30 else "low",
            })

        result.sort(key=lambda x: x["total"], reverse=True)
        return result

    def generate_html_dashboard(self, output_path: Path | None = None) -> Path:
        """Generate interactive HTML dashboard."""
        if not self.businesses:
            self.load()

        output_path = output_path or OUTPUT_DIR / "crm_dashboard.html"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        penetration = self.market_penetration()
        funnel = self.conversion_funnel()
        landscape = self.competitive_landscape()
        geo = self.geographic_heatmap_data()

        html_content = _build_html(penetration, funnel, landscape, geo, self.businesses)
        output_path.write_text(html_content, encoding="utf-8")
        return output_path

    def export_json(self, output_path: Path | None = None) -> Path:
        """Export all analytics as JSON."""
        if not self.businesses:
            self.load()

        output_path = output_path or OUTPUT_DIR / "crm_analytics.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        report = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "market_penetration": self.market_penetration(),
            "conversion_funnel": self.conversion_funnel(),
            "competitive_landscape": self.competitive_landscape(),
            "geographic_data": self.geographic_heatmap_data(),
        }

        output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        return output_path

    def print_summary(self) -> None:
        """Print dashboard summary to console."""
        if not self.businesses:
            self.load()

        funnel = self.conversion_funnel()
        landscape = self.competitive_landscape()
        geo = self.geographic_heatmap_data()

        print("=" * 65)
        print("GATO³ CRM Analytics Dashboard")
        print("=" * 65)

        print(f"\nTotal businesses: {len(self.businesses)}")
        print(f"Felino specialists: {landscape['felino_specialists']} ({landscape['felino_percentage']}%)")
        print(f"Actionable leads (S+ to Tier2): {funnel['actionable_leads']}")
        print(f"High priority (S+ to Tier1): {funnel['high_priority']}")

        print("\n--- Lead Funnel ---")
        for tier, data in funnel["tiers"].items():
            bar = "#" * int(data["percentage"] / 2)
            print(f"  {tier:>12}: {data['count']:>4} ({data['percentage']:>5.1f}%) {bar}")

        print("\n--- Market by City ---")
        for g in geo[:6]:
            density = {"high": "***", "medium": "**", "low": "*"}.get(g["market_density"], "")
            print(f"  {g['city']:<25} {g['total']:>4} businesses  avg_score={g['avg_lead_score']:>5.1f}  felino={g['felino_specialists']} {density}")

        print("\n--- Segment Distribution ---")
        for seg, count in list(landscape["segment_distribution"].items())[:8]:
            pct = count / len(self.businesses) * 100
            print(f"  {seg:<25} {count:>4} ({pct:>5.1f}%)")

        print("\n--- Top Rated ---")
        for entry in landscape["top_10_rated"][:5]:
            print(f"  {entry['rating']:.1f} ({entry['reviews']:>5} reviews) {entry['name']:<30} {entry['city']}")

        print("=" * 65)


def _esc(text: Any) -> str:
    return html.escape(str(text))


def _build_html(
    penetration: dict, funnel: dict, landscape: dict,
    geo: list[dict], businesses: list[CRMBusiness],
) -> str:
    """Build the HTML dashboard string."""

    # Funnel bars
    funnel_rows = ""
    tier_colors = {"S+": "#e74c3c", "S": "#e67e22", "Tier 1": "#f1c40f", "Tier 2": "#3498db", "Tier 3": "#95a5a6", "Unqualified": "#bdc3c7"}
    for tier, data in funnel["tiers"].items():
        color = tier_colors.get(tier, "#ccc")
        funnel_rows += f"""
        <tr>
            <td><strong>{_esc(tier)}</strong></td>
            <td>{data['count']}</td>
            <td>{data['percentage']}%</td>
            <td><div style="background:{color};width:{data['percentage']*3}px;height:20px;border-radius:3px"></div></td>
        </tr>"""

    # City table
    city_rows = ""
    for g in geo[:15]:
        city_rows += f"""
        <tr>
            <td>{_esc(g['city'])}</td>
            <td>{g['total']}</td>
            <td>{g['avg_lead_score']:.1f}</td>
            <td>{g['felino_specialists']}</td>
            <td>{g['high_priority_leads']}</td>
            <td><span class="badge {g['market_density']}">{g['market_density']}</span></td>
        </tr>"""

    # Segment table
    seg_rows = ""
    for seg, count in landscape["segment_distribution"].items():
        felino = landscape["segment_felino"].get(seg, 0)
        pct = count / max(len(businesses), 1) * 100
        seg_rows += f"""
        <tr>
            <td>{_esc(seg)}</td>
            <td>{count}</td>
            <td>{pct:.1f}%</td>
            <td>{felino}</td>
        </tr>"""

    # Top leads table
    top_rows = ""
    for biz in businesses[:25]:
        felino_badge = '<span class="badge felino">FELINO</span>' if biz.foco_felino else ""
        top_rows += f"""
        <tr>
            <td>{biz.lead_score:.0f}</td>
            <td><strong>{_esc(biz.lead_tier)}</strong></td>
            <td>{_esc(biz.nome_fantasia)} {felino_badge}</td>
            <td>{_esc(biz.cidade)}</td>
            <td>{_esc(biz.segmento)}</td>
            <td>{biz.google_rating:.1f}</td>
            <td>{biz.google_reviews}</td>
        </tr>"""

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GATO³ CRM Analytics Dashboard</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #f5f6fa; color: #2c3e50; padding: 20px; }}
  .container {{ max-width: 1200px; margin: 0 auto; }}
  h1 {{ font-size: 28px; margin-bottom: 5px; }}
  .subtitle {{ color: #7f8c8d; margin-bottom: 20px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-bottom: 25px; }}
  .card {{ background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
  .card h3 {{ font-size: 14px; color: #7f8c8d; text-transform: uppercase; margin-bottom: 8px; }}
  .card .value {{ font-size: 32px; font-weight: 700; }}
  .card .detail {{ font-size: 13px; color: #95a5a6; margin-top: 4px; }}
  .section {{ background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 20px; }}
  .section h2 {{ font-size: 18px; margin-bottom: 15px; padding-bottom: 8px; border-bottom: 2px solid #ecf0f1; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  th {{ text-align: left; padding: 8px 12px; background: #f8f9fa; border-bottom: 2px solid #ecf0f1; font-weight: 600; }}
  td {{ padding: 8px 12px; border-bottom: 1px solid #ecf0f1; }}
  tr:hover td {{ background: #f8f9fa; }}
  .badge {{ padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; }}
  .badge.high {{ background: #fee2e2; color: #991b1b; }}
  .badge.medium {{ background: #fef3c7; color: #92400e; }}
  .badge.low {{ background: #d1fae5; color: #065f46; }}
  .badge.felino {{ background: #ede9fe; color: #5b21b6; }}
  .footer {{ text-align: center; color: #bdc3c7; font-size: 12px; margin-top: 30px; }}
</style>
</head>
<body>
<div class="container">
  <h1>GATO³ CRM Analytics</h1>
  <p class="subtitle">ABC Paulista Pet Market Intelligence — {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>

  <div class="grid">
    <div class="card">
      <h3>Total Businesses</h3>
      <div class="value">{len(businesses)}</div>
      <div class="detail">{landscape['total_businesses']} across {len(geo)} cities</div>
    </div>
    <div class="card">
      <h3>Felino Specialists</h3>
      <div class="value" style="color:#5b21b6">{landscape['felino_specialists']}</div>
      <div class="detail">{landscape['felino_percentage']}% of total market</div>
    </div>
    <div class="card">
      <h3>Actionable Leads</h3>
      <div class="value" style="color:#2563eb">{funnel['actionable_leads']}</div>
      <div class="detail">S+ through Tier 2</div>
    </div>
    <div class="card">
      <h3>High Priority</h3>
      <div class="value" style="color:#dc2626">{funnel['high_priority']}</div>
      <div class="detail">S+ through Tier 1</div>
    </div>
  </div>

  <div class="section">
    <h2>Lead Funnel</h2>
    <table>
      <tr><th>Tier</th><th>Count</th><th>%</th><th>Distribution</th></tr>
      {funnel_rows}
    </table>
  </div>

  <div class="section">
    <h2>Market by City</h2>
    <table>
      <tr><th>City</th><th>Total</th><th>Avg Score</th><th>Felino</th><th>High Priority</th><th>Density</th></tr>
      {city_rows}
    </table>
  </div>

  <div class="section">
    <h2>Segment Distribution</h2>
    <table>
      <tr><th>Segment</th><th>Count</th><th>%</th><th>Felino</th></tr>
      {seg_rows}
    </table>
  </div>

  <div class="section">
    <h2>Top 25 Leads</h2>
    <table>
      <tr><th>Score</th><th>Tier</th><th>Business</th><th>City</th><th>Segment</th><th>Rating</th><th>Reviews</th></tr>
      {top_rows}
    </table>
  </div>

  <p class="footer">Generated by CEX N03 Builder — GATO³ CRM Automation Suite</p>
</div>
</body>
</html>"""


# --- CLI ---
if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="CRM Analytics Dashboard for GATO³")
    ap.add_argument("--crm", default=str(DEFAULT_CRM), help="Path to CRM .md file")
    ap.add_argument("--html", action="store_true", help="Generate HTML dashboard")
    ap.add_argument("--json", action="store_true", help="Export JSON analytics")
    ap.add_argument("--funnel", action="store_true", help="Show conversion funnel only")
    ap.add_argument("--landscape", action="store_true", help="Show competitive landscape")
    args = ap.parse_args()

    dashboard = AnalyticsDashboard(args.crm)

    if args.html:
        path = dashboard.generate_html_dashboard()
        print(f"Dashboard generated: {path}")
        dashboard.print_summary()
    elif args.json:
        path = dashboard.export_json()
        print(f"Analytics exported: {path}")
    elif args.funnel:
        funnel = dashboard.conversion_funnel()
        print(json.dumps(funnel, ensure_ascii=False, indent=2))
    elif args.landscape:
        ls = dashboard.competitive_landscape()
        print(json.dumps(ls, ensure_ascii=False, indent=2))
    else:
        dashboard.print_summary()
