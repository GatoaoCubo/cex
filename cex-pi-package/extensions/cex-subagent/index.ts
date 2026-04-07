/**
 * CEX Subagent Extension — Delegate tasks to nucleus agents
 *
 * Spawns isolated `pi` processes for each nucleus invocation.
 * Each agent gets its own context window, tools, and model config.
 *
 * Modes:
 *   - Single: { agent: "n03-builder", task: "build a KC for routing" }
 *   - Parallel: { tasks: [{ agent: "n01-analyst", task: "..." }, ...] }
 *   - Chain: { chain: [{ agent: "n01-analyst", task: "research {previous}" }, ...] }
 *
 * CEX defaults:
 *   - agentScope: "both" (project .pi/agents/ + user ~/.pi/agent/agents/)
 *   - confirmProjectAgents: false (CEX project agents are trusted)
 *
 * Adapted from pi's subagent example with CEX nucleus identity.
 */

import { spawn } from "node:child_process";
import * as fs from "node:fs";
import * as os from "node:os";
import * as path from "node:path";
import type { AgentToolResult } from "@mariozechner/pi-agent-core";
import type { Message } from "@mariozechner/pi-ai";
import { StringEnum } from "@mariozechner/pi-ai";
import { type ExtensionAPI, getMarkdownTheme } from "@mariozechner/pi-coding-agent";
import { Container, Markdown, Spacer, Text } from "@mariozechner/pi-tui";
import { Type } from "@sinclair/typebox";
import { type AgentConfig, type AgentScope, discoverAgents } from "./agents.js";

// ── Limits ──────────────────────────────────────────────
const MAX_PARALLEL_TASKS = 8;
const MAX_CONCURRENCY = 4;
const COLLAPSED_ITEM_COUNT = 10;

// ── Nucleus identity (for rendering) ────────────────────
const NUC_ICONS: Record<string, string> = {
	"n01-analyst": "◆",
	"n02-copywriter": "♥",
	"n03-builder": "★",
	"n04-librarian": "◉",
	"n05-operator": "⚔",
	"n06-strategist": "$",
};

// ── Formatting helpers ──────────────────────────────────
function fmtTokens(n: number): string {
	if (n < 1000) return n.toString();
	if (n < 10000) return `${(n / 1000).toFixed(1)}k`;
	if (n < 1_000_000) return `${Math.round(n / 1000)}k`;
	return `${(n / 1_000_000).toFixed(1)}M`;
}

function fmtUsage(
	usage: { input: number; output: number; cacheRead: number; cacheWrite: number; cost: number; contextTokens?: number; turns?: number },
	model?: string,
): string {
	const p: string[] = [];
	if (usage.turns) p.push(`${usage.turns} turn${usage.turns > 1 ? "s" : ""}`);
	if (usage.input) p.push(`↑${fmtTokens(usage.input)}`);
	if (usage.output) p.push(`↓${fmtTokens(usage.output)}`);
	if (usage.cacheRead) p.push(`R${fmtTokens(usage.cacheRead)}`);
	if (usage.cacheWrite) p.push(`W${fmtTokens(usage.cacheWrite)}`);
	if (usage.cost) p.push(`$${usage.cost.toFixed(4)}`);
	if (usage.contextTokens && usage.contextTokens > 0) p.push(`ctx:${fmtTokens(usage.contextTokens)}`);
	if (model) p.push(model);
	return p.join(" ");
}

function fmtToolCall(
	toolName: string,
	args: Record<string, unknown>,
	fg: (color: any, text: string) => string,
): string {
	const home = os.homedir();
	const shorten = (p: string) => (p.startsWith(home) ? `~${p.slice(home.length)}` : p);

	switch (toolName) {
		case "bash": {
			const cmd = (args.command as string) || "...";
			return fg("muted", "$ ") + fg("toolOutput", cmd.length > 60 ? `${cmd.slice(0, 60)}...` : cmd);
		}
		case "read": {
			const raw = (args.file_path || args.path || "...") as string;
			let text = fg("accent", shorten(raw));
			const offset = args.offset as number | undefined;
			const limit = args.limit as number | undefined;
			if (offset !== undefined || limit !== undefined) {
				const start = offset ?? 1;
				const end = limit !== undefined ? start + limit - 1 : "";
				text += fg("warning", `:${start}${end ? `-${end}` : ""}`);
			}
			return fg("muted", "read ") + text;
		}
		case "write": {
			const raw = (args.file_path || args.path || "...") as string;
			const lines = ((args.content || "") as string).split("\n").length;
			let text = fg("muted", "write ") + fg("accent", shorten(raw));
			if (lines > 1) text += fg("dim", ` (${lines} lines)`);
			return text;
		}
		case "edit":
			return fg("muted", "edit ") + fg("accent", shorten((args.file_path || args.path || "...") as string));
		case "ls":
			return fg("muted", "ls ") + fg("accent", shorten((args.path || ".") as string));
		case "find":
			return fg("muted", "find ") + fg("accent", (args.pattern || "*") as string) + fg("dim", ` in ${shorten((args.path || ".") as string)}`);
		case "grep":
			return fg("muted", "grep ") + fg("accent", `/${(args.pattern || "") as string}/`) + fg("dim", ` in ${shorten((args.path || ".") as string)}`);
		default: {
			const s = JSON.stringify(args);
			return fg("accent", toolName) + fg("dim", ` ${s.length > 50 ? s.slice(0, 50) + "..." : s}`);
		}
	}
}

// ── Types ───────────────────────────────────────────────
interface UsageStats {
	input: number; output: number; cacheRead: number; cacheWrite: number;
	cost: number; contextTokens: number; turns: number;
}

interface SingleResult {
	agent: string;
	agentSource: "user" | "project" | "unknown";
	task: string;
	exitCode: number;
	messages: Message[];
	stderr: string;
	usage: UsageStats;
	model?: string;
	stopReason?: string;
	errorMessage?: string;
	step?: number;
}

interface SubagentDetails {
	mode: "single" | "parallel" | "chain";
	agentScope: AgentScope;
	projectAgentsDir: string | null;
	results: SingleResult[];
}

type DisplayItem = { type: "text"; text: string } | { type: "toolCall"; name: string; args: Record<string, any> };

function getFinalOutput(messages: Message[]): string {
	for (let i = messages.length - 1; i >= 0; i--) {
		const msg = messages[i];
		if (msg.role === "assistant") {
			for (const part of msg.content) {
				if (part.type === "text") return part.text;
			}
		}
	}
	return "";
}

function getDisplayItems(messages: Message[]): DisplayItem[] {
	const items: DisplayItem[] = [];
	for (const msg of messages) {
		if (msg.role === "assistant") {
			for (const part of msg.content) {
				if (part.type === "text") items.push({ type: "text", text: part.text });
				else if (part.type === "toolCall") items.push({ type: "toolCall", name: part.name, args: part.arguments });
			}
		}
	}
	return items;
}

// ── Concurrency helper ──────────────────────────────────
async function mapConcurrent<TIn, TOut>(items: TIn[], concurrency: number, fn: (item: TIn, i: number) => Promise<TOut>): Promise<TOut[]> {
	if (items.length === 0) return [];
	const limit = Math.max(1, Math.min(concurrency, items.length));
	const results: TOut[] = new Array(items.length);
	let next = 0;
	await Promise.all(
		new Array(limit).fill(null).map(async () => {
			while (true) {
				const idx = next++;
				if (idx >= items.length) return;
				results[idx] = await fn(items[idx], idx);
			}
		}),
	);
	return results;
}

// ── Temp file for system prompt ─────────────────────────
function writeTmpPrompt(name: string, prompt: string): { dir: string; file: string } {
	const dir = fs.mkdtempSync(path.join(os.tmpdir(), "cex-subagent-"));
	const safe = name.replace(/[^\w.-]+/g, "_");
	const file = path.join(dir, `prompt-${safe}.md`);
	fs.writeFileSync(file, prompt, { encoding: "utf-8", mode: 0o600 });
	return { dir, file };
}

// ── Single agent runner ─────────────────────────────────
type OnUpdate = (partial: AgentToolResult<SubagentDetails>) => void;

async function runAgent(
	cwd: string,
	agents: AgentConfig[],
	agentName: string,
	task: string,
	taskCwd: string | undefined,
	step: number | undefined,
	signal: AbortSignal | undefined,
	onUpdate: OnUpdate | undefined,
	mkDetails: (results: SingleResult[]) => SubagentDetails,
): Promise<SingleResult> {
	const agent = agents.find((a) => a.name === agentName);
	if (!agent) {
		const available = agents.map((a) => `"${a.name}"`).join(", ") || "none";
		return {
			agent: agentName, agentSource: "unknown", task, exitCode: 1,
			messages: [], stderr: `Unknown agent: "${agentName}". Available: ${available}.`,
			usage: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, cost: 0, contextTokens: 0, turns: 0 },
			step,
		};
	}

	const args: string[] = ["--mode", "json", "-p", "--no-session"];
	if (agent.model) args.push("--model", agent.model);
	if (agent.tools?.length) args.push("--tools", agent.tools.join(","));

	let tmpDir: string | null = null;
	let tmpFile: string | null = null;

	const result: SingleResult = {
		agent: agentName, agentSource: agent.source, task, exitCode: 0,
		messages: [], stderr: "",
		usage: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, cost: 0, contextTokens: 0, turns: 0 },
		model: agent.model, step,
	};

	const emit = () => {
		onUpdate?.({
			content: [{ type: "text", text: getFinalOutput(result.messages) || "(running...)" }],
			details: mkDetails([result]),
		});
	};

	try {
		if (agent.systemPrompt.trim()) {
			const tmp = writeTmpPrompt(agent.name, agent.systemPrompt);
			tmpDir = tmp.dir;
			tmpFile = tmp.file;
			args.push("--append-system-prompt", tmpFile);
		}

		args.push(`Task: ${task}`);
		let aborted = false;

		const exitCode = await new Promise<number>((resolve) => {
			const proc = spawn("pi", args, { cwd: taskCwd ?? cwd, shell: false, stdio: ["ignore", "pipe", "pipe"] });
			let buf = "";

			const processLine = (line: string) => {
				if (!line.trim()) return;
				let ev: any;
				try { ev = JSON.parse(line); } catch { return; }

				if (ev.type === "message_end" && ev.message) {
					const msg = ev.message as Message;
					result.messages.push(msg);
					if (msg.role === "assistant") {
						result.usage.turns++;
						const u = msg.usage;
						if (u) {
							result.usage.input += u.input || 0;
							result.usage.output += u.output || 0;
							result.usage.cacheRead += u.cacheRead || 0;
							result.usage.cacheWrite += u.cacheWrite || 0;
							result.usage.cost += u.cost?.total || 0;
							result.usage.contextTokens = u.totalTokens || 0;
						}
						if (!result.model && msg.model) result.model = msg.model;
						if (msg.stopReason) result.stopReason = msg.stopReason;
						if (msg.errorMessage) result.errorMessage = msg.errorMessage;
					}
					emit();
				}
				if (ev.type === "tool_result_end" && ev.message) {
					result.messages.push(ev.message as Message);
					emit();
				}
			};

			proc.stdout.on("data", (data) => {
				buf += data.toString();
				const lines = buf.split("\n");
				buf = lines.pop() || "";
				for (const l of lines) processLine(l);
			});
			proc.stderr.on("data", (data) => { result.stderr += data.toString(); });
			proc.on("close", (code) => { if (buf.trim()) processLine(buf); resolve(code ?? 0); });
			proc.on("error", () => resolve(1));

			if (signal) {
				const kill = () => {
					aborted = true;
					proc.kill("SIGTERM");
					setTimeout(() => { if (!proc.killed) proc.kill("SIGKILL"); }, 5000);
				};
				if (signal.aborted) kill();
				else signal.addEventListener("abort", kill, { once: true });
			}
		});

		result.exitCode = exitCode;
		if (aborted) throw new Error("Subagent aborted");
		return result;
	} finally {
		if (tmpFile) try { fs.unlinkSync(tmpFile); } catch { /* */ }
		if (tmpDir) try { fs.rmdirSync(tmpDir); } catch { /* */ }
	}
}

// ── Schema ──────────────────────────────────────────────
const TaskItem = Type.Object({
	agent: Type.String({ description: "Agent name (e.g. n01-analyst, n03-builder)" }),
	task: Type.String({ description: "Task to delegate" }),
	cwd: Type.Optional(Type.String({ description: "Working directory override" })),
});

const ChainItem = Type.Object({
	agent: Type.String({ description: "Agent name" }),
	task: Type.String({ description: "Task with optional {previous} placeholder" }),
	cwd: Type.Optional(Type.String({ description: "Working directory override" })),
});

const Params = Type.Object({
	agent: Type.Optional(Type.String({ description: "Agent name for single mode" })),
	task: Type.Optional(Type.String({ description: "Task for single mode" })),
	tasks: Type.Optional(Type.Array(TaskItem, { description: "Array of {agent, task} for parallel execution" })),
	chain: Type.Optional(Type.Array(ChainItem, { description: "Sequential steps with {previous} placeholder" })),
	agentScope: Type.Optional(StringEnum(["user", "project", "both"] as const, {
		description: 'Agent scope. Default: "both" (CEX agents + user agents).',
		default: "both",
	})),
	cwd: Type.Optional(Type.String({ description: "Working directory (single mode)" })),
});

// ── Extension entry ─────────────────────────────────────
export default function (pi: ExtensionAPI) {
	pi.registerTool({
		name: "subagent",
		label: "CEX Subagent",
		description: [
			"Delegate tasks to CEX nucleus agents with isolated context.",
			"Available agents: n01-analyst (research), n02-copywriter (marketing), n03-builder (artifacts),",
			"n04-librarian (knowledge), n05-operator (code/tests), n06-strategist (monetization).",
			"Modes: single (agent+task), parallel (tasks array), chain (sequential with {previous}).",
		].join(" "),
		promptSnippet: "Delegate tasks to specialized CEX nucleus agents (n01-n06) with isolated context windows",
		promptGuidelines: [
			"Use subagent for tasks that benefit from isolated context or nucleus specialization.",
			"Chain mode: n01-analyst scouts → n03-builder constructs → n05-operator validates.",
			"Parallel mode: dispatch independent tasks to multiple nuclei simultaneously (max 8, 4 concurrent).",
			"Each nucleus has a sin-driven lens: N01=Envy(research), N02=Lust(copy), N03=Pride(build), N04=Gluttony(docs), N05=Wrath(ops), N06=Greed(strategy).",
		],
		parameters: Params,

		async execute(_id, params, signal, onUpdate, ctx) {
			const scope: AgentScope = params.agentScope ?? "both";
			const discovery = discoverAgents(ctx.cwd, scope);
			const agents = discovery.agents;

			const hasChain = (params.chain?.length ?? 0) > 0;
			const hasTasks = (params.tasks?.length ?? 0) > 0;
			const hasSingle = Boolean(params.agent && params.task);
			const modeCount = Number(hasChain) + Number(hasTasks) + Number(hasSingle);

			const mkDetails = (mode: "single" | "parallel" | "chain") => (results: SingleResult[]): SubagentDetails => ({
				mode, agentScope: scope, projectAgentsDir: discovery.projectAgentsDir, results,
			});

			if (modeCount !== 1) {
				const available = agents.map((a) => `${a.name} (${a.source})`).join(", ") || "none";
				return {
					content: [{ type: "text", text: `Provide exactly one mode. Available agents: ${available}` }],
					details: mkDetails("single")([]),
				};
			}

			// ── Chain mode ──────────────────────────────
			if (params.chain && params.chain.length > 0) {
				const results: SingleResult[] = [];
				let prev = "";

				for (let i = 0; i < params.chain.length; i++) {
					const step = params.chain[i];
					const taskText = step.task.replace(/\{previous\}/g, prev);

					const chainUpdate: OnUpdate | undefined = onUpdate
						? (partial) => {
							const cur = partial.details?.results[0];
							if (cur) onUpdate({ content: partial.content, details: mkDetails("chain")([...results, cur]) });
						}
						: undefined;

					const r = await runAgent(ctx.cwd, agents, step.agent, taskText, step.cwd, i + 1, signal, chainUpdate, mkDetails("chain"));
					results.push(r);

					const isErr = r.exitCode !== 0 || r.stopReason === "error" || r.stopReason === "aborted";
					if (isErr) {
						const msg = r.errorMessage || r.stderr || getFinalOutput(r.messages) || "(no output)";
						return { content: [{ type: "text", text: `Chain stopped at step ${i + 1} (${step.agent}): ${msg}` }], details: mkDetails("chain")(results), isError: true };
					}
					prev = getFinalOutput(r.messages);
				}
				return {
					content: [{ type: "text", text: getFinalOutput(results[results.length - 1].messages) || "(no output)" }],
					details: mkDetails("chain")(results),
				};
			}

			// ── Parallel mode ───────────────────────────
			if (params.tasks && params.tasks.length > 0) {
				if (params.tasks.length > MAX_PARALLEL_TASKS) {
					return { content: [{ type: "text", text: `Too many tasks (${params.tasks.length}). Max: ${MAX_PARALLEL_TASKS}.` }], details: mkDetails("parallel")([]) };
				}

				const all: SingleResult[] = params.tasks.map((t) => ({
					agent: t.agent, agentSource: "unknown" as const, task: t.task, exitCode: -1,
					messages: [], stderr: "",
					usage: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, cost: 0, contextTokens: 0, turns: 0 },
				}));

				const emitAll = () => {
					if (!onUpdate) return;
					const running = all.filter((r) => r.exitCode === -1).length;
					const done = all.filter((r) => r.exitCode !== -1).length;
					onUpdate({
						content: [{ type: "text", text: `Parallel: ${done}/${all.length} done, ${running} running...` }],
						details: mkDetails("parallel")([...all]),
					});
				};

				const results = await mapConcurrent(params.tasks, MAX_CONCURRENCY, async (t, idx) => {
					const r = await runAgent(ctx.cwd, agents, t.agent, t.task, t.cwd, undefined, signal,
						(partial) => { if (partial.details?.results[0]) { all[idx] = partial.details.results[0]; emitAll(); } },
						mkDetails("parallel"),
					);
					all[idx] = r;
					emitAll();
					return r;
				});

				const ok = results.filter((r) => r.exitCode === 0).length;
				const summaries = results.map((r) => {
					const out = getFinalOutput(r.messages);
					const preview = out.slice(0, 100) + (out.length > 100 ? "..." : "");
					return `[${r.agent}] ${r.exitCode === 0 ? "✓" : "✗"}: ${preview || "(no output)"}`;
				});
				return {
					content: [{ type: "text", text: `Parallel: ${ok}/${results.length} succeeded\n\n${summaries.join("\n\n")}` }],
					details: mkDetails("parallel")(results),
				};
			}

			// ── Single mode ─────────────────────────────
			if (params.agent && params.task) {
				const r = await runAgent(ctx.cwd, agents, params.agent, params.task, params.cwd, undefined, signal, onUpdate, mkDetails("single"));
				const isErr = r.exitCode !== 0 || r.stopReason === "error" || r.stopReason === "aborted";
				if (isErr) {
					const msg = r.errorMessage || r.stderr || getFinalOutput(r.messages) || "(no output)";
					return { content: [{ type: "text", text: `Agent ${r.stopReason || "failed"}: ${msg}` }], details: mkDetails("single")([r]), isError: true };
				}
				return {
					content: [{ type: "text", text: getFinalOutput(r.messages) || "(no output)" }],
					details: mkDetails("single")([r]),
				};
			}

			const available = agents.map((a) => `${a.name} (${a.source})`).join(", ") || "none";
			return { content: [{ type: "text", text: `Invalid params. Available agents: ${available}` }], details: mkDetails("single")([]) };
		},

		// ── Render: tool call ───────────────────────────
		renderCall(args, theme) {
			const scope: AgentScope = args.agentScope ?? "both";

			if (args.chain?.length) {
				let t = theme.fg("toolTitle", theme.bold("subagent "))
					+ theme.fg("accent", `chain (${args.chain.length} steps)`)
					+ theme.fg("muted", ` [${scope}]`);
				for (let i = 0; i < Math.min(args.chain.length, 3); i++) {
					const s = args.chain[i];
					const icon = NUC_ICONS[s.agent] || "·";
					const clean = s.task.replace(/\{previous\}/g, "").trim();
					const preview = clean.length > 40 ? `${clean.slice(0, 40)}...` : clean;
					t += `\n  ${theme.fg("muted", `${i + 1}.`)} ${theme.fg("accent", `${icon} ${s.agent}`)}${theme.fg("dim", ` ${preview}`)}`;
				}
				if (args.chain.length > 3) t += `\n  ${theme.fg("muted", `... +${args.chain.length - 3} more`)}`;
				return new Text(t, 0, 0);
			}

			if (args.tasks?.length) {
				let t = theme.fg("toolTitle", theme.bold("subagent "))
					+ theme.fg("accent", `parallel (${args.tasks.length} tasks)`)
					+ theme.fg("muted", ` [${scope}]`);
				for (const task of args.tasks.slice(0, 3)) {
					const icon = NUC_ICONS[task.agent] || "·";
					const preview = task.task.length > 40 ? `${task.task.slice(0, 40)}...` : task.task;
					t += `\n  ${theme.fg("accent", `${icon} ${task.agent}`)}${theme.fg("dim", ` ${preview}`)}`;
				}
				if (args.tasks.length > 3) t += `\n  ${theme.fg("muted", `... +${args.tasks.length - 3} more`)}`;
				return new Text(t, 0, 0);
			}

			const name = args.agent || "...";
			const icon = NUC_ICONS[name] || "·";
			const preview = args.task ? (args.task.length > 60 ? `${args.task.slice(0, 60)}...` : args.task) : "...";
			let t = theme.fg("toolTitle", theme.bold("subagent "))
				+ theme.fg("accent", `${icon} ${name}`)
				+ theme.fg("muted", ` [${scope}]`);
			t += `\n  ${theme.fg("dim", preview)}`;
			return new Text(t, 0, 0);
		},

		// ── Render: result ──────────────────────────────
		renderResult(result, { expanded }, theme) {
			const details = result.details as SubagentDetails | undefined;
			if (!details?.results.length) {
				const t = result.content[0];
				return new Text(t?.type === "text" ? t.text : "(no output)", 0, 0);
			}

			const mdTheme = getMarkdownTheme();
			const fg = theme.fg.bind(theme);

			const renderItems = (items: DisplayItem[], limit?: number) => {
				const show = limit ? items.slice(-limit) : items;
				const skip = limit && items.length > limit ? items.length - limit : 0;
				let t = "";
				if (skip > 0) t += fg("muted", `... ${skip} earlier items\n`);
				for (const item of show) {
					if (item.type === "text") {
						const text = expanded ? item.text : item.text.split("\n").slice(0, 3).join("\n");
						t += `${fg("toolOutput", text)}\n`;
					} else {
						t += `${fg("muted", "→ ") + fmtToolCall(item.name, item.args, fg)}\n`;
					}
				}
				return t.trimEnd();
			};

			const aggUsage = (rs: SingleResult[]) => {
				const tot = { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, cost: 0, turns: 0 };
				for (const r of rs) {
					tot.input += r.usage.input; tot.output += r.usage.output;
					tot.cacheRead += r.usage.cacheRead; tot.cacheWrite += r.usage.cacheWrite;
					tot.cost += r.usage.cost; tot.turns += r.usage.turns;
				}
				return tot;
			};

			// ── Single result ───────────────────────────
			if (details.mode === "single" && details.results.length === 1) {
				const r = details.results[0];
				const err = r.exitCode !== 0 || r.stopReason === "error" || r.stopReason === "aborted";
				const icon = err ? fg("error", "✗") : fg("success", "✓");
				const nucIcon = NUC_ICONS[r.agent] || "";
				const items = getDisplayItems(r.messages);
				const final = getFinalOutput(r.messages);

				if (expanded) {
					const c = new Container();
					let hdr = `${icon} ${fg("toolTitle", theme.bold(`${nucIcon} ${r.agent}`))}${fg("muted", ` (${r.agentSource})`)}`;
					if (err && r.stopReason) hdr += ` ${fg("error", `[${r.stopReason}]`)}`;
					c.addChild(new Text(hdr, 0, 0));
					if (err && r.errorMessage) c.addChild(new Text(fg("error", `Error: ${r.errorMessage}`), 0, 0));
					c.addChild(new Spacer(1));
					c.addChild(new Text(fg("muted", "─── Task ───"), 0, 0));
					c.addChild(new Text(fg("dim", r.task), 0, 0));
					c.addChild(new Spacer(1));
					c.addChild(new Text(fg("muted", "─── Output ───"), 0, 0));
					if (!items.length && !final) {
						c.addChild(new Text(fg("muted", "(no output)"), 0, 0));
					} else {
						for (const item of items) {
							if (item.type === "toolCall") c.addChild(new Text(fg("muted", "→ ") + fmtToolCall(item.name, item.args, fg), 0, 0));
						}
						if (final) { c.addChild(new Spacer(1)); c.addChild(new Markdown(final.trim(), 0, 0, mdTheme)); }
					}
					const u = fmtUsage(r.usage, r.model);
					if (u) { c.addChild(new Spacer(1)); c.addChild(new Text(fg("dim", u), 0, 0)); }
					return c;
				}

				let t = `${icon} ${fg("toolTitle", theme.bold(`${nucIcon} ${r.agent}`))}${fg("muted", ` (${r.agentSource})`)}`;
				if (err && r.stopReason) t += ` ${fg("error", `[${r.stopReason}]`)}`;
				if (err && r.errorMessage) t += `\n${fg("error", `Error: ${r.errorMessage}`)}`;
				else if (!items.length) t += `\n${fg("muted", "(no output)")}`;
				else {
					t += `\n${renderItems(items, COLLAPSED_ITEM_COUNT)}`;
					if (items.length > COLLAPSED_ITEM_COUNT) t += `\n${fg("muted", "(Ctrl+O to expand)")}`;
				}
				const u = fmtUsage(r.usage, r.model);
				if (u) t += `\n${fg("dim", u)}`;
				return new Text(t, 0, 0);
			}

			// ── Chain result ────────────────────────────
			if (details.mode === "chain") {
				const ok = details.results.filter((r) => r.exitCode === 0).length;
				const icon = ok === details.results.length ? fg("success", "✓") : fg("error", "✗");

				if (expanded) {
					const c = new Container();
					c.addChild(new Text(`${icon} ${fg("toolTitle", theme.bold("chain "))}${fg("accent", `${ok}/${details.results.length} steps`)}`, 0, 0));
					for (const r of details.results) {
						const rIcon = r.exitCode === 0 ? fg("success", "✓") : fg("error", "✗");
						const nucIcon = NUC_ICONS[r.agent] || "";
						c.addChild(new Spacer(1));
						c.addChild(new Text(`${fg("muted", `─── Step ${r.step}: `)}${fg("accent", `${nucIcon} ${r.agent}`)} ${rIcon}`, 0, 0));
						c.addChild(new Text(fg("muted", "Task: ") + fg("dim", r.task), 0, 0));
						for (const item of getDisplayItems(r.messages)) {
							if (item.type === "toolCall") c.addChild(new Text(fg("muted", "→ ") + fmtToolCall(item.name, item.args, fg), 0, 0));
						}
						const final = getFinalOutput(r.messages);
						if (final) { c.addChild(new Spacer(1)); c.addChild(new Markdown(final.trim(), 0, 0, mdTheme)); }
						const su = fmtUsage(r.usage, r.model);
						if (su) c.addChild(new Text(fg("dim", su), 0, 0));
					}
					const tu = fmtUsage(aggUsage(details.results));
					if (tu) { c.addChild(new Spacer(1)); c.addChild(new Text(fg("dim", `Total: ${tu}`), 0, 0)); }
					return c;
				}

				let t = `${icon} ${fg("toolTitle", theme.bold("chain "))}${fg("accent", `${ok}/${details.results.length} steps`)}`;
				for (const r of details.results) {
					const rIcon = r.exitCode === 0 ? fg("success", "✓") : fg("error", "✗");
					const nucIcon = NUC_ICONS[r.agent] || "";
					t += `\n\n${fg("muted", `─── Step ${r.step}: `)}${fg("accent", `${nucIcon} ${r.agent}`)} ${rIcon}`;
					const items = getDisplayItems(r.messages);
					t += items.length ? `\n${renderItems(items, 5)}` : `\n${fg("muted", "(no output)")}`;
				}
				const tu = fmtUsage(aggUsage(details.results));
				if (tu) t += `\n\n${fg("dim", `Total: ${tu}`)}`;
				t += `\n${fg("muted", "(Ctrl+O to expand)")}`;
				return new Text(t, 0, 0);
			}

			// ── Parallel result ─────────────────────────
			if (details.mode === "parallel") {
				const running = details.results.filter((r) => r.exitCode === -1).length;
				const ok = details.results.filter((r) => r.exitCode === 0).length;
				const fail = details.results.filter((r) => r.exitCode > 0).length;
				const live = running > 0;
				const icon = live ? fg("warning", "⏳") : fail > 0 ? fg("warning", "◐") : fg("success", "✓");
				const status = live
					? `${ok + fail}/${details.results.length} done, ${running} running`
					: `${ok}/${details.results.length} tasks`;

				if (expanded && !live) {
					const c = new Container();
					c.addChild(new Text(`${icon} ${fg("toolTitle", theme.bold("parallel "))}${fg("accent", status)}`, 0, 0));
					for (const r of details.results) {
						const rIcon = r.exitCode === 0 ? fg("success", "✓") : fg("error", "✗");
						const nucIcon = NUC_ICONS[r.agent] || "";
						c.addChild(new Spacer(1));
						c.addChild(new Text(`${fg("muted", "─── ")}${fg("accent", `${nucIcon} ${r.agent}`)} ${rIcon}`, 0, 0));
						c.addChild(new Text(fg("muted", "Task: ") + fg("dim", r.task), 0, 0));
						for (const item of getDisplayItems(r.messages)) {
							if (item.type === "toolCall") c.addChild(new Text(fg("muted", "→ ") + fmtToolCall(item.name, item.args, fg), 0, 0));
						}
						const final = getFinalOutput(r.messages);
						if (final) { c.addChild(new Spacer(1)); c.addChild(new Markdown(final.trim(), 0, 0, mdTheme)); }
						const su = fmtUsage(r.usage, r.model);
						if (su) c.addChild(new Text(fg("dim", su), 0, 0));
					}
					const tu = fmtUsage(aggUsage(details.results));
					if (tu) { c.addChild(new Spacer(1)); c.addChild(new Text(fg("dim", `Total: ${tu}`), 0, 0)); }
					return c;
				}

				let t = `${icon} ${fg("toolTitle", theme.bold("parallel "))}${fg("accent", status)}`;
				for (const r of details.results) {
					const rIcon = r.exitCode === -1 ? fg("warning", "⏳") : r.exitCode === 0 ? fg("success", "✓") : fg("error", "✗");
					const nucIcon = NUC_ICONS[r.agent] || "";
					t += `\n\n${fg("muted", "─── ")}${fg("accent", `${nucIcon} ${r.agent}`)} ${rIcon}`;
					const items = getDisplayItems(r.messages);
					t += items.length ? `\n${renderItems(items, 5)}` : `\n${fg("muted", r.exitCode === -1 ? "(running...)" : "(no output)")}`;
				}
				if (!live) {
					const tu = fmtUsage(aggUsage(details.results));
					if (tu) t += `\n\n${fg("dim", `Total: ${tu}`)}`;
				}
				if (!expanded) t += `\n${fg("muted", "(Ctrl+O to expand)")}`;
				return new Text(t, 0, 0);
			}

			const t = result.content[0];
			return new Text(t?.type === "text" ? t.text : "(no output)", 0, 0);
		},
	});
}
