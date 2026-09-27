# 贡献指南

[English](contributing.md) · **简体中文**

感谢你帮忙完善这份 Claude Opus 5.5 视频提示词库。参与贡献即表示你同意遵守[行为准则](code-of-conduct.md)。

## 什么样的提示词能收录

四条同时满足：

1. **作者公开了提示词原文**：写在帖子、帖子串或作者自己的回复里。只说「一句话做的」但没给提示词的不算，提示词只出现在截图里的也不算。
2. **是 Opus 5.5 做的**：通过 Claude Code、Claude App 或 API。加了其他工具（ElevenLabs、Seedance、Blender 等）的流程也欢迎，前提是代码由 Opus 写或由它主导搭建。
3. **产出是渲染好的视频或动画**：MP4、循环动画、讲解视频、动态图形。游戏、App、网站只有在帖子展示的是它们的渲染视频时才收。
4. **不是广告、刷屏或不适宜内容。**

不收：

- 别人整理的列表、画廊和提示词目录。请直接给作者原帖链接；构建脚本会拦截已知的聚合站。
- 不是出自作者本人原话的提示词。
- 任何泄露 API Key 或隐私的内容。

## 三条规则

1. **链接原帖。** `url` 指向作者本人的帖子（X、Reddit、LINUX DO、B 站、小红书或作者自己的页面）。
2. **提示词逐字照抄。** 字符、换行、错别字、大小写都保持原样，只去掉 `Prompt:`、「提示词：」这类标签和外层引号。作者只公开了一部分就标 `partial: true`。
3. **只翻译，不改写。** 英文提示词在 `prompt_zh` 里给中文译文；中文提示词给 `prompt_en`；其他语言两个都给。代码、`<inputs>` 这类标签、文件名、数字和画面上引用的文字保持原样。

## 如何添加

`README.md`、`README.zh-CN.md`、`prompts/`、`zh-CN/`、`guide/`、`index.html` 和 `site/data.json` 都是自动生成的，不要手改。

1. 在 `data/` 里选分类文件：

   | 文件 | 放什么 |
   |---|---|
   | `showreel.yaml` | 作品集、抽象动效、界面动效、动态文字 |
   | `launch.yaml` | 产品发布、App 和 SaaS 宣传片、品牌片、广告 |
   | `explainer.yaml` | 科学、数学、技术原理、数据故事 |
   | `history.yaml` | 历史时间线、文明、人物传记、纪录片风格 |
   | `music.yaml` | MV、歌词视频、随音乐律动的作品 |
   | `story.yaml` | 叙事短片、手绘、线稿、诗 |
   | `self.yaml` | 关于 Claude 自己的视频 |
   | `worlds.yaml` | 3D 场景、镜头穿梭、模拟、着色器 |
   | `remix.yaml` | 把现有素材、截图或参考视频改造成新视频 |

2. 添加条目。标了 required 的必填，其余可选。

   ```yaml
   - id: twoclipping-402193               # required：<作者小写>-<帖子 ID 后 6 位>
     title: One-shape UI morph loop       # required：视频是什么，不超过 8 个词
     title_zh: 单个形状变形的 UI 动效循环      # required
     url: https://x.com/twoclipping/status/2103273003555402193   # required：作者原帖
     author: twoclipping                  # required：不带 @ 的账号名
     author_name: zero
     platform: x                          # x、reddit、linuxdo、bilibili、xhs、web（默认 x）
     date: '2026-09-24'                   # required：发帖日期
     description: A square UI motion loop where one shape morphs through eleven states on a 120 BPM grid.   # required，不超过 30 个词
     description_zh: 同一个形状踩着 120 BPM 变成十一种界面状态的方形循环动效。   # required
     prompt: |-                           # required：逐字照抄
       ...
     prompt_lang: en                      # required：en、zh、ja、es……
     prompt_zh: |-                        # 译文（见规则 3）
       ...
     partial: true                        # 作者只公开了一部分时才写
     prompt_url: https://x.com/...        # 提示词在另一条帖子里时才写
     watch_url: https://www.bilibili.com/video/...   # 视频在别的平台时才写
     kind: spec                           # required：one-shot、brief、template、spec、pipeline
     tools: [playwright, ffmpeg]          # 只写作者提到的工具
     inputs: [music]                      # none、images、screenshots、logo、music、footage、reference-video、script、data、brand
     effort: max                          # 作者说了才写：max、xhigh、high、medium
     note: 'Author: about 40 minutes and 3 revisions.'   # 作者自己说的耗时、成本或 token
     note_zh: 作者称约 40 分钟、改了 3 轮。
     media:                               # 直接引用原帖的媒体，不上传到本仓库
       thumb: https://pbs.twimg.com/...
       video: https://video.twimg.com/...     # 悬停预览用的小尺寸 MP4
       video_hd: https://video.twimg.com/...  # 播放器用，不超过 1280 px
     metrics: {bookmarks: 1200, likes: 3400, views: 250000}
   ```

   `kind` 一句话说明：**one-shot** 是一到三句话；**brief** 是一段话或一个简短的创作方向清单；**template** 带占位符或会先问你要素材；**spec** 是有章节的长篇规格说明；**pipeline** 串联了多个工具或多轮提示词。

3. 运行构建并提交它改动的所有文件：

   ```bash
   uv run scripts/build.py
   ```

   构建会检查必填字段、重复的 id 和链接、`kind`/`tools`/`inputs` 取值、缺失的译文，以及聚合站链接。CI 用 `--check` 跑同样的检查。

4. 提 Pull Request。一个 PR 放一条提示词最方便审核。

不想改 YAML？直接[提 issue](https://github.com/Li-Evan/awesome-opus-5.5-video-prompts/issues/new/choose)，贴上作者原帖链接，维护者来添加。

## 同一条提示词，不同的视频

有人用已收录的提示词重新跑了一版，不要新建条目，把他的帖子加到已有条目的 `remakes` 里：

```yaml
remakes:
  - author: someone
    url: https://x.com/someone/status/...
    thumb: https://pbs.twimg.com/...
    video: https://video.twimg.com/...
```

## 写作风格

- 标题和简介说清楚视频是什么，不吹。不用 insane、mind-blowing、「炸裂」「震撼」。
- 数字和原文保持一致。
- 中文用全角标点，中文与英文、数字之间加空格（「用 Three.js 做的 3D 场景」）。

## 更新或移除

预览播不了、原帖删了、译文有误，都可以提 issue 或 PR。每周有一个定时任务检查所有封面和预览，坏掉的会自动开 issue。

作者如果希望撤下提示词或调整署名，请用[作者申请表](https://github.com/Li-Evan/awesome-opus-5.5-video-prompts/issues/new?template=creator-request.yml)，这类请求优先处理。
