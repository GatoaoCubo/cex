"""
CRM Markdown Parser -- shared foundation for all CRM tools.
Parses the pipe-delimited CRM table from N01_research output into structured records.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any

# Default CRM location
DEFAULT_CRM = Path(__file__).parent.parent.parent / "N01_research" / "output" / "output_crm_pet_abc_integrated_20260403_115045.md"

# Column mapping: header name -> CRMBusiness field
COLUMN_MAP = {
    "cnpj": "cnpj",
    "razao social": "razao_social",
    "nome fantasia": "nome_fantasia",
    "segmento": "segmento",
    "sub-segmento": "sub_segmento",
    "endereco": "endereco",
    "cidade": "cidade",
    "ring": "ring",
    "telefone": "telefone",
    "whatsapp": "whatsapp",
    "email": "email",
    "instagram": "instagram",
    "website": "website",
    "google maps url": "google_maps_url",
    "google rating": "google_rating",
    "google reviews": "google_reviews",
    "porte": "porte",
    "foco felino": "foco_felino",
    "potencial b2b": "potencial_b2b",
    "notas": "notas",
}


@dataclass
class CRMBusiness:
    """Single business record from the CRM."""

    cnpj: str = ""
    razao_social: str = ""
    nome_fantasia: str = ""
    segmento: str = ""
    sub_segmento: str = ""
    endereco: str = ""
    cidade: str = ""
    ring: str = ""
    telefone: str = ""
    whatsapp: str = ""
    email: str = ""
    instagram: str = ""
    website: str = ""
    google_maps_url: str = ""
    google_rating: float = 0.0
    google_reviews: int = 0
    porte: str = ""
    foco_felino: bool = False
    potencial_b2b: str = ""
    notas: str = ""

    # Computed fields (set by tools, not parsed)
    lead_score: float = 0.0
    lead_tier: str = ""
    data_quality_score: float = 0.0
    validation_flags: list[str] = field(default_factory=list)

    @property
    def id(self) -> str:
        """Stable identifier: CNPJ if available, else normalized name+city."""
        if self.cnpj and self.cnpj != "a_validar":
            return self.cnpj.replace(".", "").replace("/", "").replace("-", "")
        return f"{_normalize(self.nome_fantasia)}_{_normalize(self.cidade)}"

    @property
    def has_phone(self) -> bool:
        return bool(self.telefone) and self.telefone != "a_validar"

    @property
    def has_whatsapp(self) -> bool:
        return bool(self.whatsapp) and self.whatsapp != "a_validar"

    @property
    def has_email(self) -> bool:
        return bool(self.email) and self.email != "a_validar"

    @property
    def has_website(self) -> bool:
        return bool(self.website) and self.website != "a_validar"

    @property
    def has_instagram(self) -> bool:
        return bool(self.instagram) and self.instagram != "a_validar"

    @property
    def has_cnpj(self) -> bool:
        return bool(self.cnpj) and self.cnpj != "a_validar"

    @property
    def contact_channels(self) -> int:
        """Count of validated contact channels."""
        return sum([
            self.has_phone, self.has_whatsapp, self.has_email,
            self.has_website, self.has_instagram,
        ])

    @property
    def is_validated(self) -> bool:
        """Has at least CNPJ + 1 contact channel."""
        return self.has_cnpj and self.contact_channels >= 1

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _normalize(text: str) -> str:
    """Lowercase, strip accents-ish, collapse whitespace."""
    return re.sub(r"\s+", "_", text.strip().lower())


def _clean_cell(cell: str) -> str:
    """Strip markdown bold markers and whitespace from a table cell."""
    return cell.strip().strip("*").strip()


def _parse_rating(val: str) -> float:
    """Parse Google rating, handling 'a_validar' and edge cases."""
    val = _clean_cell(val)
    if not val or val == "a_validar":
        return 0.0
    try:
        return float(val)
    except ValueError:
        return 0.0


def _parse_reviews(val: str) -> int:
    """Parse review count, handling '500+', 'a_validar', etc."""
    val = _clean_cell(val)
    if not val or val == "a_validar":
        return 0
    val = val.replace("+", "").replace(",", "").replace(".", "")
    try:
        return int(val)
    except ValueError:
        return 0


def _parse_bool(val: str) -> bool:
    """Parse boolean field (foco_felino)."""
    val = _clean_cell(val).lower()
    return val in ("true", "sim", "yes", "1")


class CRMParser:
    """Parse CRM markdown tables into CRMBusiness records."""

    def __init__(self, crm_path: Path | str | None = None):
        self.crm_path = Path(crm_path) if crm_path else DEFAULT_CRM

    def parse(self) -> list[CRMBusiness]:
        """Parse the CRM markdown file and return business records."""
        if not self.crm_path.exists():
            raise FileNotFoundError(f"CRM file not found: {self.crm_path}")

        text = self.crm_path.read_text(encoding="utf-8")
        return self._parse_table(text)

    def _parse_table(self, text: str) -> list[CRMBusiness]:
        """Extract table rows from markdown text."""
        lines = text.split("\n")
        businesses: list[CRMBusiness] = []
        header_map: dict[int, str] | None = None

        for line in lines:
            line = line.strip()
            if not line.startswith("|"):
                continue

            cells = [_clean_cell(c) for c in line.split("|")[1:-1]]

            # Detect header row
            if header_map is None:
                header_map = {}
                for i, cell in enumerate(cells):
                    key = cell.lower().strip()
                    if key in COLUMN_MAP:
                        header_map[i] = COLUMN_MAP[key]
                continue

            # Skip separator row (|---|---|...)
            if all(c.replace("-", "").strip() == "" for c in cells):
                continue

            # Parse data row
            biz = self._row_to_business(cells, header_map)
            if biz.nome_fantasia:  # skip empty rows
                businesses.append(biz)

        return businesses

    def _row_to_business(self, cells: list[str], header_map: dict[int, str]) -> CRMBusiness:
        """Convert a row of cells into a CRMBusiness using the header map."""
        raw: dict[str, str] = {}
        for i, field_name in header_map.items():
            if i < len(cells):
                raw[field_name] = _clean_cell(cells[i])

        return CRMBusiness(
            cnpj=raw.get("cnpj", ""),
            razao_social=raw.get("razao_social", ""),
            nome_fantasia=raw.get("nome_fantasia", ""),
            segmento=raw.get("segmento", ""),
            sub_segmento=raw.get("sub_segmento", ""),
            endereco=raw.get("endereco", ""),
            cidade=raw.get("cidade", ""),
            ring=raw.get("ring", ""),
            telefone=raw.get("telefone", ""),
            whatsapp=raw.get("whatsapp", ""),
            email=raw.get("email", ""),
            instagram=raw.get("instagram", ""),
            website=raw.get("website", ""),
            google_maps_url=raw.get("google_maps_url", ""),
            google_rating=_parse_rating(raw.get("google_rating", "")),
            google_reviews=_parse_reviews(raw.get("google_reviews", "")),
            porte=raw.get("porte", ""),
            foco_felino=_parse_bool(raw.get("foco_felino", "")),
            potencial_b2b=raw.get("potencial_b2b", ""),
            notas=raw.get("notas", ""),
        )


# --- CLI ---
if __name__ == "__main__":
    import argparse
    import json

    ap = argparse.ArgumentParser(description="Parse CRM markdown to JSON")
    ap.add_argument("--crm", default=str(DEFAULT_CRM), help="Path to CRM .md file")
    ap.add_argument("--stats", action="store_true", help="Show summary stats only")
    args = ap.parse_args()

    parser = CRMParser(args.crm)
    businesses = parser.parse()

    if args.stats:
        cities = {}
        segments = {}
        for b in businesses:
            cities[b.cidade] = cities.get(b.cidade, 0) + 1
            segments[b.segmento] = segments.get(b.segmento, 0) + 1
        print(f"Total businesses: {len(businesses)}")
        print(f"With CNPJ: {sum(1 for b in businesses if b.has_cnpj)}")
        print(f"With phone: {sum(1 for b in businesses if b.has_phone)}")
        print(f"Validated: {sum(1 for b in businesses if b.is_validated)}")
        print(f"\nBy city: {json.dumps(dict(sorted(cities.items(), key=lambda x: -x[1])), ensure_ascii=False, indent=2)}")
        print(f"\nBy segment: {json.dumps(dict(sorted(segments.items(), key=lambda x: -x[1])), ensure_ascii=False, indent=2)}")
    else:
        out = [b.to_dict() for b in businesses]
        print(json.dumps(out, ensure_ascii=False, indent=2))
