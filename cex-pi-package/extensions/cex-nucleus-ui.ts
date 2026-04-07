/**
 * CEX Nucleus UI Extension v3
 *
 * Auto-activates when CEX_NUCLEUS env var is set.
 * Footer: identity | task | context bar | model | path (branch)
 */

import type { AssistantMessage } from "@mariozechner/pi-ai";
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { truncateToWidth, visibleWidth } from "@mariozechner/pi-tui";

const NUCLEUS_INFO: Record<string, { sin: string; short: string; icon: string }> = {
	N01: { sin: "Inveja Analitica", short: "Inveja", icon: "[+]" },
	N02: { sin: "Luxuria Criativa", short: "Luxuria", icon: "[*]" },
	N03: { sin: "Soberba Inventiva", short: "Soberba", icon: "[!]" },
	N04: { sin: "Gula por Conhecimento", short: "Gula", icon: "[o]" },
	N05: { sin: "Ira Construtiva", short: "Ira", icon: "[X]" },
	N06: { sin: "Avareza Estrategica", short: "Avareza", icon: "[$]" },
	N07: { sin: "Preguica Orquestradora", short: "Preguica", icon: "[~]" },
};

function contextBar(used: number, max: number, len: number): string {
	const pct = Math.min(1, used / max);
	const filled = Math.round(pct * len);
	return "=".repeat(filled) + "-".repeat(len - filled);
}

function fmtK(n: number): string {
	if (n < 1000) return `${n}`;
	if (n < 1_000_000) return `${(n / 1000).toFixed(0)}K`;
	return `${(n / 1_000_000).toFixed(1)}M`;
}

function getActiveTask(): string {
	// Read handoff filename to show what task is active
	const fs = require("fs");
	const nuc = (process.env.CEX_NUCLEUS || "").toLowerCase();
	const handoff = `${process.cwd()}/.cex/runtime/handoffs/${nuc}_task.md`;
	try {
		if (fs.existsSync(handoff)) {
			const text = fs.readFileSync(handoff, "utf-8").slice(0, 300);
			// Extract task from frontmatter
			const match = text.match(/task:\s*(.+)/);
			if (match) return match[1].trim().slice(0, 20);
			// Or first heading
			const heading = text.match(/^#\s+(.+)/m);
			if (heading) return heading[1].trim().slice(0, 20);
		}
	} catch {}
	return "idle";
}

function shortPath(cwd: string): string {
	// C:\Users\PC\Documents\GitHub\cex -> ~/GitHub/cex
	return cwd
		.replace(/\\/g, "/")
		.replace(/^C:\/Users\/[^/]+\/Documents\//, "~/")
		.replace(/^C:\/Users\/[^/]+\//, "~/");
}

export default function (pi: ExtensionAPI) {
	pi.on("session_start", async (_event, ctx) => {
		const nuc = process.env.CEX_NUCLEUS || "";
		const info = NUCLEUS_INFO[nuc];
		if (!info) return;

		ctx.ui.setTitle(`CEX-${nuc} ${info.sin}`);

		ctx.ui.setFooter((tui, theme, footerData) => {
			const unsub = footerData.onBranchChange(() => tui.requestRender());

			return {
				dispose: unsub,
				invalidate() {},
				render(width: number): string[] {
					// Context
					const usage = ctx.getContextUsage();
					const tokens = usage?.tokens || 0;
					const max = ctx.model?.contextWindow || 1_000_000;
					const pct = ((tokens / max) * 100).toFixed(1);

					// Git + path
					const branch = footerData.getGitBranch();
					const path = shortPath(ctx.cwd);
					const pathBranch = branch ? `${path} (${branch})` : path;

					// Model
					const model = (ctx.model?.id || "no-model").replace("claude-", "");

					// Task
					const task = getActiveTask();

					// Build segments
					const seg1 = theme.fg("accent", `${info.icon} ${nuc} ${info.short}`);
					const seg2 = theme.fg("dim", `task:`) + theme.fg("accent", task);
					const seg3 = theme.fg("dim", `${fmtK(tokens)}/${fmtK(max)} `)
						+ theme.fg("accent", `[${contextBar(tokens, max, 10)}]`)
						+ theme.fg("dim", ` ${pct}%`);
					const seg4 = theme.fg("dim", model);
					const seg5 = theme.fg("dim", pathBranch);

					// Layout: fill gaps evenly
					const sep = theme.fg("dim", " | ");
					const sepW = visibleWidth(sep);
					const parts = [seg1, seg2, seg3, seg4, seg5];
					const partsW = parts.reduce((a, p) => a + visibleWidth(p), 0);
					const totalSepW = (parts.length - 1) * sepW;
					const content = parts.join(sep);

					if (partsW + totalSepW <= width) {
						// Fits -- pad to full width
						const pad = " ".repeat(Math.max(0, width - partsW - totalSepW));
						return [truncateToWidth(content + pad, width)];
					}
					// Too wide -- truncate
					return [truncateToWidth(content, width)];
				},
			};
		});
	});
}
