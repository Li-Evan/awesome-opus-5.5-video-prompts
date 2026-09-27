# Contribution Guidelines

**English** · [简体中文](contributing.zh-CN.md)

Thanks for helping build the most useful library of prompts people used to make videos with Claude Opus 5.5. By contributing you agree to follow the [Code of Conduct](code-of-conduct.md).

## What belongs here

A prompt qualifies when all four are true:

1. **The creator shared the prompt text itself**, in the post, its thread, or their own replies. "I made this with one prompt" without the prompt does not count, and neither does a prompt that only appears in a screenshot.
2. **Opus 5.5 made it**, through Claude Code, the Claude app, or the API. Pipelines that add other tools (ElevenLabs, Seedance, Blender, and so on) are welcome as long as Opus wrote the code or directed the build.
3. **The result is a rendered video or animation**: an MP4, a loop, an explainer, a motion graphic. Games, apps, and websites belong only when the post is about a rendered video of them.
4. **It is not an ad, spam, or NSFW.**

Not accepted:

- Other people's lists, galleries, and prompt directories. Link the creator's original post instead; the build fails on known aggregators.
- Prompts copied from somewhere other than the creator's own words.
- Anything that leaks API keys or private data.

## The three rules

1. **Link the original.** `url` points to the creator's own post (X, Reddit, LINUX DO, Bilibili, 小红书, or their own page).
2. **Copy the prompt verbatim.** Same characters, line breaks, typos, and casing. Strip only labels like `Prompt:` and wrapping quotes. If the creator shared only part of it, set `partial: true`.
3. **Translate, don't rewrite.** English prompts get a Chinese translation in `prompt_zh`; Chinese prompts get `prompt_en`; any other language gets both. Keep code, tags like `<inputs>`, file names, numbers, and quoted on-screen text as they are.

## How to add a prompt

`README.md`, `README.zh-CN.md`, `prompts/`, `zh-CN/`, `guide/`, `index.html`, and `site/data.json` are generated. Do not edit them by hand.

1. Pick the category file in `data/`:

   | File | What goes there |
   |---|---|
   | `showreel.yaml` | Showreels, abstract motion graphics, UI motion, kinetic type |
   | `launch.yaml` | Product launches, app and SaaS promos, brand films, ads |
   | `explainer.yaml` | Science, math, tech, how-it-works, data stories |
   | `history.yaml` | Timelines, civilizations, biographies, documentary style |
   | `music.yaml` | Music videos, lyric videos, audio-reactive pieces |
   | `story.yaml` | Narrative shorts, hand-drawn, line art, poems |
   | `self.yaml` | Videos about Claude itself |
   | `worlds.yaml` | 3D scenes, flythroughs, simulations, shaders |
   | `remix.yaml` | Turning existing footage, screenshots, or a reference video into a new video |

2. Add an entry. Required fields are marked; everything else is optional.

   ```yaml
   - id: twoclipping-402193               # required: <author lowercase>-<last 6 digits of the post id>
     title: One-shape UI morph loop       # required: what the video is, 8 words or fewer
     title_zh: 单个形状变形的 UI 动效循环      # required
     url: https://x.com/twoclipping/status/2103273003555402193   # required: the creator's post
     author: twoclipping                  # required: handle without @
     author_name: zero
     platform: x                          # x, reddit, linuxdo, bilibili, xhs, web (default x)
     date: '2026-09-24'                   # required: when the post went up
     description: A square UI motion loop where one shape morphs through eleven states on a 120 BPM grid.   # required, 30 words or fewer
     description_zh: 同一个形状踩着 120 BPM 变成十一种界面状态的方形循环动效。   # required
     prompt: |-                           # required: verbatim
       ...
     prompt_lang: en                      # required: en, zh, ja, es, ...
     prompt_zh: |-                        # translation (see rule 3)
       ...
     partial: true                        # only if the creator shared part of it
     prompt_url: https://x.com/...        # only if the prompt is in a different post than `url`
     watch_url: https://www.bilibili.com/video/...   # only if the video lives somewhere else
     kind: spec                           # required: one-shot, brief, template, spec, pipeline
     tools: [playwright, ffmpeg]          # only tools named by the creator
     inputs: [music]                      # none, images, screenshots, logo, music, footage, reference-video, script, data, brand
     effort: max                          # only if the creator says so: max, xhigh, high, medium
     note: 'Author: about 40 minutes and 3 revisions.'   # time, cost, or tokens as stated by the creator
     note_zh: 作者称约 40 分钟、改了 3 轮。
     media:                               # hotlinked from the original post, never uploaded here
       thumb: https://pbs.twimg.com/...
       video: https://video.twimg.com/...     # a small MP4 for hover previews
       video_hd: https://video.twimg.com/...  # up to 1280 px for the player
     metrics: {bookmarks: 1200, likes: 3400, views: 250000}
   ```

   `kind` in one line each: **one-shot** is one to three sentences; **brief** is a paragraph or a short list of direction; **template** has placeholders or asks you for inputs; **spec** is a long structured document; **pipeline** chains several tools or prompts.

3. Run the build and commit everything it changes:

   ```bash
   uv run scripts/build.py
   ```

   The build checks required fields, duplicate ids and links, the `kind`, `tools`, and `inputs` vocabularies, missing translations, and aggregator links. CI runs the same check with `--check`.

4. Open a pull request. One prompt per pull request is easiest to review.

Don't want to edit YAML? [Open an issue](https://github.com/Li-Evan/awesome-opus-5.5-video-prompts/issues/new/choose) with the link to the creator's post and a maintainer will add it.

## Same prompt, different video

If someone re-runs a prompt that is already listed, do not add a new entry. Add their post to the existing entry's `remakes`:

```yaml
remakes:
  - author: someone
    url: https://x.com/someone/status/...
    thumb: https://pbs.twimg.com/...
    video: https://video.twimg.com/...
```

## Writing style

- Titles and descriptions say what the video is, not how amazing it is. No "insane", "mind-blowing", 「炸裂」, 「震撼」.
- Keep numbers identical to the source.
- Chinese text uses full-width punctuation and a space between Chinese and Latin words or numbers (「用 Three.js 做的 3D 场景」).

## Updating or removing

If a preview stopped playing, a post is gone, or a translation is wrong, open an issue or a pull request. A weekly job checks every thumbnail and preview and opens an issue for the ones that broke.

Creators who want a prompt removed or credited differently can use the [takedown form](https://github.com/Li-Evan/awesome-opus-5.5-video-prompts/issues/new?template=creator-request.yml); these requests are handled first.
