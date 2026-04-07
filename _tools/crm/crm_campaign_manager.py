"""
CRM Campaign Manager -- outreach tracking + follow-up scheduling for GATO\u00b3.

Tracks multi-channel outreach (WhatsApp, phone, email, social) per business.
Manages campaign state in a JSON file alongside the CRM.
Generates follow-up schedules and performance reports.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
from enum import Enum
from pathlib import Path
from typing import Any

from _tools.crm.crm_parser import CRMBusiness, CRMParser, DEFAULT_CRM

CAMPAIGN_DB = Path(__file__).parent.parent.parent / ".cex" / "runtime" / "crm_campaigns.json"
OUTPUT_DIR = Path(__file__).parent.parent.parent / "N01_research" / "output"


class Channel(str, Enum):
    WHATSAPP = "whatsapp"
    PHONE = "phone"
    EMAIL = "email"
    INSTAGRAM = "instagram"
    IN_PERSON = "in_person"


class ActivityType(str, Enum):
    INITIAL_CONTACT = "initial_contact"
    FOLLOW_UP = "follow_up"
    MEETING = "meeting"
    PROPOSAL = "proposal"
    NEGOTIATION = "negotiation"
    CLOSED = "closed"


class ResponseStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    DELIVERED = "delivered"
    READ = "read"
    RESPONDED = "responded"
    INTERESTED = "interested"
    NOT_INTERESTED = "not_interested"
    NEEDS_FOLLOW_UP = "needs_follow_up"
    CONVERTED = "converted"
    LOST = "lost"


# Follow-up intervals by response status (days)
FOLLOW_UP_INTERVALS = {
    ResponseStatus.PENDING: 3,
    ResponseStatus.SENT: 5,
    ResponseStatus.DELIVERED: 7,
    ResponseStatus.READ: 3,
    ResponseStatus.RESPONDED: 2,
    ResponseStatus.INTERESTED: 1,
    ResponseStatus.NEEDS_FOLLOW_UP: 5,
    ResponseStatus.NOT_INTERESTED: 30,
    ResponseStatus.CONVERTED: 0,  # no follow-up
    ResponseStatus.LOST: 0,
}


@dataclass
class CampaignActivity:
    """Single outreach activity record."""
    business_id: str
    channel: str
    date: str  # ISO format
    activity_type: str
    status: str = "pending"
    response: str = ""
    next_action: str = ""
    next_action_date: str = ""
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class BusinessCampaignState:
    """Aggregated campaign state for a single business."""
    business_id: str
    business_name: str
    cidade: str = ""
    segmento: str = ""
    lead_tier: str = ""
    total_touches: int = 0
    last_contact_date: str = ""
    last_channel: str = ""
    current_status: str = "new"
    next_action: str = ""
    next_action_date: str = ""
    activities: list[dict] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class CampaignManager:
    """Manage outreach campaigns and track activities per business."""

    def __init__(self, crm_path: Path | str | None = None, db_path: Path | None = None):
        self.parser = CRMParser(crm_path)
        self.db_path = db_path or CAMPAIGN_DB
        self.businesses: list[CRMBusiness] = []
        self.states: dict[str, BusinessCampaignState] = {}
        self._load_db()

    def _load_db(self) -> None:
        """Load campaign state from disk."""
        if self.db_path.exists():
            data = json.loads(self.db_path.read_text(encoding="utf-8"))
            for entry in data.get("states", []):
                state = BusinessCampaignState(**entry)
                self.states[state.business_id] = state

    def _save_db(self) -> None:
        """Persist campaign state to disk."""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "total_businesses": len(self.states),
            "states": [s.to_dict() for s in self.states.values()],
        }
        self.db_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def initialize_from_crm(self, scored_businesses: list[CRMBusiness] | None = None) -> int:
        """Initialize campaign states from CRM (or pre-scored list). Returns count of new entries."""
        if scored_businesses:
            self.businesses = scored_businesses
        else:
            self.businesses = self.parser.parse()

        new_count = 0
        for biz in self.businesses:
            if biz.id not in self.states:
                self.states[biz.id] = BusinessCampaignState(
                    business_id=biz.id,
                    business_name=biz.nome_fantasia,
                    cidade=biz.cidade,
                    segmento=biz.segmento,
                    lead_tier=biz.lead_tier or "",
                )
                new_count += 1

        self._save_db()
        return new_count

    def log_activity(
        self,
        business_id: str,
        channel: str,
        activity_type: str,
        status: str = "sent",
        response: str = "",
        notes: str = "",
    ) -> CampaignActivity:
        """Log an outreach activity for a business."""
        now = datetime.now(timezone.utc)
        activity = CampaignActivity(
            business_id=business_id,
            channel=channel,
            date=now.isoformat(),
            activity_type=activity_type,
            status=status,
            response=response,
            notes=notes,
        )

        # Calculate next action date
        try:
            resp_enum = ResponseStatus(status)
            interval = FOLLOW_UP_INTERVALS.get(resp_enum, 7)
        except ValueError:
            interval = 7

        if interval > 0:
            next_date = now + timedelta(days=interval)
            activity.next_action = _suggest_next_action(activity_type, status)
            activity.next_action_date = next_date.isoformat()

        # Update business state
        if business_id not in self.states:
            self.states[business_id] = BusinessCampaignState(
                business_id=business_id,
                business_name=business_id,
            )

        state = self.states[business_id]
        state.total_touches += 1
        state.last_contact_date = activity.date
        state.last_channel = channel
        state.current_status = status
        state.next_action = activity.next_action
        state.next_action_date = activity.next_action_date
        state.activities.append(activity.to_dict())

        self._save_db()
        return activity

    def get_due_followups(self, as_of: datetime | None = None) -> list[dict]:
        """Get all businesses needing follow-up as of the given date."""
        now = as_of or datetime.now(timezone.utc)
        due = []

        for state in self.states.values():
            if not state.next_action_date:
                continue
            if state.current_status in ("converted", "lost", "not_interested"):
                continue

            try:
                next_dt = datetime.fromisoformat(state.next_action_date)
                if next_dt.tzinfo is None:
                    next_dt = next_dt.replace(tzinfo=timezone.utc)
                if next_dt <= now:
                    due.append({
                        "business_id": state.business_id,
                        "business_name": state.business_name,
                        "cidade": state.cidade,
                        "tier": state.lead_tier,
                        "overdue_days": (now - next_dt).days,
                        "last_channel": state.last_channel,
                        "current_status": state.current_status,
                        "suggested_action": state.next_action,
                        "total_touches": state.total_touches,
                    })
            except (ValueError, TypeError):
                continue

        # Sort by overdue days descending
        due.sort(key=lambda x: x["overdue_days"], reverse=True)
        return due

    def campaign_stats(self) -> dict[str, Any]:
        """Generate campaign performance statistics."""
        total = len(self.states)
        if total == 0:
            return {"total": 0}

        status_counts: dict[str, int] = {}
        channel_counts: dict[str, int] = {}
        tier_counts: dict[str, int] = {}
        total_touches = 0

        for state in self.states.values():
            status_counts[state.current_status] = status_counts.get(state.current_status, 0) + 1
            tier_counts[state.lead_tier or "unscored"] = tier_counts.get(state.lead_tier or "unscored", 0) + 1
            total_touches += state.total_touches
            if state.last_channel:
                channel_counts[state.last_channel] = channel_counts.get(state.last_channel, 0) + 1

        contacted = total - status_counts.get("new", 0)
        interested = status_counts.get("interested", 0) + status_counts.get("responded", 0)
        converted = status_counts.get("converted", 0)

        return {
            "total_businesses": total,
            "contacted": contacted,
            "contact_rate": round(contacted / total * 100, 1) if total else 0,
            "interested": interested,
            "interest_rate": round(interested / max(contacted, 1) * 100, 1),
            "converted": converted,
            "conversion_rate": round(converted / max(contacted, 1) * 100, 1),
            "total_touches": total_touches,
            "avg_touches_per_business": round(total_touches / max(contacted, 1), 1),
            "by_status": dict(sorted(status_counts.items(), key=lambda x: -x[1])),
            "by_channel": dict(sorted(channel_counts.items(), key=lambda x: -x[1])),
            "by_tier": dict(sorted(tier_counts.items())),
        }

    def generate_outreach_plan(self, batch_size: int = 20) -> list[dict]:
        """Generate next outreach batch prioritized by tier + staleness."""
        candidates = []
        now = datetime.now(timezone.utc)

        for state in self.states.values():
            if state.current_status in ("converted", "lost", "not_interested"):
                continue

            # Calculate staleness (days since last contact)
            staleness = 999
            if state.last_contact_date:
                try:
                    last = datetime.fromisoformat(state.last_contact_date)
                    if last.tzinfo is None:
                        last = last.replace(tzinfo=timezone.utc)
                    staleness = (now - last).days
                except (ValueError, TypeError):
                    pass

            # Priority score: tier weight + staleness
            tier_weights = {"S+": 100, "S": 80, "Tier 1": 60, "Tier 2": 40, "Tier 3": 20, "Unqualified": 5, "": 10}
            priority = tier_weights.get(state.lead_tier, 10) + min(staleness, 30)

            candidates.append({
                "business_id": state.business_id,
                "business_name": state.business_name,
                "cidade": state.cidade,
                "tier": state.lead_tier,
                "current_status": state.current_status,
                "days_since_contact": staleness if staleness < 999 else None,
                "total_touches": state.total_touches,
                "priority_score": priority,
                "suggested_channel": _suggest_channel(state),
                "suggested_action": _suggest_next_action(
                    state.activities[-1]["activity_type"] if state.activities else "initial_contact",
                    state.current_status,
                ),
            })

        candidates.sort(key=lambda x: x["priority_score"], reverse=True)
        return candidates[:batch_size]

    def export_report(self, output_path: Path | None = None) -> Path:
        """Export campaign report as JSON."""
        output_path = output_path or OUTPUT_DIR / "crm_campaign_report.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        report = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "stats": self.campaign_stats(),
            "due_followups": self.get_due_followups(),
            "next_batch": self.generate_outreach_plan(),
        }

        output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        return output_path


def _suggest_channel(state: BusinessCampaignState) -> str:
    """Suggest best outreach channel based on history."""
    if state.total_touches == 0:
        return "whatsapp"
    # Rotate channels
    used = [a.get("channel", "") for a in state.activities]
    priority = ["whatsapp", "phone", "email", "instagram"]
    for ch in priority:
        if ch not in used:
            return ch
    return "whatsapp"  # default back to WhatsApp


def _suggest_next_action(activity_type: str, status: str) -> str:
    """Suggest next action based on current state."""
    if status in ("interested", "responded"):
        return "Agendar reuniao presencial ou call para apresentacao."
    if status == "read":
        return "Enviar follow-up personalizado com case relevante."
    if activity_type == "initial_contact":
        return "Follow-up: verificar recebimento e reforcar proposta de valor."
    if activity_type == "follow_up":
        return "Terceiro toque: oferecer amostra gratis ou visita tecnica."
    if activity_type == "meeting":
        return "Enviar proposta comercial formal."
    if activity_type == "proposal":
        return "Follow-up da proposta: esclarecer duvidas, negociar condicoes."
    return "Avaliar proximo passo baseado no historico."


# --- CLI ---
if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="CRM Campaign Manager for GATO\u00b3")
    ap.add_argument("--crm", default=str(DEFAULT_CRM), help="Path to CRM .md file")
    ap.add_argument("--init", action="store_true", help="Initialize campaign DB from CRM")
    ap.add_argument("--stats", action="store_true", help="Show campaign statistics")
    ap.add_argument("--due", action="store_true", help="Show overdue follow-ups")
    ap.add_argument("--plan", type=int, default=0, help="Generate outreach plan (N businesses)")
    ap.add_argument("--log", nargs=4, metavar=("BIZ_ID", "CHANNEL", "TYPE", "STATUS"),
                     help="Log activity: business_id channel type status")
    ap.add_argument("--export", action="store_true", help="Export campaign report")
    args = ap.parse_args()

    mgr = CampaignManager(args.crm)

    if args.init:
        count = mgr.initialize_from_crm()
        print(f"Initialized {count} new businesses in campaign DB.")
        print(f"Total: {len(mgr.states)} businesses tracked.")
    elif args.log:
        biz_id, channel, atype, status = args.log
        act = mgr.log_activity(biz_id, channel, atype, status)
        print(f"Logged: {channel} {atype} -> {status}")
        if act.next_action:
            print(f"Next: {act.next_action} (by {act.next_action_date[:10]})")
    elif args.due:
        due = mgr.get_due_followups()
        if due:
            print(f"\n{len(due)} overdue follow-ups:")
            for d in due[:20]:
                print(f"  [{d['tier']:>6}] {d['business_name']:<30} overdue {d['overdue_days']}d | {d['suggested_action']}")
        else:
            print("No overdue follow-ups.")
    elif args.plan > 0:
        plan = mgr.generate_outreach_plan(args.plan)
        print(f"\nOutreach plan ({len(plan)} businesses):")
        for p in plan:
            days = f"{p['days_since_contact']}d ago" if p['days_since_contact'] is not None else "never"
            print(f"  [{p['tier']:>6}] {p['business_name']:<30} via {p['suggested_channel']:<10} ({days})")
    elif args.stats:
        stats = mgr.campaign_stats()
        print(json.dumps(stats, ensure_ascii=False, indent=2))
    elif args.export:
        path = mgr.export_report()
        print(f"Report exported to: {path}")
    else:
        ap.print_help()
