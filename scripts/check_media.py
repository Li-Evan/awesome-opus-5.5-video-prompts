# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Check that every thumbnail and preview video still loads (without a referrer, like the site).

Usage:
  uv run scripts/check_media.py                        # print broken media
  uv run scripts/check_media.py --report dead-media.md # also write a markdown report when something is broken
"""

import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def alive(url, tries=3):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Range": "bytes=0-1023"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status < 400
        except urllib.error.HTTPError as err:
            if err.code in (403, 404, 410):
                return False
        except Exception:
            pass
        time.sleep(2 * (i + 1))
    return False


def main():
    order = yaml.safe_load((ROOT / "data" / "sections.yaml").read_text())["categories"]
    checks = []
    for slug in order:
        for e in yaml.safe_load((ROOT / "data" / f"{slug}.yaml").read_text()).get("entries") or []:
            for key in ("thumb", "video"):
                url = (e.get("media") or {}).get(key)
                if url:
                    checks.append((slug, e["id"], key, url))
    with ThreadPoolExecutor(12) as ex:
        results = list(ex.map(lambda c: alive(c[3]), checks))
    dead = [c for c, ok in zip(checks, results) if not ok]
    for slug, eid, key, url in dead:
        print(f"{slug}/{eid} {key} {url}")
    print(f"{len(checks) - len(dead)}/{len(checks)} media URLs load")
    if dead and "--report" in sys.argv:
        path = Path(sys.argv[sys.argv.index("--report") + 1])
        lines = ["These previews or thumbnails no longer load. Remove the `media` key or refresh it from the original post.", ""]
        lines += [f"- `data/{slug}.yaml` · `{eid}` · {key}: {url}" for slug, eid, key, url in dead]
        path.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
