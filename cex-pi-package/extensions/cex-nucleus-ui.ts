/**
 * CEX Nucleus UI Extension
 * 
 * Auto-activates on startup:
 * - Sets terminal title to nucleus identity
 * - Replaces footer with nucleus info + sin identity
 * - Colors footer using theme accent
 * 
 * Reads CEX_NUCLEUS env var to determine which nucleus this is.
 */

import type { AssistantMessage } from "@mariozechner/pi-ai";
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { truncateToWidth, visibleWidth } from "@mariozechner/pi-tui";

const NUCLEUS_INFO: Record<string, { sin: string; icon: string; domain: string }> = {
	N01: { sin: "Inveja Analitica", icon: "[+]", domain: "Research" },
	N02: { sin: "Luxuria Criativa", icon: "[*]", domain: "Marketing" },
	N03: { sin: "Soberba Inventiva", icon: "[!]", domain: "Builder" },
	N04: { sin: "Gula por Conhecimento", icon: "[o]", domain: "Knowledge" },
	N05: { sin: "Ira Construtiva", icon: "[X]", domain: "Operations" },
	N06: { sin: "Avareza Estrategica", icon: "[$]", domain: "Commercial" },
	N07: { sin: "Preguica Orquestradora", icon: "[~]", domain: "Orchestrator" },
};

export default function (pi: ExtensionAPI) {
	pi.on("session_start", async (_event, ctx) => {
		const nuc = process.env.CEX_NUCLEUS || "";
		const info = NUCLEUS_INFO[nuc];

		if (!info) return; // Not a CEX nucleus session

		// Set terminal title
		ctx.ui.setTitle(`CEX-${nuc} ${info.sin}`);

		// Set custom footer with nucleus identity
		ctx.ui.setFooter((tui, theme, footerData) => {
			const unsub = footerData.onBranchChange(() => tui.requestRender());

			return {
				dispose: unsub,
				invalidate() {},
				render(width: number): string[] {
					// Token stats
					let input = 0, output = 0, cost = 0;
					for (const e of ctx.sessionManager.getBranch()) {
						if (e.type === "message" && e.message.role === "assistant") {
							const m = e.message as AssistantMessage;
							input += m.usage.input;
							output += m.usage.output;
							cost += m.usage.cost.total;
						}
					}

					const branch = footerData.getGitBranch();
					const fmt = (n: number) => (n < 1000 ? `${n}` : `${(n / 1000).toFixed(1)}k`);

					// Left: nucleus identity
					const nucleusId = theme.fg("accent", `${info.icon} CEX-${nuc} ${info.sin}`);

					// Center: stats
					const stats = theme.fg("dim", `R${fmt(input)} W${fmt(output)} $${cost.toFixed(2)}`);

					// Right: model + branch
					const branchStr = branch ? ` (${branch})` : "";
					const model = ctx.model?.id || "no-model";
					const right = theme.fg("dim", `${model}${branchStr}`);

					// Layout
					const leftW = visibleWidth(nucleusId);
					const rightW = visibleWidth(right);
					const statsW = visibleWidth(stats);
					const padL = " ".repeat(Math.max(1, Math.floor((width - leftW - statsW - rightW) / 2)));
					const padR = " ".repeat(Math.max(1, width - leftW - statsW - rightW - padL.length));

					return [truncateToWidth(nucleusId + padL + stats + padR + right, width)];
				},
			};
		});

		// Status indicator
		ctx.ui.setStatus("cex", `${info.icon} ${nuc} ${info.domain}`);
	});
}
