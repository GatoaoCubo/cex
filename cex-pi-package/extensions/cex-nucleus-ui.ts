/**
 * CEX Nucleus UI Extension v4
 *
 * Auto-activates when CEX_NUCLEUS env var is set.
 * Footer adapts to window width:
 *   Wide (120+): [X] N05 Ira | 6K/1M [==--------] 0.6% | opus-4-6 | ~/GitHub/cex (main)
 *   Grid (80):   [X] N05 Ira | 6K/1M [==------] | opus-4-6 | cex (main)
 *   Narrow (60): [X] N05 Ira | 6K/1M 0.6% | opus-4-6
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { truncateToWidth, visibleWidth } from "@mariozechner/pi-tui";

const NUC: Record<string, { short: string; sector: string; icon: string; sin: string }> = {
	N01: { short: "Inveja", sector: "Research", icon: "[+]", sin: "Inveja Analitica" },
	N02: { short: "Luxuria", sector: "Marketing", icon: "[*]", sin: "Luxuria Criativa" },
	N03: { short: "Soberba", sector: "Builder", icon: "[!]", sin: "Soberba Inventiva" },
	N04: { short: "Gula", sector: "Knowledge", icon: "[o]", sin: "Gula por Conhecimento" },
	N05: { short: "Ira", sector: "Operations", icon: "[X]", sin: "Ira Construtiva" },
	N06: { short: "Avareza", sector: "Commercial", icon: "[$]", sin: "Avareza Estrategica" },
	N07: { short: "Preguica", sector: "Orchestrator", icon: "[~]", sin: "Preguica Orquestradora" },
};

function bar(used: number, max: number, len: number): string {
	const f = Math.round(Math.min(1, used / max) * len);
	return "=".repeat(f) + "-".repeat(len - f);
}

function fmtK(n: number): string {
	if (n < 1000) return `${n}`;
	if (n < 1_000_000) return `${(n / 1000).toFixed(0)}K`;
	return `${(n / 1_000_000).toFixed(1)}M`;
}

function shortPath(cwd: string, maxLen: number): string {
	let p = cwd.replace(/\\/g, "/")
		.replace(/^C:\/Users\/[^/]+\/Documents\//, "~/")
		.replace(/^C:\/Users\/[^/]+\//, "~/");
	if (p.length > maxLen) {
		// Just use last folder name
		const parts = p.split("/");
		p = parts[parts.length - 1] || p;
	}
	return p;
}

export default function (pi: ExtensionAPI) {
	pi.on("session_start", async (_event, ctx) => {
		const nuc = process.env.CEX_NUCLEUS || "";
		const info = NUC[nuc];
		if (!info) return;

		ctx.ui.setTitle(`CEX-${nuc} ${info.sin}`);

		ctx.ui.setFooter((tui, theme, footerData) => {
			const unsub = footerData.onBranchChange(() => tui.requestRender());

			return {
				dispose: unsub,
				invalidate() {},
				render(width: number): string[] {
					const usage = ctx.getContextUsage();
					const tokens = usage?.tokens || 0;
					const max = ctx.model?.contextWindow || 1_000_000;
					const pct = ((tokens / max) * 100).toFixed(1);
					const branch = footerData.getGitBranch();
					const model = (ctx.model?.id || "").replace("claude-", "");
					const sep = theme.fg("dim", " | ");

					// Identity: icon + nucleus + sin + sector
					const id = theme.fg("accent", `${info.icon} ${nuc} ${info.short}`)
						+ theme.fg("dim", ` ${info.sector}`);

					if (width >= 100) {
						// WIDE (full screen): path + bar + pct
						const path = shortPath(ctx.cwd, 25);
						const loc = theme.fg("dim", branch ? `${path} (${branch})` : path);
						const ctx_ = theme.fg("dim", `${fmtK(tokens)}/${fmtK(max)} `)
							+ theme.fg("accent", `[${bar(tokens, max, 10)}]`)
							+ theme.fg("dim", ` ${pct}%`);
						const mod = theme.fg("dim", model);
						return [truncateToWidth(id + sep + ctx_ + sep + mod + sep + loc, width)];
					}

					if (width >= 55) {
						// GRID (~64 cols): token count + wide bar + path
						const folder = ctx.cwd.replace(/\\/g, "/").split("/").pop() || "";
						const loc = theme.fg("dim", branch ? `${folder} (${branch})` : folder);
						const barLen = Math.min(10, Math.max(4, width - 58));
						const ctx_ = theme.fg("dim", `${fmtK(tokens)}/${fmtK(max)} `)
							+ theme.fg("accent", `[${bar(tokens, max, barLen)}]`)
							+ theme.fg("dim", ` ${pct}%`);
						const mod = theme.fg("dim", model);
						return [truncateToWidth(id + sep + ctx_ + sep + mod + sep + loc, width)];
					}

					// NARROW (< 55): minimal
					const ctx_ = theme.fg("dim", `${pct}%`);
					const mod = theme.fg("dim", model);
					return [truncateToWidth(id + sep + ctx_ + sep + mod, width)];
				},
			};
		});
	});
}
