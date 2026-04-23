#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_cdp.py -- Chrome DevTools Protocol helper for CEX

Control Chrome via CDP WebSocket. Requires --remote-debugging-port=9222.

Subcommands: status | tabs | navigate | click | type | read | elements
             eval | new-tab | screenshot

Selector strategies (click/type):
  css:#btn  text:Submit  aria:Close  coord:100,200
  Auto-detect: starts with . # [ => CSS, else text search.

Dependency: websockets + stdlib. See --help for full usage.
"""

import argparse
import asyncio
import base64
import json
import sys
import urllib.error
import urllib.request


def safe_print(text):
    """Print text safely on cp1252/ASCII terminals."""
    if isinstance(text, str):
        text = text.encode("ascii", "replace").decode("ascii")
    print(text)


def fail(msg):
    """Print failure message and exit."""
    safe_print("[FAIL] " + msg)
    sys.exit(1)


class CdpClient:
    """Manages a CDP WebSocket connection to a single Chrome tab."""

    def __init__(self, port=9222, timeout_ms=30000):
        self.port = port
        self.timeout = timeout_ms / 1000.0
        self._ws = None
        self._msg_id = 0

    def get_tabs(self):
        """Fetch open page tabs via CDP HTTP endpoint."""
        url = "http://127.0.0.1:%d/json" % self.port
        try:
            req = urllib.request.urlopen(url, timeout=5)
            data = json.loads(req.read().decode("utf-8"))
        except (urllib.error.URLError, OSError, ConnectionError):
            fail(
                "Chrome CDP not active on port %d. "
                "Run: boot/chrome_cdp.ps1" % self.port
            )
        pages = [t for t in data if t.get("type") == "page"]
        if not pages:
            fail("No page tabs found")
        return pages

    async def connect(self, tab_index=0):
        """Open WebSocket to a specific tab."""
        import websockets
        tabs = self.get_tabs()
        if tab_index >= len(tabs):
            fail("Tab index %d out of range (have %d tabs)" % (tab_index, len(tabs)))
        ws_url = tabs[tab_index]["webSocketDebuggerUrl"]
        self._ws = await asyncio.wait_for(
            websockets.connect(ws_url, max_size=50 * 1024 * 1024),
            timeout=self.timeout,
        )

    async def send(self, method, params=None):
        """Send a CDP command and return the result."""
        self._msg_id += 1
        msg = {"id": self._msg_id, "method": method}
        if params:
            msg["params"] = params
        await self._ws.send(json.dumps(msg))
        while True:
            raw = await asyncio.wait_for(self._ws.recv(), timeout=self.timeout)
            resp = json.loads(raw)
            if resp.get("id") == self._msg_id:
                if "error" in resp:
                    fail("CDP error: %s" % resp["error"].get("message", str(resp["error"])))
                return resp.get("result", {})

    async def evaluate(self, expression, await_promise=False):
        """Evaluate JS in the page context."""
        params = {"expression": expression, "returnByValue": True}
        if await_promise:
            params["awaitPromise"] = True
        result = await self.send("Runtime.evaluate", params)
        obj = result.get("result", {})
        if obj.get("subtype") == "error":
            fail("JS error: %s" % obj.get("description", str(obj)))
        return obj.get("value")

    async def close(self):
        if self._ws:
            await self._ws.close()


# -- Selector parsing --

def parse_selector(raw):
    """Parse selector string into (strategy, value) tuple."""
    if raw.startswith("css:"):
        return ("css", raw[4:])
    if raw.startswith("text:"):
        return ("text", raw[5:])
    if raw.startswith("aria:"):
        return ("aria", raw[5:])
    if raw.startswith("coord:"):
        return ("coord", raw[6:])
    # auto-detect
    if raw and raw[0] in ".#[":
        return ("css", raw)
    return ("text", raw)


def _esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")


def js_click(strategy, value):
    """Generate JS to click an element by strategy. Returns JS string."""
    v = _esc(value)
    if strategy == "css":
        find = "var el = document.querySelector('%s');" % v
    elif strategy == "aria":
        find = "var el = document.querySelector('[aria-label=\"%s\"]');" % v.replace("'", '"')
    else:  # text
        find = (
            "var all = document.querySelectorAll("
            "'button,a,input,[role=button],[role=tab],label,span,div');"
            "var el = null;"
            "for (var i = 0; i < all.length; i++) {"
            "  if (all[i].innerText && all[i].innerText.trim() === '%s') { el = all[i]; break; }"
            "}"
            "if (!el) {"
            "  for (var i = 0; i < all.length; i++) {"
            "    if (all[i].innerText && all[i].innerText.trim().indexOf('%s') !== -1)"
            "      { el = all[i]; break; }"
            "  }"
            "}" % (v, v)
        )
    return find + (
        "if (!el) throw new Error('not found');"
        "el.scrollIntoView({block:'center'});"
        "el.click(); 'clicked'"
    )


def js_type_into(selector_js, text):
    t = _esc(text)
    return (
        "%s"
        "var nativeSet = Object.getOwnPropertyDescriptor("
        "  window.HTMLTextAreaElement.prototype, 'value');"
        "if (!nativeSet) nativeSet = Object.getOwnPropertyDescriptor("
        "  window.HTMLInputElement.prototype, 'value');"
        "nativeSet.set.call(el, '%s');"
        "el.dispatchEvent(new Event('input', {bubbles: true}));"
        "el.dispatchEvent(new Event('change', {bubbles: true}));"
        "'typed'" % (selector_js, t)
    )


def js_find_element(strategy, value):
    """Return JS that finds element and stores in `el`. Throws if missing."""
    v = _esc(value)
    if strategy == "css":
        return "var el = document.querySelector('%s'); if (!el) throw new Error('not found');" % v
    if strategy == "text":
        return (
            "var _all = document.querySelectorAll("
            "'button,a,input,textarea,select,[role=button],[role=tab],label,span,div');"
            "var el = null;"
            "for (var i = 0; i < _all.length; i++) {"
            "  if (_all[i].innerText && _all[i].innerText.trim() === '%s') { el = _all[i]; break; }"
            "} if (!el) {"
            "  for (var i = 0; i < _all.length; i++) {"
            "    if (_all[i].innerText && _all[i].innerText.trim().indexOf('%s') !== -1)"
            "      { el = _all[i]; break; }"
            "  }"
            "} if (!el) throw new Error('not found');" % (v, v)
        )
    if strategy == "aria":
        return (
            'var el = document.querySelector(\'[aria-label="%s"]\');'
            "if (!el) throw new Error('not found');" % v.replace("'", '"')
        )
    fail("Cannot use strategy '%s' for type command" % strategy)


JS_ELEMENTS = (
    "var sels = 'button,a,input,textarea,select,[role=button],[role=tab]';"
    "var els = document.querySelectorAll(sels);"
    "var out = [];"
    "for (var i = 0; i < els.length; i++) {"
    "  var e = els[i];"
    "  var tag = e.tagName.toLowerCase();"
    "  var role = e.getAttribute('role') || '';"
    "  var txt = (e.innerText || e.value || e.placeholder || '').trim().substring(0, 60);"
    "  var lbl = e.getAttribute('aria-label') || '';"
    "  var id = e.id ? '#' + e.id : '';"
    "  var cls = e.className && typeof e.className === 'string' "
    "    ? '.' + e.className.trim().split(/\\s+/).join('.') : '';"
    "  var hint = id || cls || tag;"
    "  out.push(tag + ' | ' + role + ' | ' + txt + ' | ' + lbl + ' | ' + hint);"
    "}"
    "out.join('\\n')"
)

JS_READ_TEXT = (
    "document.body.innerText.substring(0, 50000)"
)


# -- Subcommand handlers --

async def cmd_status(args):
    cdp = CdpClient(port=args.port, timeout_ms=args.timeout)
    tabs = cdp.get_tabs()
    safe_print("[OK] CDP active on port %d -- %d page tab(s)" % (args.port, len(tabs)))


async def cmd_tabs(args):
    cdp = CdpClient(port=args.port, timeout_ms=args.timeout)
    tabs = cdp.get_tabs()
    for i, t in enumerate(tabs):
        safe_print("[%d] %s" % (i, t.get("title", "(no title)")))
        safe_print("    %s" % t.get("url", ""))


async def cmd_navigate(args):
    cdp = CdpClient(port=args.port, timeout_ms=args.timeout)
    await cdp.connect(args.tab)
    await cdp.send("Page.navigate", {"url": args.url})
    await asyncio.sleep(1)
    title = await cdp.evaluate("document.title")
    safe_print("[OK] Navigated to: %s" % str(title))
    await cdp.close()


async def cmd_click(args):
    cdp = CdpClient(port=args.port, timeout_ms=args.timeout)
    await cdp.connect(args.tab)
    strategy, value = parse_selector(args.selector)
    if strategy == "coord":
        parts = value.split(",")
        x, y = float(parts[0]), float(parts[1])
        for evt in ("mousePressed", "mouseReleased"):
            await cdp.send("Input.dispatchMouseEvent", {
                "type": evt, "x": x, "y": y, "button": "left", "clickCount": 1
            })
        safe_print("[OK] Clicked at (%s, %s)" % (parts[0], parts[1]))
    else:
        await cdp.evaluate(js_click(strategy, value))
        safe_print("[OK] Clicked: %s:%s" % (strategy, value))
    await cdp.close()


async def cmd_type(args):
    cdp = CdpClient(port=args.port, timeout_ms=args.timeout)
    await cdp.connect(args.tab)
    strategy, value = parse_selector(args.selector)
    find_js = js_find_element(strategy, value)
    full_js = js_type_into(find_js, args.text)
    await cdp.evaluate(full_js)
    safe_print("[OK] Typed %d chars into %s:%s" % (len(args.text), strategy, value))
    await cdp.close()


async def cmd_read(args):
    cdp = CdpClient(port=args.port, timeout_ms=args.timeout)
    await cdp.connect(args.tab)
    text = await cdp.evaluate(JS_READ_TEXT)
    safe_print(str(text or ""))
    await cdp.close()


async def cmd_elements(args):
    cdp = CdpClient(port=args.port, timeout_ms=args.timeout)
    await cdp.connect(args.tab)
    raw = await cdp.evaluate(JS_ELEMENTS)
    safe_print("tag | role | text | aria-label | selector_hint")
    safe_print("-" * 70)
    if raw:
        safe_print(str(raw))
    await cdp.close()


async def cmd_eval(args):
    cdp = CdpClient(port=args.port, timeout_ms=args.timeout)
    await cdp.connect(args.tab)
    result = await cdp.evaluate(args.expression)
    safe_print(str(result) if result is not None else "undefined")
    await cdp.close()


async def cmd_new_tab(args):
    cdp = CdpClient(port=args.port, timeout_ms=args.timeout)
    tabs = cdp.get_tabs()
    await cdp.connect(0)
    await cdp.send("Target.createTarget", {"url": args.url})
    safe_print("[OK] Opened new tab: %s" % args.url)
    await cdp.close()


async def cmd_screenshot(args):
    cdp = CdpClient(port=args.port, timeout_ms=args.timeout)
    await cdp.connect(args.tab)
    result = await cdp.send("Page.captureScreenshot", {"format": "png"})
    b64 = result.get("data", "")
    out_path = args.output or "screenshot.png"
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(b64))
    safe_print("[OK] Screenshot saved: %s (%d bytes)" % (out_path, len(b64) * 3 // 4))
    await cdp.close()


def build_parser():
    p = argparse.ArgumentParser(
        prog="cex_cdp.py",
        description="Chrome DevTools Protocol helper -- control Chrome via CDP",
    )
    p.add_argument("--port", type=int, default=9222, help="CDP port (default: 9222)")
    p.add_argument("--timeout", type=int, default=30000, help="Timeout in ms (default: 30000)")

    sub = p.add_subparsers(dest="command", help="Subcommand")

    sub.add_parser("status", help="Check if CDP is alive")
    sub.add_parser("tabs", help="List open tabs")

    nav = sub.add_parser("navigate", help="Navigate tab to URL")
    nav.add_argument("url")
    nav.add_argument("--tab", type=int, default=0)

    clk = sub.add_parser("click", help="Click element")
    clk.add_argument("selector", help="css:/text:/aria:/coord: or auto-detect")
    clk.add_argument("--tab", type=int, default=0)

    typ = sub.add_parser("type", help="Type into input field")
    typ.add_argument("selector", help="Element selector")
    typ.add_argument("text", help="Text to type")
    typ.add_argument("--tab", type=int, default=0)

    rd = sub.add_parser("read", help="Dump page text")
    rd.add_argument("--tab", type=int, default=0)

    el = sub.add_parser("elements", help="List interactive elements")
    el.add_argument("--tab", type=int, default=0)

    ev = sub.add_parser("eval", help="Evaluate JS expression")
    ev.add_argument("expression")
    ev.add_argument("--tab", type=int, default=0)

    nt = sub.add_parser("new-tab", help="Open new tab")
    nt.add_argument("url")

    ss = sub.add_parser("screenshot", help="Take screenshot")
    ss.add_argument("--tab", type=int, default=0)
    ss.add_argument("-o", "--output", help="Output file path (default: screenshot.png)")

    return p


DISPATCH = {
    "status": cmd_status,
    "tabs": cmd_tabs,
    "navigate": cmd_navigate,
    "click": cmd_click,
    "type": cmd_type,
    "read": cmd_read,
    "elements": cmd_elements,
    "eval": cmd_eval,
    "new-tab": cmd_new_tab,
    "screenshot": cmd_screenshot,
}


def main():
    parser = build_parser()
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    handler = DISPATCH.get(args.command)
    if not handler:
        fail("Unknown command: %s" % args.command)
    try:
        asyncio.run(handler(args))
    except KeyboardInterrupt:
        sys.exit(130)


if __name__ == "__main__":
    main()
