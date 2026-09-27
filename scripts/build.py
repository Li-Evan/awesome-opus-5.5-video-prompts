# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Render the README, category pages, the director's toolkit and the website from data/*.yaml.

Usage:
  uv run scripts/build.py          # write files
  uv run scripts/build.py --check  # fail if data is invalid or generated files are stale
"""

import html
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPO = "Li-Evan/awesome-opus-5.5-video-prompts"
REPO_URL = f"https://github.com/{REPO}"
SITE_URL = "https://li-evan.github.io/awesome-opus-5.5-video-prompts/"
BLOB = f"{REPO_URL}/blob/main"
FEATURED = 6
TOP = 12
COLUMNS = 3

KINDS = {
    "one-shot": ("One-shot", "一句话"),
    "brief": ("Brief", "短描述"),
    "template": ("Template", "模板"),
    "spec": ("Spec", "详细规格"),
    "pipeline": ("Pipeline", "多工具流程"),
}
TOOLS = {
    "canvas": "Canvas", "svg": "SVG", "threejs": "Three.js", "webgl": "WebGL", "p5js": "p5.js", "remotion": "Remotion",
    "hyperframes": "HyperFrames", "manim": "Manim", "blender": "Blender", "gsap": "GSAP", "webaudio": "Web Audio",
    "tts": "TTS", "elevenlabs": "ElevenLabs", "seedance": "Seedance", "veo": "Veo", "kling": "Kling", "ffmpeg": "ffmpeg",
    "playwright": "Playwright", "python": "Python", "claude-code": "Claude Code", "claude-app": "Claude app",
    "suno": "Suno", "lyria": "Lyria", "whisper": "Whisper", "gpt-image": "GPT Image", "nano-banana": "Nano Banana",
    "runway": "Runway", "higgsfield": "Higgsfield", "magnific": "Magnific", "fal": "fal", "figma": "Figma",
}
INPUTS = {
    "none": ("No inputs", "无需素材"), "images": ("Images", "图片"), "screenshots": ("Screenshots", "截图"),
    "logo": ("Logo", "Logo"), "music": ("Music", "音乐"), "footage": ("Footage", "视频素材"),
    "reference-video": ("Reference video", "参考视频"), "script": ("Script", "脚本"), "data": ("Data", "数据"),
    "brand": ("Brand kit", "品牌素材"),
}
PLATFORMS = {"x": "X", "reddit": "Reddit", "linuxdo": "LINUX DO", "bilibili": "Bilibili", "xhs": "小红书", "web": "Web"}
LANG_NAMES = {"en": ("English", "英文"), "zh": ("Chinese", "中文"), "ja": ("Japanese", "日文"), "es": ("Spanish", "西班牙文"),
              "pt": ("Portuguese", "葡萄牙文"), "fr": ("French", "法文"), "de": ("German", "德文"), "ko": ("Korean", "韩文"),
              "it": ("Italian", "意大利文"), "ru": ("Russian", "俄文"), "tr": ("Turkish", "土耳其文"), "id": ("Indonesian", "印尼文"),
              "ar": ("Arabic", "阿拉伯文"), "vi": ("Vietnamese", "越南文"), "nl": ("Dutch", "荷兰文"), "pl": ("Polish", "波兰文")}
REQUIRED = ("id", "title", "title_zh", "url", "author", "date", "description", "description_zh", "prompt", "prompt_lang", "kind")
# Other people's lists: discovery only, never linked.
AGGREGATORS = ("github.com/athemeroy/awesome-opus-5-5-videos", "github.com/yihui-dev/awesome-opus5-5-videos",
               "github.com/joeseesun/opus-video-prompts", "github.com/chuspeeism/awesome-opus-5-5-videos",
               "github.com/krillinai/awesome-opus-animation", "github.com/tripogrowthlab/awesome-opus-5-5-prompts",
               "github.com/opusvideo/awesome-claude-video", "github.com/ismoshushi/awesome-opus-video-skills",
               "skillry.dev", "youmind.com", "img.dsxzai.com")

T = {
    "en": {
        "readme": "README.md", "other_readme": "README.zh-CN.md", "switch": "**English** · [简体中文](README.zh-CN.md)",
        "tagline": "Prompts people actually used to make videos with Claude Opus 5.5, copied word for word from each creator's own post.",
        "lead": ("**{n} prompts from {c} creators**, each with a preview, the original post, a Chinese translation, and notes on "
                 "tools, inputs and cost. Opus 5.5 does not generate pixels: it writes code that draws every frame, so the prompt is the whole recipe."),
        "open_site": "▶ Open the gallery", "toolkit": "Director's toolkit", "contribute": "Contribute",
        "why": "Why this list",
        "why_items": [
            "**Verified at the source.** Every prompt is copied from the creator's own post, thread or reply and machine-checked against it. No paraphrases, no prompts from other people's lists.",
            "**Bilingual.** Every prompt keeps its original language and comes with an English or Chinese translation.",
            "**Learn to direct, not just copy.** The toolkit explains how the best prompts are built, the words that change a render, and how to fix a one-shot result.",
        ],
        "contents": "Contents", "quick": "Quick Start", "try": "Three prompts to try first",
        "browse": "Browse by Category", "top": "Most-Saved Prompts",
        "top_intro": "Ranked by bookmarks on the original post, the best signal of \"I want to reuse this\".",
        "see_all": "See all {n} prompts →", "prompts_n": "{n} prompts", "resources": "Tools, Skills and Guides",
        "method": "How Entries Are Collected", "rights": "Rights and Takedown", "contributing": "Contributing",
        "back": "← Back to the list", "sorted": "{n} prompts, most saved first.", "original": "Original post ↗",
        "translation": "中文译文", "translation_en": "English translation", "note": "Note",
        "partial": "The author shared only part of this prompt.", "prompt_from": "Prompt posted in [this reply]({u}).",
        "full_toolkit": "Read the full toolkit →", "vocab_more": "{n} more terms in the full toolkit →",
        "watch": "Watch the video ↗", "remakes": "Also rendered from this prompt by", "count_label": "prompts", "tools_label": "Tools", "inputs_label": "Inputs", "effort_label": "Effort",
        "method_text": [
            "Candidates came from X search, Reddit, LINUX DO, and posts that other lists and galleries pointed to (used only to find original posts, never copied).",
            "For each candidate we fetched the post, the author's thread and the author's replies, and kept it only if the author shared the prompt text there.",
            "A validator checks that every prompt in this list is a verbatim substring of the author's own text. Titles, descriptions and translations are written for this list.",
            "Metrics (bookmarks, likes, views) are snapshots from the date in the footer of the site; previews stream from the original post and are not re-hosted.",
        ],
        "rights_text": ("Prompts, videos and thumbnails belong to their creators and are quoted here for reference with a link to the source. "
                        "The curation, descriptions, translations and the director's toolkit are released under [CC BY 4.0](LICENSE). "
                        "If you are a creator and want your prompt removed or credited differently, [open an issue]({repo}/issues/new?template=creator-request.yml) and it will be handled quickly."),
        "contrib_text": "Found a prompt that belongs here? Read [contributing.md](contributing.md) and open an issue or pull request with the link to the creator's post.",
        "updated": "Last updated {d}.",
    },
    "zh": {
        "readme": "README.zh-CN.md", "other_readme": "README.md", "switch": "[English](README.md) · **简体中文**",
        "tagline": "大家真正用 Claude Opus 5.5 做出视频的提示词，每一条都从作者本人的帖子里逐字摘录。",
        "lead": ("**{n} 条提示词，来自 {c} 位创作者**。每条都有预览、原帖链接、英文或中文译文，以及用到的工具、需要的素材和作者自述的耗时成本。"
                 "Opus 5.5 不直接生成画面，而是写代码画出每一帧，所以提示词就是完整的配方。"),
        "open_site": "▶ 打开在线画廊", "toolkit": "导演工具箱", "contribute": "参与贡献",
        "why": "这个列表有什么不同",
        "why_items": [
            "**回原帖核实。** 每条提示词都从作者本人的帖子、串推或回复里摘录，并用程序逐字比对。不收转述，不从别人的合集里抄。",
            "**中英对照。** 每条提示词保留原文，同时附中文或英文译文。",
            "**不只是抄，还教你当导演。** 工具箱讲清楚好提示词的结构、能精确改动成片的镜头词汇，以及一句话出片后该怎么修。",
        ],
        "contents": "目录", "quick": "三分钟上手", "try": "先试这三条",
        "browse": "按分类浏览", "top": "收藏最多的提示词",
        "top_intro": "按原帖的收藏数排序。收藏数最能说明「我想拿来用」。",
        "see_all": "查看全部 {n} 条 →", "prompts_n": "{n} 条", "resources": "工具、Skill 与教程",
        "method": "收录方法", "rights": "版权与下架",
        "contributing": "参与贡献", "back": "← 返回列表", "sorted": "共 {n} 条，按收藏数排序。", "original": "原帖 ↗",
        "translation": "English translation", "translation_en": "English translation", "note": "备注",
        "partial": "作者只公开了这条提示词的一部分。", "prompt_from": "提示词发在[这条回复]({u})里。",
        "full_toolkit": "查看完整工具箱 →", "vocab_more": "完整工具箱里还有 {n} 个词 →",
        "watch": "观看视频 ↗", "remakes": "用同一条提示词做过的还有", "count_label": "条", "tools_label": "工具", "inputs_label": "素材", "effort_label": "Effort",
        "method_text": [
            "候选来自 X 搜索、Reddit、LINUX DO，以及其他列表和画廊指向的原帖（只用来找原帖，不抄它们的内容）。",
            "每条候选都抓取了原帖、作者的串推和作者在评论区的回复，只有作者本人在其中公开了提示词原文才收录。",
            "校验程序会检查每条提示词都是作者原文的逐字子串。标题、说明和译文由本列表撰写。",
            "收藏、点赞、浏览数是网站页脚日期那天的快照；预览视频直接从原帖加载，不转存。",
        ],
        "rights_text": ("提示词、视频和封面归原作者所有，这里引用供参考并附原帖链接。"
                        "整理、说明、译文和导演工具箱以 [CC BY 4.0](LICENSE) 协议发布。"
                        "如果你是作者，希望撤下提示词或调整署名，请[提一个 issue]({repo}/issues/new?template=creator-request.yml)，会尽快处理。"),
        "contrib_text": "发现应该收录的提示词？请阅读 [contributing.zh-CN.md](contributing.zh-CN.md)，带上作者原帖链接提 issue 或 PR。",
        "updated": "最后更新于 {d}。",
    },
}


def fail(msg):
    sys.exit(f"build error: {msg}")


def load():
    order = yaml.safe_load((DATA / "sections.yaml").read_text())["categories"]
    cats = []
    for slug in order:
        sec = yaml.safe_load((DATA / f"{slug}.yaml").read_text())
        sec["slug"] = slug
        sec["entries"] = sec.get("entries") or []
        for e in sec["entries"]:
            e["category"] = slug
        cats.append(sec)
    toolkit = yaml.safe_load((DATA / "toolkit.yaml").read_text())
    resources = yaml.safe_load((DATA / "resources.yaml").read_text())
    return cats, toolkit, resources


def validate(cats, resources):
    ids, urls = {}, {}
    for sec in cats:
        if "️" in sec["emoji"]:
            fail(f"{sec['slug']}: emoji contains U+FE0F")
        for e in sec["entries"]:
            where = f"{sec['slug']}:{e.get('id')}"
            for k in REQUIRED:
                if not str(e.get(k) or "").strip():
                    fail(f"{where} missing {k}")
            if e["id"] in ids:
                fail(f"duplicate id {e['id']} ({ids[e['id']]} and {sec['slug']})")
            ids[e["id"]] = sec["slug"]
            if e["url"] in urls:
                fail(f"duplicate url {e['url']}")
            urls[e["url"]] = e["id"]
            if e["kind"] not in KINDS:
                fail(f"{where} unknown kind {e['kind']}")
            for t in e.get("tools") or []:
                if t not in TOOLS:
                    fail(f"{where} unknown tool {t}")
            for i in e.get("inputs") or []:
                if i not in INPUTS:
                    fail(f"{where} unknown input {i}")
            lang = e["prompt_lang"]
            if lang != "zh" and not (e.get("prompt_zh") or "").strip():
                fail(f"{where} needs prompt_zh")
            if lang != "en" and not (e.get("prompt_en") or "").strip():
                fail(f"{where} needs prompt_en")
            if is_aggregator(e["url"]):
                fail(f"{where} links an aggregator")
    for g in resources["groups"]:
        for r in g["entries"]:
            if is_aggregator(r["url"]):
                fail(f"resource {r['name']} links an aggregator")


def is_aggregator(url):
    p = urlparse(url.lower())
    path = p.netloc.removeprefix("www.") + p.path.rstrip("/")
    return any(path == a or path.startswith(a + "/") or p.netloc.endswith(a) for a in AGGREGATORS)


def pick(e, key, lang):
    return (e.get(f"{key}_zh") if lang == "zh" else None) or e.get(key) or ""


def fmt_n(n):
    n = int(n or 0)
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M".replace(".0M", "M")
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def score(e):
    m = e.get("metrics") or {}
    return (m.get("bookmarks") or 0, m.get("likes") or 0, m.get("views") or 0)


def anchor(text):
    a = text.strip().lower()
    a = re.sub(r"[^\w\- 一-鿿]", "", a)
    return a.replace(" ", "-")


def esc(s):
    return html.escape(str(s or ""), quote=True)


def fence(text):
    ticks = "```"
    while ticks in text:
        ticks += "`"
    return f"{ticks}text\n{text.rstrip()}\n{ticks}"


def meta_line(e, lang):
    m = e.get("metrics") or {}
    plat = e.get("platform", "x")
    if plat == "x":
        bits = [f"[@{e['author']}](https://x.com/{e['author']})"]
    else:
        prefix = "u/" if plat == "reddit" else "@"
        bits = [f"{prefix}{e['author']} ({PLATFORMS.get(plat, plat)})"]
    bits.append(str(e["date"])[:10])
    if m.get("bookmarks"):
        bits.append(f"🔖 {fmt_n(m['bookmarks'])}")
    if m.get("views"):
        bits.append(f"▶ {fmt_n(m['views'])}")
    bits.append(f"`{KINDS[e['kind']][1 if lang == 'zh' else 0]}`")
    tools = [TOOLS[t] for t in e.get("tools") or [] if t not in ("claude-code", "claude-app")]
    if tools:
        bits.append(" · ".join(tools[:4]))
    return " · ".join(bits)


def page_path(slug, lang):
    return f"prompts/{slug}.md" if lang == "en" else f"zh-CN/prompts/{slug}.md"


def card(e, lang, link):
    media = e.get("media") or {}
    m = e.get("metrics") or {}
    title = pick(e, "title", lang)
    img = media.get("thumb")
    parts = []
    if img:
        parts.append(f'<a href="{esc(link)}"><img src="{esc(img)}" alt="{esc(title)}" width="100%"></a><br>')
    sub = [("u/" if e.get("platform") == "reddit" else "@") + e["author"]]
    if m.get("bookmarks"):
        sub.append(f"🔖 {fmt_n(m['bookmarks'])}")
    if m.get("views"):
        sub.append(f"▶ {fmt_n(m['views'])}")
    sub.append(KINDS[e["kind"]][1 if lang == "zh" else 0])
    parts.append(f'<b><a href="{esc(link)}">{esc(title)}</a></b><br><sub>{esc(" · ".join(sub))}</sub><br>{esc(pick(e, "description", lang))}')
    return f'<td width="{100 // COLUMNS}%" valign="top">{"".join(parts)}</td>'


def grid(entries, lang, link_fn):
    rows = []
    for i in range(0, len(entries), COLUMNS):
        cells = "".join(card(e, lang, link_fn(e)) for e in entries[i:i + COLUMNS])
        rows.append(f"<tr>\n{cells}\n</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def entry_link(e, lang, from_root=True):
    slug = e["category"]
    base = f"{BLOB}/{page_path(slug, lang)}"
    return f"{base}#{anchor(pick(e, 'title', lang))}"


def render_readme(cats, toolkit, resources, lang, today):
    t = T[lang]
    entries = [e for s in cats for e in s["entries"]]
    creators = {e["author"].lower() for e in entries}
    L = []
    L.append('<div align="center">\n')
    L.append(f'<a href="{SITE_URL}{"?lang=zh" if lang == "zh" else ""}"><img src="site/banner.png" alt="Awesome Opus 5.5 Video Prompts" width="100%"></a>\n')
    L.append("# Awesome Opus 5.5 Video Prompts [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
    L.append(f"{t['tagline']}\n")
    L.append(f"{t['switch']}\n")
    site = SITE_URL + ("?lang=zh" if lang == "zh" else "")
    tk = "guide/director-toolkit.md" if lang == "en" else "zh-CN/guide/director-toolkit.md"
    contrib = "contributing.md" if lang == "en" else "contributing.zh-CN.md"
    L.append(f"**[{t['open_site']}]({site})** · [{t['toolkit']}]({tk}) · [{t['contribute']}]({contrib})\n")
    L.append("</div>\n")
    L.append(t["lead"].format(n=len(entries), c=len(creators)) + "\n")
    L.append(f"## {t['why']}\n")
    L.extend(f"- {x}" for x in t["why_items"])
    L.append("")
    toc = [(t["quick"], anchor(t["quick"])), (t["top"], anchor(t["top"])), (t["browse"], anchor(t["browse"]))]
    toc_sub = [(f"{s['emoji']} {pick(s, 'title', lang)}", anchor(f"{s['emoji']} {pick(s, 'title', lang)}")) for s in cats]
    toc += [(pick(toolkit["workflow"], "title", lang), anchor(pick(toolkit["workflow"], "title", lang))),
            (t["resources"], anchor(t["resources"])), (t["method"], anchor(t["method"])),
            (t["rights"], anchor(t["rights"])), (t["contributing"], anchor(t["contributing"]))]
    L.append(f"## {t['contents']}\n")
    for i, (name, a) in enumerate(toc):
        L.append(f"- [{name}](#{a})")
        if name == t["browse"]:
            L.extend(f"  - [{n}](#{x})" for n, x in toc_sub)
    L.append("")

    q = toolkit["quickstart"]
    L.append(f"## {t['quick']}\n")
    L.append(pick(q, "intro", lang).strip() + "\n")
    for i, s in enumerate(q["steps"], 1):
        L.append(f"{i}. {s['zh' if lang == 'zh' else 'en']}")
    L.append("")
    L.append(f"**{t['try']}**\n")
    starters = pick_starters(entries)
    for e in starters:
        L.append(f"- **{pick(e, 'title', lang)}** ({meta_line(e, lang)})\n")
        L.append(indent(fence(e["prompt"]), "  ") + "\n")

    L.append(f"## {t['top']}\n")
    L.append(t["top_intro"] + "\n")
    top = sorted(entries, key=score, reverse=True)[:TOP]
    L.append(grid(top, lang, lambda e: entry_link(e, lang)) + "\n")

    L.append(f"## {t['browse']}\n")
    L.append("| | " + (" | ".join(["Category", "Prompts"] if lang == "en" else ["分类", "数量"])) + " |")
    L.append("|---|---|---:|")
    for s in cats:
        L.append(f"| {s['emoji']} | [{pick(s, 'title', lang)}]({page_path(s['slug'], lang)}) | {len(s['entries'])} |")
    L.append("")
    for s in cats:
        es = sorted(s["entries"], key=score, reverse=True)
        L.append(f"### {s['emoji']} {pick(s, 'title', lang)}\n")
        L.append(pick(s, "description", lang) + "\n")
        if es:
            L.append(grid(es[:FEATURED], lang, lambda e: entry_link(e, lang)) + "\n")
        L.append(f"**[{t['see_all'].format(n=len(es))}]({page_path(s['slug'], lang)})**\n")

    L.extend(render_toolkit_summary(toolkit, lang, tk))
    L.extend(render_resources(resources, lang, level="##"))
    L.append(f"## {t['method']}\n")
    L.extend(f"- {x}" for x in t["method_text"])
    L.append("")
    L.append(f"## {t['rights']}\n")
    L.append(t["rights_text"].format(repo=REPO_URL) + "\n")
    L.append(f"## {t['contributing']}\n")
    L.append(t["contrib_text"] + "\n")
    L.append(f"<sub>{t['updated'].format(d=today)}</sub>\n")
    return "\n".join(L)


def indent(text, pad):
    return "\n".join(pad + line if line else line for line in text.splitlines())


def pick_starters(entries):
    by_id = {e["id"]: e for e in entries}
    chosen = []
    one = [e for e in entries if e["kind"] == "one-shot" and e["prompt_lang"] == "en"]
    zh = [e for e in entries if e["prompt_lang"] == "zh" and len(e["prompt"]) < 400]
    tpl = [e for e in entries if e["kind"] in ("template", "spec") and len(e["prompt"]) < 2500]
    for pool in (one, zh, tpl):
        pool = sorted(pool, key=score, reverse=True)
        for e in pool:
            if e["id"] not in {c["id"] for c in chosen}:
                chosen.append(e)
                break
    return [c for c in chosen if c["id"] in by_id]


def render_toolkit_summary(tk, lang, tk_path):
    t = T[lang]
    L = []
    w = tk["workflow"]
    L.append(f"## {pick(w, 'title', lang)}\n")
    L.append(f"{pick(w, 'credit', lang)} [↗]({w['credit_url']})\n")
    L.append("| # | " + ("Step | What to do" if lang == "en" else "步骤 | 怎么做") + " |")
    L.append("|---|---|---|")
    for i, s in enumerate(w["steps"], 1):
        L.append(f"| {i} | **{pick(s, 'title', lang)}** | {s['zh' if lang == 'zh' else 'en']} |")
    L.append("")
    v = tk["vocabulary"]
    L.append(f"### {pick(v, 'title', lang)}\n")
    L.append(pick(v, "intro", lang) + "\n")
    head = "| Term | When you want | Say |" if lang == "en" else "| 术语 | 你想要 | 这样说 |"
    L.append(head)
    L.append("|---|---|---|")
    for term in v["terms"][:8]:
        L.append(f"| `{term['term']}` | {pick(term, 'want', lang)} | {pick(term, 'say', lang)} |")
    L.append("")
    L.append(f"[{t['vocab_more'].format(n=len(v['terms']) - 8)}]({tk_path})\n")
    c = tk["checklist"]
    L.append(f"### {pick(c, 'title', lang)}\n")
    L.append(f"{pick(c, 'intro', lang)} {pick(c, 'credit', lang)} [↗]({c['credit_url']})\n")
    for item in c["items"]:
        L.append(f"- [ ] {item['zh' if lang == 'zh' else 'en']} → {pick(item, 'fix', lang)}")
    L.append("")
    L.append(f"**[{t['full_toolkit']}]({tk_path})**\n")
    return L


def render_resources(res, lang, level="##"):
    t = T[lang]
    L = [f"{level} {t['resources']}\n"]
    for g in res["groups"]:
        L.append(f"{level}# {pick(g, 'title', lang)}\n")
        for r in g["entries"]:
            stars = f" ⭐ {fmt_n(r['stars'])}" if r.get("stars") else ""
            L.append(f"- [{pick(r, 'name', lang)}]({r['url']}){stars} - {pick(r, 'description', lang)}")
        L.append("")
    return L


def render_category(sec, lang, today):
    t = T[lang]
    es = sorted(sec["entries"], key=score, reverse=True)
    other = page_path(sec["slug"], "zh" if lang == "en" else "en")
    up = "../" if lang == "en" else "../../"
    readme = up + ("README.md" if lang == "en" else "README.zh-CN.md")
    switch = f"**English** · [简体中文]({up}{other})" if lang == "en" else f"[English]({up}{other}) · **简体中文**"
    L = [f"# {sec['emoji']} {pick(sec, 'title', lang)}\n", f"[{t['back']}]({readme}) · {switch}\n",
         pick(sec, "description", lang) + " " + t["sorted"].format(n=len(es)) + "\n"]
    for e in es:
        title = pick(e, "title", lang)
        media = e.get("media") or {}
        L.append(f"### {title}\n")
        if media.get("thumb"):
            L.append(f'<a href="{esc(e["url"])}"><img src="{esc(media["thumb"])}" alt="{esc(title)}" width="480"></a>\n')
        L.append(meta_line(e, lang) + "\n")
        L.append(pick(e, "description", lang) + "\n")
        if e.get("partial"):
            L.append(f"> {t['partial']}\n")
        L.append(fence(e["prompt"]) + "\n")
        tr, label = translation(e, lang)
        if tr:
            L.append(f"<details><summary>{label}</summary>\n\n{fence(tr)}\n\n</details>\n")
        extras = []
        if e.get("inputs") and e["inputs"] != ["none"]:
            extras.append(f"{t['inputs_label']}: " + ", ".join(INPUTS[i][1 if lang == 'zh' else 0] for i in e["inputs"]))
        if e.get("effort"):
            extras.append(f"{t['effort_label']}: {e['effort']}")
        note = pick(e, "note", lang)
        if note:
            extras.append(note)
        if extras:
            L.append("<sub>" + esc(" · ".join(extras)) + "</sub>\n")
        if e.get("remakes"):
            who = ", ".join(f"[@{r['author']}]({r['url']})" for r in e["remakes"][:12])
            more = f" +{len(e['remakes']) - 12}" if len(e["remakes"]) > 12 else ""
            L.append(f"<sub>{t['remakes']}: {who}{more}</sub>\n")
        links = [f"[{t['original']}]({e['url']})"]
        if e.get("watch_url"):
            links.append(f"[{t['watch']}]({e['watch_url']})")
        if e.get("prompt_url") and e["prompt_url"] != e["url"]:
            links.append(t["prompt_from"].format(u=e["prompt_url"]))
        L.append(" · ".join(links) + "\n")
        L.append("---\n")
    L.append(f"<sub>{t['updated'].format(d=today)}</sub>\n")
    return "\n".join(L)


def translation(e, lang):
    """The one translation worth showing next to the original on a page in `lang`."""
    src = e["prompt_lang"]
    if src == "zh":
        return e.get("prompt_en"), "English translation"
    if lang == "zh" or src == "en":
        return e.get("prompt_zh"), "中文译文"
    return e.get("prompt_en"), "English translation"


def render_toolkit_page(tk, lang):
    up = "../" if lang == "en" else "../../"
    readme = up + ("README.md" if lang == "en" else "README.zh-CN.md")
    other = "zh-CN/guide/director-toolkit.md" if lang == "en" else "guide/director-toolkit.md"
    switch = f"**English** · [简体中文]({up}{other})" if lang == "en" else f"[English]({up}{other}) · **简体中文**"
    title = "Director's Toolkit" if lang == "en" else "导演工具箱"
    L = [f"# {title}\n", f"[{T[lang]['back']}]({readme}) · {switch}\n"]
    q = tk["quickstart"]
    L.append(f"## {pick(q, 'title', lang)}\n")
    L.append(pick(q, "intro", lang).strip() + "\n")
    for i, s in enumerate(q["steps"], 1):
        L.append(f"{i}. {s['zh' if lang == 'zh' else 'en']}")
    L.append("")
    w = tk["workflow"]
    L.append(f"## {pick(w, 'title', lang)}\n")
    L.append(f"{pick(w, 'credit', lang)} [↗]({w['credit_url']})\n")
    for i, s in enumerate(w["steps"], 1):
        L.append(f"### {i}. {pick(s, 'title', lang)}\n")
        L.append(s["zh" if lang == "zh" else "en"] + "\n")
    a = tk["anatomy"]
    L.append(f"## {pick(a, 'title', lang)}\n")
    L.append(f"{pick(a, 'credit', lang)} [↗]({a['credit_url']})\n")
    L.append("| " + ("Section | What goes in it" if lang == "en" else "段落 | 写什么") + " |")
    L.append("|---|---|")
    for p in a["parts"]:
        L.append(f"| `{p['tag']}` | {p['zh' if lang == 'zh' else 'en']} |")
    L.append("")
    v = tk["vocabulary"]
    L.append(f"## {pick(v, 'title', lang)}\n")
    L.append(pick(v, "intro", lang) + "\n")
    L.append("| Term | When you want | Say |" if lang == "en" else "| 术语 | 你想要 | 这样说 |")
    L.append("|---|---|---|")
    for term in v["terms"]:
        L.append(f"| `{term['term']}` | {pick(term, 'want', lang)} | {pick(term, 'say', lang)} |")
    L.append("")
    c = tk["checklist"]
    L.append(f"## {pick(c, 'title', lang)}\n")
    L.append(f"{pick(c, 'intro', lang)} {pick(c, 'credit', lang)} [↗]({c['credit_url']})\n")
    L.append("| " + ("Symptom | Fix" if lang == "en" else "症状 | 改法") + " |")
    L.append("|---|---|")
    for item in c["items"]:
        L.append(f"| {item['zh' if lang == 'zh' else 'en']} | {pick(item, 'fix', lang)} |")
    L.append("")
    return "\n".join(L)


def site_data(cats, toolkit, resources, today):
    entries = []
    for s in cats:
        for e in s["entries"]:
            d = {k: e.get(k) for k in ("id", "title", "title_zh", "url", "watch_url", "author", "author_name", "platform", "date", "description",
                                       "description_zh", "prompt", "prompt_lang", "prompt_en", "prompt_zh", "prompt_url", "partial",
                                       "kind", "tools", "inputs", "effort", "note", "note_zh", "media", "metrics", "category", "remakes")}
            entries.append({k: v for k, v in d.items() if v not in (None, "", [], False)})
    return {
        "updated": today,
        "categories": [{k: s[k] for k in ("slug", "emoji", "title", "title_zh", "description", "description_zh")} for s in cats],
        "kinds": {k: {"en": v[0], "zh": v[1]} for k, v in KINDS.items()},
        "tools": TOOLS,
        "inputs": {k: {"en": v[0], "zh": v[1]} for k, v in INPUTS.items()},
        "langs": {k: {"en": v[0], "zh": v[1]} for k, v in LANG_NAMES.items()},
        "toolkit": toolkit,
        "resources": resources,
        "entries": entries,
    }


def write(path, text, check, stale):
    path = ROOT / path
    if check:
        if not path.exists() or path.read_text() != text:
            stale.append(str(path.relative_to(ROOT)))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def main():
    check = "--check" in sys.argv
    cats, toolkit, resources = load()
    validate(cats, resources)
    stamp = ROOT / "data" / "updated.txt"
    today = stamp.read_text().strip() if stamp.exists() else date.today().isoformat()
    stale = []
    for lang in ("en", "zh"):
        write(T[lang]["readme"], render_readme(cats, toolkit, resources, lang, today), check, stale)
        for s in cats:
            write(page_path(s["slug"], lang), render_category(s, lang, today), check, stale)
        write("guide/director-toolkit.md" if lang == "en" else "zh-CN/guide/director-toolkit.md", render_toolkit_page(toolkit, lang), check, stale)
    data = site_data(cats, toolkit, resources, today)
    n = len(data["entries"])
    write("site/data.json", json.dumps(data, ensure_ascii=False, separators=(",", ":")), check, stale)
    tpl = (ROOT / "site" / "template.html").read_text()
    creators = len({e["author"].lower() for e in data["entries"]})
    page = (tpl.replace("{{COUNT}}", str(n)).replace("{{CREATORS}}", str(creators)).replace("{{UPDATED}}", today)
               .replace("{{SITE_URL}}", SITE_URL).replace("{{REPO_URL}}", REPO_URL))
    write("index.html", page, check, stale)
    urls = [SITE_URL, SITE_URL + "?lang=zh"]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{html.escape(u)}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sitemap, check, stale)
    if check and stale:
        fail("generated files are stale, run `uv run scripts/build.py`: " + ", ".join(stale))
    print(f"{'checked' if check else 'built'} {n} prompts from {creators} creators in {len(cats)} categories")


if __name__ == "__main__":
    main()
