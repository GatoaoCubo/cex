"""
Module 15: Performance Analytics Engine
=========================================
Tracks yield per technique, quality scores, execution time.
Learning system adapts technique weights over time.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from cex_discovery_pipeline.agents.base_agent import AgentResult
from cex_discovery_pipeline.miners.base_miner import MinerResult

logger = logging.getLogger(__name__)

ANALYTICS_DIR = Path(__file__).parent.parent / "output" / "analytics"


@dataclass
class TechniqueMetrics:
    """Performance metrics for a single mining technique."""

    name: str
    total_runs: int = 0
    total_found: int = 0
    total_new: int = 0
    avg_execution_time: float = 0.0
    avg_success_rate: float = 0.0
    avg_quality_score: float = 0.0
    cost_per_discovery: float = 0.0

    @property
    def yield_per_run(self) -> float:
        return self.total_found / max(self.total_runs, 1)

    @property
    def efficiency_score(self) -> float:
        """Combined score: yield * quality / time."""
        if self.avg_execution_time == 0:
            return 0.0
        return (
            self.yield_per_run
            * self.avg_quality_score
            / max(self.avg_execution_time, 1)
        )


@dataclass
class PipelineMetrics:
    """Aggregated pipeline execution metrics."""

    run_id: str = ""
    timestamp: str = ""
    region: str = ""
    niche: str = ""
    total_raw: int = 0
    total_deduplicated: int = 0
    total_validated: int = 0
    total_final: int = 0
    execution_time_seconds: float = 0.0
    technique_metrics: dict[str, TechniqueMetrics] = field(default_factory=dict)
    agent_metrics: dict[str, dict[str, Any]] = field(default_factory=dict)
    duplicate_rate: float = 0.0
    validation_pass_rate: float = 0.0


class AnalyticsEngine:
    """
    Tracks and analyzes pipeline performance.
    Stores history for learning-based optimization.
    """

    def __init__(self, analytics_dir: Path | None = None):
        self._dir = analytics_dir or ANALYTICS_DIR
        self._dir.mkdir(parents=True, exist_ok=True)
        self._history: list[PipelineMetrics] = []
        self._load_history()

    def _load_history(self) -> None:
        history_file = self._dir / "history.json"
        if history_file.exists():
            with open(history_file, encoding="utf-8") as f:
                data = json.load(f)
            for entry in data:
                metrics = PipelineMetrics(**{
                    k: v for k, v in entry.items()
                    if k != "technique_metrics" and k != "agent_metrics"
                })
                self._history.append(metrics)

    def record_run(
        self,
        miner_results: dict[str, MinerResult],
        agent_results: dict[str, AgentResult],
        total_final: int,
        execution_time: float,
        region: str = "",
        niche: str = "",
    ) -> PipelineMetrics:
        """Record a pipeline run for analytics."""
        metrics = PipelineMetrics(
            run_id=f"run_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}",
            timestamp=datetime.now(timezone.utc).isoformat(),
            region=region,
            niche=niche,
            total_final=total_final,
            execution_time_seconds=execution_time,
        )

        # Technique metrics
        total_raw = 0
        for name, mr in miner_results.items():
            total_raw += mr.total_found
            metrics.technique_metrics[name] = TechniqueMetrics(
                name=name,
                total_runs=1,
                total_found=mr.total_found,
                avg_execution_time=mr.execution_time_seconds,
                avg_success_rate=mr.success_rate,
            )
        metrics.total_raw = total_raw

        # Agent metrics
        for name, ar in agent_results.items():
            metrics.agent_metrics[name] = {
                "processed": ar.processed_count,
                "modified": ar.modified_count,
                "rejected": ar.rejected_count,
                "time": ar.execution_time_seconds,
            }
            if name == "deduplicator":
                metrics.total_deduplicated = ar.processed_count - ar.rejected_count
                metrics.duplicate_rate = (
                    ar.rejected_count / max(ar.processed_count, 1)
                )
            elif name == "validator":
                metrics.total_validated = ar.processed_count - ar.rejected_count
                metrics.validation_pass_rate = (
                    (ar.processed_count - ar.rejected_count)
                    / max(ar.processed_count, 1)
                )

        self._history.append(metrics)
        self._save_history()
        self._save_run_report(metrics)

        logger.info(
            "[Analytics] Run %s recorded: %d raw -> %d final (%.1fs)",
            metrics.run_id, metrics.total_raw,
            metrics.total_final, metrics.execution_time_seconds,
        )
        return metrics

    def get_technique_rankings(self) -> list[dict[str, Any]]:
        """
        Rank techniques by efficiency across all historical runs.
        Returns sorted list of technique performance summaries.
        """
        agg: dict[str, TechniqueMetrics] = {}

        for run in self._history:
            for name, tm in run.technique_metrics.items():
                if name not in agg:
                    agg[name] = TechniqueMetrics(name=name)
                a = agg[name]
                a.total_runs += tm.total_runs
                a.total_found += tm.total_found
                a.avg_execution_time = (
                    (a.avg_execution_time * (a.total_runs - 1) + tm.avg_execution_time)
                    / a.total_runs
                )
                a.avg_success_rate = (
                    (a.avg_success_rate * (a.total_runs - 1) + tm.avg_success_rate)
                    / a.total_runs
                )

        rankings = sorted(
            agg.values(),
            key=lambda t: t.efficiency_score,
            reverse=True,
        )
        return [
            {
                "name": t.name,
                "total_runs": t.total_runs,
                "total_found": t.total_found,
                "yield_per_run": round(t.yield_per_run, 1),
                "avg_time_s": round(t.avg_execution_time, 1),
                "avg_success_rate": round(t.avg_success_rate, 3),
                "efficiency_score": round(t.efficiency_score, 4),
            }
            for t in rankings
        ]

    def suggest_weight_updates(self) -> dict[str, float]:
        """
        Based on historical performance, suggest updated technique weights.
        Used by ContextEngine to adapt technique_weights.yaml.
        """
        rankings = self.get_technique_rankings()
        if not rankings:
            return {}

        max_eff = max(r["efficiency_score"] for r in rankings) or 1.0
        return {
            r["name"]: round(r["efficiency_score"] / max_eff, 3)
            for r in rankings
        }

    def get_summary(self) -> dict[str, Any]:
        """Get overall analytics summary."""
        if not self._history:
            return {"total_runs": 0, "message": "No runs recorded yet"}

        total_discovered = sum(r.total_raw for r in self._history)
        total_final = sum(r.total_final for r in self._history)
        avg_time = sum(r.execution_time_seconds for r in self._history) / len(self._history)
        avg_dedup = sum(r.duplicate_rate for r in self._history) / len(self._history)

        return {
            "total_runs": len(self._history),
            "total_discovered": total_discovered,
            "total_final": total_final,
            "avg_execution_time_s": round(avg_time, 1),
            "avg_duplicate_rate": round(avg_dedup, 3),
            "avg_yield_per_run": round(total_final / len(self._history), 1),
            "technique_rankings": self.get_technique_rankings(),
        }

    def _save_history(self) -> None:
        history_file = self._dir / "history.json"
        data = []
        for m in self._history:
            entry = {
                "run_id": m.run_id,
                "timestamp": m.timestamp,
                "region": m.region,
                "niche": m.niche,
                "total_raw": m.total_raw,
                "total_final": m.total_final,
                "execution_time_seconds": m.execution_time_seconds,
                "duplicate_rate": m.duplicate_rate,
                "validation_pass_rate": m.validation_pass_rate,
            }
            data.append(entry)
        with open(history_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _save_run_report(self, metrics: PipelineMetrics) -> None:
        report_file = self._dir / f"{metrics.run_id}.json"
        report = {
            "run_id": metrics.run_id,
            "timestamp": metrics.timestamp,
            "region": metrics.region,
            "niche": metrics.niche,
            "total_raw": metrics.total_raw,
            "total_deduplicated": metrics.total_deduplicated,
            "total_validated": metrics.total_validated,
            "total_final": metrics.total_final,
            "execution_time_seconds": metrics.execution_time_seconds,
            "duplicate_rate": metrics.duplicate_rate,
            "validation_pass_rate": metrics.validation_pass_rate,
            "techniques": {
                name: {
                    "found": tm.total_found,
                    "time": tm.avg_execution_time,
                    "success_rate": tm.avg_success_rate,
                }
                for name, tm in metrics.technique_metrics.items()
            },
            "agents": metrics.agent_metrics,
        }
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
