"""
CRM Discovery Sync — integration with cex_discovery_pipeline for ongoing CRM updates.

Bridges the discovery pipeline's BusinessRecord format with the CRM markdown table.
Supports:
  - Converting discovery results (JSON) to CRM format
  - Incremental CRM updates (new + enhanced records)
  - Change detection between CRM versions
  - Data source health monitoring
"""

from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from _tools.crm.crm_parser import CRMBusiness, CRMParser, DEFAULT_CRM

OUTPUT_DIR = Path(__file__).parent.parent.parent / "N01_research" / "output"
DISCOVERY_OUTPUT = Path(__file__).parent.parent.parent / "cex_discovery_pipeline" / "output"
SYNC_LOG = Path(__file__).parent.parent.parent / ".cex" / "runtime" / "crm_sync_log.json"


@dataclass
class SyncResult:
    """Result of a sync operation."""
    timestamp: str = ""
    source_file: str = ""
    total_source_records: int = 0
    new_records: int = 0
    enhanced_records: int = 0
    duplicate_skipped: int = 0
    changes: list[dict] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "source_file": self.source_file,
            "total_source_records": self.total_source_records,
            "new_records": self.new_records,
            "enhanced_records": self.enhanced_records,
            "duplicate_skipped": self.duplicate_skipped,
            "changes": self.changes,
        }


def _normalize(text: str) -> str:
    """Normalize text for comparison."""
    return re.sub(r"\s+", " ", text.strip().lower())


def _fuzzy_match(a: str, b: str) -> float:
    """Fuzzy string similarity ratio."""
    return SequenceMatcher(None, _normalize(a), _normalize(b)).ratio()


class DiscoverySync:
    """Sync discovery pipeline results into the CRM."""

    def __init__(self, crm_path: Path | str | None = None):
        self.crm_path = Path(crm_path) if crm_path else DEFAULT_CRM
        self.parser = CRMParser(self.crm_path)
        self.existing: list[CRMBusiness] = []
        self._existing_index: dict[str, CRMBusiness] = {}
        self.sync_history: list[dict] = []
        self._load_history()

    def _load_history(self) -> None:
        """Load sync history from disk."""
        if SYNC_LOG.exists():
            data = json.loads(SYNC_LOG.read_text(encoding="utf-8"))
            self.sync_history = data.get("history", [])

    def _save_history(self, result: SyncResult) -> None:
        """Append sync result to history."""
        self.sync_history.append(result.to_dict())
        SYNC_LOG.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "total_syncs": len(self.sync_history),
            "history": self.sync_history[-50:],  # keep last 50
        }
        SYNC_LOG.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def _load_existing(self) -> None:
        """Load current CRM data and build lookup index."""
        self.existing = self.parser.parse()
        self._existing_index = {}

        for biz in self.existing:
            # Index by CNPJ digits
            if biz.has_cnpj:
                cnpj_key = re.sub(r"[^\d]", "", biz.cnpj)
                self._existing_index[f"cnpj:{cnpj_key}"] = biz

            # Index by phone digits
            if biz.has_phone:
                phone_key = re.sub(r"[^\d]", "", biz.telefone)
                self._existing_index[f"phone:{phone_key}"] = biz

            # Index by normalized name+city
            name_key = f"name:{_normalize(biz.nome_fantasia)}:{_normalize(biz.cidade)}"
            self._existing_index[name_key] = biz

    def _find_match(self, record: dict) -> CRMBusiness | None:
        """Find a matching existing CRM record for a discovery record."""
        # Exact CNPJ match
        cnpj = re.sub(r"[^\d]", "", record.get("cnpj", ""))
        if cnpj and len(cnpj) == 14:
            match = self._existing_index.get(f"cnpj:{cnpj}")
            if match:
                return match

        # Exact phone match
        phone = re.sub(r"[^\d]", "", record.get("phone", ""))
        if phone and len(phone) >= 10:
            match = self._existing_index.get(f"phone:{phone}")
            if match:
                return match

        # Fuzzy name+city match
        name = record.get("name", "")
        city = record.get("city", "")
        if name and city:
            key = f"name:{_normalize(name)}:{_normalize(city)}"
            match = self._existing_index.get(key)
            if match:
                return match

            # Broader fuzzy search
            for biz in self.existing:
                if _normalize(biz.cidade) != _normalize(city):
                    continue
                if _fuzzy_match(biz.nome_fantasia, name) >= 0.85:
                    return biz

        return None

    def _discovery_to_crm(self, record: dict) -> CRMBusiness:
        """Convert a discovery pipeline BusinessRecord dict to CRMBusiness."""
        return CRMBusiness(
            cnpj=record.get("cnpj", "") or "a_validar",
            razao_social=record.get("name", ""),
            nome_fantasia=record.get("name", ""),
            segmento=record.get("category", "") or record.get("subcategory", "") or "a_validar",
            sub_segmento=record.get("subcategory", "") or "a_validar",
            endereco=record.get("address", "") or "a_validar",
            cidade=record.get("city", "") or "a_validar",
            ring=_infer_ring(record.get("city", "")),
            telefone=record.get("phone", "") or "a_validar",
            whatsapp="a_validar",
            email=record.get("email", "") or "a_validar",
            instagram=record.get("social_instagram", "") or "a_validar",
            website=record.get("website", "") or "a_validar",
            google_maps_url=record.get("source_url", "") or "a_validar",
            google_rating=float(record.get("rating", 0) or 0),
            google_reviews=int(record.get("review_count", 0) or 0),
            porte="a_validar",
            foco_felino=False,
            potencial_b2b="a_validar",
            notas=f"Discovery sync {datetime.now().strftime('%Y-%m-%d')} | source: {record.get('source', 'unknown')}",
        )

    def _enhance_record(self, existing: CRMBusiness, new_data: dict) -> list[str]:
        """Fill in 'a_validar' fields from new discovery data. Returns list of enhanced fields."""
        enhanced = []
        field_map = {
            "phone": "telefone",
            "email": "email",
            "website": "website",
            "social_instagram": "instagram",
            "address": "endereco",
            "cnpj": "cnpj",
            "source_url": "google_maps_url",
        }

        for src_field, dst_field in field_map.items():
            current = getattr(existing, dst_field, "")
            new_val = new_data.get(src_field, "")
            if (not current or current == "a_validar") and new_val:
                setattr(existing, dst_field, new_val)
                enhanced.append(dst_field)

        # Enhance numeric fields if zero
        if existing.google_rating == 0 and new_data.get("rating"):
            existing.google_rating = float(new_data["rating"])
            enhanced.append("google_rating")

        if existing.google_reviews == 0 and new_data.get("review_count"):
            existing.google_reviews = int(new_data["review_count"])
            enhanced.append("google_reviews")

        return enhanced

    def sync_from_json(self, json_path: Path | str) -> SyncResult:
        """Sync discovery results from a JSON file into the CRM."""
        json_path = Path(json_path)
        if not json_path.exists():
            raise FileNotFoundError(f"Discovery results not found: {json_path}")

        self._load_existing()

        data = json.loads(json_path.read_text(encoding="utf-8"))

        # Handle different JSON structures
        if isinstance(data, list):
            records = data
        elif isinstance(data, dict):
            records = data.get("businesses", data.get("results", data.get("records", [])))
            if not records and "businesses" not in data:
                # Try to find list values
                for v in data.values():
                    if isinstance(v, list) and v and isinstance(v[0], dict):
                        records = v
                        break
        else:
            records = []

        result = SyncResult(
            timestamp=datetime.now(timezone.utc).isoformat(),
            source_file=str(json_path),
            total_source_records=len(records),
        )

        new_businesses: list[CRMBusiness] = []

        for record in records:
            if not isinstance(record, dict):
                continue
            if not record.get("name"):
                continue

            match = self._find_match(record)

            if match:
                # Try to enhance existing record
                enhanced_fields = self._enhance_record(match, record)
                if enhanced_fields:
                    result.enhanced_records += 1
                    result.changes.append({
                        "type": "enhanced",
                        "business": match.nome_fantasia,
                        "fields": enhanced_fields,
                    })
                else:
                    result.duplicate_skipped += 1
            else:
                # New record
                new_biz = self._discovery_to_crm(record)
                new_businesses.append(new_biz)
                result.new_records += 1
                result.changes.append({
                    "type": "new",
                    "business": new_biz.nome_fantasia,
                    "city": new_biz.cidade,
                    "source": record.get("source", "unknown"),
                })

        # Save sync result
        self._save_history(result)

        # If there are new businesses, report them (actual CRM write is separate)
        if new_businesses:
            new_path = OUTPUT_DIR / f"crm_new_discoveries_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            new_path.parent.mkdir(parents=True, exist_ok=True)
            new_data = [b.to_dict() for b in new_businesses]
            new_path.write_text(json.dumps(new_data, ensure_ascii=False, indent=2), encoding="utf-8")
            result.changes.append({
                "type": "export",
                "file": str(new_path),
                "count": len(new_businesses),
            })

        return result

    def detect_changes(self, other_crm_path: Path | str) -> dict[str, Any]:
        """Detect changes between current CRM and another version."""
        current = self.parser.parse()
        other_parser = CRMParser(other_crm_path)
        other = other_parser.parse()

        current_ids = {b.id: b for b in current}
        other_ids = {b.id: b for b in other}

        added = [b.nome_fantasia for bid, b in other_ids.items() if bid not in current_ids]
        removed = [b.nome_fantasia for bid, b in current_ids.items() if bid not in other_ids]
        common = set(current_ids.keys()) & set(other_ids.keys())

        modified = []
        for bid in common:
            c = current_ids[bid]
            o = other_ids[bid]
            changes = []
            for field_name in ["telefone", "email", "website", "instagram", "endereco", "google_rating"]:
                cv = getattr(c, field_name)
                ov = getattr(o, field_name)
                if cv != ov and str(ov) != "a_validar":
                    changes.append({"field": field_name, "old": str(cv), "new": str(ov)})
            if changes:
                modified.append({"business": c.nome_fantasia, "changes": changes})

        return {
            "current_count": len(current),
            "other_count": len(other),
            "added": added,
            "removed": removed,
            "modified": modified,
            "added_count": len(added),
            "removed_count": len(removed),
            "modified_count": len(modified),
        }

    def source_health(self) -> dict[str, Any]:
        """Check health of discovery data sources."""
        results = {}

        # Scan discovery output for result files
        if DISCOVERY_OUTPUT.exists():
            for f in DISCOVERY_OUTPUT.glob("*.json"):
                try:
                    data = json.loads(f.read_text(encoding="utf-8"))
                    if isinstance(data, dict):
                        count = len(data.get("businesses", data.get("results", [])))
                    elif isinstance(data, list):
                        count = len(data)
                    else:
                        count = 0
                    results[f.name] = {
                        "records": count,
                        "size_kb": round(f.stat().st_size / 1024, 1),
                        "modified": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
                        "status": "ok" if count > 0 else "empty",
                    }
                except (json.JSONDecodeError, KeyError):
                    results[f.name] = {"status": "parse_error"}

        # Check CRM file
        crm_status = "ok" if self.crm_path.exists() else "missing"
        results["crm_main"] = {
            "path": str(self.crm_path),
            "status": crm_status,
            "size_kb": round(self.crm_path.stat().st_size / 1024, 1) if self.crm_path.exists() else 0,
        }

        return {
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "sources": results,
            "total_sources": len(results),
            "healthy": sum(1 for v in results.values() if v.get("status") == "ok"),
        }

    def backup_crm(self) -> Path:
        """Create a timestamped backup of the current CRM file."""
        if not self.crm_path.exists():
            raise FileNotFoundError(f"CRM file not found: {self.crm_path}")

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.crm_path.parent / f"output_crm_pet_abc_backup_{ts}.md"
        shutil.copy2(self.crm_path, backup_path)
        return backup_path


def _infer_ring(city: str) -> str:
    """Infer ring classification from city name."""
    city_lower = city.lower().strip() if city else ""
    abc_cities = {"são caetano do sul", "santo andré", "são bernardo do campo", "diadema", "mauá", "ribeirão pires", "rio grande da serra"}
    grande_sp = {"guarulhos", "osasco", "barueri", "cotia", "taboão da serra", "carapicuíba"}

    if city_lower in abc_cities or "abc" in city_lower:
        return "1_abc"
    elif city_lower in grande_sp:
        return "2_grande_sp"
    elif city_lower == "são paulo":
        return "3_capital"
    else:
        return "4_interior"


# --- CLI ---
if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="CRM Discovery Sync for GATO³")
    ap.add_argument("--crm", default=str(DEFAULT_CRM), help="Path to CRM .md file")
    ap.add_argument("--sync", help="Sync from discovery JSON file")
    ap.add_argument("--diff", help="Detect changes vs another CRM file")
    ap.add_argument("--health", action="store_true", help="Check data source health")
    ap.add_argument("--backup", action="store_true", help="Backup current CRM")
    ap.add_argument("--history", action="store_true", help="Show sync history")
    args = ap.parse_args()

    syncer = DiscoverySync(args.crm)

    if args.sync:
        result = syncer.sync_from_json(args.sync)
        print(f"\nSync complete from: {result.source_file}")
        print(f"  Source records: {result.total_source_records}")
        print(f"  New: {result.new_records}")
        print(f"  Enhanced: {result.enhanced_records}")
        print(f"  Duplicates skipped: {result.duplicate_skipped}")
        if result.changes:
            print(f"\nChanges ({len(result.changes)}):")
            for c in result.changes[:20]:
                if c["type"] == "new":
                    print(f"  + {c['business']} ({c['city']})")
                elif c["type"] == "enhanced":
                    print(f"  ~ {c['business']} -> {', '.join(c['fields'])}")
                elif c["type"] == "export":
                    print(f"  >> Exported {c['count']} new records to {c['file']}")
    elif args.diff:
        changes = syncer.detect_changes(args.diff)
        print(f"\nCRM Diff: {changes['current_count']} current vs {changes['other_count']} other")
        print(f"  Added: {changes['added_count']}")
        print(f"  Removed: {changes['removed_count']}")
        print(f"  Modified: {changes['modified_count']}")
    elif args.health:
        health = syncer.source_health()
        print(f"\nData Source Health: {health['healthy']}/{health['total_sources']} healthy")
        for name, info in health["sources"].items():
            status = info.get("status", "unknown")
            records = info.get("records", "")
            size = info.get("size_kb", "")
            print(f"  {status:>5} | {name:<40} | {records} records | {size} KB")
    elif args.backup:
        path = syncer.backup_crm()
        print(f"Backup saved: {path}")
    elif args.history:
        if syncer.sync_history:
            print(f"\nSync history ({len(syncer.sync_history)} entries):")
            for entry in syncer.sync_history[-10:]:
                print(f"  {entry['timestamp'][:19]} | +{entry['new_records']} new | ~{entry['enhanced_records']} enhanced | from {Path(entry['source_file']).name}")
        else:
            print("No sync history found.")
    else:
        ap.print_help()
