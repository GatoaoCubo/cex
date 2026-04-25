#!/usr/bin/env python3
"""cex_outreach.py -- CEX Influencer CRM Outreach Queue Manager.

Manages a personalized outreach queue for the CEX influencer CRM.
Reads from crm_data.json (read-only), writes state to outreach_state.json
and daily queue to outreach_queue.json.

Subcommands:
    generate  -- Pick top N contacts and generate personalized messages
    today     -- Show today's queued outreach
    send      -- Mark a contact as contacted
    followups -- Show follow-up-due contacts
    stats     -- Pipeline statistics
    status    -- Update a contact's outreach status

Usage:
    python _tools/cex_outreach.py generate --count 3
    python _tools/cex_outreach.py today
    python _tools/cex_outreach.py send 34
    python _tools/cex_outreach.py followups
    python _tools/cex_outreach.py stats
    python _tools/cex_outreach.py status 34 replied
"""

import argparse
import json
import os
import random
import sys
import textwrap
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# Safe stdout for Windows terminals (cp1252 cannot render UTF-8 PT-BR).
# Messages are stored in JSON as UTF-8; console output uses replace fallback.
# ---------------------------------------------------------------------------

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_OUTPUT_DIR = os.path.join(_REPO_ROOT, "N06_commercial", "P05_output")
_CRM_PATH = os.path.join(_OUTPUT_DIR, "crm_data.json")
_STATE_PATH = os.path.join(_OUTPUT_DIR, "outreach_state.json")
_QUEUE_PATH = os.path.join(_OUTPUT_DIR, "outreach_queue.json")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VALID_STATUSES = [
    "not_started", "researched", "contacted",
    "replied", "converted", "declined",
]

FOLLOWUP_DAYS = 7

# Known platform names for column-shift detection
KNOWN_PLATFORMS = {
    "Twitter/X", "YouTube", "GitHub", "Instagram", "Newsletter",
    "Telegram", "Podcast", "LinkedIn", "Blog", "Discord",
    "Conference", "Academic", "Education", "Meetup", "Community",
    "Reddit", "Slack",
}

# Platform -> template platform code
PLATFORM_CODES = {
    "Twitter/X": "X",
    "Email": "EM",
    "YouTube": "YT",
    "Discord": "DC",
    "LinkedIn": "LI",
    "Reddit": "RD",
    "Newsletter": "NL",
    "Blog": "BG",
    "GitHub": "OSS",
    "Podcast": "EM",
    "Telegram": "EM",
    "Instagram": "EM",
    "Conference": "EM",
    "Academic": "EM",
    "Education": "EM",
    "Meetup": "EM",
    "Community": "DC",
    "Slack": "DC",
}

# Region code mapping
REGION_CODES = {
    "BR": "BR",
    "GLOBAL": "EN",
}

# Opening line variations
OPENINGS_EN = [
    "Hey {name},",
    "Hi {name} --",
    "{name},",
    "Hey -- quick note for {name}.",
    "Hi {name}!",
]

OPENINGS_BR = [
    "Oi {name},",
    "E ai {name},",
    "{name},",
    "Fala {name} --",
    "Oi! {name},",
]

# Positioning -- unaccented PT-BR matching tpl_outreach_messages.md convention.
# Accented forms live in the JSON output only (via CRM data passthrough).
CEX_ONELINER_EN = "The AI brain that compounds intelligence."
CEX_ONELINER_BR = "O cerebro de IA que acumula inteligencia."

CEX_PITCH_EN = (
    "AI agents today are disposable -- you prompt, you get an answer, "
    "it evaporates. CEX is different. It is an AI brain, not an agent. "
    "300 typed knowledge artifacts, a mandatory 8-step reasoning pipeline, "
    "and 7 specialized nuclei produce scored, governed output that lives "
    "in your git repo. Run it on Claude, Gemini, Codex, or Ollama. "
    "Your knowledge compounds. Your provider does not matter."
)

CEX_PITCH_BR = (
    "Agentes de IA hoje sao descartaveis -- voce faz um "
    "prompt, recebe uma resposta, ela evapora. CEX e diferente. "
    "E um cerebro de IA, nao um agente. 300 artefatos de "
    "conhecimento tipados, um pipeline de raciocinio obrigatorio "
    "de 8 passos e 7 nucleos especializados produzem saidas "
    "pontuadas e governadas que vivem no seu repositorio git. Rode em "
    "Claude, Gemini, Codex ou Ollama. Seu conhecimento se acumula. Seu "
    "provedor nao importa."
)

# ---------------------------------------------------------------------------
# Message body templates (simplified from tpl_outreach_messages.md).
# Keys: template_id -> (subject, body) where body uses {name}, {their_content},
#        {their_platform}, {cex_oneliner}, {cex_pitch}, {personal_note}.
# We store a representative set; fallback logic fills gaps.
# All PT-BR uses unaccented form (matching the template file convention).
# ---------------------------------------------------------------------------

TEMPLATES = {
    # --- T1 ---
    "T1-X-EN": (
        None,
        "Huge fan of your work on {their_content}. It connects to something "
        "we just shipped.\n\n"
        "We built CEX -- {cex_oneliner} An open-source AI brain with 300 "
        "typed knowledge artifacts, a mandatory 8-step reasoning pipeline, "
        "and multi-runtime support (Claude, Gemini, Codex, Ollama).\n\n"
        "I think your audience would find the architecture genuinely "
        "interesting.\n\n"
        "Would you be open to a 10-minute async demo? No strings.\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T1-X-BR": (
        None,
        "Acompanho seu trabalho ha tempos -- {their_content} foi "
        "exatamente o tipo de conteudo que me fez querer compartilhar "
        "isso com voce.\n\n"
        "Lancamos o CEX -- {cex_oneliner} Um cerebro de IA "
        "open-source com 300 tipos de artefatos, pipeline de raciocinio "
        "obrigatorio de 8 passos, e suporte multi-runtime.\n\n"
        "Topa uma demo de 10 minutos? Sem compromisso.\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T1-EM-EN": (
        "CEX: typed AI brain -- 300 kinds, 8F pipeline, 4 runtimes (open source)",
        "I have been following your work on {their_content} -- particularly "
        "relevant to what we have been building.\n\n"
        "{cex_pitch}\n\n"
        "I would love to get your take on the architecture. We are pre-launch "
        "and looking for technical eyes, not marketing endorsements.\n\n"
        "Would a 15-minute demo work?\n\n{personal_note}\n\n"
        "github.com/gato3ao3/cex",
    ),
    "T1-EM-BR": (
        "CEX: cerebro de IA tipado -- 300 tipos, pipeline 8F, 4 runtimes",
        "Acompanho seu trabalho em {their_content} -- particularmente "
        "relevante para o que estamos construindo.\n\n"
        "{cex_pitch}\n\n"
        "Gostaria da sua opiniao sobre a arquitetura. Estamos em "
        "pre-lancamento e buscamos olhos tecnicos.\n\n"
        "Uma demo de 15 minutos funciona?\n\n{personal_note}\n\n"
        "github.com/gato3ao3/cex",
    ),
    "T1-YT-EN": (
        "Collab idea: typed AI brain with visible 8-step reasoning trace",
        "Your work on {their_platform} is outstanding -- {their_content} "
        "made me think you would genuinely enjoy tearing apart our "
        "architecture.\n\n"
        "We built CEX -- {cex_pitch}\n\n"
        "The 8F reasoning trace runs live -- viewers see each of the 8 steps "
        "executing. 4-runtime comparison side-by-side. Quality scoring in "
        "real time.\n\n"
        "Zero editorial control from our side. Your video, your take.\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    # --- T2 ---
    "T2-X-EN": (
        None,
        "Saw your work on {their_content}. Resonated hard.\n\n"
        "We just open-sourced CEX -- a typed AI brain with 300 artifact "
        "kinds, mandatory quality scoring, and 4-runtime support "
        "(Claude/Gemini/Codex/Ollama).\n\n"
        "The 8F reasoning pipeline is the part I think you would find most "
        "interesting -- mandatory, quality-gated, visible trace.\n\n"
        "Happy to share early access or a quick demo. Interested?\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T2-X-BR": (
        None,
        "Vi seu trabalho sobre {their_content}. Achei muito relevante.\n\n"
        "Acabamos de lancar o CEX em open-source -- um cerebro "
        "de IA tipado com 300 tipos de artefatos, pontuacao de "
        "qualidade obrigatoria, e suporte a 4 runtimes.\n\n"
        "Posso compartilhar acesso antecipado ou uma demo rapida. "
        "Interessa?\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T2-EM-EN": (
        "CEX: what if AI artifacts were typed like database schemas?",
        "Quick pitch, honest ask.\n\n"
        "CEX is an open-source AI brain where every output is a typed "
        "knowledge artifact -- not unstructured text. 300 artifact kinds, "
        "12 domain pillars, mandatory 8-step reasoning with quality "
        "scoring.\n\n"
        "Your work on {their_content} made me think you would have a strong "
        "opinion on whether this architecture solves a real problem.\n\n"
        "Would love 15 minutes -- demo or just a conversation. We are "
        "pre-launch and seeking people who will tell us what is wrong.\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T2-EM-BR": (
        "CEX: e se artefatos de IA fossem tipados como schemas de banco?",
        "Pitch curto, pergunta honesta.\n\n"
        "CEX e um cerebro de IA open-source onde cada saida "
        "e um artefato de conhecimento tipado. 300 tipos de artefatos, "
        "12 pilares de dominio, raciocinio obrigatorio de 8 "
        "passos com pontuacao de qualidade.\n\n"
        "Seu trabalho em {their_content} me fez pensar que voce teria "
        "uma opiniao forte sobre essa arquitetura.\n\n"
        "Topa 15 minutos?\n\n{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T2-DC-EN": (
        None,
        "I have been following your takes on {their_content} -- consistently "
        "great.\n\n"
        "We just open-sourced CEX -- a typed AI brain with 300 artifact "
        "kinds and a mandatory reasoning pipeline.\n\n"
        "Not another agent framework. Every output is quality-scored (9.0 "
        "target) and lives in your git repo. Runs on "
        "Claude/Gemini/Codex/Ollama.\n\n"
        "Would love your honest take: github.com/gato3ao3/cex\n\n"
        "{personal_note}",
    ),
    "T2-LI-EN": (
        None,
        "Your work on {their_content} caught my attention.\n\n"
        "We are building CEX, an open-source typed knowledge system for AI "
        "agents. 300 typed artifact kinds, scored (9.0 quality target), and "
        "governed (8-step mandatory reasoning pipeline). Runs on 4 runtimes "
        "-- no vendor lock-in.\n\n"
        "Would you be open to a quick look?\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T2-LI-BR": (
        None,
        "Seu trabalho sobre {their_content} chamou minha atencao.\n\n"
        "Estamos construindo o CEX, um sistema de conhecimento tipado "
        "open-source para agentes de IA. 300 tipos, pontuado (meta 9.0) e "
        "governado (pipeline de 8 passos). Roda em 4 runtimes -- sem "
        "lock-in.\n\n"
        "Topa dar uma olhada?\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T2-YT-EN": (
        "Collab idea: typed AI brain demo",
        "Your {their_platform} content on {their_content} is great.\n\n"
        "We built CEX -- {cex_oneliner} 300 artifact kinds, 8-step "
        "reasoning trace, 4-runtime support. Would make a strong demo "
        "video.\n\n"
        "Interested in a walkthrough or a roast session?\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T2-YT-BR": (
        "Ideia de collab: cerebro de IA tipado",
        "Seu conteudo sobre {their_content} no {their_platform} e "
        "otimo.\n\n"
        "Construimos o CEX -- {cex_oneliner} 300 tipos de artefatos, "
        "trace de raciocinio de 8 passos, suporte a 4 runtimes. "
        "Renderia um video forte.\n\n"
        "Topa um walkthrough ou uma sessao de critica?\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    # --- T3 ---
    "T3-X-EN": (
        None,
        "Your work on {their_content} is genuinely interesting.\n\n"
        "We have been working on something related: a typed knowledge system "
        "for AI agents -- 300 artifact kinds, 8-step reasoning pipeline, "
        "runs on Claude/Gemini/Codex/Ollama. MIT licensed.\n\n"
        "Repo: github.com/gato3ao3/cex\n\n{personal_note}",
    ),
    "T3-RD-EN": (
        None,
        "Interesting angle. We have been working on a different take on "
        "this.\n\n"
        "CEX produces typed knowledge artifacts -- 300 kinds, 12 domain "
        "pillars, mandatory 8-step reasoning pipeline scoring every output "
        "(9.0 target). Runs on Claude/Gemini/Codex/Ollama. MIT licensed.\n\n"
        "github.com/gato3ao3/cex -- happy to answer architecture questions."
        "\n\n{personal_note}",
    ),
    "T3-DC-EN": (
        None,
        "Show & Tell: CEX -- a typed AI brain (open source)\n\n"
        "300 typed artifact kinds, 12 domain pillars, mandatory 8-step "
        "reasoning pipeline. Every output is scored (9.0 target), compiled, "
        "and version-controlled. Runs on Claude/Gemini/Codex/Ollama.\n\n"
        "Quick demo: /build landing_page -> complete, quality-gated artifact"
        "\n\ngithub.com/gato3ao3/cex\n\n{personal_note}",
    ),
    "T3-BG-EN": (
        "Guest post pitch: Convention over Configuration for AI Agents",
        "I would like to pitch a guest post on a topic I think your readers "
        "would find provocative: what Rails taught us about building AI "
        "systems.\n\n"
        "CEX applies convention-over-configuration to AI: 300 typed kinds, "
        "12 pillars, mandatory reasoning pipeline. {cex_oneliner}\n\n"
        "1,500-2,000 words, benchmarks + architecture diagrams. Happy to "
        "have your editorial team reshape.\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T3-NL-EN": (
        "For your newsletter: typed AI brain with 300 artifact kinds (open source)",
        "Quick pitch: CEX is an open-source AI brain that takes a different "
        "approach from LangChain, CrewAI, and OpenAI Agents SDK.\n\n"
        "Every AI output is a typed knowledge artifact. 300 kinds. 12 "
        "domain pillars. Mandatory quality scoring (9.0 target). Runs on "
        "Claude/Gemini/Codex/Ollama.\n\n"
        "Stats: 300 kinds, 302 builders, 12 pillars, 8-step pipeline, 144 "
        "tools, 4 runtimes.\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T3-EM-EN": (
        "CEX: typed AI brain (open source) -- 300 kinds, 8F pipeline",
        "Your work on {their_content} made me think you would have a strong "
        "take on this.\n\n"
        "{cex_pitch}\n\n"
        "Would love your honest reaction -- including 'this is wrong because "
        "X'. Pre-launch, seeking technical eyes.\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T3-EM-BR": (
        "CEX: cerebro de IA tipado (open source) -- 300 tipos, pipeline 8F",
        "Seu trabalho em {their_content} me fez pensar que voce teria "
        "uma opiniao forte sobre isso.\n\n"
        "{cex_pitch}\n\n"
        "Sua reacao honesta -- incluindo 'isso esta errado "
        "porque X' -- e exatamente o que precisamos.\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    # --- T4 ---
    "T4-P2P-EN": (
        None,
        "Saw your work on {their_content} and thought you might find this "
        "interesting.\n\n"
        "We are building CEX -- an open-source AI brain with typed knowledge "
        "artifacts (300 kinds, 8-step reasoning, runs on "
        "Ollama/Claude/Gemini/Codex).\n\n"
        "Pre-launch, looking for early users who want to break things.\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T4-OSS-EN": (
        None,
        "I noticed your contributions on {their_platform} -- solid work on "
        "{their_content}.\n\n"
        "We are building CEX, an open-source AI brain (MIT licensed) and we "
        "are looking for contributors. The codebase is Python + YAML + "
        "Markdown. 144 tools, 302 builder definitions, 300 artifact kinds.\n\n"
        "If you are curious: github.com/gato3ao3/cex\n\n"
        "Even a code review would be valuable.\n\n{personal_note}",
    ),
    "T4-BLD-EN": (
        None,
        "Your work on {their_content} shows you think deeply about "
        "{their_platform}.\n\n"
        "We are building CEX -- a typed AI brain where 300 artifact kinds "
        "are organized across 12 pillars. We have 302 builder agents but "
        "are missing depth in your area.\n\n"
        "Would you want to co-build? Full credit, MIT licensed.\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    "T4-P2P-BR": (
        None,
        "Vi seu trabalho em {their_content} e achei que voce ia curtir "
        "isso.\n\n"
        "Estamos construindo o CEX -- um cerebro de IA open-source com "
        "300 tipos de artefatos, pipeline de 8 passos, roda em "
        "Ollama/Claude/Gemini/Codex.\n\n"
        "Pre-lancamento, buscando early users. Interessa?\n\n"
        "{personal_note}\n\ngithub.com/gato3ao3/cex",
    ),
    # --- Follow-ups ---
    "FU-NR-EN": (
        None,
        "Following up on my message about CEX (typed AI brain, 300 artifact "
        "kinds, open source). Totally understand if the timing is not "
        "right.\n\n"
        "No pressure either way.\n\ngithub.com/gato3ao3/cex",
    ),
    "FU-NR-BR": (
        None,
        "Passando pra dar um oi sobre o CEX (cerebro de IA tipado, 300 "
        "tipos, open source). Entendo totalmente se o timing nao "
        "e o melhor agora.\n\n"
        "Sem pressao.\n\ngithub.com/gato3ao3/cex",
    ),
}


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------

def _load_json(path, default=None):
    """Load a JSON file, returning default if missing or corrupt."""
    if not os.path.isfile(path):
        return default if default is not None else []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        return default if default is not None else []


def _save_json(path, data):
    """Save data as pretty-printed JSON."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
    return path


def _load_crm():
    """Load CRM contacts from crm_data.json (read-only source)."""
    contacts = _load_json(_CRM_PATH, [])
    if not contacts:
        print("[FAIL] Cannot load CRM data from: %s" % _CRM_PATH)
        sys.exit(1)
    return contacts


def _load_state():
    """Load outreach state overrides."""
    return _load_json(_STATE_PATH, {})


def _save_state(state):
    """Save outreach state overrides."""
    _save_json(_STATE_PATH, state)


def _load_queue():
    """Load the daily outreach queue."""
    return _load_json(_QUEUE_PATH, [])


def _save_queue(queue):
    """Save the daily outreach queue."""
    _save_json(_QUEUE_PATH, queue)


# ---------------------------------------------------------------------------
# Contact normalization (handles column-shift in CRM data)
# ---------------------------------------------------------------------------

def _normalize_contact(raw):
    """Fix column-shifted CRM records and return a normalized dict.

    Some records have their columns shifted:
      - platform contains tier value (T1-T4)
      - handle contains the real platform
      - followers contains the real handle
    We detect and correct this.
    """
    c = dict(raw)  # shallow copy

    plat = c.get("platform", "")
    tier = c.get("tier", "")

    # Detection: if platform field is a tier code, columns are shifted
    if plat in ("T1", "T2", "T3", "T4"):
        real_platform = c.get("handle", "")
        real_handle = c.get("followers", "")
        # If tier was '--', use the platform field as tier
        if tier == "--":
            c["tier"] = plat
        c["platform"] = real_platform
        c["handle"] = real_handle
        c["followers"] = "--"

    # Detection: if platform starts with a digit (like '3.0M'), it is a
    # follower count stuffed in the wrong column (Reddit-type records)
    elif plat and plat[0].isdigit():
        c["followers"] = plat
        c["platform"] = "Reddit"  # best guess for these records
        # handle is often 'HIGH' (engagement), not a real handle
        if c.get("handle", "").upper() in ("HIGH", "MEDIUM", "LOW"):
            c["handle"] = c.get("name", "")

    # Fix tier='--' without platform shift (edge case)
    if c.get("tier", "--") == "--":
        c["tier"] = "T4"  # default unknown to lowest tier

    return c


def _get_effective_status(contact, state):
    """Get the effective outreach status for a contact."""
    num = str(contact.get("num", ""))
    if num in state and "status" in state[num]:
        return state[num]["status"]
    return contact.get("outreach_status", "not_started")


def _extract_first_sentence(text):
    """Extract the first sentence from a notes field."""
    if not text or text == "--":
        return ""
    # Split on common sentence terminators
    for sep in [";", ".", "!"]:
        idx = text.find(sep)
        if idx > 0 and idx < 120:
            return text[:idx].strip()
    # No terminator -- return up to 100 chars
    if len(text) > 100:
        return text[:100].strip()
    return text.strip()


# ---------------------------------------------------------------------------
# Template selection and message generation
# ---------------------------------------------------------------------------

def _resolve_platform_code(platform):
    """Map a platform name to its template code."""
    if not platform:
        return "EM"
    # Direct match
    if platform in PLATFORM_CODES:
        return PLATFORM_CODES[platform]
    # Partial match (e.g. 'Twitter/X/YT' -> 'X')
    for known, code in PLATFORM_CODES.items():
        if known in platform:
            return code
    return "EM"  # fallback to email


def _resolve_region_code(region):
    """Map a region to its template region code."""
    if not region:
        return "EN"
    return REGION_CODES.get(region.upper().strip(), "EN")


def _select_template_id(tier, platform, region):
    """Build the template ID and find the best match with fallback."""
    plat_code = _resolve_platform_code(platform)
    reg_code = _resolve_region_code(region)
    tier = tier if tier in ("T1", "T2", "T3", "T4") else "T4"

    # Exact match
    tid = "%s-%s-%s" % (tier, plat_code, reg_code)
    if tid in TEMPLATES:
        return tid

    # Fallback 1: same tier + EM + same region
    fb1 = "%s-EM-%s" % (tier, reg_code)
    if fb1 in TEMPLATES:
        return fb1

    # Fallback 2: same tier + same platform + EN
    fb2 = "%s-%s-EN" % (tier, plat_code)
    if fb2 in TEMPLATES:
        return fb2

    # Fallback 3: same tier + EM + EN
    fb3 = "%s-EM-EN" % tier
    if fb3 in TEMPLATES:
        return fb3

    # Fallback 4: same tier + X + EN
    fb4 = "%s-X-EN" % tier
    if fb4 in TEMPLATES:
        return fb4

    # Fallback 5: same tier, any platform code that exists
    for key in TEMPLATES:
        if key.startswith(tier + "-"):
            return key

    # Fallback 6: T4-P2P-EN (lowest common denominator)
    return "T4-P2P-EN"


def _resolve_channel(platform, contact_method):
    """Determine the outreach channel based on platform + contact method."""
    cm = (contact_method or "").lower()
    if "email" in cm:
        return "Email"
    if "dm" in cm:
        return "DM"
    if "linkedin" in cm:
        return "LinkedIn"

    plat = (platform or "").lower()
    if "twitter" in plat or "x" in plat.split("/"):
        return "DM"
    if "youtube" in plat:
        return "Email"
    if "discord" in plat:
        return "Discord"
    if "linkedin" in plat:
        return "LinkedIn"
    if "github" in plat:
        return "GitHub/DM"
    if "reddit" in plat:
        return "Reddit"
    if "newsletter" in plat:
        return "Email"
    if "telegram" in plat:
        return "Telegram"
    return "Email"


def _generate_message(contact, template_id):
    """Generate a personalized outreach message for a contact."""
    region = (contact.get("region") or "GLOBAL").upper().strip()
    is_br = region == "BR"
    name = contact.get("name", "there")
    # Extract first name
    first_name = name.split("(")[0].strip().split()[0] if name else "there"

    # Select opening
    openings = OPENINGS_BR if is_br else OPENINGS_EN
    opening = random.choice(openings).format(name=first_name)

    # Get template body
    if template_id in TEMPLATES:
        _subj, body_tpl = TEMPLATES[template_id]
    else:
        _subj, body_tpl = TEMPLATES.get("T4-P2P-EN", (None, ""))

    # Build substitution values
    oneliner = CEX_ONELINER_BR if is_br else CEX_ONELINER_EN
    pitch = CEX_PITCH_BR if is_br else CEX_PITCH_EN
    personal_note = _extract_first_sentence(contact.get("notes", ""))

    body = body_tpl.format(
        name=first_name,
        their_content=contact.get("content_type", "your recent work"),
        their_platform=contact.get("platform", "your platform"),
        cex_oneliner=oneliner,
        cex_pitch=pitch,
        personal_note=personal_note,
    )

    return "%s\n\n%s" % (opening, body)


def _generate_followup_message(contact):
    """Generate a follow-up (no response) message."""
    region = (contact.get("region") or "GLOBAL").upper().strip()
    is_br = region == "BR"
    name = contact.get("name", "there")
    first_name = name.split("(")[0].strip().split()[0] if name else "there"

    tid = "FU-NR-BR" if is_br else "FU-NR-EN"
    openings = OPENINGS_BR if is_br else OPENINGS_EN
    opening = random.choice(openings).format(name=first_name)

    _subj, body_tpl = TEMPLATES.get(tid, TEMPLATES["FU-NR-EN"])
    body = body_tpl.format(
        name=first_name,
        their_content=contact.get("content_type", ""),
        their_platform=contact.get("platform", ""),
        cex_oneliner=CEX_ONELINER_EN,
        cex_pitch=CEX_PITCH_EN,
        personal_note="",
    )
    return "%s\n\n%s" % (opening, body)


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def cmd_generate(args):
    """Pick top N contacts and generate personalized outreach messages."""
    count = args.count
    today = datetime.now().strftime("%Y-%m-%d")

    crm = _load_crm()
    state = _load_state()
    queue = _load_queue()

    # Set of contact nums already queued today
    queued_today = set()
    for item in queue:
        if item.get("queued_date") == today:
            queued_today.add(str(item.get("contact_num", "")))

    # Filter eligible contacts
    eligible = []
    for raw in crm:
        c = _normalize_contact(raw)
        num = str(c.get("num", ""))
        eff_status = _get_effective_status(c, state)
        if eff_status != "not_started":
            continue
        if num in queued_today:
            continue
        priority = 0
        try:
            priority = int(c.get("priority", 0))
        except (ValueError, TypeError):
            pass
        eligible.append((priority, c))

    # Sort by priority descending, take top N
    eligible.sort(key=lambda x: x[0], reverse=True)
    selected = [c for _, c in eligible[:count]]

    if not selected:
        print("[i] No eligible contacts found (all contacted or already queued today).")
        return

    new_items = []
    for c in selected:
        tier = c.get("tier", "T4")
        platform = c.get("platform", "")
        region = c.get("region", "GLOBAL")
        contact_method = c.get("contact_method", "")

        template_id = _select_template_id(tier, platform, region)
        message = _generate_message(c, template_id)
        channel = _resolve_channel(platform, contact_method)
        personal_note = _extract_first_sentence(c.get("notes", ""))

        item = {
            "contact_num": str(c.get("num", "")),
            "name": c.get("name", ""),
            "platform": platform,
            "handle": c.get("handle", ""),
            "tier": tier,
            "region": region,
            "priority": c.get("priority", 0),
            "template_id": template_id,
            "message": message,
            "channel": channel,
            "profile_url": "",
            "queued_date": today,
            "status": "queued",
            "follow_up_date": None,
            "notes_for_human": personal_note,
        }
        new_items.append(item)

    # Merge with existing queue (replace any same-num entries for today)
    existing_nums = set(str(it.get("contact_num", "")) for it in new_items)
    kept = [
        it for it in queue
        if not (
            str(it.get("contact_num", "")) in existing_nums
            and it.get("queued_date") == today
        )
    ]
    kept.extend(new_items)
    _save_queue(kept)

    print("[OK] Generated %d outreach messages for %s" % (len(new_items), today))
    for item in new_items:
        print(
            "  [>>] #%s %s [%s] %s | %s | Priority: %s | Template: %s"
            % (
                item["contact_num"],
                item["name"],
                item["tier"],
                item["region"],
                item["channel"],
                item["priority"],
                item["template_id"],
            )
        )
    print("\nRun 'python _tools/cex_outreach.py today' to review messages.")


def cmd_today(args):
    """Show today's queued outreach contacts."""
    today = datetime.now().strftime("%Y-%m-%d")
    queue = _load_queue()

    todays = [it for it in queue
              if it.get("queued_date") == today and it.get("status") == "queued"]

    if not todays:
        print("[i] No outreach queued for today (%s)." % today)
        print("    Run 'python _tools/cex_outreach.py generate --count 3'"
              " to queue contacts.")
        return

    print("=== TODAY'S OUTREACH (%s) ===" % today)
    print("")

    for idx, item in enumerate(todays, 1):
        total = len(todays)
        print(
            "%d/%d  %s [%s] %s | %s | Priority: %s"
            % (
                idx,
                total,
                item.get("name", "?"),
                item.get("tier", "?"),
                item.get("region", "?"),
                item.get("channel", "?"),
                item.get("priority", "?"),
            )
        )
        print("     Template: %s" % item.get("template_id", "?"))
        print("     Message:")
        print("     ---")
        msg = item.get("message", "")
        for line in msg.split("\n"):
            wrapped = textwrap.fill(
                line, width=76,
                initial_indent="     ", subsequent_indent="     ",
            )
            print(wrapped if wrapped.strip() else "")
        print("     ---")
        print("     Action: Copy message, open %s" % item.get("channel", "Email"))
        notes = item.get("notes_for_human", "")
        if notes:
            print("     Notes: %s" % notes)
        print("")

    print("---")
    print("Commands:")
    print("  python _tools/cex_outreach.py send <contact_num>"
          "    -- Mark as sent")
    print("  python _tools/cex_outreach.py status <num> <status>"
          " -- Update status")


def cmd_send(args):
    """Mark a contact as contacted."""
    num = str(args.num)
    today = datetime.now().strftime("%Y-%m-%d")
    followup = (
        datetime.now() + timedelta(days=FOLLOWUP_DAYS)
    ).strftime("%Y-%m-%d")

    state = _load_state()
    queue = _load_queue()

    # Find the contact in the queue
    found_in_queue = False
    for item in queue:
        if str(item.get("contact_num", "")) == num:
            item["status"] = "sent"
            item["follow_up_date"] = followup
            found_in_queue = True

    # Update state
    if num not in state:
        state[num] = {}
    state[num]["status"] = "contacted"
    state[num]["contacted_date"] = today
    state[num]["follow_up_date"] = followup
    state[num]["updated"] = today

    _save_state(state)
    _save_queue(queue)

    # Look up name from queue or CRM
    name = "?"
    for item in queue:
        if str(item.get("contact_num", "")) == num:
            name = item.get("name", "?")
            break
    if name == "?":
        crm = _load_crm()
        for raw in crm:
            if str(raw.get("num", "")) == num:
                name = raw.get("name", "?")
                break

    loc = "queue" if found_in_queue else "state only"
    print("[OK] Marked #%s (%s) as contacted (%s)" % (num, name, loc))
    print("     Contacted: %s" % today)
    print("     Follow-up due: %s" % followup)


def cmd_followups(args):
    """Show contacts due for follow-up."""
    today = datetime.now().strftime("%Y-%m-%d")
    state = _load_state()
    crm = _load_crm()

    # Build lookup
    crm_by_num = {}
    for raw in crm:
        c = _normalize_contact(raw)
        crm_by_num[str(c.get("num", ""))] = c

    due = []
    for num, info in state.items():
        if info.get("status") != "contacted":
            continue
        fu_date = info.get("follow_up_date", "")
        if not fu_date or fu_date > today:
            continue
        contact = crm_by_num.get(num, {})
        if not contact:
            continue
        due.append((num, info, contact))

    if not due:
        print("[i] No follow-ups due as of %s." % today)
        return

    print("=== FOLLOW-UPS DUE (%s) ===" % today)
    print("")

    for idx, (num, info, contact) in enumerate(due, 1):
        name = contact.get("name", "?")
        tier = contact.get("tier", "?")
        region = contact.get("region", "?")
        platform = contact.get("platform", "?")
        contacted = info.get("contacted_date", "?")
        channel = _resolve_channel(
            platform, contact.get("contact_method", ""),
        )

        msg = _generate_followup_message(contact)

        print(
            "%d/%d  %s [%s] %s | %s | Contacted: %s"
            % (idx, len(due), name, tier, region, channel, contacted)
        )
        print("     Follow-up message:")
        print("     ---")
        for line in msg.split("\n"):
            wrapped = textwrap.fill(
                line, width=76,
                initial_indent="     ", subsequent_indent="     ",
            )
            print(wrapped if wrapped.strip() else "")
        print("     ---")
        print(
            "     Action: Send follow-up via %s, or mark"
            " 'replied'/'declined'" % channel
        )
        print("")

    print("---")
    print("Commands:")
    print("  python _tools/cex_outreach.py send <num>"
          "              -- Re-send (resets follow-up)")
    print("  python _tools/cex_outreach.py status <num> replied"
          "     -- They replied")
    print("  python _tools/cex_outreach.py status <num> declined"
          "    -- Not interested")


def cmd_stats(args):
    """Show outreach pipeline statistics."""
    crm = _load_crm()
    state = _load_state()
    queue = _load_queue()
    today = datetime.now().strftime("%Y-%m-%d")
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    total = len(crm)

    # Count by effective status
    counts = {}
    for raw in crm:
        c = _normalize_contact(raw)
        num = str(c.get("num", ""))
        eff = _get_effective_status(c, state)
        counts[eff] = counts.get(eff, 0) + 1

    not_started = counts.get("not_started", 0)
    researched = counts.get("researched", 0)
    contacted = counts.get("contacted", 0)
    replied = counts.get("replied", 0)
    converted = counts.get("converted", 0)
    declined = counts.get("declined", 0)

    # This week's sends
    week_sent = 0
    for num, info in state.items():
        cd = info.get("contacted_date", "")
        if cd >= week_ago:
            week_sent += 1

    # Response rate
    total_contacted = contacted + replied + converted + declined
    response_rate = 0.0
    if total_contacted > 0:
        response_rate = ((replied + converted) / total_contacted) * 100.0

    # Follow-ups due
    fu_due = 0
    for num, info in state.items():
        if info.get("status") == "contacted":
            fu_date = info.get("follow_up_date", "")
            if fu_date and fu_date <= today:
                fu_due += 1

    # Queued today
    queued_today = sum(
        1 for it in queue
        if it.get("queued_date") == today and it.get("status") == "queued"
    )

    print("=== OUTREACH PIPELINE STATS ===")
    print("")
    print(
        "Total CRM: %d | Not started: %d | Researched: %d | "
        "Contacted: %d | Replied: %d | Converted: %d | Declined: %d"
        % (total, not_started, researched, contacted,
           replied, converted, declined)
    )
    print(
        "This week: %d sent | Response rate: %.0f%% | "
        "Follow-ups due: %d | Queued today: %d"
        % (week_sent, response_rate, fu_due, queued_today)
    )
    print("")

    # Tier breakdown
    tier_counts = {}
    for raw in crm:
        c = _normalize_contact(raw)
        t = c.get("tier", "T4")
        tier_counts[t] = tier_counts.get(t, 0) + 1
    print("By tier:")
    for t in sorted(tier_counts.keys()):
        print("  %s: %d contacts" % (t, tier_counts[t]))

    # Region breakdown
    region_counts = {}
    for raw in crm:
        c = _normalize_contact(raw)
        r = c.get("region", "GLOBAL").upper().strip()
        region_counts[r] = region_counts.get(r, 0) + 1
    print("")
    print("By region:")
    for r in sorted(region_counts.keys()):
        print("  %s: %d contacts" % (r, region_counts[r]))


def cmd_status(args):
    """Update a contact's outreach status."""
    num = str(args.num)
    new_status = args.new_status

    if new_status not in VALID_STATUSES:
        print(
            "[FAIL] Invalid status '%s'. Valid: %s"
            % (new_status, ", ".join(VALID_STATUSES))
        )
        sys.exit(1)

    today = datetime.now().strftime("%Y-%m-%d")
    state = _load_state()

    if num not in state:
        state[num] = {}

    old_status = state[num].get("status", "not_started")
    state[num]["status"] = new_status
    state[num]["updated"] = today

    # Set specific date fields
    if new_status == "contacted" and "contacted_date" not in state[num]:
        state[num]["contacted_date"] = today
        state[num]["follow_up_date"] = (
            datetime.now() + timedelta(days=FOLLOWUP_DAYS)
        ).strftime("%Y-%m-%d")
    elif new_status == "replied":
        state[num]["replied_date"] = today
    elif new_status == "converted":
        state[num]["converted_date"] = today

    _save_state(state)

    # Look up name
    name = "?"
    crm = _load_crm()
    for raw in crm:
        if str(raw.get("num", "")) == num:
            name = raw.get("name", "?")
            break

    print(
        "[OK] #%s (%s): %s -> %s (updated %s)"
        % (num, name, old_status, new_status, today)
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog="cex_outreach",
        description="CEX Influencer CRM Outreach Queue Manager",
    )
    sub = parser.add_subparsers(dest="command", help="Available subcommands")

    # generate
    p_gen = sub.add_parser(
        "generate",
        help="Pick top N contacts and generate personalized outreach messages",
    )
    p_gen.add_argument(
        "--count", "-n", type=int, default=3,
        help="Number of contacts to queue (default: 3)",
    )

    # today
    sub.add_parser(
        "today",
        help="Show today's queued outreach contacts",
    )

    # send
    p_send = sub.add_parser(
        "send",
        help="Mark a contact as contacted (by contact num)",
    )
    p_send.add_argument("num", help="Contact number from CRM")

    # followups
    sub.add_parser(
        "followups",
        help="Show contacts due for follow-up (contacted + past follow-up date)",
    )

    # stats
    sub.add_parser(
        "stats",
        help="Show outreach pipeline statistics",
    )

    # status
    p_status = sub.add_parser(
        "status",
        help="Update a contact's outreach status",
    )
    p_status.add_argument("num", help="Contact number from CRM")
    p_status.add_argument(
        "new_status",
        choices=VALID_STATUSES,
        help="New status: %s" % ", ".join(VALID_STATUSES),
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    dispatch = {
        "generate": cmd_generate,
        "today": cmd_today,
        "send": cmd_send,
        "followups": cmd_followups,
        "stats": cmd_stats,
        "status": cmd_status,
    }

    fn = dispatch.get(args.command)
    if fn:
        fn(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
