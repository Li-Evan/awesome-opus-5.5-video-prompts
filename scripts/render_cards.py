# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright", "pillow"]
# ///
"""Render site/og.png (1200x630) and site/banner.png (1600x560) from site/og.html with the local Chrome.

Usage: uv run scripts/render_cards.py [comma-separated entry ids for the film strip]
"""

import functools
import http.server
import sys
import threading
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SIZES = {"og.png": (1200, 630), "banner.png": (1600, 560)}


def main():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT / "site"))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    query = f"?ids={sys.argv[1]}" if len(sys.argv) > 1 else ""
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        for name, (w, h) in SIZES.items():
            page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            page.goto(f"http://127.0.0.1:{server.server_port}/og.html{query}")
            page.wait_for_selector("body[data-ready]", timeout=60000)
            page.wait_for_timeout(300)
            out = ROOT / "site" / name
            page.screenshot(path=str(out))
            # 256-color palette keeps the README light; the grain hides the banding
            Image.open(out).convert("RGB").quantize(256, dither=Image.Dither.FLOYDSTEINBERG).save(out, optimize=True)
            print(f"site/{name} {w}x{h}")
        browser.close()
    server.shutdown()


if __name__ == "__main__":
    main()
