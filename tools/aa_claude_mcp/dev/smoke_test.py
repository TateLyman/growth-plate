"""
End-to-end check of the AnnaLocal MCP bridge.

Spawns aa_mcp.py over stdio exactly the way Claude Code does, lists its tools,
and calls each one against a running local endpoint (the dev fixture in
dev/stub_aa_app.py, or a real local Anna's Archive instance).

Run:  python dev/smoke_test.py            # expects AA_BASE_URL reachable
      AA_BASE_URL=http://127.0.0.1:8000 python dev/smoke_test.py
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

HERE = Path(__file__).resolve().parent
SERVER = HERE.parent / "aa_mcp.py"
BASE_URL = os.environ.get("AA_BASE_URL", "http://localtest.me:8000")

PASS, FAIL = "PASS", "FAIL"
results: list[tuple[str, str, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    results.append((PASS if ok else FAIL, name, detail))
    print(f"[{PASS if ok else FAIL}] {name}{(' — ' + detail) if detail else ''}", flush=True)


def payload(result) -> object:
    """Structured content when present, else the text block (parsed if it is JSON)."""
    if getattr(result, "structured_content", None):
        sc = result.structured_content
        return sc.get("result", sc) if isinstance(sc, dict) else sc
    text = "\n".join(c.text for c in result.content if getattr(c, "type", "") == "text")
    try:
        return json.loads(text)
    except (ValueError, TypeError):
        return text


async def main() -> int:
    params = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER)],
        env={**os.environ, "AA_BASE_URL": BASE_URL},
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            init = await session.initialize()
            record("initialize", True, f"server: {init.server_info.name}")

            tools = await session.list_tools()
            names = sorted(t.name for t in tools.tools)
            expected = ["aa_health", "aa_llm_guide", "aa_open_record", "aa_search"]
            record("list_tools", names == expected, ", ".join(names))

            health = payload(await session.call_tool("aa_health"))
            record("aa_health", isinstance(health, str) and health.startswith("OK"), str(health)[:120])

            search = payload(await session.call_tool(
                "aa_search", {"query": "growth plate Notch", "limit": 5}
            ))
            hits = search.get("results", []) if isinstance(search, dict) else []
            record("aa_search returns hits", bool(hits), f"{len(hits)} result(s)")
            record(
                "aa_search filters download links",
                all("download" not in h["path"].lower() for h in hits),
                "no /download paths in results",
            )

            if hits:
                rec = payload(await session.call_tool("aa_open_record", {"path": hits[0]["path"]}))
                ok = isinstance(rec, dict) and bool(rec.get("text"))
                record("aa_open_record", ok, (rec.get("title", "") if isinstance(rec, dict) else "")[:90])
                record(
                    "aa_open_record strips scripts",
                    ok and "console.log" not in rec["text"],
                    "no <script> body in extracted text",
                )

            guide = payload(await session.call_tool("aa_llm_guide"))
            record("aa_llm_guide", isinstance(guide, dict) and bool(guide.get("text")))

            for name, path, needle in [
                ("download endpoint blocked", "/download/abc123", "not exposed"),
                ("slow_download blocked", "/slow_download/abc123", "not exposed"),
                ("torrent endpoint blocked", "/torrents/x", "not exposed"),
                ("remote host blocked", "https://annas-archive.org/md5/abc", "not local"),
                ("non-text response refused", "/blob.bin", "non-text"),
            ]:
                res = await session.call_tool("aa_open_record", {"path": path})
                msg = str(payload(res))
                record(name, bool(res.is_error) and needle in msg, msg[:110])

    # A dead endpoint must produce an actionable message, not a stack trace.
    dead = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER)],
        env={**os.environ, "AA_BASE_URL": "http://127.0.0.1:9"},
    )
    async with stdio_client(dead) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            res = await session.call_tool("aa_health")
            msg = str(payload(res))
            record("unreachable instance explained", bool(res.is_error) and "Cannot reach" in msg, msg[:110])

    # A non-local AA_BASE_URL must be rejected outright.
    remote_base = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER)],
        env={**os.environ, "AA_BASE_URL": "https://annas-archive.org"},
    )
    async with stdio_client(remote_base) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            res = await session.call_tool("aa_health")
            msg = str(payload(res))
            record("non-local AA_BASE_URL rejected", bool(res.is_error) and "must point to a local" in msg, msg[:110])

    failed = [r for r in results if r[0] == FAIL]
    print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
    if failed:
        print(json.dumps([{"check": n, "detail": d} for _, n, d in failed], indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
