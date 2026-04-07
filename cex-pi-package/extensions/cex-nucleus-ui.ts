/**
 * CEX Nucleus UI Extension v2
 *
 * Auto-activates when CEX_NUCLEUS env var is set.
 * - Custom footer: identity + context bar + model + branch
 * - Terminal title: CEX-N0X Sin Name
 * - No $ cost (misleading for subscription users)
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

function contextBar(used: number, max: number, barLen: number): string {
	const pct = Math.min(1, used / max);
	const filled = Math.round(pct * barLen);
	const empty = barLen - filled;
	return "=".repeat(filled) + "-".repeat(empty);
}

function fmtTokens(n: number): string {
	if (n < 1000) return `${n}`;
	if (n < 1_000_000) return `${(n / 1000).toFixed(0)}K`;
	return `${(n / 1_000_000).toFixed(1)}M`;
}

export default function (pi: ExtensionAPI) {
	pi.on("session_start", async (_event, ctx) => {
		const nuc = process.env.CEX_NUCLEUS || "";
		const info = NUCLEUS_INFO[nuc];
		if (!info) return;

		// Terminal title
		ctx.ui.setTitle(`CEX-${nuc} ${info.sin}`);

		// Custom footer
		ctx.ui.setFooter((tui, theme, footerData) => {
			const unsub = footerData.onBranchChange(() => tui.requestRender());

			return {
				dispose: unsub,
				invalidate() {},
				render(width: number): string[] {
					// Context usage
					const usage = ctx.getContextUsage();
					const ctxTokens = usage?.tokens || 0;
					const ctxMax = ctx.model?.contextWindow || 1_000_000;
					const pct = ((ctxTokens / ctxMax) * 100).toFixed(1);

					// Git branch
					const branch = footerData.getGitBranch();
					const branchStr = branch ? `(${branch})` : "";

					// Model (short name)
					const modelFull = ctx.model?.id || "no-model";
					const modelShort = modelFull.replace("claude-", "").replace("anthropic/", "");

					// LEFT: nucleus identity
					const left = theme.fg("accent", `${info.icon} ${nuc} ${info.short}`);

					// CENTER: context bar
					const bar = contextBar(ctxTokens, ctxMax, 10);
					const center = theme.fg("dim", `${fmtTokens(ctxTokens)}/${fmtTokens(ctxMax)}`)
						+ " "
						+ theme.fg("accent", "[") + theme.fg("accent", bar) + theme.fg("accent", "]")
						+ " "
						+ theme.fg("dim", `${pct}%`);

					// RIGHT: model + branch
					const right = theme.fg("dim", `${modelShort} ${branchStr}`);

					// Layout with padding
					const lw = visibleWidth(left);
					const cw = visibleWidth(center);
					const rw = visibleWidth(right);
					const totalContent = lw + cw + rw;
					const gap = Math.max(2, Math.floor((width - totalContent) / 2));
					const padL = " ".repeat(gap);
					const padR = " ".repeat(Math.max(1, width - lw - cw - rw - gap));

					return [truncateToWidth(left + padL + center + padR + right, width)];
				},
			};
		});
	});
}
